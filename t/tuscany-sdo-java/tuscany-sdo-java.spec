Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires: rpm-build-java
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
# %%version is ahead of its definition. Predefining for rpm 4.0 compatibility.
%define version 1.1.1
%global namedreltag %{nil}
%global namedversion %{version}%{?namedreltag}
%global api_version 2.1
%global api_name tuscany-sdo-api-r%{api_version}

Name:          tuscany-sdo-java
Version:       1.1.1
Release:       alt2_17jpp8
Summary:       Service Data Objects 2.1 Java API spec
License:       ASL 2.0
Url:           http://tuscany.apache.org/sdo-java.html
Source0:       ftp://ftp.gbnet.net/pub/apache/dist/tuscany/java/sdo/%{version}/apache-tuscany-sdo-%{version}-src.tar.gz

BuildRequires: mvn(junit:junit)
BuildRequires: maven-local
BuildRequires: maven-assembly-plugin
BuildRequires: maven-plugin-bundle
# required by plugin-bundle
BuildRequires: mvn(org.apache.maven.shared:maven-shared-components:pom:)

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
Group: Development/Java
Summary:       Javadoc for %{name}
BuildArch: noarch

%description javadoc
This package contains the API documentation for %{name}.

%prep
%setup -q -n tuscany-sdo-%{version}-src

%pom_disable_module lib
%pom_disable_module impl
%pom_disable_module tools
%pom_disable_module plugin
%pom_disable_module sample
%pom_disable_module distribution
%pom_disable_module java5tools

%pom_remove_plugin :maven-javadoc-plugin
%pom_remove_plugin :maven-javadoc-plugin sdo-api

sed -i 's|<artifactId>tuscany-sdo-api-r${specVersion}</artifactId>|<artifactId>%{api_name}</artifactId>|' $( find . -iname "pom.xml")

sed -i 's|pom.name|project.name|' sdo-api/pom.xml
sed -i 's|pom.description|project.description|' sdo-api/pom.xml
sed -i 's|pom.organization.name|project.organization.name|' sdo-api/pom.xml
%pom_xpath_set "pom:project/pom:dependencies/pom:dependency[pom:artifactId='tuscany-sdo-api-r2.1']/pom:version" '
${project.version}'

sed -i 's/\r//' LICENSE NOTICE README RELEASE_NOTES

# RHBZ #842622
sed -i 's#<source>1.4</source>#<source>1.5</source>#' pom.xml sdo-api/pom.xml
sed -i 's#<target>1.4</target>#<target>1.5</target>#' pom.xml sdo-api/pom.xml

%mvn_file :%{api_name} %{name}
%mvn_file :%{api_name} tuscany-sdo-api

%build

%mvn_build

%install
%mvn_install

%files -f .mfiles
%doc README RELEASE_NOTES
%doc LICENSE NOTICE

%files javadoc -f .mfiles-javadoc
%doc LICENSE NOTICE

%changelog
* Thu Nov 09 2017 Igor Vlasenko <viy@altlinux.ru> 1.1.1-alt2_17jpp8
- fc27 update

* Sun Oct 22 2017 Igor Vlasenko <viy@altlinux.ru> 1.1.1-alt2_16jpp8
- new jpp release

* Fri Dec 16 2016 Igor Vlasenko <viy@altlinux.ru> 1.1.1-alt2_15jpp8
- new fc release

* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 1.1.1-alt2_14jpp8
- new fc release

* Sat Feb 06 2016 Igor Vlasenko <viy@altlinux.ru> 1.1.1-alt2_12jpp8
- java 8 mass update

* Mon Sep 08 2014 Igor Vlasenko <viy@altlinux.ru> 1.1.1-alt2_8jpp7
- new release

* Mon Aug 04 2014 Igor Vlasenko <viy@altlinux.ru> 1.1.1-alt2_6jpp7
- new release

* Mon Jul 14 2014 Igor Vlasenko <viy@altlinux.ru> 1.1.1-alt2_3jpp7
- NMU rebuild to move poms and fragments

* Sun Sep 09 2012 Igor Vlasenko <viy@altlinux.ru> 1.1.1-alt1_3jpp7
- fc release

