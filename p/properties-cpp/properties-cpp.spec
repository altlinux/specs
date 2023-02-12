%define _unpackaged_files_terminate_build 1

Name: properties-cpp
Version: 0.0.2
Release: alt1

Summary: C++11 library providing properties/signal
License: LGPLv3
Group: System/Libraries
Url: https://gitlab.com/ubports/development/core/lib-cpp/properties-cpp

Packager: Nikolay Strelkov <snk@altlinux.org>

Source: %name-%version.tar
Patch: %name-disable-tests.patch

BuildRequires(pre): rpm-macros-cmake

BuildRequires: cmake gcc-c++

%description
A very simple convenience library for handling properties and
signals in C++11.

%package devel
Summary: Header files for properties-cpp
Group: Development/C++

%description devel
A very simple convenience library for handling properties and
signals in C++11.

This package provides development headers for properties-cpp.

%prep
%setup
%patch -p1

%build
%cmake
%cmake_build

%install
%cmake_install

%files devel
%doc COPYING README.md
%_includedir/core
%_pkgconfigdir/%name.pc

%changelog
* Fri Dec 30 2022 Nikolay Strelkov <snk@altlinux.org> 0.0.2-alt1
- Initial build for Sisyphus
