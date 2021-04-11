%define ver_major 1.8
%define api_ver 1.0
%define _name wpebackend-fdo

Name: lib%_name
Version: %ver_major.3
Release: alt1

Summary: A WPE backend designed for Linux desktop systems
Group: System/Libraries
License: BSD-2-Clause
Url: https://github.com/Igalia/WPEBackend-fdo

Source: %url/releases/download/%version/%_name-%version.tar.xz

BuildRequires(pre): rpm-macros-cmake
BuildRequires: cmake gcc-c++
BuildRequires: libgio-devel libEGL-devel
BuildRequires: libwpe-devel >= %ver_major libepoxy-devel
BuildRequires: wayland-devel libwayland-server-devel libwayland-egl-devel

%description
%summary

%package devel
Summary: Development files for %name
Group: Development/C++
Requires: %name = %version-%release

%description devel
This package provides files for developing applications that use %name.

%prep
%setup -n %_name-%version

%build
%add_optflags %(getconf LFS_CFLAGS)
%cmake -DCMAKE_BUILD_TYPE="Release"
%cmake_build

%install
%cmakeinstall_std

%files
%_libdir/libWPEBackend-fdo-%api_ver.so.*
%doc NEWS COPYING

%files devel
%_includedir/wpe-fdo-%api_ver/
%_libdir/libWPEBackend-fdo-%api_ver.so
%_pkgconfigdir/%_name-%api_ver.pc

%changelog
* Mon Apr 12 2021 Yuri N. Sedunov <aris@altlinux.org> 1.8.3-alt1
- 1.8.3

* Sun Mar 21 2021 Yuri N. Sedunov <aris@altlinux.org> 1.8.2-alt1
- 1.8.2

* Fri Sep 11 2020 Yuri N. Sedunov <aris@altlinux.org> 1.8.0-alt1
- 1.8.0

* Tue Jun 02 2020 Yuri N. Sedunov <aris@altlinux.org> 1.6.1-alt1
- 1.6.1

* Mon Mar 16 2020 Yuri N. Sedunov <aris@altlinux.org> 1.6.0-alt1
- 1.6.0

* Sun Dec 22 2019 Yuri N. Sedunov <aris@altlinux.org> 1.4.0-alt2
- fixed build

* Mon Sep 23 2019 Yuri N. Sedunov <aris@altlinux.org> 1.4.0-alt1
- 1.4.0

* Mon Jun 17 2019 Yuri N. Sedunov <aris@altlinux.org> 1.3.1-alt1
- first build for Sisyphus



