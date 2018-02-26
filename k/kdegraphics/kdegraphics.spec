%undefine __libtoolize
%define qtdir %_qt3dir
%define _optlevel s
%define _keep_libtool_files 1

%define unstable 0
%define gphoto 1
%define cmake 1

%add_findpackage_path %_K3bindir
%add_findprov_lib_path %_libdir/kde3

Name: kdegraphics
Version: 3.5.13
Release: alt3

Group: Graphical desktop/KDE
Summary: K Desktop Environment - Graphics
License: GPL
Url: http://www.kde.org/

Packager: Sergey V Turchin <zerg@altlinux.org>

Requires: %name-kamera = %version-%release
Requires: %name-kcoloredit = %version-%release
Requires: %name-kdvi = %version-%release
Requires: %name-kfax = %version-%release
Requires: %name-kfile = %version-%release
Requires: %name-kgamma = %version-%release
Requires: %name-kghostview = %version-%release
Requires: %name-kiconedit = %version-%release
Requires: %name-kmrml = %version-%release
Requires: %name-kooka = %version-%release
Requires: %name-kolourpaint = %version-%release
Requires: %name-kpdf = %version-%release
Requires: %name-kpovmodeler = %version-%release
Requires: %name-kruler = %version-%release
Requires: %name-ksnapshot = %version-%release
Requires: %name-ksvg = %version-%release
Requires: %name-kuickshow = %version-%release
Requires: %name-kview = %version-%release
Requires: %name-kviewshell = %version-%release
Requires: %name-libkscan = %version-%release

Source: kdegraphics-%version.tar
#Source: kdegraphics-3.0.98.tar.bz2
Source1: kdegraphics-kghostviewrc


# RH
Patch1: kdegraphics-3.3.0-misc.patch
Patch2: kdegraphics-3.3.1-xorg.patch
#
Patch4: kdegraphics-3.5.1-warning.patch
Patch5: kdegraphics-3.5.2-kpdf-xft.patch
# MDK
# ALT
Patch101: 3.5.12-fix-linking.patch
Patch102: kdegraphics-3.5.10-alt-fix-compile.patch
# Security
Patch301: xpdf-3.02pl4.patch
Patch302: security_01_CVE-2009-0945.diff
Patch303: security_02_CVE-2009-1709.diff
Patch304: xpdf-3.02-CVE-2010-3702.patch
Patch305: xpdf-3.02-CVE-2010-3704.patch
Patch306: tde-3.5.13-build-defdir.patch
Patch307: tde-3.5.13-DSO.patch


# Automatically added by buildreq on Tue Apr 13 2004 (-bi)
#BuildRequires: Mesa XFree86-devel XFree86-libs fontconfig-devel freetype2-devel gcc-c++ gcc-g77 glib2 imlib-devel kde-settings kdelibs-devel libGLU-devel libart_lgpl-devel libarts-devel libgphoto2-devel libieee1284-devel libjpeg-devel liblcms-devel libpng-devel libqt3-devel libsane-devel libstdc++-devel libtiff-devel libungif-devel libusb-devel menu-devel pkgconfig qt3-designer tetex-core xml-utils zlib-devel
BuildRequires(pre): cmake glibc-core kdelibs-devel
BuildRequires: fontconfig-devel freetype2-devel
BuildRequires: gcc-c++ imlib-devel libart_lgpl-devel
BuildRequires: libieee1284-devel libjpeg-devel openexr-devel
BuildRequires: liblcms-devel libpng-devel libqt3-devel libsane-devel libstdc++-devel
BuildRequires: libtiff-devel libungif-devel libusb-devel menu-devel pkg-config
BuildRequires: qt3-designer tetex-core xml-utils zlib-devel
BuildRequires: libfribidi-devel fribidi t1lib-devel libpoppler13-devel
BuildRequires: libacl-devel libattr-devel
BuildRequires: libXxf86vm-devel
#BuildRequires: kdelibs-devel-cxx = %__gcc_version_base
BuildRequires: kdelibs >= %version kdelibs-devel >= %version
%if %gphoto
BuildRequires: libgphoto2 libgphoto2-devel liblockdev-devel
%endif

%description
kdegraphics is a collection of graphic oriented applications:
 * kamera: digital camera io_slave for Konqueror. Together gPhoto this
          allows you to access your camera's picture with the URL camera:/
 * kcoloredit: contains two programs: a color value editor and also a color
               picker
 * kdvi: program (and embeddable KPart) to display *.DVI files from TeX
 * kfax: a program to display raw and tiffed fax images (g3, g3-2d, g4)
 * kfaxview: an embeddable KPart to display tiffed fax images
 * kfile-plugins: provide meta information for graphic files
 * kgamma: XFree86 Gamma correction KControl module.
 * kghostview: program (and embeddable KPart) to display *.PDF and *.PS
 * kiconedit: an icon editor
 * kmrml: A Konqueror plugin for searching pictures
 * kolourpaint: a simple pixel oriented image drawing program
 * kooka: a raster image scan program, based on SANE and libkscan
 * kpdf: a pdf viewer
 * kpovmodeler: A graphical editor for povray scenes
 * kruler: a ruler in inch, centimeter and pixel to check distances on the
           screen
 * ksnapshot: make snapshots of the screen contents
 * ksvg: SVG graphics viewer
 * kuickshow: fast and comfortable imageviewer
 * kview: picture viewer, provided as standalone program and embeddable KPart
 * kviewshell: generic framework for viewer applications

%package common
Summary: Common empty package for %name
Group: Graphical desktop/KDE
BuildArch: noarch
Requires: kde-common >= 3.2
Conflicts: kdegraphics <= 3.0
#
%description common
Common empty package for %name

%package kpdf
Summary: PDF viewer for KDE
Group: Graphics
Requires: %{get_dep kdelibs}
Requires: %name-common = %version-%release
#
%description kpdf
A PDF file viewer for KDE.
In addition to being a standalone viewer application,
kpdf acts as a Konqueror plugin.

%package ksvg
Summary: KDE implementation of the SVG
Group: Publishing
Requires: %{get_dep kdelibs}
Requires: %name-common = %version-%release
#
%description ksvg
KDE implementation of the
Scalable Vector Graphics Specifications.

%package kgamma
Summary: Simple tool for monitor gamma correction
Group: Graphics
Requires: %{get_dep kdelibs}
Requires: %name-common = %version-%release
Provides: kgamma = %version-%release
Obsoletes: kgamma
#
%description kgamma
KGamma allows you to alter the monitor's gamma correction of XFree86.
But that's not all to do. For good results you have to set the
correct brightness, contrast and color balance of your monitor.

%package kamera
Summary: Digital camera support for KDE
Group: Graphics
Requires: %{get_dep kdelibs}
Requires: %name-common = %version-%release
#
%description kamera
Kamera adds support for digital cameras to KDE.
After installing kamera, you can access your digital camera just like
a filesystem from KDE applications.

%package kcoloredit
Summary: KDE palette editor and color chooser
Group: Graphics
Requires: %{get_dep kdelibs}
Requires: %name-common = %version-%release
#
%description kcoloredit
KDE palette editor and color chooser.
kcoloredit can be used by other programs (and scripts) to pick a color or
edit a palette.

%package kdvi
Summary: KDE DVI (TeX output) file viewer
Group: Publishing
Requires: %{get_dep kdelibs}
Requires: %name-common = %version-%release
Requires: ghostscript-utils
#
%description kdvi
A DVI (TeX output) file viewer for KDE.

%package kfax
Summary: KDE Fax viewer
Group: Communications
Requires: %{get_dep kdelibs}
Requires: %name-common = %version-%release
#
%description kfax
A KDE viewer for incoming faxes

%package kfile
Summary: KFile module for reading graphical files information
Group: File tools
Requires: %{get_dep kdelibs}
Requires: %name-common = %version-%release
Provides: %name-kfile-png = %version-%release
Obsoletes: kdegraphics-kfile-png
#
%description kfile
The KFile plugin allows all applications using KFile (e.g. Konqueror) to view
information on bmp,dvi,gif,ico,jpeg,pcx,pdf,png,pnm,ps,tga,tiff,xbm files.

%package kghostview
Summary: PostScript viewer for KDE
Group: Publishing
Requires: %{get_dep kdelibs}
Requires: %name-common = %version-%release
Requires: ghostscript-module-X
#
%description kghostview
A PostScript file viewer for KDE.
In addition to being a standalone viewer application,
kghostview acts as a Konqueror plugin.

%package kiconedit
Summary: An icon editor for creating KDE icons
Group: Graphics
Requires: %{get_dep kdelibs}
Requires: %name-common = %version-%release
#
%description kiconedit
An icon editor for creating KDE icons

%package kmrml
Summary: MRML for KDE -- Content based image retrieval
Group: Graphics
Requires: %{get_dep kdelibs}
Requires: %name-common = %version-%release
#
%description kmrml
MRML is short for Multimedia Retrieval Markup Language,
which defines a protocol for querying a server for images
based on their content. See http://www.mrml.net about MRML
and the GNU Image Finding Tool (GIFT), an MRML server.

This package consists of an mrml kio-slave that handles
the communication with the MRML server and a KPart to
be embedded e.g. into Konqueror.

%package kooka
Summary: KDE scanner application
Group: Graphics
Requires: %{get_dep kdelibs}
Requires: %name-common = %version-%release
#
%description kooka
Kooka is a KDE application for previewing, cutting and receiving images
from a scanner.

%package kolourpaint
Summary: A paint program for KDE
Group: Graphics
Requires: %{get_dep kdelibs}
Requires: %name-common = %version-%release
#
%description kolourpaint
A paint program for KDE.

%package kpovmodeler
Summary: A graphical editor for povray scenes for KDE
Group: Graphics
Requires: %{get_dep kdelibs}
Requires: %name-common = %version-%release
Requires: povray
#
%description kpovmodeler
KPovModeler is a graphical editor for povray scenes.

%package kruler
Summary: A screen ruler and color measurement tool
Group: Graphics
Requires: %{get_dep kdelibs}
Requires: %name-common = %version-%release
#
%description kruler
A screen ruler and color measurement tool

%package ksnapshot
Summary: A KDE applet for taking snapshots of the desktop
Group: Graphics
Requires: %{get_dep kdelibs}
Requires: %name-common = %version-%release
#
%description ksnapshot
A KDE applet for taking screenshots.
ksnapshot allows both capturing the whole desktop and capturing just
the active window.

%package kuickshow
Summary: Quick picture viewer for KDE
Group: Graphics
Requires: %{get_dep kdelibs}
Requires: %name-common = %version-%release
#
%description kuickshow
Kuickshow is a picture viewer for KDE. It displays the directory structure,
displaying images as thumbnails.
Clicking on an image shows the image in its normal size.

%package kview
Summary: KDE Image Viewer
Group: Graphics
Requires: %{get_dep kdelibs}
Requires: %name-common = %version-%release
#
%description kview
KView is a KDE image viewer, supporting a wide range of graphics file formats.

%package kviewshell
Summary: Plugin integration for KView
Group: Graphics
Requires: %{get_dep kdelibs}
Requires: %name-common = %version-%release
Requires: %name-kview
#
%description kviewshell
KViewShell allows the kview image viewer to be embedded into other KDE
applications.

%package libkscan
Summary: KDE library for scanner support
Group: Graphics
Requires: %{get_dep kdelibs}
Requires: %name-common = %version-%release
#
%description libkscan
Library to access scanners used by kooka (and koffice)

%package devel
Summary: Include files for kdegraphics
Group: Development/KDE and QT
Requires: %name-common = %version-%release
Requires: %name-ksvg = %version-%release
Requires: %name-kviewshell = %version-%release
Requires: %name-libkscan = %version-%release
#
%description devel
This package contains include files needed to build applications
based on kdegraphic.

%prep
%setup -q -n kdegraphics-%version
%patch1 -p1
%patch2 -p1
#
%patch4 -p1
%patch5 -p1
#
%patch101 -p1
###%patch102 -p1
#
pushd kpdf/xpdf
%patch301 -p1
popd
%patch302 -p1
%patch303 -p1
pushd kpdf/xpdf
%patch304 -p0
%patch305 -p0
popd
%patch306
%patch307

%if %cmake
%else
sed -i '\|\${kdeinit}_LDFLAGS[[:space:]]=[[:space:]].*-no-undefined|s|-no-undefined|-no-undefined -Wl,--warn-unresolved-symbols|' admin/am_edit
for f in `find $PWD -type f -name Makefile.am`
do
    sed -i -e '\|_la_LDFLAGS.*[[:space:]]-module[[:space:]]|s|-module|-module \$(KDE_PLUGIN)|' $f
    #sed -i -e '\|_la_LDFLAGS.*[[:space:]]-no-undefined|s|-no-undefined|-no-undefined -Wl,--allow-shlib-undefined|' $f
    grep -q -e 'lib.*SOURCES' $f || continue
    RPATH_LINK_OPTS+=" -Wl,-rpath-link,`dirname $f`/.libs"
done
sed -i "s|\(-Wl,--as-needed\)| $RPATH_LINK_OPTS \1|g" admin/acinclude.m4.in
sed -i -e 's|\$USER_INCLUDES|-I%_includedir/tqtinterface \$USER_INCLUDES|' admin/acinclude.m4.in

find ./ -type f -name Makefile.am | \
while read f
do
    sed -i -e 's|\(.*_la_LIBADD[[:space:]]*\)=\(.*\)|\1= \$(LIBART_LIBS) -lfontconfig -lkdefx -lkdeinit_kded -lDCOP \$(LIB_KDEPRINT) \$(LIB_KPARTS) \$(LIB_KHTML) \$(LIB_KIO) \$(LIB_KDEUI) \$(LIB_KDECORE) \$(LIB_QT) \2|' $f
done
make -f admin/Makefile.common cvs ||:
%endif

%build
rm -rf %buildroot
export QTDIR=%qtdir
export KDEDIR=%_K3prefix

export PATH=$QTDIR/bin:$KDEDIR/bin:$PATH
export PKG_CONFIG_PATH=%_libdir/pkgconfig
export LD_LIBRARY_PATH=$QTDIR/%_lib:$KDEDIR/%_lib:$LD_LIBRARY_PATH
export LDFLAGS="-L%buildroot/%_libdir -L%buildroot/%_libdir/kde3 -L%_libdir"

%if %cmake
BD=%_builddir/%name-%version/BUILD

if ! [ -f $BD/CMakeCache.txt ]
then
%K3cmake \
    -DWITH_T1LIB=ON \
    -DWITH_LIBPAPER=ON \
    -DWITH_TIFF=ON \
    -DWITH_OPENEXR=ON \
    -DWITH_PDF=ON \
    -DBUILD_ALL=ON
fi
%K3make

%else
# else if cmake

%K3configure \
%if %unstable
    --enable-debug=full \
%else
    --disable-debug \
%endif
    --enable-final \
%if %gphoto
    --with-kamera \
%else
    --without-kamera \
%endif
    --with-openexr \
    --enable-multithreaded-kpdf
#    --with-poppler \

sed -ri 's/^(hardcode_libdir_flag_spec|runpath_var)=.*/\1=/' libtool
%make_build

%endif
# end if cmake

%install
%if %unstable
%set_strip_method none
%endif

%K3install

%if %cmake
install -dm 0755 %buildroot/%_kde3_iconsdir/
mv %buildroot/%_iconsdir/hicolor %buildroot/%_kde3_iconsdir/hicolor/

install -dm 0755 %buildroot/%_K3applnk/Graphics/
install -m 0644 %buildroot/%_K3xdg_apps/kruler.desktop %buildroot/%_K3applnk/Graphics/kruler.desktop

%endif

install -d %buildroot/%_K3conf/
install -m 0644 %SOURCE1 %buildroot/%_K3conf/kghostviewrc


%files
%files common
%_K3conf/*
%_K3cfg/*

%files ksvg
%_K3bindir/printnodetest
%_K3bindir/svgdisplay
%_K3lib/libksvgplugin.so*
%_K3lib/libksvgrendererlibart.so*
%_K3lib/svgthumbnail.so*
%_K3libdir/libksvg.so*
%_K3libdir/libtext2path.so*
%_K3apps/ksvg
%_K3srv/ksvglibartcanvas.desktop
%_K3srv/ksvgplugin.desktop
%_K3srv/svgthumbnail.desktop
%_K3srvtyp/ksvgrenderer.desktop

%files kpdf
%_K3bindir/kpdf
%_K3lib/libkpdfpart.so*
%_K3apps/kpdf
%_K3apps/kpdfpart
%_K3srv/kpdf_part.desktop
%_kde3_iconsdir/hicolor/*/apps/kpdf.*
%_K3doc/en/kpdf
%_K3xdg_apps/kpdf.desktop

%files kgamma
%_K3bindir/xf86gammacfg
%_K3lib/kcm_kgamma.so*
%_K3apps/kgamma
%_kde3_iconsdir/hicolor/*/apps/kgamma.*
%_K3doc/en/kgamma
%_K3xdg_apps/kgamma.desktop

%files kamera
%_K3lib/*kamera*.so*
%_K3iconsdir/crystalsvg/*/*/camera*
%_K3srv/camera.protocol
%doc %_K3doc/en/kamera
%_K3xdg_apps/kamera.desktop

%files kcoloredit
%_K3bindir/kcoloredit
%_K3bindir/kcolorchooser
#%_K3libdir/kcolorchooser*
%_K3apps/kcoloredit
%_kde3_iconsdir/hicolor/*/apps/kcoloredit.png
%_kde3_iconsdir/hicolor/*/apps/kcolorchooser.png
%doc %_K3doc/en/kcoloredit
%_K3xdg_apps/kcoloredit.desktop
%_K3xdg_apps/kcolorchooser.desktop

%files kdvi
%_K3bindir/kdvi
%_K3lib/kdvipart.so*
%_K3xdg_apps/kdvi.desktop
%_K3apps/kdvi
%_K3srv/kdvimultipage.desktop
%_kde3_iconsdir/hicolor/*/apps/kdvi.*
%doc %_K3doc/en/kdvi

%files kfax
%_K3bindir/kfax
#%_K3lib/kfaxpart.*
%_kde3_iconsdir/hicolor/*/apps/kfax.*
%_K3xdg_apps/kfax.desktop
%_K3apps/kfax
#
%_K3bindir/kfaxview
%_K3xdg_apps/kfaxview.desktop
%_K3libdir/libkfaximage.so*
%_K3lib/kfaxviewpart.so*
%_K3apps/kfaxview/
%_kde3_iconsdir/hicolor/*/apps/kfaxview.*
%_K3srv/kfaxmultipage.desktop
%_K3srv/kfaxmultipage_tiff.desktop

%files kfile
%_K3lib/kfile_*.so*
%_K3srv/kfile_*.*
%_K3libdir/libpoppler-tqt.so*

%files kghostview
%_K3bindir/kghostview
%_K3libdir/libkghostviewlib.so*
%_K3lib/libkghostviewpart.so*
%_K3lib/gsthumbnail.so*
#%config %_datadir/config/kghostviewrc
%_K3apps/kconf_update/kghostview.upd
%_K3apps/kconf_update/update-to-xt-names.pl
%_K3apps/kghostview
%_K3srv/gsthumbnail.desktop
%_K3srv/kghostview_part.desktop
%_kde3_iconsdir/hicolor/*/apps/kghostview.png
%_K3xdg_apps/kghostview.desktop
%doc %_K3doc/en/kghostview

%files kiconedit
%_K3apps/kiconedit
%_kde3_iconsdir/hicolor/*/apps/kiconedit.png
%_K3xdg_apps/kiconedit.desktop
%_K3bindir/kiconedit
%doc %_K3doc/en/kiconedit

%files kmrml
%_K3bindir/mrmlsearch
%_K3libdir/libkdeinit_mrmlsearch.so*
%_K3lib/kcm_kmrml.so*
%_K3lib/kded_daemonwatcher.so*
%_K3lib/kio_mrml.so*
%_K3lib/libkmrmlpart.so*
%_K3lib/mrmlsearch.so*
%_K3apps/konqueror/servicemenus/mrml-servicemenu.desktop
%_K3mimelnk/text/mrml.desktop
%_K3srv/kded/daemonwatcher.desktop
%_K3srv/mrml.protocol
%_K3srv/mrml_part.desktop
%_K3xdg_apps/kcmkmrml.desktop

%files kooka
%_K3bindir/kooka
#%_datadir/config/kookarc
%_K3apps/kooka
%_K3xdg_apps/kooka.desktop
%doc %_K3doc/en/kooka

%files kolourpaint
%doc kolourpaint/COPYING kolourpaint/NEWS kolourpaint/README kolourpaint/VERSION
%_K3bindir/kolourpaint
%_K3apps/kolourpaint
%_kde3_iconsdir/hicolor/*/apps/kolourpaint.*
%_K3xdg_apps/kolourpaint.desktop
%doc %_K3doc/en/kolourpaint

%files kpovmodeler
%_K3bindir/kpovmodeler
%_K3libdir/libkpovmodeler.so*
%_K3lib/libkpovmodelerpart.so*
%_K3apps/kpovmodeler
%doc %_K3doc/en/kpovmodeler
%_kde3_iconsdir/hicolor/*/apps/kpovmodeler.*
%_K3iconsdir/crystalsvg/*/*/kpovmodeler_doc.png
%_K3xdg_apps/kpovmodeler.desktop

%files kruler
%_kde3_iconsdir/hicolor/*/apps/kruler.png
%_K3apps/kruler
%_K3bindir/kruler
%doc %_K3doc/en/kruler
%_K3applnk/Graphics/kruler.desktop
%_K3xdg_apps/kruler.desktop

%files ksnapshot
%_K3bindir/ksnapshot
%_kde3_iconsdir/hicolor/*/apps/ksnapshot.*
%_K3xdg_apps/ksnapshot.desktop
%doc %_K3doc/en/ksnapshot

%files kuickshow
%_K3bindir/kuickshow
%_K3libdir/libkdeinit_kuickshow.so*
%_K3lib/kuickshow.so*
%_kde3_iconsdir/hicolor/*/apps/kuickshow.png
%_K3xdg_apps/kuickshow.desktop
%_K3apps/kuickshow
%doc %_K3doc/en/kuickshow

%files kview
%_K3bindir/kview
%_K3libdir/libkimageviewer.so*
%_K3libdir/libkdeinit_kview.so*
%_K3lib/libphotobook.so*
%_K3lib/kview.so*
%_K3lib/kcm_kview*.so*
#%_K3libdir/libkviewsupport.*
%_K3lib/kviewerpart.so*
%_K3lib/kview_*plugin.so*
%_K3lib/libkviewcanvas.so*
%_K3lib/libkviewviewer.so*
%_K3apps/photobook/
%_K3apps/kview
%_K3apps/kviewviewer
%_kde3_iconsdir/hicolor/*/apps/kview.png
%_K3srv/kviewviewer.desktop
%_K3srv/kviewcanvas.desktop
%_K3srv/kconfiguredialog/kview*
%_K3srv/photobook.desktop
%_K3srvtyp/kimageviewer.desktop
%_K3srvtyp/kimageviewercanvas.desktop
%_K3iconsdir/crystalsvg/*/apps/photobook.*
%doc %_K3doc/en/kview
%_K3xdg_apps/kview.desktop

%files kviewshell
%_K3bindir/kviewshell
%_K3libdir/libkmultipage*.so*
%_K3libdir/libdjvu.so*
%_K3lib/emptymultipagepart.so*
%_K3lib/djvuviewpart.so*
%_K3apps/djvumultipage.rc
%_K3apps/kviewshell
%_K3apps/kviewerpart
%_K3srv/djvumultipage.desktop
%_K3srv/emptymultipage.desktop
%_K3srvtyp/kmultipage.desktop
%_K3iconsdir/crystalsvg/*/*/kviewshell.png

%files libkscan
%_K3libdir/libkscan*.so*
%_K3iconsdir/crystalsvg/*/*/palette_color.png
%_K3iconsdir/crystalsvg/*/*/palette_gray.png
%_K3iconsdir/crystalsvg/*/*/palette_halftone.png
%_K3iconsdir/crystalsvg/*/*/palette_lineart.png
%_K3srv/scanservice.desktop

%files devel
%if %_keep_libtool_files
%_K3libdir/*.la
%_K3lib/*.la
%endif
%_K3includedir/*.h
%_K3includedir/kde/*.h
%_K3includedir/dom/*.h
%_K3includedir/libtext2path*/
%_K3includedir/ksvg/
%_K3includedir/kviewshell/


%changelog
* Thu Jun 21 2012 Roman Savochenko <rom_as@altlinux.ru> 3.5.13-alt3
- Poppler direct set to version 0.16.

* Sun Jun 16 2012 Roman Savochenko <rom_as@altlinux.ru> 3.5.13-alt2
- Build by DSO fix.

* Thu Feb 23 2012 Roman Savochenko <rom_as@altlinux.ru> 3.5.13-alt1
- TDE 3.5.13 release build

* Fri Feb 10 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.5.12-alt4.1
- Removed bad RPATH

* Fri Dec 02 2011 Sergey V Turchin <zerg@altlinux.org> 3.5.12-alt4
- built without poppler

* Tue Nov 08 2011 Sergey V Turchin <zerg@altlinux.org> 3.5.12-alt3
- fix build requires

* Wed Apr 20 2011 Andrey Cherepanov <cas@altlinux.org> 3.5.12-alt2.1
- remove xorg-x11-devel requirement

* Fri Feb 18 2011 Sergey V Turchin <zerg@altlinux.org> 3.5.12-alt2
- move to alternate place

* Wed Dec 29 2010 Sergey V Turchin <zerg@altlinux.org> 3.5.12-alt1
- new version

* Mon Oct 18 2010 Sergey V Turchin <zerg@altlinux.org> 3.5.10-alt5.M41.1
- built for M41

* Mon Oct 18 2010 Sergey V Turchin <zerg@altlinux.org> 3.5.10-alt5.M51.1
- built for M51

* Thu Oct 14 2010 Sergey V Turchin <zerg@altlinux.org> 3.5.10-alt6
- CVE-2010-3702 CVE-2010-3704 (ALT#24295)

* Tue Mar 09 2010 Sergey V Turchin <zerg@altlinux.org> 3.5.10-alt5
- fix to build with new autotools

* Thu Dec 24 2009 Sergey V Turchin <zerg@altlinux.org> 3.5.10-alt3.M41.1
- new built for M41

* Thu Dec 24 2009 Sergey V Turchin <zerg@altlinux.org> 3.5.10-alt3.M51.1
- built for M51

* Thu Dec 24 2009 Sergey V Turchin <zerg@altlinux.org> 3.5.10-alt4
- update to lastest branch 3.5
- Security fixes:
  - CVE-2009-0945
  - CVE-2009-1709

* Mon Oct 19 2009 Sergey V Turchin <zerg@altlinux.org> 3.5.10-alt2.M41.1
- built for M41

* Mon Oct 19 2009 Sergey V Turchin <zerg@altlinux.org> 3.5.10-alt3
- security fixes:
  - CVE-2009-3608

* Wed Apr 22 2009 Sergey V Turchin <zerg@altlinux.org> 3.5.10-alt1.M41.1
- built for M41

* Tue Apr 21 2009 Sergey V Turchin <zerg@altlinux.org> 3.5.10-alt2
- remove deprecated macroses from specfile

* Mon Apr 20 2009 Vladimir Lettiev <crux@altlinux.ru> 3.5.10-alt1.1
- Security fixes:
  - CVE-2009-0146
  - CVE-2009-0147
  - CVE-2009-0166
  - CVE-2009-0799
  - CVE-2009-0800
  - CVE-2009-1179
  - CVE-2009-1180
  - CVE-2009-1181
  - CVE-2009-1182
  - CVE-2009-1183

* Tue Aug 26 2008 Sergey V Turchin <zerg at altlinux dot org> 3.5.10-alt1
- new version

* Tue Apr 22 2008 Sergey V Turchin <zerg at altlinux dot org> 3.5.9-alt4
- build kpdf without poppler
- sync patches with MDK
- fix file confilicts between subpackages

* Fri Apr 18 2008 Sergey V Turchin <zerg at altlinux dot org> 3.5.9-alt3
- add %%*_ldconfig to kfax and kghostview
- rebuilt with new poppler

* Wed Mar 19 2008 Sergey V Turchin <zerg at altlinux dot org> 3.5.9-alt2
- rebuilt with new libgphoto2

* Fri Feb 22 2008 Sergey V Turchin <zerg at altlinux dot org> 3.5.9-alt1
- new version

* Wed Oct 17 2007 Sergey V Turchin <zerg at altlinux dot org> 3.5.8-alt1
- new version

* Wed Sep 26 2007 Sergey V Turchin <zerg at altlinux dot org> 3.5.7-alt3
- built kpdf with poppler

* Wed Aug 08 2007 Sergey V Turchin <zerg at altlinux dot org> 3.5.7-alt2
- add patch to fix CVE-2007-3387

* Wed May 23 2007 Sergey V Turchin <zerg at altlinux dot org> 3.5.7-alt1
- new version

* Mon Mar 26 2007 Sergey V Turchin <zerg at altlinux dot org> 3.5.6-alt2
- return requires to povray

* Fri Jan 26 2007 Sergey V Turchin <zerg at altlinux dot org> 3.5.6-alt1
- new version

* Thu Jan 25 2007 Sergey V Turchin <zerg at altlinux dot org> 3.5.5-alt2
- dont require povray while #10427 not fixed

* Mon Oct 16 2006 Sergey V Turchin <zerg at altlinux dot org> 3.5.5-alt1
- new version

* Mon Sep 04 2006 Sergey V Turchin <zerg at altlinux dot org> 3.5.4-alt1
- new version
- update some patches; thanks Alexey Morozov

* Mon Jun 19 2006 Sergey V Turchin <zerg at altlinux dot org> 3.5.3-alt2
- bump release to push incoming@ALT

* Tue Jun 06 2006 Sergey V Turchin <zerg at altlinux dot org> 3.5.3-alt1
- new version

* Mon May 22 2006 Sergey V Turchin <zerg at altlinux dot org> 3.5.2-alt3
- add patch for new freetype from KDE SVN
- merge patches from FC

* Thu May 18 2006 Sergey V Turchin <zerg at altlinux dot org> 3.5.2-alt2
- rebuilt with new gcc/libpoppler

* Thu Mar 30 2006 Sergey V Turchin <zerg at altlinux dot org> 3.5.2-alt1
- new version
- add patch to detect fribidi; 10x Alexey Morozov

* Fri Mar 24 2006 Sergey V Turchin <zerg at altlinux dot org> 3.5.1-alt3
- fix build with new binutils

* Mon Feb 27 2006 Sergey V Turchin <zerg at altlinux dot org> 3.5.1-alt2
- add patch for CVE-2006-0301
- fix BuildRequires

* Wed Feb 01 2006 Sergey V Turchin <zerg at altlinux dot org> 3.5.1-alt1
- new version

* Tue Jan 10 2006 Sergey V Turchin <zerg at altlinux dot org> 3.5.0-alt2
- add patch for pdf import in kpdf

* Wed Dec 07 2005 Sergey V Turchin <zerg at altlinux dot org> 3.5.0-alt1
- new version

* Tue Jun 07 2005 Sergey V Turchin <zerg at altlinux dot org> 3.4.1-alt1
- new version

* Fri Apr 01 2005 Sergey V Turchin <zerg at altlinux dot org> 3.4.0-alt1
- new version

* Mon Jan 24 2005 Sergey V Turchin <zerg at altlinux dot org> 3.3.2-alt4
- add patch for xpdf from kpdf

* Tue Jan 18 2005 Sergey V Turchin <zerg at altlinux dot org> 3.3.2-alt3
- rebuild

* Tue Jan 18 2005 Sergey V Turchin <zerg at altlinux dot org> 3.3.2-alt2
- rebuild gcc3.4

* Tue Jan 11 2005 Sergey V Turchin <zerg at altlinux dot org> 3.3.2-alt1
- rebuild

* Wed Jan 05 2005 ZerG <zerg@altlinux.ru> 3.3.2-alt0.0.M24
- new version

* Wed Dec 22 2004 Sergey V Turchin <zerg at altlinux dot org> 3.3.1-alt5
- add patch for xpdf in kpdf

* Wed Oct 20 2004 Sergey V Turchin <zerg at altlinux dot org> 3.3.1-alt4
- more fix patch for xpdf in kpdf
  thanks ldv@altlinux

* Tue Oct 19 2004 Sergey V Turchin <zerg at altlinux dot org> 3.3.1-alt3
- fix patch for xpdf in kpdf
  thanks ldv@altlinux

* Mon Oct 18 2004 Sergey V Turchin <zerg at altlinux dot org> 3.3.1-alt2
- add patch to fix xpdf in kpdf

* Thu Oct 07 2004 Sergey V Turchin <zerg at altlinux dot org> 3.3.1-alt1
- new version

* Sat Oct 02 2004 Sergey V Turchin <zerg at altlinux dot org> 3.3.0-alt1
- new version

* Wed Jun 16 2004 Sergey V Turchin <zerg at altlinux dot org> 3.2.3-alt2
- fix requires

* Mon Jun 07 2004 Sergey V Turchin <zerg at altlinux dot org> 3.2.3-alt1
- new version

* Wed May 19 2004 Sergey V Turchin <zerg at altlinux dot org> 3.2.2-alt2
- fix open non-latin1 filenames in kpdf
- use system xpdfrc in kpdf

* Tue Apr 13 2004 Sergey V Turchin <zerg at altlinux dot org> 3.2.2-alt1
- new version

* Tue Mar 16 2004 Sergey V Turchin <zerg at altlinux dot org> 3.2.1-alt1
- update code from KDE_3_2_BRANCH 

* Fri Mar 12 2004 Sergey V Turchin <zerg at altlinux dot org> 3.2.0-alt1
- new version
- update code from KDE_3_2_BRANCH

* Thu Sep 18 2003 Sergey V Turchin <zerg at altlinux dot org> 3.1.4-alt1
- update code from cvs

* Tue Sep 16 2003 Sergey V Turchin <zerg at altlinux dot org> 3.1.3-alt2
- rebuild with new libexif
- fix build requires

* Wed Aug 20 2003 Sergey V Turchin <zerg at altlinux dot org> 3.1.3-alt1
- update code from cvs

* Tue Jul 22 2003 Sergey V Turchin <zerg at altlinux dot org> 3.1.3-alt0.1
- update code from cvs

* Tue Jul 01 2003 Sergey V Turchin <zerg at altlinux dot org> 3.1.2-alt3
- update code from cvs

* Wed May 28 2003 Sergey V Turchin <zerg at altlinux dot ru> 3.1.2-alt2
- fix Provides

* Mon May 26 2003 Sergey V Turchin <zerg at altlinux dot ru> 3.1.2-alt1
- update code from cvs KDE_3_1_BRANCH

* Tue Apr 29 2003 Sergey V Turchin <zerg at altlinux dot ru> 3.1.1-alt4
- update code from cvs KDE_3_1_BRANCH

* Tue Apr 08 2003 Sergey V Turchin <zerg at altlinux dot ru> 3.1.1-alt3
- update code from cvs KDE_3_1_BRANCH
- apply ghostscript security fix patches

* Wed Apr 02 2003 Sergey V Turchin <zerg@altlinux.ru> 3.1.1-alt2
- rebuild with new libexif

* Mon Mar 31 2003 Sergey V Turchin <zerg@altlinux.ru> 3.1.1-alt1
- update code from cvs KDE_3_1_BRANCH

* Fri Mar 14 2003 Sergey V Turchin <zerg@altlinux.ru> 3.1.1-alt0.1
- update code from cvs KDE_3_1_BRANCH

* Tue Feb 18 2003 Sergey V Turchin <zerg@altlinux.ru> 3.1.0-alt5
- update code from cvs KDE_3_1_BRANCH

* Fri Feb 07 2003 Sergey V Turchin <zerg@altlinux.ru> 3.1.0-alt4
- update from cvs
- remove Requires: povray

* Tue Feb 04 2003 Sergey V Turchin <zerg@altlinux.ru> 3.1.0-alt3
- update from cvs

* Wed Jan 22 2003 Sergey V Turchin <zerg@altlinux.ru> 3.1.0-alt2
- update from cvs

* Thu Jan 09 2003 Sergey V Turchin <zerg@altlinux.ru> 3.1.0-alt1
- update from cvs
- add MDK patches

* Tue Nov 26 2002 Sergey V Turchin <zerg@altlinux.ru> 3.1.0-alt0.21
- update from cvs

* Wed Nov 06 2002 Sergey V Turchin <zerg@altlinux.ru> 3.1.0-alt0.20.rc2
- rc2

* Fri Nov 01 2002 Sergey V Turchin <zerg@altlinux.ru> 3.1.0-alt0.20.rc1
- rc1
- increase %%release to easy check dependencies

* Thu Oct 24 2002 Sergey V Turchin <zerg@altlinux.ru> 3.1.0-alt0.11
- update from cvs
- rebuild with new libgphoto
- recreate %%patch2

* Tue Oct 15 2002 Sergey V Turchin <zerg@altlinux.ru> 3.1.0-alt0.10
- update from cvs
- increase %%release to upgrade Daedalus

* Tue Sep 10 2002 Sergey V Turchin <zerg@altlinux.ru> 3.0.3-alt2
- rebuild with gcc 3.2

* Mon Aug 19 2002 Sergey V Turchin <zerg@altlinux.ru> 3.0.3-alt1
- new version

* Tue Jul 23 2002 Sergey V Turchin <zerg@altlinux.ru> 3.0.2-alt2
- add losted patch2

* Wed Jul 03 2002 Sergey V Turchin <zerg@altlinux.ru> 3.0.2-alt1
- new version

* Wed Jun 19 2002 AEN <aen@logic.ru> 3.0.1-alt3
- x11alpha driver for gs > 7.00 (patch2)

* Mon Jun 17 2002 Sergey V Turchin <zerg@altlinux.ru> 3.0.1-alt2
- fix menu items

* Sun May 26 2002 ZerG <zerg@altlinux.ru> 3.0.1-alt1
- new version

* Thu Apr 25 2002 Sergey V Turchin <zerg@altlinux.ru> 3.0-alt2
- move to /usr

* Thu Apr 04 2002 Sergey V Turchin <zerg@altlinux.ru> 3.0-alt1
- release

* Tue Apr 02 2002 Sergey V Turchin <zerg@altlinux.ru> 3.0-alt0.2.cvs20020401
- update from cvs

* Fri Mar 29 2002 Sergey V Turchin <zerg@altlinux.ru> 3.0-alt0.1.rc3
- build for ALT

* Mon Mar 25 2002 Laurent MONTEL <lmontel@mandrakesoft.com> 3.0-0.rc3.5mdk
- Fix buildrequires for 8.3
- Reactivate gphoto

* Mon Mar 25 2002 Laurent MONTEL <lmontel@mandrakesoft.com> 3.0-0.rc3.4mdk
- Fix build requires for 8.2
- Readd kooka

* Fri Mar 22 2002 Laurent MONTEL <lmontel@mandrakesoft.com> 3.0-0.rc3.3mdk
- RC3

* Sat Feb 09 2002 David BAUDENS <baudens@mandrakesoft.com> 3.0-0.beta2.3mdk
- Fix ./configure
- Enable debug
- Set unstable macro to 1
- Re-create devel package
- Fix and clean %%files sections

* Thu Feb 07 2002 Laurent MONTEL <lmontel@mandrakesoft.com> 3.0-0.beta2.2mdk
- Fix requires

* Wed Feb 06 2002 Laurent MONTEL <lmontel@mandrakesoft.com> 3.0-0.beta2.1mdk
- beta2

* Sat Dec 08 2001 Laurent MONTEL <lmontel@mandrakesoft.com> 3.0beta1-2mdk
- kde 3.0 beta1

* Sat Nov 24 2001 Laurent MONTEL <lmontel@mandrakesoft.com> 3.0-1mdk
- kde 3.0

