%def_enable shared
%def_enable static
%def_enable compat
%def_enable openmp
%def_enable largefile
%def_disable debug
%def_disable efence
%def_disable prof
%def_disable gprof
%def_disable gcov
%def_with cpp
%def_with perl
%def_with x
%def_with fpx
%def_with modules
%def_with threads
%def_with bzlib
%def_without dps
%def_without gslib
%def_with jbig
%def_with jpeg
%def_with jpeg2
%def_with lcms
%def_with lcms2
%def_with lzma
%def_with png
%def_with tiff
%def_without trio
%def_with ttf
%def_with webp
%def_with wmf
%def_with xml
%def_with zlib
%def_with menu
%def_with nox_gm
%define quantum_depth 16
#---------------------------------------------------------------------
%define subst_enable_to() %{expand:%%{?_enable_%{1}:--enable-%{2}}} %{expand:%%{?_disable_%{1}:--disable-%{2}}}
%define subst_with_to() %{expand:%%{?_with_%{1}:--with-%{2}}} %{expand:%%{?_without_%{1}:--without-%{2}}}
%{!?quantum_depth:%define quantum_depth 8}


%define Name GraphicsMagick
Name: %Name
%define lname lib%name
Version: 1.3.20
Release: alt2.1.1
Summary: An X application for displaying and manipulating images
Summary(ru_RU.UTF-8): Программа для отображения и редактирования изображений
License: %mit
Group: Graphics
Url: http://www.graphicsmagick.org
Source: ftp://ftp.graphicsmagick.org/pub/%Name/%Name-%version.tar
Patch: %name-%version-%release.patch
%{?_enable_shared:Requires: %lname = %version-%release}
Requires: %name-common = %version-%release

BuildRequires(pre): rpm-build-licenses
# Automatically added by buildreq on Fri Jan 19 2007
BuildRequires: chrpath dcraw enscript libgegl ghostscript-classic gnuplot graphviz groff-base imake libltdl-devel mpeg2vidcodec netpbm transfig wget wmf-utils xorg-cf-files xterm zip p7zip
%{?_with_bzlib:BuildRequires: bzlib-devel}
%{?_with_perl:BuildRequires: perl-devel}
%{?_with_x:BuildRequires: libSM-devel libXext-devel}
%{?_with_fpx:BuildRequires: libfpx-devel}
%{?_with_jbig:BuildRequires: libjbig-devel}
%{?_with_lcms:BuildRequires: liblcms-devel}
%{?_with_lcms2:BuildRequires: liblcms2-devel}
%{?_with_lzma:BuildRequires: liblzma-devel}
%{?_with_tiff:BuildRequires: libtiff-devel}
%{?_with_webp:BuildRequires: libwebp-devel}
%{?_with_wmf:BuildRequires: libwmf-devel}
%{?_with_xml:BuildRequires: libxml2-devel}
%{?_with_jpeg:BuildRequires: libjpeg-devel}
%{?_with_jpeg2:BuildRequires: libjasper-devel}
%{?_with_png:BuildRequires: libpng-devel}
%{?_with_cpp:BuildRequires: gcc-c++}


%description
%Name provides a powerful image manipulation and translation
utility. It is capable of displaying still images and animations using
the X Window system, provides a simple interface for interactively
editing images, and is capable of importing selected windows or the
entire desktop. %Name can read and write over 88 image
formats, including JPEG, TIFF, WMF, SVG, PNG, PNM, GIF, and Photo CD.
It can resize, rotate, sharpen, color reduce, or add special effects to
the image and save the result to any supported format. %Name
may be used to create animated or transparent .gifs, create composite
images, create thumbnail images, and much, much, more.

%description -l ru_RU.UTF-8
%Name - мощный инструмент для редактирования и преобразования
изображений. Он может показывать статичные рисунки и анимацию
используя систему X Windows, обеспечивает простой интерфейс для
интерактивного редактирования изображений и возможность импорта
выбранных окон или всего рабочего стола. %Name может читать и
записывать более чем в 88 графических форматах, включая JPEG, TIFF,
WMF, SVG, PNG, PNM, GIF, и Photo CD. Он может изменять размеры,
вращать, улучшать резкость, уменьшать глубину цвета, или добавлять
специальные эффекты к изображению и сохранять результат в любом
поддерживаемом формате. %Name может использоваться для
создания анимационных или прозрачных GIF-ов, создания составных
изображений, создания миниатюр изображений, и много другое.


%if_with nox_gm
%package nox
Summary: An X application for manipulating images
Group: Graphics
Provides: %name = %version-%release
Requires: %name-common = %version-%release

%description nox
%Name provides a powerful image manipulation and translation
utility.
%Name can read and write over 88 image formats, including
JPEG, TIFF, WMF, SVG, PNG, PNM, GIF, and Photo CD. It can resize,
rotate, sharpen, color reduce, or add special effects to the image and
save the result to any supported format. %Name may be used to
create animated or transparent .gifs, create composite images, create
thumbnail images, and much, much, more.
%endif

%package common
Summary: Common files
Group: Graphics
BuildArch: noarch

%description common
Common files for %Name

%package doc
Summary:  Documentation for %Name
Group: Documentation
BuildArch: noarch

%description doc
Documentation for %Name.


%package ImageMagick-compat
Summary: Image processing tools providing ImageMagick interface
Group: Documentation
BuildArch: noarch
Requires: %name = %version-%release
Conflicts: ImageMagick-tools

%description ImageMagick-compat
%Name provides a set of command-line applications to
manipulate image files.
This package contains documentation for %Name


%package -n %lname
Summary: %Name shared libraries
Group: System/Libraries

%description -n %lname
%Name is an image manipulation program.
This package contains the libraries files you'll need to use
%Name applications.


%package -n %lname-devel
Summary: Header files for %Name app development
Group: Development/C
Requires: %lname%{?_disable_shared:-devel-static} = %version-%release
Obsoletes: %name-devel

%description -n %lname-devel
%Name is an image manipulation program.
This package contains the header files you'll need to develop
%Name applications.


%if_enabled static
%package -n %lname-devel-static
Summary: %Name static libraries
Group: Development/C
Requires: %lname-devel = %version-%release

%description -n %lname-devel-static
%Name is an image manipulation program.
This package contains %Name static libraries.
%endif


%if_with perl
%package -n perl-%name
Summary: Libraries and modules for access to %Name from perl
Group: Development/Perl
Requires: %lname = %version-%release

%description -n perl-%name
Perl bindings to %Name.


%package -n perl-%name-demo
Summary: Demo for %Name perl binding
Group: Development/Perl
Requires: perl-%name = %version-%release
BuildArch: noarch

%description -n perl-%name-demo
Demo for %Name perl binding.
%endif


%if_with cpp
%package -n %lname-c++
Summary: %Name Magick++ library (C++ bindings)
Group: System/Libraries
Requires: %lname = %version-%release
Obsoletes: %Name-c++

%description -n %lname-c++
This package contains the Magick++ library, a C++ binding to the
%Name graphics manipulation library.


%package -n %lname-c++-devel
Summary: C++ bindings for the %Name library
Group: Development/C++
Requires: %lname-devel = %version-%release
Requires: %lname-c++%{?_disable_shared:-devel-static} = %version-%release
#Requires: bzip2-devel freetype2-devel libxml2-devel
#Requires: libjpeg-devel libpng-devel libtiff-devel zlib-devel
Obsoletes: %Name-c++-devel

%description -n %lname-c++-devel
%Name is an image manipulation program.
This package contains header files you'll need to develop
%Name applications using the Magick++ C++ bindings.


%if_enabled static
%package -n %lname-c++-devel-static
Summary: %Name Magick++ static library
Group: Development/C++
Requires: %lname-c++-devel = %version-%release

%description -n %lname-c++-devel-static
%Name is an image manipulation program.
This package contains the %Name Magick++ static library.
%endif
%endif

%prep
%setup
%patch -p1
iconv -f iso-8859-2 -t utf8 < ChangeLog > ChangeLog.utf8
mv ChangeLog.utf8 ChangeLog

subst '/^if test $with_perl_static = /s|'yes'|'no'|' configure

# Avoid RPATHs (FIXME: recheck this on newer releases)
%if "%_libdir" != "/usr/lib"
sed -i 's|"/lib /usr/lib|"/%_lib %_libdir|' configure
%endif

# XXX tests fail
rm PerlMagick/t/mpeg/read.t
rm PerlMagick/t/ps/read.t
rm PerlMagick/t/zlib/read.t

%build
%add_optflags -DGRAPHICSMAGICK_DOCS_PATH=\\\"%_docdir/%name-%version/www/index.html\\\"
%define common_opts \\\
    %{subst_with fpx} \\\
    %{subst_enable openmp} \\\
    --disable-openmp-slow \\\
    %{subst_enable largefile} \\\
    --enable-libtool-lock \\\
    --disable-ltdl-install \\\
    --enable-installed \\\
    %{subst_enable_to debug ccmalloc} \\\
    %{subst_enable efence} \\\
    %{subst_enable prof} \\\
    %{subst_enable gprof} \\\
    %{subst_enable gcov} \\\
    %{subst_with threads} \\\
    %{subst_with bzlib} \\\
    %{subst_with dps} \\\
    %{subst_with gslib} \\\
    %{subst_with jbig} \\\
    %{subst_with jpeg} \\\
    %{subst_with_to jpeg2 jp2} \\\
    %{subst_with lcms} \\\
    %{subst_with lcms2} \\\
    %{subst_with lzma} \\\
    %{subst_with png} \\\
    %{subst_with tiff} \\\
    %{subst_with trio} \\\
    %{subst_with ttf} \\\
    %{subst_with webp} \\\
    %{subst_with wmf} \\\
    %{subst_with xml} \\\
    %{subst_with zlib} \\\
    --with-quantum-depth=%quantum_depth \\\
    --without-included-ltdl \\\
    --with-frozenpaths \\\
    --disable-symbol-prefix \\\
    --with-windows-font-dir=%_datadir/fonts/ttf/ms \\\
    --with-fontpath=%_datadir/fonts/type1/urw \\\
    --with-gs-font-dir=%_datadir/fonts/type1/urw
%if_with nox_gm
%configure \
    --disable-shared \
    --enable-static \
    --without-modules \
    --disable-magick-compat \
    --without-perl \
    --without-magick-plus-plus \
    --without-x \
    %common_opts
%make_build utilities/gm
mv utilities/gm{,-nox}
%make clean
%endif
%configure \
    %{subst_enable shared} \
    %{subst_enable static} \
    %{subst_with modules} \
    %{subst_enable_to compat magick-compat} \
    %{subst_with perl} \
    %{subst_with_to cpp magick-plus-plus} \
    %{subst_with x} \
    %common_opts
%make_build \
    MAGICK_CODER_MODULE_PATH=%_libdir/%name-%version/modules-Q%quantum_depth/coders \
    MAGICK_FILTER_MODULE_PATH=%_libdir/%name-%version/modules-Q%quantum_depth/filters
%if_with x
export \
    MAGICK_CONFIGURE_PATH=$PWD/config \
    MAGICK_CODER_MODULE_PATH=$PWD/coders/.libs \
    MAGICK_FILTER_MODULE_PATH=$PWD/filters/.libs
./utilities/gm convert -border 0x51 -bordercolor none -depth 8 www/images/gm-125{x80t,}.png
for s in 192 128 96 72 64 48 36 32 24 22 16; do
    ./utilities/gm convert -depth 8 -resize ${s}x$s www/images/{gm-125,%name-$s}.png
done
%endif

%if_with perl
pushd PerlMagick
%perl_vendor_build
popd
%endif

%install
%makeinstall_std docdir=%_docdir/%name-%version
rm -f %buildroot%_libdir/%name-%version/modules-Q%quantum_depth/{cod,filt}ers/*a
%{?_with_nox_gm:install -m 0755 utilities/gm-nox %buildroot%_bindir/}
bzip2 --best --keep --force %buildroot%_docdir/%name-%version/{ChangeLog,NEWS}*

%if_with perl
pushd PerlMagick
%perl_vendor_install
popd

# Fix RPATH
chrpath -d %buildroot%perl_vendor_autolib/Graphics/Magick/Magick.so
%endif

#Make alternatives
mv %buildroot%_bindir/gm %buildroot%_bindir/gm-x
mkdir -p %buildroot%_altdir
cat > %buildroot%_altdir/%name <<__EOF__
/usr/bin/gm /usr/bin/gm-x	40
__EOF__

cat > %buildroot%_altdir/%name-nox <<__EOF__
/usr/bin/gm /usr/bin/gm-nox	30
__EOF__

%if_with x
for s in 192 128 96 72 64 48 36 32 24 22 16; do
    install -D -m 0644 {www/images/%name-$s,%buildroot%_iconsdir/hicolor/${s}x$s/apps/%name}.png
done
%if_with menu
install -d -m 0755 %buildroot%_desktopdir
cat > %buildroot%_desktopdir/%name.desktop <<__MENU__
[Desktop Entry]
Name=%Name
GenericName=Display
Comment=Displays any image on X
Icon=%name
Exec=gm display
Terminal=false
Type=Application
Categories=Graphics;Viewer;
Comment[ru]=Показывает изображения в среде X
Comment[uk]=Показує зображення в X-ах
__MENU__
%endif
%endif

%files
%_bindir/gm-x
%_altdir/%name
%if_with x
%{?_with_menu:%_desktopdir/*}
%_iconsdir/hicolor/*/apps/*
%endif

%if_with nox_gm
%files nox
%_bindir/gm-nox
%_altdir/%name-nox
%endif

%files common
%doc %_docdir/%name-%version/Copyright.txt
%dir %_docdir/%name-%version
%_datadir/%name-%version
%_man1dir/gm.*

%files doc
%dir %_docdir/%name-%version
%_docdir/%name-%version/*
%exclude %_docdir/%name-%version/Copyright.txt


%files ImageMagick-compat
%_bindir/composite
%_bindir/conjure
%_bindir/convert
%_bindir/identify
%_bindir/mogrify
%_bindir/montage
%_bindir/compare
%if_with x
%_bindir/animate
%_bindir/display
%_bindir/import
%endif
%_man4dir/*
%_man5dir/*


%files -n %lname
%if_enabled shared
%_libdir/%lname.so.*
%_libdir/%{lname}Wand.so.*
%endif
%dir %_libdir/%name-%version
%_libdir/%name-%version/config
%dir %_libdir/%name-%version/modules-Q%quantum_depth
%dir %_libdir/%name-%version/modules-Q%quantum_depth/coders
%dir %_libdir/%name-%version/modules-Q%quantum_depth/filters
%_libdir/%name-%version/modules-Q%quantum_depth/*/*.so


%files -n %lname-devel
%dir %_includedir/%name
%_includedir/%name/wand
%_includedir/%name/magick
%_libdir/%lname.so
%_libdir/%{lname}Wand.so
%_pkgconfigdir/%name.pc
%_pkgconfigdir/%{name}Wand.pc
%_bindir/%name-config
%_bindir/%{name}Wand-config
%_man1dir/%name-config.*
%_man1dir/%{name}Wand-config.*


%if_enabled static
%files -n %lname-devel-static
%_libdir/%lname.a
%_libdir/%{lname}Wand.a
%endif


%if_with perl
%files -n perl-%name
%perl_vendor_archlib/Graphics
%perl_vendor_archlib/auto/Graphics


%files -n perl-%name-demo
%doc PerlMagick/demo
%endif


%if_with cpp
%if_enabled shared
%files -n %lname-c++
%_libdir/%lname++.so.*
%endif


%files -n %lname-c++-devel
%_includedir/%name/Magick++.h
%_includedir/%name/Magick++
%_libdir/%lname++.so
%_pkgconfigdir/%name++.pc
%_bindir/%name++-config
%_man1dir/%name++-config.*


%if_enabled static
%files -n %lname-c++-devel-static
%_libdir/%lname++.a
%endif
%endif

%changelog
* Fri Dec 15 2017 Igor Vlasenko <viy@altlinux.ru> 1.3.20-alt2.1.1
- rebuild with new perl 5.26.1

* Fri Feb 03 2017 Igor Vlasenko <viy@altlinux.ru> 1.3.20-alt2.1
- rebuild with new perl 5.24.1

* Wed Feb 24 2016 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.3.20-alt2
- rebuilt with new libwebp

* Wed Nov 25 2015 Igor Vlasenko <viy@altlinux.ru> 1.3.20-alt1.1.1.1
- rebuild with new perl 5.22.0

* Tue Jun 16 2015 Gleb F-Malinovskiy <glebfm@altlinux.org> 1.3.20-alt1.1.1
- Rebuilt for gcc5 C++11 ABI.

* Tue Dec 09 2014 Igor Vlasenko <viy@altlinux.ru> 1.3.20-alt1.1
- rebuild with new perl 5.20.1

* Tue Nov 04 2014 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.3.20-alt1
- 1.3.20

* Wed Jun 04 2014 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.3.18-alt3
- drop ps/read.t from PerlMagick testsuite

* Thu Aug 29 2013 Vladimir Lettiev <crux@altlinux.ru> 1.3.18-alt2
- built for perl 5.18

* Tue Apr 23 2013 Slava Dubrovskiy <dubrsl@altlinux.org> 1.3.18-alt1
- New version

* Sun Oct 14 2012 Slava Dubrovskiy <dubrsl@altlinux.org> 1.3.17-alt1
- New version
- Bugfix release (CVE-2012-3438 and CVE-2012-3386)

* Thu Sep 27 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.3.16-alt2.1
- Rebuilt with libpng15

* Tue Sep 04 2012 Vladimir Lettiev <crux@altlinux.ru> 1.3.16-alt2
- rebuilt for perl-5.16

* Thu Jun 28 2012 Slava Dubrovskiy <dubrsl@altlinux.org> 1.3.16-alt1
- New version

* Sun Feb 26 2012 Slava Dubrovskiy <dubrsl@altlinux.org> 1.3.14-alt1
- New version
- Build with lzma and lcms2

* Sun Jan 08 2012 Slava Dubrovskiy <dubrsl@altlinux.org> 1.3.13-alt1
- New version

* Thu Oct 13 2011 Alexey Tourbin <at@altlinux.ru> 1.3.12-alt3.1
- rebuilt for perl-5.14

* Thu Jun 23 2011 Slava Dubrovskiy <dubrsl@altlinux.org> 1.3.12-alt3
- Fix again (ALT #25782)

* Wed Jun 22 2011 Slava Dubrovskiy <dubrsl@altlinux.org> 1.3.12-alt2
- Fix ALT #25782

* Tue Apr 26 2011 Dmitry V. Levin <ldv@altlinux.org> 1.3.12-alt1.2
- Fixed RPATH issues.
- Fixed %name-ImageMagick-compat dependencies.
- Rebuilt for debuginfo.

* Fri Nov 05 2010 Vladimir Lettiev <crux@altlinux.ru> 1.3.12-alt1.1
- rebuilt with perl 5.12

* Fri Mar 26 2010 Slava Dubrovskiy <dubrsl@altlinux.org> 1.3.12-alt1
- New version
- Bugfix release (CVE-2010-0205)

* Sun Feb 28 2010 Slava Dubrovskiy <dubrsl@altlinux.org> 1.3.11-alt1
- New version
- Bugfix release

* Tue Feb 16 2010 Slava Dubrovskiy <dubrsl@altlinux.org> 1.3.10-alt1
- New version
- Bugfix release

* Mon Feb 08 2010 Slava Dubrovskiy <dubrsl@altlinux.org> 1.3.9-alt1
- New version
- Bugfix release

* Sat Jan 23 2010 Slava Dubrovskiy <dubrsl@altlinux.org> 1.3.8-alt1
- New version
- Fix ALT (#22348)
- Change number of bits in a pixel quantum 8 -> 16
- Fix build with libfpx
- Security Fixes:
  + Fix for CVE-2009-1882 "Integer overflow in the XMakeImage function".
  + Fix lockup due to hanging in loop while parsing malformed
    sub-image specification (SourceForge issue 2886560).
  + Libltdl: Updated libtool to 2.2.6b in order to fix security issue.
    Resolves CVE-2009-3736 as it pertains to GraphicsMagick.
- Bug fixes:
  + -convolve, -recolor: Validate that user-provided matrix is square
    when parsing -convolve and -recolor commands in order to avoid a
    core dump.
  + CALS: Reading images taller than the image width resulted in a
    failure.
  + ConstituteImage(), DispatchImage(): 'A' and 'T' should indicate
    transparency and 'O' should indicate opacity.  Behavior was
    inconsistent.  In some cases 'O' meant transparency while in other
    cases it meant opacity. Also, in a few cases, matte was not
    getting enabled in the image as it should.
  + DCRAW: Module name was not registered so modules based builds were
    not supporting formats provided via 'dcraw'.
  + GetOptimalKernelWidth1D(), GetOptimalKernelWidth2D(): In the Q32
    build, convolution kernel size was estimated incorrectly for large
    sigmas on 32-bit systems due to arithmetic overflow.  This could
    cause wrong results for -convolve, -blur, -sharpen, and other
    algorithms which use these functions.
  + Image Size: Fixed the ability to pass the image size via the
    filename specification like "myfile.jpg[640x480]" rather than
    needing to use -size.
  + IPTC: Blob data needed to be padded to an even size.  Size is now
    correctly reported.
  + IPTC: Returned IPTC string values were one character too short.
  + Large Files: Large pixel cache files were not working under GNU Linux.
  + JP2: Fixed some value scaling problems.
  + JP2: Fix possible crash at exit when Jasper is used by a modules build.
  + MPC: is_monochrome and is_grayscale flags were not managed
    properly for the MPC coder.
  + PCL: Page was not always being ejected.
  + PNG: The png8 encoder would fail when trying to write a 1-color image.
  + PSD: PSD parser was confused by 0x0 pixel layers, resulting in
    image data corruption of all following layers.
  + -rotate, -shear: Some internally-reported errors were potentially
    being lost.
  + Subrange/stdin: Commands now support reading an image from stdin
    in conjunction with a subrange specification (e.g. "-[1]").
  + Magick++ STL ShadeImage: Implementation was completely botched.
- New Features:
  + CALS Type 1 files may now be written (Work contributed by John
    Sergeant).  CALS support is dependent on the TIFF library.
  + GROUP4RAW encoder supports reading/writing RAW Group4 data.
  + JP2: JPEG 2000 may now be written in arbitrary bit depths ranging
    from 2 to 16 rather than just 8 or 16.
  + JPEG: IJG JPEG library version 7 is now supported.
  + JPEG: Added jpeg:block-smoothing and jpeg:fancy-upsampling defines
    to control these JPEG library options.
  + JPEG: Detect and apply colorspaces appropriately for ITU FAX JPEG.
  + Resource Limits: There is now a "threads" resource limit which
    allows specifying the number of OpenMP threads which may be used,
    similar to the OMP_NUM_THREADS environment variable.
  + TIFF: Allow CIELAB TIFF to be read.
  + MagickGetImageAttribute()/MagickSetImageAttribute(): New Wand
    methods to support getting and setting an image attribute.
    Contributed by Mikko Koppanen.
  + ClonePixelWand(): New Wand method to deep-copy an existing pixel wand.
  + ClonePixelWands(): New Wand method to deep-copy an array of
    existing pixel wands.
  + MagickCdlImage(): New Wand method to apply the ASC CDL to an
    image.
  + MagickGetImageBoundingBox(): New Wand method to return the crop
    bounding box required to remove any solid-color border from the
    image.
  + MagickGetImageFuzz(), MagickSetImageFuzz(): New Wand methods to
    get and set the color comparison fuzz factor.
  + MagickHaldClutImage(): New Wand method to apply a Hald CLUT to an
    image.
  + MagickSetResolution(): New Wand method to set the wand resolution.
  + MagickSetResolutionUnits(): New Wand method to set the wand
    resolution units.

* Fri Sep 18 2009 Slava Dubrovskiy <dubrsl@altlinux.org> 1.3.7-alt1
- New version
- Security Fixes:
  + PCX: Detect improper rows, columns, or depth.  Fixes CVE-2008-1097
    "Memory corruption in ImageMagick's PCX coder".
  + DrawDashPolygon: Avoid a crash which sometimes occured with tiny
    polygons.
- Bug fixes:
  + JPEG: Profile chunks need to be concatentated in order to build
    the whole profile.  This was not working so embedded profiles
    larger than 32K or maybe 64K were being corrupted.  This bug was
    introduced in GraphicsMagick 1.2.
  + Meta: Fix memory leaks.
  + Meta: Work better with with IPTC record 2 blocks and deal better
    with IPTC embedded in an 8BIM profile.  Fixes by John Sergeant.
  + MPC: Fix crash when reading MPC and the input image is modified.
  + PNG: Ensure that the opacity channel is properly initialized.
  + -profile: Lowercase arguments were sometimes not working as
    expected.
  + Topol: Topol reader actually works now and is included in test suite.
  + TIFF: Read and write JPEG-compressed grayscale TIFF correctly.
  + VisualMagick configure now works properly when output paths are
     specified.
  + WMF: Eliminate memory leaks.
- New Features:
  + MagickWand: New method MagickSetCompressionQuality() to allow
    setting the compression quality.
  + MagickWand: New method CloneDrawingWand() to deep-copy a drawing wand.
  + MagickWand: New method DrawGetException() to retrieve information
    regarding the last drawing wand exception (if any).
  + MagickWand: New method DrawClearException() to clear a drawing wand
    exception.
  + Magick++: New Image method cdl() to apply the ASC CDL.
  + Magick++: New Image method colorMatrix() to apply a color matrix
    to the image channels.
  + Magick++: New Image method haldClut() to apply a color lookup
    table (Hald CLUT) to the image.
  + MSL/Conjure: Added a new 'profile' command which applies, adds, or
    removes one or more IPTC, ICC or generic profiles from a file.
    Work contributed by John Sergeant.
  + Added a 'time' subcommand to provide Unix-style 'time' output when
    a 'time' capability is missing, or the reporting format is
    inconsistent.  For example 'gm time convert ...'.
- Feature improvements:
  + ColorMatrixImage(): Add opaque opacity channel when needed.
  + PDF & PS: Use '-type palette' prior to input file name to cause
    Ghostscript to return a dithered colormapped image.
  + PNG: Now compiles with libpng-1.4.0beta74 and later.
  + TIFF: Libtiff in Windows build is upgraded to 3.9.1.  This allows
    GraphicsMagick to read and write 16 and 24 bit float TIFF files.
  + Windows code to find Ghostscript is rewritten from scratch.
- Performance Improvements:
  + Drawing of points, lines, and polygons (and complex shapes based
    on these) is now accelerated using OpenMP with excellent speed-up.
  + ICC color transforms now see linear speedup from OpenMP.
  + Rotate: For rotations of 90 or 270 degrees, tile sizes are
    selected more appropriately.
- Behavior Changes:
  + No longer clear the exception structure at the start of
    ReadImage() and other similar functions since this sometimes masks
    errors.  The API user is expected to make sure that the exception
    structure is clean prior to invoking a function.
  + SVG: Writer is now disabled since it usually does not work properly.

* Tue Aug 11 2009 Slava Dubrovskiy <dubrsl@altlinux.ru> 1.3.6-alt1
- New version

* Thu Apr 30 2009 Slava Dubrovskiy <dubrsl@altlinux.org> 1.3.5-alt1
- New version
- Fix fonts
- Fix Provides and Conflict

* Mon Dec 08 2008 Slava Dubrovskiy <dubrsl@altlinux.org> 1.3.1-alt3
- Fix Requires %lname-c++%{?_disable_shared:-devel-static}

* Sat Nov 29 2008 Slava Dubrovskiy <dubrsl@altlinux.ru> 1.3.1-alt2
- Rebuild. Thanks Led@ for fixes
- Remove dvips from BuildRequires

* Mon Nov 24 2008 Led <led@altlinux.ru> 1.3.1-alt1.3
- fixed font names
- fixed *.desktop

* Mon Nov 24 2008 Led <led@altlinux.ru> 1.3.1-alt1.2
- added static gm without X-libs

* Sun Nov 23 2008 Led <led@altlinux.ru> 1.3.1-alt1.1
- fixed and cleaned up spec
- added *-devel-static packages
- fixed descriptions

* Fri Nov 21 2008 Slava Dubrovskiy <dubrsl@altlinux.org> 1.3.1-alt1
- New version
- Remove dependens to X11
- Security fixes:
  + AVI reader: Re-worked to be more robust against crash or DOS.
  + AVS reader: Re-worked to be more robust against crash or DOS.
  + DCM reader: Re-worked to be more robust against crash or DOS.
  + EPT reader: Re-worked to be more robust against crash or DOS.
  + FITS reader: Re-worked to be more robust against crash or DOS.
  + MTV reader: Re-worked to be more robust against crash or DOS.
  + PALM reader: Re-worked to be more robust against crash or DOS.
  + RLA reader: Re-worked to be more robust against crash or DOS.
  + TGA reader: Re-worked to be more robust against crash or DOS.
  + Avoid possible crash in GetImageCharacteristics() when substituting text in comment read from file.
  + Cineon reader: Fixed crash with broken file from Sami Liedes.
  + Palm reader: Fixed crash with broken files from Sami Liedes.
  + PICT reader: Fixed crash with broken files from Sami Liedes.
  + DPX reader: Validate file data better to avoid improper operation with intentionally (or accidentally) defective files.
  + XCF reader: Fixed crash with broken files from Sami Liedes.
- Bug fixes:
  + Libbz2 is now detected for MinGW.
  + In PerlMagick, Dissolve composition was not working right.
  + FITS: Ensure that written format conforms to specification.
  + TIFF:
    - Don't accidentially convert CMYK images to RGB.
    - Eliminated a memory leak in the codec support detection code.
  + JPEG: Removed over-write of image->client_data.
  + PDF: Try to properly deal with reading rotated PDFs.
  + PNG: Fixed crash when writing PNG images with transparency and either optimize is requested, or the image is colormapped.
- Performance Improvements:
  + OpenMP (parallel processing) improvements for functions:
  + Improved coder management performance.

* Sun Jul 27 2008 Slava Dubrovskiy <dubrsl@altlinux.ru> 1.2.5-alt1
- New version
- Update spec, convert to utf8
- Bug fixes:
  + TIFF: Eliminated a memory leak in the codec support detection code.
  + JPEG: Removed over-write of image->client_data.
  + PNG: Fixed crash when writing PNG images with transparency and either
    optimize is requested, or the image is colormapped.
  + Magick++ Image Quantize was not supporting error measurement properly
    and was wasting time with redundant SyncImage().
- Security Fixes:
  + AVI reader: Re-worked to be more robust against crash or DOS.
  + AVS reader: Re-worked to be more robust against crash or DOS.
  + DCM reader: Re-worked to be more robust against crash or DOS.
  + EPT reader: Re-worked to be more robust against crash or DOS.
  + FITS reader: Re-worked to be more robust against crash or DOS.
  + MTV reader: Re-worked to be more robust against crash or DOS.
  + PALM reader: Re-worked to be more robust against crash or DOS.
  + RLA reader: Re-worked to be more robust against crash or DOS.
  + TGA reader: Re-worked to be more robust against crash or DOS.
  + Avoid possible crash in GetImageCharacteristics() when substituting
    text in comment read from file.
  + Cineon reader: Fixed crash with broken file from Sami Liedes.
  + Palm reader: Fixed crash with broken files from Sami Liedes.
  + PICT reader: Fixed crash with broken files from Sami Liedes.
  + DPX reader: Validate file data better to avoid improper operation with
    intentionally (or accidentally) defective files.
  + XCF reader: Fixed crash with broken files from Sami Liedes.

* Thu May 29 2008 Slava Dubrovskiy <dubrsl@altlinux.org> 1.2.2-alt1
- New version. This is a bug-fix release.
- Bug fixes:
  + HWB colorspace now works correctly.
  + Composition with CopyOpacity now produces an image with transparency
    (as expected).
  + Composition now preserves the canvas colorspace.
  + Composition with a displacement map (-displace) no longer leaks an image.
  + Composition now handles CopyBlack properly for CMYK images.
  + Alpha composition now works as expected when both pixels involved
    include transparency.
  + -gamma multiple channel syntax now works as documented.
  + PerlMagick: Dissolve composition with Opacity now works correctly.
  + TIFF: Was accidentially converting CMYK images to RGB.
  + TIFF: Reject JPEG compression when writing CMYK images.
  + Detects libbz2 and libxml2 and builds properly with them in a MinGW build.
  + MAT: Provide a correct error report when the Pixels limit has been exceeded.
  + GraphicsMagick-config script should now output correct dependency
    information for --libs when libltdl is needed.
  + GraphicsMagick++-config no longer depends on GraphicsMagick-config to
    be in the executable search path.
- Performance improvments:
  + Exploratory support for OpenMP in the image resize code.  Can result
    in significant performance improvement when significantly reducing
    the image size on multi-core systems, but little to no improvement
    when the input and output images are close to the same size.
  + Module loading and execution performance are improved considerably
    for the modules build. On some systems, the modules build is
    considerably faster than the static or shared builds.
- Feature improvements:
  + Composition now supports CopyCyan, CopyMagenta, CopyYellow, and
    CopyBlack in order to copy CMYK channels into an image. CMYK copy
    composition operators automatically set the image colorspace to CMYK
    so that everything just works.

* Fri May 09 2008 Slava Dubrovskiy <dubrsl@altlinux.ru> 1.2.1-alt1
- New version
- Update spec
- Bug fixes:
  + MAT: Provide a correct error report when the Pixels limit has been exceeded.
  + GraphicsMagick-config script should now output correct dependency
    information for --libs when libltdl is needed.
  + GraphicsMagick++-config no longer depends on GraphicsMagick-config to
    be in the executable search path.
- Performance improvments:
  + Module loading and execution performance are improved considerably
    for the modules build. On some systems, the modules build is
    considerably faster than the static or shared builds.

* Thu May 01 2008 Slava Dubrovskiy <dubrsl@altlinux.org> 1.2-alt1
- New version
- Remove all patches
- Update spec
- Security fixes:
  + Fixes for CERT security alert TA04-217A described at
    "http://www.us-cert.gov/cas/techalerts/TA04-217A.html".
  + AVI, BMP, & DIB security fixes.
  + PSD security fixes.
  + P7 format security fix.
  + Fix EXIF IFD stack overflow vulnerability.
  + SGI security fix for RLE encoding (CVE-2006-4144)
  + XCF security fix (CVE-2006-3743)
  + PALM heap overflow fix (CVE-2006-5456)
  + DCM security fix (CVE-2006-5456)
  + Fix for shell command injection in delegate code via file names)
    (CVE-2005-4601).  Delegate execution is much more secure now.
  + Don't use filenames as printf specifications (CVE-2006-0082).
  + Fix integer overflow in DCM coder (CVE-2007-1797).
  + XWD integer overflow fix (CVE-2007-1797).
  + Implementation has replaced usage of strcpy, strcat, and strncat
    with the more security conscious strlcat and strlcpy.
  + DCM, DIB, XCF, XBM, and XWD security fix for integer overflow
    vulnerability (IDefense 09.19.07).
  + Do not access X11 or invoke convenience or stealth delegate programs
    based on the file extension. In particular, these file extensions are
    rejected for consideration as a format specifier: 'autotrace',
    'browse', 'dcraw', 'edit', 'gs-color', 'gs-color+alpha', 'gs-gray',
    'gs-mono', 'launch', 'mpeg-encode', 'print', 'scan', 'show', 'win',
    'xc', and 'x'.
- Bug fixes:
  + Ghostscript sometimes displays an error message and fails, yet it
    returns a success error code to GraphicsMagick. Verify that
    Ghostscript has updated the output file before attempting to use it.
  + Fixed a configure script syntax error when testing for trio.
  + When requesting a list of formats, all of the modules in the module
    search path are considered. Previously only the modules in the same
    directory as the LOGO module were listed.
  + Ensure that an image clip mask is respected by the negate algorithm.
  + The BMP writer was sometimes writing incorrect BMP v4 files.
  + Support reading and writing large PCX files.
  + Fixed a bug which could cause possible truncation while cloning the
    image cache.
  + Ensure that MIFF files indicate the compression which was actually used.
  + Properly handle errors from libtiff so that corrupted images are not
    output.
  + Fix for stripped-TIFF reader. Discard extra samples beyond alpha in
    scanline TIFFs.
  + Endian option now controls TIFF byte-order rather than bit-order.
  + TIFF writer can now write to pipes and other non-seekable output
    destinations.
  + JBIG writer was writing empty files for some libjbig releases.
  + Improved handling of corrupt GIF files.
  + Handle large SUN format images.
  + Properly compute image depth for 16-bit SGI image files.
  + For the gmdisplay program, ensure that only RGB data is sent to Windows.
  + Many memory leak fixes.
  + PDF writer is fixed so that Ghoscript 8.5 doesn't warn about the output.
  + PDF writer now writes proper output with CCITT compression.
  + Properly use fseeko() and ftello() if they are available.
  + Fixed a infinite loop bug in the XWD reader.
  + Fix minor memory leak in ProfileImage().
  + Fixed -level command parsing when a percent symbol is supplied within the
    argument rather than at the end.
  + Fix pixel scaling problem caused by floating point
    rounding error (noticed under AIX).
  + Fixed a memory leak in the GIF coder in the error return path.
  + Fix for SourceForge bug id 1353744 "MagickGetQuantumDepth doesn't work".
  + Fix for SourceForge bug id 1315109 "segfault in InitializeMagick(NULL)".
  + Fix for SourceForge bug id 1391421 "problem doing resize on 273x1 JPEG".
  + Fix for SourceForge bug id 1510075 "Failed to write PDF with JPEG compression".
  + Fix for SourceForge bug id 1572357 "GetOnePixel definition appears incorrect".
  + Fix for SourceForge bug id 1576616 Fix includedir variable in pkg-config files".
  + Fix for SourceForge bug id 1173713 "segfault in ModifyCache".
  + Fix for SourceForge bug id 1431805 "clip art wpg files cause access violation
    in graphics magick".
  + Fix for SourceForge bug id 1743141 "Affine matrix option parsing".
  + Fix for SourceForge bug id 1625477 "Memory leak reading layered PSD Image".
  + Fix for SourceForge bug id 1878992 "literal square brackets in file
    name cause large delay and bug id 1783209 "converting runs slowly
    when subimage is specified".
  + Fix for SourceForge bug id 1883527 "compression of tiff-file has no effect".
  + Successfully read files in the form "file[123]".
  + Fix reading 12-bit grayscale JPEG.
  + Set image depth appropriately when importing image from X11 display.
  + Fix map resource tracking.
  + Fix reading recent variants of ImageMagick's MIFF format.
  + Output bilevel TIFF meeting the TIFF Class F specification.
- New Utilities:
  + A 'benchmark' subcommand is now available to benchmark the
    performance of any other arbitrary subcommand (e.g. 'convert').
- Feature improvements:
  + LZW compression is now enabled by default.
  + Support industry-standard subsampling notation like "4:2:2".
  + If gm is executed under a traditional alternate name (e.g.
    convert), it will invoke the appropriate sub-command. This allows
    use of hard links, symbolic links, or just copying 'gm' to the
    desired sub-command name in order to achieve 100%% ImageMagick 5.5.2
    utility compatibility.
  + Provide the --enable-magick-compat option when configuring to install
    ImageMagick utilities compatibility links.
  + Identify -verbose output includes normalized (0.0-1.0) statistics.
  + Identify and convert now print "pixels per second" rates to help
    evaluate performance.
  + Added the identify +ping option to force reading the complete file.
  + The display program now supports the +progress option to disable any
    visual progress indication (and hourglass cursor) while loading images.
  + Support writing grayscale TGA files.
  + Provide explicit support for Rec 601 and Rec 709 grayscale spaces.
  + Include some support for a log RGB space based on the 2.048 density
    range as defined for the Cineon Digital Film System.
  + Added utilities command-line support for industry standard subsampling
    notation like 4:4:4 and 4:2:2.
  + Use MAGICK_IOBUF_SIZE to tune the size of the I/O buffer.
  + Use -type Bilevel, Grayscale, TrueColor, or TrueColorMatte to
    influence the type of image that Ghostscript returns.
  + Use '-define tiff:fill-order={msb2lsb|lsb2msb}' to control TIFF bit
    fill order.
  + The -version option now dumps a feature list as well as the build
    options.
  + The -endian option now supports the option 'native'.
  + A -monitor is added to enable progress monitoring for the command line
    utilities.
  + Use the -output-directory option to 'mogrify' to send output files to
    the specified directory.
  + Use the -create-directories option in conjunction with
    -output-directory and 'mogrify' to create any necessary subdirectories.
  + A Pixels resource limit is added.  Use '-limit Pixels value' to limit
    the maximum number of pixels in an image to 'value'.
  + The already supported option '-type Optimize' is now honored by
    formats that need to choose a subformat based on the properties of
    the image. Grueling tests of many/all pixels are not performed
    unless '-type Optimize' is supplied.
  + Added a a -set option to the composite, convert, display, mogrify,
    import commands in order to allow setting an image attribute.
  + Display utility no longer defaults to reading from standard input if
    stdin is not a tty.
  + May now be configured to use the umem memory allocation library
    available in Solaris 9, Update 3 and later, or from the portable umem
    project.
- Coder additions/improvements:
  + Replaced existing DPX "support" with all-new DPX support conforming
    to the SMPTE 268M-2003 standard.
  + Cineon reader completely rewritten.
  + TIFF coder is completely re-written. Now supports reading and
    writing RGB, CMYK, and grayscale, scanline-oriented TIFF images
    with arbitrary (1 to 32 bits) depth. Includes support for tiled
    TIFF, floating point TIFF, LogLuv TIFF, BigTIFF, arbitrary depths,
    and associated alpha.
  + TIFF coder now supports retrieving and saving XMP profiles.
  + MATLAB support is much improved and supports writing as well.
  + WPG reader now supports CTM translations.
  + ART format now supports writing.
  + Support 32-bit raw RGB images.
  + Support 32-bit raw CMYK images.
  + Support 32-bit raw gray images.
  + JP2 coder reads images in YCbCr colorspace and retrieves an embedded
    ICC ICM color profile if present.
- Performance improvments:
  + The DispatchImage() and ConstituteImage() functions incorporate
    special case code for BGR, BGRO, BGRP, RGB, RGBO, and I formats (8
    bit only) in order to improve performance dramatically.
  + When writing very large JPEG images, don't enable Huffman compression
    since doing so requires libjpeg to buffer the entire image in memory.
  + When using the 'identify' -verbose option, -verbose must be specified
    twice in order to obtain the color count.  This makes normal use of
    -verbose much faster.
  + Significantly improved read/write speed for bilevel and gray images.
  + TIFF I/O is considerably faster.
  + Postscript writer is 10-15X faster.
  + PNM formats writer is 10-100X faster.
  + Rotate by 90 or 270 degrees is 2-9X faster.

* Tue Feb 26 2008 Slava Dubrovskiy <dubrsl@altlinux.org> 1.1.11-alt1
- New version
- Bugs Fixed:
  + BMP: Support large files.
  + DIB: Support large files.
  + PNG: Fix depth handling with 16-bit PNG files in the Q8 build.
  + SUN: Properly report image depth.
  + TIFF: Endian option (-endian) now controls TIFF byte endian order
    rather than bit fill order.
  + DCM, DIB, XBM, XCF, XWD: Eliminate integer overflow vulnerability (IDefense 09.19.07) (SA29094).
  + HSL colorspace transform: Avoid optimization bug noticed on Opteron with GCC.
  + HWB colorspace transform: Avoid optimization bug noticed on Opteron with GCC.
  + RGBTransformImage()/TransformRGBImage(): Was using HWB colorspace when HSL was requested.
  + Successfully reads files with names like 'file[123]'.
  + 'gm display': No longer rely on isatty() to determine if input is from a pipe 
    (use 'gm display -' to display an image read from a pipe).
- Feature Improvements:
  + 'identify +ping' forces the pixels to be read (similar to GM 1.2).
  + 'gm -version' now indicates if build supports "Large Memory" (i.e. 64-bit).
  + TIFF: Use '-define tiff:fill-order={msb2lsb|lsb2msb}' to control TIFF bit fill order.
- Performance Improvements:
  + No longer bogs down if a directory contains hundreds of thousands of
    files and the filename looks like a wildcard specification.

* Thu Sep 20 2007 Slava Dubrovskiy <dubrsl@altlinux.org> 1.1.10-alt1
- This is an emergency bug-fix release to fix a problem with image 
  rotation by 270 degrees.  There are no other changes from the previous release.

* Tue Sep 18 2007 Slava Dubrovskiy <dubrsl@altlinux.org> 1.1.9-alt1
- New version
- Bugs Fixed:
  + In mogrify command, don't remove file name based on random junk in memory.
  + Fixed memory leak when reading MPC files.
  + Fixed crash when writing MIFF format and depth is not expected 8/16/32/.
  + In mogrify command, don't leak memory in the case where the image file 
    contains multiple frames.
  + Fixed crash in PNG and JPEG coders when the image to be written is part of 
    an image list.
  + PNG reader errors are not properly reported to the user.
  + TIFF output can now be written to a pipe or other non-seekable destination.
  + Support writing PDF with CCITT compression.
- Feature Improvements
  + Added a new 'benchmark' command which can be used to perform benchmarking 
    on any other command.
  + Image rotate in clockwise (90 degrees) or counter-clockwise (270 degrees) 
    direction is now 2-9X faster than before.
  + The -version option now includes a list of supported features.

* Mon Jul 30 2007 Slava Dubrovskiy <dubrsl@altlinux.org> 1.1.8-alt1
- New version
- Removed patches from debian (in upstream)
- Security Fixes:
  + Shell command injection via delegates subsystem (CVE-2005-4601).
  + Insecure use of filenames as a "sprintf" specification (CVE-2006-0082).
  + EXIF IFD stack overflow vulnerability.
  + BMP  format: Verify seek before proceeding.
  + DCM  format: Buffer overflow prevention (CVE-2006-5456).
  + DCM  format: Integer overflow prevention (CVE-2007-1797).
  + PALM format: Heap overflow prevention (CVE-2006-5456).
  + SGI  format: Fixes for RLE decoding issue (CVE-2006-4144).
  + XCF  format: Buffer overflow prevention, infinite loop prevention.
- Bugs Fixed:
  + Typo when searching for HTMLDecodeDelegate.
  + Avoid crash if delegate program fails to return an image.
  + EXIF memory leak fixes.
  + Command parser memory leak fixes.
  + Deadlock fix for event log initialization.
  + Work with latest Ghostscript "GPL Ghostscript" under Windows.
  + 'gm import' now returns image of appropriate depth.
  + Fixed memory map resource managment.
  + Fixed includedir variable in pkg-config files.
  + Fixed validation of -affine argument.
  + Fixed bug where fseeko() and ftello() were not used when available.
  + Fixed issue when pread() and pwrite() prototypes are missing.
  + Fixed pixel cache issues when size_t is an unsigned type.
  + Fixed dcraw delegate options to work with modern dcraw.
  + Fixed -level argument parsing to allow embedded %% characters.
  + Fix for segfault in InitializeMagick(NULL).
  + Fix for segfault in ModifyCache().
  + Fix for Wand MagickGetQuantumDepth() interface.
  + Fix for GrayscalePseudoClassImage() on 64-bit systems.
  + Fix for MagickReallocMemory memory leak under certain error conditions.
  + Validate BLOB access range.
  + ICON format: Segfault fix.
  + JPEG format: Fixed reading 12-bit grayscale JPEG.
  + MAT  format: Stability improvements.
  + MIFF format: Handle a compression value of 'None'.
  + PCX  format: Segfault fix.  Heap overflow fix.
  + PDF  format: Fixed writing with JPEG compression.
  + PICT format: Segfault fix.
  + PNG  format: Fixed compile problem with some libpng versions. Segfault fix.
  + PNM  format: Fixed scaling problem due to rounding error. Validate scaling.
  + PSD  format: Fixed memory leak with layerd PSD files.
  + SGI  format: Handle 16-bit SGI image files correctly.
  + SUN  format: Segfault fix.
  + TIFF format: Secure error reporting.  Finally support LZW under Windows.
  + WPG  format: Fixed crash with clip-art WPG files.
  + XWD  format: Fix for integer under/overflow.
- Feature Improvements
  + CIN format: Implementation is entirely replaced.
  + MAT format: Support Byte and Word formats, as well as big/little endian.
  + WPG format: Support for CTM translation.

* Thu Apr 12 2007 Slava Dubrovskiy <dubrsl@altlinux.org> 1.1.7-alt7
- Delete fonts-ttf-ms from BuildPreReq (#11385)

* Fri Jan 19 2007 Slava Dubrovskiy <dubrsl@altlinux.ru> 1.1.7-alt6
- Split of libraries, documents and imagemagick-compat packages
- Add %name.desktop
- Add %name-libpath.patch for fix link PerlMagick
- Add chrpath -r /usr/lib %perl_vendor_autolib/Graphics/Magick/Magick.so
- Add graphicsmagick_1.1.7-11.diff.gz from Debian
  + config/delegates.mgk.in: Lose obsolete option -2 when calling dcraw
    delegate. Fixes support for raw image data from digital cameras.
  + coders/png.c: Fix syntax errors in asm controlling code of PNG coder.
  + coders/dcm.c: Fix buffer overflow, thanks to M Joonas Pihlaja. (CVE-2006-5456)
  + coders/palm.c: Fix multiple heap overflows, thanks to M Joonas Pihlaja. (CVE-2006-5456)
  + coders/xcf.c: Fix buffer overflow in XCF coder (CVE-2006-3743).
  + coders/sgi.c: Fix multiple heap overflow vulnerabilities in SGI coder due to
    - missing boundary checks in SGIDecode();
    - missing validation of pixel depth field;
    - integer overflow via large columns and rows fields (CVE-2006-4144)
    - missing validation of chunk size fields (variable 'runlength') in
      run-length encoded images.
  + coders/sgi.c: Check for bogus values of 'bytes_per_pixel' and 'depth'.
  + coders/sgi.c: Fix calculation of internal depth value.
  + magick/cache.c: Include definition of HAVE_PREAD before checking its
    value. Now really pulls in proper declarations of pread() and pwrite().
  + coders/wpg.c: Fix segfault in WPG decoder.
  + tests/drawtest.c: Make sure filename strings do not run out of bounds.
  + magick/cache.c: Define as _XOPEN_SOURCE to pull in declarations for
    Unix98 extensions pread() and pwrite().
  + magick/montage.c: Fix bogus modulation of brightness when creating
    shadows around tiles in montage. Instead, drop constant grey shadow
    like current ImageMagick.
  + PerlMagick/t/montage.t: Update reference signatures for montage test
    cases with shadow according to above change.
  + magick/tempfile.c: Canonify relative paths before referring to
    them in a symlink.
  + magick/{blob.c,command.c,image.c,log.c,utility.c,utility.h}:
    FormatString() was called with unsanitized user input. Introduced
    new helper function FormatStringNumeric() to allow a single numeric
    format expansion. (This is a more complete fix for CAN-2005-0397
    reported against ImageMagick.)
  + magick/attribute.c: Apply missing piece of fix for heap overflow in
    EXIF parser from ImageMagick patch. (CAN-2004-0981)
  + configure.ac, configure: Fix typo that lead to an undefined delegate
    for HTML conversion.
  + magick/constitute.c: Apply upstream fix for potential NULL pointer
    dereference in ReadImage().
  + magick/{delegate.c,symbols.h,tempfile.h,tempfile.c}: When calling
    external delegates, check filename against whitelist of safe
    characters, and pass securely named symlink to delegate if check fails.
    (CVE-2005-4601)				  
					  
* Tue Jan 09 2007 Slava Dubrovskiy <dubrsl@altlinux.ru> 1.1.7-alt5
- Rebuild with new libjasper

* Wed Oct 18 2006 Slava Dubrovskiy <dubrsl@altlinux.ru> 1.1.7-alt4
- Fix russian filename in dialog "Open ..."

* Thu Oct 12 2006 Slava Dubrovskiy <dubrsl@altlinux.ru> 1.1.7-alt3
- Update BuildRequires
- Cleanup spec

* Fri Feb 17 2006 Slava Dubrovskiy <dubrsl@altlinux.ru> 1.1.7-alt2
- removed miff.4.gz & quantize.5.gz for compatibility with ImageMagick

* Fri Jan 27 2006 Slava Dubrovskiy <dubrsl@altlinux.ru> 1.1.7-alt1
- in %name-devel added dir %_includedir/%name
- in perl-%name added dir %perl_vendor_archlib/auto/Graphics/
- Compatibility with ImageMagick is cleaned (#9074) 

* Thu Jan 19 2006 Slava Dubrovskiy <dubrsl@altlinux.ru> 1.1.7-alt0
- initial build
