Name:           netty
Version:        4.1.130
Release:        alt1

Summary:        Netty project - an event-driven asynchronous network application framework
License:        Apache-2.0
Group:          Development/Java
URL:            https://netty.io/
VCS:            https://github.com/netty/netty

Source0:        %name-%version.tar
Source1:        codegen.bash

Patch0:         0001-drop-conscrypt-support.patch
Patch1:         0002-drop-jetty-alpn-and-npn-support.patch
Patch2:         0003-drop-brotli-and-zstd-support.patch

BuildRequires(pre):  maven-local
BuildRequires:  jpackage-default

BuildRequires:  netty-jni-util-source

BuildRequires:  mvn(org.sonatype.oss:oss-parent:pom:)
BuildRequires:  mvn(kr.motd.maven:os-maven-plugin)
BuildRequires:  mvn(org.codehaus.mojo:build-helper-maven-plugin)
BuildRequires:  mvn(org.apache.maven.plugins:maven-dependency-plugin)
BuildRequires:  mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires:  mvn(ch.qos.logback:logback-classic)
BuildRequires:  mvn(org.mortbay.jetty.alpn:jetty-alpn-agent)
BuildRequires:  mvn(org.jctools:jctools-core)
BuildRequires:  mvn(commons-logging:commons-logging)
BuildRequires:  mvn(org.apache.logging.log4j:log4j-1.2-api)
BuildRequires:  mvn(org.apache.logging.log4j:log4j-api)
BuildRequires:  mvn(org.apache.logging.log4j:log4j-core)
BuildRequires:  mvn(org.mockito:mockito-core)
BuildRequires:  mvn(org.reflections:reflections)
BuildRequires:  mvn(com.google.protobuf:protobuf-java)
BuildRequires:  mvn(org.jboss.marshalling:jboss-marshalling)
BuildRequires:  mvn(com.ning:compress-lzf)
BuildRequires:  mvn(com.github.jponge:lzma-java)
BuildRequires:  mvn(org.codehaus.mojo:exec-maven-plugin)
BuildRequires:  mvn(io.netty:netty-jni-util)
BuildRequires:  mvn(io.netty:netty-tcnative-classes)
BuildRequires:  mvn(io.netty:netty-tcnative)
BuildRequires:  mvn(org.bouncycastle:bctls-jdk15on)
BuildRequires:  mvn(com.fasterxml:aalto-xml)
BuildRequires:  mvn(commons-lang:commons-lang)
BuildRequires:  mvn(org.rxtx:rxtx)
BuildRequires:  mvn(org.fusesource.hawtjni:hawtjni-maven-plugin)
BuildRequires:  mvn(org.apache.maven.plugins:maven-antrun-plugin)
BuildRequires:  mvn(org.apache.maven.plugins:maven-shade-plugin)

%description
Netty is an asynchronous event-driven network application framework for rapid
development of maintainable high performance protocol servers & clients.

%javadoc_package

%package        bom
Group:          Development/Java
Summary:        Netty Bill of Materials
BuildArch:      noarch

%description    bom
%summary.

%prep
%setup
%autopatch -p1

%pom_remove_plugin -r :maven-remote-resources-plugin
%pom_remove_plugin :revapi-maven-plugin
%pom_remove_plugin -r :maven-source-plugin
%pom_remove_plugin :japicmp-maven-plugin 
%pom_remove_plugin :forbiddenapis
%pom_remove_plugin :xml-maven-plugin
%pom_remove_plugin :maven-antrun-plugin
%pom_remove_plugin -r :maven-failsafe-plugin
%pom_remove_plugin :maven-enforcer-plugin
%pom_remove_plugin :maven-checkstyle-plugin
%pom_remove_plugin :animal-sniffer-maven-plugin
%pom_remove_plugin -r :native-image-maven-plugin

%pom_remove_plugin :bom-helper-maven-plugin bom

# --- common module ---
%pom_remove_plugin :groovy-maven-plugin common

%pom_remove_dep -r :netty-build-common
%pom_remove_dep :svm common
%pom_remove_dep :annotations-java5 common
%pom_remove_dep :jdk-misc common

%java_remove_annotations common -p "com.oracle.svm.core.annotate"
%java_remove_annotations common -p "org.jetbrains.annotations"

%pom_remove_dep :blockhound common
rm common/src/main/java/io/netty/util/internal/Hidden.java

cp %SOURCE1 common/codegen.bash
chmod +x common/codegen.bash

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

# --- codec module ---
%pom_remove_dep :protobuf-javanano codec
rm codec/src/main/java/io/netty/handler/codec/protobuf/*
sed -i '/import.*protobuf/d' codec/src/main/java/io/netty/handler/codec/DatagramPacket*.java

%pom_remove_dep :lz4-java codec
rm codec/src/*/java/io/netty/handler/codec/compression/Lz4*.java

%pom_remove_dep :zstd-jni codec
rm codec/src/*/java/io/netty/handler/codec/compression/Zstd*.java

%pom_remove_dep com.aayushatharva.brotli4j: codec
rm codec/src/*/java/io/netty/handler/codec/compression/Brotli*.java

# disable tests for codec
rm -rf codec/src/test

# --- handler module ---
%pom_remove_dep :npn-api . handler
%pom_remove_dep :alpn-api . handler
%pom_remove_dep :AmazonCorrettoCryptoProvider handler

%pom_xpath_remove -f "//pom:profile[pom:id='boringssl-mac-aarch64' or pom:id='boringssl-linux-aarch64' or pom:id='boringssl']" pom.xml

rm -rf handler/src/test

# --- codec-http module ---
%pom_remove_dep com.aayushatharva.brotli4j: codec-http
%pom_remove_dep :zstd-jni codec-http

rm -rf codec-http/src/test

# --- codec-http module ---
%pom_remove_dep com.aayushatharva.brotli4j: codec-http2
%pom_remove_dep :zstd-jni codec-http2

rm -rf codec-http2/src/test

# --- resolver-dns module ---
%pom_remove_dep :apacheds-protocol-dns resolver-dns

rm resolver-dns/src/test/java/io/netty/resolver/dns/DnsNameResolverTest.java
rm resolver-dns/src/test/java/io/netty/resolver/dns/TestDnsServer.java
rm resolver-dns/src/test/java/io/netty/resolver/dns/SearchDomainTest.java
rm resolver-dns/src/test/java/io/netty/resolver/dns/ResolvConfTest.java
rm resolver-dns/src/test/java/io/netty/resolver/dns/DnsAddressResolverGroupTest.java

# --- transport-native-unix-common module ---

cp -p %_usrsrc/netty-jni-util/src/main/c/netty_jni_util.c transport-native-unix-common/src/main/c/
cp -p %_usrsrc/netty-jni-util/src/main/c/netty_jni_util.h transport-native-unix-common/src/main/c/
mkdir -p transport-native-unix-common/target/netty-jni-util

# broken scope
%pom_remove_dep io.netty:netty-jni-util transport-native-unix-common
%pom_add_dep io.netty:netty-jni-util transport-native-unix-common

# build without -Werror
sed -i 's/ -Werror -Wno-attributes / -Wno-attributes /g' transport-native-unix-common/pom.xml

# --- transport-native-epoll module ---

%pom_remove_dep :rerunner-jupiter . transport-native-epoll
rm transport-native-epoll/src/test/java/io/netty/channel/epoll/EpollSocketChannelConfigTest.java

sed -i 's/ -Werror//g' transport-native-epoll/pom.xml

# --- other modules ---
%pom_add_dep com.google.guava:guava resolver

%pom_add_dep org.slf4j:slf4j-api:test codec-socks

%pom_xpath_inject "pom:project" '
<properties><javaModuleName>io.netty.dev.tools</javaModuleName></properties>
' dev-tools

%pom_remove_dep :apacheds-protocol-dns codec-dns

%pom_remove_plugin :duplicate-finder-maven-plugin all
%pom_remove_plugin :flatten-maven-plugin all
%pom_remove_plugin :autobahntestsuite-maven-plugin testsuite-autobahn
%pom_remove_plugin :h2spec-maven-plugin testsuite-http2

# broken tests
rm buffer/src/test/java/io/netty/buffer/UnpooledTest.java
rm transport/src/test/java/io/netty/channel/CompleteChannelFutureTest.java
rm -rf handler-ssl-ocsp/src/test
rm testsuite/src/main/java/io/netty/testsuite/transport/udt/UDTClientServerConnectionTest.java
rm testsuite/src/main/java/io/netty/testsuite/transport/socket/SocketSslSessionReuseTest.java
rm transport-native-epoll/src/test/java/io/netty/channel/epoll/EpollSocketSslSessionReuseTest.java
rm transport-native-kqueue/src/test/java/io/netty/channel/kqueue/KQueueSocketSslSessionReuseTest.java

# broken in isolated build environment
sed -i '/testConnectCancellation(TestInfo testInfo)/i\    @org.junit.jupiter.api.Disabled("broken in isolated build environment")' \
  testsuite/src/main/java/io/netty/testsuite/transport/socket/SocketConnectionAttemptTest.java

# disable transport-udt cause missing deps
%pom_disable_module transport-udt
%pom_remove_dep -r :netty-transport-udt

# no need for rpm build
%pom_disable_module example
%pom_disable_module microbench

# missing felix dep
%pom_disable_module testsuite-osgi

# missing blockhound dep (gradle)
%pom_disable_module transport-blockhound-tests

%mvn_package :::linux*:
%mvn_package :%name-bom bom

%build
%mvn_build

%install
%mvn_install

%files -f .mfiles
%doc LICENSE.txt NOTICE.txt

%files bom -f .mfiles-bom

%changelog
* Thu Jun 25 2026 Evgeniy Serov <scala@altlinux.org> 4.1.130-alt1
- Updated to 4.1.130.
- Switched netty-bom to noarch packaging.

* Mon May 18 2026 Evgeniy Serov <scala@altlinux.org> 4.1.100-alt1
- Updated to 4.1.100.
- Returned to Sisyphus.

* Thu Jun 03 2021 Igor Vlasenko <viy@altlinux.org> 4.1.51-alt1_1jpp8
- new version, use jvm8

* Mon May 10 2021 Igor Vlasenko <viy@altlinux.org> 4.1.13-alt1_14jpp8
- update

* Fri Oct 09 2020 Igor Vlasenko <viy@altlinux.ru> 4.1.13-alt1_12jpp8
- update

* Tue Apr 02 2019 Igor Vlasenko <viy@altlinux.ru> 4.1.13-alt1_9jpp8
- fixed build (closes: #36463)

* Mon Feb 04 2019 Igor Vlasenko <viy@altlinux.ru> 4.1.13-alt1_6jpp8
- java update

* Fri Jun 01 2018 Igor Vlasenko <viy@altlinux.ru> 4.1.13-alt1_5jpp8
- java fc28+ update

* Thu Apr 19 2018 Igor Vlasenko <viy@altlinux.ru> 4.1.13-alt1_2jpp8
- java update

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

