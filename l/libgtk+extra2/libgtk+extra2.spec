%define oname gtk+extra
%define _gtkdocdir %_datadir/gtk-doc/html

Name: libgtk+extra2
Version: 2.1.2
Release: alt2.1

Packager: Vitaly Lipatov <lav@altlinux.ru>

Summary: GtkExtra Widget Set

License: LGPL
Group: System/Libraries
Url: http://gtkextra.sourceforge.net

Source: http://prdownloads.sourceforge.net/gtkextra/%version/%oname-%version.tar
Patch: gtkitementry.patch
Patch1: gtk+extra-2.1.2-alt-make-3.82.patch

# Automatically added by buildreq on Wed Apr 21 2010
BuildRequires: glibc-devel gtk-doc libgtk+2-devel

# _gtkdocdir
BuildPreReq: rpm-build-compat

%description
A library of dynamically linked gtk+ widgets including
GtkSheet, GtkPlot, and GtkIconList

%package devel
Summary: GtkExtra Widget Set header files
Group: Development/C
Requires: %name = %version-%release

%description devel
This package contents development files
for compiling programs that use gtk+extra widgets.

%package devel-docs
Summary: Documentation for GtkExtra Widget Set
Group: Development/Documentation
BuildArch: noarch
Conflicts: %name-devel < %version-%release

%description devel-docs
This package contents development documentation
for gtk+extra widgets.

%prep
%setup -n %oname-%version
subst "s|#include <glib/gunicode.h>||g" gtkextra/gtkcharsel.c

%patch -p2
%patch1 -p2
#chmod -x ChangeLog

%build
%configure \
	--disable-static \
	--enable-gtk-doc
%make_build

%install
%makeinstall_std

cp -fR docs/tutorial %buildroot%_gtkdocdir/

%files
%doc AUTHORS README ChangeLog
%_libdir/*.so.*

%files devel
%_includedir/*
%_libdir/*.so
%_pkgconfigdir/*

%files devel-docs
%_gtkdocdir/*

%changelog
* Thu Dec 06 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.1.2-alt2.1
- Fixed build with make 3.82
- Extracted docs into separate package

* Sun May 06 2012 Vitaly Lipatov <lav@altlinux.ru> 2.1.2-alt2
- fix build without direct glib/ using

* Tue Nov 09 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.1.2-alt1.1
- Rebuilt for soname set-versions

* Wed Apr 21 2010 Vitaly Lipatov <lav@altlinux.ru> 2.1.2-alt1
- build new version, cleanup spec

* Sun Jan 08 2006 Vitaly Lipatov <lav@altlinux.ru> 2.1.1-alt0.1
- new version

* Sun Sep 11 2005 Vitaly Lipatov <lav@altlinux.ru> 2.1.0-alt0.1
- new version

* Mon Jan 17 2005 Vitaly Lipatov <lav@altlinux.ru> 1.1.0-alt0.1snap20050102
- gtk2 version

* Mon Dec 06 2004 Vitaly Lipatov <lav@altlinux.ru> 0.99.17-alt2
- update spec
- revert to Sisyphus for eas build support

* Thu Nov 14 2002 Stanislav Ievlev <inger@altlinux.ru> 0.99.17-alt1
- 0.99.17
- return real packager tag

* Mon Nov 12 2001 Stanislav Ievlev <inger@altlinux.ru> 0.99.16-alt2
- small spec cleanups

* Mon Nov 12 2001 Yuri N. Sedunov <aris@altlinux.ru> 0.99.16-alt1
- First build for Sisyphus
