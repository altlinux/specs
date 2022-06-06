BuildRequires: javapackages-local
Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-java
BuildRequires: unzip
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-1.8-compat
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Name:           microba
Version:        0.4.4.3
Release:        alt4_15jpp8
Summary:        Set of JFC (Swing) components
License:        BSD
URL:            http://microba.sourceforge.net/
Source0:        http://downloads.sourceforge.net/project/%{name}/%{name}/%{version}/%{name}-%{version}-full.zip
Source1:        https://maven.atlassian.com/content/repositories/atlassian-public/com/michaelbaranov/%{name}/%{version}/%{name}-%{version}.pom
# set javac source/target to 1.5
# don't put the javadoc documentation into a jar file
Patch0:         %{name}-0.4.4.3-build.patch
# temporary build fix
Patch1:         %{name}-0.4.4.3-disable-jgraph.patch

BuildRequires:  ant
BuildRequires:  dos2unix
BuildRequires:  jpackage-utils
# BuildRequires:  jgraph
BuildArch:      noarch
Source44: import.info

%description
Microba features a set of finely crafted and feature rich JFC (Swing)
components. Among them are CalendarPane, DatePicker, DatePickerCellEditor
for JTree and JTable, MarkerBar, and GradientEditor.

%package javadoc
Group: Development/Java
Summary:        Javadoc for %{name}
BuildArch: noarch

%description javadoc
API documentation for %{name}.

%prep
%setup -q -c
unzip -q %{name}-%{version}-sources.jar
find . -name '*.jar' -delete
%patch0 -p0
%patch1 -p0

dos2unix *.txt

# install in _javadir
%mvn_file com.michaelbaranov:%{name} %{name}
%mvn_alias com.michaelbaranov:%{name} "net.sf.%{name}:%{name}"

%build

ant bin_release doc_release

%mvn_artifact %{SOURCE1} redist/%{name}-%{version}.jar

%install
%mvn_install -J javadoc

%files -f .mfiles
%doc readme.txt change.log.txt
%doc license.txt

%files javadoc -f .mfiles-javadoc
%doc license.txt

%changelog
* Mon Jun 06 2022 Igor Vlasenko <viy@altlinux.org> 0.4.4.3-alt4_15jpp8
- migrated to %%mvn_artifact

* Thu Oct 08 2020 Igor Vlasenko <viy@altlinux.ru> 0.4.4.3-alt3_15jpp8
- fixed build with new java

* Sat Nov 18 2017 Igor Vlasenko <viy@altlinux.ru> 0.4.4.3-alt2_15jpp8
- added BR: javapackages-local for javapackages 5

* Tue Oct 17 2017 Igor Vlasenko <viy@altlinux.ru> 0.4.4.3-alt1_15jpp8
- new jpp release

* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 0.4.4.3-alt1_14jpp8
- new fc release

* Tue Feb 02 2016 Igor Vlasenko <viy@altlinux.ru> 0.4.4.3-alt1_13jpp8
- new version

* Mon Sep 08 2014 Igor Vlasenko <viy@altlinux.ru> 0.4.4.3-alt1_10jpp7
- new release

* Mon Jul 28 2014 Igor Vlasenko <viy@altlinux.ru> 0.4.4.3-alt1_9jpp7
- new release

* Mon Sep 17 2012 Igor Vlasenko <viy@altlinux.ru> 0.4.4.3-alt1_5jpp7
- new version

