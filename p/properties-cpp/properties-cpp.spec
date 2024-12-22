%define _unpackaged_files_terminate_build 1

Name: properties-cpp
Version: 0.0.3
Release: alt1

Summary: C++11 library providing properties/signal
License: LGPLv3
Group: System/Libraries
Url: https://gitlab.com/ubports/development/core/lib-cpp/properties-cpp

Source: %name-%version.tar
Patch: %name-%version-alt-disable-tests.patch

BuildRequires(pre): rpm-macros-cmake

BuildRequires: cmake
BuildRequires: gcc-c++

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
* Sat Nov 23 2024 Nikolay Strelkov <snk@altlinux.org> 0.0.3-alt1
- New version 0.0.3.

* Sun Nov 12 2023 Nikolay Strelkov <snk@altlinux.org> 0.0.2-alt2
- Handle review issues:
  + removed obsolete Packager tag
  + break BuildRequires to multiple lines
  + renamed patch

* Fri Dec 30 2022 Nikolay Strelkov <snk@altlinux.org> 0.0.2-alt1
- Initial build for Sisyphus
