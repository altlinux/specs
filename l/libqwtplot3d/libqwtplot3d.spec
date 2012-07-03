#  08 April 2008: the project is stopped
Name: libqwtplot3d
Version: 0.3.0
Release: alt1.svn20090915.3

Summary: 3D plotting widget extension to the Qt GUI

License: LGPL
Group: System/Libraries
Url: http://qwtplot3d.sourceforge.net/

Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: http://prdownloads.sf.net/qwtplot3d/qwtplot3d-%version.tar.bz2
#Patch: libqwtplot3d-0.2.7-linestyles-qti.patch

# Automatically added by buildreq on Thu Aug 02 2007
BuildRequires: gcc-c++ libqt4-devel qt4-settings

BuildPreReq: libGL-devel libGLU-devel

%description
QwtPlot3D is a feature-rich Qt/OpenGL-based C++ programming library.
It provides essentially a bunch of 3D-widgets for programmers.

%package devel
Summary: Development tools for programs which uses QwtPlot3D Widget set
Group: Development/C
Requires: %name = %version

%description devel
QwtPlot3D is a feature-rich Qt/OpenGL-based C++ programming library.
It provides essentially a bunch of 3D-widgets for programmers.

%prep
%setup -q -n qwtplot3d
#patch -p1

%build
export QTDIR=%_qt4dir
export PATH=$QTDIR/bin:$PATH
qmake qwtplot3d.pro
%make_build

%install
mkdir -p %buildroot{%_libdir,%_includedir/qwtplot3d}
for n in include/*.h ; do
    install -m 644 $n %buildroot%_includedir/qwtplot3d
done

# install, preserving links
chmod 644 lib/libqwtplot3d.so*
for n in lib/libqwtplot3d.so* ; do
    cp -d $n %buildroot%_libdir
done

%files
%_libdir/libqwtplot3d.so.*

%files devel
%_includedir/qwtplot3d
%_libdir/libqwtplot3d.so

%changelog
* Sun Mar 27 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.3.0-alt1.svn20090915.3
- BuildRequires: replaced libmesa-devel by libGL-devel and libGLU-devel

* Sat Feb 26 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.3.0-alt1.svn20090915.2
- Rebuilt for debuginfo

* Wed Oct 20 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.3.0-alt1.svn20090915.1
- Rebuilt for soname set-versions

* Tue Sep 15 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.3.0-alt1.svn20090915
- Version 0.3.0 (unreleased)

* Tue Sep 15 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.2.7-alt3
- Fixed for gcc 4.4

* Sat Dec 27 2008 Vitaly Lipatov <lav@altlinux.ru> 0.2.7-alt2
- add linestyles patch (fix bug #18109)

* Thu Aug 02 2007 Vitaly Lipatov <lav@altlinux.ru> 0.2.7-alt1
- new version 0.2.7 (with rpmrb script)
- use Qt4, update buildreq

* Sun Jun 11 2006 Vitaly Lipatov <lav@altlinux.ru> 0.2.6-alt0.1
- new version 0.2.6 (with rpmrb script)
- fix Source URL

* Fri Feb 11 2005 Vitaly Lipatov <lav@altlinux.ru> 0.2.4-alt0.2beta
- move libraries to %_libdir, fix .so placement
- move include to %_includedir

* Mon Dec 27 2004 Vitaly Lipatov <lav@altlinux.ru> 0.2.4-alt0.1beta
- first build for ALT Linux Sisyphus
