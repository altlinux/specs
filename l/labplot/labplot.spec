%define oname LabPlot
%define pre .alpha2
Name: labplot
Version: 2.0.0
Release: alt5.svn20090921

Summary: Function and Data Plotter

Packager: Vitaly Lipatov <lav@altlinux.ru>

Url: http://labplot.sourceforge.net
Group: Sciences/Other
License: GPL

# https://labplot.svn.sourceforge.net/svnroot/labplot
Source: %oname-%version%pre.tar.bz2
Source1: %name-%version.desktop
Source2: CMakeCache.txt

# Automatically added by buildreq on Sun Jan 18 2009
BuildRequires: ccmake gcc-c++ kde4base-runtime kde4libs-devel
BuildRequires: libXScrnSaver-devel libXau-devel libXcomposite-devel
BuildRequires: libXdamage-devel libXdmcp-devel libXpm-devel libXt-devel
BuildRequires: libXtst-devel libXv-devel libXxf86misc-devel libcdf-devel
BuildRequires: libgsl-devel libhdf5-devel libnetcdf-devel
BuildRequires: libqt4-devel libxkbfile-devel xorg-xf86vidmodeproto-devel
BuildPreReq: chrpath bison

Conflicts: labplot1.6
Requires: ImageMagick >= 5.4.7 gsl pstoedit

%description
This is a program for plotting of functions and data manipulation.

A versatile spreadsheet for data import and editing was added. Also a better
3 dimensional plot with rotation and colormaps is available.
Newly supported are data set operations and image manipulations. One can now 
import over 80 different images formats and export directly to ps, eps or pdf.
The plots now use double buffering and LabPlot supports scripting using
QSA.

%package scidavis
Summary: Function and Data Plotter (experimental Qt frontend)
Group: Sciences/Other
Requires: ImageMagick >= 5.4.7 gsl pstoedit

%description scidavis
This is a program for plotting of functions and data manipulation.

A versatile spreadsheet for data import and editing was added. Also a better
3 dimensional plot with rotation and colormaps is available.
Newly supported are data set operations and image manipulations. One can now 
import over 80 different images formats and export directly to ps, eps or pdf.
The plots now use double buffering and LabPlot supports scripting using
QSA.

SciDAVis introduces an abstraction of the application design called
"aspect framework" or "5 layer model".

%prep
%setup -q -n %oname-%version%pre
sed -i 's|@LIBDIR@|%_libdir|g' src/qtfrontend/config.pri

install -p -m644 %SOURCE2 .
sed -i "s|@PWD@|$PWD|g" CMakeCache.txt

%build
cmake -Wdev --debug-output -DCMAKE_INSTALL_PREFIX=%prefix .

%make_build

# build SciDAvis

pushd src/qtfrontend
qmake-qt4 QMAKE_CFLAGS_RELEASE="%optflags" \
	QMAKE_CXXFLAGS_RELEASE="%optflags" scidavis.pro
%make_build
popd

%install
%makeinstall_std

install -m644 -D %SOURCE1 %buildroot%_desktopdir/%name.desktop

mv %buildroot%_bindir/%name %buildroot%_bindir/%oname
ln -s %oname %buildroot%_bindir/%name

# install SciDAvis

pushd src/qtfrontend
%make_install INSTALL_ROOT=%buildroot install
install -d %buildroot%_libdir/scidavis
mv %buildroot%_bindir/*.so %buildroot%_libdir/scidavis
chrpath -r %_libdir/scidavis %buildroot%_bindir/scidavis
popd

#

%find_lang %oname --with-kde

%files -f %oname.lang
%doc AUTHORS README COPYING WISHLIST ChangeLog
%_bindir/*
%exclude %_bindir/scidavis
%_libdir/*so.*
%_datadir/apps/%oname/
%_desktopdir/*

%files scidavis
%doc %_docdir/scidavis
%_bindir/scidavis
%_libdir/scidavis

%changelog
* Wed Jun 06 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.0.0-alt5.svn20090921
- Fixed build

* Thu Sep 08 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.0.0-alt4.svn20090921.8
- Rebuilt with libhdf5-7

* Sun Apr 24 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.0.0-alt4.svn20090921.7
- Rebuilt with libnetcdf7

* Fri Mar 18 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.0.0-alt4.svn20090921.6
- Rebuilt for debuginfo

* Mon Feb 14 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.0.0-alt4.svn20090921.5
- Fixed build

* Tue Nov 02 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.0.0-alt4.svn20090921.4
- Rebuilt for soname set-versions

* Mon Oct 18 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.0.0-alt4.svn20090921.3
- Built without system liborigin

* Tue Jul 27 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.0.0-alt4.svn20090921.2
- Rebuilt with Qt 4.7

* Tue Nov 24 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.0.0-alt4.svn20090921.1
- Rebuilt with gsl 1.13-alt1

* Thu Nov 05 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.0.0-alt4.svn20090921
- New snapshot
- Added SciDAvis (experimental Qt frontend)

* Wed Jun 03 2009 Vitaly Lipatov <lav@altlinux.ru> 2.0.0-alt2
- rebuild with libnetcdf-4.0.1

* Mon Jan 05 2009 Vitaly Lipatov <lav@altlinux.ru> 2.0.0-alt1
- new version (2.0.0)
- build with libnetcdf-4.0

* Mon Jan 05 2009 Vitaly Lipatov <lav@altlinux.ru> 1.6.0.2-alt1
- new version (1.6.0.2)

* Tue Oct 04 2005 Vitaly Lipatov <lav@altlinux.ru> 1.5.0-alt0.4
- new version

* Mon Dec 27 2004 Vitaly Lipatov <lav@altlinux.ru> 1.4.0-alt1
- new version

* Mon Nov 08 2004 Vitaly Lipatov <lav@altlinux.ru> 1.3.1-alt1
- release

* Fri Sep 17 2004 ALT QA Team Robot <qa-robot@altlinux.org> 1.3.1-alt0.1pre2.1
- Rebuilt with libtiff.so.4.

* Sat Jul 31 2004 Vitaly Lipatov <lav@altlinux.ru> 1.3.1-alt0.1pre2
- new version
- add russian translation

* Sat Jun 19 2004 Vitaly Lipatov <lav@altlinux.ru> 1.3.0-alt1
- first build for Sisyphus

