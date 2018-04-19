Epoch: 1
Group: Development/Other
# BEGIN SourceDeps(oneline):
BuildRequires: rpm-build-java
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Name:          opensaml-java
Version:       3.1.1
Release:       alt1_4jpp8
Summary:       Java OpenSAML library

# Only these files are without license headers:
# ./opensaml-core/src/main/resources/schema/datatypes.dtd
# ./opensaml-core/src/main/resources/schema/XMLSchema.dtd
# ./opensaml-saml-impl/src/test/resources/data/org/opensaml/saml/metadata/resolver/filter/impl/script8.js
# ./opensaml-saml-impl/src/test/resources/data/org/opensaml/saml/metadata/resolver/filter/impl/script.js
# ./opensaml-xmlsec-impl/src/test/java/org/opensaml/xmlsec/impl/BasicWhitelistBlacklistConfigurationTest.java
# Not available LICENSE file in source directory structure. Sent a mail @ users@shibboleth.net
License:       ASL 2.0
URL:           http://shibboleth.net/products/opensaml-java.html
# svn export https://svn.shibboleth.net/java-opensaml/tags/3.1.1 opensaml-java-3.1.1
# find ./opensaml-java-3.1.1 -name "*.class" -print -delete
# find ./opensaml-java-3.1.1 -name "*.jar" -print -delete
# tar cJf opensaml-java-3.1.1.tar.xz opensaml-java-3.1.1
Source0:       %{name}-%{version}.tar.xz

BuildRequires: maven-local
BuildRequires: mvn(commons-codec:commons-codec)
BuildRequires: mvn(javax.json:javax.json-api)
BuildRequires: mvn(javax.servlet:javax.servlet-api)
BuildRequires: mvn(joda-time:joda-time)
BuildRequires: mvn(net.shibboleth:parent-v3:pom:)
BuildRequires: mvn(net.shibboleth.utilities:java-support)
BuildRequires: mvn(net.spy:spymemcached)
BuildRequires: mvn(org.apache.httpcomponents:httpclient)
BuildRequires: mvn(org.apache.santuario:xmlsec)
BuildRequires: mvn(org.apache.velocity:velocity)
BuildRequires: mvn(org.cryptacular:cryptacular)
BuildRequires: mvn(org.bouncycastle:bcprov-jdk15on)
BuildRequires: mvn(org.glassfish:javax.json)
BuildRequires: mvn(org.hibernate:hibernate-entitymanager)
BuildRequires: mvn(org.hibernate.javax.persistence:hibernate-jpa-2.1-api)
BuildRequires: mvn(org.ldaptive:ldaptive)
BuildRequires: mvn(org.springframework:spring-orm)

# test deps
%if 0
# BuildRequires: mvn(com.unboundid:unboundid-ldapsdk)
BuildRequires: mvn(commons-dbcp:commons-dbcp)
BuildRequires: mvn(mysql:mysql-connector-java)
BuildRequires: mvn(net.shibboleth.utilities:java-support:tests:)
# BuildRequires: mvn(net.shibboleth.ext:spring-extensions)
BuildRequires: mvn(org.hsqldb:hsqldb)
# https://bugzilla.redhat.com/show_bug.cgi?id=1217395
BuildRequires: mvn(org.postgresql:postgresql)
BuildRequires: mvn(org.springframework:spring-context)
BuildRequires: mvn(org.springframework:spring-core)
BuildRequires: mvn(org.springframework:spring-test)
%endif

BuildArch:     noarch
Source44: import.info

%description
OpenSAML is a set of open source C++ & Java libraries meant to support
developers working with the Security Assertion Markup Language (SAML).
OpenSAML 2, the current version, supports SAML 1.0, 1.1, and 2.0. 

%package core
Group: Development/Other
Summary:       OpenSAML-Java :: Core

%description core
OpenSAML-Java :: Core.

%package messaging-api
Group: Development/Other
Summary:       OpenSAML-Java :: Messaging API

%description messaging-api
OpenSAML-Java :: Messaging API.

%package messaging-impl
Group: Development/Other
Summary:       OpenSAML-Java :: Messaging Implementations

%description messaging-impl
OpenSAML-Java :: Messaging Implementations.

%package parent
Group: Development/Other
Summary:       OpenSAML Parent POM

%description parent
OpenSAML Parent POM.

%package profile-api
Group: Development/Other
Summary:       OpenSAML-Java :: Profile API

%description profile-api
OpenSAML-Java :: Profile API.

%package profile-impl
Group: Development/Other
Summary:       OpenSAML-Java :: Profile Implementations

%description profile-impl
OpenSAML-Java :: Profile Implementations.

%package saml-api
Group: Development/Other
Summary:       OpenSAML-Java :: SAML Provider API

%description saml-api
OpenSAML-Java :: SAML Provider API.

%package saml-impl
Group: Development/Other
Summary:       OpenSAML-Java :: SAML Provider Implementations

%description saml-impl
OpenSAML-Java :: SAML Provider Implementations.

%package security-api
Group: Development/Other
Summary:       OpenSAML-Java :: Security API

%description security-api
OpenSAML-Java :: Security API.

%package security-impl
Group: Development/Other
Summary:       OpenSAML-Java :: Security Implementation

%description security-impl
OpenSAML-Java :: Security Implementation.

%package soap-api
Group: Development/Other
Summary:       OpenSAML-Java :: SOAP Provider API

%description soap-api
OpenSAML-Java :: SOAP Provider API.

%package soap-impl
Group: Development/Other
Summary:       OpenSAML-Java :: SOAP Provider Implementations

%description soap-impl
OpenSAML-Java :: SOAP Provider Implementations.

%package storage-api
Group: Development/Other
Summary:       OpenSAML-Java :: Storage API

%description storage-api
OpenSAML-Java :: Storage API.

%package storage-impl
Group: Development/Other
Summary:       OpenSAML-Java :: Storage Implementation

%description storage-impl
OpenSAML-Java :: Storage Implementation.

%package xacml-api
Group: Development/Other
Summary:       OpenSAML-Java :: XACML Provider API

%description xacml-api
OpenSAML-Java :: XACML Provider API.

%package xacml-impl
Group: Development/Other
Summary:       OpenSAML-Java :: XACML Provider Implementations

%description xacml-impl
OpenSAML-Java :: XACML Provider Implementations.

%package xacml-saml-api
Group: Development/Other
Summary:       OpenSAML-Java :: SAML XACML Profile API

%description xacml-saml-api
OpenSAML-Java :: SAML XACML Profile API.

%package xacml-saml-impl
Group: Development/Other
Summary:       OpenSAML-Java :: SAML XACML Profile Implementation

%description xacml-saml-impl
OpenSAML-Java :: SAML XACML Profile Implementation.

%package xmlsec-api
Group: Development/Other
Summary:       OpenSAML-Java :: XML Security API

%description xmlsec-api
OpenSAML-Java :: XML Security API.

%package xmlsec-impl
Group: Development/Other
Summary:       OpenSAML-Java :: XML Security Implementation

%description xmlsec-impl
OpenSAML-Java :: XML Security Implementation.

%package javadoc
Group: Development/Java
Summary:       Javadoc for %{name}
BuildArch: noarch

%description javadoc
This package contains javadoc for %{name}.

%prep
%setup -q -n %{name}-%{version}

# This is a dummy POM added just to ease building in the RPM platforms
cat > pom.xml << EOF
<?xml version="1.0" encoding="UTF-8"?>
<project
  xmlns="http://maven.apache.org/POM/4.0.0"
  xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 http://maven.apache.org/maven-v4_0_0.xsd"
  xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
  <modelVersion>4.0.0</modelVersion>
  <groupId>org.opensaml</groupId>
  <artifactId>opensaml-project</artifactId>
  <packaging>pom</packaging>
  <version>%{version}</version>
  <modules>
    <module>opensaml-parent</module>
  </modules>
</project>
EOF

%mvn_package :opensaml-project __noinstall

%build
# Test skipped for unavailable test deps: net.shibboleth.ext:spring-extensions
%mvn_build -sf

%install
%mvn_install

%files core -f .mfiles-opensaml-core
%files messaging-api -f .mfiles-opensaml-messaging-api
%files messaging-impl -f .mfiles-opensaml-messaging-impl
%files parent -f .mfiles-opensaml-parent
%files profile-api -f .mfiles-opensaml-profile-api
%files profile-impl -f .mfiles-opensaml-profile-impl
%files saml-api -f .mfiles-opensaml-saml-api
%files saml-impl -f .mfiles-opensaml-saml-impl
%files security-api -f .mfiles-opensaml-security-api
%files security-impl -f .mfiles-opensaml-security-impl
%files soap-api -f .mfiles-opensaml-soap-api
%files soap-impl -f .mfiles-opensaml-soap-impl
%files storage-api -f .mfiles-opensaml-storage-api
%files storage-impl -f .mfiles-opensaml-storage-impl
%files xacml-api -f .mfiles-opensaml-xacml-api
%files xacml-impl -f .mfiles-opensaml-xacml-impl
%files xacml-saml-api -f .mfiles-opensaml-xacml-saml-api
%files xacml-saml-impl -f .mfiles-opensaml-xacml-saml-impl
%files xmlsec-api -f .mfiles-opensaml-xmlsec-api
%files xmlsec-impl -f .mfiles-opensaml-xmlsec-impl

%files javadoc -f .mfiles-javadoc

%changelog
* Mon Apr 16 2018 Igor Vlasenko <viy@altlinux.ru> 1:3.1.1-alt1_4jpp8
- java update

* Thu Nov 09 2017 Igor Vlasenko <viy@altlinux.ru> 1:3.1.1-alt1_3jpp8
- fc27 update

* Fri Nov 03 2017 Igor Vlasenko <viy@altlinux.ru> 1:3.1.1-alt1_2jpp8
- new version

* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 2.5.3-alt2_10jpp8
- new fc release

* Sun Feb 07 2016 Igor Vlasenko <viy@altlinux.ru> 2.5.3-alt2_9jpp8
- java 8 mass update

* Mon Sep 08 2014 Igor Vlasenko <viy@altlinux.ru> 2.5.3-alt2_6jpp7
- new release

* Fri Aug 22 2014 Igor Vlasenko <viy@altlinux.ru> 2.5.3-alt2_4jpp7
- added BR: for xmvn

* Mon Jul 28 2014 Igor Vlasenko <viy@altlinux.ru> 2.5.3-alt1_4jpp7
- new release

* Tue Feb 26 2013 Igor Vlasenko <viy@altlinux.ru> 2.5.3-alt1_2jpp7
- fc update

