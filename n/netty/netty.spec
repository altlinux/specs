Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-java
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
# %%version is ahead of its definition. Predefining for rpm 4.0 compatibility.
%define version 4.0.42
# Disable generation of debuginfo package
%global debug_package %{nil}
%global namedreltag .Final
%global namedversion %{version}%{?namedreltag}

Name:           netty
Version:        4.0.42
Release:        alt1_2jpp8
Summary:        An asynchronous event-driven network application framework and tools for Java
License:        ASL 2.0
URL:            https://netty.io/
Source0:        https://github.com/netty/netty/archive/netty-%{namedversion}.tar.gz
Patch0:         0001-Remove-OpenSSL-parts-depending-on-tcnative.patch
Patch1:         0002-Remove-NPN-ALPN.patch

BuildRequires:  maven-local
BuildRequires:  mvn(ant-contrib:ant-contrib)
BuildRequires:  mvn(com.google.protobuf:protobuf-java)
BuildRequires:  mvn(com.jcraft:jzlib)
BuildRequires:  mvn(commons-logging:commons-logging)
BuildRequires:  mvn(kr.motd.maven:os-maven-plugin)
BuildRequires:  mvn(log4j:log4j:1.2.17)
BuildRequires:  mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires:  mvn(org.apache.logging.log4j:log4j-api)
BuildRequires:  mvn(org.apache.maven.plugins:maven-antrun-plugin)
BuildRequires:  mvn(org.apache.maven.plugins:maven-dependency-plugin)
BuildRequires:  mvn(org.bouncycastle:bcpkix-jdk15on)
BuildRequires:  mvn(org.codehaus.mojo:build-helper-maven-plugin)
BuildRequires:  mvn(org.fusesource.hawtjni:maven-hawtjni-plugin)
BuildRequires:  mvn(org.javassist:javassist)
BuildRequires:  mvn(org.jboss.marshalling:jboss-marshalling)
BuildRequires:  mvn(org.jctools:jctools-core)
BuildRequires:  mvn(org.slf4j:slf4j-api)
BuildRequires:  mvn(org.sonatype.oss:oss-parent:pom:)
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
%pom_disable_module "testsuite-osgi"
%pom_disable_module "tarball"
%pom_disable_module "microbench"
%pom_remove_plugin :maven-checkstyle-plugin
%pom_remove_plugin :animal-sniffer-maven-plugin
%pom_remove_plugin :maven-enforcer-plugin
%pom_remove_plugin :maven-antrun-plugin
%pom_remove_plugin :maven-dependency-plugin
%pom_remove_plugin :maven-shade-plugin
%pom_remove_plugin :maven-shade-plugin common
%pom_remove_plugin :xml-maven-plugin
%pom_remove_plugin -r :maven-release-plugin
%pom_remove_plugin -r :maven-clean-plugin
%pom_remove_plugin -r :maven-source-plugin
%pom_remove_plugin -r :maven-deploy-plugin
%pom_remove_plugin -r :maven-jxr-plugin
# Optional things we don't ship
%pom_remove_dep ":\${tcnative.artifactId}"
%pom_remove_dep ":\${tcnative.artifactId}" handler
%pom_remove_dep "org.eclipse.jetty.npn:npn-api"
%pom_remove_dep "org.eclipse.jetty.npn:npn-api" handler
%pom_remove_dep "org.eclipse.jetty.alpn:alpn-api"
%pom_remove_dep "org.eclipse.jetty.alpn:alpn-api" handler

sed -i 's|taskdef|taskdef classpathref="maven.plugin.classpath"|' all/pom.xml

%pom_xpath_inject "pom:plugins/pom:plugin[pom:artifactId = 'maven-antrun-plugin']" '<dependencies><dependency><groupId>ant-contrib</groupId><artifactId>ant-contrib</artifactId><version>1.0b3</version></dependency></dependencies>' all/pom.xml
%pom_xpath_inject "pom:execution[pom:id = 'build-native-lib']/pom:configuration" '<verbose>true</verbose>' transport-native-epoll/pom.xml

# Upstream has jctools bundled.
%pom_xpath_set "pom:build/pom:plugins/pom:plugin[pom:artifactId = 'maven-bundle-plugin']/pom:executions/pom:execution[pom:id = 'generate-manifest']/pom:configuration/pom:instructions/pom:Import-Package" 'org.jctools.*,sun.misc;resolution:=optional;*' common/pom.xml

# Tell xmvn to install attached artifact, which it does not
# do by default. In this case install all attached artifacts with
# the linux classifier.
%mvn_package ":::linux*:"

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

