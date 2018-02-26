%define ver_major 0.10
%define _gst_libdir %_libdir/gstreamer-%ver_major

Name: python-module-gst
Version: 0.10.22
Release: alt2
Summary: Python bindings for GStreamer
Group: Development/Python
License: LGPL
Url: http://gstreamer.freedesktop.org/
Packager: Valery Inozemtsev <shrek@altlinux.ru>

Provides: gst-python = %version-%release

Source: %name-%version.tar
Source1: common.tar
Patch: %name-%version-%release.patch

%setup_python_module gst

BuildRequires: gst-plugins-devel python-module-pygtk-devel python-module-pygobject-devel python-modules-compiler

%description
This module contains a wrapper that allows GStreamer applications
to be written in Python.

%package devel
Summary: Python development files for Gstreamer
Group: Development/Python
Requires: %name = %version-%release

%description devel
Python development files for Gstreamer

%prep
%setup -q -a1
%patch -p1

mkdir -p m4

%build
%autoreconf
%configure
%make_build

%install
%make DESTDIR=%buildroot install

rm -fr %buildroot%_datadir/gst-python/%ver_major/examples
find %buildroot -type f -name \*.la -delete

%files
%doc AUTHORS NEWS
%python_sitelibdir/*
#_gst_libdir/*.so
%_datadir/gst-python

%files devel
%_includedir/gstreamer-%ver_major
%_pkgconfigdir/gst-python-0.10.pc

%changelog
* Thu May 10 2012 Valery Inozemtsev <shrek@altlinux.ru> 0.10.22-alt2
- acinclude.m4: use python-config --libs for libs, not --ldflags

* Tue Nov 01 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.10.22-alt1.1
- Rebuild with Python-2.7

* Tue Nov 01 2011 Valery Inozemtsev <shrek@altlinux.ru> 0.10.22-alt1
- 0.10.22

* Mon Mar 28 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.10.21-alt1.1
- Rebuilt for debuginfo

* Sat Jan 22 2011 Valery Inozemtsev <shrek@altlinux.ru> 0.10.21-alt1
- 0.10.21

* Thu Dec 02 2010 Valery Inozemtsev <shrek@altlinux.ru> 0.10.20-alt1
- 0.10.20

* Fri Jul 23 2010 Valery Inozemtsev <shrek@altlinux.ru> 0.10.19-alt1
- 0.10.19

* Thu Feb 11 2010 Valery Inozemtsev <shrek@altlinux.ru> 0.10.18-alt1
- 0.10.18

* Mon Oct 05 2009 Valery Inozemtsev <shrek@altlinux.ru> 0.10.17-alt1
- 0.10.17

* Sun Aug 30 2009 Valery Inozemtsev <shrek@altlinux.ru> 0.10.16.1-alt1
- 0.10.16.1

* Wed Aug 05 2009 Valery Inozemtsev <shrek@altlinux.ru> 0.10.16-alt1
- 0.10.16

* Wed Jul 08 2009 Valery Inozemtsev <shrek@altlinux.ru> 0.10.15-alt2
- rebuild

* Mon May 11 2009 Valery Inozemtsev <shrek@altlinux.ru> 0.10.15-alt1
- 0.10.15

* Sun Apr 26 2009 Valery Inozemtsev <shrek@altlinux.ru> 0.10.14-alt1
- 0.10.14

* Wed Jun 18 2008 Igor Zubkov <icesik@altlinux.org> 0.10.12-alt1
- 0.10.11 -> 0.10.12

* Sat May 24 2008 Igor Zubkov <icesik@altlinux.org> 0.10.11-alt1
- 0.10.10 -> 0.10.11

* Fri May 16 2008 Igor Zubkov <icesik@altlinux.org> 0.10.10-alt2
- rebuild

* Sun Feb 24 2008 Igor Zubkov <icesik@altlinux.org> 0.10.10-alt1
- 0.10.9 -> 0.10.10

* Mon Feb 11 2008 Grigory Batalov <bga@altlinux.ru> 0.10.9-alt2.1
- Rebuilt with python-2.5.

* Mon Feb 11 2008 Grigory Batalov <bga@altlinux.ru> 0.10.9-alt2
- Link with current python version.

* Fri Nov 30 2007 Igor Zubkov <icesik@altlinux.org> 0.10.9-alt1
- 0.10.8 -> 0.10.9

* Fri Oct 12 2007 Igor Zubkov <icesik@altlinux.org> 0.10.8-alt2
- fix rebuild with new rpm

* Thu Sep 06 2007 Igor Zubkov <icesik@altlinux.org> 0.10.8-alt1
- 0.10.7 -> 0.10.8

* Tue Aug 28 2007 Igor Zubkov <icesik@altlinux.org> 0.10.7-alt2
- move devel files to devel subpackage (closes #12595)

* Fri May 04 2007 Igor Zubkov <icesik@altlinux.org> 0.10.7-alt1
- fix linking

* Sun Feb 04 2007 Vitaly Lipatov <lav@altlinux.ru> 0.10.7-alt0.1
- new version 0.10.7 (with rpmrb script)

* Thu Sep 21 2006 Vitaly Lipatov <lav@altlinux.ru> 0.10.5-alt0.1
- new version (0.10.5)

* Mon May 08 2006 Vitaly Lipatov <lav@altlinux.ru> 0.10.4-alt0.1
- initial build for ALT Linux Sisyphus

* Tue Dec 20 2005 Thomas Vander Stichele <thomas at apestaart dot org>
- updated spec file

* Thu Oct 06 2005 Edward Hervey < edward at fluendo dot com >
- Updated spec file for 0.9

* Fri Nov 05 2004 Christian Schaller < uraeus at gnome org >
- Remerged spec file with cvs version

* Tue Oct 12 2004 Thomas Vander Stichele <thomas at apestaart dot org>
- 0.7.93-0.fdr.1: new upstream release

* Mon Jun 21 2004 Thomas Vander Stichele <thomas at apestaart dot org>
- 0.7.92-0.fdr.1: new upstream release

* Wed Mar 31 2004 Thomas Vander Stichele <thomas at apestaart dot org>
- 0.7.91-0.fdr.1: new upstream release

* Tue Sep 02 2003 Thomas Vander Stichele <thomas at apestaart dot org>
- 0.1.0-0.fdr.1: first fedora release
