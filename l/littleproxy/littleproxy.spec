Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires: rpm-build-java
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Name:          littleproxy
Version:       1.1.0
Release:       alt2_2jpp8
Summary:       High Performance HTTP Proxy
License:       ASL 2.0
URL:           http://www.littleshoot.org/littleproxy/
Source0:       https://github.com/adamfisk/LittleProxy/archive/%{name}-%{version}.tar.gz

Patch0:        littleproxy-1.1.0-remove-netty-udt.patch

BuildRequires: maven-local
BuildRequires: mvn(com.google.guava:guava)
BuildRequires: mvn(commons-cli:commons-cli)
BuildRequires: mvn(commons-codec:commons-codec)
BuildRequires: mvn(commons-io:commons-io)
BuildRequires: mvn(dnsjava:dnsjava)
BuildRequires: mvn(io.netty:netty-all)
BuildRequires: mvn(junit:junit)
BuildRequires: mvn(log4j:log4j:1.2.17)
BuildRequires: mvn(org.apache.commons:commons-exec)
BuildRequires: mvn(org.apache.commons:commons-lang3)
BuildRequires: mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires: mvn(org.apache.httpcomponents:httpclient)
BuildRequires: mvn(org.apache.maven.plugins:maven-enforcer-plugin)
BuildRequires: mvn(org.eclipse.jetty:jetty-server:8.1)
BuildRequires: mvn(org.hamcrest:hamcrest-core)
BuildRequires: mvn(org.hamcrest:hamcrest-library)
BuildRequires: mvn(org.jctools:jctools-core)
BuildRequires: mvn(org.littleshoot:dnssec4j)
BuildRequires: mvn(org.mockito:mockito-core)
BuildRequires: mvn(org.slf4j:slf4j-api)
BuildRequires: mvn(org.slf4j:slf4j-log4j12)
BuildRequires: mvn(org.sonatype.oss:oss-parent:pom:)

BuildArch:     noarch
Source44: import.info

%description
LittleProxy is a high performance HTTP proxy written in Java and
using the Netty networking framework.

%package javadoc
Group: Development/Java
Summary:       Javadoc for %{name}
BuildArch: noarch

%description javadoc
This package contains javadoc for %{name}.

%prep
%setup -q -n LittleProxy-%{name}-%{version}

find . -name "*.class" -print -delete
find . -name "*.jar" -print -delete

%patch0 -p1
%pom_remove_dep :barchart-udt-bundle
%pom_remove_dep :netty-transport-udp
rm src/test/java/org/littleshoot/proxy/*UDT*Test.java

# Unavailable plugins
%pom_remove_plugin :nexus-staging-maven-plugin

%pom_remove_plugin :maven-site-plugin
%pom_remove_plugin :maven-shade-plugin
mkdir src/main/resources
cp -p src/main/config/log4j.xml src/main/resources

%pom_xpath_set "pom:project/pom:packaging" bundle
%pom_add_plugin org.apache.felix:maven-bundle-plugin . "
<extensions>true</extensions>
<configuration>
  <instructions>
    <Bundle-Version>\${project.version}</Bundle-Version>
    <Main-Class>org.littleshoot.proxy.Launcher</Main-Class>
  </instructions>
</configuration>
<executions>
  <execution>
    <id>bundle-manifest</id>
    <phase>process-classes</phase>
    <goals>
      <goal>manifest</goal>
    </goals>
  </execution>
</executions>"

# 8.1.17.v20150415
%pom_change_dep :jetty-server ::8.1
%pom_xpath_inject "pom:dependency[pom:artifactId = 'jetty-server']" "
<exclusions>
 <exclusion>
  <groupId>org.eclipse.jetty.orbit</groupId>
  <artifactId>javax.servlet</artifactId>
 </exclusion>
</exclusions>"

# org.seleniumhq.selenium:selenium-java:2.46.0
%pom_remove_dep :selenium-java
rm src/test/java/org/littleshoot/proxy/EndToEndStoppingTest.java
# org.mock-server:mockserver-netty:3.10.4
%pom_remove_dep :mockserver-netty
rm src/test/java/org/littleshoot/proxy/ClonedProxyTest.java \
 src/test/java/org/littleshoot/proxy/HttpFilterTest.java \
 src/test/java/org/littleshoot/proxy/KeepAliveTest.java \
 src/test/java/org/littleshoot/proxy/MessageTerminationTest.java \
 src/test/java/org/littleshoot/proxy/ProxyHeadersTest.java \
 src/test/java/org/littleshoot/proxy/ServerGroupTest.java \
 src/test/java/org/littleshoot/proxy/TimeoutTest.java

# NoClassDefFoundError: org/jctools/queues/SpscLinkedQueue
%pom_add_dep org.jctools:jctools-core:1.2.1:test

# Connection refused: /127.0.0.1:0
rm src/test/java/org/littleshoot/proxy/ChainedProxyWithFallbackTest.java \
 src/test/java/org/littleshoot/proxy/ChainedProxyWithFallbackToDirectDueToSSLTest.java \
 src/test/java/org/littleshoot/proxy/ChainedProxyWithFallbackToOtherChainedProxyDueToSSLTest.java \
 src/test/java/org/littleshoot/proxy/ClientAuthenticationNotRequiredTCPChainedProxyTest.java \
 src/test/java/org/littleshoot/proxy/EncryptedTCPChainedProxyTest.java \
 src/test/java/org/littleshoot/proxy/MitmProxyTest.java \
 src/test/java/org/littleshoot/proxy/MITMUsernamePasswordAuthenticatingProxyTest.java \
 src/test/java/org/littleshoot/proxy/MitmWithChainedProxyTest.java \
 src/test/java/org/littleshoot/proxy/MitmWithClientAuthenticationNotRequiredTCPChainedProxyTest.java \
 src/test/java/org/littleshoot/proxy/MitmWithEncryptedTCPChainedProxyTest.java \
 src/test/java/org/littleshoot/proxy/MitmWithUnencryptedTCPChainedProxyTest.java \
 src/test/java/org/littleshoot/proxy/SimpleProxyTest.java \
 src/test/java/org/littleshoot/proxy/UnencryptedTCPChainedProxyTest.java \
 src/test/java/org/littleshoot/proxy/UsernamePasswordAuthenticatingProxyTest.java \
 src/test/java/org/littleshoot/proxy/MitmWithBadServerAuthenticationTCPChainedProxyTest.java \
 src/test/java/org/littleshoot/proxy/MitmWithBadClientAuthenticationTCPChainedProxyTest.java

# @ random fails with: Socket Too many open files
rm src/test/java/org/littleshoot/proxy/IdleTest.java

%mvn_file :%{name} %{name}

%build

%mvn_build -- -Dmaven.test.skip.exec=true

%install
%mvn_install

%files -f .mfiles
%doc README.md
%doc COPYRIGHT.txt LICENSE.txt

%files javadoc -f .mfiles-javadoc
%doc COPYRIGHT.txt LICENSE.txt

%changelog
* Fri Nov 17 2017 Igor Vlasenko <viy@altlinux.ru> 1.1.0-alt2_2jpp8
- fixed build with new jctools

* Thu Nov 09 2017 Igor Vlasenko <viy@altlinux.ru> 1.1.0-alt1_2jpp8
- fc27 update

* Wed Oct 18 2017 Igor Vlasenko <viy@altlinux.ru> 1.1.0-alt1_1jpp8
- new jpp release

* Fri Dec 16 2016 Igor Vlasenko <viy@altlinux.ru> 0.5.3-alt1_3jpp8
- new fc release

* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 0.5.3-alt1_2jpp8
- new fc release

* Mon Feb 08 2016 Igor Vlasenko <viy@altlinux.ru> 0.5.3-alt1_1jpp8
- new version

* Mon Sep 08 2014 Igor Vlasenko <viy@altlinux.ru> 0.4-alt1_6jpp7
- new release

* Mon Jul 28 2014 Igor Vlasenko <viy@altlinux.ru> 0.4-alt1_4jpp7
- new release

* Mon Oct 01 2012 Igor Vlasenko <viy@altlinux.ru> 0.4-alt1_2jpp7
- new version

