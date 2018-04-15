# BEGIN SourceDeps(oneline):
BuildRequires: /usr/bin/desktop-file-install /usr/bin/desktop-file-validate rpm-build-java
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Name:           antlrworks
Version:        1.5.2
Release:        alt1_9jpp8
Summary:        Grammar development environment for ANTLR v3 grammars

Group:          Development/Java
License:        BSD
URL:            http://www.antlr3.org/works
Source0:        https://github.com/antlr/%{name}/archive/%{version}/%{name}-%{version}.tar.gz
Source1:        %{name}.desktop
Source2:        %{name}.appdata.xml
# Fix compilation with JGoodies Forms >= 1.7.1
Patch0:         %{name}-1.5.2-jgoodies-forms_1.7.1.patch
# Add xdg-open to the list of available browsers to open the help
Patch1:         %{name}-1.5.2-browsers.patch

BuildRequires:  desktop-file-utils
BuildRequires:  libappstream-glib
BuildRequires:  maven-local
BuildRequires:  mvn(com.jgoodies:jgoodies-forms)
BuildRequires:  mvn(org.antlr:antlr)
BuildRequires:  mvn(org.antlr:antlr-runtime)
BuildRequires:  mvn(org.antlr:stringtemplate)
BuildRequires:  mvn(org.sonatype.oss:oss-parent:pom:)
Requires:       graphviz libgraphviz
# Owns /usr/share/icons/hicolor
Requires:       icon-theme-hicolor
# Antlrworks requires javac
BuildArch:      noarch
Source44: import.info

%description
ANTLRWorks is a novel grammar development environment for ANTLR v3 grammars
written by Jean Bovet (with suggested use cases from Terence Parr). It combines
an excellent grammar-aware editor with an interpreter for rapid prototyping and
a language-agnostic debugger for isolating grammar errors. ANTLRWorks helps
eliminate grammar nondeterminisms, one of the most difficult problems for
beginners and experts alike, by highlighting nondeterministic paths in the
syntax diagram associated with a grammar. ANTLRWorks' goal is to make grammars
more accessible to the average programmer, improve maintainability and
readability of grammars by providing excellent grammar navigation and
refactoring tools, and address the most common questions and problems
encountered by grammar developers.


%prep
%setup -q
%patch0 -p0
%patch1 -p0

# Remove MacOSX-specific code
rm -r src/org/antlr/xjlib/appkit/app/MacOS/

%pom_remove_dep com.apple:AppleJavaExtensions
%pom_change_dep com.jgoodies:forms com.jgoodies:jgoodies-forms


%build
%mvn_build -j


%install
%mvn_install

%jpackage_script org.antlr.works.IDE "-Xmx400m" "" antlrworks:antlr:antlr3:antlr3-runtime:jgoodies-common:jgoodies-forms:stringtemplate:stringtemplate4 %{name} false

desktop-file-install \
  --dir=$RPM_BUILD_ROOT%{_datadir}/applications \
  %{SOURCE1}

install -Dpm 0644 resources/icons/app.png $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/128x128/apps/%{name}.png
for i in 16 32 64; do
  install -Dpm 0644 resources/icons/app_${i}x$i.png $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/${i}x$i/apps/%{name}.png
done

install -Dpm 0644 %{SOURCE2} $RPM_BUILD_ROOT/%{_datadir}/appdata/%{name}.appdata.xml

mkdir -p $RPM_BUILD_ROOT`dirname /etc/java/%name.conf`
touch $RPM_BUILD_ROOT/etc/java/%name.conf


%check
desktop-file-validate $RPM_BUILD_ROOT%{_datadir}/applications/%{name}.desktop

appstream-util validate-relax --nonet $RPM_BUILD_ROOT%{_datadir}/appdata/%{name}.appdata.xml


%files -f .mfiles
%doc History.txt
%{_bindir}/%{name}
%{_datadir}/applications/*.desktop
%{_datadir}/icons/hicolor/*/apps/*.*
%{_datadir}/appdata/*.appdata.xml
%config(noreplace,missingok) /etc/java/%name.conf


%changelog
* Sun Apr 15 2018 Igor Vlasenko <viy@altlinux.ru> 1.5.2-alt1_9jpp8
- java update

* Thu Nov 09 2017 Igor Vlasenko <viy@altlinux.ru> 1.5.2-alt1_7jpp8
- fc27 update

* Sun Oct 22 2017 Igor Vlasenko <viy@altlinux.ru> 1.5.2-alt1_6jpp8
- new jpp release

* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 1.5.2-alt1_4jpp8
- new fc release

* Sun Feb 07 2016 Igor Vlasenko <viy@altlinux.ru> 1.5.2-alt1_3jpp8
- java8 mass update

* Sat Feb 09 2013 Igor Vlasenko <viy@altlinux.ru> 1.4.3-alt1_8jpp7
- jgoodies fix

* Mon Sep 17 2012 Igor Vlasenko <viy@altlinux.ru> 1.4.3-alt1_6jpp7
- new version

