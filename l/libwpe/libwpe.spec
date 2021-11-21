%define api_ver 1.0

Name: libwpe
Version: 1.12.0
Release: alt1

Summary: General-purpose library for the WPE-flavored port of WebKit
Group: System/Libraries
License: BSD-2-Clause
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
* Sun Oct 03 2021 Yuri N. Sedunov <aris@altlinux.org> 1.12.0-alt1
- 1.12.0

* Mon Apr 12 2021 Yuri N. Sedunov <aris@altlinux.org> 1.10.0-alt1
- 1.10.0

* Fri Sep 11 2020 Yuri N. Sedunov <aris@altlinux.org> 1.8.0-alt1
- 1.8.0

* Mon Mar 16 2020 Yuri N. Sedunov <aris@altlinux.org> 1.6.0-alt1
- 1.6.0

* Thu Oct 31 2019 Yuri N. Sedunov <aris@altlinux.org> 1.4.0.1-alt1
- 1.4.0.1

* Mon Sep 23 2019 Yuri N. Sedunov <aris@altlinux.org> 1.4.0-alt1
- 1.4.0

* Mon Jun 17 2019 Yuri N. Sedunov <aris@altlinux.org> 1.3.1-alt1
- first build for Sisyphus


