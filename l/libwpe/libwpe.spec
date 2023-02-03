%define api_ver 1.0

%def_enable check
%def_enable docs

Name: libwpe
Version: 1.14.1
Release: alt1

Summary: General-purpose library for the WPE-flavored port of WebKit
Group: System/Libraries
License: BSD-2-Clause
Url: https://github.com/WebPlatformForEmbedded/%name

Source: %url/releases/download/%version/%name-%version.tar.xz

BuildRequires(pre): rpm-macros-meson
BuildRequires: meson gcc-c++
BuildRequires: libEGL-devel libxkbcommon-devel
%{?_enable_docs:BuildRequires: hotdoc}

%description
%summary

%package devel
Summary: Development files for %name
Group: Development/C++
Requires: %name = %EVR

%description devel
This package provides files for developing applications that
use %name.

%package devel-doc
Summary: Development documentation for %name
Group: Development/Documentation
BuildArch: noarch
Conflicts: %name < %version

%description devel-doc
This package contains development documentation for %name.

%prep
%setup

%build
%meson \
%{?_enable_docs:-Dbuild-docs=true}
%nil
%meson_build

%install
%meson_install

%check
%__meson_test

%files
%_libdir/libwpe-%api_ver.so.*
%doc NEWS COPYING

%files devel
%_includedir/wpe-%api_ver/
%_libdir/libwpe-%api_ver.so
%_pkgconfigdir/wpe-%api_ver.pc

%if_enabled docs
%files devel-doc
%_datadir/doc/%name/
%endif

%changelog
* Fri Feb 03 2023 Yuri N. Sedunov <aris@altlinux.org> 1.14.1-alt1
- 1.14.1

* Tue Sep 20 2022 Yuri N. Sedunov <aris@altlinux.org> 1.14.0-alt1
- 1.14.0

* Wed Aug 24 2022 Yuri N. Sedunov <aris@altlinux.org> 1.12.3-alt1
- 1.12.3

* Mon Aug 01 2022 Yuri N. Sedunov <aris@altlinux.org> 1.12.2-alt1
- 1.12.2 (ported to Meson build system)
- new devel-doc subpackage

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


