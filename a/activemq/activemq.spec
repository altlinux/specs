# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-java
BuildRequires: maven-local
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-compat
Name:          activemq
Version:       5.6.0
Release:       alt2_5jpp7
Summary:       Open source messaging and Integration Patterns server
Group:         Development/Java
License:       ASL 2.0
URL:           http://activemq.apache.org
# git clone -b activemq-5.6.0 https://github.com/apache/activemq.git activemq-core-5.6.0
# rm -rf activemq-core-5.6.0/.git
# tar cJf activemq-core-5.6.0.tar.xz activemq-core-5.6.0
Source0:       activemq-5.6.0.tar.xz

BuildRequires: activeio
BuildRequires: activemq-protobuf
BuildRequires: derby
BuildRequires: geronimo-jta
BuildRequires: jasypt
BuildRequires: javacc-maven-plugin
BuildRequires: jettison
BuildRequires: jpackage-utils
BuildRequires: maven-clean-plugin
BuildRequires: maven-compiler-plugin
BuildRequires: maven-enforcer-plugin
BuildRequires: maven-gpg-plugin
BuildRequires: maven-idea-plugin
BuildRequires: maven-javadoc-plugin
BuildRequires: maven-plugin-cobertura
BuildRequires: maven-pmd-plugin
BuildRequires: maven-release-plugin
BuildRequires: maven-source-plugin
BuildRequires: maven-surefire-plugin
BuildRequires: maven-surefire-provider-junit4
BuildRequires: maven-xbean-plugin
BuildRequires: springframework-jms

# Required for /usr/share/java/activemq directory
Requires: activemq-protobuf

Requires: jpackage-utils

BuildArch: noarch
Source44: import.info


%description
The most popular and powerful open source messaging and Integration Patterns
server.

%package javadoc
Group: Development/Java
Summary: Javadoc for %{name}
Requires: jpackage-utils
BuildArch: noarch

%description javadoc
This package contains javadoc for %{name}

%package core
Group: Development/Java
Summary: ActiveMQ Core
Requires: %{name} = %{version}-%{release}
Requires: %{name}-jaas = %{version}-%{release}
Requires: %{name}-kahadb = %{version}-%{release}
Requires: jpackage-utils
Requires: activemq-protobuf
Requires: activeio
Requires: jettison
Requires: springframework-jms
Requires: geronimo-jta
Requires: derby
Requires: jasypt

%description core
ActiveMQ Core Library

%package jaas
Group: Development/Java
Summary: ActiveMQ Jaas
Requires: %{name} = %{version}-%{release}
Requires: jpackage-utils

%description jaas
ActiveMQ Jaas Library

%package kahadb
Group: Development/Java
Summary: ActiveMQ KahaDB
Requires: %{name} = %{version}-%{release}
Requires: jpackage-utils
Requires: activemq-protobuf
Requires: activeio

%description kahadb
A file based persistence database that is local to the message broker that
is using it. It has been optimized for fast persistence and is the the default
storage mechanism from ActiveMQ 5.4 onwards. KahaDB uses less file descriptors
and provides faster recovery than its predecessor, the AMQ Message Store.

%prep

%setup -q -n %{name}-%{version}

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

# Remove missing test dependencies
%pom_remove_dep org.springframework:spring-test

# Remove missing optional dependencies
%pom_remove_dep org.apache.geronimo.specs:geronimo-j2ee-management_1.1_spec

# Remove xstream support (fedora version is out of date)
rm -rf %{name}-core/src/main/java/org/apache/activemq/transport/stomp
rm -rf %{name}-core/src/main/java/org/apache/activemq/util/XStreamFactoryBean.java
%pom_remove_dep com.thoughtworks.xstream:xstream %{name}-core/pom.xml

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

%build
mvn-rpmbuild -Dmaven.test.skip=true \
    -Dproject.build.sourceEncoding=UTF-8 \
    install javadoc:aggregate

%install

install -d -m 755 %{buildroot}%{_javadir}/%{name}
install -d -m 755 %{buildroot}%{_mavenpomdir}

for m in %{name}-core %{name}-jaas kahadb; do
    install -pm 644 ${m}/target/${m}-%{version}.jar %{buildroot}%{_javadir}/%{name}/${m}.jar
    install -pm 644 ${m}/pom.xml %{buildroot}%{_mavenpomdir}/JPP.%{name}-${m}.pom
    %add_maven_depmap JPP.%{name}-${m}.pom %{name}/${m}.jar
done

# Parent POM
install -pm 644 pom.xml %{buildroot}%{_mavenpomdir}/JPP-%{name}.pom
%add_maven_depmap JPP-%{name}.pom
mkdir -p %{buildroot}%{_javadocdir}/%{name}
cp -rp target/site/apidocs/* %{buildroot}%{_javadocdir}/%{name}

%files
%doc LICENSE NOTICE README.txt
# Not owning /usr/share/java/activemq since it is owned by activemq-protobuf
%{_mavenpomdir}/JPP-%{name}.pom
%{_mavendepmapfragdir}/%{name}

%files javadoc
%doc LICENSE NOTICE
%{_javadocdir}/%{name}

%files core
%doc LICENSE NOTICE
%{_javadir}/%{name}/%{name}-core.jar
%{_mavenpomdir}/JPP.%{name}-%{name}-core.pom

%files jaas
%doc LICENSE NOTICE
%{_javadir}/%{name}/%{name}-jaas.jar
%{_mavenpomdir}/JPP.%{name}-%{name}-jaas.pom

%files kahadb
%doc LICENSE NOTICE
%{_javadir}/%{name}/kahadb.jar
%{_mavenpomdir}/JPP.%{name}-kahadb.pom

%changelog
* Thu Aug 07 2014 Igor Vlasenko <viy@altlinux.ru> 5.6.0-alt2_5jpp7
- rebuild with maven-local

* Mon Jul 28 2014 Igor Vlasenko <viy@altlinux.ru> 5.6.0-alt1_5jpp7
- new release

* Mon Oct 01 2012 Igor Vlasenko <viy@altlinux.ru> 5.6.0-alt1_3jpp7
- new version

