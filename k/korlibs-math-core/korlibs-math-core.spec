%define _unpackaged_files_terminate_build 1

Name: korlibs-math-core
Version: 6.1.0
Release: alt1

Summary: Kotlin core math and numeric utilities
License: MIT
Group: Development/Java
URL: https://github.com/korlibs/korlibs-math-core
VCS: https://github.com/korlibs/korlibs-math-core.git

Source: %name-%version.tar
Source1: LICENSE
Patch: %name-system.patch

BuildArch: noarch
BuildRequires(pre): rpm-macros-gradle
BuildRequires: java-17-openjdk-devel
BuildRequires: xgradle
BuildRequires: kotlin-gradle-plugin
BuildRequires: korlibs-number
BuildRequires: korlibs-platform
BuildRequires: kotlin-test
BuildRequires: junit

%description
Korlibs Math Core provides numeric operations, range conversion, bit
operations and interpolation utilities. This package contains its complete
JVM implementation and common Kotlin publication metadata.

%prep
%setup
%autopatch -p1
cp %SOURCE1 LICENSE

%build
%gradle_publish -Dorg.gradle.java.home=%_jvmdir/java-17-openjdk

%install
%gradle_register --artifacts=korlibs-math-core
%gradle_install

%check
%gradle_check -Dorg.gradle.java.home=%_jvmdir/java-17-openjdk

%files -f .mfiles
%doc LICENSE

%changelog
* Tue Nov 03 2026 Ivan Khanas <xeno@altlinux.org> 6.1.0-alt1
- Initial build for ALT.
