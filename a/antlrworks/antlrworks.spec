# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-java
BuildRequires: /usr/bin/desktop-file-install /usr/bin/desktop-file-validate
# END SourceDeps(oneline)
%filter_from_requires /^java-headless/d
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
Name:           antlrworks
Version:        1.5.2
Release:        alt1_4jpp8
Summary:        Grammar development environment for ANTLR v3 grammars

Group:          Development/Java
License:        BSD
URL:            http://www.antlr3.org/works
Source0:        https://github.com/antlr/%{name}/archive/%{version}/%{name}-%{version}.tar.gz
Source1:        %{name}.desktop
# Disable embedding of dependency jars files into antlrworks jar file
Patch0:         %{name}-1.5.2-build.patch
# Fix compilation with JGoodies Forms >= 1.7.1
Patch1:         %{name}-1.5.2-jgoodies-forms_1.7.1.patch
# Add xdg-open to the list of available browsers to open the help
Patch2:         %{name}-1.5.2-browsers.patch

BuildRequires:  ant
BuildRequires:  antlr3-tool >= 3.5
BuildRequires:  desktop-file-utils
BuildRequires:  jgoodies-forms >= 1.7.1
BuildRequires:  stringtemplate
BuildRequires:  stringtemplate4
Requires:       antlr3-tool >= 3.5
Requires: graphviz libgraphviz
# Owns /usr/share/icons/hicolor
Requires:       icon-theme-hicolor
# Antlrworks requires javac
Requires:       jgoodies-forms >= 1.7.1
Requires:       stringtemplate4
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
%patch0 -p0 -b .build
%patch1 -p0 -b .jgoodies-forms_1.7.1
%patch2 -p0 -b .browsers

# Fix version
sed -i "s|^version=.*|version=%{version}|" build.properties

# Add JARs to the default classpath folder
mkdir -p lib/
build-jar-repository -s -p lib/ antlr3-runtime jgoodies-forms stringtemplate stringtemplate4/ST4 


%build
ant build -Daw.lib=lib/ -Dantlr3.jar=antlr3-runtime.jar -Djgoodies.jar=jgoodies-forms.jar


%install
install -Dpm 0644 dist/%{name}-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}.jar

%jpackage_script org.antlr.works.IDE "-Xmx400m" "" antlrworks:antlr:antlr3:antlr3-runtime:jgoodies-common:jgoodies-forms:stringtemplate:stringtemplate4 %{name} true

desktop-file-install \
  --dir=$RPM_BUILD_ROOT%{_datadir}/applications \
  %{SOURCE1}

install -Dpm 0644 resources/icons/app.png $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/128x128/apps/%{name}.png
for i in 16 32 64; do
  install -Dpm 0644 resources/icons/app_${i}x$i.png $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/${i}x$i/apps/%{name}.png
done

mkdir -p $RPM_BUILD_ROOT`dirname /etc/java/%name.conf`
touch $RPM_BUILD_ROOT/etc/java/%name.conf


%check
desktop-file-validate $RPM_BUILD_ROOT%{_datadir}/applications/%{name}.desktop


%files
%doc History.txt
%{_bindir}/%{name}
%{_datadir}/applications/*.desktop
%{_datadir}/icons/hicolor/*/apps/*.png
%{_javadir}/*.jar
%config(noreplace,missingok) /etc/java/%name.conf


%changelog
* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 1.5.2-alt1_4jpp8
- new fc release

* Sun Feb 07 2016 Igor Vlasenko <viy@altlinux.ru> 1.5.2-alt1_3jpp8
- java8 mass update

* Sat Feb 09 2013 Igor Vlasenko <viy@altlinux.ru> 1.4.3-alt1_8jpp7
- jgoodies fix

* Mon Sep 17 2012 Igor Vlasenko <viy@altlinux.ru> 1.4.3-alt1_6jpp7
- new version

