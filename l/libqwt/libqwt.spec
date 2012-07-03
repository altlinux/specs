Name: libqwt
Version: 5.2.0
Release: alt7
Epoch: 1

Summary: 2D plotting widget extension to the Qt GUI

License: LGPL
Group: System/Libraries
Url: http://sourceforge.net/projects/qwt

Packager: Vitaly Lipatov <lav@altlinux.ru>

Source: http://prdownloads.sf.net/qwt/qwt-%version.tar.bz2
Patch: %name-%version.patch

Conflicts: libqwt5_3 = 5.3.0-alt1.svn20090920
Obsoletes: libqwt5_3 = 5.3.0-alt1.svn20090920

# Automatically added by buildreq on Tue Jul 21 2009
BuildRequires: gcc-c++ libqt4-devel libXext-devel

%description
Qwt is an extension to the Qt GUI library from Troll Tech AS.
The Qwt library contains widgets and components which are
primarily useful for technical and scientifical purposes.
It includes a 2-D plotting widget, different kinds of sliders,
and much more.

%package devel
Summary: Development tools for programs which uses Qwt Widget set
Group: Development/C
Requires: %name = %version

%description devel
The libqwt-devel package contains the header files and static libraries
necessary for developing programs using the Qwt Widget set

If you want to develop programs which will use this set of widgets,
you should install this package. You need also to install the libqwt package.

%prep
%setup
%patch -p1
subst "s|/lib|/%_lib|g" qwtconfig.pri

%build
export QTDIR=%_qt4dir
export PATH=$QTDIR/bin:$PATH
qmake qwt.pro

# incompatible with SMP build
%make

%install
%make_install install INSTALL_ROOT=%buildroot

# clean up the example tree
(cd examples; make distclean)
(cd examples; rm -f .*.cache */.*.cache */*/.*.cache)
(cd examples; rm -rf Makefile */moc */obj */*/moc */*/obj)

rm -rf %buildroot/usr/doc

%files
%doc CHANGES README
%_libdir/libqwt.so.*
%_qt4dir/plugins/designer/*.so

%files devel
%doc doc/html/
%doc examples/
%_includedir/qwt/
%_libdir/libqwt.so
%_man3dir/*

%changelog
* Sat Feb 26 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1:5.2.0-alt7
- Rebuilt for debuginfo

* Mon Oct 25 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1:5.2.0-alt6
- Rebuilt for soname set-versions

* Mon Sep 28 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1:5.2.0-alt5
- Restored old version (wish of ldv@)

* Thu Jul 23 2009 Vitaly Lipatov <lav@altlinux.ru> 5.2.0-alt2
- build for Sisyphus

* Wed Jul 22 2009 Michael Shigorin <mike@altlinux.org> 5.2.0-alt1
- new version 5.2.0 (with rpmrb script) (closes: #20844)
- updated patch
- buildreq

* Wed Jun 18 2008 Vitaly Lipatov <lav@altlinux.ru> 5.1.1-alt1
- new version 5.1.1 (with rpmrb script) - fix #14854

* Thu May 15 2008 Vitaly Lipatov <lav@altlinux.ru> 5.1.0-alt1
- new version 5.1.0 (with rpmrb script)

* Thu Aug 02 2007 Vitaly Lipatov <lav@altlinux.ru> 5.0.2-alt2
- fix build on x86_64

* Tue Jul 31 2007 Vitaly Lipatov <lav@altlinux.ru> 5.0.2-alt1
- new version 5.0.2 (with rpmrb script)
- build with QT4, fix install process
- disable man for API, use html version

* Sun Jun 18 2006 Vitaly Lipatov <lav@altlinux.ru> 5.0-alt0.1
- new version (snapshot 20060130)

* Sat Jul 30 2005 Vitaly Lipatov <lav@altlinux.ru> 4.2.0-alt4
- fix bug #7496 (pseudo unexpanded macros)

* Tue Mar 01 2005 Vitaly Lipatov <lav@altlinux.ru> 4.2.0-alt3
- move include to %_includedir

* Fri Feb 11 2005 Vitaly Lipatov <lav@altlinux.ru> 4.2.0-alt2
- move libraries to %_libdir, fix .so placement

* Fri Dec 03 2004 Vitaly Lipatov <lav@altlinux.ru> 4.2.0-alt1
- first build for ALT Linux Sisyphus

* Mon Oct 15 2001 Lenny Cartier <lenny@mandrakesoft.com> 0.3.0-3mdk
- rebuild against new libpng

* Mon Aug 20 2001 Lenny Cartier <lenny@mandrakesoft.com> 0.3.0-2mdk
- rebuild

* Tue Jan 26 2001 Lenny Cartier <lenny@mandrakesoft.com> 0.3.0-1mdk
- added by Stefano Borini <munehiro@ferrara.linux.it> :
	- First RPM release

