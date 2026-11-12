%define _unpackaged_files_terminate_build 1

Name: korlibs-string
Version: 6.1.0
Release: alt1

Summary: Kotlin string and text utilities
License: MIT
Group: Development/Java
URL: https://github.com/korlibs/korlibs-string
VCS: https://github.com/korlibs/korlibs-string.git

Source: %name-%version.tar
Source1: LICENSE
Patch: %name-system.patch

BuildArch: noarch
BuildRequires(pre): rpm-macros-gradle
BuildRequires: java-17-openjdk-devel
BuildRequires: xgradle
BuildRequires: kotlin-gradle-plugin
BuildRequires: kotlinx-atomicfu
BuildRequires: korlibs-platform
BuildRequires: kotlin-test
BuildRequires: junit

%description
Korlibs String provides case conversion, indentation and other text
utilities. This package contains its complete JVM implementation and
common Kotlin publication metadata.

%prep
%setup
%autopatch -p1
cp %SOURCE1 LICENSE

%build
%gradle_publish -Dorg.gradle.java.home=%_jvmdir/java-17-openjdk

%install
%gradle_register --artifacts=korlibs-string
%gradle_install

%check
%gradle_check -Dorg.gradle.java.home=%_jvmdir/java-17-openjdk

%files -f .mfiles
%doc LICENSE

%changelog
* Tue Nov 03 2026 Ivan Khanas <xeno@altlinux.org> 6.1.0-alt1
- Initial build for ALT.
