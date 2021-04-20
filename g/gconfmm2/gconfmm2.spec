%define pkgname gconfmm
%define api_version 2.6
Name: gconfmm2
Version: 2.28.3
Release: alt1

Summary: A C++ interface for GConf2
License: LGPLv2.1
Group: System/Libraries
Url: http://gtkmm.sourceforge.net/
#https://download.gnome.org/sources/gconfmm/2.28/
Source: %name-%version.tar
Patch0: gconfmm26-2.28.3-no-extern-c-glib-includes.patch
BuildRequires: gcc-c++ libGConf-devel libglibmm-devel libgtkmm2-devel libsigc++2.0-devel pkg-config

%description
This package provides a C++ interface for gconf2.  It is a subpackage
of the Gtk-- project.  The interface provides a convenient interface for C++
programmers to create Gnome GUIs with GTK+'s flexible object-oriented
framework.

%package -n lib%name
Summary: %summary
Group: %group

%description -n lib%name
This package provides a C++ interface for gconf2.  It is a subpackage
of the Gtk-- project.  The interface provides a convenient interface for C++
programmers to create Gnome GUIs with GTK+'s flexible object-oriented
framework.

%package -n lib%name-devel
Summary: Headers and development files of GConf 2 C++ wrapper
Group: Development/GNOME and GTK+
Requires: lib%name = %version

%description -n lib%name-devel
This package contains the headers and various development files needed,
when compiling or developing programs which want GConf 2 C++ wrapper.

%prep
%setup -q 
%patch0 -p1

%build
%configure --disable-static

%make

%install
%makeinstall

%files -n lib%name
%doc COPYING.LIB
%_libdir/*.so.*

%files -n lib%name-devel
%doc AUTHORS COPYING.LIB ChangeLog NEWS README
%_includedir/*
%_libdir/%pkgname-%api_version
%_pkgconfigdir/*.pc
%_libdir/*.so

%changelog
* Tue Apr 20 2021 Anton Farygin <rider@altlinux.ru> 2.28.3-alt1
- 2.28.3
- added patch from RH against FTBFS with "extern C"

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
