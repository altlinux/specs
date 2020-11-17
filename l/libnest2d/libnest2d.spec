# Unpackaged files in buildroot should terminate build
%define _unpackaged_files_terminate_build 1

Name:     libnest2d
Version:  0.4
Release:  alt1

Summary:  2D irregular bin packaging and nesting library written in modern C++
License:  LGPL-3.0
Group:    Other
Url:      https://github.com/tamasmeszaros/libnest2d

Packager: Anton Midyukov <antohami@altlinux.org>

Source:   %name-%version.tar

# PATCH-FIX-UPSTREAM -- https://github.com/tamasmeszaros/libnest2d/pull/18
Patch0:   Add-disallowed-areas.patch

BuildRequires(pre): rpm-macros-cmake
BuildRequires: gcc-c++
BuildRequires: cmake
BuildRequires: libpolyclipping-devel
BuildRequires: boost-devel
BuildRequires: libnlopt-devel

%description
%summary

%package devel
Summary: Library for the 2D bin packaging problem
Group:   Other
Requires: boost-devel-headers
Requires: libpolyclipping-devel
Requires: libnlopt-devel

%description devel
A library and framework for the 2D bin packaging problem.

%prep
%setup
%patch0 -p1
sed -i -e "s/ lib\([^n]\)/ "%_lib"\1/" CMakeLists.txt

%build
%cmake -DLIBNEST2D_HEADER_ONLY=ON
%cmake_build

%install
%cmakeinstall_std

%files devel
%doc README.md LICENSE.txt
%_includedir/libnest2d
%_libdir/cmake/Libnest2D

%changelog
* Mon Nov 16 2020 Anton Midyukov <antohami@altlinux.org> 0.4-alt1
- Initial build for Sisyphus
