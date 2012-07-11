%define rname glibmm
%define major 2.32

Name: libglibmm
Version: %major.1
Release: alt1
Summary: C++ wrapper for GLib
License: LGPL
Group: System/Libraries
Url: http://gtkmm.sourceforge.net/
Packager: GNOME Maintainers Team <gnome@packages.altlinux.org>

Source: ftp://ftp.gnome.org/pub/gnome/sources/glibmm/%major/%rname-%version.tar.xz

AutoReq: yes, noperl
BuildRequires: gcc-c++ mm-common libgio-devel >= 2.31.20 libsigc++2.0-devel

%description
A C++ interface for glib library.

This package contains the library needed to run programs dynamically
linked with glibmm.

%package devel
Summary: Headers and development files of glibmm
Group: Development/GNOME and GTK+
Requires: %name = %version-%release

%description devel
A C++ interface for glib library.

This package contains the headers and development files that are needed,
when trying to develop or compile applications which need glibmm.

%package doc
Summary: glibmm documentation
Group: Development/Documentation
BuildArch: noarch

%description doc
Gtkmm provides a C++ interface to the GTK+ GUI library.
glibmm originally belongs to gtkmm, but is now separated,
for use with non-GUI software written in C++.

This package contains all API documentation for glibmm.

%add_findreq_skiplist %_libdir/%rname-2.4/proc/*

%prep
%setup -q -n %rname-%version

%build
%autoreconf
%configure \
	--disable-static
%make_build

%install
%make DESTDIR=%buildroot install

%check
%make check

%files
%doc AUTHORS NEWS
%_libdir/*.so.*

%files devel
%_includedir/g*mm-2.4
%_libdir/*.so
%_libdir/g*mm-2.4
%_pkgconfigdir/*.pc
%_datadir/devhelp/books/%rname-2.4

%files doc
%_docdir/%rname-2.4

%changelog
* Wed Jul 11 2012 Yuri N. Sedunov <aris@altlinux.org> 2.32.1-alt1
- 2.32.1

* Tue Apr 10 2012 Yuri N. Sedunov <aris@altlinux.org> 2.32.0-alt1
- 2.32.0

* Wed Mar 28 2012 Yuri N. Sedunov <aris@altlinux.org> 2.31.22-alt1
- 2.31.22

* Mon Jan 16 2012 Yuri N. Sedunov <aris@altlinux.org> 2.30.1-alt1
- 2.30.1

* Tue Sep 27 2011 Yuri N. Sedunov <aris@altlinux.org> 2.30.0-alt1
- 2.30.0

* Tue Jun 14 2011 Yuri N. Sedunov <aris@altlinux.org> 2.28.2-alt1
- 2.28.2

* Thu May 12 2011 Yuri N. Sedunov <aris@altlinux.org> 2.28.1-alt1
- 2.28.1

* Wed Apr 06 2011 Yuri N. Sedunov <aris@altlinux.org> 2.28.0-alt1
- 2.28.0

* Thu Mar 31 2011 Yuri N. Sedunov <aris@altlinux.org> 2.27.99.2-alt1
- 2.27.99.2

* Wed Mar 23 2011 Yuri N. Sedunov <aris@altlinux.org> 2.27.98-alt1
- 2.27.98

* Tue Mar 15 2011 Yuri N. Sedunov <aris@altlinux.org> 2.27.97-alt1
- 2.27.97

* Mon Feb 28 2011 Yuri N. Sedunov <aris@altlinux.org> 2.27.95-alt1
- 2.27.95

* Mon Feb 21 2011 Yuri N. Sedunov <aris@altlinux.org> 2.27.94-alt1
- 2.27.94

* Wed Feb 09 2011 Yuri N. Sedunov <aris@altlinux.org> 2.27.93-alt1
- 2.27.93

* Sun Oct 03 2010 Yuri N. Sedunov <aris@altlinux.org> 2.25.5-alt1
- 2.25.5

* Tue May 04 2010 Yuri N. Sedunov <aris@altlinux.org> 2.24.2-alt1
- 2.24.2

* Fri Apr 16 2010 Yuri N. Sedunov <aris@altlinux.org> 2.24.1-alt1
- 2.24.1

* Wed Apr 07 2010 Yuri N. Sedunov <aris@altlinux.org> 2.24.0-alt1
- 2.24.0

* Mon Jan 11 2010 Yuri N. Sedunov <aris@altlinux.org> 2.23.1-alt1
- 2.23.1

* Fri Oct 02 2009 Valery Inozemtsev <shrek@altlinux.ru> 2.22.1-alt1
- 2.22.1

* Mon Sep 21 2009 Valery Inozemtsev <shrek@altlinux.ru> 2.20.2-alt1
- 2.20.2

* Tue Nov 04 2008 Vitaly Lipatov <lav@altlinux.ru> 2.18.1-alt1
- new version 2.18.1 (with rpmrb script)

* Sat Apr 12 2008 Vitaly Lipatov <lav@altlinux.ru> 2.16.1-alt1
- new version 2.16.1 (with rpmrb script)

* Sun Jan 13 2008 Vitaly Lipatov <lav@altlinux.ru> 2.14.2-alt1
- new version (2.14.2)
- rename source package to libglibmm
- cleanup spec

* Sun Apr 29 2007 Vitaly Lipatov <lav@altlinux.ru> 2.13.4-alt1
- new version 2.13.4 (with rpmrb script)

* Sat Apr 07 2007 Vitaly Lipatov <lav@altlinux.ru> 2.13.3-alt1
- new version 2.13.3 (with rpmrb script)

* Sun Nov 12 2006 Vitaly Lipatov <lav@altlinux.ru> 2.13.2-alt0.1
- new version 2.13.2 (with rpmrb script)

* Sat Sep 02 2006 Vitaly Lipatov <lav@altlinux.ru> 2.12.0-alt0.1
- new version 2.12.0 (with rpmrb script)

* Fri Jul 21 2006 Vitaly Lipatov <lav@altlinux.ru> 2.11.2-alt0.1
- new version 2.11.2 (with rpmrb script)
- use major in spec

* Tue Feb 21 2006 Vitaly Lipatov <lav@altlinux.ru> 2.9.1-alt0.1
- new version 2.9.1 (with rpmrb script)

* Sun Sep 11 2005 Vitaly Lipatov <lav@altlinux.ru> 2.8.0-alt1
- new version

* Thu Mar 17 2005 Vitaly Lipatov <lav@altlinux.ru> 2.6.1-alt1
- new version

* Thu Jan 20 2005 Vitaly Lipatov <lav@altlinux.ru> 2.5.4-alt1
- new version
- build with gcc3.4

* Sat Dec 18 2004 Vitaly Lipatov <lav@altlinux.ru> 2.5.1-alt1
- new version
- fix static package
- fix descriptions

* Mon Nov 08 2004 Vitaly Lipatov <lav@altlinux.ru> 2.4.5-alt1
- new version

* Sat Sep 04 2004 Vitaly Lipatov <lav@altlinux.ru> 2.4.4-alt1
- new version

* Thu Jul 15 2004 Vitaly Lipatov <lav@altlinux.ru> 2.4.3-alt1
- new version
- use a macro for ldconfig
- remove LICENSE from doc

* Wed Jun 09 2004 Vitaly Lipatov <lav@altlinux.ru> 2.4.2-alt1
- new version

* Mon May 24 2004 Vitaly Lipatov <lav@altlinux.ru> 2.4.1-alt1
- first build for Sisyphus (thanks Mandrake)

* Tue May 04 2004 Abel Cheung <deaddog@deaddog.org> 2.4.1-1mdk
- New version

* Tue Apr 27 2004 Abel Cheung <deaddog@deaddog.org> 2.4.0-1mdk
- First Mandrake package

