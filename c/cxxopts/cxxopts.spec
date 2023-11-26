%define _name cxxopts

%def_enable check

Name: %_name
Version: 3.1.1
Release: alt1

Summary: Lightweight C++ option parser library
License: MIT
Group: System/Libraries
Url: https://github.com/jarro2783/cxxopts

Source: %url/archive/v%version/%_name-%version.tar.gz

BuildRequires(pre): rpm-macros-cmake
BuildRequires: gcc-c++ cmake
%{?_enable_check:BuildRequires: ctest}

%description
This is a lightweight C++ option parser library, supporting the standard
GNU style syntax for options.

%package devel
Summary: Development files for %name
Group: Development/C++

%description devel
Development files for %name.

%prep
%setup -n %_name-%version

%build
%cmake
%cmake_build

%install
%cmake_install

%check
%cmake_build -t test

%files devel
%_includedir/%_name.hpp
%_libdir/cmake/%_name/
%_pkgconfigdir/%_name.pc

%changelog
* Sun Nov 26 2023 Yuri N. Sedunov <aris@altlinux.org> 3.1.1-alt1
- first build for Sisyphus



