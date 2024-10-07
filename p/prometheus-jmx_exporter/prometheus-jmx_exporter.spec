Name:    prometheus-jmx_exporter
Version: 1.0.1
Release: alt2
Summary: A process for exposing JMX Beans via HTTP for Prometheus consumption

Group:   Development/Java
License: Apache-2.0
URL:     https://github.com/prometheus/jmx_exporter
Source0: jmx_exporter-%version.tar
Source1: m2.tar

BuildRequires(pre): rpm-build-java
BuildRequires: java-devel >= 17.0
BuildRequires: /proc
BuildRequires: maven-local
BuildRequires: maven-plugin-bundle
BuildRequires: maven-shade-plugin
BuildRequires: maven-profile
BuildRequires: maven-artifact-manager
BuildRequires: maven-plugin-registry

ExcludeArch: %ix86 armh

Requires: java >= 17.0

Provides: prometheus-jmx-exporter = %EVR
Obsoletes: prometheus-jmx-exporter < %EVR

%description
%summary

%prep
%setup -n jmx_exporter-%version
tar xf %SOURCE1 -C ~
# Disable integration tests
subst '/integration_test_suite/d' pom.xml

%build
%mvn_build -- -Dmaven.test.skip=true package

%install
mkdir -p %buildroot%_datadir/java/%name
cp jmx_prometheus_common/target/jmx_prometheus_common-%version.jar %buildroot%_datadir/java/%name
cp jmx_prometheus_httpserver/target/jmx_prometheus_httpserver-%version.jar %buildroot%_datadir/java/%name
cp jmx_prometheus_javaagent/target/jmx_prometheus_javaagent-%version.jar %buildroot%_datadir/java/%name
install -Dpm 644 pom.xml %buildroot%_mavenpomdir/JPP-jmx_exporter.pom

%files
%doc docs/README.md
%_datadir/java/%name
%_mavenpomdir/*

%changelog
* Mon Oct 07 2024 Andrey Cherepanov <cas@altlinux.org> 1.0.1-alt2
- Obsoletes prometheus-jmx-exporter.

* Mon Sep 23 2024 Andrey Cherepanov <cas@altlinux.org> 1.0.1-alt1
- Initial build for Sisyphus.
