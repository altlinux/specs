%define api_ver 1.0

Name: libwpe
Version: 1.4.0.1
Release: alt1

Summary: General-purpose library for the WPE-flavored port of WebKit
Group: System/Libraries
License: BSD
Url: https://github.com/WebPlatformForEmbedded/%name

Source: %url/releases/download/%version/%name-%version.tar.xz

BuildRequires(pre): rpm-macros-cmake
BuildRequires: cmake gcc-c++
BuildRequires: libEGL-devel libxkbcommon-devel

%description
%summary

%package devel
Summary: Development files for %name
Group: Development/C++
Requires: %name = %version-%release

%description devel
This package provides files for developing applications that
use %name.

%prep
%setup

%build
%cmake -DCMAKE_BUILD_TYPE="Release"
%cmake_build

%install
%cmakeinstall_std

%files
%_libdir/libwpe-%api_ver.so.*
%doc NEWS COPYING

%files devel
%_includedir/wpe-%api_ver/
%_libdir/libwpe-%api_ver.so
%_pkgconfigdir/wpe-%api_ver.pc

%changelog
* Thu Oct 31 2019 Yuri N. Sedunov <aris@altlinux.org> 1.4.0.1-alt1
- 1.4.0.1

* Mon Sep 23 2019 Yuri N. Sedunov <aris@altlinux.org> 1.4.0-alt1
- 1.4.0

* Mon Jun 17 2019 Yuri N. Sedunov <aris@altlinux.org> 1.3.1-alt1
- first build for Sisyphus


