%define api_version 3.0
%define rname gtkmm
%define ver_major 3.4
%def_disable atkmm
%def_disable demos

Name: libgtkmm3
Version: %ver_major.0
Release: alt1

Summary: A C++ interface for GTK3 (a GUI library for X)
License: LGPL
Group: System/Libraries
Url: http://gtkmm.sourceforge.net/
Packager: GNOME Maintainers Team <gnome@packages.altlinux.org>

Source: ftp://ftp.gnome.org/pub/gnome/sources/%rname/%ver_major/%rname-%version.tar.xz

Provides: %rname = %version

BuildRequires: gcc-c++ mm-common libgtk+3-devel >= 3.4.0
BuildRequires: libglibmm-devel >= 2.32.0 libpangomm-devel >= 2.28.2
BuildRequires: libatkmm-devel >= 2.22.5 libcairomm-devel >= 1.9.2

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
Group: Development/C++
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
%setup -q -n %rname-%version

%build
%autoreconf
%configure \
	--disable-static \
	%{?_enable_atkmm:--enable-api-atkmm}
%make_build

%install
%make DESTDIR=%buildroot gtkmm_docdir=%_docdir/%rname-%api_version install

%files
%doc AUTHORS NEWS
%_libdir/*.so.*

%files devel
%{?_enable_atkmm:%_includedir/atkmm*}
%_includedir/gdkmm-%api_version
%_includedir/%rname-%api_version
%_libdir/*.so
%_libdir/gdkmm-%api_version
%_libdir/%rname-%api_version
%_pkgconfigdir/*.pc

%files doc
%_datadir/devhelp/books/%rname-%api_version
%_docdir/%rname-%api_version

%if_enabled demos
%files demos
%_datadir/%rname-%api_version
%endif

%changelog
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
