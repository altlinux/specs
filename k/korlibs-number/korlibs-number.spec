%define _unpackaged_files_terminate_build 1

Name: korlibs-number
Version: 6.1.0
Release: alt1

Summary: Kotlin fixed point and extended number types
License: MIT
Group: Development/Java
URL: https://github.com/korlibs/korlibs-number
VCS: https://github.com/korlibs/korlibs-number.git
BuildArch: noarch

Source: %name-%version.tar
Source1: LICENSE
Patch: %name-system.patch

BuildRequires(pre): rpm-macros-gradle
BuildRequires: java-17-openjdk-devel
BuildRequires: xgradle
BuildRequires: kotlin-gradle-plugin
BuildRequires: mvn(org.jetbrains.kotlin:kotlin-test)
BuildRequires: mvn(org.jetbrains.kotlin:kotlin-test-junit)
BuildRequires: mvn(junit:junit)

%description
Korlibs Number provides fixed point numbers, half precision floating point,
brain floating point, and 53-bit integer types. This package contains its
complete JVM implementation and common Kotlin metadata.

%prep
%setup
%autopatch -p1
cp %SOURCE1 LICENSE

%build
%gradle_publish

%install
%gradle_register --artifacts=korlibs-number
%gradle_install

%check
%gradle_check jvmTest

%files -f .mfiles
%doc LICENSE

%changelog
* Mon Nov 09 2026 Ivan Khanas <xeno@altlinux.org> 6.1.0-alt1
- Initial build for ALT.
