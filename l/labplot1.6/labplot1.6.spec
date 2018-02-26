#./.libs/libLabPlot.so: undefined reference to `Qwt3D::SurfacePlot::SurfacePlot(QWidget*, char const*)'
# system qwt3d built with QT4

%define oname LabPlot
%define pre %nil
Name: labplot1.6
Version: 1.6.0.2
Release: alt2.qa6

Summary: Function and Data Plotter
Summary(ru_RU.KOI8-R): Построитель графиков по данным и функциям

Packager: Vitaly Lipatov <lav@altlinux.ru>

Url: http://labplot.sourceforge.net
Group: Sciences/Other
License: GPL

Source: http://prdownloads.sourceforge.net/labplot/%oname-%version%pre.tar.bz2
Source1: %name.desktop
#Source1: %name-%version.ru.po
Patch: %name.patch

BuildPreReq: automake autoconf kdebase-wm libaudiofile-devel chrpath
BuildPreReq: kdelibs-devel
# manually removed: boson gcc-g77 hostinfo
# Automatically added by buildreq on Sun Jan 18 2009
BuildRequires: gcc-c++ gcc-fortran ghostscript-utils imake kdepim-devel libGL-devel libImageMagick-devel libXt-devel libcdf-devel libfftw3-devel libgsl-devel libhdf5-devel libjasper-devel libjpeg-devel libnetcdf-devel libqt3-qsa-devel libtiff-devel pstoedit qt3-designer xml-utils xorg-cf-files

#BuildRequires: bzlib-devel fontconfig freetype2-devel gcc-c++ kde-settings kdelibs-devel libImageMagick-devel libarts-devel libaudiofile-devel libfftw3-devel libgsl-devel libjasper-devel libjpeg-devel liblcms-devel libnetcdf-devel libpng-devel libqscintilla-designer libqt3-devel libqt3-qsa-devel libqt3-settings libqwt-devel libstdc++-devel libtiff-devel pstoedit qt3-designer xml-utils xorg-x11-devel xorg-x11-libs zlib-devel

Requires: ImageMagick >= 5.4.7 gsl pstoedit

%description
This is a program for plotting of functions and data manipulation.

A versatile spreadsheet for data import and editing was added. Also a better
3 dimensional plot with rotation and colormaps is available.
Newly supported are data set operations and image manipulations. One can now 
import over 80 different images formats and export directly to ps, eps or pdf.
The plots now use double buffering and LabPlot supports scripting using
QSA.

%prep
%setup -q -n %oname-%version%pre
%patch

%build
#autoreconf
autoconf -f
export QTDIR=%_libdir/qt3
export KDEDIR=%_libdir/kde3
export PATH=$QTDIR/bin:$KDEDIR/bin:$PATH
%add_optflags -I%_includedir/tqtinterface
%configure --disable-static --disable-rpath \
	--enable-fftw3 --enable-gl --enable-audiofile --enable-jasper \
	--enable-gsl --enable-qsa \
	--disable-system-liborigin \
	--enable-cdf --enable-netcdf \
	--without-arts

%make_build

%install
%makeinstall_std
install -m644 -D %SOURCE1 %buildroot%_desktopdir/%name.desktop

install -D -m644 src/icons/lo32-app-LabPlot.png %buildroot%_niconsdir/%name.png
install -D -m644 src/icons/lo16-app-LabPlot.png %buildroot%_miconsdir/%name.png
install -D -m644 src/icons/hi48-app-LabPlot.png %buildroot%_liconsdir/%name.png

for i in %buildroot%_bindir/* %buildroot%_libdir/*.so.*
do
	chrpath -d $i ||:
done

%find_lang LabPlot --with-kde

%files -f LabPlot.lang
%doc README TODO INSTALL ChangeLog CHANGES FEATURES LabPlot.lsm doc/cephes.doc
%_bindir/*
%_desktopdir/*
%_datadir/mimelnk/application/x-lpl.desktop
%_datadir/mimelnk/application/x-lml.desktop
%_datadir/apps/LabPlot/
%_niconsdir/%{name}*
%_iconsdir/hicolor/*/apps/*.png
%_iconsdir/hicolor/*/mimetypes/*.png
%_iconsdir/locolor/*/apps/*.png
%_iconsdir/locolor/*/mimetypes/*.png
%_liconsdir/%{name}*
%_miconsdir/%{name}*
%_man1dir/*
%_libdir/libLabPlot.so.*
%_libdir/libLabPlotcephes.so.*
%_libdir/libLabPlotqwtplot3d.so.*

%changelog
* Wed Jun 06 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.6.0.2-alt2.qa6
- Fixed build

* Mon May 21 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.6.0.2-alt2.qa5
- Fixed build

* Wed Feb 01 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.6.0.2-alt2.qa4
- Removed bad RPATH

* Sun Apr 24 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.6.0.2-alt2.qa3
- Rebuilt with libnetcdf7

* Fri Mar 18 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.6.0.2-alt2.qa2
- Rebuilt for debuginfo and without arts

* Tue Nov 24 2009 Repocop Q. A. Robot <repocop@altlinux.org> 1.6.0.2-alt2.qa1
- NMU (by repocop): the following fixes applied:
  * pixmap-in-deprecated-location for labplot1.6
  * postclean-05-filetriggers for spec file

* Wed Jun 03 2009 Vitaly Lipatov <lav@altlinux.ru> 1.6.0.2-alt2
- rebuild with libnetcdf v4.0.1 and libhdf5 v1.8.3

* Mon Jan 05 2009 Vitaly Lipatov <lav@altlinux.ru> 1.6.0.2-alt1
- new version (1.6.0.2)

* Tue Nov 13 2007 Vitaly Lipatov <lav@altlinux.ru> 1.6.0-alt1.rc2
- rc2 (1.6.0)

* Thu Aug 02 2007 Vitaly Lipatov <lav@altlinux.ru> 1.6.0-alt1.pre2
- prerelease2 (1.6.0)
- cleanup spec

* Sun Jun 11 2006 Vitaly Lipatov <lav@altlinux.ru> 1.6.0-alt1.pre1
- prerelease1 (1.6.0)

* Wed May 24 2006 Vitaly Lipatov <lav@altlinux.ru> 1.5.1-alt1
- new version (1.5.1)

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

