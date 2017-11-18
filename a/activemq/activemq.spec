BuildRequires: apache-parent
Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-java
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Name:          activemq
Version:       5.6.0
Release:       alt3_18jpp8
Summary:       Open source messaging and Integration Patterns server
License:       ASL 2.0
URL:           http://activemq.apache.org
# git clone -b activemq-5.6.0 https://github.com/apache/activemq.git activemq-core-5.6.0
# rm -rf activemq-core-5.6.0/.git
# tar cJf activemq-core-5.6.0.tar.xz activemq-core-5.6.0
Source0:       activemq-5.6.0.tar.xz

Patch0:        activemq-5.6.0-jaas-CVE-2015-6524.patch
Patch1:        activemq-5.6.0-CVE-2015-5254.patch

BuildRequires: maven-local
BuildRequires: mvn(com.thoughtworks.xstream:xstream)
BuildRequires: mvn(commons-net:commons-net)
BuildRequires: mvn(org.apache.derby:derby)
BuildRequires: mvn(org.apache.activemq:activeio-core)
BuildRequires: mvn(org.apache.activemq.protobuf:activemq-protobuf)
BuildRequires: mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires: mvn(org.apache.geronimo.specs:geronimo-jms_1.1_spec)
BuildRequires: mvn(org.apache.geronimo.specs:geronimo-jta_1.1_spec)
BuildRequires: mvn(org.apache.maven.plugins:maven-antrun-plugin)
BuildRequires: mvn(org.apache.maven.plugins:maven-clean-plugin)
BuildRequires: mvn(org.apache.maven.plugins:maven-enforcer-plugin)
BuildRequires: mvn(org.apache.rat:apache-rat-plugin)
BuildRequires: mvn(org.apache.xbean:maven-xbean-plugin)
BuildRequires: mvn(org.codehaus.jettison:jettison)
BuildRequires: mvn(org.codehaus.mojo:javacc-maven-plugin)
BuildRequires: mvn(org.jasypt:jasypt)
BuildRequires: mvn(org.springframework:spring-jms)

BuildArch:     noarch
Source44: import.info

%description
The most popular and powerful open source messaging and Integration Patterns
server.

%package core
Group: Development/Java
Summary:       ActiveMQ Core

%description core
ActiveMQ Core Library.

%package jaas
Group: Development/Java
Summary:       ActiveMQ Jaas

%description jaas
ActiveMQ Jaas Library.

%package kahadb
Group: Development/Java
Summary:       ActiveMQ KahaDB

%description kahadb
A file based persistence database that is local to the message broker that
is using it. It has been optimized for fast persistence and is the the default
storage mechanism from ActiveMQ 5.4 onwards. KahaDB uses less file descriptors
and provides faster recovery than its predecessor, the AMQ Message Store.

%package javadoc
Group: Development/Java
Summary:       Javadoc for %{name}
BuildArch: noarch

%description javadoc
This package contains javadoc for %{name}.

%prep

%setup -q -n %{name}-%{version}
%patch0 -p1
%patch1 -p1

# Disable modules
for m in all camel console fileserver blueprint karaf \
    openwire-generator optional pool ra rar run spring \
    tooling web web-demo web-console xmpp jmdns_1.0
do
    %pom_disable_module %{name}-${m}
done

%pom_disable_module assembly

# Remove missing plugin for activemq-core
%pom_remove_dep xsddoc:maven-xsddoc-plugin %{name}-core/pom.xml

# Remove missing plugin
%pom_remove_plugin org.codehaus.mojo:ianal-maven-plugin
%pom_remove_plugin -r :cobertura-maven-plugin
# Workaround for new bundle plugin
%pom_xpath_remove "pom:plugin[pom:artifactId = 'maven-bundle-plugin' ]/pom:configuration"

# Remove missing test dependencies
%pom_remove_dep org.springframework:spring-test

# Remove missing optional dependencies
%pom_remove_dep org.apache.geronimo.specs:geronimo-j2ee-management_1.1_spec

# Remove jmdns support
rm -rf %{name}-core/src/main/java/org/apache/activemq/transport/discovery/zeroconf
%pom_remove_dep org.apache.activemq:activemq-jmdns_1.0 %{name}-core/pom.xml

# Remove leveldb support
rm -rf %{name}-core/src/main/java/org/apache/activemq/store/leveldb
%pom_remove_dep org.fusesource.fuse-extra:fusemq-leveldb %{name}-core/pom.xml

# Remove mqtt support
rm -rf %{name}-core/src/main/java/org/apache/activemq/transport/mqtt
%pom_remove_dep org.fusesource.mqtt-client:mqtt-client %{name}-core/pom.xml

# Remove other optional dependencies
%pom_remove_dep org.apache.activemq:activemq-openwire-generator %{name}-core/pom.xml
%pom_remove_dep org.apache.geronimo.specs:geronimo-j2ee-management_1.1_spec %{name}-core/pom.xml
%pom_remove_dep org.apache.geronimo.specs:geronimo-jta_1.0.1B_spec %{name}-core/pom.xml
%pom_remove_dep org.apache.geronimo.specs:geronimo-jacc_1.1_spec %{name}-core/pom.xml
%pom_remove_dep org.apache.geronimo.specs:geronimo-annotation_1.0_spec %{name}-core/pom.xml

chmod 644 LICENSE README.txt

# Fix license file encoding
mv LICENSE LICENSE.orig
iconv -f iso-8859-1 -t utf-8 LICENSE.orig > LICENSE

%mvn_package ":activemq-core:{xsd}::" __noinstall

%build
%mvn_build -sf

%install
%mvn_install

%files -f .mfiles-activemq-parent
%doc README.txt
%doc LICENSE NOTICE

%files core -f .mfiles-activemq-core
%doc LICENSE NOTICE

%files jaas -f .mfiles-activemq-jaas
%doc LICENSE NOTICE

%files kahadb -f .mfiles-kahadb
%doc LICENSE NOTICE

%files javadoc -f .mfiles-javadoc
%doc LICENSE NOTICE

%changelog
* Sat Nov 18 2017 Igor Vlasenko <viy@altlinux.ru> 5.6.0-alt3_18jpp8
- added BR: apache-parent for javapackages 5

* Sun Oct 22 2017 Igor Vlasenko <viy@altlinux.ru> 5.6.0-alt2_18jpp8
- new jpp release

* Fri Dec 16 2016 Igor Vlasenko <viy@altlinux.ru> 5.6.0-alt2_17jpp8
- new fc release

* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 5.6.0-alt2_15jpp8
- new fc release

* Mon Feb 08 2016 Igor Vlasenko <viy@altlinux.ru> 5.6.0-alt2_12jpp8
- new version

* Thu Aug 07 2014 Igor Vlasenko <viy@altlinux.ru> 5.6.0-alt2_5jpp7
- rebuild with maven-local

* Mon Jul 28 2014 Igor Vlasenko <viy@altlinux.ru> 5.6.0-alt1_5jpp7
- new release

* Mon Oct 01 2012 Igor Vlasenko <viy@altlinux.ru> 5.6.0-alt1_3jpp7
- new version

