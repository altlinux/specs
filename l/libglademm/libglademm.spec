%define devhelp_bookdir %_datadir/devhelp/books

%define req_libglade_version 2.5.1
%define req_gtkmm_version 2.12.0

%define api_version 2.4
%define libname_basic glademm
%define major 2.6

Name: libglademm
Version: %major.7
Release: alt2.qa1
Summary: C++ interface of glade2 library
License: LGPL
Group: System/Libraries
Url: http://gtkmm.sourceforge.net/
Packager: GNOME Maintainers Team <gnome@packages.altlinux.org>

Source: http://ftp.gnome.org/pub/GNOME/sources//%name/%major/%name-%version.tar.bz2

BuildRequires: doxygen gcc-c++ graphviz libglade-devel libgtkmm2-devel xsltproc
BuildPreReq: libglade2-devel >= %req_libglade_version
BuildPreReq: libgtkmm2-devel >= %req_gtkmm_version

%description
This package provides a C++ interface for glade2.  It is a subpackage
of the Gtk-- project.  The interface provides a convenient interface for C++
programmers to create glade2 objects.

%package devel
Summary: Development related files of %name
Group: Development/GNOME and GTK+
Requires: %name = %version-%release
Requires: libglade2-devel >= %req_libglade_version

%description devel
Thie package provides headers and various development files needed for
compiling or developing applications that use Glade 2 C++ interface.

%package doc
Summary: Documentation for %name
Group: Development/GNOME and GTK+

%description doc
Thie package provides documentation for
compiling or developing applications that use Glade 2 C++ interface.

%prep
%setup -q
subst "s|gnomemm-2.6/libglademm-2.4/docs|%name-%version|g" docs/reference/doxygen_to_devhelp.xsl

%build
%configure \
	--disable-static

%make_build

%install
%make DESTDIR=%buildroot docdir=%_docdir/%name-doc-%version install

%files
%doc AUTHORS
%_libdir/%{name}*.so.*

%files devel
%doc AUTHORS ChangeLog INSTALL
%_includedir/*
%_libdir/%name-%api_version
%_pkgconfigdir/%name-%api_version.pc
%_libdir/%{name}*.so

%files doc
%devhelp_bookdir/%name-%api_version/
%_docdir/%name-doc-%version

%changelog
* Thu Nov 25 2010 Igor Vlasenko <viy@altlinux.ru> 2.6.7-alt2.qa1
- rebuild using girar-nmu to require/provide setversion 
  by request of mithraen@

* Sun Sep 27 2009 Valery Inozemtsev <shrek@altlinux.ru> 2.6.7-alt2
- fixed build

* Tue Nov 04 2008 Vitaly Lipatov <lav@altlinux.ru> 2.6.7-alt1
- new version 2.6.7 (with rpmrb script)

* Sun Apr 13 2008 Vitaly Lipatov <lav@altlinux.ru> 2.6.6-alt1
- new version 2.6.6 (with rpmrb script)

* Sun Jan 13 2008 Vitaly Lipatov <lav@altlinux.ru> 2.6.5-alt1
- new version 2.6.5 (with rpmrb script)
- cleanup spec, update buildreq

* Sat Sep 02 2006 Vitaly Lipatov <lav@altlinux.ru> 2.6.3-alt0.1
- new version 2.6.3 (with rpmrb script)

* Fri Jul 21 2006 Vitaly Lipatov <lav@altlinux.ru> 2.6.2-alt0.1
- new version 2.6.2 (with rpmrb script)

* Sun Sep 11 2005 Vitaly Lipatov <lav@altlinux.ru> 2.6.1-alt1
- new version

* Thu Mar 17 2005 Vitaly Lipatov <lav@altlinux.ru> 2.6.0-alt1
- new version

* Tue Jan 25 2005 Vitaly Lipatov <lav@altlinux.ru> 2.5.1-alt1.1
- fix buildreq

* Thu Jan 20 2005 Vitaly Lipatov <lav@altlinux.ru> 2.5.1-alt1
- new version
- build with gcc3.4
- use a macro for ldconfig

* Sat Jun 19 2004 Vitaly Lipatov <lav@altlinux.ru> 2.4.1-alt1
- new version
- remove COPYING from files
- split doc package

* Mon May 31 2004 Vitaly Lipatov <lav@altlinux.ru> 2.4.0-alt1
- new version

* Sun Feb 15 2004 Vitaly Lipatov <lav@altlinux.ru> 2.1.2-alt1
- first build for Sisyphus

* Sat Nov 01 2003 Abel Cheung <deaddog@deaddog.org> 2.1.2-3mdk
- Revert previous change (Don't blindly add provides, libglademm and
  glademm are entirely different thing)

* Wed Oct 29 2003 Per Øyvind Karlsen <peroyvind@linux-mandrake.com> 2.1.2-2mdk
- provides (lib64..)

* Thu Oct 02 2003 Abel Cheung <deaddog@deaddog.org> 2.1.2-1mdk
- 2.1.2
- Patch1: Make libtool 1.5 always search for staging libraries first
  during relinking
- Provides plain package name

* Wed Aug 13 2003 Abel Cheung <maddog@linux.org.hk> 2.0.1-1mdk
- Rename glademm2.0 -> libglademm2.0, avoid confusion with
  the real glademm package
- Build static library
- Build doc
- Need not provide glademm2.0{,-devel} since nothing require them
- Patch0: Fix doc/reference/Doxyfile (which was having old variable that
  belongs to gnomeuimm package)

* Sun Apr 6 2003 Austin Acton <aacton@yorku.ca> 1.3.10-1mdk
- initial package
