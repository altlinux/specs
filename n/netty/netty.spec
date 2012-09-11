BuildRequires: /proc maven-enforcer-plugin
BuildRequires: jpackage-compat
Name:           netty
Version:        3.2.4
Release:        alt1_2jpp7
Summary:        An asynchronous event-driven network application framework and tools for Java

Group:          Development/Java
License:        ASL 2.0
URL:            http://www.jboss.org/netty
Source0:        http://sourceforge.net/projects/jboss/files/%{name}-%{version}.Final-dist.tar.bz2

Patch0:         0001-Remove-optional-deps.patch
Patch1:         0002-Replace-jboss-logger-with-jdk-logger.patch
Patch2:         0003-Fix-javadoc-plugin-configuration.patch
Patch3:         0004-Remove-antun-execution-for-removing-examples.patch

BuildArch:     noarch

# This pulls in all of the required java and maven stuff
BuildRequires:  maven
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

Requires:       protobuf-java
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
%setup -q -n %{name}-%{version}.Final

# just to be sure, but not used anyway
rm -rf jar/

# example doesn't build with our protobuf
rm -rf src/main/java/org/jboss/netty/example/localtime


%patch0 -p1
%patch1 -p1

# we don't have jboss logging facilites so we replace it with jdk logger
rm src/main/java/org/jboss/netty/logging/JBossLogger*.java
%patch2 -p1
%patch3 -p1

%build
# skipping tests because we don't have all dependencies in Fedora
mvn-rpmbuild -Dmaven.test.skip=true \
        install javadoc:javadoc


%install
install -d -m 755 $RPM_BUILD_ROOT%{_javadir}

install -m 644 target/%{name}-%{version}.Final.jar \
  $RPM_BUILD_ROOT%{_javadir}/%{name}.jar


install -d -m 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}
cp -pr target/site/apidocs/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}

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
* Tue Sep 11 2012 Igor Vlasenko <viy@altlinux.ru> 3.2.4-alt1_2jpp7
- complete build

* Wed Mar 07 2012 Igor Vlasenko <viy@altlinux.ru> 3.2.4-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

