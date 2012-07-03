
%add_findreq_skiplist %_K4apps/*/scripts/*/*.py
%add_findreq_skiplist %_K4apps/*/scripts/*/*.rb

%def_disable kivio
%def_enable kformula
%def_enable kexi
%def_enable python
%def_disable apidox
%def_disable wpg

%define flake_major 8

Name: koffice
Version: 2.3.3
Release: alt11
Serial: 4

Group: Office
Summary: Set of office applications for KDE
Url: http://www.koffice.org/
License: GPL

Requires: %name-okular-odp = %serial:%version-%release
Requires: %name-kword = %serial:%version-%release
Requires: %name-kplato = %serial:%version-%release
Requires: %name-kspread = %serial:%version-%release
Requires: %name-kpresenter = %serial:%version-%release
%if_enabled kformula
Requires: %name-kformula = %serial:%version-%release
%endif
%if_enabled kivio
Requires: %name-kivio = %serial:%version-%release
%endif
Requires: %name-kchart = %serial:%version-%release
Requires: %name-krita = %serial:%version-%release
Requires: %name-karbon = %serial:%version-%release
%if_enabled kexi
Requires: %name-kexi = %serial:%version-%release
%endif
#Requires: %name-kugar = %serial:%version-%release


Source: %name-%version.tar
Source1: FindOkular.cmake
Patch1: koffice-2.1.0-alt-find-gm.patch
Patch2: koffice-2.3.1-alt-fix-linking.patch
Patch3: koffice-2.3.3-alt-fix-compile.patch
Patch4: koffice-2.3.3-alt-glib2.32.patch

# Automatically added by buildreq on Mon Nov 17 2008 (-bi)
#BuildRequires: eigen2 gcc-c++ getfemxx kde4base-runtime kde4graphics-devel kde4pimlibs-devel koffice-devel libGraphicsMagick-devel libXScrnSaver-devel libXcomposite-devel libXft-devel libXpm-devel libXt-devel libXtst-devel libXv-devel libXxf86misc-devel libbfd-devel libexiv2-devel libglew-devel libgsl-devel libjpeg-devel liblcms-devel libldap-devel libpoppler-qt4-devel libqca2-devel libqimageblitz-devel libwpg-devel libwv2-devel libxkbfile-devel libxslt-devel nvidia_glx_177.80 openexr-devel pstoedit rpm-build-ruby xorg-xf86vidmodeproto-devel xsltproc
BuildRequires(pre): kde4libs-devel
BuildRequires: gcc-c++ libxml2-devel libfftw3-devel libgomp-devel glib2-devel libgsf-devel
BuildRequires: eigen2 getfemxx libqtgtl-devel libdcmtk-devel liblcms2-devel create-resources
BuildRequires: kde4base-runtime-devel >= 4.1 kde4graphics-devel >= 4.1 kde4pimlibs-devel >= 4.1
BuildRequires: libGraphicsMagick-devel rpm-build-ruby rpm-build-python
BuildRequires: libbfd-devel libexiv2-devel libglew-devel libgsl-devel libjpeg-devel libldap-devel libpoppler-qt4-devel
BuildRequires: libqca2-devel libqimageblitz-devel libwv2-devel >= 0.4.2 libxslt-devel
%if_enabled wpg
BuildRequires: libwpg2-devel
%endif
BuildRequires: openexr-devel pstoedit libpstoedit-devel xsltproc
BuildRequires: libMySQL-devel libsqlite3-devel libxbase-devel libfreetds-devel libopenjpeg-devel
%if_enabled apidox
BuildRequires: doxygen, graphviz
%endif

%description
Office applications for the K Desktop Environment.

KOffice contains:
   * KWord: word processor
   * KSpread: spreadsheet
   * KPresenter: presentations
   * KChart: diagram generator
   * Kugar: A tool for generating business quality reports.
   * Kivio: A Visio(r)-style flowcharting application.
   * Kexi: an integrated environment for managing data
   * Some filters (Excel 97, Winword 97/2000, etc.)
   * karbon: the scalable vector drawing application for KDE.
   * kformula:  a formula editor for KOffice.
   * krita: painting and image editing application.
   * koshell
   * kplato: a project management.

%package common
Summary: %name common package
Group: System/Configuration/Other
Requires: kde-common >= 4.1
%description common
%name common package

%package core
Summary: %name core files
Group: System/Configuration/Other
Requires: %name-common = %serial:%version-%release
Requires: wordnet create-resources
Requires: kde4libs >= %{get_version kde4libs}
Requires: kde4base-runtime
Provides: koffice-libs = %version-%release
Obsoletes: koffice-libs < %version-%release
%description core
%name  core files

%package -n libkoguiutils
Summary: Koffice 2 core library
Group: System/Libraries
Requires: %name-common = %serial:%version-%release
%description -n libkoguiutils
Koffice2 core library

%package -n libkoaction
Summary: Koffice 2 core library
Group: System/Libraries
Requires: %name-common = %serial:%version-%release
%description -n libkoaction
Koffice2 core library

%package -n libkobase
Summary: Koffice 2 core library
Group: System/Libraries
Requires: %name-common = %serial:%version-%release
%description -n libkobase
Koffice2 core library

%package -n libkocolorwidgets
Summary: Koffice 2 core library
Group: System/Libraries
Requires: %name-common = %serial:%version-%release
%description -n libkocolorwidgets
Koffice2 core library

%package -n libkoplugin
Summary: Koffice 2 core library
Group: System/Libraries
Requires: %name-common = %serial:%version-%release
%description -n libkoplugin
Koffice2 core library

%package -n libkowidgets
Summary: Koffice 2 core library
Group: System/Libraries
Requires: %name-common = %serial:%version-%release
%description -n libkowidgets
Koffice2 core library

%package -n libkokross
Summary: Koffice 2 core library
Group: System/Libraries
Requires: %name-common = %serial:%version-%release
%description -n libkokross
Koffice2 core library

%package -n libkomain
Summary: Koffice 2 core library
Group: System/Libraries
Requires: %name-common = %serial:%version-%release
%description -n libkomain
Koffice2 core library

%package -n libkopageapp
Summary: Koffice 2 core library
Group: System/Libraries
Requires: %name-common = %serial:%version-%release
%description -n libkopageapp
Koffice2 core library

%package -n libkoresources
Summary: Koffice 2 core library
Group: System/Libraries
Requires: %name-common = %serial:%version-%release
%description -n libkoresources
Koffice2 core library

%package -n libkotext
Summary: Koffice 2 core library
Group: System/Libraries
Requires: %name-common = %serial:%version-%release
%description -n libkotext
Koffice2 core library

%package -n libkowmf
Summary: Koffice 2 core library
Group: System/Libraries
Requires: %name-common = %serial:%version-%release
%description -n libkowmf
Koffice2 core library

%package -n libkoodf
Summary: Koffice 2 core library
Group: System/Libraries
Requires: %name-common = %serial:%version-%release
%description -n libkoodf
Koffice2 core library

%package -n libkostore
Summary: Koffice 2 core library
Group: System/Libraries
Requires: %name-common = %serial:%version-%release
%description -n libkostore
Koffice2 core library

%package -n libkwmf
Summary: Koffice 2 core library
Group: System/Libraries
Requires: %name-common = %serial:%version-%release
%description -n libkwmf
Koffice2 core library

%package -n libflake%flake_major
Summary: Koffice 2 core library
Group: System/Libraries
Requires: %name-common = %serial:%version-%release
%description -n libflake%flake_major
Koffice2 core library

%package -n libpigmentcms
Summary: Koffice 2 core library
Group: System/Libraries
Requires: %name-common = %serial:%version-%release
%description -n libpigmentcms
Koffice2 core library

%package -n libkochart
Summary: Koffice 2 core library
Group: System/Libraries
Requires: %name-common = %serial:%version-%release
%description -n libkochart
Koffice2 core library

%package -n libkoffice_graya_u16
Summary: Koffice 2 core library
Group: System/Libraries
Requires: %name-common = %serial:%version-%release
%description -n libkoffice_graya_u16
Koffice2 core library

%package -n libkofficegrayau8colorspace
Summary: Koffice 2 core library
Group: System/Libraries
Requires: %name-common = %serial:%version-%release
%description -n libkofficegrayau8colorspace
Koffice2 core library

%package devel
Group: Development/KDE and QT
Summary: Header files for developing koffice2 applications
Requires: %name-core = %serial:%version-%release
Conflicts: libflake-devel
%description devel
Header files needed for developing koffice2 applications

%package kword
Summary: Word processor for koffice2
Group: Office
Requires: %name-core = %serial:%version-%release
%description kword
Kword is a word processor for kde project

%package -n libkwordexportfilters
Summary: Koffice 2 core library
Group: System/Libraries
Requires: %name-common = %serial:%version-%release
%description -n libkwordexportfilters
Koffice2 core library

%package -n libkwordprivate
Summary: Koffice 2 core library
Group: System/Libraries
Requires: %name-common = %serial:%version-%release
%description -n libkwordprivate
Koffice2 core library

%package kplato
Summary: A new project management application for koffice2
Group: Office
Requires: %name-core = %serial:%version-%release
%description kplato
A new project management application for koffice2

%package -n libchartshapelib
Summary: Koffice 2 core library
Group: System/Libraries
Requires: %name-common = %serial:%version-%release
%description -n libchartshapelib
Koffice2 core library

%package -n libkplatomodels
Summary: Koffice 2 core library
Group: System/Libraries
Requires: %name-common = %serial:%version-%release
%description -n libkplatomodels
Koffice2 core library

%package -n libkplatokernel
Summary: Koffice 2 core library
Group: System/Libraries
Requires: %name-common = %serial:%version-%release
%description -n libkplatokernel
Koffice2 core library

%package -n libkplatoprivate
Summary: Koffice 2 core library
Group: System/Libraries
Requires: %name-common = %serial:%version-%release
%description -n libkplatoprivate
Koffice2 core library

%package -n libkplatoui
Summary: Koffice 2 core library
Group: System/Libraries
Requires: %name-common = %serial:%version-%release
%description -n libkplatoui
Koffice2 core library

%package -n libkplatoworkapp
Summary: Koffice 2 core library
Group: System/Libraries
Requires: %name-common = %serial:%version-%release
%description -n libkplatoworkapp
Koffice2 core library

%package -n libkplatoworkfactory
Summary: Koffice 2 core library
Group: System/Libraries
Requires: %name-common = %serial:%version-%release
%description -n libkplatoworkfactory
Koffice2 core library

%package kspread
Summary: SpreadSheet for koffice2
Group: Office
Requires: %name-core = %serial:%version-%release
%description kspread
KSpread is a spreadsheet for kde project

%package -n libkspreadcommon
Summary: Koffice 2 core library
Group: System/Libraries
Requires: %name-common = %serial:%version-%release
%description -n libkspreadcommon
Koffice2 core library

%package -n libkspreadodf
Summary: Koffice 2 core library
Group: System/Libraries
Requires: %name-common = %serial:%version-%release
%description -n libkspreadodf
Koffice2 core library

%package kpresenter
Summary: Presentation for koffice2
Group: Office
Requires: %name-core = %serial:%version-%release
Requires: xdg-utils
%description kpresenter
KPresenter is a presentation for kde project

%package -n libkpresenterprivate
Summary: Koffice 2 core library
Group: System/Libraries
Requires: %name-common = %serial:%version-%release
%description -n libkpresenterprivate
Koffice2 core library

%package kformula
Summary: Formula for koffice2
Group: Office
Requires: %name-core = %serial:%version-%release
%description kformula
KFormula is a formula for kde project

%package -n libkformulalib
Summary: Koffice 2 core library
Group: System/Libraries
Requires: %name-common = %serial:%version-%release
%description -n libkformulalib
Koffice2 core library

%package -n libkformulaprivate
Summary: Koffice 2 core library
Group: System/Libraries
Requires: %name-common = %serial:%version-%release
%description -n libkformulaprivate
Koffice2 core library

%package koshell
Summary: Koshell for koffice2
Group: Graphical desktop/KDE
Requires: %name-core = %serial:%version-%release
%description koshell
Koshell for kde project

%package kivio
Summary: Diagramme for koffice2
Group: Office
Requires: %name-core = %serial:%version-%release
%description kivio
Kivio is a diagramme for kde project

%package -n libkivioprivate
Summary: Koffice 2 core library
Group: System/Libraries
Requires: %name-common = %serial:%version-%release
%description -n libkivioprivate
Koffice2 core library

%package kchart
Summary: Chart and diagram drawing
Group: Office
Requires: %name-core = %serial:%version-%release
%description kchart
Kchart is a chart and diagram drawing program

%package -n libkdchart
Summary: Koffice 2 core library
Group: System/Libraries
Requires: %name-common = %serial:%version-%release
%description -n libkdchart
Koffice2 core library

%package -n libkchartcommon
Summary: Koffice 2 core library
Group: System/Libraries
Requires: %name-common = %serial:%version-%release
%description -n libkchartcommon
Koffice2 core library

%package -n libkisexiv
Summary: Koffice 2 core library
Group: System/Libraries
Requires: %name-common = %serial:%version-%release
%description -n libkisexiv
Koffice2 core library

%package krita
Summary: A pixel-based image manipulation program
Group: Graphics
Requires: %name-core = %serial:%version-%release
%description krita
Krita is a pixel-based image manipulation program

%package -n libkrita_xyz_u16
Summary: Koffice 2 core library
Group: System/Libraries
Requires: %name-common = %serial:%version-%release
%description -n libkrita_xyz_u16
Koffice2 core library

%package -n libkritaui
Summary: Koffice 2 core library
Group: System/Libraries
Requires: %name-common = %serial:%version-%release
%description -n libkritaui
Koffice2 core library

%package -n libkritarulerassistantcommon
Summary: Koffice 2 core library
Group: System/Libraries
Requires: %name-common = %serial:%version-%release
%description -n libkritarulerassistantcommon
Koffice2 core library

%package -n libkrossmodulekrita
Summary: Koffice 2 core library
Group: System/Libraries
Requires: %name-common = %serial:%version-%release
%description -n libkrossmodulekrita
Koffice2 core library

%package -n libkritagrayscale
Summary: Koffice 2 core library
Group: System/Libraries
Requires: %name-common = %serial:%version-%release
%description -n libkritagrayscale
Koffice2 core library

%package -n libkritaimage
Summary: Koffice 2 core library
Group: System/Libraries
Requires: %name-common = %serial:%version-%release
%description -n libkritaimage
Koffice2 core library

%package -n libkritalibpaintop
Summary: Koffice 2 core library
Group: System/Libraries
Requires: %name-common = %serial:%version-%release
%description -n libkritalibpaintop
Koffice2 core library

%package -n libkritabasicdynamiccoloringprogram
Summary: Koffice 2 core library
Group: System/Libraries
Requires: %name-common = %serial:%version-%release
%description -n libkritabasicdynamiccoloringprogram
Koffice2 core library

%package -n libkritabasicdynamicshapeprogram
Summary: Koffice 2 core library
Group: System/Libraries
Requires: %name-common = %serial:%version-%release
%description -n libkritabasicdynamicshapeprogram
Koffice2 core library

%package -n libkritadynamicbrush
Summary: Koffice 2 core library
Group: System/Libraries
Requires: %name-common = %serial:%version-%release
%description -n libkritadynamicbrush
Koffice2 core library

%package -n libkritalibbrush
Summary: Koffice 2 core library
Group: System/Libraries
Requires: %name-common = %serial:%version-%release
%description -n libkritalibbrush
Koffice2 core library

%package karbon
Summary: Scalable drawing for koffice2
Group: Graphics
Requires: %name-core = %serial:%version-%release
%description karbon
Karbon is a scalable drawing for kde project

%package -n libkarboncommon
Summary: Koffice 2 core library
Group: System/Libraries
Requires: %name-common = %serial:%version-%release
%description -n libkarboncommon
Koffice2 core library

%package -n libkarbonui
Summary: Koffice 2 core library
Group: System/Libraries
Requires: %name-common = %serial:%version-%release
%description -n libkarbonui
Koffice2 core library

%package kexi
Summary: An integrated environment for managing data
Group: Databases
Requires: %name-core = %serial:%version-%release
%description kexi
Karbon is an integrated environment for managing data

%package -n libkexicore
Summary: Koffice 2 core library
Group: System/Libraries
Requires: %name-common = %serial:%version-%release
%description -n libkexicore
Koffice2 core library

%package -n libkexidatatable
Summary: Koffice 2 core library
Group: System/Libraries
Requires: %name-common = %serial:%version-%release
%description -n libkexidatatable
Koffice2 core library

%package -n libkexidb
Summary: Koffice 2 core library
Group: System/Libraries
Requires: %name-common = %serial:%version-%release
%description -n libkexidb
Koffice2 core library

%package -n libkexiextendedwidgets
Summary: Koffice 2 core library
Group: System/Libraries
Requires: %name-common = %serial:%version-%release
%description -n libkexiextendedwidgets
Koffice2 core library

%package -n libkexiformutils
Summary: Koffice 2 core library
Group: System/Libraries
Requires: %name-common = %serial:%version-%release
%description -n libkexiformutils
Koffice2 core library

%package -n libkexiguiutils
Summary: Koffice 2 core library
Group: System/Libraries
Requires: %name-common = %serial:%version-%release
%description -n libkexiguiutils
Koffice2 core library

%package -n libkeximain
Summary: Koffice 2 core library
Group: System/Libraries
Requires: %name-common = %serial:%version-%release
%description -n libkeximain
Koffice2 core library

%package -n libkeximigrate
Summary: Koffice 2 core library
Group: System/Libraries
Requires: %name-common = %serial:%version-%release
%description -n libkeximigrate
Koffice2 core library

%package -n libkexirelationsview
Summary: Koffice 2 core library
Group: System/Libraries
Requires: %name-common = %serial:%version-%release
%description -n libkexirelationsview
Koffice2 core library

%package -n libkformdesigner
Summary: Koffice 2 core library
Group: System/Libraries
Requires: %name-common = %serial:%version-%release
%description -n libkformdesigner
Koffice2 core library

%package -n libkexiutils
Summary: Koffice 2 core library
Group: System/Libraries
Requires: %name-common = %serial:%version-%release
%description -n libkexiutils
Koffice2 core library

%package kugar
Summary: Kugar for koffice2
Group: Office
Requires: %name-core = %serial:%version-%release
%description kugar
Kugar is a template based XML report engine for kde project

%package -n libkoproperty
Summary: Koffice 2 core library
Group: System/Libraries
Requires: %name-common = %serial:%version-%release
%description -n libkoproperty
Koffice2 core library

%package -n libkoreport
Summary: Koffice 2 core library
Group: System/Libraries
Requires: %name-common = %serial:%version-%release
%description -n libkoreport
Koffice2 core library

%package -n libkowv2
Summary: Koffice 2 core library
Group: System/Libraries
Requires: %name-common = %serial:%version-%release
%description -n libkowv2
Koffice2 core library

%package -n libmsooxml
Summary: Koffice 2 core library
Group: System/Libraries
Requires: %name-common = %serial:%version-%release
%description -n libmsooxml
Koffice2 core library

%package okular-odp
Summary: ODP file renderer for Okular
Group: Office
Requires: %name-core = %serial:%version-%release
Requires: kde4graphics-okular
%description okular-odp
ODP file renderer for Okular.

%prep
%setup -q -n %name-%version
cp -ar %SOURCE1 cmake/modules/
#%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1

#find ./ -type f -name CMakeLists.txt | grep -v -e '\./libs/CMakeLists.txt' | \
#while read f
#do
#    sed -i \
#	-e 's|\([{([:space:]]\)flake\([})[:space:]]\)|\1koflake\2|g' \
#	-e 's|^[[:space:]]*flake\([})[:space:]]\)|koflake\1|' \
#	-e 's|\([{([:space:]]\)flake[[:space:]]*$|\1koflake|' \
#	-e 's|^[[:space:]]*flake[[:space:]]*$|koflake|' \
#	$f
#done
#sed -i "s|koflake|flake|" kformula/CMakeLists.txt


%build
%K4cmake \
    -DKDE4_ENABLE_FPIE:BOOL=ON \
    -DBUILD_xbase=FALSE \
    -DFreeTDS_LIBRARIES=-lsybdb
#    -DKDE4_ENABLE_FINAL:BOOL=ON \

%K4make -j1
%if_enabled apidox
%K4make apidox
%endif

%install
%K4install

%if_enabled apidox
make install-apidox DESTDIR=%buildroot/
list=`ls -d */ -1`;
echo $list;
for i in $list ; do
	cd $i;
		if grep '^include .*Doxyfile.am' Makefile.am; then
			echo "installing apidox from $i" ;
			make install-apidox DESTDIR=%buildroot/ ;
		fi
	cd ../;
done;
%endif


%files
%files common
%files core
#%_K4xdg_apps/koffice.desktop
#
%_K4lib/spellcheck.so
%_K4lib/commentshape.so
%_K4lib/karbonsvgimport.so
%if_enabled wpg
%_K4lib/wpgimport.so
%endif
%_K4lib/karbonfiltereffects.so
%_K4lib/icalendarexport.so
%_K4lib/karbonpdfimport.so
%_K4lib/paragraphtool.so
%_K4lib/pluginshape.so
%_K4lib/powerpointimport.so
%_K4lib/kolcmsengine.so
#%_K4lib/vectorshape.so
%_K4lib/videoshape.so
%_K4lib/koreport_*.so
%_K4lib/kodocinfopropspage.so
#
%dir %_K4apps/koffice/
%_K4apps/koffice/autocorrect
%_K4apps/koffice/koffice_shell.rc
%_K4apps/koffice/thesaurus
%_K4apps/koproperty
#
%_K4apps/koffice/icons/
%_K4iconsdir/hicolor/*/mimetypes/*
%_K4iconsdir/hicolor/16x16/actions/black.png
%_K4iconsdir/hicolor/16x16/actions/highlight.png
%_K4iconsdir/hicolor/16x16/actions/pen.png
%_K4iconsdir/oxygen/16x16/actions/object-align-horizontal-center-koffice.png
%_K4iconsdir/oxygen/16x16/actions/object-align-horizontal-left-koffice.png
%_K4iconsdir/oxygen/16x16/actions/object-align-horizontal-right-koffice.png
%_K4iconsdir/oxygen/16x16/actions/object-align-vertical-bottom-koffice.png
%_K4iconsdir/oxygen/16x16/actions/object-align-vertical-bottom-top-koffice.png
%_K4iconsdir/oxygen/16x16/actions/object-align-vertical-center-koffice.png
%_K4iconsdir/oxygen/16x16/actions/object-align-vertical-top-koffice.png
%_K4iconsdir/oxygen/16x16/actions/object-group-koffice.png
%_K4iconsdir/oxygen/16x16/actions/object-order-back-koffice.png
%_K4iconsdir/oxygen/16x16/actions/object-order-front-koffice.png
%_K4iconsdir/oxygen/16x16/actions/object-order-lower-koffice.png
%_K4iconsdir/oxygen/16x16/actions/object-order-raise-koffice.png
%_K4iconsdir/oxygen/16x16/actions/object-ungroup-koffice.png
%_K4iconsdir/oxygen/scalable/actions/shape-choose.svgz
%_K4iconsdir/oxygen/*/actions/table.*
%_K4iconsdir/oxygen/32x32/actions/shape-choose.png
%_K4iconsdir/oxygen/32x32/actions/x-shape-chart.png
%_K4iconsdir/oxygen/32x32/actions/x-shape-connection.png
%_K4iconsdir/oxygen/32x32/actions/x-shape-formula.png
%_K4iconsdir/oxygen/32x32/actions/x-shape-image.png
%_K4iconsdir/oxygen/32x32/actions/x-shape-text.png
#
%_K4srv/ServiceMenus/kchart_konqi.desktop
%_K4apps/musicshape
%_K4srv/autocorrect.desktop
%_K4srv/changecase.desktop
%_K4srv/defaulttools.desktop
%_K4srv/divineproportionshape.desktop
%_K4srv/generic_filter.desktop
#%_K4srv/kformdesigner/kformdesigner_containers.desktop
#%_K4srv/kformdesigner/kformdesigner_stdwidgets.desktop
%_K4srv/kofficedockers.desktop
%_K4srv/kofficethumbnail.desktop
%_K4srv/kounavail.desktop
%_K4srv/musicshape.desktop
%_K4srv/pathshapes.desktop
%_K4srv/pictureshape.desktop
%_K4srv/pluginshape.desktop
%_K4srv/textshape.desktop
%_K4srv/textvariables.desktop
%_K4srv/artistictextshape.desktop
%_K4srv/Filterkpr2odf.desktop
%_K4srv/paragraphtool.desktop
%_K4srv/kopabackgroundtool.desktop
%_K4srv/kolcmsengine.desktop
#%_K4srv/vectorshape.desktop
%_K4srv/videoshape.desktop
%_K4srv/spellcheck.desktop
%_K4srv/commentshape.desktop
%_K4srv/koreport_*.desktop
%_K4srv/kodocinfopropspage.desktop
%_K4srvtyp/koreport_*.desktop
%_K4srvtyp/filtereffect.desktop
%_K4srvtyp/scripteventaction.desktop
%_K4srvtyp/flakedevice.desktop
%_K4srvtyp/pigmentextension.desktop
%_K4srvtyp/flake.desktop
%_K4srvtyp/flakeshape.desktop
%_K4srvtyp/flaketool.desktop
%_K4srvtyp/inlinetextobject.desktop
%_K4srvtyp/kochart.desktop
%_K4srvtyp/kofficedocker.desktop
%_K4srvtyp/kofficepart.desktop
%_K4srvtyp/kofilter.desktop
%_K4srvtyp/kofilterwrapper.desktop
%_K4srvtyp/koplugin.desktop
%_K4srvtyp/texteditingplugin.desktop
%_K4srvtyp/textvariableplugin.desktop
#
%_K4lib/autocorrect.so
%_K4lib/asciiexport.so
%_K4lib/asciiimport.so
%_K4lib/changecase.so
%_K4lib/defaulttools.so
%_K4lib/divineproportionshape.so
%_K4lib/kofficedockers.so
%_K4lib/kofficescan.so
%_K4lib/kofficethumbnail.so
%_K4lib/abiwordexport.so
%_K4lib/musicshape.so
%_K4lib/pathshapes.so
%_K4lib/pictureshape.so
%_K4lib/textshape.so
%_K4lib/textvariables.so
%_K4lib/artistictextshape.so
%_K4lib/Filterkpr2odf.so
%_K4lib/mswordodf_import.so
%_K4lib/kopabackgroundtool.so
#
%_K4bindir/kthesaurus
%_K4xdg_apps/KThesaurus.desktop
%_K4srv/thesaurustool.desktop
%_K4lib/thesaurustool.so
%_K4libdir/libkdeinit4_kthesaurus.so
#
%_K4bindir/koconverter
#%_K4doc/en/kchart
%_K4doc/en/koffice
%_K4doc/en/thesaurus
#%_K4doc/en/koshell
#%_K4xdg_mime/msooxml-all.xml

%files -n libkoplugin
%_K4libdir/libkoplugin.so.*
%files -n libkowidgets
%_K4libdir/libkowidgets.so.*
%files -n libkokross
%_K4libdir/libkokross.so.*
%files -n libkomain
%_K4libdir/libkomain.so.*
%files -n libkopageapp
%_K4libdir/libkopageapp.so.*
%files -n libkotext
%_K4libdir/libkotext.so.*
%files -n libkowmf
%_K4libdir/libkowmf.so.*
%files -n libkoodf
%_K4libdir/libkoodf.so.*
%files -n libkwmf
%_K4libdir/libkwmf.so.*
%files -n libflake%flake_major
%_K4libdir/libflake.so.%{flake_major}*
%files -n libpigmentcms
%_K4libdir/libpigmentcms.so.*
%_K4apps/pigmentcms
%files -n libkochart
%_K4libdir/libkochart.so.*
%files -n libkoproperty
%_K4libdir/libkoproperty.so.*
%files -n libkoreport
%_K4libdir/libkoreport.so.*
%files -n libkowv2
%_K4libdir/libkowv2.so.*
#%files -n libkrossmodulekrita
#%_K4libdir/libkrossmodulekrita.so.*
%files -n libmsooxml
%_K4libdir/libmsooxml.so.*

%files devel
%_K4apps/cmake/modules/*
%_K4includedir/*
%_K4link/*.so

%files okular-odp
%_K4lib/okularGenerator_odp.so
%_K4xdg_apps/okularApplication_odp.desktop
%_K4srv/libokularGenerator_odp.desktop
%_K4srv/okularOdp.desktop

%files kword
%_K4bindir/kword
%_K4iconsdir/*/*/apps/kword.png
%_K4xdg_apps/kword.desktop
%_K4srv/ServiceMenus/kword_konqi.desktop
%_K4apps/kword
%_K4apps/xsltfilter/export/kword/xslfo/*
%_K4conf/kwordrc
%_K4srv/html-odf_export.desktop
%_K4srv/kword_*.desktop
%_K4srv/krossmodulekword.desktop
%_K4srv/kwordpart.desktop
%_K4srv/xslt_export.desktop
%_K4srv/xslt_import.desktop
%_K4lib/dcmimport.so
%_K4lib/htmlodf_export.so
%_K4lib/krossmodulekword.so
%_K4lib/kwordkword1dot3import.so
%_K4lib/kwordpart.so
%_K4lib/abiwordimport.so
%_K4lib/amiproexport.so
%_K4lib/amiproimport.so
%_K4lib/applixspreadimport.so
%_K4lib/applixwordimport.so
%_K4lib/csvexport.so
%_K4lib/csvimport.so
%_K4lib/dbaseimport.so
%_K4lib/docbookexport.so
%_K4lib/excelimporttodoc.so
%_K4lib/generickofilter.so
%_K4lib/gnumericexport.so
%_K4lib/gnumericimport.so
%_K4lib/hancomwordimport.so
%_K4lib/htmlexport.so
%_K4lib/htmlimport.so
%_K4lib/kounavailpart.so
%_K4lib/oowriterexport.so
%_K4lib/oowriterimport.so
%_K4lib/opencalcexport.so
%_K4lib/opencalcimport.so
%_K4lib/palmdocexport.so
%_K4lib/palmdocimport.so
%_K4lib/qproimport.so
%_K4lib/rtfexport.so
%_K4lib/rtfimport.so
%_K4lib/wmlexport.so
%_K4lib/wmlimport.so
%if_enabled wpg
%_K4lib/wpexport.so
%_K4lib/wpimport.so
%endif
%_K4lib/xsltexport.so
%_K4lib/xsltimport.so
%_K4lib/docximport.so
%_K4libdir/libkdeinit4_kword.so
%_K4datadir/templates/.source/TextDocument.kwt
%_K4datadir/templates/TextDocument.desktop
#%_K4doc/en/kword

%files -n libkwordexportfilters
%_K4libdir/libkwordexportfilters.so.*
%files -n libkwordprivate
%_K4libdir/libkwordprivate.so.*

%files kplato
%_K4bindir/kplato
%_K4bindir/kplatowork
%_K4xdg_apps/kplato.desktop
%_K4xdg_apps/kplatowork.desktop
%_K4apps/kplato
%_K4apps/kplatowork
%_K4conf/kplatorc
%_K4conf/kplatoworkrc
%_K4cfg/kplatosettings.kcfg
%_K4libdir/libkdeinit4_kplato.so
%_K4libdir/libkdeinit4_kplatowork.so
%_K4lib/krossmodulekplato.so
%_K4lib/kplatopart.so
%_K4lib/kplatoworkpart.so
%_K4srv/kplatopart.desktop
%_K4srv/krossmodulekplato.desktop
%_K4srv/kplatoworkpart.desktop
%_K4srv/kplato_icalendar_export.desktop
%_K4srvtyp/kplato_schedulerplugin.desktop
%_K4iconsdir/hicolor/*/*/kplato*.*
#%_K4doc/en/kplato

%files -n libkplatoworkapp
%_K4libdir/libkplatoworkapp.so.*
%files -n libkplatoworkfactory
%_K4libdir/libkplatoworkfactory.so.*

%files -n libchartshapelib
%_K4libdir/libchartshapelib.so.*
%files -n libkplatomodels
%_K4libdir/libkplatomodels.so.*
%files -n libkplatokernel
%_K4libdir/libkplatokernel.so.*
%files -n libkplatoprivate
%_K4libdir/libkplatoprivate.so.*
%files -n libkplatoui
%_K4libdir/libkplatoui.so.*

%files kspread
%_K4bindir/kspread
%_K4lib/krossmodulekspread.so
%_K4lib/kspread*.so
%_K4lib/spreadsheetshape.so
%_K4lib/xlsximport.so
%_K4libdir/libkdeinit4_kspread.so

%_K4iconsdir/hicolor/*/apps/kspread.png

%_K4xdg_apps/kspread.desktop
%_K4srv/ServiceMenus/kspread_konqi.desktop
%_K4apps/kspread
%_K4cfg/kspread.kcfg
%_K4conf/kspreadrc
%_K4doc/en/kspread

%_K4srv/krossmodulekspread.desktop
%_K4srv/kspread*.desktop
%_K4srvtyp/kspread_plugin.desktop
%_K4srv/spreadsheetshape.desktop
%_K4datadir/templates/.source/SpreadSheet.kst
%_K4datadir/templates/SpreadSheet.desktop

%files -n libkspreadcommon
%_K4libdir/libkspreadcommon.so.*
%files -n libkspreadodf
%_K4libdir/libkspreadodf.so.*

%files kpresenter
%_K4bindir/kpresenter
%_K4lib/kpresenterpart.so
%_K4lib/kpr_pageeffect_*.so
%_K4lib/kpr_shapeanimation_example.so
%_K4lib/kpresentereventactions.so
%_K4lib/kpresentertoolanimation.so
%_K4lib/kprvariables.so
%_K4lib/pptximport.so
%_K4libdir/libkdeinit4_kpresenter.so
%_K4xdg_apps/kpresenter.desktop
%_K4conf/kpresenterrc
%_K4apps/kpresenter
%_K4iconsdir/hicolor/*/apps/kpresenter.png
%_K4srv/ServiceMenus/kpresenter_konqi.desktop
%_K4srv/kpresenterpart.desktop
%_K4srv/kpresenter_powerpoint_import.desktop
%_K4srv/kpresentereventactions.desktop
%_K4srv/kpr_pageeffect_*.desktop
%_K4srv/kpr_shapeanimation_example.desktop
%_K4srv/kpresentertoolanimation.desktop
%_K4srv/kprvariables.desktop
%_K4srv/kpresenter_pptx_import.desktop
%_K4srvtyp/presentationeventaction.desktop
%_K4srvtyp/kpr_pageeffect.desktop
%_K4srvtyp/kpr_shapeanimation.desktop
%_K4datadir/templates/.source/Presentation.kpt
%_K4datadir/templates/Presentation.desktop
%_K4doc/en/kpresenter

%files -n libkpresenterprivate
%_K4libdir/libkpresenterprivate.so.*

%if_enabled kformula
%files kformula
#%_K4bindir/kformula
#%_K4libdir/libkdeinit_kformula.so
#%_K4lib/kformulapart.so
%_K4lib/formulashape.so
#%_K4xdg_apps/kformula.desktop
%_K4apps/formulashape
#%_K4apps/kformula
%_K4iconsdir/hicolor/*/apps/kformula.*
#%_K4srv/kformulapart.desktop
%_K4srv/formulashape.desktop
#%_K4srv/ServiceMenus/kformula_konqi.desktop
%_K4doc/en/kformula
%files -n libkformulalib
%_K4libdir/libkformulalib.so.*
%files -n libkformulaprivate
%_K4libdir/libkformulaprivate.so.*
%endif


%if_enabled kivio
%files kivio
%_K4bindir/kivio
%_K4lib/kiviopart.so
%_K4libdir/libkdeinit4_kivio.so
%_K4xdg_apps/kivio.desktop
%_K4apps/kivio
%_K4srv/kiviopart.desktop
%_K4doc/en/kivio
%_K4srv/ServiceMenus/kivio_konqi.desktop
%files -n libkivioprivate
%_K4libdir/libkivioprivate.so.*
%endif

%files kchart
#%_K4bindir/kchart
%_K4lib/chartshape.so
#%_K4lib/kchartpart.so
#%_K4libdir/libkdeinit4_kchart.so
#%_K4lib/kchartgenericimageexport.so
#%_K4lib/kchartsvgexport.so
#
%_K4srv/chartshape.desktop
%_K4srv/kchartpart.desktop
#%_K4srv/kchart_*_export.desktop
#%_K4xdg_apps/kchart.desktop
#%_K4cfg/kchart.kcfg
#%_K4apps/kchart
#%_K4iconsdir/hicolor/*/apps/kchart.png

%files -n libkdchart
%_K4libdir/libkdchart.so.*
#%files -n libkchartcommon
#%_K4libdir/libkchartcommon.so.*
#%files -n libkisexiv
#%_K4libdir/libkisexiv2.so.*

%files krita
%_K4bindir/krita
%_K4lib/*krita*
%_K4libdir/libkdeinit4_krita.so
%_K4xdg_apps/krita.desktop
%_K4xdg_apps/krita_*.desktop
#%_K4xdg_apps/krita_magick.desktop
%_K4srv/ServiceMenus/krita_konqi.desktop
%_K4srv/*krita*.desktop
%_K4srvtyp/*krita*.desktop
%_K4iconsdir/hicolor/*/apps/krita.*
%_K4apps/krita
%_K4apps/kritaplugins
%_K4conf/kritarc
%_K4conf/krita.knsrc
#
%_datadir/color/icc/krita/*.icm
%_datadir/color/icc/pigment/*.icm
%_K4srvtyp/pigment.desktop
%_K4xdg_mime/krita_ora.xml
#
#%_K4doc/en/krita

%files -n libkritaui
%_K4libdir/libkritaui.so.*
%files -n libkritaimage
%_K4libdir/libkritaimage.so.*
%files -n libkritalibpaintop
%_K4libdir/libkritalibpaintop.so.*
%files -n libkritalibbrush
%_K4libdir/libkritalibbrush.so.*

%files karbon
%_K4bindir/karbon
%_K4libdir/libkdeinit4_karbon.so
%_K4lib/karbon_flattenpathplugin.so
%_K4lib/karbon_whirlpinchplugin.so
%_K4lib/karbontools.so
%_K4lib/karbonpart.so
%_K4lib/karbonpngexport.so
%_K4lib/karbonsvgexport.so
%_K4lib/karbonepsimport.so
%_K4lib/wmfexport.so
%_K4lib/wmfimport.so
%_K4lib/karbon1ximport.so
%_K4lib/karbon_refinepathplugin.so
%_K4lib/karbon_roundcornersplugin.so
%_K4xdg_apps/karbon.desktop
%_K4apps/karbon
%_K4srv/ServiceMenus/karbon_konqi.desktop
%_K4conf/karbonrc

%_K4doc/en/karbon

%_K4srv/karbon*.desktop
%_K4srvtyp/karbon_module.desktop
#%_K4datadir/templates/.source/Illustration.karbon
#%_K4datadir/templates/Illustration.desktop
%_K4iconsdir/hicolor/*/apps/karbon.*

%files -n libkarboncommon
%_K4libdir/libkarboncommon.so.*
%files -n libkarbonui
%_K4libdir/libkarbonui.so.*

%if_enabled kexi
%files kexi
%_K4bindir/kexi
%_K4lib/kexidb_*.so
%_K4lib/kexihandler_*.so
%_K4lib/keximigrate_*.so
%_K4lib/kexirelationdesignshape.so
%_K4lib/kformdesigner_containers.so
%_K4lib/kformdesigner_kexidbwidgets.so
%_K4lib/kformdesigner_stdwidgets.so
%_K4lib/krossmodulekexidb.so
%_K4xdg_apps//kexi.desktop
%_K4apps/kexi
%_K4conf/kexirc
%_K4srv/kexi
%_K4srv/kexidb_*.desktop
%_K4srv/keximigrate_*.desktop
%_K4srv/kexirelationdesignshape.desktop
%_K4srv/kformdesigner
%_K4srvtyp/kexidb_driver.desktop
%_K4srvtyp/kexihandler.desktop
%_K4srvtyp/keximigration_driver.desktop
%_K4srvtyp/widgetfactory.desktop
%_K4doc/en/kexi

%files -n libkexicore
%_K4libdir/libkexicore.so.*
%files -n libkexidatatable
%_K4libdir/libkexidatatable.so.*
%files -n libkexidb
%_K4libdir/libkexidb.so.*
%files -n libkexiextendedwidgets
%_K4libdir/libkexiextendedwidgets.so.*
%files -n libkexiformutils
%_K4libdir/libkexiformutils.so.*
%files -n libkexiguiutils
%_K4libdir/libkexiguiutils.so.*
%files -n libkeximain
%_K4libdir/libkeximain.so.*
%files -n libkeximigrate
%_K4libdir/libkeximigrate.so.*
%files -n libkexirelationsview
%_K4libdir/libkexirelationsview.so.*
%files -n libkexiutils
%_K4libdir/libkexiutils.so.*
%files -n libkformdesigner
%_K4libdir/libkformdesigner.so.*
%endif

%changelog
* Thu Jun 21 2012 Sergey V Turchin <zerg@altlinux.org> 4:2.3.3-alt11
- rebuilt with new poppler

* Thu Jun 21 2012 Sergey V Turchin <zerg@altlinux.org> 4:2.3.3-alt9.M60P.1
- built for M60P

* Thu Jun 07 2012 Sergey V Turchin <zerg@altlinux.org> 4:2.3.3-alt10
- built without libwpg

* Wed Apr 04 2012 Sergey V Turchin <zerg@altlinux.org> 4:2.3.3-alt9
- fix to build with new glib2

* Sat Feb 18 2012 Sergey V Turchin <zerg@altlinux.org> 4:2.3.3-alt7.M60P.1
- rebuild with new exiv2

* Fri Feb 10 2012 Sergey V Turchin <zerg@altlinux.org> 4:2.3.3-alt8
- fix to build

* Wed Dec 14 2011 Sergey V Turchin <zerg@altlinux.org> 4:2.3.3-alt6.M60P.1
- built for M60P

* Wed Dec 14 2011 Sergey V Turchin <zerg@altlinux.org> 4:2.3.3-alt7
- fix libko* deps

* Thu Nov 03 2011 Sergey V Turchin <zerg@altlinux.org> 4:2.3.3-alt4.M60P.1
- built for M60P

* Wed Nov 02 2011 Sergey V Turchin <zerg@altlinux.org> 4:2.3.3-alt6
- rebuilt with new exiv2

* Tue Oct 18 2011 Sergey V Turchin <zerg@altlinux.org> 4:2.3.3-alt4.M60T.1
- built for M60T

* Wed Sep 21 2011 Sergey V Turchin <zerg@altlinux.org> 4:2.3.3-alt5
- rebuilt with kde-4.7

* Thu Jul 14 2011 Sergey V Turchin <zerg@altlinux.org> 4:2.3.3-alt3.M60P.1
- built for M60P

* Wed Jul 13 2011 Sergey V Turchin <zerg@altlinux.org> 4:2.3.3-alt4
- don't package karbon template

* Mon Jun 06 2011 Sergey V Turchin <zerg@altlinux.org> 4:2.3.3-alt3
- move templates to appropriate packages

* Wed Apr 20 2011 Sergey V Turchin <zerg@altlinux.org> 4:2.3.3-alt2
- fix build requires

* Wed Mar 16 2011 Sergey V Turchin <zerg@altlinux.org> 4:2.3.3-alt1
- new version

* Fri Jan 21 2011 Sergey V Turchin <zerg@altlinux.org> 4:2.3.1-alt1
- new version

* Tue Oct 05 2010 Sergey V Turchin <zerg@altlinux.org> 4:2.2.2-alt0.M51.1
- built for M51

* Mon Oct 04 2010 Sergey V Turchin <zerg@altlinux.org> 4:2.2.2-alt1
- new version

* Mon Aug 23 2010 Sergey V Turchin <zerg@altlinux.org> 4:2.2.1-alt3
- rebuilt with new poppler

* Mon Aug 02 2010 Sergey V Turchin <zerg@altlinux.org> 4:2.2.1-alt2
- rebuilt with new poppler

* Tue Jul 20 2010 Sergey V Turchin <zerg@altlinux.org> 4:2.2.1-alt0.M51.1
- built for M51

* Mon Jul 19 2010 Sergey V Turchin <zerg@altlinux.org> 4:2.2.1-alt1
- new version

* Mon Jun 07 2010 Sergey V Turchin <zerg@altlinux.org> 4:2.2.0-alt2
- rebuilt with new exiv2

* Thu Jun 03 2010 Sergey V Turchin <zerg@altlinux.org> 4:2.2.0-alt1
- new version

* Tue Jun 01 2010 Sergey V Turchin <zerg@altlinux.org> 4:2.1.2-alt2
- rebuilt with new exiv2

* Thu May 13 2010 Sergey V Turchin <zerg@altlinux.org> 4:2.1.2-alt0.M51.1
- build for M51

* Thu May 13 2010 Sergey V Turchin <zerg@altlinux.org> 4:2.1.2-alt1
- new version

* Thu Apr 22 2010 Sergey V Turchin <zerg@altlinux.org> 4:2.1.1-alt0.M51.1
- build for M51

* Tue Jan 26 2010 Sergey V Turchin <zerg@altlinux.org> 4:2.1.1-alt1
- new version

* Mon Jan 11 2010 Sergey V Turchin <zerg@altlinux.org> 4:2.1.0-alt2
- rebuilt with new exiv2

* Mon Dec 14 2009 Sergey V Turchin <zerg@altlinux.org> 4:2.1.0-alt1
- new version

* Mon Aug 24 2009 Sergey V Turchin <zerg@altlinux.org> 4:2.0.2-alt1
- new version

* Thu Jul 23 2009 Sergey V Turchin <zerg@altlinux.org> 4:2.0.1-alt2.1
- rebuilt witn new exiv2

* Wed Jul 01 2009 Sergey V Turchin <zerg@altlinux.org> 4:2.0.1-alt0.M50.1
- built for M50

* Tue Jun 30 2009 Sergey V Turchin <zerg@altlinux.org> 4:2.0.1-alt1
- new version

* Tue Jun 23 2009 Sergey V Turchin <zerg@altlinux.org> 4:2.0.0-alt2
- rebuilt

* Sat Jun 06 2009 Sergey V Turchin <zerg@altlinux.org> 4:2.0.0-alt0.M50.1
- built for M50

* Fri Jun 05 2009 Sergey V Turchin <zerg@altlinux.org> 4:2.0.0-alt1
- 2.0.0 release

* Fri Apr 10 2009 Sergey V Turchin <zerg@altlinux.org> 4:1.9.99.0-alt0.M50.1
- build for M50

* Wed Apr 08 2009 Sergey V Turchin <zerg@altlinux.org> 4:1.9.99.0-alt1
- RC1

* Mon Apr 06 2009 Sergey V Turchin <zerg@altlinux.org> 4:1.9.98.7-alt1
- beta7

* Thu Jan 22 2009 Sergey V Turchin <zerg at altlinux dot org> 4:1.9.98.5-alt1
- beta5

* Fri Dec 12 2008 Sergey V Turchin <zerg at altlinux dot org> 4:1.9.98.3-alt1
- beta4

* Mon Nov 24 2008 Sergey V Turchin <zerg at altlinux dot org> 4:1.9.98.2-alt2
- rename libflake to libkoflake

* Tue Nov 18 2008 Sergey V Turchin <zerg at altlinux dot org> 4:1.9.98.2-alt1
- beta3

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

