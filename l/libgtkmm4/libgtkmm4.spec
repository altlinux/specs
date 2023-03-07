%def_disable snapshot
%define rname gtkmm
%define ver_major 4.9
%define api_ver 4.0

%def_disable demos
%def_enable check
%def_enable docs

Name: lib%{rname}4
Version: %ver_major.3
Release: alt1

Summary: A C++ interface for GTK4 library
License: GPL-2.0 and LGPL-2.1
Group: System/Libraries
Url: http://gtkmm.sourceforge.net/

%if_disabled snapshot
Source: ftp://ftp.gnome.org/pub/gnome/sources/%rname/%ver_major/%rname-%version.tar.xz
%else
Source: %rname-%version.tar
%endif

Provides: %rname-%api_ver = %version

%define gtk_ver 4.9.3
%define glibmm_api_ver 2.68
%define glibmm_ver 2.68.0
%define pangomm_api_ver 2.48
%define pangomm_ver 2.50.0
%define cairomm_api_ver 1.16
%define cairomm_ver 1.16.0

BuildRequires(pre): meson
BuildRequires: gcc-c++ mm-common libgtk4-devel >= %gtk_ver
BuildRequires: libglibmm%glibmm_api_ver-devel >= %glibmm_ver
BuildRequires: libpangomm%pangomm_api_ver-devel >= %pangomm_ver
BuildRequires: libcairomm%cairomm_api_ver-devel >= %cairomm_ver libepoxy-devel
%{?_enable_docs:BuildRequires: docbook-style-xsl doxygen graphviz fonts-ttf-open-sans xsltproc}
%{?_enable_check:BuildRequires: xvfb-run}

%description
Gtkmm provides a C++ interface to the GTK4 library.

%package devel
Summary: Headers for developing programs that will use %name
Group: Development/C++
Requires: %name = %EVR
Provides: %rname-%api_ver-devel = %version

%description devel
This package contains the static libraries and header files needed for
developing gtkmm applications.

%package devel-doc
Summary: Documentation for developing with %name
Group: Development/Documentation
BuildArch: noarch

%description devel-doc
This package contains the documentation for
developing gtkmm applications.

%package demos
Summary: Demos for developing programs that will use %name
Group: Development/C++
BuildArch: noarch
Conflicts: %name < %version

%description demos
The %name-demos package contains source code of demo programs for %name.

%prep
%setup -n %rname-%version

%build
%{?_enable_snapshot:mm-common-prepare -f}
%meson \
    %{?_disable_atkmm:-Dbuild-atkmm-api=false} \
    %{?_disable_demos:-Dbuild-demos=false} \
    %{?_enable_docs:-Dbuild-documentation=true} \
    %{?_enable_snapshot:-Dmaintainer-mode=true
    -Dbuild-documentation=true}
%nil
%meson_build

%install
%meson_install

%check
export LD_LIBRARY_PATH=%buildroot%_libdir
xvfb-run %meson_test

%files
%doc AUTHORS NEWS
%_libdir/*.so.*

%files devel
%_includedir/%rname-%api_ver
%_libdir/*.so
%_libdir/%rname-%api_ver
%_pkgconfigdir/*.pc

%if_enabled docs
%files devel-doc
%_datadir/devhelp/books/%rname-%api_ver
%_docdir/%rname-%api_ver
%endif

%if_enabled demos
%files demos
%_datadir/%rname-%api_ver
%endif

%changelog
* Tue Mar 07 2023 Yuri N. Sedunov <aris@altlinux.org> 4.9.3-alt1
- 4.9.3

* Mon Sep 12 2022 Yuri N. Sedunov <aris@altlinux.org> 4.8.0-alt1
- 4.8.0

* Mon Mar 21 2022 Yuri N. Sedunov <aris@altlinux.org> 4.6.1-alt1
- 4.6.1

* Fri Mar 04 2022 Yuri N. Sedunov <aris@altlinux.org> 4.6.0-alt1
- 4.6.0

* Thu Sep 09 2021 Yuri N. Sedunov <aris@altlinux.org> 4.4.0-alt1
- 4.4.0

* Fri May 21 2021 Yuri N. Sedunov <aris@altlinux.org> 4.0.2-alt1
- 4.0.2

* Tue Feb 23 2021 Yuri N. Sedunov <aris@altlinux.org> 4.0.1-alt1
- 4.0.1

* Sun Dec 20 2020 Yuri N. Sedunov <aris@altlinux.org> 4.0.0-alt1
- first build for Sisyphus

