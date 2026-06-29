Name:           metrics
Version:        4.1.12.1
Release:        alt1

Summary:        Capturing JVM- and application-level metrics. So you know what's going on
License:        Apache-2.0
Group:          Development/Java
URL:            https://metrics.dropwizard.io/
VCS:            https://github.com/dropwizard/metrics

Source0:        %name-%version.tar

BuildRequires(pre):  maven-local
BuildRequires:  jpackage-default

BuildRequires:  mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires:  mvn(org.glassfish.jersey:jersey-bom:pom:)
BuildRequires:  mvn(org.codehaus.mojo:build-helper-maven-plugin)
BuildRequires:  mvn(org.apache.maven.plugins:maven-shade-plugin)
BuildRequires:  mvn(org.openjdk.jmh:jmh-core)
BuildRequires:  mvn(org.openjdk.jmh:jmh-generator-annprocess)
BuildRequires:  mvn(com.fasterxml.jackson.core:jackson-databind)
BuildRequires:  mvn(org.apache.logging.log4j:log4j-api)
BuildRequires:  mvn(org.apache.logging.log4j:log4j-core)
BuildRequires:  mvn(ch.qos.logback:logback-classic)

BuildArch:      noarch

%description
Metrics provides a powerful toolkit of ways to measure the behavior of critical
components in your production environment.

With modules for common libraries like Jetty, Logback, Log4j, Apache HttpClient,
Ehcache, JDBI, Jersey and reporting backends like Graphite, Metrics provides you
with full-stack visibility.

%javadoc_package

%package        parent
Summary:        Metrics Parent
Group:          Development/Java

%description    parent
The Metrics library.

%package        annotation
Summary:        Annotations for Metrics
Group:          Development/Java

%description    annotation
A dependency-less package of just the annotations used by other Metrics modules.

%package        benchmarks
Summary:        Benchmarks for Metrics
Group:          Development/Java

%description    benchmarks
A development module for performance benchmarks of Metrics classes.

%package        bom
Summary:        Metrics BOM
Group:          Development/Java

%description    bom
Bill of Materials for Metrics.

%package        collectd
Summary:        Metrics Integration for Collectd
Group:          Development/Java

%description    collectd
A reporter for Metrics which announces measurements to Collectd.

%package        healthchecks
Summary:        Metrics Health Checks
Group:          Development/Java

%description    healthchecks
An addition to Metrics which provides the ability to run application-specific
health checks, allowing you to check your application's heath in production.

%package        httpclient
Summary:        Metrics Integration for Apache HttpClient
Group:          Development/Java

%description    httpclient
An Apache HttpClient wrapper providing Metrics instrumentation of connection
pools, request durations and rates, and other useful information.

%package        jmx
Summary:        Metrics Integration with JMX
Group:          Development/Java

%description    jmx
A set of classes which allow you to report metrics via JMX.

%package        json
Summary:        Jackson Integration for Metrics
Group:          Development/Java

%description    json
A set of Jackson modules which provide serializers for most Metrics classes.

%package        jvm
Summary:        JVM Integration for Metrics
Group:          Development/Java

%description    jvm
A set of classes which allow you to monitor critical aspects of your Java
Virtual Machine using Metrics.

%package        log4j2
Summary:        Metrics Integration for Log4j 2.x
Group:          Development/Java

%description    log4j2
An instrumented appender for Log4j 2.x.

%package        logback
Summary:        Metrics Integration for Logback
Group:          Development/Java

%description    logback
An instrumented appender for Logback.

%package        servlet
Summary:        Metrics Integration for Servlets
Group:          Development/Java

%description    servlet
An instrumented filter for servlet environments.

%prep
%setup

%pom_remove_plugin :maven-enforcer-plugin
%pom_remove_plugin :maven-source-plugin
%pom_remove_plugin :maven-javadoc-plugin

%pom_remove_plugin :maven-dependency-plugin
%pom_remove_plugin :maven-release-plugin
%pom_remove_plugin :maven-checkstyle-plugin
%pom_remove_plugin :maven-site-plugin
%pom_remove_plugin :maven-project-info-reports-plugin

# Disable Error Prone compiler plugin
%pom_xpath_remove "pom:plugin[pom:artifactId='maven-compiler-plugin']/pom:configuration/pom:annotationProcessorPaths"
%pom_xpath_remove "pom:plugin[pom:artifactId='maven-compiler-plugin']/pom:configuration/pom:compilerArgs"

%pom_disable_module docs
%pom_disable_module metrics-caffeine
%pom_disable_module metrics-ehcache
%pom_disable_module metrics-graphite
%pom_disable_module metrics-httpclient5
%pom_disable_module metrics-httpasyncclient
%pom_disable_module metrics-jcache
%pom_disable_module metrics-jcstress
%pom_disable_module metrics-jdbi
%pom_disable_module metrics-jdbi3
%pom_disable_module metrics-jersey2
%pom_disable_module metrics-jetty9
%pom_disable_module metrics-servlets

%build
%mvn_build -f -s

%install
%mvn_install

%files -f .mfiles-metrics-core
%doc LICENSE NOTICE *.md

%files benchmarks -f .mfiles-metrics-benchmarks
%doc metrics-benchmarks/README.md

%files parent -f .mfiles-metrics-parent
%files annotation -f .mfiles-metrics-annotation
%files bom -f .mfiles-metrics-bom
%files collectd -f .mfiles-metrics-collectd
%files healthchecks -f .mfiles-metrics-healthchecks
%files httpclient -f .mfiles-metrics-httpclient
%files jmx -f .mfiles-metrics-jmx
%files json -f .mfiles-metrics-json
%files jvm -f .mfiles-metrics-jvm
%files log4j2 -f .mfiles-metrics-log4j2
%files logback -f .mfiles-metrics-logback
%files servlet -f .mfiles-metrics-servlet

%changelog
* Tue May 19 2026 Evgeniy Serov <scala@altlinux.org> 4.1.12.1-alt1
- Updated to 2.1.12.1.
- Returned to Sisyphus.

* Sat Jul 13 2019 Igor Vlasenko <viy@altlinux.ru> 3.1.2-alt1_8jpp8
- explicit build with java8

* Thu May 31 2018 Igor Vlasenko <viy@altlinux.ru> 3.1.2-alt1_6jpp8
- java update

* Thu Nov 09 2017 Igor Vlasenko <viy@altlinux.ru> 3.1.2-alt1_5jpp8
- fc27 update

* Sun Oct 22 2017 Igor Vlasenko <viy@altlinux.ru> 3.1.2-alt1_4jpp8
- new jpp release

* Tue Dec 06 2016 Igor Vlasenko <viy@altlinux.ru> 3.1.2-alt1_3jpp8
- new version

* Mon Feb 08 2016 Igor Vlasenko <viy@altlinux.ru> 3.0.1-alt1_6jpp8
- new version
