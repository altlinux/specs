Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-java
# END SourceDeps(oneline)
%filter_from_requires /^java-headless/d
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
# %%name or %%version is ahead of its definition. Predefining for rpm 4.0 compatibility.
%define name arquillian-core
%define version 1.1.11
%global namedreltag .Final
%global namedversion %{version}%{?namedreltag}

Name:          arquillian-core
Version:       1.1.11
Release:       alt1_3jpp8
Summary:       Java Testing Platform for the JVM Member
# No license header report @ https://github.com/arquillian/arquillian-core/issues/101
License:       ASL 2.0
URL:           http://arquillian.org/
Source0:       https://github.com/arquillian/arquillian-core/archive/%{namedversion}.tar.gz

BuildRequires: graphviz libgraphviz
BuildRequires: maven-local
BuildRequires: mvn(javax.annotation:jsr250-api)
BuildRequires: mvn(javax.el:el-api)
BuildRequires: mvn(javax.enterprise:cdi-api)
BuildRequires: mvn(javax.inject:javax.inject)
BuildRequires: mvn(jdepend:jdepend)
BuildRequires: mvn(junit:junit)
BuildRequires: mvn(org.jboss:jboss-parent:pom:)
BuildRequires: mvn(org.jboss.apiviz:apiviz)
BuildRequires: mvn(org.jboss.shrinkwrap:shrinkwrap-api)
BuildRequires: mvn(org.jboss.shrinkwrap:shrinkwrap-bom:pom:)
BuildRequires: mvn(org.jboss.shrinkwrap:shrinkwrap-impl-base)
BuildRequires: mvn(org.jboss.shrinkwrap.descriptors:shrinkwrap-descriptors-api-base)
BuildRequires: mvn(org.jboss.shrinkwrap.descriptors:shrinkwrap-descriptors-api-javaee)
BuildRequires: mvn(org.jboss.shrinkwrap.descriptors:shrinkwrap-descriptors-bom:pom:)
BuildRequires: mvn(org.jboss.shrinkwrap.descriptors:shrinkwrap-descriptors-impl-javaee)
BuildRequires: mvn(org.jboss.shrinkwrap.descriptors:shrinkwrap-descriptors-spi)
BuildRequires: mvn(org.jboss.shrinkwrap.resolver:shrinkwrap-resolver-bom:pom:)
BuildRequires: mvn(org.jboss.spec.javax.ejb:jboss-ejb-api_3.1_spec)
BuildRequires: mvn(org.jboss.spec.javax.servlet:jboss-servlet-api_3.0_spec)
BuildRequires: mvn(org.jboss.weld:weld-core)
BuildRequires: mvn(org.apache.maven.plugins:maven-enforcer-plugin)
BuildRequires: mvn(org.codehaus.mojo:buildnumber-maven-plugin)
BuildRequires: mvn(org.eclipse.jetty:jetty-server:8.1)
BuildRequires: mvn(org.eclipse.jetty:jetty-servlet:8.1)
BuildRequires: mvn(org.mockito:mockito-all)
BuildRequires: mvn(org.slf4j:slf4j-simple)
BuildRequires: mvn(org.testng:testng)

BuildArch:     noarch
Source44: import.info

%description
Arquillian is a revolutionary testing platform built on the JVM that
substantially reduces the effort required to write and execute Java
middle-ware integration and functional tests. No more mocks.
No more container life-cycle and deployment hassles. Just real tests!

%package api
Group: Development/Java
Summary:       Arquillian Core API

%description api
API for the Core.

%package impl-base
Group: Development/Java
Summary:       Arquillian Core Implementation Base

%description impl-base
Implementation Base for the Core.

%package parent
Group: Development/Java
Summary:       Arquillian Core Aggregator

%description parent
Arquillian Core Aggregator POM.

%package spi
Group: Development/Java
Summary:       Arquillian Core SPI

%description spi
Service Provider Interface for the Core.

%package -n arquillian-bom
Group: Development/Java
Summary:       Arquillian BOM

%description -n arquillian-bom
Arquillian Bill Of Material.

%package -n arquillian-build
Group: Development/Java
Summary:       Arquillian Build

%description -n arquillian-build
Arquillian Build Configuration POM.

%package -n arquillian-config-api
Group: Development/Java
Summary:       Arquillian Config API

%description -n arquillian-config-api
API for the Config Module.

%package -n arquillian-config-impl-base
Group: Development/Java
Summary:       Arquillian Config Implementation Base
License:       ASL 2.0 and LGPLv2+
# Unknown jboss-common-core version
# LGPLv2:
# ./config/impl-base/src/main/java/org/jboss/arquillian/config/impl/extension/StringPropertyReplacer.java (Revision: 2898)
# ./config/impl-base/src/main/java/org/jboss/arquillian/config/impl/extension/SysPropertyActions.java (Revision: 2787)
Provides:      bundled(jboss-common-core)

%description -n arquillian-config-impl-base
Implementation for the Config module.

%package -n arquillian-config-parent
Group: Development/Java
Summary:       Arquillian Config Aggregator

%description -n arquillian-config-parent
Arquillian Config Aggregator POM.

%package -n arquillian-config-spi
Group: Development/Java
Summary:       Arquillian Config SPI

%description -n arquillian-config-spi
Service Provider Interface for the Config Module.

%package -n arquillian-container-impl-base
Group: Development/Java
Summary:       Arquillian Container Implementation Base
# LGPLv2: ./container/impl-base/src/main/java/org/jboss/arquillian/container/impl/DefaultServerKillProcessor.java
License:       ASL 2.0 and LGPLv2+

%description -n arquillian-container-impl-base
Implementation for the container extension.

%package -n arquillian-container-parent
Group: Development/Java
Summary:       Arquillian Container Aggregator

%description -n arquillian-container-parent
Arquillian Container Aggregator POM.

%package -n arquillian-container-spi
Group: Development/Java
Summary:       Arquillian Container SPI
# LGPLv2:
# ./container/spi/src/main/java/org/jboss/arquillian/container/spi/ServerKillProcessor.java
# ./container/spi/src/main/java/org/jboss/arquillian/container/spi/event/StartClassContainers.java
# ./container/spi/src/main/java/org/jboss/arquillian/container/spi/event/StopClassContainers.java
License:       ASL 2.0 and LGPLv2+

%description -n arquillian-container-spi
Service Provider Interface for the container extension.

%package -n arquillian-container-test-api
Group: Development/Java
Summary:       Arquillian Container Test API
# LGPLv2:
# ./container/test-api/src/main/java/org/jboss/arquillian/container/test/api/Config.java
# ./container/test-api/src/main/java/org/jboss/arquillian/container/test/api/ContainerController.java
License:       ASL 2.0 and LGPLv2+

%description -n arquillian-container-test-api
Integration with the Test extension for the container extension.

%package -n arquillian-container-test-impl-base
Group: Development/Java
Summary:       Arquillian Container Test Implementation Base

%description -n arquillian-container-test-impl-base
Integration with the Test extension for the container extension.

%package -n arquillian-container-test-spi
Group: Development/Java
Summary:       Arquillian Container Test SPI

%description -n arquillian-container-test-spi
Integration with the Test extension for the container extension.

%package -n arquillian-junit-container
Group: Development/Java
Summary:       Arquillian TestRunner JUnit Container

%description -n arquillian-junit-container
JUnit Container Implementation for the Arquillian Project.

%package -n arquillian-junit-core
Group: Development/Java
Summary:       Arquillian TestRunner JUnit Core

%description -n arquillian-junit-core
JUnit Implementation for the Arquillian Project.

%package -n arquillian-junit-parent
Group: Development/Java
Summary:       Arquillian TestRunner JUnit Aggregator

%description -n arquillian-junit-parent
Arquillian JUnit Aggregator POM.

%package -n arquillian-junit-standalone
Group: Development/Java
Summary:       Arquillian TestRunner JUnit Standalone

%description -n arquillian-junit-standalone
JUnit Standalone Implementation for the Arquillian Project.

%package -n arquillian-parent
Group: Development/Java
Summary:       Arquillian Aggregator

%description -n arquillian-parent
Arquillian Aggregator POM.

%package -n arquillian-protocol-jmx
Group: Development/Java
Summary:       Arquillian Protocol JMX

%description -n arquillian-protocol-jmx
Protocol handler for communicating via JMX.

%package -n arquillian-protocol-parent
Group: Development/Java
Summary:       Arquillian Protocol Aggregator

%description -n arquillian-protocol-parent
Arquillian Protocol Aggregator POM.

%package -n arquillian-protocol-servlet
Group: Development/Java
Summary:       Arquillian Protocol Servlet 2.5/3.x
# LGPLv2:
# ./protocols/servlet/src/main/java/org/jboss/arquillian/protocol/servlet/arq514hack/descriptors/api/application/WebModule.java
# ./protocols/servlet/src/main/java/org/jboss/arquillian/protocol/servlet/arq514hack/descriptors/api/web/ServletDef.java
# ./protocols/servlet/src/main/java/org/jboss/arquillian/protocol/servlet/arq514hack/descriptors/impl/application/WebModuleImpl.java
# ./protocols/servlet/src/main/java/org/jboss/arquillian/protocol/servlet/arq514hack/descriptors/impl/web/ServletDefImpl.java
# ./protocols/servlet/src/main/java/org/jboss/arquillian/protocol/servlet/arq514hack/descriptors/impl/web/ServletMappingDefImpl.java
# ./protocols/servlet/src/main/java/org/jboss/arquillian/protocol/servlet/arq514hack/descriptors/impl/web/Strings.java
License:       ASL 2.0 and LGPLv2+

%description -n arquillian-protocol-servlet
Protocol handler for communicating using a Servlet / HTTP following the
Servlet 2.5/ 2.5/.x spec.

%package -n arquillian-test-api
Group: Development/Java
Summary:       Arquillian Test API

%description -n arquillian-test-api
API for the Test integration.

%package -n arquillian-test-impl-base
Group: Development/Java
Summary:       Arquillian Test Implementation Base

%description -n arquillian-test-impl-base
Implementation Base for the Test integration.

%package -n arquillian-test-parent
Group: Development/Java
Summary:       Arquillian Test Aggregator

%description -n arquillian-test-parent
Arquillian Test Aggregator POM.

%package -n arquillian-test-spi
Group: Development/Java
Summary:       Arquillian Test SPI

%description -n arquillian-test-spi
Service Provider Interface for the Test integration.

%package -n arquillian-testenricher-cdi
Group: Development/Java
Summary:       Arquillian TestEnricher CDI

%description -n arquillian-testenricher-cdi
CDI TestEnricher for the Arquillian Project.

%package -n arquillian-testenricher-ejb
Group: Development/Java
Summary:       Arquillian TestEnricher EJB

%description -n arquillian-testenricher-ejb
EJB TestEnricher for the Arquillian Project.

%package -n arquillian-testenricher-initialcontext
Group: Development/Java
Summary:       Arquillian TestEnricher InitialContext

%description -n arquillian-testenricher-initialcontext
InitialContext TestEnricher for the Arquillian Project.

%package -n arquillian-testenricher-parent
Group: Development/Java
Summary:       Arquillian TestEnricher Aggregator

%description -n arquillian-testenricher-parent
Arquillian TestEnricher Aggregator POM.

%package -n arquillian-testenricher-resource
Group: Development/Java
Summary:       Arquillian TestEnricher Resource

%description -n arquillian-testenricher-resource
Resource TestEnricher for the Arquillian Project.

%package -n arquillian-testng-container
Group: Development/Java
Summary:       Arquillian TestRunner TestNG Container

%description -n arquillian-testng-container
TestNG Container Implementation for the Arquillian Project.

%package -n arquillian-testng-core
Group: Development/Java
Summary:       Arquillian TestRunner TestNG Core

%description -n arquillian-testng-core
TestNG Implementations for the Arquillian Project.

%package -n arquillian-testng-parent
Group: Development/Java
Summary:       Arquillian TestRunner TestNG Aggregator

%description -n arquillian-testng-parent
Arquillian TestNG Aggregator POM.

%package -n arquillian-testng-standalone
Group: Development/Java
Summary:       Arquillian TestRunner TestNG Standalone

%description -n arquillian-testng-standalone
TestNG Standalone Implementation for the Arquillian Project.

%package javadoc
Group: Development/Java
Summary:       Javadoc for %{name}
BuildArch: noarch

%description javadoc
This package contains javadoc for %{name}.

%prep
%setup -q -n %{name}-%{namedversion}

%pom_remove_plugin -r org.codehaus.mojo:animal-sniffer-maven-plugin

# Use testng:5.14.6
# cannot find symbol: class AnnotationTypeEnum location: package org.testng.internal
sed -i '/AnnotationTypeEnum/d' \
 testng/core/src/test/java/org/jboss/arquillian/testng/TestNGTestBaseClass.java
 
# Use jetty:8.1.2.v20120308
%pom_xpath_set pom:properties/pom:version.jetty_jetty 8.1 protocols/servlet

%build

%mvn_build -s -- -Pejb31

%install
%mvn_install

%files api -f .mfiles-%{name}-api
%doc README.asciidoc
%doc LICENSE

%files impl-base -f .mfiles-%{name}-impl-base
%files spi -f .mfiles-%{name}-spi
%files parent -f .mfiles-%{name}-parent
%doc LICENSE

%files -n arquillian-bom -f .mfiles-arquillian-bom
%doc LICENSE

%files -n arquillian-build -f .mfiles-arquillian-build
%doc LICENSE

%files -n arquillian-config-api -f .mfiles-arquillian-config-api
%files -n arquillian-config-impl-base -f .mfiles-arquillian-config-impl-base
%files -n arquillian-config-spi -f .mfiles-arquillian-config-spi
%files -n arquillian-config-parent -f .mfiles-arquillian-config-parent
%doc LICENSE

%files -n arquillian-container-impl-base -f .mfiles-arquillian-container-impl-base
%files -n arquillian-container-spi -f .mfiles-arquillian-container-spi
%files -n arquillian-container-test-api -f .mfiles-arquillian-container-test-api
%files -n arquillian-container-test-impl-base -f .mfiles-arquillian-container-test-impl-base
%files -n arquillian-container-test-spi -f .mfiles-arquillian-container-test-spi
%files -n arquillian-container-parent -f .mfiles-arquillian-container-parent
%doc LICENSE

%files -n arquillian-junit-container -f .mfiles-arquillian-junit-container
%files -n arquillian-junit-core -f .mfiles-arquillian-junit-core
%files -n arquillian-junit-standalone -f .mfiles-arquillian-junit-standalone
%files -n arquillian-junit-parent -f .mfiles-arquillian-junit-parent
%doc LICENSE

%files -n arquillian-parent -f .mfiles-arquillian-parent
%doc LICENSE

%files -n arquillian-protocol-jmx -f .mfiles-arquillian-protocol-jmx
%files -n arquillian-protocol-servlet -f .mfiles-arquillian-protocol-servlet
%files -n arquillian-protocol-parent -f .mfiles-arquillian-protocol-parent
%doc LICENSE

%files -n arquillian-test-api -f .mfiles-arquillian-test-api
%files -n arquillian-test-impl-base -f .mfiles-arquillian-test-impl-base
%files -n arquillian-test-spi -f .mfiles-arquillian-test-spi
%files -n arquillian-test-parent -f .mfiles-arquillian-test-parent
%doc LICENSE

%files -n arquillian-testenricher-cdi -f .mfiles-arquillian-testenricher-cdi
%files -n arquillian-testenricher-ejb -f .mfiles-arquillian-testenricher-ejb
%files -n arquillian-testenricher-initialcontext -f .mfiles-arquillian-testenricher-initialcontext
%files -n arquillian-testenricher-resource -f .mfiles-arquillian-testenricher-resource
%files -n arquillian-testenricher-parent -f .mfiles-arquillian-testenricher-parent
%doc LICENSE

%files -n arquillian-testng-container -f .mfiles-arquillian-testng-container
%files -n arquillian-testng-core -f .mfiles-arquillian-testng-core
%files -n arquillian-testng-standalone -f .mfiles-arquillian-testng-standalone
%files -n arquillian-testng-parent -f .mfiles-arquillian-testng-parent
%doc LICENSE

%files javadoc -f .mfiles-javadoc
%doc LICENSE

%changelog
* Mon Dec 19 2016 Igor Vlasenko <viy@altlinux.ru> 1.1.11-alt1_3jpp8
- new version

* Wed Sep 12 2012 Igor Vlasenko <viy@altlinux.ru> 1.0.2-alt1_1jpp7
- new version

