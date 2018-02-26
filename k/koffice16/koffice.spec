%define __libtoolize true
%define unstable 0
%define _optlevel s
%define glibc_core_ver %{get_version glibc-core}
%define _keep_libtool_files 1
%_K_if_ver_lt %glibc_core_ver 2.11
%define _keep_libtool_files 0
%endif
%def_disable gmagick

%add_findprov_lib_path %_libkde
%add_findpackage_path %_K3bindir
%add_findreq_skiplist %_Kapps/kross/python/RestrictedPython/*
%add_findreq_skiplist %_Kapps/chalk/scripts/*/*.rb
%add_verify_elf_skiplist %_libdir/libkexiformutils.so*
%add_verify_elf_skiplist %_libdir/libkexirelationsview.so*
%add_verify_elf_skiplist %_libdir/libkexidb.so*
%add_verify_elf_skiplist %_libdir/libkrossapi.so*
%add_verify_elf_skiplist %_libdir/libkexiguiutils.so*
%set_verify_elf_method no

%define qtdir %_qt3dir
%define kdedir %_K3prefix

%define rname koffice
Name: %{rname}16
Version: 1.6.3
%define rlz alt24
%define beta %nil
Serial: 4

%if "%beta" == "%nil"
Release: %rlz
%else
Release: %rlz.%beta
%endif

Group: Office
Summary: Set of office applications for KDE
URL: http://www.koffice.org/
License: GPL

#Requires: koffice-kexi = %version-%release
Requires: koffice-kivio = %version-%release
#Requires: koffice-karbon = %version-%release
#Requires: koffice-kchart = %version-%release
#Requires: koffice-chalk = %version-%release
#Requires: koffice-kformula = %version-%release
#Requires: koffice-libs = %version-%release
#Requires: koffice-kpresenter = %version-%release
#Requires: koffice-kspread = %version-%release
#Requires: koffice-kugar = %version-%release
#Requires: koffice-kword = %version-%release
#Requires: koffice-kplato = %version-%release

%if "%beta" == "%nil"
Source: koffice-%version.tar
%else
Source: koffice-%version-%beta.tar
%endif

# ALT
Patch20: koffice-1.6.2-alt-desktop-categories.patch
Patch21: koffice-1.6.2-alt-no-kexi-examples.patch
Patch22: koffice-1.6.3-alt-new-imagick.patch
Patch23: koffice-1.6.3-alt-new2-imagick.patch
Patch24: koffice-1.6.3-alt-new3-imagick.patch
Patch25: koffice-1.6.3-alt-disable-gm.patch
Patch27: koffice-1.6.3-alt-no-tools.patch
Patch30: tde-3.5.13-build-defdir-autotool.patch
Patch31: koffice-1.6.3-alt-automake.patch

# Automatically added by buildreq on Thu Mar 18 2004 (-bi)
#BuildRequires: XFree86-devel XFree86-libs bzlib-devel doxygen fontconfig-devel freetype2-devel gcc-c++ glib2-devel kde-settings kdelibs-devel libImageMagick-devel libart_lgpl-devel libarts-devel libaspell-devel libexif-devel libgsf-devel libjpeg-devel liblcms-devel libpng-devel libqt3-devel libstdc++-devel libtiff-devel libwv2-devel libxml2-devel libxslt-devel pkgconfig python-devel qt3-designer qt3-doc xml-utils zlib-devel

BuildRequires(pre): kdelibs-devel
BuildRequires: bzlib-devel doxygen openexr-devel
BuildPreReq: libX11-devel libXaw-devel libXext-devel libXv-devel libICE-devel
BuildRequires: fontconfig-devel freetype2-devel gcc-c++ glib2-devel
BuildRequires: libImageMagick-devel
%if_enabled gmagick
BuildRequires: libGraphicsMagick-c++-devel
%endif
BuildRequires: kdelibs-devel libart_lgpl-devel
BuildRequires: libaspell-devel libexif-devel libgsf-devel libjpeg-devel liblcms-devel
BuildRequires: libpng-devel libqt3-devel libstdc++-devel libtiff-devel libwv2-devel
BuildRequires: libxml2-devel libxslt-devel pkg-config python-devel ruby libruby-devel
#BuildRequires: libpoppler-qt-devel
BuildRequires: libMySQL-devel libwpd-devel
#BuildRequires: libpqxx-devel
#libacl-devel libattr-devel
BuildRequires: qt3-designer qt3-doc xml-utils zlib-devel libreadline-devel
#BuildRequires: kdelibs-devel-cxx = %__gcc_version_base
BuildRequires: kdelibs >= 3.0.0 kdelibs-devel >= 3.0.0

%description
Office applications for the K Desktop Environment.

KOffice contains:
   * KWord: word processor
   * KSpread: spreadsheet
   * KPresenter: presentations
   * KChart: diagram generator
   * Kontour
   * Krayon
   * Kugar
   * Kivio
   * Some filters (Excel 97, Winword 97/2000, etc.)

%package common
Summary: Common empty package for %{rname}
Group: Graphical desktop/KDE
Requires: kde-common >= 3.2
Conflicts: koffice <= 1.2.1-alt4
%description common
Common empty package for %{rname}

%package devel
Group: Development/KDE and QT
Summary: Header files for developing koffice applications
Requires: %name-common = %serial:%version-%release
#
%description devel
Header files needed for developing koffice applications.

%package libs
Group: System/Libraries
Summary: Common libraries for koffice
Requires: kdelibs >= %{get_version kdelibs}
Requires: %name-common = %serial:%version-%release
%description libs
Common libraries for koffice

%package kplato
Group: Office
Summary: Project planning and management application
Requires: kdelibs >= %{get_version kdelibs}
Requires: %name-common = %serial:%version-%release
#
%description kplato
Kplato is a project management application and a planning tool.
As an integrated component of Koffice, Kplato can
be used within larger documents of other Koffice components.

%package karbon
Group: Graphics
Summary: Vector graphics application
Requires: kdelibs >= %{get_version kdelibs}
Requires: %name-common = %serial:%version-%release
#
%description karbon
Vector graphics application

%package kchart
Group: Office
Summary: Chart generator
Requires: kdelibs >= %{get_version kdelibs}
Requires: %name-common = %serial:%version-%release
#
%description kchart
Chart generator

%package kformula
Group: Office
Summary: Formula editor
Requires: kdelibs >= %{get_version kdelibs}
Requires: %name-common = %serial:%version-%release
#
%description kformula
Formula editor

%package -n koffice-kivio
Group: Office
Summary: Flowcharting tool
Requires: kdelibs >= %{get_version kdelibs}
Requires: %name-common = %serial:%version-%release
%description -n koffice-kivio
Flowcharting tool

%package kontour
Group: Office
Summary: Illustration tool
Obsoletes: kontour
Requires: kdelibs >= %{get_version kdelibs}
Requires: %name-common = %serial:%version-%release
#
%description kontour
Illustration tool

%package koshell
Group: Office
Summary: Koffice workspace
Requires: kdelibs >= %{get_version kdelibs}
Requires: %name-common = %serial:%version-%release
#
%description koshell
Koffice workspace

%package kpresenter
Group: Office
Summary: Presentation tool
Requires: kdelibs >= %{get_version kdelibs}
Requires: %name-common = %serial:%version-%release
#
%description kpresenter
Presentation tool

%package kspread
Group: Office
Summary: Spreadsheet application
Requires: kdelibs >= %{get_version kdelibs}
Requires: %name-common = %serial:%version-%release
#
%description kspread
Spreadsheet application

%package kugar
Group: Office
Summary: A template driven report viewer for XML data
Requires: kdelibs >= %{get_version kdelibs}
Requires: %name-common = %serial:%version-%release
#
%description kugar
A template driven report viewer for XML data

%package chalk
Group: Graphics
Summary: Paint application for bitmap images.
Requires: kdelibs >= %{get_version kdelibs}
Requires: %name-common = %serial:%version-%release
#
%description chalk
Chalk is a paint application for bitmap images.

%package kword
Group: Office
Summary: Word processor
Requires: kdelibs >= %{get_version kdelibs}
Requires: %name-common = %serial:%version-%release
#
%description kword
Word processor

%package -n koffice-kexi
Group: Office
Summary: Database management
Requires: kdelibs >= %{get_version kdelibs}
Requires: %name-common = %serial:%version-%release
%description -n koffice-kexi
Office database management program

%prep
%if "%beta" == "%nil"
%setup -q -n %{rname}-%version
%else
%setup -q -n %{rname}-%version-%beta
%endif

%patch20 -p1
%patch21 -p1
%patch22 -p1
%patch23 -p1
%patch24 -p1
%if_disabled gmagick
%patch25 -p1
%endif
%patch27 -p1
%patch30
%patch31 -p0

# hack to fix add .h .cpp .moc
#for f in `find ./ -type f -name \*.ui`
#do
#    %qtdir/bin/uic $f -o `echo $f|sed "s/\.ui/.h/"` 2>/dev/null ||:
#    %qtdir/bin/uic $f -impl `echo $f|sed "s/\.ui/.h/"` $f -o `echo $f|sed "s/\.ui/.cpp/"` 2>/dev/null ||:
#done
#for f in `find ./ -type f -name \*.h`; do %qtdir/bin/moc $f -o `echo $f|sed "s/\.h/.moc/"` 2>/dev/null ||:; done

# fix compile with qt-3.3.8d
sed -i "s|QSplitterLayoutStruct|KDGanttSplitterLayoutStruct|g" kdgantt/KDGanttMinimizeSplitter.*

%if %_keep_libtool_files
for f in `find $PWD -type f -name Makefile.am`
do
    grep -q LDFLAGS $f || continue
    RPATH_LINK_OPTS+=" -Wl,-rpath-link,`dirname $f`/.libs"
done
sed -i "s|\(-Wl,--as-needed\)| $RPATH_LINK_OPTS \1|g" admin/acinclude.m4.in
%else
#subst "s/\(Wl,--no-undefined\)/-Wl,--warn-unresolved-symbols \1/g" admin/acinclude.m4.in
subst "s/\(Wl,--no-undefined\)/ -Wl,--allow-shlib-undefined \1/g" admin/acinclude.m4.in
subst "s/\-lkdeui/-lkdeui -lpthread/g" admin/acinclude.m4.in
subst "s/\.la/.so/g" admin/acinclude.m4.in
%endif

cp -Rp /usr/share/libtool/aclocal/libtool.m4 admin/libtool.m4.in
cp -Rp /usr/share/libtool/config/ltmain.sh admin/ltmain.sh
make -f admin/Makefile.common cvs


%build
#export PYTHONDIR=/usr/lib/python2.2
export QTDIR=%qtdir KDEDIR=%kdedir
export PATH=$QTDIR/bin:$KDEDIR/bin:$PATH
export LDFLAGS="-L%qtdir/lib"
export CXXFLAGS="-I%_includedir/poppler/qt3"
export DO_NOT_COMPILE="example karbon chalk kword kspread kchart kpresenter kformula kugar chalk kplato kexi"
# add_optflags %optflags_shared -DHAVE_EACCESS -I%_includedir/tqtinterface

%configure \
    \
%if "%beta" != "%nil" || %unstable
    --disable-final \
%else
    --enable-final \
%endif
    \
%if %unstable
    --enable-debug=full \
%else
    --enable-debug=no \
%endif
%if "%beta" != "%nil"
    --enable-debug=yes \
%endif
    \
%ifarch x86_64
    --enable-libsuffix=64 \
%endif
    --disable-static \
    --enable-shared \
    --disable-embedded \
    --disable-palmtop \
    --with-xinerama \
    --with-gnu-ld \
    --enable-new-ldflags \
    --with-pic \
    --disable-rpath \
    --program-transform-name="" \
    --mandir=%_mandir \
    --enable-mysql \
    --enable-scripting \
		--without-arts

#    --enable-pgsql \

%make_build
#make_build -C filters/kpresenter/powerpoint
#make_build -C filters/chalk/magick

%install
%if %unstable
%set_strip_method none
%endif

%make install DESTDIR=%buildroot RUN_KAPPFINDER=no
#make install DESTDIR=%buildroot RUN_KAPPFINDER=no -C filters/kpresenter/powerpoint
#make install DESTDIR=%buildroot RUN_KAPPFINDER=no -C filters/chalk/magick

# delete files same with kdelibs
#for n in `rpm -ql kdelibs| grep /usr/share/mimelnk`
#do
#    [ -f %buildroot/$n ] && rm -f  %buildroot/$n
#done

# move .desktop-s
for f in `find %buildroot/%_Kapplnk -type f -name *.desktop| grep -v chalk_`
do
    mv $f %buildroot/%_Kmenudir/
done
for f in `find %buildroot/%_Kapplnk -type f -name *.desktop| grep -v '.hidden'`
do
    mv $f %buildroot/%_Kapplnk/.hidden/
done

# move configs
mkdir -p %buildroot/%_Kconfig
#mv %buildroot/%_datadir/config/* %buildroot/%_Kconfig/


%files
%files common

%files libs
%doc %_docdir/HTML/en/koffice
%_bindir/krossrunner
%_Klibdir/clipartthumbnail.so*
%_Klibdir/kodocinfopropspage.so*
%_Klibdir/kofficescan.so*
%_Klibdir/kofficethumbnail.so*
%_Klibdir/krosspython.so*
%_Klibdir/libgenerickofilter.so*
%_Klibdir/libkounavailpart.so*
%_Klibdir/libthesaurustool.so*
%_Klibdir/libxsltexport.so*
%_Klibdir/libxsltimport.so*
%_libdir/libkformulalib.so*
%_libdir/libkochart.so*
%_libdir/libkofficecore.so*
%_libdir/libkofficeui.so*
%_libdir/libkopainter.so*
%_libdir/libkopalette.so*
%_libdir/libkoproperty.so*
%_libdir/libkotext.so*
%_libdir/libkowmf.so*
%_libdir/libkrossapi.so*
%_libdir/libkrossmain.so*
%_libdir/libkstore.so*
%_libdir/libkwmf.so*
%_Kapps/koffice/
%_Kapps/kofficewidgets/
%_Kapps/kross/
%_Kapps/thesaurus/
%_Kapps/xsltfilter/
%_iconsdir/*/*/actions/abs.png
%_iconsdir/*/*/actions/brackets.png
%_iconsdir/*/*/actions/frac.png
%_iconsdir/*/*/actions/gsub.png
%_iconsdir/*/*/actions/gsup.png
%_iconsdir/*/*/actions/int.png
%_iconsdir/*/*/actions/lsub.png
%_iconsdir/*/*/actions/lsup.png
%_iconsdir/*/*/actions/matrix.png
%_iconsdir/*/*/actions/multiline.png
%_iconsdir/*/*/actions/onetwomatrix.png
%_iconsdir/*/*/actions/over.png
%_iconsdir/*/*/actions/paren.png
%_iconsdir/*/*/actions/prod.png
%_iconsdir/*/*/actions/rsub.png
%_iconsdir/*/*/actions/rsup.png
%_iconsdir/*/*/actions/sqrt.png
%_iconsdir/*/*/actions/sum.png
%_iconsdir/*/*/actions/under.png
%_iconsdir/*/*/actions/inscol.png
%_iconsdir/*/*/actions/insrow.png
%_iconsdir/*/*/actions/remcol.png
%_iconsdir/*/*/actions/remrow.png
%_Kservices/clipartthumbnail.desktop
%_Kservices/generic_filter.desktop
%_Kservices/kodocinfopropspage.desktop
%_Kservices/kofficethumbnail.desktop
%_Kservices/kounavail.desktop
%_Kservices/thesaurustool.desktop
%_Kservices/xslt_export.desktop
%_Kservices/xslt_import.desktop
#%_Kservices/ole_powerpoint97_import.desktop
%_Kservicetypes/kochart.desktop
%_Kservicetypes/kofficepart.desktop
%_Kservicetypes/kofilter.desktop
%_Kservicetypes/kofilterwrapper.desktop
%_Kservicetypes/koplugin.desktop
# ---------- kfile ------------
%_Klibdir/kfile_abiword.so*
%_Klibdir/kfile_gnumeric.so*
%_Klibdir/kfile_koffice.so*
%_Klibdir/kfile_ooo.so*
%_Kservices/kfile_abiword.desktop
%_Kservices/kfile_gnumeric.desktop
%_Kservices/kfile_koffice.desktop
%_Kservices/kfile_ooo.desktop
# ---------- koshell ------------
%doc %_docdir/HTML/en/koshell
%_bindir/koshell
%_libdir/libkdeinit_koshell.so*
%_Klibdir/koshell.so*
%_Kcfg/koshell.kcfg
%_Kmenudir/koshell.desktop
%_Kapps/koshell
%_iconsdir/*/*/apps/koshell.*
#
#%doc %_docdir/HTML/en/thesaurus
#%_Klibdir/kthesaurus.so*
#%_libdir/libkdeinit_kthesaurus.so*
#%_Kmenudir/KThesaurus.desktop
#%_bindir/koconverter
#%_bindir/kthesaurus
#%_Klibdir/krossruby.so*
#%_Klibdir/libolefilter.so*
#%_libdir/libkchartimageexport.so*
#%_libdir/libkchartcommon.so*
#%_libdir/libkdchart.so*
#%_libdir/libkspreadcommon.so*


%files -n koffice-kivio
%_Klibdir/libkivioimageexport.so*
%_Kservices/kivio_image_export.desktop
%_datadir/apps/konqueror/servicemenus/kivio_konqi.desktop
%_Kcfg/kivio.kcfg
#
%doc %_docdir/HTML/en/kivio
%_bindir/kivio
%_Klibdir/kivio.so*
%_Klibdir/libkivioconnectortool.so*
%_Klibdir/libkiviopart.so*
%_Klibdir/libkivioselecttool.so*
%_Klibdir/libkiviotargettool.so*
%_Klibdir/libkiviotexttool.so*
%_Klibdir/libkiviozoomtool.so*
%_Klibdir/straight_connector.so*
%_libdir/libkdeinit_kivio.so
%_libdir/libkiviocommon.so*
%_Kmenudir/kivio.desktop
%_Kapps/kivio/
%_iconsdir/*/*/apps/kivio.png
%_Kservices/kivioconnectortool.desktop
%_Kservices/kiviopart.desktop
%_Kservices/kivioselecttool.desktop
%_Kservices/kiviotargettool.desktop
%_Kservices/kiviotexttool.desktop
%_Kservices/kiviozoomtool.desktop

%if 0
%files -n koffice-kexi
%_datadir/apps/konqueror/servicemenus/kexi_konqi.desktop
#
%doc %_docdir/HTML/en/kexi
%_bindir/kexi
%_bindir/kexi_*
%_bindir/ksqlite*
%_Klibdir/kexidb_*.so*
%_Klibdir/kexihandler_*.so*
%_Klibdir/keximigrate_*.so*
%_Klibdir/kexi.so*
%_Klibdir/kformdesigner_*.so*
%_Klibdir/krosskexiapp.so*
%_Klibdir/krosskexidb.so*
%_libdir/libkdeinit_kexi.so*
%_libdir/libkexidbparser.so*
%_libdir/libkexidb.so*
%_libdir/libkexiutils.so*
%_libdir/libkexicore.so*
%_libdir/libkexidatatable.so*
%_libdir/libkexiextendedwidgets.so*
%_libdir/libkexiformutils.so*
%_libdir/libkexiguiutils.so*
%_libdir/libkeximain.so*
%_libdir/libkeximigrate.so*
%_libdir/libkexirelationsview.so*
%_libdir/libkexisql2.so*
%_libdir/libkexisql3.so*
%_libdir/libkformdesigner.so*
%_Kmenudir/kexi.desktop
%_datadir/apps/kexi/
%config %_Kconfig/kexirc
%config %_Kconfig/magic/kexi.magic
%_iconsdir/*/*/mimetypes/kexiproject_*.*
%_iconsdir/*/*/apps/kexi.*
%_Kmimelnk/application/x-kexiproject-*.desktop
%_Kmimelnk/application/x-kexi-connectiondata.desktop
%_Kservices/kexidb_*.desktop
%_Kservices/kexi/
%_Kservices/keximigrate_*.desktop
%_Kservices/kformdesigner/
%_Kservicetypes/kexidb_driver.desktop
%_Kservicetypes/kexihandler.desktop
%_Kservicetypes/keximigration_driver.desktop
%_Kservicetypes/widgetfactory.desktop

%files karbon
%_datadir/apps/konqueror/servicemenus/karbon_konqi.desktop
%_datadir/templates/Illustration.desktop
%_datadir/templates/.source/Illustration.karbon
#
%_Klibdir/libkarbon*import.so*
%_Klibdir/libkarbon*export.so*
%_Klibdir/liboodrawimport.so*
%_Klibdir/libwmfexport.so*
%_Klibdir/libwmfimport.so*
%_Kservices/karbon_*_import.desktop
%_Kservices/karbon_*_export.desktop
#
%doc %_docdir/HTML/en/karbon
%_bindir/karbon
%_Klibdir/karbon_*.so*
%_Klibdir/karbon.so*
%_Klibdir/libkarbonpart.so*
%_libdir/libkarboncommon.so*
%_libdir/libkdeinit_karbon.so*
%_Kmenudir/karbon.desktop
%_Kapps/karbon/
%_iconsdir/*/*/apps/karbon.*
%_Kservices/karbondefaulttools.desktop
%_Kservices/karbonimagetool.desktop
%_Kservices/karbonpart.desktop
%_Kservices/karbonzoomtool.desktop
%_Kservicetypes/karbon_module.desktop


%files kchart
%doc %_docdir/HTML/en/kchart
%_Kapps/konqueror/servicemenus/kchart_konqi.desktop
%_Klibdir/libkchart*export.so*
%_datadir/services/kchart_*_export.desktop
#
%_bindir/kchart
%_Klibdir/kchart.so*
%_Klibdir/libkchartpart.so*
%_libdir/libkdeinit_kchart.so*
%_Kmenudir/kchart.desktop
%_Kapps/kchart
%_iconsdir/*/*/apps/kchart.png
%_Kservices/kchartpart.desktop


%files chalk
%_datadir/apps/konqueror/servicemenus/chalk_konqi.desktop
#
%_Klibdir/libchalk*export.so*
%_Klibdir/libchalk*import.so*
%_Klibdir/chalkselectopaque.so*
%_Kapplnk/.hidden/chalk_magick.desktop
%_Kapplnk/.hidden/chalk_jpeg.desktop
%_Kapplnk/.hidden/chalk_openexr.desktop
%_Kapplnk/.hidden/chalk_png.desktop
%_Kapplnk/.hidden/chalk_raw.desktop
%_Kapplnk/.hidden/chalk_tiff.desktop
%_Kapplnk/.hidden/chalk_pdf.desktop
%_Kservices/chalk_*_export.desktop
%_Kservices/chalk_*_import.desktop
%_Kservices/chalkselectopaque.desktop
#
%doc %_docdir/HTML/en/chalk
%_bindir/chalk
%_Klibdir/chalkbumpmap.so*
%_Klibdir/chalkcimg.so*
%_Klibdir/chalkcmykplugin.so*
%_Klibdir/chalkcolorrange.so*
%_Klibdir/chalkcolorsfilters.so*
%_Klibdir/chalkcolorspaceconversion.so*
%_Klibdir/chalkconvolutionfilters.so*
%_Klibdir/chalkdefaultpaintops.so*
%_Klibdir/chalkdefaulttools.so*
%_Klibdir/chalkdropshadow.so*
%_Klibdir/chalkembossfilter.so*
%_Klibdir/chalkexample.so*
%_Klibdir/chalkfiltersgallery.so*
%_Klibdir/chalkgrayplugin.so*
%_Klibdir/chalkhistogramdocker.so*
%_Klibdir/chalkhistogram.so*
%_Klibdir/chalkimageenhancement.so*
%_Klibdir/chalkimagesize.so*
%_Klibdir/chalk_*_plugin.so*
%_Klibdir/chalkoilpaintfilter.so*
%_Klibdir/chalkpixelizefilter.so*
%_Klibdir/chalkraindropsfilter.so*
%_Klibdir/chalkrgbplugin.so*
%_Klibdir/chalkrotateimage.so*
%_Klibdir/chalkroundcornersfilter.so*
%_Klibdir/chalkscreenshot.so*
%_Klibdir/chalkscripting.so*
%_Klibdir/chalkselectiontools.so*
%_Klibdir/chalkseparatechannels.so*
%_Klibdir/chalkshearimage.so*
%_Klibdir/chalksmalltilesfilter.so*
#%_Klibdir/chalksmearybrush.so*
%_Klibdir/chalk.so*
%_Klibdir/chalksobelfilter.so*
%_Klibdir/chalktoolcrop.so*
%_Klibdir/chalktoolfilter.so*
%_Klibdir/chalktoolpolygon.so*
%_Klibdir/chalktoolpolyline.so*
%_Klibdir/chalktoolselectsimilar.so*
%_Klibdir/chalktoolstar.so*
%_Klibdir/chalktooltransform.so*
%_Klibdir/chalkwetplugin.so*
%_Klibdir/krosschalkcore.so*
%_Klibdir/libchalkpart.so*
%_Klibdir/chalkcolorify.so*
%_Klibdir/chalklevelfilter.so*
%_Klibdir/chalkblurfilter.so*
%_Klibdir/chalkextensioncolorsfilters.so*
%_Klibdir/chalkfastcolortransfer.so*
%_Klibdir/chalklenscorrectionfilter.so*
%_Klibdir/chalkmodifyselection.so*
%_Klibdir/chalknoisefilter.so*
%_Klibdir/chalkrandompickfilter.so*
%_Klibdir/chalksubstrate.so*
%_Klibdir/chalktoolcurves.so*
%_Klibdir/chalktoolperspectivegrid.so*
%_Klibdir/chalktoolperspectivetransform.so*
%_Klibdir/chalkunsharpfilter.so*
%_Klibdir/chalkwavefilter.so*
%_libdir/libkdeinit_chalk.so*
%_libdir/libchalkcolor.so*
%_libdir/libchalkcommon.so*
%_libdir/libchalkgrayscale.so*
%_libdir/libchalk_*.so*
%_libdir/libchalkimage.so*
%_libdir/libchalkrgb.so*
%_libdir/libchalkscripting.so*
%_libdir/libchalkui.so*
%_Kmenudir/chalk.desktop
%_Kapps/chalk/
%_Kapps/chalkplugins/
%_iconsdir/*/*/apps/chalk.*
%_Kservices/chalkbumpmapfilter.desktop
%_Kservices/chalkcimg.desktop
%_Kservices/chalkcmykplugin.desktop
%_Kservices/chalk_*_plugin.desktop
%_Kservices/chalkcolorrange.desktop
%_Kservices/chalkcolorsfilter.desktop
%_Kservices/chalkcolorifyfilter.desktop
%_Kservices/chalkcolorspaceconversion.desktop
%_Kservices/chalkconvolutionfilters.desktop
%_Kservices/chalkdefaultpaintops.desktop
%_Kservices/chalkdefaulttools.desktop
%_Kservices/chalkdropshadow.desktop
%_Kservices/chalkembossfilter.desktop
%_Kservices/chalkexample.desktop
%_Kservices/chalkfiltersgallery.desktop
%_Kservices/chalkgrayplugin.desktop
%_Kservices/chalkhistogram.desktop
%_Kservices/chalkhistogramdocker.desktop
%_Kservices/chalkimageenhancement.desktop
%_Kservices/chalkimagesize.desktop
%_Kservices/chalkoilpaintfilter.desktop
%_Kservices/chalklevelfilter.desktop
%_Kservices/chalkpart.desktop
#%_Klibdir/chalkperftest.so*
#%_Kservices/chalkperftest.desktop
%_Kservices/chalkpixelizefilter.desktop
%_Kservices/chalkraindropsfilter.desktop
%_Kservices/chalkrgbplugin.desktop
%_Kservices/chalkrotateimage.desktop
%_Kservices/chalkroundcornersfilter.desktop
%_Kservices/chalkscreenshot.desktop
%_Kservices/chalkscripting.desktop
%_Kservices/chalkselectiontools.desktop
%_Kservices/chalkseparatechannels.desktop
%_Kservices/chalkshearimage.desktop
%_Kservices/chalksmalltilesfilter.desktop
#%_Kservices/chalksmearybrush.desktop
%_Kservices/chalksobelfilter.desktop
%_Kservices/chalktoolcrop.desktop
%_Kservices/chalktoolfilter.desktop
%_Kservices/chalktoolpolygon.desktop
%_Kservices/chalktoolpolyline.desktop
%_Kservices/chalktoolselectsimilar.desktop
%_Kservices/chalktoolstar.desktop
%_Kservices/chalktooltransform.desktop
%_Kservices/chalkwetplugin.desktop
%_Kservices/chalkblurfilter.desktop
%_Kservices/chalkextensioncolorsfilters.desktop
%_Kservices/chalkfastcolortransfer.desktop
%_Kservices/chalklenscorrectionfilter.desktop
%_Kservices/chalkmodifyselection.desktop
%_Kservices/chalknoisefilter.desktop
%_Kservices/chalkrandompickfilter.desktop
%_Kservices/chalksubstrate.desktop
%_Kservices/chalktoolcurves.desktop
%_Kservices/chalktoolperspectivegrid.desktop
%_Kservices/chalktoolperspectivetransform.desktop
%_Kservices/chalkunsharpfilter.desktop
%_Kservices/chalkwavefilter.desktop
%_Kservicetypes/chalk_*.desktop



%files kformula
%_datadir/apps/konqueror/servicemenus/kformula_konqi.desktop
%_Klibdir/libkfolatexexport.so*
%_Klibdir/libkfomathmlexport.so*
%_Klibdir/libkfomathmlimport.so*
%_Klibdir/libkfopngexport.so*
%_Klibdir/libkfosvgexport.so*
%_datadir/services/kformula_*_import.desktop
%_datadir/services/kformula_*_export.desktop
#
%doc %_docdir/HTML/en/kformula
%_bindir/kformula
%_Klibdir/kformula.so*
%_Klibdir/libkformulapart.so*
%_libdir/libkdeinit_kformula.so*
%_Kmenudir/kformula.desktop
%_Kapps/kformula/
%_iconsdir/*/*/apps/kformula.png
%_Kservices/kformulapart.desktop



%files kpresenter
%_datadir/apps/konqueror/servicemenus/kpresenter_konqi.desktop
%_datadir/templates/.source/Presentation.kpt
%_datadir/templates/Presentation.desktop
#
%_Klibdir/libkpresenterbmpexport.so*
%_Klibdir/libkpresenterjpegexport.so*
%_Klibdir/libkpresentermngexport.so*
%_Klibdir/libkpresenterpngexport.so*
%_Klibdir/libkpresentersvgexport.so*
%_Klibdir/libkpresenterxbmexport.so*
%_Klibdir/libkpresenterxpmexport.so*
%_Klibdir/libkprkword.so*
%_Klibdir/libooimpressexport.so*
%_Klibdir/libooimpressimport.so*
%_Klibdir/libpowerpointimport.so*
%_libdir/libkpresenterimageexport.so*
%_Kservices/kpresenter_*_export.desktop
%_Kservices/kpresenter_*_import.desktop
%_Kservices/kprkword.desktop
#
%doc %_docdir/HTML/en/kpresenter
%_bindir/kpresenter
%_bindir/kprconverter.pl
%_Klibdir/kpresenter.so*
%_Klibdir/libkpresenterpart.so*
%_libdir/libkdeinit_kpresenter.so*
%_libdir/libkpresenterprivate.so*
%_Kapps/kpresenter/
%_Kmenudir/kpresenter.desktop
%_iconsdir/*/*/apps/kpresenter.png
%_Kservices/kpresenterpart.desktop


%files kspread
%_Kapps/konqueror/servicemenus/kspread_konqi.desktop
%_datadir/templates/SpreadSheet.desktop
%_datadir/templates/.source/SpreadSheet.kst
#
%_datadir/services/kspread_*_import.desktop
%_datadir/services/kspread_*_export.desktop
%_Klibdir/libcsvexport.so*
%_Klibdir/libcsvimport.so*
%_Klibdir/libapplixspreadimport.so
%_Klibdir/libdbaseimport.so
%_Klibdir/libexcelimport.so*
%_Klibdir/libgnumericexport.so*
%_Klibdir/libgnumericimport.so*
%_Klibdir/libkspread*export.so*
%_Klibdir/libopencalcexport.so*
%_Klibdir/libopencalcimport.so*
%_Klibdir/libqproimport.so*
%_Klibdir/krosskspreadcore.so*
%_Klibdir/kspreadscripting.so*
%_Klibdir/libkspreadkexiimport.so*
#
%doc %_docdir/HTML/en/kspread
%_bindir/kspread
%_libdir/libkdeinit_kspread.so*
%_Klibdir/libkspreadinsertcalendar.so*
%_Klibdir/libkspreadpart.so*
%_Klibdir/kspread.so*
%_Kmenudir/kspread.desktop
%_datadir/apps/kspread/
%_iconsdir/*/*/apps/kspread.png
%_Kservices/kspreadpart.desktop
%_Kservices/kspreadscripting.desktop


%files kugar
%_Klibdir/libkugarnopimport.so*
%_Kservices/kugar_kugar_import.desktop
#
%doc %_docdir/HTML/en/kugar
%_bindir/kugar
%_bindir/kudesigner
%_Klibdir/kugar.so*
%_Klibdir/kudesigner.so*
%_Klibdir/libkudesignerpart.so*
%_Klibdir/libkugarpart.so*
%_libdir/libkdeinit_kugar.so*
%_libdir/libkdeinit_kudesigner.so*
%_libdir/libkudesignercore.so*
%_libdir/libkugarlib.so*
%_Kmenudir/kugar.desktop
%_Kmenudir/kudesigner.desktop
%_Kapps/kudesigner/
%_Kapps/kugar
%_iconsdir/*/*/apps/kugar.png
%_iconsdir/*/*/apps/kudesigner.png
%_iconsdir/*/*/mimetypes/kugardata.png
%_Kservices/kugarpart.desktop


%files kword
%_Kapps/konqueror/servicemenus/kword_*.desktop
%_datadir/templates/.source/TextDocument.kwt
%_datadir/templates/TextDocument.desktop
#
%_libdir/libkwordexportfilters.so*
%_Klibdir/libabiwordexport.so*
%_Klibdir/libabiwordimport.so*
%_Klibdir/libamiproexport.so*
%_Klibdir/libamiproimport.so*
%_Klibdir/libapplixwordimport.so*
%_Klibdir/libasciiexport.so*
%_Klibdir/libasciiimport.so*
%_Klibdir/libdocbookexport.so*
%_Klibdir/libhancomwordimport.so*
%_Klibdir/libhtmlexport.so*
%_Klibdir/libhtmlimport.so*
%_Klibdir/libkwordkword1dot3import.so*
%_Klibdir/libkwordlatexexport.so*
%_Klibdir/libmswordimport.so*
%_Klibdir/libmswriteexport.so*
%_Klibdir/libmswriteimport.so*
%_Klibdir/liboowriterexport.so*
%_Klibdir/liboowriterimport.so*
%_Klibdir/libpalmdocexport.so*
%_Klibdir/libpalmdocimport.so*
%_Klibdir/libpdfimport.so*
%_Klibdir/librtfexport.so*
%_Klibdir/librtfimport.so*
%_Klibdir/libwmlexport.so*
%_Klibdir/libwmlimport.so*
%_Klibdir/libwpexport.so*
%_Klibdir/libwpimport.so*
%_Kservices/kword_*_export.desktop
%_Kservices/kword_*_import.desktop
#
%doc %_docdir/HTML/en/kword
%_bindir/kword
%_Klibdir/kwmailmerge_*.so*
%_Klibdir/kword.so*
%_Klibdir/libkwordpart.so*
%_libdir/libkdeinit_kword.so*
%_libdir/libkwmailmerge_interface.so*
%_libdir/libkwordprivate.so*
%_Kapps/kword/
%_iconsdir/*/*/apps/kword.png
%_Kmenudir/kword.desktop
%_Kservices/kwmailmerge_*.desktop
%_Kservices/kwordpart.desktop
%_Kservices/kwserialletter_*
%_Kservicetypes/kwmailmerge.desktop


%files kplato
%doc %_docdir/HTML/en/kplato
%_bindir/kplato
%_libdir/libkdeinit_kplato.so*
%_Klibdir/kplato.so*
%_Klibdir/libkplatopart.so*
%_Kapps/kplato/
%_Kservices/kplatopart.desktop
%_iconsdir/*/*/apps/kplato.*
%_Kmenudir/kplato.desktop

%files devel
%doc %_docdir/HTML/en/koffice-apidocs/
%_includedir/*
%if %_keep_libtool_files
%_libdir/*.la
%_Klibdir/*.la
%endif

%endif

%changelog
* Wed Apr 18 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4:1.6.3-alt24
- Fixed build with new automake

* Thu Feb 23 2012 Roman Savochenko <rom_as@altlinux.ru> 4:1.6.3-alt23
- Build for TDE 3.5.13 release

* Mon Nov 28 2011 Sergey V Turchin <zerg@altlinux.org> 4:1.6.3-alt22
- fix compile with qt-3.3.8d
- built without poppler

* Sat Oct 22 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 4:1.6.3-alt21.1
- Rebuild with Python-2.7

* Sun Mar 27 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4:1.6.3-alt21
- Avoid using xorg-devel in BuildRequires

* Fri Mar 18 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4:1.6.3-alt20
- Rebuilt for debuginfo

* Wed Mar 09 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4:1.6.3-alt19
- Built without arts

* Tue Jan 25 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4:1.6.3-alt18
- Fixed build

* Tue Jul 20 2010 Sergey V Turchin <zerg@altlinux.org> 4:1.6.3-alt16.M51.1
- built for M51

* Tue Jul 20 2010 Sergey V Turchin <zerg@altlinux.org> 4:1.6.3-alt17
- fix to build with python-2.5

* Tue Jul 20 2010 Sergey V Turchin <zerg@altlinux.org> 4:1.6.3-alt15.M51.1
- built for M51

* Fri Jun 04 2010 Sergey V Turchin <zerg@altlinux.org> 4:1.6.3-alt16
- don't package kexi

* Sun Jan 17 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4:1.6.3-alt14.2
- Fixed for autoconf 2.6

* Mon Nov 30 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4:1.6.3-alt14.1
- Rebuilt with python 2.6

* Wed Sep 16 2009 Sergey V Turchin <zerg@altlinux.org> 4:1.6.3-alt14
- built only kexi and kivio (ALT#21583)

* Thu May 22 2008 Sergey V Turchin <zerg at altlinux dot org> 4:1.6.3-alt12
- built without GraphicsMagick

* Mon Apr 14 2008 Sergey V Turchin <zerg at altlinux dot org> 4:1.6.3-alt11
- fix ruby requires
- don't package dublicate files

* Fri Feb 15 2008 Sergey V Turchin <zerg at altlinux dot org> 4:1.6.3-alt10
- rebuilt with new python

* Fri Dec 14 2007 Sergey V Turchin <zerg at altlinux dot org> 4:1.6.3-alt9
- fix compile with new ImageMagick

* Mon Nov 12 2007 Sergey V Turchin <zerg at altlinux dot org> 4:1.6.3-alt8
- fix compile with new ImageMagick

* Thu Nov 08 2007 Sergey V Turchin <zerg at altlinux dot org> 4:1.6.3-alt7
- add patch to fix CVE-2007-4352, CVE-2007-5392, CVE-2007-5393

* Wed Oct 10 2007 Sergey V Turchin <zerg at altlinux dot org> 4:1.6.3-alt6
- rebuilt with new poppler

* Mon Oct 08 2007 Sergey V Turchin <zerg at altlinux dot org> 4:1.6.3-alt5
- fix files section to add kritaselectopaque plugin
- rebuilt with new poppler

* Fri Sep 28 2007 Sergey V Turchin <zerg at altlinux dot org> 4:1.6.3-alt4
- fix compile with new ImageMagick

* Tue Sep 25 2007 Sergey V Turchin <zerg at altlinux dot org> 4:1.6.3-alt3
- add fix for CVE-2007-3387

* Thu Jun 14 2007 Sergey V Turchin <zerg at altlinux dot org> 4:1.6.3-alt2
- fix files section to resolve subpackages requires; thanks shrek@alt

* Fri Jun 08 2007 Sergey V Turchin <zerg at altlinux dot org> 4:1.6.3-alt1
- new version

* Wed May 30 2007 Sergey V Turchin <zerg at altlinux dot org> 4:1.6.2-alt3
- rebuilt with new config files placement macros

* Thu Mar 29 2007 Sergey V Turchin <zerg at altlinux dot org> 4:1.6.2-alt2
- rebuilt with new libpqxx

* Mon Feb 26 2007 Sergey V Turchin <zerg at altlinux dot org> 4:1.6.2-alt1
- new version

* Mon Jan 15 2007 Sergey V Turchin <zerg at altlinux dot org> 4:1.6.1-alt1
- new version

* Wed Oct 18 2006 Sergey V Turchin <zerg at altlinux dot org> 4:1.6.0-alt1
- new version

* Mon Jul 17 2006 Sergey V Turchin <zerg at altlinux dot org> 4:1.5.2-alt1
- new version

* Thu Jul 06 2006 Sergey V Turchin <zerg at altlinux dot org> 4:1.5.1-alt2
- rebuilt with new libpqxx

* Tue May 23 2006 Sergey V Turchin <zerg at altlinux dot org> 4:1.5.1-alt1
- new version

* Fri Apr 14 2006 Sergey V Turchin <zerg at altlinux dot org> 4:1.5.0-alt2
- built with PostgreSQL support in Kexi

* Thu Apr 13 2006 Sergey V Turchin <zerg at altlinux dot org> 4:1.5.0-alt1
- 1.5 release

* Mon Apr 10 2006 Sergey V Turchin <zerg at altlinux dot org> 4:1.5.0-alt0.1.rc1
- RC1

* Wed Feb 01 2006 Sergey V Turchin <zerg at altlinux dot org> 4:1.4.2-alt4
- fix build requires

* Fri Jan 27 2006 Sergey V Turchin <zerg at altlinux dot org> 4:1.4.2-alt3
- fix build on x86_64

* Tue Jan 10 2006 Sergey V Turchin <zerg at altlinux dot org> 4:1.4.2-alt2
- add patch for pdf import

* Mon Oct 17 2005 Sergey V Turchin <zerg at altlinux dot org> 4:1.4.2-alt1
- new version

* Tue Oct 11 2005 Sergey V Turchin <zerg at altlinux dot org> 4:1.4.1-alt4
- add patch for rtf filter

* Thu Sep 15 2005 Sergey V Turchin <zerg at altlinux dot org> 4:1.4.1-alt3
- rebuilt with new ImageMagik

* Tue Sep 13 2005 Sergey V Turchin <zerg at altlinux dot org> 4:1.4.1-alt2
- rebuilt with new ImageMagik

* Fri Aug 12 2005 Sergey V Turchin <zerg at altlinux dot org> 4:1.4.1-alt1
- new version

* Fri Jul 01 2005 Sergey V Turchin <zerg at altlinux dot org> 4:1.4.0a-alt1
- new version

* Thu Jun 09 2005 Sergey V Turchin <zerg at altlinux dot org> 4:1.3.98-alt1
- new version

* Thu Mar 17 2005 Sergey V Turchin <zerg at altlinux dot org> 4:1.3.5-alt3
- rebuild with new python

* Mon Jan 24 2005 Sergey V Turchin <zerg at altlinux dot org> 4:1.3.5-alt2
- add patch for xpdf filter

* Tue Jan 11 2005 Sergey V Turchin <zerg at altlinux dot org> 4:1.3.5-alt1
- new version

* Mon Oct 11 2004 Sergey V Turchin <zerg at altlinux dot org> 4:1.3.3-alt1
- new version

* Thu Jul 08 2004 Sergey V Turchin <zerg at altlinux dot org> 4:1.3.2-alt1
- new version

* Fri Jun 18 2004 Sergey V Turchin <zerg at altlinux dot org> 4:1.3.1-alt2
- fix "rebuild failed"
- fix menu

* Thu May 06 2004 Sergey V Turchin <zerg at altlinux dot org> 4:1.3.1-alt1
- new version

* Thu Mar 18 2004 Sergey V Turchin <zerg at altlinux dot org> 4:1.3.0-alt2
- fix starting via customized menu

* Thu Mar 18 2004 Sergey V Turchin <zerg at altlinux dot org> 4:1.3.0-alt1
- release

* Fri Dec 05 2003 Sergey V Turchin <zerg at altlinux dot org> 4:1.3.0-alt0.3.rc1
- remove *.la files from package
- rebuild with new ImageMagic
- update wv2 to 0.2.1

* Tue Nov 04 2003 Sergey V Turchin <zerg at altlinux dot org> 4:1.3.0-alt0.2.rc1
- 1.3-rc1

* Thu Oct 02 2003 Sergey V Turchin <zerg at altlinux dot org> 4:1.3.0-alt0.1.beta4
- 1.3-beta4

* Wed Aug 27 2003 Sergey V Turchin <zerg at altlinux dot org> 4:1.3.0-alt0.1.beta3
- 1.3-beta3

* Fri Jun 20 2003 Sergey V Turchin <zerg at altlinux dot org> 4:1.3.0-alt0.1.cvs
- update from cvs

* Tue May 06 2003 Sergey V Turchin <zerg at altlinux dot ru> 4:1.3.0-alt0.0.2.beta1
- 1.3-beta1 test build

* Mon Mar 17 2003 Sergey V Turchin <zerg@altlinux.ru> 4:1.2.1-alt5
- update code from cvs KOFFICE_1_2_BRANCH
- split

* Wed Feb 12 2003 Sergey V Turchin <zerg@altlinux.ru> 4:1.2.1-alt4
- update code from cvs KOFFICE_1_2_BRANCH

* Wed Jan 22 2003 Sergey V Turchin <zerg@altlinux.ru> 4:1.2.1-alt3
- exclude %_datadir/services/otherofficethumbnail.desktop

* Mon Jan 13 2003 Sergey V Turchin <zerg@altlinux.ru> 4:1.2.1-alt2
- update from cvs

* Mon Dec 16 2002 Sergey V Turchin <zerg@altlinux.ru> 4:1.2.1-alt1
- new version

* Fri Nov 29 2002 Sergey V Turchin <zerg@altlinux.ru> 4:1.2-alt5
- update from cvs

* Mon Nov 04 2002 Sergey V Turchin <zerg@altlinux.ru> 4:1.2-alt4
- update from cvs
- fix requires

* Wed Sep 11 2002 Sergey V Turchin <zerg@altlinux.ru> 4:1.2-alt3
- final
- build wit gcc3.2 && objprelink

* Tue Aug 20 2002 Sergey V Turchin <zerg@altlinux.ru> 4:1.2-alt2
- update from cvs

* Fri Aug 09 2002 Sergey V Turchin <zerg@altlinux.ru> 4:1.2-alt1.rc1
- new version

* Thu Apr 25 2002 Sergey V Turchin <zerg@altlinux.ru> 4:1.1.1-alt5
- rebuild with KDE3

* Mon Mar 18 2002 Sergey V Turchin <zerg@altlinux.ru> 4:1.1.1-alt4
- sync with cooker (memleak patches)

* Tue Jan 22 2002 Sergey V Turchin <zerg@altlinux.ru> 4:1.1.1-alt3
- rebuild without fam

* Tue Jan 15 2002 Sergey V Turchin <zerg@altlinux.ru> 4:1.1.1-alt2
- sync with coocker (update cvs branch)

* Tue Oct 30 2001 Sergey V Turchin <zerg@altlinux.ru> 4:1.1-alt8
- fix buildrequires

* Fri Oct 12 2001 AEN <aen@logic.ru> 1.1-alt7
- rebuilt with libpng.so.3

* Thu Aug 30 2001 Sergey V Turchin <zerg@altlinux.ru> 1.1-alt6
- release 1.1

* Tue Aug 28 2001 Konstantin Volckov <goldhead@altlinux.ru> 1.1-alt5
- Fixed dependencies

* Fri Aug 24 2001 Konstantin Volckov <goldhead@altlinux.ru> 1.1-alt4
- Fixed .la files

* Fri Aug 24 2001 Konstantin Volckov <goldhead@altlinux.ru> 1.1-alt3
- Some spec cleanup
- Fixed filelists

* Fri Aug 23 2001 Rider <rider@altlinux.ru> 1.1-alt2
= koshell open file patch

* Tue Aug 21 2001 Rider <rider@altlinux.ru> 1.1-alt1
- latest CVS (1.1 final)

* Mon Jul 30 2001 Sergey V Turchin <zerg@altlinux.ru> 1.1-alt0.rc1.2
- build RC1 for ALT

* Sat Jul 21 2001 Laurent MONTEL <lmontel@mandrakesoft.com> 1.1-0.rc1.2mdk
- Fix doc for Mandrake 8.1 (patch0)

* Sat Jul 21 2001 Laurent MONTEL <lmontel@mandrakesoft.com> 1.1-0.rc1.1mdk
- koffice 1.1 RC1

* Thu Jul 05 2001 Laurent MONTEL <lmontel@mandrakesoft.com> 1.1-0.beta3.4mdk
- Rebuild with kde2.2beta1

* Wed Jun 27 2001 Laurent MONTEL <lmontel@mandrakesoft.com> 1.1-0.beta3.3mdk
- Fix crash in killustrator and kword

* Mon Jun 25 2001 David BAUDENS <baudens@mandrakesoft.com> 1.1-0.beta3.2mdk
- Build for Cooker
- Add missing PreReq
- Move koshell in Office/Accessories (Frederic CROZAT)

* Mon Jun 18 2001 David BAUDENS <baudens@mandrakesoft.com> 1.1-0.beta3.1mdk
- 1.1.beta3
- Begin to add tests to automatically build right package for right distribution
- Fix and adapt LMDK menu structure for each supported LDMK distributions
- Complete BuildRequires for each supported LMDK distributions
- Make Munu structure generation readable (i.e. respect alphabetic order)
- Fix Obsoletes (i.e. learn to a package to don't obsole itself)
- Enable debug and don't strip when we are not in final release
- Enable xinerama for 8.1 distribution (currently Cooker)
- Disable --enable-final at present time (currently broken)
- Disable --enable-debug for LMDK 8.0 (buggy GCC)
- Move static libraries in devel package

* Wed Jun 13 2001 Frederic Crozat <fcrozat@mandrakesoft.com> 1.1-0.beta2.3mdk
- New Office menu structure

* Thu May 24 2001 David BAUDENS <baudens@mandrakesoft.com> 1.1-0.beta2.2mdk
- Re-enable debug (low level)
- Fix CFLAGS and CXXFLAGS
- Fix Menu structure

* Thu May 17 2001 Laurent MONTEL <lmontel@mandrakesoft.com> 1.1-0.beta2.1mdk
- koffice1.1beta2

* Fri Apr 20 2001 Laurent MONTEL <lmontel@mandrakesoft.cpm> 1.1-0.beta1.1mdk
- koffice1.1beta1
- Increase Epoch because now name of this package is koffice1.1 and no longer
  koffice2.0

* Wed Apr 11 2001 Laurent MONTEL <lmontel@mandrakesoft.com> 2.1-7mdk
- Update code
- port to new kde menu entry

* Mon Apr 09 2001 Laurent MONTEL <lmontel@mandrakesoft.com> 2.1-6mdk
- Update code

* Tue Mar 27 2001 Laurent MONTEL <lmontel@mandrakesoft.com> 2.1-5mdk
- Add missing files

* Mon Mar 26 2001 Laurent MONTEL <lmontel@mandrakesoft.com> 2.1-4mdk
- Update code + add kugar

* Sat Mar 17 2001 Laurent MONTEL <lmontel@mandrakesoft.com> 2.1-3mdk
- Update code

* Thu Mar 08 2001 laurent MONTEL <lmontel@mandrakesoft.com> 2.1-2mdk
- New kword version

* Thu Mar 08 2001 Laurent MONTEL <lmontel@mandrakesoft.com> 2.1-1mdk
- First package of new Koffice

