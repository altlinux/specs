Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-java
# END SourceDeps(oneline)
%filter_from_requires /^java-headless/d
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
# %%name or %%version is ahead of its definition. Predefining for rpm 4.0 compatibility.
%define name netty3
%define version 3.9.3
%global namedreltag .Final
%global namedversion %{version}%{?namedreltag}

Name:           netty3
Version:        3.9.3
Release:        alt1_4jpp8
Summary:        An asynchronous event-driven network application framework and tools for Java
License:        ASL 2.0 and BSD
URL:            http://netty.io/
Source0:        http://netty.googlecode.com/files/netty-%{namedversion}-dist.tar.bz2
Patch0:         netty-port-to-jzlib-1.1.0.patch
Patch1:         disableNPN.patch

BuildArch:      noarch

BuildRequires:  maven-local
BuildRequires:  mvn(ant-contrib:ant-contrib)
BuildRequires:  mvn(com.google.protobuf:protobuf-java)
BuildRequires:  mvn(com.jcraft:jzlib)
BuildRequires:  mvn(commons-logging:commons-logging)
BuildRequires:  mvn(io.netty:netty-tcnative)
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

Requires: netty-tcnative
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
%setup -q -n netty-%{namedversion}
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
%pom_xpath_remove "pom:dependency[pom:artifactId[text()='netty-tcnative']]/pom:scope"
# Set scope of optional compile dependencies to 'provided'
%pom_xpath_set "pom:dependency[pom:scope[text()='compile']
	       and pom:optional[text()='true']]/pom:scope" provided

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
rm -rf src/main/java/org/jboss/netty/util/internal/jzlib
%pom_add_dep com.jcraft:jzlib
sed -i s/org.jboss.netty.util.internal.jzlib/com.jcraft.jzlib/ \
    $(find src/main/java/org/jboss/netty/handler/codec -name \*.java | sort -u)
%patch0 -p1
%patch1 -p1

#adapting to excluded dep
 rm -v src/main/java/org/jboss/netty/handler/ssl/JettyNpnSslEngine.java

%mvn_compat_version : %{version} %{namedversion} 3
%mvn_alias : org.jboss.netty:
%mvn_file  : %{name}

%build

# skipping tests because we don't have easymockclassextension
%mvn_build -f

%install
%mvn_install

%files -f .mfiles
%doc README.md
%doc LICENSE.txt NOTICE.txt

%files javadoc -f .mfiles-javadoc
%doc LICENSE.txt NOTICE.txt
 
%changelog
* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 3.9.3-alt1_4jpp8
- new fc release

* Thu Feb 11 2016 Igor Vlasenko <viy@altlinux.ru> 3.9.3-alt1_3jpp8
- full build

* Sat Jan 30 2016 Igor Vlasenko <viy@altlinux.ru> 3.9.3-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

