Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires: rpm-build-java
# END SourceDeps(oneline)
BuildRequires: bash4
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
# fedora bcond_with macro
%define bcond_with() %{expand:%%{?_with_%{1}:%%global with_%{1} 1}}
%define bcond_without() %{expand:%%{!?_without_%{1}:%%global with_%{1} 1}}
# redefine altlinux specific with and without
%define with()         %{expand:%%{?with_%{1}:1}%%{!?with_%{1}:0}}
%define without()      %{expand:%%{?with_%{1}:0}%%{!?with_%{1}:1}}
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
# %%version is ahead of its definition. Predefining for rpm 4.0 compatibility.
%define version 4.1.13
# Disable generation of debuginfo package
%global debug_package %{nil}
%global namedreltag .Final
%global namedversion %{version}%{?namedreltag}

%bcond_with     jp_minimal

Name:           netty
Version:        4.1.13
Release:        alt1_1jpp8
Summary:        An asynchronous event-driven network application framework and tools for Java
License:        ASL 2.0
URL:            https://netty.io/
Source0:        https://github.com/netty/netty/archive/netty-%{namedversion}.tar.gz
# Upsteam uses a simple template generator script written in groovy and run with gmaven
# We don't have the plugin and want to avoid groovy dependency
# This script is written in bash+sed and performs the same task
Source1:        codegen.bash
Patch0:         0001-Remove-OpenSSL-parts-depending-on-tcnative.patch
Patch1:         0002-Remove-NPN.patch
Patch2:         0003-Remove-conscrypt-ALPN.patch

BuildRequires:  maven-local
BuildRequires:  mvn(ant-contrib:ant-contrib)
BuildRequires:  mvn(com.jcraft:jzlib)
BuildRequires:  mvn(commons-logging:commons-logging)
BuildRequires:  mvn(kr.motd.maven:os-maven-plugin)
BuildRequires:  mvn(log4j:log4j:1.2.17)
BuildRequires:  mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires:  mvn(org.apache.logging.log4j:log4j-api)
BuildRequires:  mvn(org.apache.maven.plugins:maven-antrun-plugin)
BuildRequires:  mvn(org.apache.maven.plugins:maven-dependency-plugin)
BuildRequires:  mvn(org.apache.maven.plugins:maven-remote-resources-plugin)
BuildRequires:  mvn(org.codehaus.mojo:build-helper-maven-plugin)
BuildRequires:  mvn(org.codehaus.mojo:exec-maven-plugin)
BuildRequires:  mvn(org.eclipse.jetty.alpn:alpn-api)
BuildRequires:  mvn(org.fusesource.hawtjni:maven-hawtjni-plugin)
BuildRequires:  mvn(org.javassist:javassist)
BuildRequires:  mvn(org.jctools:jctools-core)
BuildRequires:  mvn(org.slf4j:slf4j-api)
BuildRequires:  mvn(org.sonatype.oss:oss-parent:pom:)
%if %{without jp_minimal}
BuildRequires:  mvn(com.fasterxml:aalto-xml)
BuildRequires:  mvn(com.github.jponge:lzma-java)
BuildRequires:  mvn(com.google.protobuf.nano:protobuf-javanano)
BuildRequires:  mvn(com.google.protobuf:protobuf-java)
BuildRequires:  mvn(com.ning:compress-lzf)
BuildRequires:  mvn(net.jpountz.lz4:lz4)
BuildRequires:  mvn(org.bouncycastle:bcpkix-jdk15on)
BuildRequires:  mvn(org.jboss.marshalling:jboss-marshalling)
%endif
Source44: import.info

%description
Netty is a NIO client server framework which enables quick and easy
development of network applications such as protocol servers and
clients. It greatly simplifies and streamlines network programming
such as TCP and UDP socket server.

'Quick and easy' doesn't mean that a resulting application will suffer
from a maintainability or a performance issue. Netty has been designed
carefully with the experiences earned from the implementation of a lot
of protocols such as FTP, SMTP, HTTP, and various binary and
text-based legacy protocols. As a result, Netty has succeeded to find
a way to achieve ease of development, performance, stability, and
flexibility without a compromise.

%package javadoc
Group: Development/Java
Summary:   API documentation for %{name}
BuildArch: noarch

%description javadoc
%{summary}.

%prep
%setup -q -n netty-netty-%{namedversion}

%patch0 -p1
%patch1 -p1
%patch2 -p1

# Missing Mavenized rxtx
%pom_disable_module "transport-rxtx"
%pom_remove_dep ":netty-transport-rxtx" all
# Missing com.barchart.udt:barchart-udt-bundle:jar:2.3.0
%pom_disable_module "transport-udt"
%pom_remove_dep ":netty-transport-udt" all
%pom_remove_dep ":netty-build" all
# Not needed
%pom_disable_module "example"
%pom_remove_dep ":netty-example" all
%pom_disable_module "testsuite"
%pom_disable_module "testsuite-autobahn"
%pom_disable_module "testsuite-osgi"
%pom_disable_module "tarball"
%pom_disable_module "microbench"

%pom_xpath_inject 'pom:plugin[pom:artifactId="maven-remote-resources-plugin"]' '
<dependencies>
<dependency>
<groupId>io.netty</groupId>
<artifactId>netty-dev-tools</artifactId>
<version>${project.version}</version>
</dependency>
</dependencies>'

%pom_remove_plugin :maven-antrun-plugin
# get-jetty-alpn-agent
%pom_remove_plugin :maven-dependency-plugin
# style checker
%pom_remove_plugin :xml-maven-plugin
%pom_remove_plugin -r :maven-checkstyle-plugin
%pom_remove_plugin -r :animal-sniffer-maven-plugin
%pom_remove_plugin -r :maven-enforcer-plugin
%pom_remove_plugin -r :maven-shade-plugin
%pom_remove_plugin -r :maven-release-plugin
%pom_remove_plugin -r :maven-clean-plugin
%pom_remove_plugin -r :maven-source-plugin
%pom_remove_plugin -r :maven-deploy-plugin
%pom_remove_plugin -r :maven-jxr-plugin
%pom_remove_plugin -r :maven-javadoc-plugin
%pom_remove_plugin -r :forbiddenapis

cp %{SOURCE1} common/codegen.bash
%pom_add_plugin org.codehaus.mojo:exec-maven-plugin common '
<executions>
    <execution>
        <id>generate-collections</id>
        <phase>generate-sources</phase>
        <goals>
            <goal>exec</goal>
        </goals>
        <configuration>
            <executable>common/codegen.bash</executable>
        </configuration>
    </execution>
</executions>
'
%pom_remove_plugin :groovy-maven-plugin common

%if %{with jp_minimal}
%pom_remove_dep -r "com.google.protobuf:protobuf-java"
%pom_remove_dep -r "com.google.protobuf.nano:protobuf-javanano"
rm codec/src/main/java/io/netty/handler/codec/protobuf/*
sed -i '/import.*protobuf/d' codec/src/main/java/io/netty/handler/codec/DatagramPacket*.java
%pom_remove_dep -r "org.jboss.marshalling:jboss-marshalling"
rm codec/src/main/java/io/netty/handler/codec/marshalling/*
%pom_remove_dep -r org.bouncycastle
rm handler/src/main/java/io/netty/handler/ssl/util/BouncyCastleSelfSignedCertGenerator.java
sed -i '/BouncyCastleSelfSignedCertGenerator/s/.*/throw new UnsupportedOperationException();/' \
    handler/src/main/java/io/netty/handler/ssl/util/SelfSignedCertificate.java
%pom_remove_dep -r com.fasterxml:aalto-xml
%pom_disable_module codec-xml
%pom_remove_dep :netty-codec-xml all
%pom_remove_dep -r com.github.jponge:lzma-java
rm codec/src/*/java/io/netty/handler/codec/compression/Lzma*.java
%pom_remove_dep -r com.ning:compress-lzf
rm codec/src/*/java/io/netty/handler/codec/compression/Lzf*.java
%pom_remove_dep -r net.jpountz.lz4:lz4
rm codec/src/*/java/io/netty/handler/codec/compression/Lz4*.java

%endif # jp_minimal

sed -i 's|taskdef|taskdef classpathref="maven.plugin.classpath"|' all/pom.xml

%pom_xpath_inject "pom:plugins/pom:plugin[pom:artifactId = 'maven-antrun-plugin']" '<dependencies><dependency><groupId>ant-contrib</groupId><artifactId>ant-contrib</artifactId><version>1.0b3</version></dependency></dependencies>' all/pom.xml
%pom_xpath_inject "pom:execution[pom:id = 'build-native-lib']/pom:configuration" '<verbose>true</verbose>' transport-native-epoll/pom.xml

# Upstream has jctools bundled.
%pom_xpath_remove "pom:build/pom:plugins/pom:plugin[pom:artifactId = 'maven-bundle-plugin']/pom:executions/pom:execution[pom:id = 'generate-manifest']/pom:configuration/pom:instructions/pom:Import-Package" common/pom.xml

# Tell xmvn to install attached artifact, which it does not
# do by default. In this case install all attached artifacts with
# the linux classifier.
%mvn_package ":::linux*:"
sed -i -e s,/bin/bash,/bin/bash4, common/codegen.bash

%build
export CFLAGS="$RPM_OPT_FLAGS" LDFLAGS="$RPM_LD_FLAGS"
%mvn_build -f

%install
%mvn_install

%files -f .mfiles
%doc LICENSE.txt NOTICE.txt

%files javadoc -f .mfiles-javadoc
%doc LICENSE.txt NOTICE.txt

%changelog
* Sat Nov 18 2017 Igor Vlasenko <viy@altlinux.ru> 4.1.13-alt1_1jpp8
- new version

* Wed Nov 01 2017 Igor Vlasenko <viy@altlinux.ru> 4.0.42-alt1_2jpp8
- new jpp release

* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 4.0.28-alt1_3jpp8
- new fc release

* Wed Feb 10 2016 Igor Vlasenko <viy@altlinux.ru> 4.0.28-alt1_2jpp8
- new version

* Mon Sep 08 2014 Igor Vlasenko <viy@altlinux.ru> 3.6.6-alt1_2jpp7
- new release

* Mon Aug 25 2014 Igor Vlasenko <viy@altlinux.ru> 3.6.3-alt1_3jpp7
- new version

* Thu Aug 21 2014 Igor Vlasenko <viy@altlinux.ru> 3.5.11-alt3_1jpp7
- added BR: for xmvn

* Thu Aug 07 2014 Igor Vlasenko <viy@altlinux.ru> 3.5.11-alt2_1jpp7
- rebuild with maven-local

* Wed Feb 13 2013 Igor Vlasenko <viy@altlinux.ru> 3.5.11-alt1_1jpp7
- fc update

* Mon Oct 08 2012 Igor Vlasenko <viy@altlinux.ru> 3.5.8-alt1_1jpp7
- new version

* Thu Sep 20 2012 Igor Vlasenko <viy@altlinux.ru> 3.5.3-alt1_1jpp7
- new version

* Tue Sep 11 2012 Igor Vlasenko <viy@altlinux.ru> 3.2.4-alt1_2jpp7
- complete build

* Wed Mar 07 2012 Igor Vlasenko <viy@altlinux.ru> 3.2.4-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

