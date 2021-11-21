%define ver_major 1.12
%define api_ver 1.0
%define _name wpebackend-fdo

%def_enable docs
%def_enable check

Name: lib%_name
Version: %ver_major.0
Release: alt1

Summary: A WPE backend designed for Linux desktop systems
Group: System/Libraries
License: BSD-2-Clause
Url: https://github.com/Igalia/WPEBackend-fdo

Source: %url/releases/download/%version/%_name-%version.tar.xz

BuildRequires(pre): meson
BuildRequires: gcc-c++
BuildRequires: libgio-devel libEGL-devel
BuildRequires: libwpe-devel >= %ver_major libepoxy-devel
BuildRequires: wayland-devel libwayland-server-devel libwayland-egl-devel
BuildRequires: libxkbcommon-devel
%{?_enable_docs:BuildRequires: hotdoc}
%description
%summary

%package devel
Summary: Development files for %name
Group: Development/C++
Requires: %name = %EVR

%description devel
This package provides files for developing applications that use %name.

%package devel-doc
Summary: Development documentation for %name
Group: Development/Documentation
BuildArch: noarch
Conflicts: %name < %version

%description devel-doc
This package provides development documentation for %_name library.

%prep
%setup -n %_name-%version

%build
%meson \
%{?_enable_docs:-Dbuild_docs=true}
%nil
%meson_build

%install
%meson_install

%check
export LD_LIBRARY_PATH=%buildroot%_libdir
%meson_test

%files
%_libdir/libWPEBackend-fdo-%api_ver.so.*
%doc NEWS COPYING

%files devel
%_includedir/wpe-fdo-%api_ver/
%_libdir/libWPEBackend-fdo-%api_ver.so
%_pkgconfigdir/%_name-%api_ver.pc

%if_enabled docs
%files devel-doc
%_datadir/doc/WPEBackend-fdo/
%endif

%changelog
* Wed Oct 20 2021 Yuri N. Sedunov <aris@altlinux.org> 1.12.0-alt1
- 1.12.0

* Tue Jun 08 2021 Yuri N. Sedunov <aris@altlinux.org> 1.10.0-alt1
- 1.10.0 (ported to Meson build system)
- new -devel-doc subpackage

* Thu May 13 2021 Yuri N. Sedunov <aris@altlinux.org> 1.8.4-alt1
- 1.8.4

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



