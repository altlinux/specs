Name: mypaint
Version: 1.1.0
Release: alt1

Summary: A simple paint program
Group: Graphics
License: GPLv2+
Url: http://mypaint.info/

Source: http://download.gna.org/%name/%name-%version.tar.bz2

Requires: %name-data = %version-%release
# python.req bug?
Requires: python-module-protobuf python-modules-json
# A cause to modify rpm-build-gir -- both Gtk+{2,3} gir-packages provide typelib(Gtk)
Requires: libgtk+2-gir

BuildRequires: gcc-c++ glib2-devel python-devel libnumpy-devel scons swig protobuf-compiler
BuildRequires: libpng-devel libjson-devel python-modules-json liblcms2-devel libgtk+2-devel
BuildRequires: python-module-pygobject-devel gobject-introspection-devel

%description
Mypaint is a fast and easy/simple painter program. It comes with a large
brush collection including charcoal and ink to emulate real media, but the
highly configurable brush engine allows you to experiment with your own
brushes and with not-quite-natural painting.

%package data
Summary: A simple paint program
Group: Graphics
BuildArch: noarch

%description data
Mypaint is a fast and easy/simple painter program. It comes with a large
brush collection including charcoal and ink to emulate real media, but the
highly configurable brush engine allows you to experiment with your own
brushes and with not-quite-natural painting.

This package contains the data files needed for the program.

%package -n lib%name-devel-static
Summary: Static mypaint brush library
Group: Development/C

%description -n lib%name-devel-static
Mypaint is a fast and easy/simple painter program. It comes with a large
brush collection including charcoal and ink to emulate real media, but the
highly configurable brush engine allows you to experiment with your own
brushes and with not-quite-natural painting.

This package provides files needed for development applications statically linked
with mypaint brush library.

%add_python_lib_path %_datadir/%name

%prep
%setup -q
# fix libdir
subst 's|lib\/mypaint|%_lib\/mypaint|' SConstruct SConscript mypaint.py
subst 's|prefix\/lib|prefix\/%_lib|' brushlib/SConscript
# fix pkgconfig-file by preventing substitution
subst 's|@LIBDIR@|%_libdir|' brushlib/pkgconfig.pc.in

%build
scons

%install
scons prefix=%buildroot%_prefix install
%find_lang %name

%files -f %name.lang
%_bindir/*
%_libdir/%name

%files data
%_datadir/%name
%_datadir/applications/*
%_iconsdir/hicolor/*/*/*
%doc README changelog

%if 0
%files -n lib%name-devel-static
%_libdir/lib%name.a
%_includedir/lib%name/
%_pkgconfigdir/lib%name.pc
%endif

%changelog
* Fri Jan 25 2013 Yuri N. Sedunov <aris@altlinux.org> 1.1.0-alt1
- 1.1.0

* Sun Apr 15 2012 Yuri N. Sedunov <aris@altlinux.org> 1.0.0-alt2
- rebuilt to remove libpython2.7 dependency

* Thu Nov 24 2011 Yuri N. Sedunov <aris@altlinux.org> 1.0.0-alt1
- 1.0.0

* Tue Oct 25 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.9.1-alt3.1
- Rebuild with Python-2.7

* Fri Jun 24 2011 Yuri N. Sedunov <aris@altlinux.org> 0.9.1-alt3
- replaced obsolete python-module-json by python-modules-json

* Mon May 02 2011 Yuri N. Sedunov <aris@altlinux.org> 0.9.1-alt2
- rebuild against current numpy

* Sat Mar 05 2011 Yuri N. Sedunov <aris@altlinux.org> 0.9.1-alt1
- 0.9.1

* Tue Jan 04 2011 Yuri N. Sedunov <aris@altlinux.org> 0.9.0-alt2
- explicitly requires python-module-json

* Sun Dec 19 2010 Yuri N. Sedunov <aris@altlinux.org> 0.9.0-alt1
- 0.9.0 (ALT #24610)

* Mon Jul 26 2010 Yuri N. Sedunov <aris@altlinux.org> 0.8.2-alt2
- rebuild against current numpy (closes #23769)

* Mon Mar 01 2010 Yuri N. Sedunov <aris@altlinux.org> 0.8.2-alt1
- 0.8.2

* Mon Feb 22 2010 Yuri N. Sedunov <aris@altlinux.org> 0.8.1-alt1
- new version

* Fri Feb 19 2010 Yuri N. Sedunov <aris@altlinux.org> 0.8.0-alt2
- %%_bindir/mypaint moved to main arch dependent package

* Sun Jan 31 2010 Yuri N. Sedunov <aris@altlinux.org> 0.8.0-alt1
- 0.8.0

* Fri Jan 29 2010 Yuri N. Sedunov <aris@altlinux.org> 0.7.1-alt1
- first build for Sisyphus

