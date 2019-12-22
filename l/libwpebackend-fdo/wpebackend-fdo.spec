%define api_ver 1.0
%define _name wpebackend-fdo

Name: lib%_name
Version: 1.4.0
Release: alt2

Summary: A WPE backend designed for Linux desktop systems
Group: System/Libraries
License: BSD
Url: https://github.com/Igalia/WPEBackend-fdo

Source: %url/releases/download/%version/%_name-%version.tar.xz
Patch: wpebackend-fdo-1.4.0-up-build_egl.patch

BuildRequires(pre): rpm-macros-cmake
BuildRequires: cmake gcc-c++
BuildRequires: libgio-devel libEGL-devel
BuildRequires: libwpe-devel >= %version
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
%patch -p1

%build
%add_optflags -D_FILE_OFFSET_BITS=64
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
* Sun Dec 22 2019 Yuri N. Sedunov <aris@altlinux.org> 1.4.0-alt2
- fixed build

* Mon Sep 23 2019 Yuri N. Sedunov <aris@altlinux.org> 1.4.0-alt1
- 1.4.0

* Mon Jun 17 2019 Yuri N. Sedunov <aris@altlinux.org> 1.3.1-alt1
- first build for Sisyphus



