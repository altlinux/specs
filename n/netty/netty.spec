# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-java
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-compat
Name:           netty
Version:        3.5.11
Release:        alt1_1jpp7
Summary:        An asynchronous event-driven network application framework and tools for Java

Group:          Development/Java
License:        ASL 2.0
URL:            https://netty.io/
Source0:        https://github.com/downloads/%{name}/%{name}/%{name}-%{version}.Final-dist.tar.bz2

BuildArch:      noarch

BuildRequires:  maven
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

Requires:       jpackage-utils
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
%%{summary}.

%prep
%setup -q -n %{name}-%{version}.Final
# just to be sure, but not used anyway
rm -rf jar doc license

%pom_xpath_remove "pom:plugin[pom:artifactId[text()='maven-jxr-plugin']]"
%pom_xpath_remove "pom:plugin[pom:artifactId[text()='maven-checkstyle-plugin']]"
%pom_remove_plugin org.eclipse.m2e:lifecycle-mapping
%pom_remove_dep javax.activation:activation
%pom_remove_plugin :animal-sniffer-maven-plugin
%pom_xpath_remove "pom:execution[pom:id[text()='remove-examples']]"
%pom_xpath_remove "pom:plugin[pom:artifactId[text()='maven-javadoc-plugin']]/pom:configuration"

sed s/jboss-logging-spi/jboss-logging/ -i pom.xml

%build
# skipping tests because we don't have easymockclassextension
mvn-rpmbuild -Dmaven.test.skip=true install javadoc:aggregate


%install
install -d -m 755 $RPM_BUILD_ROOT%{_javadir}

install -m 644 target/%{name}-%{version}.Final.jar \
  $RPM_BUILD_ROOT%{_javadir}/%{name}.jar

install -d -m 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}
cp -pr target/site/apidocs/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}

install -d -m 755 $RPM_BUILD_ROOT%{_mavenpomdir}
install -pm 644 pom.xml $RPM_BUILD_ROOT/%{_mavenpomdir}/JPP-%{name}.pom

%add_maven_depmap -a org.jboss.netty:netty JPP-%{name}.pom %{name}.jar

%files
%doc LICENSE.txt NOTICE.txt
%{_javadir}/%{name}.jar
%{_mavendepmapfragdir}/%{name}
%{_mavenpomdir}/JPP-%{name}.pom

%files javadoc
%doc LICENSE.txt NOTICE.txt
%{_javadocdir}/%{name}

%changelog
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

