%define _unpackaged_files_terminate_build 1
%def_without check

Name: blockhound
Version: 1.0.18
Release: alt1

Summary: Blocking call detector for non-blocking Java threads
License: Apache-2.0
Group: Development/Java
Url: https://github.com/reactor/BlockHound
VCS: https://github.com/reactor/BlockHound.git
BuildArch: noarch

Source0: %name-%version.tar
Patch0: %name-%version-alt-build.patch

BuildRequires(pre): rpm-macros-gradle
BuildRequires: java-21-openjdk-devel
BuildRequires: shadow-gradle-plugin
BuildRequires: xgradle
BuildRequires: mvn(com.google.auto.service:auto-service)
BuildRequires: mvn(net.bytebuddy:byte-buddy)
BuildRequires: mvn(net.bytebuddy:byte-buddy-agent)
BuildRequires: mvn(org.junit.platform:junit-platform-launcher)

%if_with check
# Upstream tests require Reactor Core and RxJava test providers; Reactor Core
# currently waits for this package, so the test-only cycle is recorded and skipped.
BuildRequires: mvn(io.projectreactor:reactor-core)
BuildRequires: mvn(io.reactivex.rxjava2:rxjava)
BuildRequires: mvn(junit:junit)
BuildRequires: mvn(org.assertj:assertj-core)
BuildRequires: mvn(org.junit.jupiter:junit-jupiter-api)
BuildRequires: mvn(org.junit.jupiter:junit-jupiter-engine)
%endif

%package junit-platform
Summary: JUnit Platform integration for BlockHound tests
Group: Development/Java
Requires: %name = %EVR

%description
BlockHound is a Java agent that detects blocking calls from non-blocking
threads. The agent packages its required Byte Buddy runtime classes.

%description junit-platform
JUnit Platform listener that enables BlockHound checks for test executions.

%prep
%setup -q
%autopatch -p1

%build
# Keep the optional JMH-only benchmarks project out of the RPM publication graph.
%gradle_publish -PaltPackageBuild=true --stacktrace

%install
%mvn_package io.projectreactor.tools:blockhound-junit-platform blockhound-junit-platform
%gradle_register --artifacts=blockhound-,blockhound-junit-platform-
%gradle_install

%if_with check
%check
%gradle_check -PtestToolchainVersion=21 -PaltPackageBuild=true --stacktrace
%endif

%files -f .mfiles
%doc README.md LICENSE

%files junit-platform -f .mfiles-blockhound-junit-platform

%changelog
* Thu Oct 29 2026 Ivan Khanas <xeno@altlinux.org> 1.0.18-alt1
- Initial build for ALT.
