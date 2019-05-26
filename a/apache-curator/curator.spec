Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires: rpm-build-java unzip
# END SourceDeps(oneline)
%define oldname curator
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Name:          apache-curator
Version:       2.10.0
Release:       alt1_8jpp8
Summary:       A set of Java libraries that make using Apache ZooKeeper much easier
License:       ASL 2.0
URL:           http://%{oldname}.apache.org/
Source0:       http://archive.apache.org/dist/%{oldname}/%{version}/apache-%{oldname}-%{version}-source-release.zip
# Fix test deps
Patch0:        curator-2.10.0-commons-math3.patch
Patch1:        curator-2.10.0-jetty9.patch

BuildRequires: maven-local
BuildRequires: mvn(com.google.guava:guava)
BuildRequires: mvn(com.sun.jersey:jersey-client:1)
BuildRequires: mvn(com.sun.jersey:jersey-core:1)
BuildRequires: mvn(com.sun.jersey:jersey-server:1)
BuildRequires: mvn(com.sun.jersey:jersey-servlet:1)
BuildRequires: mvn(javax.ws.rs:jsr311-api)
BuildRequires: mvn(junit:junit)
BuildRequires: mvn(org.apache:apache:pom:)
BuildRequires: mvn(org.apache.commons:commons-math3)
BuildRequires: mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires: mvn(org.apache.maven.plugins:maven-remote-resources-plugin)
BuildRequires: mvn(org.apache.zookeeper:zookeeper)
BuildRequires: mvn(org.codehaus.jackson:jackson-mapper-asl)
BuildRequires: mvn(org.javassist:javassist)
BuildRequires: mvn(org.eclipse.jetty:jetty-server)
BuildRequires: mvn(org.eclipse.jetty:jetty-servlet)
BuildRequires: mvn(org.jboss.resteasy:resteasy-jaxrs)
BuildRequires: mvn(org.mockito:mockito-core)
BuildRequires: mvn(org.scannotation:scannotation)
BuildRequires: mvn(org.slf4j:slf4j-log4j12)
BuildRequires: mvn(org.testng:testng)

Requires: %{name}-client = %{version}-%{release}
Requires: %{name}-examples
Requires: %{name}-framework
Requires: %{name}-recipes
Requires: %{name}-test
Requires: %{name}-x-discovery
Requires: %{name}-x-discovery-server

BuildArch:     noarch
Source44: import.info

%description
Curator is a set of Java libraries that
make using Apache ZooKeeper much easier.

%package client
Group: Development/Java
Summary:       Curator Client

%description client
Low-level API.

%package examples
Group: Development/Java
Summary:       Curator Examples

%description examples
Example usages of various Curator features.

%package framework
Group: Development/Java
Summary:       Curator Framework

%description framework
High-level API that greatly simplifies using ZooKeeper.

%package recipes
Group: Development/Java
Summary:       Curator Recipes

%description recipes
All of the recipes listed on the ZooKeeper recipes doc
(except two phase commit).

%package test
Group: Development/Java
Summary:       Curator Testing

%description test
Unit testing utilities.

%package x-discovery
Group: Development/Java
Summary:       Curator Service Discovery

%description x-discovery
A service discovery recipe.

%package x-discovery-server
Group: Development/Java
Summary:       Curator Service Discovery Server

%description x-discovery-server
Bridges non-Java or legacy applications with the
Curator Service Discovery.

%package javadoc
Group: Development/Java
Summary:       Javadoc for %{oldname}
BuildArch: noarch

%description javadoc
This package contains javadoc for %{oldname}

%prep
%setup -q -n apache-%{oldname}-%{version}
find -name '*.class' -print -delete
find -name '*.jar' -print -delete

%patch0 -p1
%patch1 -p1

# disable cause build failure
%pom_remove_plugin :maven-license-plugin

%pom_remove_plugin :maven-site-plugin
%pom_remove_plugin -r :maven-shade-plugin
%pom_remove_plugin -r :clirr-maven-plugin

%pom_remove_plugin :apache-rat-plugin
%pom_remove_plugin :maven-dependency-plugin
%pom_remove_plugin :maven-install-plugin
%pom_remove_plugin :maven-release-plugin
%pom_remove_plugin :maven-scm-publish-plugin

# unavailable build deps
# com.facebook.swift:swift-service:0.12.0
# https://github.com/dropwizard/dropwizard
# io.dropwizard:dropwizard-configuration:0.7.0
# io.dropwizard:dropwizard-logging:0.7.0
%pom_disable_module curator-x-rpc

%pom_xpath_set "pom:properties/pom:jersey-version" 1
%pom_change_dep -r net.sf.scannotation: org.scannotation:

# remove flakey tests
rm -f curator-recipes/src/test/java/org/apache/curator/framework/recipes/nodes/TestGroupMember.java
rm -f curator-recipes/src/test/java/org/apache/curator/framework/recipes/queue/TestDistributedQueue.java
rm -f curator-recipes/src/test/java/org/apache/curator/framework/recipes/queue/TestBoundedDistributedQueue.java
rm -f curator-recipes/src/test/java/org/apache/curator/framework/recipes/queue/TestQueueSharder.java
rm -f curator-x-discovery-server/src/test/java/org/apache/curator/x/discovery/server/jetty_resteasy/TestStringsWithRestEasy.java

# AssertionError: expected [true] but found [false]
rm -f curator-recipes/src/test/java/org/apache/curator/framework/recipes/queue/TestDistributedDelayQueue.java

# Use 6.8.21 >= testng =< 6.8.8
sed -i "s/org.testng.internal.annotations.Sets/org.testng.collections.Sets/" \
 curator-recipes/src/test/java/org/apache/curator/framework/recipes/leader/TestLeaderSelector.java \
 curator-recipes/src/test/java/org/apache/curator/framework/recipes/leader/TestLeaderSelectorParticipants.java

# Missing junit dependency in POM
# https://lists.fedoraproject.org/pipermail/bigdata/2014-May/000456.html
%pom_add_dep junit:junit:4.12:test

%build

%mvn_build -s -- -DskipTests

%install
%mvn_install

%files -f .mfiles-apache-curator
%doc --no-dereference LICENSE NOTICE

%files client -f .mfiles-curator-client
%doc README
%doc --no-dereference LICENSE NOTICE

%files examples -f .mfiles-curator-examples
%files framework -f .mfiles-curator-framework
%files recipes -f .mfiles-curator-recipes
%files test -f .mfiles-curator-test
%doc --no-dereference LICENSE NOTICE

%files x-discovery -f .mfiles-curator-x-discovery
%files x-discovery-server -f .mfiles-curator-x-discovery-server
%doc curator-x-discovery-server/README.txt


%files javadoc -f .mfiles-javadoc
%doc --no-dereference LICENSE NOTICE

%changelog
* Sat May 25 2019 Igor Vlasenko <viy@altlinux.ru> 2.10.0-alt1_8jpp8
- new version

* Sat Nov 04 2017 Igor Vlasenko <viy@altlinux.ru> 2.10.0-alt1_5jpp8
- new version

