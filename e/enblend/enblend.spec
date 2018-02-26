Summary: A tool for combine images (make a panoramas) using a multiresolution spline
Name: enblend
Version: 4.0
Release: alt1.1
License: VIGRA License
Group: Graphics
URL: http://enblend.sourceforge.net/
Packager: Sergei Epiphanov <serpiph@altlinux.ru>
Source0: %name-%version.tar.gz

Provides: enfuse


BuildRequires: boost-devel gcc-c++ libstdc++-devel automake autoconf
BuildRequires: libjpeg-devel libpng-devel libtiff-devel libglew-devel liblcms-devel
BuildRequires: libxmi-devel libXmu-devel libXi-devel
BuildRequires: libGLU-devel libGLUT-devel openexr-devel liblcms-devel libstlport-devel
BuildRequires: gnuplot texinfo fonts-ttf-freefont ghostscript perl transfig tidy

%description
enblend  overlays  multiple  TIFF  images using the Burt & Adelson mul-
tiresolution spline.  This technique tries to make  the  seams  between
the  input  images  invisible and very suitable to make panoramas.

%prep

%setup -q

%build

export CPPFLAGS=-I/usr/include/lcms
autoreconf -fisv
#mkdir build
#cd build
%configure
%make
#cd ..
%install

#cd build
%makeinstall

%files
%doc AUTHORS NEWS README VIGRA_LICENSE
%_bindir/*
%_man1dir/*
/usr/share/info/*


%changelog
* Fri Apr 08 2011 Anton V. Boyarshinov <boyarsh@altlinux.ru> 4.0-alt1.1
- build fixed

* Wed Nov 10 2010 Sergei Epiphanov <serpiph@altlinux.ru> 4.0-alt1
- New version

* Tue Jun 23 2009 Anton V. Boyarshinov <boyarsh@altlinux.ru> 3.2-alt3.1
- rebuild with libpng.git=1.2.37-alt2

* Wed Jun 03 2009 Anton V. Boyarshinov <boyarsh@altlinux.ru> 3.2-alt3
- build fixed: added INFO-DIR-SECTION into .info 

* Thu Dec 18 2008 Sergei Epiphanov <serpiph@altlinux.ru> 3.2-alt2
- Fix due to repocop warning

* Sat Nov 01 2008 Anton V. Boyarshinov <boyarsh@altlinux.ru> 3.2-alt1
- New version 

* Fri Jul 25 2008 Sergei Epiphanov <serpiph@altlinux.ru> 3.0-alt2
- Add Packager tag

* Sun Feb 11 2007 Sergei Epiphanov <serpiph@altlinux.ru> 3.0-alt1
- New version

* Fri Dec 16 2005 Sergei Epiphanov <serpiph@altlinux.ru> 2.5-alt1
- New version needed for hugin-0.5. Changes and bugfixes from 2.3:
  + Fixed a bug where Enblend would crash when the -w parameter was used.
  + Fixed a bug where Enblend would sometimes say "mask transition line bounding box undefined."
  + Added support for cropped and shifted TIFF files, such as those produced by Nona.
  + Enblend will now create output files with embedded ICC profiles, if a profile is found in one of the input images.
  + Improved the speed of the mask generation algorithm.
  + See the complete release notes at Sourceforge.

* Fri Jun 17 2005 Anton V. Boyarshinov <boyarsh@altlinux.ru> 2.3-alt1
- The maximum number of levels you can specify with the -l parameter has been reduced from 30 to 29. While both of these are impractically large, at least 29 does not lead to arithmetic overflow and a subsequent crash.
- TIFF library warning messages have been turned off
-  Fixed a bug that caused primary-color spots to appear in overexposed areas of 16-bpp images.
- Fixed a problem with Enblend crashing on large panoramas.
- Support for signed and unsigned 16-bit, 32-bit, single- and double-precision floating point pixel types.
- No more banding artifacts in the sky, even with 8-bit images.
- Sophisticated memory/disk balancing. You can tell Enblend how much memory it is allowed to use, and it will swap to disk after that.
- Support for large panoramas. I have tested that Enblend can blend a 1.2 gigapixel, 16-bit per channel color image. You should be able to go right up to 4 gigabyte limit of the TIFF format.
- Optional blending in CIE L*a*b* color space

* Mon May 24 2004 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1.3-alt1
- first build for ALTLinux
