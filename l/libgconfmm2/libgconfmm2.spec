%define _name gconfmm
%define api_version 2.6
%define major 2.28

Name: libgconfmm2
Version: %major.2
Release: alt2

Summary: A C++ interface for GConf2
License: LGPL
Group: System/Libraries
Url: http://gtkmm.sourceforge.net/

Packager: Vitaly Lipatov <lav@altlinux.ru>

Source: http://ftp.gnome.org/pub/GNOME/sources/%_name/%major/%_name-%version.tar.bz2

BuildPreReq: doxygen
BuildRequires: mm-common gcc-c++ libGConf-devel libgtkmm2-devel

%description
This package provides a C++ interface for gconf2.  It is a subpackage
of the Gtk-- project.  The interface provides a convenient interface for C++
programmers to create Gnome GUIs with GTK+'s flexible object-oriented
framework.

%package devel
Summary: Headers and development files of GConf 2 C++ wrapper
Group: Development/GNOME and GTK+
Requires: %name = %version-%release

%description devel
This package contains the headers and various development files needed,
when compiling or developing programs which want GConf 2 C++ wrapper.

%package doc
Summary: Documentation of %_name library
Group: Development/C++
BuildArch: noarch
Conflicts: %name-devel < %version

%description doc
This package provides API documentation of %_name library.

%define pkgdocdir %_docdir/%_name-%api_version

%prep
%setup -q -n %_name-%version

%build
mm-common-prepare
%autoreconf
%configure \
           --disable-static \
           --enable-shared

%make_build

%install
%make DESTDIR=%buildroot install

%files
%_libdir/*.so.*
%doc AUTHORS NEWS README

%files devel
%_includedir/%_name-%api_version/
%_libdir/%_name-%api_version/
%_pkgconfigdir/%_name-%api_version.pc
%_libdir/*.so

%files doc
%_datadir/devhelp/books/*
%pkgdocdir/reference/

%changelog
* Thu Apr 21 2011 Yuri N. Sedunov <aris@altlinux.org> 2.28.2-alt2
- rebuild using new mm-common

* Thu Nov 25 2010 Igor Vlasenko <viy@altlinux.ru> 2.28.2-alt1.qa1
- rebuild using girar-nmu to require/provide setversion 
  by request of mithraen@

* Wed Jun 16 2010 Yuri N. Sedunov <aris@altlinux.org> 2.28.2-alt1
- 2.28.2

* Tue Nov 24 2009 Yuri N. Sedunov <aris@altlinux.org> 2.28.0-alt1
- 2.28.0
- removed obsolete *ldconfig from %%post{,un}
- new -doc noarch package

* Tue Nov 04 2008 Vitaly Lipatov <lav@altlinux.ru> 2.24.0-alt1
- new version 2.24.0 (with rpmrb script)

* Tue Apr 15 2008 Vitaly Lipatov <lav@altlinux.ru> 2.22.0-alt1
- new version 2.22.0 (with rpmrb script)

* Sun Jan 13 2008 Vitaly Lipatov <lav@altlinux.ru> 2.20.0-alt1
- new version 2.20.0 (with rpmrb script)
- rename source package to libgconfmm2
- clean spec, update buildreq, remove COPYING.LIB

* Sat Apr 07 2007 Vitaly Lipatov <lav@altlinux.ru> 2.18.0-alt1
- new version 2.18.0 (with rpmrb script)

* Sat Sep 02 2006 Vitaly Lipatov <lav@altlinux.ru> 2.16.0-alt0.1
- new version 2.16.0 (with rpmrb script)

* Fri Jul 21 2006 Vitaly Lipatov <lav@altlinux.ru> 2.14.2-alt0.1
- new version 2.14.2 (with rpmrb script)
- enable examples again

* Sun Sep 11 2005 Vitaly Lipatov <lav@altlinux.ru> 2.12.0-alt1
- new version

* Thu Mar 17 2005 Vitaly Lipatov <lav@altlinux.ru> 2.10.0-alt1
- new version

* Fri Jan 21 2005 Vitaly Lipatov <lav@altlinux.ru> 2.9.2-alt1
- new version
- build with gcc3.4

* Mon May 24 2004 Vitaly Lipatov <lav@altlinux.ru> 2.6.1-alt1
- new version

* Sun Feb 15 2004 Vitaly Lipatov <lav@altlinux.ru> 2.0.1-alt1
- first build for Sisyphus (thanks Mandrake)

* Fri Aug 29 2003 Abel Cheung <deaddog@deaddog.org> 2.0.1-5mdk
- Can't even fix changelog? Counter black magic with black magic

* Fri Aug 29 2003 Abel Cheung <deaddog@deaddog.org> 2.0.1-4mdk
- Rebuild again, main library RPM vaporized (Thx Austin)
- Relax -devel requirement a little bit

* Fri Aug 22 2003 Abel Cheung <maddog@linux.org.hk> 2.0.1-3mdk
- Rebuild against new gtkmm

* Wed Aug 13 2003 Abel Cheung <maddog@linux.org.hk> 2.0.1-2mdk
- Enable static libraries
- Other spec tweaks

* Sun Apr 6 2003 Austin Acton <aacton@yorku.ca> 2.0.0-1mdk
- initial package
