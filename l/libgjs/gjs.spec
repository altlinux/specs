%define ver_major 1.32
%define _name gjs

Name: lib%_name
Version: %ver_major.0
Release: alt1

Summary: Javascript Bindings for GNOME
Group: System/Libraries
# The following files contain code from Mozilla which
# is triple licensed under MPL1.1/LGPLv2+/GPLv2+:
# The console module (modules/console.c)
# Stack printer (gjs/stack.c)
License: MIT and (MPLv1.1 or GPLv2+ or LGPLv2+)
Url: http://live.gnome.org/Gjs/

Source: ftp://ftp.gnome.org/pub/gnome/sources/%_name/%ver_major/%_name-%version.tar.xz
#Source: %_name-%version.tar
Patch: %_name-1.31.10-alt-gi.patch

%define glib_ver 2.32.0
%define gi_ver 1.32.0

BuildRequires: gcc-c++ libmozjs-devel >= 1.8.5 libcairo-devel
BuildRequires: glib2-devel >= %glib_ver gobject-introspection-devel >= %gi_ver
BuildRequires: libdbus-glib-devel libreadline-devel libcairo-gobject-devel

# for check
BuildRequires: /proc dbus-tools-gui

%description
Gjs allows using GNOME libraries from Javascript. It's based on the
Spidermonkey Javascript engine from Mozilla and the GObject introspection
framework.

%package devel
Summary: Development package for %name
Group: Development/C
Requires: %name = %version-%release

%description devel
Files for development with %name.

%prep
%setup -q -n %_name-%version
%patch -b .gi

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
%_bindir/gjs
%_bindir/gjs-console
%_libdir/*.so.*
%dir %_libdir/gjs-1.0
%_libdir/gjs-1.0/*.so

%_typelibdir/GjsDBus-1.0.typelib

%_datadir/gjs-1.0
%doc COPYING NEWS README

%exclude %_libdir/gjs-1.0/*.la

%files devel
%_includedir/gjs-1.0
%_libdir/*.so
%_libdir/pkgconfig/gjs-1.0.pc
%_libdir/pkgconfig/gjs-dbus-1.0.pc
%_libdir/pkgconfig/gjs-internals-1.0.pc

%_girdir/GjsDBus-1.0.gir

%doc examples/*

%changelog
* Tue Mar 27 2012 Yuri N. Sedunov <aris@altlinux.org> 1.32.0-alt1
- 1.32.0

* Sat Jan 14 2012 Yuri N. Sedunov <aris@altlinux.org> 1.30.1-alt1
- 1.30.1

* Tue Sep 27 2011 Yuri N. Sedunov <aris@altlinux.org> 1.30.0-alt1
- 1.30.0

* Mon Sep 05 2011 Yuri N. Sedunov <aris@altlinux.org> 0.7.14-alt5
- rebuilt against libmozjs-1.8.5 not xulrunner.

* Thu Aug 25 2011 Yuri N. Sedunov <aris@altlinux.org> 0.7.14-alt4
- Rebuild against new xulrunner 6.0.
- disabled tests temporarily.

* Tue Aug 02 2011 Paul Wolneykien <manowar@altlinux.ru> 0.7.14-alt3
- Rebuild against new xulrunner 5.0.
- Use patches related to GNOME bug #646471.

* Sun Apr 10 2011 Yuri N. Sedunov <aris@altlinux.org> 0.7.14-alt2
- rebuilt against new xulrunner-2.0

* Mon Apr 04 2011 Yuri N. Sedunov <aris@altlinux.org> 0.7.14-alt1
- 0.7.14

* Fri Mar 11 2011 Yuri N. Sedunov <aris@altlinux.org> 0.7.13-alt1
- 0.7.13

* Wed Feb 23 2011 Yuri N. Sedunov <aris@altlinux.org> 0.7.11-alt1
- 0.7.11

* Wed Jan 26 2011 Yuri N. Sedunov <aris@altlinux.org> 0.7.10-alt1
- 0.7.10

* Wed Oct 06 2010 Yuri N. Sedunov <aris@altlinux.org> 0.7.4-alt1
- 0.7.4

* Sun Oct 03 2010 Yuri N. Sedunov <aris@altlinux.org> 0.7.3-alt1
- 0.7.3

* Sun Aug 29 2010 Yuri N. Sedunov <aris@altlinux.org> 0.7.1-alt1
- 0.7.1

* Fri Mar 19 2010 Yuri N. Sedunov <aris@altlinux.org> 0.6-alt1
- 0.6

* Sat Mar 13 2010 Yuri N. Sedunov <aris@altlinux.org> 0.5-alt2
- build current snapshot
- updated buildreqs

* Tue Feb 16 2010 Yuri N. Sedunov <aris@altlinux.org> 0.5-alt1
- 0.5

* Tue Aug 25 2009 Yuri N. Sedunov <aris@altlinux.org> 0.4-alt1
- 0.4

* Thu Aug 13 2009 Yuri N. Sedunov <aris@altlinux.org> 0.3-alt1
- adapted for Sisyphus

* Fri Aug  7 2009 Peter Robinson <pbrobinson@gmail.com> 0.3-2
- Updates from the review request

* Wed Jul  8 2009 Peter Robinson <pbrobinson@gmail.com> 0.3-1
- New upstream release. Clarify licensing for review

* Sat Jun 27 2009 Peter Robinson <pbrobinson@gmail.com> 0.2-1
- Initial packaging
