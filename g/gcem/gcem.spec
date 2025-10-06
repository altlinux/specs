%define _name gcem

Name: %_name
Version: 1.18.0
Release: alt1

Summary: A C++ compile-time math library using generalized constant expressions
Group: System/Libraries
License: Apache-2.0
Url: https://github.com/kthohr/gcem

Vcs: https://github.com/kthohr/gcem.git

Source: https://github.com/kthohr/gcem/archive/v%version/%_name-%version.tar.gz

BuildRequires(pre): rpm-macros-cmake
BuildRequires: cmake gcc-c++

%description
GCE-Math (Generalized Constant Expression Math) is a templated C++
library enabling compile-time computation of mathematical functions

%package devel
Summary: %_name development files
Group: Development/C++

%description devel
GCE-Math library headers and CMake files.

%prep
%setup -n %_name-%version

%build
%cmake -DCMAKE_BUILD_TYPE:STRING="Release"
%cmake_build

%install
%cmake_install

%files devel
%_includedir/%_name.hpp
%_includedir/%{_name}_incl/
%_libdir/cmake/%_name/
%doc README* NOTICE.txt

%changelog
* Mon Oct 06 2025 Yuri N. Sedunov <aris@altlinux.org> 1.18.0-alt1
- first build for Sisyphus


