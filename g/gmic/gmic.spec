%define gimpplugindir %(gimptool-2.0 --gimpplugindir)

Name: gmic
Version: 1.5.0.8
Release: alt1

Summary: G'MIC is an interpreter of image processing macros
License: CeCILL
Group: Graphics

Url: http://gmic.sourceforge.net/
Source: http://downloads.sourceforge.net/gmic/gmic_%version.tar.gz
Patch1: gmic-1.4.8.1-bashcompletion.patch

# Automatically added by buildreq on Wed Mar 09 2011
BuildRequires: gcc-c++ imake libGraphicsMagick-c++-devel libImageMagick-devel libXext-devel libXrandr-devel libavformat-devel libfftw3-devel libgimp-devel libjpeg-devel libopencv-devel libpng-devel libswscale-devel libtiff-devel openexr-devel xorg-cf-files

%description
G'MIC (GREYC's Magic Image Converter) is an interpreter of image processing
macros whose goal is to convert, manipulate and visualize generic 1D/2D/3D
multi-spectral image datasets.

%package -n gimp-plugin-gmic
Summary: Image denoising and interpolation plugin for GIMP
Group: Graphics
Requires: gimp

%description -n gimp-plugin-gmic
G'MIC (GREYC's Magic Image Converter) is an interpreter of image processing
macros whose goal is to convert, manipulate and visualize generic 1D/2D/3D
multi-spectral image datasets.

%prep
%setup -n gmic-%version
%patch1 -p1

%build
# Fix check: InitializeMagick found in GraphicsMagick lib, not GraphicsMagick++
subst 's/-lGraphicsMagick++/-lGraphicsMagick/g' configure
subst 's/-lMagick++/-lMagickCore/g' configure

subst 's/-Dcimg_use_magick/-Dcimg_use_magick `GraphicsMagick++-config --cppflags`/' src/Makefile

# Fixes for opencv2:
subst 's/-lcv/-lopencv_imgproc/g; s/-lhighgui/-lopencv_highgui/g' configure src/Makefile

subst 's/strip /#strip /' src/Makefile

%configure
%make_build

%install
%makeinstall_std

%files
%config /etc/bash_completion.d/*
%_bindir/*
%_man1dir/*
%lang(fr) %_mandir/fr/man1/*

%files -n gimp-plugin-gmic
%gimpplugindir/plug-ins/*

%changelog
* Sun Jan 08 2012 Victor Forsiuk <force@altlinux.org> 1.5.0.8-alt1
- 1.5.0.8

* Tue Dec 27 2011 Victor Forsiuk <force@altlinux.org> 1.5.0.7-alt1
- 1.5.0.7

* Sat Nov 12 2011 Victor Forsiuk <force@altlinux.org> 1.5.0.6-alt1
- 1.5.0.6

* Wed Aug 31 2011 Victor Forsiuk <force@altlinux.org> 1.5.0.1-alt1
- 1.5.0.1

* Sun Aug 14 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.5.0.0-alt1.1
- Rebuilt with OpenCV 2.3.1

* Sun Jul 10 2011 Victor Forsiuk <force@altlinux.org> 1.5.0.0-alt1
- 1.5.0.0

* Sun Jun 19 2011 Victor Forsiuk <force@altlinux.org> 1.4.9.5-alt1
- 1.4.9.5

* Tue May 10 2011 Victor Forsiuk <force@altlinux.org> 1.4.9.2-alt1
- 1.4.9.2

* Mon Apr 04 2011 Victor Forsiuk <force@altlinux.org> 1.4.9.0-alt1
- 1.4.9.0

* Fri Mar 04 2011 Victor Forsiuk <force@altlinux.org> 1.4.8.2-alt1
- 1.4.8.2

* Mon Feb 21 2011 Victor Forsiuk <force@altlinux.org> 1.4.8.1-alt1
- 1.4.8.1
- Package bash completion file.

* Tue Feb 01 2011 Victor Forsiuk <force@altlinux.org> 1.4.7.4-alt1
- 1.4.7.4

* Wed Dec 01 2010 Victor Forsiuk <force@altlinux.org> 1.4.5.2-alt1
- 1.4.5.2
- Patched to build with libopencv2 (patch by real@).

* Tue Sep 14 2010 Anton Farygin <rider@altlinux.ru> 1.4.1.0-alt1.1
- NMU: rebuild with new ImageMagick

* Thu Sep 09 2010 Victor Forsiuk <force@altlinux.org> 1.4.1.0-alt1
- 1.4.1.0

* Wed Jul 14 2010 Anton Farygin <rider@altlinux.ru> 1.3.4.0-alt1.1
- NMU: rebuild with new ImageMagick

* Tue Mar 09 2010 Victor Forsiuk <force@altlinux.org> 1.3.4.0-alt1
- 1.3.4.0

* Mon Feb 22 2010 Victor Forsiuk <force@altlinux.org> 1.3.3.6-alt1
- 1.3.3.6

* Thu Nov 26 2009 Victor Forsyuk <force@altlinux.org> 1.3.3.0-alt1
- 1.3.3.0

* Wed Aug 26 2009 Victor Forsyuk <force@altlinux.org> 1.3.2.4-alt1
- 1.3.2.4

* Mon Jun 15 2009 Victor Forsyuk <force@altlinux.org> 1.3.2.0-alt1
- 1.3.2.0

* Thu Mar 19 2009 Victor Forsyuk <force@altlinux.org> 1.3.1.1-alt1
- 1.3.1.1

* Wed Mar 11 2009 Victor Forsyuk <force@altlinux.org> 1.3.0.4-alt1
- 1.3.0.4

* Tue Feb 17 2009 Victor Forsyuk <force@altlinux.org> 1.3.0.3-alt1
- Initial build.
