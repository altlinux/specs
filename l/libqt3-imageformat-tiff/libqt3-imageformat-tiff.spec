%define dist TiffIO
%define major 1
%define minor 2
%define beta  0
%define distrel   e
%define altrel  alt3
#
%define tar  %dist-%major%minor%beta%distrel
%define INSTDIR	%_qt3dir/plugins/imageformats
%define PLUGIN libTiffIO.so

%define rel %altrel
%if %distrel != "%nil"
%define rel %altrel.%distrel
%endif

Name: libqt3-imageformat-tiff
Version: %major%minor%beta
Release: %rel

Group: System/Libraries
Summary: Plugin to add TIFF images read/write capabilities to the Qt3
Url: http://artis.inrialpes.fr/Logiciels/TiffIO
License: CeCILL_V1


Source: ftp://tiffio.sourceforge.net/%tar.tgz


# Automatically added by buildreq on Thu Apr 21 2011 (-bi)
# optimized out: elfutils fontconfig libX11-devel libXext-devel libstdc++-devel python-base ruby zlib-devel
#BuildRequires: gcc-c++ libjpeg-devel libqt3-devel libtiff-devel rpm-build-ruby
BuildRequires: gcc-c++ libjpeg-devel libqt3-devel libtiff-devel

%description
TiffIO is a plugin that add TIFF images read/write capabilities to the Qt3
QImage class.

Adding the generated plugin in the Qt's tree enable any Qt application to
manipulate TIFF images. TiffIO come with a self-test suite, and have been
compiled and used successfully on a variety of windows and unixes platforms.

All TIFF operations are based on libtiff 3.7.2, this plugin is just a wrapper
that enable to use it transparently from the QImage class, and the QImageIO


%prep
%setup -n %tar
rm -rf libtiff-*
echo "QMAKE_CXXFLAGS_RELEASE += %optflags %optflags_shared" >> rules.pri
qmake-qt3 CONFIG+=libtiff TIFF=%_includedir TiffIO.pro

%build
%make_build


%install
mkdir -p %buildroot/%INSTDIR
install -m 0644 %PLUGIN %buildroot/%INSTDIR


%files
%doc README* Licence*
%INSTDIR/%PLUGIN
%docdir %DOCDIR

%changelog
* Thu Apr 21 2011 Sergey V Turchin <zerg@altlinux.org> 120-alt3.e
- fix build requires

* Thu Dec 13 2007 Sergey V Turchin <zerg at altlinux dot org> 120-alt2.e
- fix build requires

* Thu Dec 13 2007 Sergey V Turchin <zerg at altlinux dot org> 120-alt1.e
- built for ALT

* Wed Feb 10 2006 <Jean-Dominique.Gascuel@imag.fr>
- Added support for Lab 3x16 and RGBA 4x32 color schemes.

* Mon Feb 06 2006 <Jean-Dominique.Gascuel@imag.fr>
- Upgrade to libtiff 3.8.0++ (beta CVS), to cure crash
  with uncommon features of TIFF (YCrCb color space,
  multipage, etc.)
- FIX bug preventing Qt4.1 version to have tiff/tif in the Qt's
  stringlist of recognized format.

* Wed Jan 11 2006 <Jean-Dominique.Gascuel@imag.fr>
- Upgrade to libtiff 3.8.0, patched against compile error & crashe.
- Fix mix-up between bit and byte order for bitmaps.
- Added image viewer demo.
- Added more test image in the regression test.

* Fri Oct 14 2005 <Jean-Dominique.Gascuel@imag.fr>
- First version ov the spec file for TiffIO 1.1.0 rel 3
