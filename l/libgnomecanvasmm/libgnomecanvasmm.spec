%define pkgname gnomecanvasmm
%define api_version 2.6
%define major 2.26

Name: libgnomecanvasmm
Version: %major.0
Release: alt1.qa1

Summary: A C++ interface for GNOME 2 canvas library
License: LGPL
Group: System/Libraries
Url: http://gtkmm.sourceforge.net/

Packager: Vitaly Lipatov <lav@altlinux.ru>

Source: ftp://ftp.gnome.org/pub/gnome/sources/libgnomecanvasmm/%major/%name-%version.tar.bz2

# Automatically added by buildreq on Sun Jan 13 2008
BuildRequires: doxygen gcc-c++ libgnomecanvas-devel libgtkmm2-devel

BuildRequires: libgtkmm2-devel >= 2.8.0

%description
This package provides a C++ interface for gnomecanvas2. It is a subpackage
of the Gtk-- project.  The interface provides a convenient interface for C++
programmers to create GNOME GUIs with GTK+'s flexible object-oriented
framework.

%package devel
Summary: Headers and development files of GNOME 2 canvas library
Group: Development/GNOME and GTK+
Requires: %name = %version-%release

%description devel
This package contains the headers and various development files needed
for compiling or development of applications that wants C++ interface
of GNOME 2 canvas library.

%package doc
Summary: Documentation for %name library
Group: Development/C++
BuildArch: noarch
Conflicts: %name < %version

%description doc
This package provides API documentation for %name library.

%prep
%setup -q

%build
%configure \
		--disable-maintainer-mode \
		--disable-static \
		--enable-shared

%make_build
cd docs/reference && %make

%install
%makeinstall_std

%files
%doc README
%_libdir/*.so.*

%files devel
%doc AUTHORS ChangeLog NEWS 
%_includedir/lib%pkgname-%api_version/
%_libdir/*.so
%_libdir/lib%pkgname-%api_version/
%_pkgconfigdir/*.pc

%files doc
%doc docs/reference/html

%changelog
* Sat Nov 27 2010 Igor Vlasenko <viy@altlinux.ru> 2.26.0-alt1.qa1
- rebuild using girar-nmu to require/provide setversion 
  by request of mithraen@

* Tue Nov 24 2009 Yuri N. Sedunov <aris@altlinux.org> 2.26.0-alt1
- 2.26.0
- removed obsolete *ldconfig from %%post{,un}

* Tue Nov 04 2008 Vitaly Lipatov <lav@altlinux.ru> 2.23.1-alt1
- new version 2.23.1 (with rpmrb script)

* Tue Apr 15 2008 Vitaly Lipatov <lav@altlinux.ru> 2.22.0-alt1
- new version 2.22.0 (with rpmrb script)

* Sun Jan 13 2008 Vitaly Lipatov <lav@altlinux.ru> 2.20.0-alt1
- new version 2.20.0
- cleanup spec, remove COPYING
- update buildreq

* Sat Sep 02 2006 Vitaly Lipatov <lav@altlinux.ru> 2.16.0-alt0.1
- new version 2.16.0 (with rpmrb script)

* Sat Jul 22 2006 Vitaly Lipatov <lav@altlinux.ru> 2.14.0-alt0.1
- new version 2.14.0 (with rpmrb script)

* Sun Sep 11 2005 Vitaly Lipatov <lav@altlinux.ru> 2.12.0-alt1
- new version

* Thu Mar 17 2005 Vitaly Lipatov <lav@altlinux.ru> 2.10.0-alt1
- new version

* Fri Jan 21 2005 Vitaly Lipatov <lav@altlinux.ru> 2.8.0-alt1
- new version
- build with gcc3.4
- use a macro for ldconfig

* Sun Jun 06 2004 Vitaly Lipatov <lav@altlinux.ru> 2.6.1-alt1
- new version

* Sun Feb 15 2004 Vitaly Lipatov <lav@altlinux.ru> 2.0.1-alt1
- first build for Sisyphus (thanks Mandrake)

* Mon Feb 09 2004 Abel Cheung <deaddog@deaddog.org> 2.0.1-4mdk
- Fix BuildRequires

* Fri Sep 05 2003 Abel Cheung <deaddog@deaddog.org> 2.0.1-3mdk
- Replace my changelog with Austin's
- Add missing BuildRequires

* Fri Sep 05 2003 Abel Cheung <deaddog@deaddog.org> 2.0.1-2mdk
- Provides basic package name as well

* Sun Aug 24 2003 Austin Acton <aacton@yorku.ca> 2.0.1-1mdk
- 2.0.1
- don't use configure macro
- try to revert to standard name
- adopt Abel's changes (build doc, build static lib)

* Wed Aug 13 2003 Abel Cheung <maddog@linux.org.hk> 2.0.0-2mdk
- Build static library as well
- Spec file rename to libgnomecanvasmm2.0
- Misc spec file tweaks
- Provides/Obsoletes gnomecanvasmm2.0{,-devel} is unnecessary since
  nothing requires them
- Build docs

* Sun Apr 6 2003 Austin Acton <aacton@yorku.ca> 2.0.0-1mdk
- initial package
