Group: Development/Java
BuildRequires: /proc rpm-build-java
BuildRequires: jpackage-1.8-compat
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Name:           archaius
Version:        0.7.3
Release:        alt1_9jpp8
Summary:        Library for configuration management API 
License:        ASL 2.0
URL:            https://github.com/Netflix/archaius/wiki
Source0:        https://github.com/Netflix/%{name}/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
Patch0:         archaius.build.gradle.patch
Patch1:         archaius.disable.utf8.tests.patch
BuildArch:      noarch

BuildRequires:  gradle-local
BuildRequires:  mvn(com.fasterxml.jackson.core:jackson-annotations)
BuildRequires:  mvn(com.fasterxml.jackson.core:jackson-core)
BuildRequires:  mvn(com.fasterxml.jackson.core:jackson-databind)
BuildRequires:  mvn(com.google.code.findbugs:jsr305)
BuildRequires:  mvn(com.google.guava:guava)
BuildRequires:  mvn(commons-configuration:commons-configuration)
BuildRequires:  mvn(org.slf4j:slf4j-api)

BuildRequires:  mvn(org.apache.zookeeper:zookeeper)
BuildRequires:  mvn(org.apache.curator:curator-client)
BuildRequires:  mvn(org.apache.curator:curator-recipes)

# For unit tests
BuildRequires:  mvn(log4j:log4j)
BuildRequires:  mvn(org.slf4j:slf4j-simple)
BuildRequires:  mvn(org.slf4j:slf4j-log4j12)
BuildRequires:  mvn(org.apache.derby:derby)
BuildRequires:  mvn(org.apache.curator:curator-test)
Source44: import.info

%description
Archaius is a configuration management library with a focus on Dynamic
Properties sourced from multiple configuration stores.

%package javadoc
Group: Development/Java
Summary: API documentation for %{name}
BuildArch: noarch

%description javadoc
This package provides API documentation for %{name}.

%package core
Group: Development/Java
Summary: Core library of %{name}

Requires:  mvn(com.fasterxml.jackson.core:jackson-annotations)
Requires:  mvn(com.fasterxml.jackson.core:jackson-core)
Requires:  mvn(com.fasterxml.jackson.core:jackson-databind)
Requires:  mvn(com.google.code.findbugs:jsr305)
Requires:  mvn(com.google.guava:guava)
Requires:  mvn(commons-configuration:commons-configuration)
Requires:  mvn(org.slf4j:slf4j-api)

%package zookeeper
Group: Development/Java
Summary: ZooKeeper connection library for %{name}

Requires:  mvn(com.netflix.archaius:archaius-core)
Requires:  mvn(org.apache.zookeeper:zookeeper)
Requires:  mvn(org.apache.curator:curator-client)
Requires:  mvn(org.apache.curator:curator-recipes)

%description core
Core library of %{name}. This package provides the functionality to use system
properties, property files and JMX as configuration source.

%description zookeeper
ZooKeeper connection library for %{name}. This package provides the
functionality to use ZooKeeper as configuration source.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

find . -name '*.jar' ! -name 'classpathTestResources.jar' -delete
find . -name '*.class' -delete

%build core
gradle -s --offline archaius-core:build
gradle -s --offline archaius-zookeeper:build

javadoc -d javadoc -sourcepath archaius-core/src/main/java:archaius-zookeeper/src/main/java -subpackages com.netflix.config -Xdoclint:none

%mvn_artifact com.netflix.archaius:archaius-core:%{version} archaius-core/build/libs/archaius-core.jar
%mvn_artifact com.netflix.archaius:archaius-zookeeper:%{version} archaius-zookeeper/build/libs/archaius-zookeeper.jar

%mvn_package ":archaius-core" core
%mvn_package ":archaius-zookeeper" zookeeper

%install
%mvn_install -J javadoc

%files core -f .mfiles-core
%doc README.md
%doc --no-dereference LICENSE

%files zookeeper -f .mfiles-zookeeper
%doc README.md
%doc --no-dereference LICENSE

%files javadoc -f .mfiles-javadoc
%doc README.md
%doc --no-dereference LICENSE

%changelog
* Sun Sep 29 2019 Igor Vlasenko <viy@altlinux.ru> 0.7.3-alt1_9jpp8
- new version

