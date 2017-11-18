Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-fedora-compat
BuildRequires: java-devel-default rpm-build-java
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
# fedora __isa_bits tmp hack
%ifarch x86_64
%define __isa_bits 64
%else
%define __isa_bits 32
%endif
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
# empty debuginfo
%global debug_package %nil

Name:          artemis
Version:       1.4.0
Release:       alt1_7jpp8
Summary:       Java high performance, clustered, asynchronous messaging system
License:       ASL 2.0
URL:           https://activemq.apache.org/artemis/
Source0:       https://github.com/apache/activemq-artemis/archive/%{version}/%{name}-%{version}.tar.gz

Patch0: artemis-netty-4.1.patch

BuildRequires: gcc-c++
BuildRequires: ctest cmake
BuildRequires: libaio-devel
BuildRequires: libtool
BuildRequires: maven-local
BuildRequires: mvn(com.google.guava:guava)
BuildRequires: mvn(commons-beanutils:commons-beanutils)
BuildRequires: mvn(io.airlift:airline)
BuildRequires: mvn(io.netty:netty-all)
BuildRequires: mvn(javax.inject:javax.inject)
BuildRequires: mvn(javax.json:javax.json-api)
BuildRequires: mvn(javax.xml.bind:jaxb-api)
BuildRequires: mvn(junit:junit)
BuildRequires: mvn(org.apache:apache:pom:)
BuildRequires: mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires: mvn(org.apache.johnzon:johnzon-core)
BuildRequires: mvn(org.apache.geronimo.specs:geronimo-annotation_1.1_spec)
BuildRequires: mvn(org.apache.geronimo.specs:geronimo-ejb_3.0_spec)
BuildRequires: mvn(org.apache.geronimo.specs:geronimo-jta_1.1_spec)
BuildRequires: mvn(org.apache.maven:maven-plugin-api)
BuildRequires: mvn(org.apache.maven.plugins:maven-antrun-plugin)
BuildRequires: mvn(org.apache.maven.plugins:maven-dependency-plugin)
BuildRequires: mvn(org.apache.maven.plugins:maven-enforcer-plugin)
BuildRequires: mvn(org.apache.maven.plugins:maven-install-plugin)
BuildRequires: mvn(org.apache.maven.plugins:maven-plugin-plugin)
BuildRequires: mvn(org.apache.maven.plugin-tools:maven-plugin-annotations)
BuildRequires: mvn(org.apache.qpid:proton-j)
BuildRequires: mvn(org.apache.qpid:proton-jms)
BuildRequires: mvn(org.apache.rat:apache-rat-plugin)
BuildRequires: mvn(org.codehaus.mojo:build-helper-maven-plugin)
BuildRequires: mvn(org.codehaus.mojo:javacc-maven-plugin)
BuildRequires: mvn(org.easymock:easymock)
BuildRequires: mvn(org.eclipse.aether:aether-api)
BuildRequires: mvn(org.eclipse.aether:aether-util)
BuildRequires: mvn(org.eclipse.jetty:jetty-server)
BuildRequires: mvn(org.eclipse.jetty:jetty-webapp)
BuildRequires: mvn(org.eclipse.osgi:org.eclipse.osgi)
BuildRequires: mvn(org.eclipse.osgi:org.eclipse.osgi.services)
BuildRequires: mvn(org.glassfish.jaxb:jaxb-jxc)
BuildRequires: mvn(org.glassfish.jaxb:jaxb-runtime)
BuildRequires: mvn(org.jboss.logging:jboss-logging)
BuildRequires: mvn(org.jboss.logging:jboss-logging-processor)
BuildRequires: mvn(org.jboss.logmanager:jboss-logmanager)
BuildRequires: mvn(org.jboss.modules:jboss-modules)
BuildRequires: mvn(org.jboss.spec.javax.jms:jboss-jms-api_2.0_spec)
BuildRequires: mvn(org.jboss.spec.javax.resource:jboss-connector-api_1.7_spec)
BuildRequires: mvn(org.jboss.resteasy:resteasy-atom-provider)
BuildRequires: mvn(org.jboss.resteasy:resteasy-jackson-provider)
BuildRequires: mvn(org.jboss.resteasy:resteasy-jaxb-provider)
BuildRequires: mvn(org.jboss.resteasy:resteasy-jaxrs)
BuildRequires: mvn(org.jboss.resteasy:tjws)
BuildRequires: mvn(org.jgroups:jgroups)
BuildRequires: mvn(org.slf4j:slf4j-api)
BuildRequires: mvn(org.springframework:spring-beans)
BuildRequires: mvn(org.springframework:spring-context)
BuildRequires: mvn(org.springframework:spring-core)
BuildRequires: mvn(org.springframework:spring-jms)
BuildRequires: mvn(postgresql:postgresql)
BuildRequires: mvn(xalan:xalan)
Source44: import.info


%description
Apache ActiveMQ Artemis is an open source project to
build a multi-protocol, embeddable, very high performance,
clustered, asynchronous messaging system. Artemis
is an example of Message Oriented Middleware (MoM).

%package boot
Group: Development/Java
Summary:       ActiveMQ Artemis Boot
BuildArch:     noarch

%description boot
ActiveMQ Artemis Boot.

%package cli
Group: Development/Java
Summary:       ActiveMQ Artemis CLI
BuildArch:     noarch

%description cli
ActiveMQ Artemis CLI.

%package commons
Group: Development/Java
Summary:       ActiveMQ Artemis Commons
# ./artemis-commons/src/main/java/org/apache/activemq/artemis/utils/Base64.java
License:       ASL 2.0 and Public Domain
BuildArch:     noarch
Provides:      bundled(java-base64) = 2.2.2

%description commons
ActiveMQ Artemis Commons.

%package core-client
Group: Development/Java
Summary:       ActiveMQ Artemis Core Client
BuildArch:     noarch

%description core-client
ActiveMQ Artemis Core Client.

%package dto
Group: Development/Java
Summary:       ActiveMQ Artemis DTO
BuildArch:     noarch

%description dto
ActiveMQ Artemis DTO.

%package jdbc-store
Group: Development/Java
Summary:       ActiveMQ Artemis JDBC Store
BuildArch:     noarch

%description jdbc-store
ActiveMQ Artemis JDBC Store.

%package jms-client
Group: Development/Java
Summary:       ActiveMQ Artemis JMS Client
BuildArch:     noarch

%description jms-client
ActiveMQ Artemis JMS Client.

%package jms-server
Group: Development/Java
Summary:       ActiveMQ Artemis JMS Server
BuildArch:     noarch

%description jms-server
ActiveMQ Artemis JMS Server.

%package journal
Group: Development/Java
Summary:       ActiveMQ Artemis Journal
BuildArch:     noarch

%description journal
ActiveMQ Artemis Journal.

%package maven-plugin
Group: Development/Java
Summary:       ActiveMQ Artemis Maven Plugin
BuildArch:     noarch

%description maven-plugin
ActiveMQ Artemis Maven Plugin.

%package native
Group: Development/Java
Summary:       ActiveMQ Artemis native library

%description native
Artemis distributes a native library,
used as a bridge for its fast journal,
between Artemis and Linux libaio.

%package protocols
Group: Development/Java
Summary:       ActiveMQ Artemis Protocols POM
BuildArch:     noarch

%description protocols
ActiveMQ Artemis Protocols Parent POM.

%package amqp-protocol
Group: Development/Java
Summary:       ActiveMQ Artemis Protocol AMQP
BuildArch:     noarch

%description amqp-protocol
Apache ActiveMQ Artemis supports for AMQP 1.0
specification.

%package hornetq-protocol
Group: Development/Java
Summary:       ActiveMQ Artemis Protocol HornetQ
BuildArch:     noarch

%description hornetq-protocol
ActiveMQ Artemis Protocol HornetQ.

%package hqclient-protocol
Group: Development/Java
Summary:       ActiveMQ Artemis Protocol HQClient
BuildArch:     noarch

%description hqclient-protocol
Apache ActiveMQ Artemis Protocol HQClient.

%package proton-plug
Group: Development/Java
Summary:       ActiveMQ Artemis Protocol Proton
BuildArch:     noarch

%description proton-plug
Apache ActiveMQ Artemis Protocol Proton.

%package stomp-protocol
Group: Development/Java
Summary:       ActiveMQ Artemis Protocol STOMP
BuildArch:     noarch

%description stomp-protocol
Apache ActiveMQ Artemis Protocol STOMP.

%package ra
Group: Development/Java
Summary:       ActiveMQ Artemis RAR
BuildArch:     noarch

%description ra
Apache ActiveMQ Artemis RAR.

%package rest
Group: Development/Java
Summary:       ActiveMQ Artemis REST Interface Implementation
BuildArch:     noarch

%description rest
Apache ActiveMQ Artemis REST Interface Implementation.

%package selector
Group: Development/Java
Summary:       ActiveMQ Artemis Selector Implementation
BuildArch:     noarch

%description selector
Apache ActiveMQ Artemis Selector Implementation.

%package server
Group: Development/Java
Summary:       ActiveMQ Artemis Server
BuildArch:     noarch

%description server
Apache ActiveMQ Artemis Server.

%package server-osgi
Group: Development/Java
Summary:       ActiveMQ Artemis Server OSGi
BuildArch:     noarch

%description server-osgi
Apache ActiveMQ Artemis Server OSGi.

%package service-extensions
Group: Development/Java
Summary:       ActiveMQ Artemis Service Extensions
BuildArch:     noarch

%description service-extensions
Apache ActiveMQ Artemis Service Extensions.

%package web
Group: Development/Java
Summary:       ActiveMQ Artemis Web
BuildArch:     noarch

%description web
Apache ActiveMQ Artemis Web.

%package spring-integration
Group: Development/Java
Summary:       ActiveMQ Artemis Spring Integration
BuildArch:     noarch

%description spring-integration
Apache ActiveMQ Artemis Spring Integration.

%package pom
Group: Development/Java
Summary:       ActiveMQ Artemis POM
BuildArch:     noarch

%description pom
ActiveMQ Artemis Parent POM.

%package javadoc
Group: Development/Java
Summary:       Javadoc for %{name}
BuildArch:     noarch

%description javadoc
This package contains javadoc for %{name}.

%package doc
Group: Development/Java
Summary:       Documentation for %{name}
BuildArch:     noarch

%description doc
Documentation for %{name}.

%prep
%setup -q -n activemq-%{name}-%{version}
%patch0 -p1

# Cleanup
find -name "*.class" -print -delete
find -name "*.dll" -print -delete
find -name "*.exe" -print -delete
find -name "*.jar" -print -delete
find -name "*.so" -print -delete
rm -r .mvn .settings


%pom_change_dep -r :geronimo-json_1.0_spec javax.json:javax.json-api:1.0 artemis-core-client artemis-jms-server tests/integration-tests pom.xml

# Use org.hornetq:hornetq-checkstyle-checks:0.2
%pom_remove_plugin -r :maven-checkstyle-plugin

%pom_remove_plugin -r :maven-help-plugin
%pom_remove_plugin -r :maven-source-plugin

# Use org.codehaus.plexus:plexus-compiler-javac-errorprone:2.5
%pom_remove_plugin :maven-compiler-plugin
for p in artemis-native \
 artemis-protocols/artemis-proton-plug \
 artemis-protocols/artemis-stomp-protocol
do
 %pom_add_plugin org.apache.maven.plugins:maven-compiler-plugin ${p} "
 <configuration>
  <compilerArgument>-proc:none</compilerArgument>
 </configuration>"
done

%pom_remove_plugin -r :findbugs-maven-plugin

# Not available runtime dep
%pom_remove_dep -r com.sun.winsw:winsw
%pom_remove_plugin :maven-dependency-plugin artemis-cli

# org.osgi:6.0.0
%pom_change_dep -r org.osgi:org.osgi.core org.eclipse.osgi:org.eclipse.osgi
%pom_change_dep -r org.osgi:osgi.cmpn org.eclipse.osgi:org.eclipse.osgi.services

%pom_change_dep -r :geronimo-j2ee-connector_1.5_spec org.jboss.spec.javax.resource:jboss-connector-api_1.7_spec
%pom_change_dep -r :geronimo-jms_2.0_spec org.jboss.spec.javax.jms:jboss-jms-api_2.0_spec
# Update jaxb gId
%pom_change_dep -r com.sun.xml.bind:jaxb-jxc org.glassfish.jaxb:jaxb-jxc
%pom_change_dep -r com.sun.xml.bind:jaxb-impl org.glassfish.jaxb:jaxb-runtime

# org.eclipse.jetty.aggregate:jetty-all::uber:9.3.10.v20160621
%pom_xpath_remove -r "pom:dependency[pom:artifactId='jetty-all']/pom:classifier"
%pom_change_dep -r :jetty-all org.eclipse.jetty:jetty-server
%pom_add_dep org.eclipse.jetty:jetty-webapp:'${jetty.version}' artemis-web

# https://bugzilla.redhat.com/show_bug.cgi?id=1217395
# org.postgresql:postgresql:9.4-1205-jdbc4
%pom_change_dep -r org.postgresql:postgresql postgresql:

%pom_change_dep -r log4j: ::1.2.17

%pom_disable_module artemis-distribution
%pom_disable_module artemis-website
%pom_disable_module artemis-features
%pom_disable_module tests

%pom_disable_module integration/activemq-aerogear-integration
%pom_disable_module integration/activemq-vertx-integration
# https://bugzilla.redhat.com/show_bug.cgi?id=998251
# org.apache.activemq:activemq-client:5.12.0
%pom_disable_module artemis-openwire-protocol artemis-protocols
# https://bugzilla.redhat.com/show_bug.cgi?id=1359246
# io.netty:netty-codec-mqtt:5.0.0.Alpha2
%pom_disable_module artemis-mqtt-protocol artemis-protocols

%pom_xpath_remove "pom:plugin[pom:artifactId='maven-bundle-plugin']/pom:configuration/pom:instructions/pom:_exportcontents" artemis-server-osgi
%pom_xpath_remove "pom:plugin[pom:artifactId='maven-bundle-plugin']/pom:configuration/pom:instructions/pom:Embed-Dependency" artemis-server-osgi
%pom_xpath_inject "pom:plugin[pom:artifactId='maven-bundle-plugin']/pom:configuration" "
<excludeDependencies>true</excludeDependencies>" artemis-server-osgi

# [ERROR]     'dependencies.dependency.(groupId:artifactId:type:classifier)'
# must be unique: org.apache.activemq:artemis-commons:jar
# -> duplicate declaration of version ${project.version} @ org.apache.activemq:artemis-proton-plug:[unknown-version]
%pom_remove_dep :artemis-commons::test artemis-protocols/artemis-proton-plug

%build

# compile native library
(
 cd artemis-native
 %{fedora_cmake} .
%make_build
)
# Some test dependecies are not available 
# e.g. org.apache.qpid:qpid-client:0.24,org.apache.qpid:qpid-jms-client:0.5.0
%mvn_build -fs

%install
%mvn_install

# Install native stuff
mkdir -p %{buildroot}%{_libdir}/%{name}
install -pm 755 artemis-native/bin/libartemis-native-%{__isa_bits}.so %{buildroot}%{_libdir}/%{name}/libartemis-native.so

%files boot -f .mfiles-artemis-boot
%doc LICENSE NOTICE

%files cli -f .mfiles-artemis-cli
%doc LICENSE NOTICE

%files commons -f .mfiles-artemis-commons
%doc LICENSE NOTICE

%files core-client -f .mfiles-artemis-core-client
%doc README.md

%files dto -f .mfiles-artemis-dto
%files jdbc-store -f .mfiles-artemis-jdbc-store
%files jms-client -f .mfiles-artemis-jms-client
%files jms-server -f .mfiles-artemis-jms-server
%files journal -f .mfiles-artemis-journal
%files maven-plugin -f .mfiles-artemis-maven-plugin

%files native -f .mfiles-artemis-native
%{_libdir}/%{name}
%doc LICENSE NOTICE

%files protocols -f .mfiles-artemis-protocols
%doc LICENSE NOTICE

%files amqp-protocol -f .mfiles-artemis-amqp-protocol
%files hornetq-protocol -f .mfiles-artemis-hornetq-protocol
%files hqclient-protocol -f .mfiles-artemis-hqclient-protocol
%files proton-plug -f .mfiles-artemis-proton-plug
%files stomp-protocol -f .mfiles-artemis-stomp-protocol

%files ra -f .mfiles-artemis-ra
%files rest -f .mfiles-artemis-rest
%files selector -f .mfiles-artemis-selector
%doc LICENSE NOTICE

%files server -f .mfiles-artemis-server
%files server-osgi -f .mfiles-artemis-server-osgi
%files service-extensions -f .mfiles-artemis-service-extensions
%files web -f .mfiles-artemis-web

%files spring-integration -f .mfiles-artemis-spring-integration
%files pom -f .mfiles-artemis-pom
%doc LICENSE NOTICE

%files javadoc -f .mfiles-javadoc
%doc LICENSE NOTICE

%files doc
%doc docs/*
%doc LICENSE NOTICE

%changelog
* Sat Nov 18 2017 Igor Vlasenko <viy@altlinux.ru> 1.4.0-alt1_7jpp8
- fixed build with netty

* Sun Oct 22 2017 Igor Vlasenko <viy@altlinux.ru> 1.4.0-alt1_4jpp8
- new jpp release

* Mon Dec 19 2016 Igor Vlasenko <viy@altlinux.ru> 1.4.0-alt1_2jpp8
- new version

