# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-java
BuildRequires: unzip
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-compat
Name:          maven-shared-resources
Version:       1
Release:       alt1_1jpp7
Summary:       A collection of templates that are specific to the Maven project
Group:         Development/Java
License:       ASL 2.0
URL:           http://maven.apache.org/shared/maven-shared-resources/
Source0:       http://repo1.maven.org/maven2/org/apache/maven/shared/%{name}/%{version}/%{name}-%{version}-source-release.zip
#Source1:       ...
#Patch0:        ...
BuildRequires: jpackage-utils

BuildRequires: maven-local
BuildRequires: maven-compiler-plugin
BuildRequires: maven-jar-plugin
BuildRequires: maven-remote-resources-plugin
BuildRequires: maven-resources-plugin
BuildRequires: maven-surefire-plugin

# use old maven-shared for bootstrap the new maven-shared-components package
BuildRequires: mvn(org.apache.maven.shared:maven-shared-components)
#Requires:      mvn(org.apache.maven.shared:maven-shared-components)

Requires:      jpackage-utils
BuildArch:     noarch
Source44: import.info

%description
This is a collection of templates that are specific to the Maven project.
They are probably not of interest to projects other than Apache Maven.

%prep
%setup -q

%build

mvn-rpmbuild package

%install
mkdir -p %{buildroot}%{_javadir}/%{name}
install -m 644 target/%{name}-%{version}.jar %{buildroot}%{_javadir}/%{name}.jar

mkdir -p %{buildroot}%{_mavenpomdir}
install -pm 644 pom.xml %{buildroot}%{_mavenpomdir}/JPP-%{name}.pom
%add_maven_depmap

%files
%{_javadir}/%{name}.jar
%{_mavenpomdir}/JPP-%{name}.pom
%{_mavendepmapfragdir}/%{name}
%doc LICENSE NOTICE

%changelog
* Mon Aug 25 2014 Igor Vlasenko <viy@altlinux.ru> 1-alt1_1jpp7
- update

* Sun Aug 24 2014 Igor Vlasenko <viy@altlinux.ru> 1-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

