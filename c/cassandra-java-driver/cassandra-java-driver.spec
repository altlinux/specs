Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires: rpm-build-java
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Name:		cassandra-java-driver
Version:	3.1.4
Release:	alt1_2jpp8
Summary:	DataStax Java Driver for Apache Cassandra
License:	ASL 2.0
URL:		https://github.com/datastax/java-driver
Source0:	https://github.com/datastax/java-driver/archive/%{version}.tar.gz

# added --allow-script-in-comments option to javadoc plugin
# https://bugzilla.redhat.com/show_bug.cgi?id=1417677
Patch0:		%{name}-%{version}-allow-script-in-comments.patch

BuildRequires:	maven-local
BuildRequires:	mvn(io.dropwizard.metrics:metrics-core)
BuildRequires:	mvn(com.fasterxml.jackson.core:jackson-databind)
BuildRequires:	mvn(com.google.guava:guava)
BuildRequires:	mvn(io.netty:netty-handler)
BuildRequires:	mvn(io.netty:netty-transport-native-epoll)
BuildRequires:	mvn(javax.json:javax.json-api)
BuildRequires:	mvn(joda-time:joda-time)
BuildRequires:	mvn(log4j:log4j:1.2.17)
BuildRequires:	mvn(net.jpountz.lz4:lz4)
BuildRequires:	mvn(org.apache.commons:commons-exec)
BuildRequires:	mvn(org.assertj:assertj-core)
BuildRequires:	mvn(org.hdrhistogram:HdrHistogram)
BuildRequires:	mvn(org.mockito:mockito-all)
BuildRequires:	mvn(org.ow2.asm:asm-all)
BuildRequires:	mvn(org.slf4j:slf4j-log4j12)
BuildRequires:	mvn(org.sonatype.oss:oss-parent:pom:)
BuildRequires:	mvn(org.testng:testng)
BuildRequires:	mvn(org.xerial.snappy:snappy-java)
BuildRequires:	mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires:	mvn(com.github.jnr:jnr-ffi)
BuildRequires:	mvn(com.github.jnr:jnr-posix)
BuildRequires:	mvn(org.codehaus.mojo:build-helper-maven-plugin)
BuildRequires:	mvn(org.apache.maven.plugins:maven-failsafe-plugin)
BuildRequires:	mvn(org.apache.felix:org.apache.felix.framework)
# driver-tests stress module dependencies
#BuildRequires:	mvn(net.sf.jopt-simple:jopt-simple)
#BuildRequires:	mvn(com.yammer.metrics:metrics-core) missing
BuildArch:	noarch
Source44: import.info

%description
A driver for Apache Cassandra 1.2+ that works exclusively with the
Cassandra Query Language version 3 (CQL3) and Cassandra's binary protocol.

%package extras
Group: Development/Java
Summary:	DataStax Java Driver for Apache Cassandra - Extras
Requires:	%{name} = %{version}-%{release}

%description extras
Extended functionality for the Java driver.

%package mapping
Group: Development/Java
Summary:	DataStax Java Driver for Apache Cassandra - Object Mapping
Requires:	%{name} = %{version}-%{release}

%description mapping
Object mapper for the DataStax CQL Java Driver.

%package parent
Group: Development/Java
Summary:	DataStax Java Driver for Apache Cassandra - Parent POM

%description parent
Parent POM for the DataStax Java Driver.

%package tests
Group: Development/Java
Summary:	DataStax Java Driver for Apache Cassandra - Tests
Requires:	%{name} = %{version}-%{release}

%description tests
Tests for the DataStax Java Driver.

%package javadoc
Group: Development/Java
Summary:	Javadoc for %{name}
BuildArch: noarch

%description javadoc
This package contains javadoc for %{name}.

%prep
%setup -qn java-driver-%{version}

# allow-script-in-comments.patch
%patch0 -p1

# Unneeded features
%pom_disable_module driver-dist
%pom_disable_module driver-examples
# missing dependency for stress tests
%pom_disable_module stress driver-tests
# Unavailable plugins
%pom_remove_plugin -r :animal-sniffer-maven-plugin:
%pom_remove_plugin -r :clirr-maven-plugin
%pom_remove_plugin -r :license-maven-plugin
# kr.motd.maven:os-maven-plugin:1.4.1.Final
%pom_xpath_remove -r "pom:build/pom:extensions"
# Unwanted tasks
%pom_remove_plugin -r :maven-source-plugin
%pom_remove_plugin -r :maven-release-plugin
%pom_remove_plugin :gmaven-plugin driver-mapping
%pom_xpath_remove "pom:plugin[pom:artifactId='maven-javadoc-plugin']/pom:executions/pom:execution/pom:goals"
# Disable shaded copy of netty artifacts
%pom_remove_plugin -r :maven-shade-plugin driver-core

# remove hidden files from documentation
rm manual/statements/.nav
rm manual/object_mapper/.nav

%mvn_package ":cassandra-driver-tests-parent" tests
%mvn_package ":cassandra-driver-tests-osgi" tests

%build
# Unavailable test dep org.cassandra:java-client:0.11.0 
%mvn_build -fs

%install
%mvn_install

%files -f .mfiles-cassandra-driver-core
%doc README.md changelog faq manual upgrade_guide
%doc LICENSE

%files extras -f .mfiles-cassandra-driver-extras
%files mapping -f .mfiles-cassandra-driver-mapping
%files parent -f .mfiles-cassandra-driver-parent
%doc LICENSE

%files tests -f .mfiles-tests

%files javadoc -f .mfiles-javadoc
%doc LICENSE

%changelog
* Thu Nov 16 2017 Igor Vlasenko <viy@altlinux.ru> 3.1.4-alt1_2jpp8
- new version

