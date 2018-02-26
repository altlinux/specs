Name: gobject-introspection
Version: 1.32.1
Release: alt1

Summary: Introspection system for GObject-based libraries
Group: Development/C
License: GPLv2+, LGPLv2+, MIT
URL: http://live.gnome.org/GObjectIntrospection
Packager: Valery Inozemtsev <shrek@altlinux.ru>

Provides: gir-repository = %version-%release
Obsoletes: gir-repository

Source: %name-%version.tar.xz

BuildPreReq: libgio-devel >= 2.32.0
BuildRequires: flex gtk-doc libcairo-devel libcairo-gobject-devel libffi-devel libgio-devel
BuildRequires: python-devel python-modules-ctypes python-modules-compiler rpm-build-gir

%description
GObject Introspection can scan C header and source files in order to
generate introspection "typelib" files.  It also provides an API to examine
typelib files, useful for creating language bindings among other
things.

%package devel
Summary: Libraries and headers for gobject-introspection
Group: Development/C
Requires: %name = %version-%release libgio-devel rpm-build-gir
Provides: gir-repository-devel = %version-%release
Obsoletes: gir-repository-devel

%description devel
Libraries and headers for gobject-introspection

%package devel-doc
Summary: Documentation for gobject-introspection
Group: Development/C
BuildArch: noarch
Conflicts: %name < %version

%description devel-doc
This package provides development documentation for gobject-introspection

%prep
%setup -q

%build
%autoreconf
%configure \
	--disable-static \
	--enable-gtk-doc
%make

%check
%make check

%install
%make DESTDIR=%buildroot install

find %buildroot%_libdir -name \*.la -delete

%files
%_libdir/lib*.so.*
%_libdir/girepository-1.0

%files devel
%_includedir/%name-1.0
%_bindir/g-ir-*
%_libdir/lib*.so
%dir %_libdir/%name
%_libdir/%name/giscanner/
%_pkgconfigdir/*.pc
%_datadir/gir-1.0
%_datadir/%name-1.0
%_datadir/aclocal/*.m4
%_man1dir/*.1*

%files devel-doc
%_datadir/gtk-doc/html/*

%changelog
* Wed Apr 18 2012 Yuri N. Sedunov <aris@altlinux.org> 1.32.1-alt1
- 1.32.1

* Tue Mar 27 2012 Yuri N. Sedunov <aris@altlinux.org> 1.32.0-alt1
- 1.32.0

* Fri Jan 20 2012 Yuri N. Sedunov <aris@altlinux.org> 1.30.0-alt2
- updated from upstream git, in particular fixed build on arm platform

* Mon Oct 24 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.30.0-alt1.1
- Rebuild with Python-2.7

* Fri Sep 23 2011 Yuri N. Sedunov <aris@altlinux.org> 1.30.0-alt1
- 1.30.0

* Tue Aug 30 2011 Yuri N. Sedunov <aris@altlinux.org> 1.29.17-alt1
- 1.29.17

* Fri Aug 12 2011 Yuri N. Sedunov <aris@altlinux.org> 1.29.16-alt1
- 1.29.16

* Thu Jun 30 2011 Yuri N. Sedunov <aris@altlinux.org> 1.29.0-alt1
- 1.29.0

* Sat Mar 26 2011 Yuri N. Sedunov <aris@altlinux.org> 0.10.6-alt1
- 0.10.6

* Fri Mar 11 2011 Yuri N. Sedunov <aris@altlinux.org> 0.10.4-alt1
- 0.10.4

* Fri Feb 25 2011 Yuri N. Sedunov <aris@altlinux.org> 0.10.3-alt1
- 0.10.3

* Wed Feb 09 2011 Yuri N. Sedunov <aris@altlinux.org> 0.10.2-alt1
- 0.10.2

* Mon Jan 31 2011 Alexey Shabalin <shaba@altlinux.ru> 0.10.1-alt1
- 0.10.1
- new devel-doc subpackage (aris@)

* Thu Dec 23 2010 Alexey Shabalin <shaba@altlinux.ru> 0.10.0-alt1
- 0.10.0

* Mon Oct 18 2010 Alexey Shabalin <shaba@altlinux.ru> 0.9.12-alt1
- 0.9.12

* Mon Oct 04 2010 Alexey Shabalin <shaba@altlinux.ru> 0.9.10-alt1
- pre 0.9.11 snapshot
- Obsoletes: gir-repository

* Thu Aug 19 2010 Kirill A. Shutemov <kas@altlinux.org> 0.6.14-alt2
- Rebuild with new libffi.

* Fri Jun 04 2010 Alexey Shabalin <shaba@altlinux.ru> 0.6.14-alt1
- 0.6.14

* Wed May 26 2010 Alexey Shabalin <shaba@altlinux.ru> 0.6.12-alt1
- 0.6.12

* Tue Apr 20 2010 Alexey Shabalin <shaba@altlinux.ru> 0.6.10-alt1
- 0.6.10

* Wed Mar 31 2010 Alexey Shabalin <shaba@altlinux.ru> 0.6.9-alt2
- rebuild with modified rpm-build-gir

* Fri Mar 19 2010 Valery Inozemtsev <shrek@altlinux.ru> 0.6.9-alt1
- 0.6.9

* Fri Mar 12 2010 Valery Inozemtsev <shrek@altlinux.ru> 0.6.8-alt1
- 0.6.8

* Tue Mar 09 2010 Valery Inozemtsev <shrek@altlinux.ru> 0.6.7-alt2
- devel: requires rpm-build-gir

* Thu Dec 24 2009 Valery Inozemtsev <shrek@altlinux.ru> 0.6.7-alt1
- 0.6.7

* Mon Dec 14 2009 Valery Inozemtsev <shrek@altlinux.ru> 0.6.6-alt1
- 0.6.6

* Sun Sep 06 2009 Valery Inozemtsev <shrek@altlinux.ru> 0.6.5-alt1
- 0.6.5

* Tue Aug 25 2009 Valery Inozemtsev <shrek@altlinux.ru> 0.6.4-alt1
- 0.6.4

* Mon Aug 03 2009 Valery Inozemtsev <shrek@altlinux.ru> 0.6.3-alt1
- initial release

