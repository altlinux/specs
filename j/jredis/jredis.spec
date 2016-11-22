Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-java
# END SourceDeps(oneline)
%filter_from_requires /^java-headless/d
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
%global githash 0eed7931ea0aa827fe74dfa808467c16e12d6e96

Name:          jredis
# This release is compatible with newer Redis release
Version:       2.0.0
Release:       alt1_0.2.a.0jpp8
Summary:       Java Client and Connectors for Redis
License:       ASL 2.0
# https://code.google.com/p/jredis/
URL:           https://github.com/alphazero/jredis
Source0:       https://github.com/alphazero/jredis/archive/%{githash}/%{name}-%{githash}.tar.gz

BuildRequires: maven-local
BuildRequires: mvn(commons-logging:commons-logging)
BuildRequires: mvn(log4j:log4j:1.2.17)
BuildRequires: mvn(org.testng:testng)

BuildArch:     noarch
Source44: import.info

%description
JRedis is a high-performance Java client and connector framework and
reference implementation for Redis distributed hash key-value
database. It will provide both synchronous clients and asynchronous
connections for Redis. The connectors will be both passive
(non-threaded) and active, to address deployment scenarios and
usage requirements.

This package contains JRedis Parent POM.

%package core
Group: Development/Java
Summary:       JRedis Core Parent POM

%description core
The Core module is composed of all the core elements that
are used to create JRedis clients and connectors for the
Redis server.  

This includes: 

- the specification (API),
- the reference implementation (RI),
- the benchmark module (BENCH)

This package contains JRedis Core Parent POM.

%package core-api
Group: Development/Java
Summary:       JRedis Core API

%description core-api
JRedis Core Specification API.

%package core-bench
Group: Development/Java
Summary:       JRedis Benchmark Module

%description core-bench
JRedis Benchmark Module.

%package core-ri
Group: Development/Java
Summary:       JRedis Core RI

%description core-ri
JRedis Core Reference Implementation.

%package javadoc
Group: Development/Java
Summary:       Javadoc for %{name}
BuildArch: noarch

%description javadoc
This package contains javadoc for %{name}.

%prep
%setup -q -n %{name}-%{githash}
find . -name "*.class" -delete
find . -name "*.jar" -delete

%pom_disable_module examples
%pom_disable_module all core
%pom_remove_plugin :maven-source-plugin
%pom_remove_plugin -r :maven-assembly-plugin

%pom_xpath_set -r "pom:dependency[pom:artifactId = 'log4j']/pom:version" 1.2.17

%build

# Test suite disabled, because use web connection
%mvn_build -s -f -- -Dproject.build.sourceEncoding=UTF-8

%install
%mvn_install

%files -f .mfiles-%{name}
%doc documentation/design/*
%doc LICENSE NOTICE

%files core -f .mfiles-%{name}-core
%doc core/README
%doc core/LICENSE core/NOTICE

%files core-api -f .mfiles-%{name}-core-api
%doc README RELEASE-NOTES.txt
%doc core/api/LICENSE core/api/NOTICE

%files core-bench -f .mfiles-%{name}-core-bench
%doc core/bench/LICENSE core/bench/NOTICE

%files core-ri -f .mfiles-%{name}-core-ri
%doc core/ri/LICENSE core/ri/NOTICE
 
%files javadoc -f .mfiles-javadoc
%doc LICENSE NOTICE

%changelog
* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 2.0.0-alt1_0.2.a.0jpp8
- new fc release

* Thu Feb 11 2016 Igor Vlasenko <viy@altlinux.ru> 2.0.0-alt1_0.1.a.0jpp8
- new version

