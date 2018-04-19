Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires: rpm-build-java
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
%define fedora 27
# fedora bcond_with macro
%define bcond_with() %{expand:%%{?_with_%{1}:%%global with_%{1} 1}}
%define bcond_without() %{expand:%%{!?_without_%{1}:%%global with_%{1} 1}}
# redefine altlinux specific with and without
%define with()         %{expand:%%{?with_%{1}:1}%%{!?with_%{1}:0}}
%define without()      %{expand:%%{?with_%{1}:0}%%{!?with_%{1}:1}}
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
# %%version is ahead of its definition. Predefining for rpm 4.0 compatibility.
%define version 2.2.0
# Conditionals to help breaking org.wildfly.core:wildfly-controller <-> org.wildfly.legacy.test:wildfly-legacy-spi dependency cycle
%if 0%{?fedora}
%bcond_with legacy_test
%endif

%global namedreltag .Final
%global namedversion %{version}%{?namedreltag}

Name:          wildfly-core
Version:       2.2.0
Release:       alt1_8jpp8
Summary:       The core run-time of WildFly

# ASL 2.0: ./controller/src/main/java/org/jboss/as/controller/remote/CompletedFuture.java
#          ./controller-client/src/main/java/org/jboss/as/controller/client/helpers/standalone/ServerDeploymentHelper.java
#          ./embedded/src/main/java/org/wildfly/core/embedded/*
#          ./host-controller/src/main/java/org/jboss/as/host/controller/mgmt/DomainHostExcludeRegistry.java
#          ./process-controller/src/main/java/org/jboss/as/process/stdin/*
#          ./remoting/subsystem/src/main/java/org/jboss/as/remoting/ConnectorChildResource.java
#          ./server/src/main/java/org/jboss/as/server/parsing/ExtensionHandler.java
#          ./server/src/main/java/org/jboss/as/server/controller/resources/CapabilityRegistryResourceDefinition.java
#          ./server/src/main/java/org/jboss/as/server/controller/resources/ModuleInfoHandler.java
#          ./server/src/main/java/org/jboss/as/server/mgmt/ManagementWorkerService.java
#          ./testsuite/shared/src/main/java/*
#          ./threads/src/main/java/org/jboss/as/threads/ThreadsParser2_0.java
# BSD 2 C:  ./cli/src/main/java/org/jboss/as/cli/gui/component/ButtonTabComponent.java
# Some file without license headers https://issues.jboss.org/browse/WFCORE-1575
License:       ASL 2.0 and BSD and LGPLv2+
URL:           http://wildfly.org/
# sh wildfly-core-create-tarball.sh 2.2.0.Final
Source0:       %{name}-%{namedversion}-clean.tar.xz
Source1:       wildfly-core-create-tarball.sh

BuildRequires: maven-local
BuildRequires: mvn(io.undertow:undertow-core) >= 1.4.0
BuildRequires: mvn(junit:junit)
BuildRequires: mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires: mvn(org.apache.maven:maven-aether-provider)
BuildRequires: mvn(org.apache.maven.plugins:maven-assembly-plugin)
BuildRequires: mvn(org.apache.maven.plugins:maven-dependency-plugin)
BuildRequires: mvn(org.apache.maven.plugins:maven-shade-plugin)
BuildRequires: mvn(org.codehaus.plexus:plexus-utils)
BuildRequires: mvn(org.codehaus.woodstox:stax2-api)
BuildRequires: mvn(org.codehaus.woodstox:woodstox-core-asl)
BuildRequires: mvn(org.eclipse.aether:aether-api)
BuildRequires: mvn(org.eclipse.aether:aether-spi)
BuildRequires: mvn(org.eclipse.aether:aether-util)
BuildRequires: mvn(org.eclipse.aether:aether-connector-basic)
BuildRequires: mvn(org.eclipse.aether:aether-transport-file)
BuildRequires: mvn(org.eclipse.aether:aether-transport-http)
BuildRequires: mvn(org.fusesource.jansi:jansi)
BuildRequires: mvn(org.jboss:jandex)
BuildRequires: mvn(org.jboss:jboss-dmr) >= 1.3.0
BuildRequires: mvn(org.jboss:jboss-parent:pom:)
BuildRequires: mvn(org.jboss:jboss-vfs)
BuildRequires: mvn(org.jboss:staxmapper) >= 1.2.0
BuildRequires: mvn(org.jboss.aesh:aesh) >= 0.66.8
BuildRequires: mvn(org.jboss.byteman:byteman)
BuildRequires: mvn(org.jboss.classfilewriter:jboss-classfilewriter) >= 1.1.2
BuildRequires: mvn(org.jboss.invocation:jboss-invocation)
BuildRequires: mvn(org.jboss.jandex:jandex-maven-plugin)
BuildRequires: mvn(org.jboss.logging:jul-to-slf4j-stub)
BuildRequires: mvn(org.jboss.logmanager:jboss-logmanager) >= 2.0.4
BuildRequires: mvn(org.jboss.logmanager:log4j-jboss-logmanager) >= 1.1.2
BuildRequires: mvn(org.jboss.marshalling:jboss-marshalling)
BuildRequires: mvn(org.jboss.marshalling:jboss-marshalling-river)
BuildRequires: mvn(org.jboss.modules:jboss-modules) >= 1.5.2
BuildRequires: mvn(org.jboss.msc:jboss-msc)
BuildRequires: mvn(org.jboss.remoting:jboss-remoting)
BuildRequires: mvn(org.jboss.remotingjmx:remoting-jmx)
BuildRequires: mvn(org.jboss.sasl:jboss-sasl) >= 1.0.5
BuildRequires: mvn(org.jboss.slf4j:slf4j-jboss-logmanager)
BuildRequires: mvn(org.jboss.spec.javax.interceptor:jboss-interceptors-api_1.2_spec)
BuildRequires: mvn(org.jboss.stdio:jboss-stdio)
BuildRequires: mvn(org.jboss.threads:jboss-threads)
BuildRequires: mvn(org.jboss.xnio:xnio-api)
BuildRequires: mvn(org.jboss.xnio:xnio-nio)
BuildRequires: mvn(org.picketbox:picketbox) >= 4.9.5
BuildRequires: mvn(org.slf4j:slf4j-api)
BuildRequires: mvn(org.wildfly.build:wildfly-feature-pack-build-maven-plugin)
BuildRequires: mvn(org.wildfly.build:wildfly-server-provisioning-maven-plugin)
BuildRequires: mvn(org.wildfly.common:wildfly-common)
BuildRequires: mvn(org.wildfly.security:wildfly-elytron)
BuildRequires: mvn(xerces:xercesImpl)
BuildRequires: mvn(xml-resolver:xml-resolver)
BuildRequires: xmvn

%if %{with legacy_test}
BuildRequires: mvn(com.google.guava:guava)
BuildRequires: mvn(commons-io:commons-io)
BuildRequires: mvn(commons-lang:commons-lang)
BuildRequires: mvn(javax.inject:javax.inject)
BuildRequires: mvn(log4j:log4j:12)
BuildRequires: mvn(org.apache.directory.api:api-ldap-codec-standalone)
BuildRequires: mvn(org.apache.directory.jdbm:apacheds-jdbm1:bundle:)
BuildRequires: mvn(org.apache.directory.server:apacheds-core-annotations)
BuildRequires: mvn(org.apache.directory.server:apacheds-interceptor-kerberos)
BuildRequires: mvn(org.apache.directory.server:apacheds-parent:pom:)
BuildRequires: mvn(org.apache.directory.server:apacheds-server-annotations)
BuildRequires: mvn(org.apache.httpcomponents:httpclient)
BuildRequires: mvn(org.apache.httpcomponents:httpcore)
BuildRequires: mvn(org.apache.httpcomponents:httpmime)
BuildRequires: mvn(org.apache.maven.plugins:maven-antrun-plugin)
BuildRequires: mvn(org.codehaus.mojo:keytool-api-1.7)
BuildRequires: mvn(org.codehaus.mojo:keytool-maven-plugin)
BuildRequires: mvn(org.codehaus.mojo:xml-maven-plugin)
BuildRequires: mvn(org.jboss.byteman:byteman-bmunit)
BuildRequires: mvn(org.jboss.byteman:byteman-install)
BuildRequires: mvn(org.jboss.byteman:byteman-submit)
BuildRequires: mvn(org.jboss.metadata:jboss-metadata-common) >= 10.0.0
BuildRequires: mvn(org.jboss.shrinkwrap:shrinkwrap-api)
BuildRequires: mvn(org.jboss.shrinkwrap:shrinkwrap-impl-base)
BuildRequires: mvn(org.mockito:mockito-all)
BuildRequires: mvn(org.slf4j:jcl-over-slf4j)
# https://gil.fedorapeople.org/syslog4j.spec
BuildRequires: mvn(org.syslog4j:syslog4j)
BuildRequires: mvn(org.wildfly.legacy.test:wildfly-legacy-spi)
%endif

# ./process-controller/src/main/java/org/jboss/as/process/stdin/*
Provides:      bundled(apache-common-codec) = 1.7

BuildArch:     noarch
Source44: import.info

%description
This project provides the core run-time that is used by the
Wildfly application server. This includes:

* Modular class loading
* Unified management, including domain mode
* Basic deployment architecture
* CLI for management

%package javadoc
Group: Development/Java
Summary:       Javadoc for %{name}
BuildArch: noarch

%description javadoc
This package contains javadoc for %{name}.

%package feature-pack
Group: Development/Java
Summary:       WildFly: Core Feature Pack

%description feature-pack
WildFly: Core Feature Pack.

%prep
%setup -q -n %{name}-%{namedversion}

%if %{without legacy_test}
%pom_disable_module subsystem-test
%pom_disable_module testsuite
%pom_disable_module tests remoting
%pom_disable_module tests io
%pom_disable_module core-model-test
%pom_remove_dep -r org.wildfly.core:wildfly-core-model-test-framework
# org.apache.directory.server:apacheds-parent:pom:2.0.0-M15
%pom_remove_dep -r org.apache.directory.server:apacheds-parent
%else
%pom_xpath_set "pom:properties/pom:version.log4j" 1.2.17
%endif

%pom_remove_plugin -r :maven-shade-plugin
%pom_remove_plugin -r :maven-enforcer-plugin
%pom_remove_plugin -r org.zanata:zanata-maven-plugin

# Use not available org.wildfly.checkstyle:wildfly-checkstyle-config:jar:1.0.0.Final
%pom_remove_plugin -r :maven-checkstyle-plugin
%pom_remove_dep -r :wildfly-checkstyle-config

%pom_remove_dep sun.jdk:jconsole cli
%pom_add_dep sun.jdk:jconsole cli

cp -p core-feature-pack/src/main/resources/content/LICENSE.txt .

%mvn_package ":wildfly-core-feature-pack" core-feature-pack
%mvn_package ":wildfly-core-dist:::" __noinstall
%mvn_package ":wildfly-core-build:zip::" __noinstall
%mvn_package ":wildfly-core-build:::" __noinstall

%build

# We don't have packaged all test dependencies. e.g. org.wildfly.legacy.test:wildfly-legacy-spi:jar:1.0.0.Alpha9
%mvn_build -f -- -X

rm target/site/apidocs/javadoc.sh

%install
%mvn_install

%files -f .mfiles
%doc README.md
%doc --no-dereference LICENSE.txt

%files javadoc -f .mfiles-javadoc
%doc --no-dereference LICENSE.txt

%files feature-pack -f .mfiles-core-feature-pack
%doc --no-dereference LICENSE.txt

%changelog
* Thu Apr 19 2018 Igor Vlasenko <viy@altlinux.ru> 2.2.0-alt1_8jpp8
- java update

* Sat Nov 04 2017 Igor Vlasenko <viy@altlinux.ru> 2.2.0-alt1_7jpp8
- new version

