BuildRequires: /proc
BuildRequires: jpackage-compat
Name:           netty
Version:        3.6.6
Release:        alt1_2jpp7
Summary:        An asynchronous event-driven network application framework and tools for Java

Group:          Development/Java
License:        ASL 2.0
URL:            https://netty.io/
Source0:        http://%{name}.googlecode.com/files/%{name}-%{version}.Final-dist.tar.bz2
Patch0:         %{name}-port-to-jzlib-1.1.0.patch

BuildArch:      noarch

BuildRequires:  maven-local
BuildRequires:  maven-antrun-plugin
BuildRequires:  maven-assembly-plugin
BuildRequires:  maven-compiler-plugin
BuildRequires:  maven-enforcer-plugin
BuildRequires:  maven-javadoc-plugin
BuildRequires:  maven-plugin-bundle
BuildRequires:  maven-resources-plugin
BuildRequires:  maven-source-plugin
BuildRequires:  maven-surefire-plugin
BuildRequires:  ant-contrib

BuildRequires:  felix-osgi-compendium
BuildRequires:  felix-osgi-core
BuildRequires:  jboss-logging
BuildRequires:  jboss-marshalling
BuildRequires:  protobuf-java
BuildRequires:  slf4j
BuildRequires:  sonatype-oss-parent
BuildRequires:  tomcat-servlet-3.0-api
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
BuildArch: noarch

%description javadoc
%{summary}.

%prep
%setup -q -n %{name}-%{version}.Final
# just to be sure, but not used anyway
rm -rf jar doc license

%pom_remove_plugin :maven-jxr-plugin
%pom_remove_plugin :maven-checkstyle-plugin
%pom_remove_plugin org.eclipse.m2e:lifecycle-mapping
%pom_remove_dep javax.activation:activation
%pom_remove_plugin :animal-sniffer-maven-plugin
%pom_xpath_remove "pom:execution[pom:id[text()='remove-examples']]"
%pom_xpath_remove "pom:plugin[pom:artifactId[text()='maven-javadoc-plugin']]/pom:configuration"
# Set scope of optional compile dependencies to 'provided'
%pom_xpath_set "pom:dependency[pom:scope[text()='compile']
	       and pom:optional[text()='true']]/pom:scope" provided

sed s/jboss-logging-spi/jboss-logging/ -i pom.xml

# Remove bundled jzlib and use system jzlib
rm -rf src/main/java/org/jboss/netty/util/internal/jzlib
%pom_add_dep com.jcraft:jzlib
sed -i s/org.jboss.netty.util.internal.jzlib/com.jcraft.jzlib/ \
    $(find src/main/java/org/jboss/netty/handler/codec -name \*.java | sort -u)
%patch0 -p1

%build
%mvn_alias : org.jboss.netty:
%mvn_file  : %{name}
# skipping tests because we don't have easymockclassextension
%mvn_build -f

%install
%mvn_install

%files -f .mfiles
%doc LICENSE.txt NOTICE.txt

%files javadoc -f .mfiles-javadoc
%doc LICENSE.txt NOTICE.txt

%changelog
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

