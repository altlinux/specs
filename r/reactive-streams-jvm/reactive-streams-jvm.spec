%define _unpackaged_files_terminate_build 1
%def_with check

Name: reactive-streams-jvm
Version: 1.0.4
Release: alt2

Summary: Standard for asynchronous stream processing with non-blocking backpressure
License: Apache-2.0
Group: Development/Java
Url: http://www.reactive-streams.org
Vcs: https://github.com/reactive-streams/reactive-streams-jvm.git
BuildArch: noarch

BuildRequires(pre): rpm-macros-gradle
BuildRequires: xgradle
BuildRequires: /proc
BuildRequires: rpm-build-java-osgi
BuildRequires: jpackage-17-compat
BuildRequires: biz-aQute-bnd-gradle-plugins
%if_with check
BuildRequires: testng
BuildRequires: beust-jcommander
%endif

Source0: %name-%version.tar
Patch0: 0001-Adapt-for-Gradle-8-alt-patch.patch
Patch1: 0002-Adapt-for-bnd-7-alt-patch.patch

%package javadoc
Group: Development/Java
Summary: API documentation for %name
BuildArch: noarch

%description
Reactive Streams is a standard for asynchronous stream processing
with non-blocking back pressure on the JVM platform. It defines a set of
interfaces and rules for implementing reactive streams that enable efficient
and resilient data flow between components, preventing overwhelming fast
producers and ensuring smooth data processing.

%description javadoc
This package contains the %summary.

%prep
%setup
%autopatch -p1

%build
%gradle_publish

%install
%gradle_register
%gradle_register_javadoc

%gradle_install

%check
%ifarch riscv64
export DEFAULT_TIMEOUT_MILLIS=200
%gradle_check
%endif

%files -f .mfiles

%files javadoc -f .mfiles-javadoc

%changelog
* Mon Nov 10 2025 Ivan A. Melnikov <iv@altlinux.org> 1.0.4-alt2
- NMU: Increase test timeouts on riscv64 to fix FTBFS.

* Mon Nov 05 2025 Ivan Khanas <xeno@altlinux.org> 1.0.4-alt1
- First build for ALT.
