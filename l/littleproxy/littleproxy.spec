Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-java
# END SourceDeps(oneline)
%filter_from_requires /^java-headless/d
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
Name:          littleproxy
Version:       0.5.3
Release:       alt1_2jpp8
Summary:       High Performance HTTP Proxy
License:       ASL 2.0
URL:           http://www.littleshoot.org/littleproxy/
Source0:       https://github.com/adamfisk/LittleProxy/archive/%{name}-%{version}.tar.gz

BuildRequires: maven-local
BuildRequires: mvn(com.google.guava:guava)
BuildRequires: mvn(commons-cli:commons-cli)
BuildRequires: mvn(commons-codec:commons-codec)
BuildRequires: mvn(commons-io:commons-io)
BuildRequires: mvn(io.netty:netty:3)
BuildRequires: mvn(javax.servlet:javax.servlet-api)
BuildRequires: mvn(junit:junit)
BuildRequires: mvn(log4j:log4j:1.2.17)
BuildRequires: mvn(org.apache.commons:commons-lang3)
BuildRequires: mvn(org.apache.httpcomponents:httpclient)
BuildRequires: mvn(org.apache.maven.plugins:maven-enforcer-plugin)
BuildRequires: mvn(org.eclipse.jetty:jetty-server:8.1.17.v20150415)
BuildRequires: mvn(org.littleshoot:dnssec4j)
BuildRequires: mvn(org.mockito:mockito-all)
BuildRequires: mvn(org.slf4j:slf4j-api)
BuildRequires: mvn(org.slf4j:slf4j-log4j12)
BuildRequires: mvn(org.sonatype.oss:oss-parent:pom:)
%if 0
# Not available test dep
BuildRequires: mvn(org.seleniumhq.selenium:selenium-java:2.28.0)
%endif

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
#%% patch0 -p1

# Unavailable plugins
%pom_remove_plugin org.sonatype.plugins:nexus-staging-maven-plugin
%pom_remove_plugin org.apache.maven.plugins:maven-site-plugin
# 8.1.14.v20131031 8.1.17.v20150415
%pom_xpath_set "pom:dependency[pom:artifactId = 'jetty-server']/pom:version" 8.1.17.v20150415
%pom_xpath_inject "pom:dependency[pom:artifactId = 'jetty-server']" "
<exclusions>
    <exclusion>
    <groupId>org.eclipse.jetty.orbit</groupId>
    <artifactId>javax.servlet</artifactId>
    </exclusion>
</exclusions>"

%pom_xpath_set "pom:dependency[pom:artifactId = 'netty']/pom:version" 3

%pom_remove_dep org.seleniumhq.selenium:selenium-java
rm -r src/test/java/org/littleshoot/proxy/EndToEndStoppingTest.java

%pom_add_dep javax.servlet:javax.servlet-api:3.1.0:test

# Use web connection
rm -r src/test/java/org/littleshoot/proxy/HttpProxyTest.java
# NoClassDefFoundError: Could not initialize class org.littleshoot.proxy.ProxyUtils
rm -r src/test/java/org/littleshoot/proxy/HttpFilterTest.java \
 src/test/java/org/littleshoot/proxy/ProxyChainTest.java \
 src/test/java/org/littleshoot/proxy/ProxyUtilsTest.java \
 src/test/java/org/littleshoot/proxy/RegexHttpRequestFilterTest.java

%mvn_file :%{name} %{name}

%build

%mvn_build

%install
%mvn_install

%files -f .mfiles
%doc README.md
%doc COPYRIGHT.txt LICENSE.txt

%files javadoc -f .mfiles-javadoc
%doc COPYRIGHT.txt LICENSE.txt

%changelog
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

