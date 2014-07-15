BuildRequires: /proc
BuildRequires: jpackage-compat
# %name or %version is ahead of its definition. Predefining for rpm 4.0 compatibility.
%define name tuscany-sdo-java
%define version 1.1.1
%global namedreltag %{nil}
%global namedversion %{version}%{?namedreltag}
%global api_version 2.1
%global api_name tuscany-sdo-api-r%{api_version}

Name:          tuscany-sdo-java
Version:       1.1.1
Release:       alt2_3jpp7
Summary:       Service Data Objects 2.1 Java API spec
Group:         Development/Java
License:       ASL 2.0
Url:           http://tuscany.apache.org/sdo-java.html
Source0:       ftp://ftp.gbnet.net/pub/apache/dist/tuscany/java/sdo/%{version}/apache-tuscany-sdo-%{version}-src.tar.gz
# disable some modules
Patch0:        tuscany-sdo-java-%{version}-pom.patch

BuildRequires: jpackage-utils

BuildRequires: junit

BuildRequires: maven
BuildRequires: maven-assembly-plugin
BuildRequires: maven-compiler-plugin
BuildRequires: maven-install-plugin
BuildRequires: maven-jar-plugin
BuildRequires: maven-javadoc-plugin
BuildRequires: maven-plugin-bundle
BuildRequires: maven-resources-plugin
BuildRequires: maven-surefire-plugin
BuildRequires: maven-surefire-provider-junit4

Requires:      jpackage-utils
BuildArch:     noarch
Source44: import.info

%description
SDO is a framework for data application development, which
includes an architecture and API. SDO does the following:

- Simplifies the J2EE data programming model
- Abstracts data in a service oriented architecture (SOA)
- Unifies data application development
- Supports and integrates XML
- Incorporates J2EE patterns and best practices

With SDO, you do not need to be familiar with a
technology-specific API in order to access and utilize data.
You need to know only one API, the SDO API, which lets you
work with data from multiple data sources, including
relational databases, entity EJB components, XML pages, Web
services, the Java Connector Architecture, JavaServer Pages
pages, and more.

This package contains only a Java API of SDO 2.1 spec.
EclipseLink is a implementation of this spec.

%package javadoc
Summary:       Javadocs for %{name}
Group:         Development/Java
Requires:      jpackage-utils
BuildArch: noarch

%description javadoc
This package contains the API documentation for %{name}.

%prep
%setup -q -n tuscany-sdo-%{version}-src
%patch0 -p0

sed -i 's|<artifactId>tuscany-sdo-api-r${specVersion}</artifactId>|<artifactId>%{api_name}</artifactId>|' $( find . -iname "pom.xml")

sed -i 's/\r//' LICENSE NOTICE README RELEASE_NOTES

# RHBZ #842622
sed -i 's#<source>1.4</source>#<source>1.5</source>#' pom.xml sdo-api/pom.xml
sed -i 's#<target>1.4</target>#<target>1.5</target>#' pom.xml sdo-api/pom.xml

%build

mvn-rpmbuild -Dmaven.test.skip=true \
	-Dproject.build.sourceEncoding=UTF-8 install javadoc:aggregate

%install

mkdir -p %{buildroot}%{_javadir}
install -pm 644 sdo-api/target/%{api_name}-%{namedversion}.jar %{buildroot}%{_javadir}/tuscany-sdo-api.jar

mkdir -p %{buildroot}%{_javadocdir}/%{name}
cp -rp target/site/apidocs/* %{buildroot}%{_javadocdir}/%{name}

mkdir -p %{buildroot}%{_mavenpomdir}
install -pm 644 pom.xml %{buildroot}%{_mavenpomdir}/JPP-tuscany-sdo.pom
install -pm 644 sdo-api/pom.xml %{buildroot}%{_mavenpomdir}/JPP-tuscany-sdo-api.pom

%add_maven_depmap JPP-tuscany-sdo.pom
%add_maven_depmap JPP-tuscany-sdo-api.pom tuscany-sdo-api.jar

%files
%{_javadir}/tuscany-sdo-api.jar
%{_mavenpomdir}/JPP-*.pom
%{_mavendepmapfragdir}/%{name}
%doc LICENSE NOTICE README RELEASE_NOTES

%files javadoc
%{_javadocdir}/%{name}
%doc LICENSE NOTICE

%changelog
* Mon Jul 14 2014 Igor Vlasenko <viy@altlinux.ru> 1.1.1-alt2_3jpp7
- NMU rebuild to move poms and fragments

* Sun Sep 09 2012 Igor Vlasenko <viy@altlinux.ru> 1.1.1-alt1_3jpp7
- fc release

