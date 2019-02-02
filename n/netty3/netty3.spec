Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires: rpm-build-java
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
# %%version is ahead of its definition. Predefining for rpm 4.0 compatibility.
%define version 3.10.6
%global namedreltag .Final
%global namedversion %{version}%{?namedreltag}

Name:           netty3
Version:        3.10.6
Release:        alt2_5jpp8
Summary:        An asynchronous event-driven network application framework and tools for Java
# CC0: src/main/java/org/jboss/netty/handler/codec/base64/Base64.java
License:        ASL 2.0 and BSD and CC0
URL:            http://netty.io/
Source0:        https://github.com/netty/netty/archive/netty-%{namedversion}.tar.gz

Patch0:         netty-3.10.6-port-to-jzlib-1.1.0.patch
Patch1:         disableNPN.patch

BuildArch:      noarch

BuildRequires:  maven-local
BuildRequires:  mvn(ant-contrib:ant-contrib)
BuildRequires:  mvn(com.google.protobuf:protobuf-java)
BuildRequires:  mvn(com.jcraft:jzlib)
BuildRequires:  mvn(commons-logging:commons-logging)
#BuildRequires:  mvn(io.netty:netty-tcnative)
BuildRequires:  mvn(javax.servlet:javax.servlet-api)
BuildRequires:  mvn(log4j:log4j:12)
BuildRequires:  mvn(org.apache.ant:ant)
BuildRequires:  mvn(org.apache.ant:ant-launcher)
BuildRequires:  mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires:  mvn(org.apache.felix:org.osgi.compendium)
BuildRequires:  mvn(org.apache.felix:org.osgi.core)
BuildRequires:  mvn(org.apache.maven.plugins:maven-antrun-plugin)
BuildRequires:  mvn(org.apache.maven.plugins:maven-enforcer-plugin)
BuildRequires:  mvn(org.apache.maven.plugins:maven-resources-plugin)
BuildRequires:  mvn(org.bouncycastle:bcpkix-jdk15on)
BuildRequires:  mvn(org.jboss.logging:jboss-logging)
BuildRequires:  mvn(org.jboss.marshalling:jboss-marshalling)
BuildRequires:  mvn(org.slf4j:slf4j-api)
BuildRequires:  mvn(org.sonatype.oss:oss-parent:pom:)

#Requires:       netty-tcnative
# src/main/java/org/jboss/netty/handler/codec/base64/Base64.java (unkown version)
Provides:       bundled(java-base64)
Source44: import.info

# mvn install:install-file -Dfile=../SOURCES/netty-tcnative.jar  -DgroupId=io.netty -DartifactId=netty-tcnative -Dversion=1.1.30.Fork2 -Dpackaging=jar
Source21: m2-build-repo-add-netty-tcnative.tar

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

# just to be sure, but not used anyway
rm -rf jar doc license

%pom_remove_plugin :maven-jxr-plugin
%pom_remove_plugin :maven-checkstyle-plugin
%pom_remove_plugin org.eclipse.m2e:lifecycle-mapping
%pom_remove_dep javax.activation:activation
%pom_remove_plugin :animal-sniffer-maven-plugin
%pom_remove_dep :npn-api
%pom_xpath_remove "pom:extension[pom:artifactId[text()='os-maven-plugin']]"
%pom_xpath_remove "pom:execution[pom:id[text()='remove-examples']]"
%pom_xpath_remove "pom:plugin[pom:artifactId[text()='maven-javadoc-plugin']]/pom:configuration"
%pom_xpath_remove "pom:dependency[pom:artifactId[text()='netty-tcnative']]/pom:classifier"
#%% pom_xpath_remove "pom:dependency[pom:artifactId[text()='netty-tcnative']]/pom:scope"
# Set scope of optional compile dependencies to 'provided'
%pom_xpath_set "pom:dependency[pom:scope[text()='compile'] and pom:optional[text()='true']]/pom:scope" provided

# Force use servlet 3.1 apis
%pom_change_dep :servlet-api javax.servlet:javax.servlet-api:3.1.0

%pom_xpath_set "pom:dependency[pom:artifactId = 'log4j']/pom:version" 12

# Uneeded tasks
%pom_remove_plugin :maven-assembly-plugin
%pom_remove_plugin :maven-source-plugin
# Unavailable plugin
%pom_remove_plugin kr.motd.maven:exec-maven-plugin
# Fix javadoc doclint
%pom_remove_plugin :maven-javadoc-plugin

sed s/jboss-logging-spi/jboss-logging/ -i pom.xml

# Remove bundled jzlib and use system jzlib
rm -r src/main/java/org/jboss/netty/util/internal/jzlib
%pom_add_dep com.jcraft:jzlib
sed -i s/org.jboss.netty.util.internal.jzlib/com.jcraft.jzlib/ \
    $(find src/main/java/org/jboss/netty/handler/codec -name \*.java | sort -u)
%patch0 -p1
%patch1 -p1

# adapting to excluded dep
rm -v src/main/java/org/jboss/netty/handler/ssl/JettyNpnSslEngine.java

%mvn_compat_version : %{version} 3.9.3 %{namedversion} 3.9.3.Final 3
%mvn_alias : org.jboss.netty:
%mvn_file  : %{name}

tar -x -C ~ -f %SOURCE21

%build

# skipping tests because we don't have easymockclassextension
%mvn_build -f

%install
%mvn_install

%files -f .mfiles
%doc README.md
%doc --no-dereference LICENSE.txt NOTICE.txt

%files javadoc -f .mfiles-javadoc
%doc --no-dereference LICENSE.txt NOTICE.txt
 
%changelog
* Sat Feb 02 2019 Igor Vlasenko <viy@altlinux.ru> 3.10.6-alt2_5jpp8
- fixed build

* Tue Jan 29 2019 Igor Vlasenko <viy@altlinux.ru> 3.10.6-alt1_5jpp8
- built w/o netty-tcnative

* Thu May 31 2018 Igor Vlasenko <viy@altlinux.ru> 3.10.6-alt1_4jpp8
- java update

* Sat Nov 04 2017 Igor Vlasenko <viy@altlinux.ru> 3.10.6-alt1_3jpp8
- new version

* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 3.9.3-alt1_4jpp8
- new fc release

* Thu Feb 11 2016 Igor Vlasenko <viy@altlinux.ru> 3.9.3-alt1_3jpp8
- full build

* Sat Jan 30 2016 Igor Vlasenko <viy@altlinux.ru> 3.9.3-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

