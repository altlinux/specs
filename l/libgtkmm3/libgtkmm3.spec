%def_disable snapshot
%define api_version 3.0
%define rname gtkmm
%define ver_major 3.24
%def_enable atkmm
%def_disable demos
%def_enable check
%def_enable docs

Name: libgtkmm3
Version: %ver_major.6
Release: alt1

Summary: A C++ interface for GTK3 (a GUI library for X)
License: GPL-2.0 and LGPL-2.1
Group: System/Libraries
Url: http://gtkmm.sourceforge.net/

%if_disabled snapshot
Source: ftp://ftp.gnome.org/pub/gnome/sources/%rname/%ver_major/%rname-%version.tar.xz
%else
Source: %rname-%version.tar
%endif

Provides: %rname = %version

%define gtk_ver 3.24.0
%define glib_ver 2.54.0
%define pangomm_ver 2.40.0
%define atkmm_ver 2.24.2
%define cairo_ver 1.12.0

BuildRequires(pre): meson
BuildRequires: gcc-c++ mm-common libgtk+3-devel >= %gtk_ver
BuildRequires: libglibmm-devel >= %glib_ver libpangomm-devel >= %pangomm_ver
BuildRequires: libcairomm-devel >= %cairo_ver libepoxy-devel
%{?_enable_atkmm:BuildRequires: libatkmm-devel >= %atkmm_ver}
%{?_enable_docs:BuildRequires: docbook-style-xsl doxygen graphviz fonts-ttf-open-sans xsltproc}
%{?_enable_check:BuildRequires: xvfb-run}

%description
Gtkmm provides a C++ interface to the GTK+ GUI library. gtkmm2 wraps GTK+ 2.
Highlights include typesafe callbacks, widgets extensible via inheritance
and a comprehensive set of widget classes that can be freely combined to
quickly create complex user interfaces.

%package devel
Summary: Headers for developing programs that will use %name
Group: Development/C++
Requires: %name = %version-%release
Provides: %rname-devel = %version

%description devel
This package contains the static libraries and header files needed for
developing gtkmm applications.

%package doc
Summary: Documentation for developing with %name
Group: Development/Documentation
BuildArch: noarch

%description doc
This package contains the documentation for
developing gtkmm applications.

%package demos
Summary: Demos for developing programs that will use %name
Group: Development/C++
BuildArch: noarch
Requires: %name-devel = %version-%release

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
%_includedir/gdkmm-%api_version
%_includedir/%rname-%api_version
%_libdir/*.so
%_libdir/gdkmm-%api_version
%_libdir/%rname-%api_version
%_pkgconfigdir/*.pc

%if_enabled docs
%files doc
%_datadir/devhelp/books/%rname-%api_version
%_docdir/%rname-%api_version
%endif

%if_enabled demos
%files demos
%_datadir/%rname-%api_version
%endif

%changelog
* Mon May 02 2022 Yuri N. Sedunov <aris@altlinux.org> 3.24.6-alt1
- 3.24.6

* Fri May 21 2021 Yuri N. Sedunov <aris@altlinux.org> 3.24.5-alt1
- 3.24.5

* Tue Feb 23 2021 Yuri N. Sedunov <aris@altlinux.org> 3.24.4-alt1
- 3.24.4

* Sun Dec 13 2020 Yuri N. Sedunov <aris@altlinux.org> 3.24.3-alt1
- 3.24.3 (ported to Meson build system)

* Fri Nov 27 2020 Yuri N. Sedunov <aris@altlinux.org> 3.24.2-alt3
- updated to 3.24.2-81-gcfa54b63

* Tue Mar 24 2020 Yuri N. Sedunov <aris@altlinux.org> 3.24.2-alt2.1
- fixed "docs" knob logic

* Sun Mar 22 2020 Yuri N. Sedunov <aris@altlinux.org> 3.24.2-alt2
- updated to 3.24.2-12-gc96e1e1a
- fixed License tag

* Thu Oct 24 2019 Yuri N. Sedunov <aris@altlinux.org> 3.24.2-alt1
- 3.24.2

* Wed Mar 20 2019 Yuri N. Sedunov <aris@altlinux.org> 3.24.1-alt1
- 3.24.1

* Thu Nov 08 2018 Yuri N. Sedunov <aris@altlinux.org> 3.24.0-alt1
- 3.24.0

* Wed Nov 07 2018 Yuri N. Sedunov <aris@altlinux.org> 3.22.3-alt1
- 3.22.3

* Wed Sep 13 2017 Yuri N. Sedunov <aris@altlinux.org> 3.22.2-alt1
- 3.22.2

* Fri Jun 23 2017 Yuri N. Sedunov <aris@altlinux.org> 3.22.1-alt1
- 3.22.1

* Tue Sep 20 2016 Yuri N. Sedunov <aris@altlinux.org> 3.22.0-alt1
- 3.22.0

* Thu Apr 14 2016 Yuri N. Sedunov <aris@altlinux.org> 3.20.1-alt1
- 3.20.1

* Mon Mar 28 2016 Yuri N. Sedunov <aris@altlinux.org> 3.20.0-alt1
- 3.20.0

* Fri Mar 18 2016 Yuri N. Sedunov <aris@altlinux.org> 3.19.12-alt1
- 3.19.12

* Tue Sep 22 2015 Yuri N. Sedunov <aris@altlinux.org> 3.18.0-alt1
- 3.18.0

* Fri Jun 12 2015 Gleb F-Malinovskiy <glebfm@altlinux.org> 3.16.0-alt1.1
- Rebuilt for gcc5 C++11 ABI.

* Wed Mar 25 2015 Yuri N. Sedunov <aris@altlinux.org> 3.16.0-alt1
- 3.16.0

* Tue Sep 23 2014 Yuri N. Sedunov <aris@altlinux.org> 3.14.0-alt1
- 3.14.0

* Mon Apr 14 2014 Yuri N. Sedunov <aris@altlinux.org> 3.12.0-alt1
- 3.12.0

* Tue Mar 04 2014 Yuri N. Sedunov <aris@altlinux.org> 3.11.8-alt1
- 3.11.8

* Mon Oct 28 2013 Yuri N. Sedunov <aris@altlinux.org> 3.10.1-alt1
- 3.10.1

* Fri Oct 11 2013 Yuri N. Sedunov <aris@altlinux.org> 3.10.0-alt1
- 3.10.0

* Fri Sep 20 2013 Yuri N. Sedunov <aris@altlinux.org> 3.9.16-alt1
- 3.9.16

* Thu May 02 2013 Yuri N. Sedunov <aris@altlinux.org> 3.8.1-alt1
- 3.8.1

* Wed Apr 17 2013 Yuri N. Sedunov <aris@altlinux.org> 3.8.0-alt1
- 3.8.0

* Sat Mar 09 2013 Yuri N. Sedunov <aris@altlinux.org> 3.7.12-alt1
- 3.7.12

* Sun Oct 21 2012 Yuri N. Sedunov <aris@altlinux.org> 3.6.0-alt1
- 3.6.0

* Sat Sep 08 2012 Yuri N. Sedunov <aris@altlinux.org> 3.5.12-alt1
- 2.33.12

* Tue Apr 10 2012 Yuri N. Sedunov <aris@altlinux.org> 3.4.0-alt1
- 3.4.0

* Wed Mar 28 2012 Yuri N. Sedunov <aris@altlinux.org> 3.3.20-alt1
- 3.3.20

* Mon Jan 16 2012 Yuri N. Sedunov <aris@altlinux.org> 3.2.0-alt2
- used %%autoreconf to fix RPATH problem

* Tue Sep 27 2011 Yuri N. Sedunov <aris@altlinux.org> 3.2.0-alt1
- 3.2.0

* Wed May 11 2011 Yuri N. Sedunov <aris@altlinux.org> 3.0.1-alt1
- 3.0.1

* Wed Apr 06 2011 Yuri N. Sedunov <aris@altlinux.org> 3.0.0-alt1
- 3.0.0

* Thu Mar 31 2011 Yuri N. Sedunov <aris@altlinux.org> 2.99.8-alt1
- 2.99.8

* Wed Mar 16 2011 Yuri N. Sedunov <aris@altlinux.org> 2.99.6-alt1
- 2.99.6

* Mon Feb 21 2011 Yuri N. Sedunov <aris@altlinux.org> 2.99.5-alt1
- 2.99.5

* Wed Feb 09 2011 Yuri N. Sedunov <aris@altlinux.org> 2.99.3-alt1
- 2.99.3

* Wed Sep 15 2010 Yuri N. Sedunov <aris@altlinux.org> 2.90.7-alt1
- 2.90.7

* Sat May 22 2010 Yuri N. Sedunov <aris@altlinux.org> 2.90.0-alt1
- first build for Sisyphus
- atkmm temporarily disabled to avoid conflict against libgtkmm2
