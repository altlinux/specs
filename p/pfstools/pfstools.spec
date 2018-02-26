%define lib_name libpfs

Name: pfstools
Version: 1.8.5
Release: alt1.1

Summary: High Dynamic Range (HDR) Images and Video manipulation tools
License: GPLv2+
Group: Graphics

Url: http://pfstools.sourceforge.net/
Source: http://downloads.sourceforge.net/pfstools/pfstools-%version.tar.gz
Patch1: pfstools-1.7.0-gcc44.patch
Patch2: pfstools-1.7.0-gdal.patch

# Automatically added by buildreq on Fri Apr 22 2011
# optimized out: fontconfig ilmbase-devel libGL-devel libGLU-devel libgfortran-devel libgotoblas2-devel libhdf5-6-seq libqt4-core libqt4-devel libqt4-gui libstdc++-devel libtiff-devel libtinfo-devel octave pkg-config texlive-latex-base zlib-devel
BuildRequires: gcc-c++ libImageMagick-devel libfftw3-devel libfreeglut-devel libgdal-devel libgeos-devel libhdf5-devel libjpeg-devel liblapack-devel libncurses-devel libnetpbm-devel libreadline-devel octave-devel openexr-devel

# Optimized out build requirements we want to add as safety belt
# (so pfstools build will not fail if due to changes in other packages
# deps listed below packages will not be pulled for build)
BuildRequires: libqt4-core libqt4-devel libqt4-gui

BuildRequires: gcc-fortran

Requires: %lib_name = %version-%release

# TODO: Move pfsglview and pfsview to own packages to prevent users from
# having to install OpenGL/GLUT and Qt?

%description
pfstools package is a set of command line (and one GUI) programs for reading,
writing, manipulating and viewing high-dynamic range (HDR) images and video
frames. All programs in the package exchange data using a simple generic file
format (pfs) for HDR data. The concept of the pfstools is similar to netpbm
package for low-dynamic range images.

%package -n %lib_name
Summary: Library for %name
Group: System/Libraries
License: LGPLv2.1+

%description -n %lib_name
This package contain the library needed to run programs linked with %lib_name.

%package -n %lib_name-devel
Summary: Headers for developing programs that will use %lib_name
Group: Development/C++
License: LGPLv2.1+
Requires: %lib_name = %version-%release

%description -n %lib_name-devel
This package contains the headers that programmers will need to develop
application which will use %lib_name.

%package octave
Summary: Octave interaction with PFS tools
Group: Graphics

%description octave
The pfstools-octave package contains programs to process red, green and blue
channels or luminance channels in pfs stream using Octave.

%package gdal
Summary: PFS Tools using the GDAL library to handle GIS information
Group: Graphics

%description gdal
The pfstools-gdal package contains programs which can handle GIS information
using the GDAL library.

%prep
%setup
%patch1 -p1
%patch2 -p1

%build
%autoreconf
# We can not use %%configure macro when build with octave in current repo...
./configure --prefix=/usr --libdir=%_libdir --disable-static --with-qtdir=%_libdir/qt4
%make_build

%install
%makeinstall_std

%files
%_bindir/pfsabsolute
%_bindir/pfscat
%_bindir/pfsclamp
%_bindir/pfscut
%_bindir/pfsextractchannels
%_bindir/pfsdisplayfunction
%_bindir/pfsflip
%_bindir/pfsgamma
%_bindir/pfsin
%_bindir/pfsindcraw
%_bindir/pfsinmulti
%_bindir/pfsinpfm
%_bindir/pfsinppm
%_bindir/pfsinrgbe
%_bindir/pfsintiff
%_bindir/pfsout
%_bindir/pfsoutffmpeg
%_bindir/pfsouthdrhtml
%_bindir/pfsoutpfm
%_bindir/pfsoutppm
%_bindir/pfsoutrgbe
%_bindir/pfsouttiff
%_bindir/pfspad
%_bindir/pfspanoramic
%_bindir/pfsrotate
%_bindir/pfssize
%_bindir/pfstag

%_bindir/pfsinexr
%_bindir/pfsoutexr
%_bindir/pfsinimgmagick
%_bindir/pfsoutimgmagick

%_bindir/pfsglview
%_bindir/pfsview
%_bindir/pfsv

%_datadir/pfstools

%_man1dir/pfsabsolute.*
%_man1dir/pfscat.*
%_man1dir/pfsclamp.*
%_man1dir/pfscut.*
%_man1dir/pfsdisplayfunction.*
%_man1dir/pfsextractchannels.*
%_man1dir/pfsflip.*
%_man1dir/pfsgamma.*
%_man1dir/pfsin.*
%_man1dir/pfsindcraw.*
%_man1dir/pfsinmulti.*
%_man1dir/pfsinpfm.*
%_man1dir/pfsinppm.*
%_man1dir/pfsinrgbe.*
%_man1dir/pfsintiff.*
%_man1dir/pfsout.*
%_man1dir/pfsoutffmpeg.*
%_man1dir/pfsouthdrhtml.*
%_man1dir/pfsoutpfm.*
%_man1dir/pfsoutppm.*
%_man1dir/pfsoutrgbe.*
%_man1dir/pfsouttiff.*
%_man1dir/pfspad.*
%_man1dir/pfspanoramic.*
%_man1dir/pfsrotate.*
%_man1dir/pfssize.*
%_man1dir/pfstag.*

%_man1dir/pfsinexr.*
%_man1dir/pfsoutexr.*
%_man1dir/pfsinimgmagick.*
%_man1dir/pfsoutimgmagick.*

%_man1dir/pfsglview.*
%_man1dir/pfsview.*
%_man1dir/pfsv.*

%files -n %lib_name
%_libdir/*.so.*

%files -n %lib_name-devel
%_includedir/pfs-*
%_libdir/pkgconfig/*.pc
%_libdir/*.so

%files octave
%_bindir/pfsoctavelum
%_bindir/pfsoctavergb
%_bindir/pfsstat
%_libdir/octave/*/site/oct/*/pfstools
%_datadir/octave/*/site/m/pfstools
%_man1dir/pfsoctavelum.*
%_man1dir/pfsoctavergb.*
%_man1dir/pfsstat.*

%files gdal
%_bindir/pfsingdal
%_man1dir/pfsingdal.*

%changelog
* Fri Jun 08 2012 Anton Farygin <rider@altlinux.ru> 1.8.5-alt1.1
- Rebuild with new libImageMagick

* Sat Dec 10 2011 Victor Forsiuk <force@altlinux.org> 1.8.5-alt1
- 1.8.5

* Sun Jun 19 2011 Victor Forsiuk <force@altlinux.org> 1.8.4-alt1
- 1.8.4

* Wed Apr 27 2011 Paul Wolneykien <manowar@altlinux.ru> 1.8.3-alt2.1
- Rebuild with the new version of Octave (3.4.0).

* Tue Apr 26 2011 Victor Forsiuk <force@altlinux.org> 1.8.3-alt2
- Renew build requirements.

* Sat Mar 26 2011 Victor Forsiuk <force@altlinux.org> 1.8.3-alt1
- 1.8.3
- Build with gdal and octave integration but separate them in
  subpackages to avoid excessive run-time deps of main package.

* Tue Sep 14 2010 Anton Farygin <rider@altlinux.ru> 1.8.2-alt1.1
- rebuild with new ImageMagick

* Wed Jul 14 2010 Victor Forsiuk <force@altlinux.org> 1.8.2-alt1
- 1.8.2

* Tue Jun 23 2009 Victor Forsyuk <force@altlinux.org> 1.8.1-alt1
- 1.8.1

* Tue Nov 18 2008 Victor Forsyuk <force@altlinux.org> 1.7.0-alt1
- 1.7.0
- Remove obsolete ldconfig calls in post-scripts.

* Wed May 21 2008 Victor Forsyuk <force@altlinux.org> 1.6.5-alt1
- 1.6.5

* Sat Mar 01 2008 ALT QA Team Robot <qa-robot@altlinux.org> 1.6.4-alt1.1
- Rebuilt due to libIlmImf.so.4 -> libIlmImf.so.6 soname change.

* Tue Feb 26 2008 Victor Forsyuk <force@altlinux.org> 1.6.4-alt1
- 1.6.4

* Fri Jul 06 2007 Victor Forsyuk <force@altlinux.org> 1.6.2-alt1
- 1.6.2

* Mon Jun 18 2007 Victor Forsyuk <force@altlinux.org> 1.6.1-alt2
- Build with libnetpbm-devel and libImageMagick-devel.

* Thu Jun 07 2007 Victor Forsyuk <force@altlinux.org> 1.6.1-alt1
- Initial build.
