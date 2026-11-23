%define _unpackaged_files_terminate_build 1
%define _without_javadoc 1

Name: oshi
Version: 7.7.3
Release: alt1

Summary: Java library for operating system and hardware information
License: MIT
Group: Development/Java
URL: https://github.com/oshi/oshi
VCS: https://github.com/oshi/oshi
Source0: oshi-%version.tar
Patch0: use-system-surefire.patch

BuildRequires(pre): rpm-macros-java
# The Java 25 profile enables oshi-core-ffm, oshi-benchmark and oshi-dist.
# Keep it disabled for noarch builds because JDK 25 is unavailable on i586.
BuildRequires: java-21-openjdk-devel
BuildRequires: maven-local
BuildRequires: mvn(org.apache.maven.plugins:maven-surefire-plugin)
BuildRequires: mvn(org.jacoco:jacoco-maven-plugin)
BuildRequires: mvn(de.thetaphi:forbiddenapis)
BuildRequires: mvn(org.apache.maven.plugins:maven-enforcer-plugin)
BuildRequires: mvn(biz.aQute.bnd:bnd-maven-plugin)
BuildRequires: mvn(net.java.dev.jna:jna-jpms) >= 5.19.1
BuildRequires: mvn(net.java.dev.jna:jna-platform-jpms) >= 5.19.1
BuildRequires: mvn(org.jspecify:jspecify)
BuildRequires: mvn(org.slf4j:slf4j-api)
BuildRequires: mvn(org.junit.jupiter:junit-jupiter-api)
BuildRequires: mvn(org.hamcrest:hamcrest)
BuildRequires: mvn(io.micrometer:micrometer-core)
BuildRequires: mvn(com.fasterxml.jackson.core:jackson-databind)
BuildRequires: mvn(org.jfree:jfreechart)

BuildArch: noarch

%description
OSHI is a free Java library providing operating system and hardware information
through JNA. This package contains the platform-neutral common API and
base classes.

%package core
Summary: JNA based OSHI implementation
Group: Development/Java

%description core
JNA implementation of OSHI operating system and hardware information APIs.

%package metrics
Summary: Micrometer integration for OSHI
Group: Development/Java

%description metrics
Micrometer metrics integration for OSHI hardware and operating system data.

%package demo
Summary: OSHI demonstration application classes
Group: Development/Java

%description demo
Demonstration application classes showing use of OSHI APIs.

%prep
%setup -q
%patch0 -p1
%pom_remove_dep io.github.pandalxb:jLibreHardwareMonitor oshi-core
# PrometheusDemoTest is a standalone server example requiring an unpackaged
# registry. The Micrometer binding tests use the core registry.
%pom_remove_dep io.micrometer:micrometer-registry-prometheus oshi-metrics
rm -f oshi-metrics/src/test/java/oshi/metrics/PrometheusDemoTest.java
# The upstream Maven profiler extension only reports build timing and is not
# needed for compilation, tests, packaging, or runtime. Hasher is offline.
rm -f .mvn/extensions.xml
%mvn_package :oshi-parent common
%mvn_package :oshi-common common
%mvn_package :oshi-core core
%mvn_package :oshi-metrics metrics
%mvn_package :oshi-demo demo
%mvn_file :oshi-common oshi-common/common
%mvn_file :oshi-core oshi-core/core
%mvn_file :oshi-metrics oshi-metrics/metrics
%mvn_file :oshi-demo oshi-demo/demo

%build
%mvn_build -s

%install
%mvn_install

%files -f .mfiles-common
%doc README.md LICENSE

%files core -f .mfiles-core
%files metrics -f .mfiles-metrics
%files demo -f .mfiles-demo
%changelog
* Mon Nov 23 2026 Ivan Khanas <xeno@altlinux.org> 7.7.3-alt1
- Initial build for ALT.
