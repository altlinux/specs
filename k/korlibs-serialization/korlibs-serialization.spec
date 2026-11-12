%define _unpackaged_files_terminate_build 1

Name: korlibs-serialization
Version: 6.1.0
Release: alt1

Summary: Structured data formats for Kotlin
License: MIT
Group: Development/Java
URL: https://github.com/korlibs/korlibs-serialization
VCS: https://github.com/korlibs/korlibs-serialization.git

Source: %name-%version.tar
Source1: LICENSE
Patch: %name-system.patch

BuildArch: noarch
BuildRequires(pre): rpm-macros-gradle
BuildRequires: java-17-openjdk-devel
BuildRequires: xgradle
BuildRequires: kotlin-gradle-plugin
BuildRequires: kotlin-test
BuildRequires: junit
BuildRequires: korlibs-string
BuildRequires: korlibs-math-core
BuildRequires: korlibs-datastructure-core
BuildRequires: korlibs-platform

%description
Korlibs Serialization provides parsers and writers for JSON, XML, YAML,
TOML, CSV and property files. This package contains its complete JVM
implementation from the independent upstream project.

%prep
%setup
%autopatch -p1
cp %SOURCE1 LICENSE

%build
%gradle_publish

%install
%gradle_register --artifacts=korlibs-serialization
%gradle_install

%check
%gradle_check

%files -f .mfiles
%doc LICENSE

%changelog
* Tue Nov 03 2026 Ivan Khanas <xeno@altlinux.org> 6.1.0-alt1
- Initial build for ALT.
