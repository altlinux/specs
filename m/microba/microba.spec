# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-java
BuildRequires: unzip
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-compat
Name:           microba
Version:        0.4.4.3
Release:        alt1_9jpp7
Summary:        Set of JFC (Swing) components
Group:          Development/Java
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
# sinjdoc doesn't do the job for us in f12, drag in real javadoc
BuildRequires:  java-devel-openjdk
BuildRequires:  jpackage-utils
# BuildRequires:  jgraph
Requires:       jpackage-utils
BuildArch:      noarch
Source44: import.info

%description
Microba features a set of finely crafted and feature rich JFC (Swing)
components. Among them are CalendarPane, DatePicker, DatePickerCellEditor
for JTree and JTable, MarkerBar, and GradientEditor.

%package javadoc
Summary:        Javadoc for %{name}
Group:          Development/Java
Requires:       %{name} = %{version}-%{release}
Requires:       jpackage-utils
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

%build

ant bin_release doc_release

%install

mkdir -p %{buildroot}%{_javadir}
install redist/%{name}-%{version}.jar %{buildroot}%{_javadir}/%{name}.jar

mkdir -p %{buildroot}%{_mavenpomdir}
install -pm 644 %{SOURCE1} %{buildroot}%{_mavenpomdir}/JPP-%{name}.pom
%add_maven_depmap JPP-%{name}.pom %{name}.jar -a "net.sf.%{name}:%{name}"

mkdir -p %{buildroot}%{_javadocdir}
cp -r javadoc %{buildroot}%{_javadocdir}/%{name}

%files
%{_javadir}/%{name}.jar
%{_mavenpomdir}/JPP-%{name}.pom
%{_mavendepmapfragdir}/%{name}
%doc license.txt readme.txt change.log.txt

%pre javadoc
[ $1 -gt 1 ] && [ -L %{_javadocdir}/%{name} ] && \
rm -rf $(readlink -f %{_javadocdir}/%{name}) %{_javadocdir}/%{name} || :

%files javadoc
%{_javadocdir}/%{name}
%doc license.txt

%changelog
* Mon Jul 28 2014 Igor Vlasenko <viy@altlinux.ru> 0.4.4.3-alt1_9jpp7
- new release

* Mon Sep 17 2012 Igor Vlasenko <viy@altlinux.ru> 0.4.4.3-alt1_5jpp7
- new version

