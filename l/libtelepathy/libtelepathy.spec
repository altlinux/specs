Name: libtelepathy
Version: 0.3.3
Release: alt2.1

Summary: Telepathy Client Library
License: LGPL
Group: System/Libraries
Url: http://telepathy.freedesktop.org/wiki/

Source0: http://telepathy.freedesktop.org/releases/libtelepathy/%name-%version.tar.gz

Packager: Igor Zubkov <icesik@altlinux.org>

# from configure.in
%define dbus_ver 0.61
%define dbus_glib_ver 0.61

Requires: libdbus >= %dbus_ver
BuildPreReq: libdbus-devel >= %dbus_ver
Requires: libdbus-glib >= %dbus_glib_ver
BuildPreReq: libdbus-glib-devel >= %dbus_glib_ver

# Automatically added by buildreq on Tue Dec 04 2007
BuildRequires: gcc-c++ python-module-PyXML python-modules-compiler telepathy-glib-devel xsltproc

%description
The Telepathy project aims to provide a unified framework for all forms
of real time conversations, including instant messaging, IRC, voice calls
and video calls. It uses the D-Bus messaging system to provide a simple
interface for client applications, allowing them to quickly benefit from
Telepathy's functionality.

%package devel
Summary: Development libraries and header files for %name
Group: Development/C
Requires: %name = %version-%release

%description devel
Development libraries and header files for %name.

%prep
%setup -q

%build
%configure \
		--disable-static
%make_build

%install
%make_install DESTDIR=%buildroot install

%files
%doc AUTHORS ChangeLog README
%_libdir/lib*.so.*

%files devel
%_libdir/lib*.so
%_pkgconfigdir/libtelepathy.pc
%dir %_includedir/telepathy-1.0
%dir %_includedir/telepathy-1.0/libtelepathy
%_includedir/telepathy-1.0/libtelepathy/*.h

%changelog
* Fri Nov 06 2009 Repocop Q. A. Robot <repocop@altlinux.org> 0.3.3-alt2.1
- NMU (by repocop): the following fixes applied:
  * post_ldconfig for libtelepathy
  * postun_ldconfig for libtelepathy

* Mon May 05 2008 Igor Zubkov <icesik@altlinux.org> 0.3.3-alt2
- fix for fresh sisyphus_check

* Sat Feb 23 2008 Igor Zubkov <icesik@altlinux.org> 0.3.3-alt1
- 0.3.1 -> 0.3.3

* Tue Dec 04 2007 Igor Zubkov <icesik@altlinux.org> 0.3.1-alt1
- 0.3.0 -> 0.3.1
- buildreq

* Tue Dec 04 2007 Igor Zubkov <icesik@altlinux.org> 0.3.0-alt1
- 0.2.0 -> 0.3.0
- buildreq

* Fri Sep 28 2007 Igor Zubkov <icesik@altlinux.org> 0.2.0-alt1
- 0.0.58 -> 0.2.0

* Wed Sep 26 2007 Igor Zubkov <icesik@altlinux.org> 0.0.58-alt1
- 0.0.57 -> 0.0.58

* Fri Sep 07 2007 Igor Zubkov <icesik@altlinux.org> 0.0.57-alt1
- 0.0.55 -> 0.0.57

* Fri Jun 22 2007 Igor Zubkov <icesik@altlinux.org> 0.0.55-alt1
- build for Sisyphus


