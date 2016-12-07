Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-java
# END SourceDeps(oneline)
%filter_from_requires /^java-headless/d
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
Name:          metrics
Version:       3.1.2
Release:       alt1_3jpp8
Summary:       Java library which gives you what your code does in production
License:       ASL 2.0
URL:           http://metrics.dropwizard.io
Source0:       https://github.com/dropwizard/metrics/archive/v%{version}.tar.gz
# Add rabbitmq-java-client 3.5.x support
Patch0:        metrics-3.1.2-amqp-client35.patch
# Use ehcache-core instead of net.sf.ehcache:ehcache:2.8.3
Patch1:        metrics-3.1.2-ehcache-core.patch

BuildRequires: maven-local
BuildRequires: mvn(ch.qos.logback:logback-classic)
BuildRequires: mvn(com.fasterxml.jackson.core:jackson-databind)
BuildRequires: mvn(com.google.guava:guava)
BuildRequires: mvn(com.rabbitmq:amqp-client)
BuildRequires: mvn(com.sun.jersey:jersey-server:1)
BuildRequires: mvn(info.ganglia.gmetric4j:gmetric4j)
BuildRequires: mvn(javax.servlet:javax.servlet-api)
BuildRequires: mvn(javax.ws.rs:javax.ws.rs-api)
BuildRequires: mvn(log4j:log4j:1.2.17)
BuildRequires: mvn(net.sf.ehcache:ehcache-core)
BuildRequires: mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires: mvn(org.apache.httpcomponents:httpasyncclient)
BuildRequires: mvn(org.apache.httpcomponents:httpclient)
BuildRequires: mvn(org.apache.logging.log4j:log4j-api)
BuildRequires: mvn(org.apache.logging.log4j:log4j-core)
BuildRequires: mvn(org.apache.maven.plugins:maven-release-plugin)
BuildRequires: mvn(org.glassfish.jersey.core:jersey-server)
BuildRequires: mvn(org.jdbi:jdbi)
BuildRequires: mvn(org.openjdk.jmh:jmh-core)
BuildRequires: mvn(org.openjdk.jmh:jmh-generator-annprocess)
BuildRequires: mvn(org.slf4j:slf4j-api)

%if 0
# metrics-jetty8
BuildRequires: mvn(org.eclipse.jetty:jetty-server:8.1.11.v20130520)
# metrics-jetty9
BuildRequires: mvn(org.eclipse.jetty:jetty-client:9.2.2.v20140723)
BuildRequires: mvn(org.eclipse.jetty:jetty-server:9.2.2.v20140723)
# metrics-jetty9-legacy
BuildRequires: mvn(org.eclipse.jetty:jetty-server:9.0.4.v20130625)
BuildRequires: mvn(org.eclipse.jetty:jetty-client:9.0.4.v20130625)
# Test deps
BuildRequires: mvn(com.sun.jersey.jersey-test-framework:jersey-test-framework-inmemory)
BuildRequires: mvn(org.glassfish.jersey.test-framework.providers:jersey-test-framework-provider-inmemory)
BuildRequires: mvn(junit:junit)
BuildRequires: mvn(org.assertj:assertj-core:jar:1.6.1)
BuildRequires: mvn(org.eclipse.jetty:jetty-servlet)
BuildRequires: mvn(org.mockito:mockito-all)
BuildRequires: mvn(org.python:jython-standalone)
BuildRequires: mvn(org.slf4j:slf4j-simple)
%endif

# Docs deps
BuildRequires: python-module-sphinx
BuildRequires: /usr/bin/pdflatex

BuildArch:     noarch
Source44: import.info

%description
Metrics is a Java library which gives you unparalleled insight
into what your code does in production.

Developed by Yammer to instrument their JVM-based back-end services,
Metrics provides a powerful toolkit of ways to measure the behavior
of critical components in your production environment.

With modules for common libraries like Jetty, Logback, Log4j,
Apache HttpClient, Ehcache, JDBI, Jersey and reporting back-ends like
Ganglia and Graphite, Metrics provides you with full-stack visibility.

For more information, please see the documentation.

This package provides the Metrics Core Library.

%package annotation
Group: Development/Java
Summary:       Annotations for Metrics

%description annotation
A dependency-less package of just the
annotations used by other Metrics modules.

%package benchmarks
Group: Development/Java
Summary:       Benchmarks for Metrics

%description benchmarks
A development module for performance benchmarks of
Metrics classes.

%package ehcache
Group: Development/Java
Summary:       Metrics Integration for Ehcache

%description ehcache
An Ehcache wrapper providing Metrics instrumentation of caches.

%package ganglia
Group: Development/Java
Summary:       Ganglia Integration for Metrics

%description ganglia
A reporter for Metrics which announces measurements
to a Ganglia cluster.

%package graphite
Group: Development/Java
Summary:       Graphite Integration for Metrics

%description graphite
A reporter for Metrics which announces measurements
to a Graphite server.

%package healthchecks
Group: Development/Java
Summary:       Metrics Health Checks

%description healthchecks
An addition to Metrics which provides the ability to
run application-specific health checks, allowing you
to check your application's heath in production.

%package httpasyncclient
Group: Development/Java
Summary:       Metrics Integration for Apache HttpAsyncClient

%description httpasyncclient
An Apache HttpAsyncClient wrapper providing Metrics
instrumentation of connection pools, request
durations and rates, and other useful information.

%package httpclient
Group: Development/Java
Summary:       Metrics Integration for Apache HttpClient

%description httpclient
An Apache HttpClient wrapper providing Metrics
instrumentation of connection pools, request
durations and rates, and other useful information.

%package jdbi
Group: Development/Java
Summary:       Metrics Integration for JDBI

%description jdbi
A JDBI wrapper providing Metrics instrumentation of
query durations and rates.

%package jersey
Group: Development/Java
Summary:       Metrics Integration for Jersey 1.x

%description jersey
A set of class providing Metrics integration for Jersey 1.x,
the reference JAX-RS implementation.

%package jersey2
Group: Development/Java
Summary:       Metrics Integration for Jersey 2.x

%description jersey2
A set of class providing Metrics integration for Jersey 2.x,
the reference JAX-RS implementation.

%if 0
%package jetty
Group: Development/Java
Summary:       Metrics Integration for Jetty 8/9

%description jetty
A set of extensions for Jetty 8/9 which provide instrumentation of
thread pools, connector metrics, and application latency and
utilization.
%endif

%package json
Group: Development/Java
Summary:       Jackson Integration for Metrics

%description json
A set of Jackson modules which provide serializers
for most Metrics classes.

%package jvm
Group: Development/Java
Summary:       JVM Integration for Metrics

%description jvm
A set of classes which allow you to monitor
critical aspects of your Java Virtual Machine
using Metrics.

%package log4j2
Group: Development/Java
Summary:       Metrics Integration for Log4j 2.x

%description log4j2
An instrumented appender for Log4j 2.x.

%package log4j
Group: Development/Java
Summary:       Metrics Integration for Log4j
Requires:      log4j12

%description log4j
An instrumented appender for Log4j.

%package logback
Group: Development/Java
Summary:       Metrics Integration for Logback

%description logback
An instrumented appender for Logback.

%package parent
Group: Development/Java
Summary:       Metrics Parent POM

%description parent
This package provides Metrics Parent POM.

%package servlet
Group: Development/Java
Summary:       Metrics Integration for Servlets

%description servlet
An instrumented filter for servlet environments.

%package servlets
Group: Development/Java
Summary:       Metrics Utility Servlets

%description servlets
A set of utility servlets for Metrics, allowing you
to expose valuable information about your production
environment.

%package javadoc
Group: Development/Java
Summary:       Javadoc for %{name}
BuildArch: noarch

%description javadoc
This package contains javadoc for %{name}.

%package doc
Group: Development/Java
Summary:       Metrics's user manual

%description doc
This package contains %{name}'s user manual.

%prep
%setup -q -n %{name}-%{version}
# Cleanup
find . -name "*.class" -delete
find . -name "*.jar" -type f -delete

%patch0 -p1
%patch1 -p1

# Unavailable build deps:
# see rhbz#861502#c3 rhbz#861502#c5 disable jetty9 sub-module (use jetty 9.0.4.v20130625)
%pom_disable_module metrics-jetty8
%pom_disable_module metrics-jetty9
%pom_disable_module metrics-jetty9-legacy

%pom_remove_plugin :findbugs-maven-plugin
%pom_remove_plugin :maven-enforcer-plugin
%pom_remove_plugin -r :maven-shade-plugin

# Disable javadoc jar
%pom_xpath_remove "pom:plugins/pom:plugin[pom:artifactId='maven-javadoc-plugin']/pom:executions"
# Disable source jar
%pom_remove_plugin :maven-source-plugin

%pom_xpath_set "pom:properties/pom:jersey.version" 1 %{name}-jersey
%pom_add_dep javax.ws.rs:javax.ws.rs-api metrics-jersey2
sed -i "s|jersey.repackaged.||" \
 metrics-jersey2/src/main/java/com/codahale/metrics/jersey2/InstrumentedResourceMethodApplicationListener.java
%pom_add_dep com.google.guava:guava metrics-jersey2

# org.assertj:assertj-core:1.6.1 *
%pom_remove_dep -r org.assertj:assertj-core

%if 0
%mvn_package ":%{name}-jetty8" %{name}-jetty
%mvn_package ":%{name}-jetty9" %{name}-jetty
%mvn_package ":%{name}-jetty9-legacy" %{name}-jetty
%endif

%mvn_alias io.dropwizard.metrics: com.codahale.metrics:

%build

# Unavailable test dep *
%mvn_build -s -f

(
  cd docs
%if 0
  make %{?_smp_mflags} latexpdf
%endif
  make %{?_smp_mflags} singlehtml
  make %{?_smp_mflags} man
)

%install
%mvn_install

mkdir -p %{buildroot}%{_mandir}/man1
install -pm 644 docs/target/man/%{name}.1 %{buildroot}%{_mandir}/man1/

rm -rf docs/target/singlehtml/.buildinfo

%files  -f .mfiles-%{name}-core
%doc README.md
%doc LICENSE NOTICE

%files annotation -f .mfiles-%{name}-annotation
%doc LICENSE NOTICE

%files benchmarks -f .mfiles-%{name}-benchmarks
%doc %{name}-benchmarks/README.md
%doc LICENSE NOTICE

%files ehcache -f .mfiles-%{name}-ehcache
%doc LICENSE NOTICE

%files ganglia -f .mfiles-%{name}-ganglia
%doc LICENSE NOTICE

%files graphite -f .mfiles-%{name}-graphite
%doc LICENSE NOTICE

%files healthchecks -f .mfiles-%{name}-healthchecks
%doc LICENSE NOTICE

%files httpasyncclient -f .mfiles-%{name}-httpasyncclient
%doc LICENSE NOTICE

%files httpclient -f .mfiles-%{name}-httpclient
%doc LICENSE NOTICE

%files jdbi -f .mfiles-%{name}-jdbi
%doc LICENSE NOTICE

%files jersey -f .mfiles-%{name}-jersey
%doc LICENSE NOTICE

%files jersey2 -f .mfiles-%{name}-jersey2
%doc LICENSE NOTICE

%if 0
%files jetty -f .mfiles-%{name}-jetty
%doc LICENSE NOTICE
%endif

%files json -f .mfiles-%{name}-json
%doc LICENSE NOTICE

%files jvm -f .mfiles-%{name}-jvm
%doc LICENSE NOTICE

%files log4j2 -f .mfiles-%{name}-log4j2
%doc LICENSE NOTICE

%files log4j -f .mfiles-%{name}-log4j
%doc LICENSE NOTICE

%files logback -f .mfiles-%{name}-logback
%doc LICENSE NOTICE

%files parent -f .mfiles-%{name}-parent
%doc LICENSE NOTICE

%files servlet -f .mfiles-%{name}-servlet
%doc LICENSE NOTICE

%files servlets -f .mfiles-%{name}-servlets
%doc LICENSE NOTICE

%files javadoc -f .mfiles-javadoc
%doc LICENSE NOTICE

%files doc
%{_mandir}/man1/%{name}.*
%doc LICENSE NOTICE
%doc docs/target/singlehtml
%if 0
%doc docs/target/latex/*.pdf
%endif

%changelog
* Tue Dec 06 2016 Igor Vlasenko <viy@altlinux.ru> 3.1.2-alt1_3jpp8
- new version

* Mon Feb 08 2016 Igor Vlasenko <viy@altlinux.ru> 3.0.1-alt1_6jpp8
- new version

