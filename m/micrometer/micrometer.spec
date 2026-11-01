%define _unpackaged_files_terminate_build 1

Name: micrometer
Version: 1.16.8
Release: alt1

Summary: JVM application metrics facade
License: Apache-2.0
Group: Development/Java
Url: https://github.com/micrometer-metrics/micrometer
VCS: https://github.com/micrometer-metrics/micrometer.git

Source0: %name-%version.tar
Patch0: %name-%version-alt-build.patch

BuildArch: noarch

BuildRequires(pre): rpm-macros-gradle
BuildRequires: java-21-openjdk-devel
BuildRequires: rpm-build-java-osgi
BuildRequires: xgradle
BuildRequires: mvn(biz.aQute.bnd:biz.aQute.bndlib)
BuildRequires: mvn(com.github.ben-manes.caffeine:caffeine)
BuildRequires: mvn(com.google.code.findbugs:jsr305)
BuildRequires: mvn(com.google.guava:guava)
BuildRequires: mvn(com.squareup.okhttp3:okhttp)
BuildRequires: mvn(io.micrometer:context-propagation)
BuildRequires: mvn(org.aspectj:aspectjrt)
BuildRequires: mvn(org.hdrhistogram:HdrHistogram)
BuildRequires: mvn(org.jspecify:jspecify)
BuildRequires: mvn(org.latencyutils:LatencyUtils)
BuildRequires: mvn(org.slf4j:slf4j-api)

%description
Micrometer provides a vendor-neutral facade for application metrics.
This ALT profile includes commons, observation, core, Java 11/21 extensions,
and health, Datadog and Elasticsearch registries. Core includes JVM, system
and JDBC instrumentation, plus Caffeine, Guava and OkHttp integrations.
Other external framework binders, Kotlin extensions and
Dropwizard instrumentation are not included. AspectJ annotations and aspect
classes are present; compile-time woven aspectOf accessors are not generated.

%prep
%setup -q
%autopatch -p1

%build
# Gradle 9.7 cannot parse JDK 27 class files (major 71).
%gradle_publish

%install
%gradle_register --artifacts=micrometer- \
    --exclude-artifacts=micrometer-bom-
%gradle_register_bom --artifacts=micrometer-bom-
%gradle_install

%files -f .mfiles
%doc README.md
%doc LICENSE NOTICE

%changelog
* Thu Oct 29 2026 Ivan Khanas <xeno@altlinux.org> 1.16.8-alt1
- Initial build for ALT.
