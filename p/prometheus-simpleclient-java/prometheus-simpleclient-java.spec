Name:           prometheus-simpleclient-java
Version:        0.16.0
Release:        alt1

Summary:        Prometheus instrumentation library for JVM applications
License:        Apache-2.0
Group:          Development/Java
URL:            http://prometheus.github.io/client_java/
VCS:            https://github.com/prometheus/client_java

Source0:        %name-%version.tar

Patch0:         remove_opentelemetry_tracer.patch

BuildRequires(pre):  rpm-macros-java
BuildRequires:  jpackage-default
BuildRequires:  maven-local

BuildRequires:  mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires:  mvn(commons-math3:commons-math3)
BuildRequires:  mvn(io.dropwizard.metrics:metrics-core)
BuildRequires:  mvn(org.mockito:mockito-core)
BuildRequires:  mvn(jakarta.xml.bind:jakarta.xml.bind-api)
BuildRequires:  mvn(org.apache.logging.log4j:log4j-core)
BuildRequires:  mvn(ch.qos.logback:logback-classic)

BuildArch:      noarch

%description
It supports Java, Clojure, Scala, JRuby, and anything else that runs on the JVM.

%javadoc_package

%prep
%setup
%autopatch -p1

%pom_remove_plugin :maven-enforcer-plugin

%pom_disable_module simpleclient_spring_web
%pom_disable_module simpleclient_spring_boot
%pom_disable_module integration_tests
%pom_disable_module simpleclient_tracer_otel_agent simpleclient_tracer
%pom_disable_module simpleclient_tracer_otel simpleclient_tracer
%pom_disable_module simpleclient_caffeine
%pom_disable_module simpleclient_hibernate
%pom_disable_module simpleclient_pushgateway
%pom_disable_module simpleclient_vertx
%pom_disable_module simpleclient_vertx4
%pom_disable_module simpleclient_httpserver
%pom_disable_module benchmarks

%pom_remove_dep io.prometheus:simpleclient_tracer_otel simpleclient
%pom_remove_dep io.prometheus:simpleclient_tracer_otel_agent simpleclient
%pom_add_dep io.prometheus:simpleclient_tracer_common:%version simpleclient

%pom_change_dep -r :hamcrest-all :hamcrest-core

%pom_change_dep -r org.eclipse.jetty:jetty-servlet org.eclipse.jetty:jetty-servlet:9.4
%pom_change_dep -r org.eclipse.jetty:jetty-server org.eclipse.jetty:jetty-server:9.4

rm -f simpleclient_servlet/src/test/java/io/prometheus/client/exporter/ExampleBenchmark.java
rm -f simpleclient_servlet_jakarta/src/test/java/io/prometheus/client/exporter/Example{Benchmark,Exporter}.java

%build
%mvn_build -- -Dmaven.compiler.release=8

%install
%mvn_install

%files -f .mfiles
%doc LICENSE NOTICE *.md

%changelog
* Tue Jul 07 2026 Evgeniy Serov <scala@altlinux.org> 0.16.0-alt1
- Updated to 0.16.0.

* Fri Jul 01 2022 Igor Vlasenko <viy@altlinux.org> 0.12.0-alt1_4jpp11
- new version

* Sat Jun 05 2021 Igor Vlasenko <viy@altlinux.org> 0.6.0-alt3_5jpp8
- to Sisyphus

* Wed Mar 17 2021 Igor Vlasenko <viy@altlinux.org> 0.6.0-alt2_5
- update to new release by fcimport

* Wed Jan 27 2021 Igor Vlasenko <viy@altlinux.ru> 0.6.0-alt2_4
- update to new release by fcimport

* Wed Sep 02 2020 Igor Vlasenko <viy@altlinux.ru> 0.6.0-alt1_4
- update to new release by fcimport

* Thu Mar 05 2020 Igor Vlasenko <viy@altlinux.ru> 0.6.0-alt1_3
- update to new release by fcimport

* Tue Oct 29 2019 Igor Vlasenko <viy@altlinux.ru> 0.6.0-alt1_2
- update to new release by fcimport

* Mon Sep 30 2019 Igor Vlasenko <viy@altlinux.ru> 0.6.0-alt1_1
- new version

