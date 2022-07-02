Group: Other
BuildRequires: /proc rpm-build-java
BuildRequires: jpackage-default
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
%global version_id parent
%global upstream_name client_java

Name:          prometheus-simpleclient-java
Version:       0.12.0
Release:       alt1_4jpp11
Summary:       Prometheus JVM Client

License:       ASL 2.0 and CC0
URL:           https://github.com/prometheus/client_java/

Source0:       https://github.com/prometheus/client_java/archive/%{version_id}-%{version}.tar.gz
# OpenTelemetry isn't in Fedora
Patch1:        remove_opentelemetry_tracer.patch

BuildArch:     noarch

BuildRequires: maven-local
BuildRequires: mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires: mvn(junit:junit)
Source44: import.info

%description
Prometheus instrumentation library for JVM applications.

%prep
%setup -q -n %{upstream_name}-%{version_id}-%{version}

# Remove included jar files
find . -name \*.jar -print0 | xargs -0 rm

# Only build the following artefacts as these are actually dependencies
# of prometheus_jmxexporter
# 
# io.prometheus:simpleclient
# io.prometheus:simpleclient_hotspot
# io.prometheus:simpleclient_httpserver
# io.prometheus:simpleclient_common
for m in simpleclient_caffeine \
         simpleclient_dropwizard \
         simpleclient_graphite_bridge \
         simpleclient_hibernate \
         simpleclient_guava \
         simpleclient_log4j \
         simpleclient_log4j2 \
         simpleclient_logback \
         simpleclient_pushgateway \
         simpleclient_servlet \
         simpleclient_spring_web \
         simpleclient_spring_boot \
         simpleclient_jetty \
         simpleclient_jetty_jdk8 \
         simpleclient_vertx \
         simpleclient_bom \
         integration_tests \
         simpleclient_servlet_common \
         simpleclient_servlet_jakarta \
         benchmarks; do
%pom_disable_module $m
done
# Only build simpleclient_tracer_common as it's being used by an Examplar class
%pom_disable_module simpleclient_tracer_otel_agent simpleclient_tracer
%pom_disable_module simpleclient_tracer_otel simpleclient_tracer

# Remove test dependencies for hotspot
%pom_remove_dep io.prometheus:simpleclient_servlet simpleclient_hotspot
%pom_remove_dep org.mockito:mockito-core simpleclient_hotspot
%pom_remove_dep org.eclipse.jetty:jetty-servlet simpleclient_hotspot
# Remove test dependencies for httpserver
%pom_remove_dep org.assertj:assertj-core simpleclient_httpserver
%pom_remove_dep javax.xml.bind:jaxb-api simpleclient_httpserver

# Remove tests which wouldn't compile with removed deps (like mockito)
for i in $(find simpleclient_hotspot/src/test/java/io/prometheus/client/hotspot -name \*.java); do
  if ! echo $i | grep -q -E 'VersionInfoExportsTest\.java'; then
    rm $i
  fi
done
rm -rf simpleclient_httpserver/src/test/java

# remove OpenTelemetry stuff, which we don't support
%patch1 -p2
%pom_remove_dep io.prometheus:simpleclient_tracer_otel simpleclient
%pom_remove_dep io.prometheus:simpleclient_tracer_otel_agent simpleclient
%pom_add_dep io.prometheus:simpleclient_tracer_common:%{version} simpleclient

# Change compiler source/target version to JDK 8 level
%pom_xpath_set "pom:build/pom:plugins/pom:plugin[pom:artifactId='maven-compiler-plugin']/pom:configuration/pom:source" "1.8" pom.xml
%pom_xpath_set "pom:build/pom:plugins/pom:plugin[pom:artifactId='maven-compiler-plugin']/pom:configuration/pom:target" "1.8" pom.xml


%build
%mvn_build -j -- -Dmaven.compiler.source=1.8 -Dmaven.compiler.target=1.8 -Dmaven.javadoc.source=1.8 -Dmaven.compiler.release=8

%install
%mvn_install

%files -f .mfiles
%doc --no-dereference LICENSE
%doc NOTICE

%changelog
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

