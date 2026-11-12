%define _unpackaged_files_terminate_build 1

Name: korlibs-platform
Version: 6.1.0
Release: alt1

Summary: Kotlin multiplatform runtime and platform information
License: MIT
Group: Development/Java
URL: https://github.com/korlibs/korlibs-platform
VCS: https://github.com/korlibs/korlibs-platform.git
BuildArch: noarch

Source: %name-%version.tar
Source1: LICENSE
Patch: %name-system.patch

BuildRequires(pre): rpm-macros-gradle
BuildRequires: java-17-openjdk-devel
BuildRequires: xgradle
BuildRequires: kotlin-gradle-plugin

%description
Korlibs Platform provides runtime and platform information, environment
access and common utility interfaces. This package contains its complete
JVM implementation and common Kotlin metadata.

%prep
%setup
%autopatch -p1
cp %SOURCE1 LICENSE

%build
%gradle_publish

%install
%gradle_register --artifacts=korlibs-platform
%gradle_install

%files -f .mfiles
%doc LICENSE

%changelog
* Mon Nov 09 2026 Ivan Khanas <xeno@altlinux.org> 6.1.0-alt1
- Initial build for ALT.
