%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1
%set_verify_elf_method strict

%define abiversion 1

%def_with check

Name: sv
Version: 1.2
Release: alt2

Summary: Public domain cross-platform semantic versioning in c99
License: Unlicense
Group: System/Libraries

Url: https://github.com/uael/sv
VCS: https://github.com/uael/sv
Source: %name-%version.tar
Patch: %name-%version-bump-minor-version-cmake.patch

BuildRequires(pre): rpm-macros-cmake
BuildRequires: cmake

%if_with check
BuildRequires: ctest
%endif

%description
This is free and unencumbered software released into the public domain.
This package installs a C language library implementing semantic
versioning for the C language.

%package -n lib%name%abiversion
Summary: Shared library for %name
Group: System/Libraries

%description -n lib%name%abiversion
This package contains shared library for software that requires %name.

%package -n lib%name-devel
Summary: Development files for %name
Group: Development/C
Requires: lib%name%abiversion = %EVR

%description -n lib%name-devel
This package contains headers and libraries for building software that
uses %name.

%prep
%setup
%patch -p1

%build
%cmake
%cmake_build

%install
%cmake_install

%check
%ctest

%files -n lib%name%abiversion
%_libdir/*.so.%abiversion
%_libdir/*.so.%abiversion.*

%files -n lib%name-devel
%_includedir/%name
%_libdir/*.so
%_pkgconfigdir/*.pc

%changelog
* Thu May 07 2026 Michael Shigorin <mike@altlinux.org> 1.2-alt2
- Fix build --without check.

* Tue Apr 14 2026 Dmitry Maksimenkov <dmaks@altlinux.org> 1.2-alt1
- Initial build for ALT.

