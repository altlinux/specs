%define _unpackaged_files_terminate_build 1

Name: korlibs-datastructure-core
Version: 6.1.0
Release: alt1

Summary: Common Kotlin data structures
License: MIT
Group: Development/Java
URL: https://github.com/korlibs/korlibs-datastructure-core
VCS: https://github.com/korlibs/korlibs-datastructure-core.git
BuildArch: noarch

Source: %name-%version.tar
Source1: LICENSE
Patch: %name-system.patch

BuildRequires(pre): rpm-macros-gradle
BuildRequires: java-17-openjdk-devel
BuildRequires: xgradle
BuildRequires: kotlin-gradle-plugin
BuildRequires: kotlinx-atomicfu

%description
Korlibs Datastructure Core provides primitive lists, a fast array list,
iterators, resource interfaces and extensible attributes. This package
contains its full JVM implementation and common Kotlin metadata.

%prep
%setup
%autopatch -p1
cp %SOURCE1 LICENSE

%build
%gradle_publish

%install
%gradle_register --artifacts=korlibs-datastructure-core
%gradle_install

%files -f .mfiles
%doc LICENSE

%changelog
* Mon Nov 09 2026 Ivan Khanas <xeno@altlinux.org> 6.1.0-alt1
- Initial build for ALT.
