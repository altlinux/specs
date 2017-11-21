Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-fedora-compat
BuildRequires: gcc-c++ rpm-build-java
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
# fedora __isa_bits tmp hack
%ifarch x86_64
%define __isa_bits 64
%else
%define __isa_bits 32
%endif
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
# %%version is ahead of its definition. Predefining for rpm 4.0 compatibility.
%define version 2.4.7
# empty debuginfo
%global debug_package %nil

%global namedreltag .Final
%global namedversion %{version}%{?namedreltag}
%global customnamedversion 2_4_7_Final

# Use this switch to rebuild without narayana
# This is useful to break the hornetq circular dependency
%if 0%{?fedora}
%bcond_with narayana
%endif

Name:          hornetq
Version:       2.4.7
Release:       alt2_6jpp8
Summary:       High performance messaging system
License:       ASL 2.0
URL:           http://hornetq.jboss.org/
Source0:       https://github.com/hornetq/hornetq/archive/HornetQ_%{customnamedversion}.tar.gz
# https://issues.jboss.org/browse/HORNETQ-1534
# Replace json.org with javax.json
Patch0:        hornetq-2.4.7-javax.json.patch
Patch1: hornetq-2.4.7-alt-netty.patch

BuildRequires: autoconf
BuildRequires: automake
BuildRequires: graphviz libgraphviz
BuildRequires: libaio-devel
BuildRequires: libtool
BuildRequires: maven-local
BuildRequires: mvn(com.github.maven-nar:nar-maven-plugin)
BuildRequires: mvn(io.netty:netty-all)
BuildRequires: mvn(java_cup:java_cup)
BuildRequires: mvn(javax.inject:javax.inject)
BuildRequires: mvn(javax.json:javax.json-api)
BuildRequires: mvn(javax.servlet:servlet-api)
BuildRequires: mvn(jdepend:jdepend)
BuildRequires: mvn(junit:junit)
BuildRequires: mvn(net.sf.saxon:saxon)
BuildRequires: mvn(org.apache.maven.plugins:maven-assembly-plugin)
BuildRequires: mvn(org.apache.maven.plugins:maven-install-plugin)
BuildRequires: mvn(org.codehaus.mojo:build-helper-maven-plugin)
BuildRequires: mvn(org.codehaus.mojo:javacc-maven-plugin)
BuildRequires: mvn(org.codehaus.mojo:xml-maven-plugin)
BuildRequires: mvn(org.jboss:jboss-transaction-spi)
BuildRequires: mvn(org.jboss.apiviz:apiviz)
BuildRequires: mvn(org.jboss.logging:jboss-logging)
BuildRequires: mvn(org.jboss.logging:jboss-logging-processor)
BuildRequires: mvn(org.jboss.logmanager:jboss-logmanager)
BuildRequires: mvn(org.jboss.naming:jnpserver)
%if %{without narayana}
BuildRequires: mvn(org.jboss.narayana.jta:jta)
BuildRequires: mvn(org.springframework:spring-beans)
BuildRequires: mvn(org.springframework:spring-context)
BuildRequires: mvn(org.springframework:spring-core)
BuildRequires: mvn(org.springframework:spring-jms)
%endif
BuildRequires: mvn(org.jboss.resteasy:resteasy-atom-provider)
BuildRequires: mvn(org.jboss.resteasy:resteasy-jackson-provider)
BuildRequires: mvn(org.jboss.resteasy:resteasy-jaxb-provider)
BuildRequires: mvn(org.jboss.resteasy:resteasy-jaxrs)
BuildRequires: mvn(org.jboss.resteasy:tjws)
BuildRequires: mvn(org.jboss.spec.javax.jms:jboss-jms-api_2.0_spec)
BuildRequires: mvn(org.jboss.spec.javax.resource:jboss-connector-api_1.6_spec)
BuildRequires: mvn(org.jboss.spec.javax.transaction:jboss-transaction-api_1.1_spec)
BuildRequires: mvn(org.jgroups:jgroups)
Source44: import.info

%description
HornetQ is an open source project to build a multi-protocol, embeddable,
very high performance, clustered, asynchronous messaging system.

%package commons
Group: Development/Java
Summary:       HornetQ Commons
# Public Domain: ./hornetq-commons/src/main/java/org/hornetq/utils/Base64.java
License:       ASL 2.0 and Public Domain
Provides:      bundled(java-base64) = 2.2.2
Obsoletes:     %{name} < 2.4.2
BuildArch:     noarch

%description commons
HornetQ Commons Classes.

%package core-client
Group: Development/Java
Summary:       HornetQ Core Client
License:       ASL 2.0 and LGPLv2+
# LGPLv2: 
#./hornetq-core-client/src/main/java/org/hornetq/core/filter/impl/Operator.java
#./hornetq-core-client/src/main/java/org/hornetq/core/filter/impl/RegExp.java
#./hornetq-core-client/src/main/java/org/hornetq/core/filter/impl/Identifier.java
BuildArch:     noarch

%description core-client
HornetQ Core Client.

%package jms-client
Group: Development/Java
Summary:       HornetQ JMS Client
BuildArch:     noarch

%description jms-client
HornetQ JMS Client Implementation.

%package jms-server
Group: Development/Java
Summary:       HornetQ JMS Server
BuildArch:     noarch

%description jms-server
HornetQ JMS Server Implementation.

%package journal
Group: Development/Java
Summary:       HornetQ Journal
BuildArch:     noarch

%description journal
HornetQ Journal.

%package native
Group: Development/Java
Summary:       HornetQ Journal

%description native
HornetQ Journal.

%package pom
Group: Development/Java
Summary:       HornetQ Parent POM
BuildArch:     noarch

%description pom
HornetQ Parent POM.

%package protocols
Group: Development/Java
Summary:       HornetQ Protocols Parent POM
BuildArch:     noarch

%description protocols
HornetQ Protocols Parent POM.

%package ra
Group: Development/Java
Summary:       HornetQ RAR
BuildArch:     noarch

%description ra
HornetQ RAR Implementation.

%package rest
Group: Development/Java
Summary:       HornetQ REST
BuildArch:     noarch

%description rest
HornetQ REST Interface Implementation.

%package server
Group: Development/Java
Summary:       HornetQ Server
License:       ASL 2.0 and LGPLv2+
# LGPLv2: ./hornetq-server/src/main/java/org/hornetq/core/messagecounter/MessageCounter.java
BuildArch:     noarch

%description server
HornetQ Server Implementation.

%package spring-integration
Group: Development/Java
Summary:       HornetQ Spring Integration
BuildArch:     noarch

%description spring-integration
HornetQ Spring Integration.

%package stomp-protocol
Group: Development/Java
Summary:       HornetQ STOMP Protocol
BuildArch:     noarch

%description stomp-protocol
HornetQ STOMP Protocol Implementation.

%package tools
Group: Development/Java
Summary:       HornetQ Tools
BuildArch:     noarch

%description tools
HornetQ Tools.

%package javadoc
Group: Development/Java
Summary:       Javadoc for %{name}
BuildArch:     noarch

%description javadoc
This package contains the API documentation for %{name}.

%prep
%setup -q -n hornetq-HornetQ_%{customnamedversion}
# Remove bundled .so files
find -name "*.so" -print -delete
find -name "*.jar" -print -delete

%patch0 -p1
rm -rf hornetq-core-client/src/main/java/org/hornetq/utils/json

%patch1 -p1

%pom_change_dep -r :geronimo-json_1.0_spec javax.json:javax.json-api:1.0 hornetq-core-client hornetq-jms-server tests/integration-tests

%pom_disable_module examples
%pom_disable_module hornetq-bootstrap
%pom_disable_module hornetq-service-sar
%pom_disable_module integration/hornetq-aerogear-integration
%pom_disable_module integration/hornetq-jboss-as-integration
%pom_disable_module integration/hornetq-twitter-integration
%pom_disable_module tests

# Incompatible version of qpid-proton-java
%pom_disable_module hornetq-amqp-protocol hornetq-protocols

%pom_remove_dep -r "org.jboss.microcontainer:jboss-kernel"

%if %{with narayana}
%pom_disable_module hornetq-jms-server
%pom_disable_module hornetq-ra
%pom_disable_module hornetq-rest
%pom_disable_module hornetq-tools
%pom_disable_module integration/hornetq-spring-integration
%endif

%pom_change_dep -r org.jboss.jbossts.jts:jbossjts-jacorb org.jboss.narayana.jta:jta
%pom_change_dep -r org.jboss.jbossts.jts:jbossjts-jacorb org.jboss.narayana.jta:jta hornetq-jms-server

%pom_remove_dep -r org.jboss.javaee:jboss-ejb-api
%pom_remove_dep -r org.jboss.javaee:jboss-jaspi-api
%pom_change_dep -r org.jboss.javaee:jboss-jca-api org.jboss.spec.javax.resource:jboss-connector-api_1.6_spec
%pom_change_dep -r org.jboss.javaee:jboss-jca-api org.jboss.spec.javax.resource:jboss-connector-api_1.6_spec hornetq-ra

%pom_remove_plugin -r :license-maven-plugin
%pom_remove_plugin -r :maven-checkstyle-plugin
%pom_remove_plugin -r :maven-help-plugin
%pom_remove_plugin -r :maven-source-plugin
%pom_remove_plugin -r :findbugs-maven-plugin

cp -p distribution/hornetq/src/main/resources/licenses/LICENSE.txt .

# Workaround for building native bits
# Currently the build script uses the .so in the hornetq-nativebin/ directory
# but we need to rebuild them. The issue is that the mvn build process does not
# use the new .so files we've built. Here is a simple workaround.
%pom_xpath_inject "pom:project/pom:profiles" "
<profile>
  <id>native</id>
  <modules>
    <module>hornetq-commons</module>
    <module>hornetq-native</module>
  </modules>
</profile>"

rm -r **/src/test/* tests/*/src/test/*

# [ERROR] 'dependencies.dependency.(groupId:artifactId:type:classifier)' must be unique duplicate declaration of version
%pom_remove_dep org.jboss.logmanager:jboss-logmanager hornetq-server
%pom_add_dep org.jboss.logmanager:jboss-logmanager:1.2.2.GA:test hornetq-server

%build

# Let's build the .so files
%mvn_build -i -f -- -Pnative,native-build
pushd hornetq-native
# Copy them to hornetq-native/bin/ dir
find -name "*.so" -exec cp {} bin/libHornetQAIO.so \;
find -name "*.so" -exec cp {} bin/libHornetQAIO%{__isa_bits}.so \;
popd

# Tests are skipped because required modules are disabled
%mvn_build -sf -- -Pmaven-release

%install
%mvn_install

# Install native stuff
install -d -m 755 %{buildroot}/%{_libdir}
cp -L hornetq-native/bin/libHornetQAIO.so %{buildroot}/%{_libdir}/libHornetQAIO.so

%files commons -f .mfiles-hornetq-commons
%doc README.md
%doc LICENSE.txt NOTICE

%files core-client -f .mfiles-hornetq-core-client
%files jms-client -f .mfiles-hornetq-jms-client
%files journal -f .mfiles-hornetq-journal

%files native -f .mfiles-hornetq-native
%{_libdir}/libHornetQAIO.so
%doc hornetq-native/README

%files pom -f .mfiles-hornetq-pom
%doc LICENSE.txt NOTICE

%files protocols -f .mfiles-hornetq-protocols
%doc LICENSE.txt NOTICE

%files server -f .mfiles-hornetq-server
%files stomp-protocol -f .mfiles-hornetq-stomp-protocol

%if %{without narayana}
%files jms-server -f .mfiles-hornetq-jms-server
%files ra -f .mfiles-hornetq-ra
%files rest -f .mfiles-hornetq-rest
%files spring-integration -f .mfiles-hornetq-spring-integration
%files tools -f .mfiles-hornetq-tools
%endif

%files javadoc -f .mfiles-javadoc
%doc LICENSE.txt NOTICE

%changelog
* Tue Nov 21 2017 Igor Vlasenko <viy@altlinux.ru> 2.4.7-alt2_6jpp8
- fixed build with new netty

* Thu Nov 09 2017 Igor Vlasenko <viy@altlinux.ru> 2.4.7-alt1_6jpp8
- fc27 update

* Sun Oct 22 2017 Igor Vlasenko <viy@altlinux.ru> 2.4.7-alt1_4jpp8
- new jpp release

* Fri Dec 16 2016 Igor Vlasenko <viy@altlinux.ru> 2.4.7-alt1_2jpp8
- new version

* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 2.4.1-alt1_7jpp8
- new fc release

* Thu Feb 11 2016 Igor Vlasenko <viy@altlinux.ru> 2.4.1-alt1_6jpp8
- build with narayana

* Thu Feb 11 2016 Igor Vlasenko <viy@altlinux.ru> 2.4.1-alt1_0jpp8
- new version. build w/o narayana

* Mon Jul 28 2014 Igor Vlasenko <viy@altlinux.ru> 2.2.13-alt2_6jpp7
- new release

* Mon Jul 14 2014 Igor Vlasenko <viy@altlinux.ru> 2.2.13-alt2_5jpp7
- NMU rebuild to move poms and fragments

* Thu Sep 13 2012 Igor Vlasenko <viy@altlinux.ru> 2.2.13-alt1_5jpp7
- new version

