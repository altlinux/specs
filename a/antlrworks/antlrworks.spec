# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-java
BuildRequires: unzip
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-compat
Name:           antlrworks
Version:        1.4.3
Release:        alt1_8jpp7
Summary:        Grammar development environment for ANTLR v3 grammars

Group:          Development/Java
License:        BSD
URL:            http://www.antlr3.org/works
Source0:        http://www.antlr3.org/download/%{name}-%{version}-src.zip
Source1:        antlrworks.desktop
# Disable embedding of dependency jars files into antlrworks jar file
Patch0:         %{name}-1.4-build.patch
# Add xdg-open and epiphany as available web browsers to open help (sent
# upstream)
Patch1:         %{name}-1.4-browsers.patch
# Fix compilation with JGoodies Forms >= 1.4.2
Patch2:         %{name}-1.4-jgoodies-forms_1.4.2.patch
# Fix compilation with OpenJDK 7
Patch3:         %{name}-1.4.3-jdk7.patch
# Fix compilation with JGoodies Forms >= 1.6.0
Patch4:         %{name}-1.4.3-jgoodies-forms_1.6.0.patch

BuildRequires:  ant
BuildRequires:  antlr-tool
BuildRequires:  antlr3-tool >= 3.3
BuildRequires:  desktop-file-utils
BuildRequires:  jgoodies-forms >= 1.6.0
BuildRequires:  stringtemplate
Requires:       antlr-tool
Requires:       antlr3-tool >= 3.3
Requires:       graphviz
# Owns /usr/share/icons/hicolor
Requires:       icon-theme-hicolor
# Antlrworks requires javac
Requires:       jgoodies-forms >= 1.6.0
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
%setup -q -c
%patch0 -p0 -b .build
%patch1 -p1 -b .browsers
%patch2 -p0 -b .jgoodies-forms_1.4.2
%patch3 -p1 -b .jdk7
%patch4 -p0 -b .jgoodies-forms_1.6.0

find -name '*.class' -o -name '*.jar' -exec rm '{}' \;


%build
export CLASSPATH=$(build-classpath antlr antlr3 antlr3-runtime jgoodies-forms stringtemplate stringtemplate4)
ant build


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

desktop-file-validate $RPM_BUILD_ROOT%{_datadir}/applications/%{name}.desktop

mkdir -p $RPM_BUILD_ROOT`dirname /etc/java/antlrworks.conf`
touch $RPM_BUILD_ROOT/etc/java/antlrworks.conf


%files
%{_bindir}/%{name}
%{_datadir}/applications/*.desktop
%{_datadir}/icons/hicolor/*/apps/*.png
%{_javadir}/*.jar
%config(noreplace,missingok) /etc/java/antlrworks.conf


%changelog
* Sat Feb 09 2013 Igor Vlasenko <viy@altlinux.ru> 1.4.3-alt1_8jpp7
- jgoodies fix

* Mon Sep 17 2012 Igor Vlasenko <viy@altlinux.ru> 1.4.3-alt1_6jpp7
- new version

