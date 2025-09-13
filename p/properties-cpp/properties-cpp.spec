%define _unpackaged_files_terminate_build 1

%def_with check

Name: properties-cpp
Version: 0.0.4
Release: alt1

Summary: C++11 library providing properties/signal
License: LGPLv3
Group: System/Libraries
Url: https://gitlab.com/ubports/development/core/lib-cpp/properties-cpp

Source: %name-%version.tar

BuildRequires(pre): rpm-macros-cmake

BuildRequires: cmake
BuildRequires: gcc-c++
BuildRequires: ayatana-cmake-modules

%if_with check
BuildRequires: ctest
BuildRequires: pkgconfig(gtest)
%endif

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

%build
%cmake \
%if_with check
       -DBUILD_TESTING=ON
%else
       -DBUILD_TESTING=OFF
%endif
%cmake_build

%check
%ctest -j1 -VV

%install
%cmake_install

%files devel
%doc COPYING README.md
%_includedir/core
%_pkgconfigdir/%name.pc

%changelog
* Sat Sep 13 2025 Nikolay Strelkov <snk@altlinux.org> 0.0.4-alt1
- New version 0.0.4.
- Enabled tests.

* Sat Nov 23 2024 Nikolay Strelkov <snk@altlinux.org> 0.0.3-alt1
- New version 0.0.3.

* Sun Nov 12 2023 Nikolay Strelkov <snk@altlinux.org> 0.0.2-alt2
- Handle review issues:
  + removed obsolete Packager tag
  + break BuildRequires to multiple lines
  + renamed patch

* Fri Dec 30 2022 Nikolay Strelkov <snk@altlinux.org> 0.0.2-alt1
- Initial build for Sisyphus
