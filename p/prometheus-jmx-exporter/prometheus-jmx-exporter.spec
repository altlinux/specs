Group: Development/Java
BuildRequires: /proc rpm-build-java
BuildRequires: jpackage-default
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
%global version_id parent
%global upstream_name jmx_exporter
%global simple_client_version 0.6.0

# Filter requires for the Java Agent as deps are shaded within.
%global jmx_or_client io\\.prometheus\\.jmx:.*|io\\.prometheus:simpleclient.*|org\\.yaml:snakeyaml.*
%global mvn_requires_filter .*mvn\\(%{jmx_or_client}\\)


Name:           prometheus-jmx-exporter
Version:        0.12.0
Release:        alt1_8jpp11
Summary:        Prometheus JMX Exporter

License:        ASL 2.0
URL:            https://github.com/prometheus/jmx_exporter/

Source0:        https://github.com/prometheus/jmx_exporter/archive/%{version_id}-%{version}.tar.gz
Patch1:         properly_rewrite_namespace.patch
Patch2:         0001-Fix-CVE-2017-18640-and-add-a-test.patch

BuildArch:  noarch

BuildRequires: maven-local
BuildRequires: mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires: mvn(org.apache.maven.plugins:maven-assembly-plugin)
BuildRequires: mvn(org.apache.maven.plugins:maven-shade-plugin)
BuildRequires: mvn(org.yaml:snakeyaml)
BuildRequires: mvn(io.prometheus:simpleclient)
BuildRequires: mvn(io.prometheus:simpleclient_hotspot)
BuildRequires: mvn(io.prometheus:simpleclient_common)
BuildRequires: mvn(io.prometheus:simpleclient_httpserver)
BuildRequires: mvn(junit:junit)

Provides: bundled(io.prometheus.jmx:collector) = %{version}
Provides: bundled(io.prometheus:simpleclient) = %{simple_client_version}
Provides: bundled(org.yaml:snakeyaml) = 1.27
Provides: bundled(biz.source_code:base64coder) = 2010.12.19
Provides: bundled(commons-codec:commons-codec) = 1.11
Provides: bundled(io.prometheus:simpleclient_hotspot) = %{simple_client_version}
Provides: bundled(io.prometheus:simpleclient_httpserver) = %{simple_client_version}
Provides: bundled(io.prometheus:simpleclient_common) = %{simple_client_version}
Source44: import.info
%filter_from_requires /^%{mvn_requires_filter}$/d

%description
JMX to Prometheus exporter: a collector that can be configured to scrape
and expose MBeans of a JMX target. This exporter is intended to be run as
a Java Agent, exposing a HTTP server and serving metrics of the local JVM.

%prep
%setup -q -n %{upstream_name}-%{version_id}-%{version}

%patch1 -p1
%patch2 -p1

%pom_remove_plugin org.vafer:jdeb jmx_prometheus_httpserver
%pom_remove_plugin org.apache.maven.plugins:maven-failsafe-plugin jmx_prometheus_javaagent
%pom_remove_plugin org.codehaus.mojo:build-helper-maven-plugin jmx_prometheus_javaagent

# Don't install artefacts from the reactor but the java agent itself. This is because
# the agent needs deps from the reactor but shades them.
%mvn_package "io.prometheus.jmx:jmx_prometheus_httpserver" __noinstall
%mvn_package "io.prometheus.jmx:parent" __noinstall

# Don't depend on obsolete sonatype-oss-parent
# See: https://github.com/prometheus/jmx_exporter/issues/420
%pom_xpath_remove pom:project/pom:parent

%build
# ignore spurious test errors with: -Dmaven.test.failure.ignore=true
%mvn_build -j -- -Dmaven.compiler.source=1.8 -Dmaven.compiler.target=1.8 -Dmaven.javadoc.source=1.8 -Dmaven.compiler.release=8

%install
%mvn_install

%files -f .mfiles
%doc --no-dereference LICENSE
%doc NOTICE

%changelog
* Wed Aug 04 2021 Igor Vlasenko <viy@altlinux.org> 0.12.0-alt1_8jpp11
- update

* Sat Jun 05 2021 Igor Vlasenko <viy@altlinux.org> 0.12.0-alt1_6jpp11
- new version

