# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-java
BuildRequires: maven
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-compat
%global oname netty

Name:           netty31
Version:        3.1.5
Release:        alt2_5jpp7
Summary:        An asynchronous event-driven network application framework and tools for Java

Group:          Development/Java
License:        ASL 2.0
URL:            https://netty.io/
Source0:        http://sourceforge.net/projects/jboss/files/netty-3.1.5.GA-dist.tar.bz2

# 1) Remove optional xnio dep
# 2) Remove optional spring dep
# 3) Fix google-guice and jboss-logging deps
Patch0:         netty31-dep-fixes.patch
# These plugins break with maven 3, so disable them for now
Patch1:         netty31-disable-doc-plugins.patch
BuildArch:      noarch

# This pulls in all of the required java and maven stuff
BuildRequires:  maven-local
BuildRequires:  maven-antrun-plugin
BuildRequires:  maven-assembly-plugin
BuildRequires:  maven-compiler-plugin
BuildRequires:  maven-eclipse-plugin
BuildRequires:  maven-javadoc-plugin
BuildRequires:  maven-resources-plugin
BuildRequires:  maven-release-plugin
BuildRequires:  maven-source-plugin
BuildRequires:  maven-surefire-plugin
BuildRequires:  maven-plugin-bundle
BuildRequires:  buildnumber-maven-plugin
BuildRequires:  ant-contrib
BuildRequires:  subversion
BuildRequires:  protobuf-java
BuildRequires:  felix-osgi-compendium
BuildRequires:  jboss-parent
BuildRequires:  jboss-logging
BuildRequires:  dos2unix
BuildRequires:  axis
BuildRequires:  apiviz

Requires:       protobuf-java
Requires:       axis
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
Summary:   API documentation for %{name}
Group:     Development/Java
Requires:  jpackage-utils
BuildArch: noarch

%description javadoc
%{summary}.

%prep
%setup -q -n %{oname}-%{version}.GA

# just to be sure, but not used anyway
rm -rf jar/

# example doesn't build with our protobuf
rm -rf src/main/java/org/jboss/netty/example/localtime

# convert the pom file before patching
dos2unix pom.xml LICENSE.txt NOTICE.txt
%patch0 -p1
%patch1 -p1

# XNIO and spring deps are removed from this build
rm -rf src/main/java/org/jboss/netty/container/spring/
rm -rf src/main/java/org/jboss/netty/channel/xnio/

%build
# skipping tests because we don't have all dependencies in Fedora
mvn-rpmbuild -Dmaven.test.skip=true \
        install javadoc:javadoc
dos2unix target/api/stylesheet.css

%install
install -d -m 755 $RPM_BUILD_ROOT%{_javadir}

install -m 644 target/%{oname}-%{version}.GA.jar \
  $RPM_BUILD_ROOT%{_javadir}/%{name}.jar


install -d -m 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}
cp -pr target/api/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}

install -d -m 755 $RPM_BUILD_ROOT%{_mavenpomdir}
install -pm 644 pom.xml $RPM_BUILD_ROOT/%{_mavenpomdir}/JPP-%{name}.pom

%add_maven_depmap JPP-%{name}.pom %{name}.jar

%files
%doc LICENSE.txt NOTICE.txt
%{_javadir}/%{name}.jar
%{_mavendepmapfragdir}/%{name}
%{_mavenpomdir}/JPP-%{name}.pom

%files javadoc
%doc LICENSE.txt NOTICE.txt
%{_javadocdir}/%{name}

%changelog
* Mon Jul 28 2014 Igor Vlasenko <viy@altlinux.ru> 3.1.5-alt2_5jpp7
- new release

* Mon Jul 14 2014 Igor Vlasenko <viy@altlinux.ru> 3.1.5-alt2_3jpp7
- NMU rebuild to move poms and fragments

* Mon Sep 17 2012 Igor Vlasenko <viy@altlinux.ru> 3.1.5-alt1_3jpp7
- new version

