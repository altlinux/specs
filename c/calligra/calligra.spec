
%add_findreq_skiplist %_K4apps/*/scripts/*/*.py
%add_findreq_skiplist %_K4apps/*/scripts/*/*.rb

# obsileted koffice version
%define koffice_ver 4:2.3.70

Name: calligra
Version: 2.9.10
Release: alt2
Epoch: 0
%define libname lib%name

Group: Office
Summary: An integrated office suite
Url: http://www.calligra-suite.org/
License: GPLv2+ / LGPLv2+

Provides: koffice = %koffice_ver
Obsoletes: koffice < %koffice_ver

Requires: %name-braindump = %EVR
Requires: %name-reports-map-element = %EVR
Requires: %name-words = %EVR
Requires: %name-sheets = %EVR
Requires: %name-stage = %EVR
Requires: %name-flow = %EVR
Requires: %name-karbon = %EVR
Requires: %name-krita = %EVR
Requires: %name-kexi = %EVR
Requires: %name-plan = %EVR
Requires: %name-okular-odf = %EVR

Source: http://download.kde.org/stable/calligra-%version/calligra-%version.tar
Source1: FindOkular.cmake
# FC
Patch1: adapt-to-libwps-0.4.patch
# ALT
Patch101: alt-build-active.patch
Patch102: alt-fix-compile.patch
Patch103: alt-disable-products.patch

# Automatically added by buildreq on Fri Nov 02 2012 (-bi)
# optimized out: automoc cmake cmake-modules docbook-dtds docbook-style-xsl elfutils fontconfig fontconfig-devel glibc-devel-static ilmbase-devel kde4libs kde4libs-devel kde4pimlibs libGL-devel libGLU-devel libICE-devel libSM-devel libX11-devel libXScrnSaver-devel libXau-devel libXcomposite-devel libXcursor-devel libXdamage-devel libXdmcp-devel libXext-devel libXfixes-devel libXft-devel libXi-devel libXinerama-devel libXpm-devel libXrandr-devel libXrender-devel libXt-devel libXtst-devel libXv-devel libXxf86misc-devel libXxf86vm-devel libdbus-devel libdbusmenu-qt2 libfreetype-devel libgpg-error libgst-plugins libjpeg-devel libpng-devel libpoppler-devel libpoppler4-qt4 libpq-devel libqt4-core libqt4-dbus libqt4-declarative libqt4-devel libqt4-gui libqt4-network libqt4-opengl libqt4-qt3support libqt4-script libqt4-sql libqt4-svg libqt4-test libqt4-uitools libqt4-webkit libqt4-xml libqt4-xmlpatterns libsoprano-devel libssl-devel libstdc++-devel libtiff-devel libxkbfile-devel openssh-common phonon-devel pkg-config python-base rpm-build-gir ruby shared-desktop-ontologies-devel shared-mime-info soprano-backend-redland soprano-backend-virtuoso xml-common xml-utils xorg-kbproto-devel xorg-xf86miscproto-devel xorg-xproto-devel zlib-devel
#BuildRequires: attica-devel boost-devel-headers cups-filters cvs eigen2 gcc-c++ git-core glib2-devel jdkgcj kde4-okular-devel kde4edu-devel kde4pimlibs-devel libexiv2-devel libfftw3-devel libfreetds-devel libglew-devel libgsl-devel libicu-devel libkdcraw4-devel liblcms2-devel libmysqlclient-devel libopenjpeg-devel libpoppler-qt4-devel libqca2-devel libqt3-devel libsqlite3-devel libxbase-devel mercurial openexr-devel postgresql-devel pstoedit python-module-distribute rpm-build-ruby soprano sqlite3 subversion valgrind zlib-devel-static
BuildRequires: attica-devel boost-devel eigen3 gcc-c++ glib2-devel rpm-build-python rpm-build-ruby
BuildRequires: kde4-okular-devel kde4edu-devel kde4pimlibs-devel libkdcraw4-devel kde-common-devel kde4base-workspace-devel
BuildRequires: libexiv2-devel libfftw3-devel libfreetds-devel libGLEW-devel libgsl-devel libicu-devel libjpeg-devel libopenjpeg-devel libtiff-devel pstoedit
BuildRequires: liblcms2-devel libmysqlclient-devel libopenjpeg-devel libpoppler-qt4-devel
BuildRequires: libqca2-devel libsqlite3-devel sqlite3 libxbase-devel openexr-devel postgresql-devel
BuildRequires: libvisio-devel libwpg-devel libwpd10-devel libwps-devel libodfgen-devel libetonyek-devel libxml2-devel
#BuildRequires: soprano-backend-redland soprano-backend-virtuoso soprano

%description
%summary.

%package common
Summary: %name common package
Group: System/Configuration/Other
BuildArch: noarch
Requires: kde-common
%description common
%name common package

%package core
Group: System/Libraries
Summary: Core support files for %name
Provides: koffice-core = %koffice_ver
Obsoletes: koffice-core < %koffice_ver
Provides:  koffice-kchart = %koffice_ver
Obsoletes: koffice-kchart < %koffice_ver
Provides:  koffice-kformula = %koffice_ver
Obsoletes: koffice-kformula < %koffice_ver
Requires: %libname = %EVR
Requires: fonts-ttf-latex-xft
Requires: kde4base-runtime-core
%description core
%summary.

%package devel
Group: Development/KDE and QT
Summary: Header files and libraries needed for %name development
Requires: kde4libs-devel
Requires: %libname = %EVR
Conflicts: libflake-devel
%description devel
Header files and libraries needed for %name development

%package active
Group: Office
Summary: Mobile version of Calligra
Requires: %name-core = %EVR
%description active
%summary.

%package braindump
Group: Office
Summary: Notes and idea gathering
Requires: %name-core = %EVR
Requires: %libname = %EVR
%description braindump
%summary.

%package reports-map-element
Group: System/Libraries
Summary: Map element for Calligra Reports
Requires: %name-core = %EVR
Requires: %libname = %EVR
Requires: kde4-marble
%description reports-map-element
%summary.

%package words
Group: Office
Summary: An intuitive word processor application with desktop publishing features
Provides: koffice-kword = %koffice_ver
Obsoletes: koffice-kword < %koffice_ver
Requires: %name-core = %EVR
Requires: %libname = %EVR
%description words
KWord is an intuitive word processor and desktop publisher application.
With it, you can create informative and attractive documents with
pleasure and ease.

%package sheets
Group: Office
Summary: A fully-featured spreadsheet application
Provides: koffice-kspread = %koffice_ver
Obsoletes: koffice-kspread < %koffice_ver
Provides: %name-tables = %EVR
Requires: %name-core = %EVR
Requires: %libname = %EVR
%description sheets
Tables is a fully-featured calculation and spreadsheet tool.  Use it to
quickly create and calculate various business-related spreadsheets, such
as income and expenditure, employee working hours...

%package stage
Group: Office
Summary: A full-featured presentation program
Provides: koffice-kpresenter = %koffice_ver
Obsoletes: koffice-kpresenter < %koffice_ver
Requires: %name-core = %EVR
Requires: %libname = %EVR
%description stage
Stage is a powerful and easy to use presentation application. You
can dazzle your audience with stunning slides containing images, videos,
animation and more.

%package flow
Group: Office
Summary: A diagramming and flowcharting application
#Provides: koffice-kivio = %koffice_ver
#Obsoletes: koffice-kivio < %koffice_ver
Requires: %name-core = %EVR
Requires: %libname = %EVR
%description flow
Flow is an easy to use diagramming and flowcharting application with
tight integration to the other KOffice applications. It enables you to
create network diagrams, organisation charts, flowcharts and more.

%package karbon
Group: Graphics
Summary: A vector drawing application
Provides: koffice-karbon = %koffice_ver
Obsoletes: koffice-karbon < %koffice_ver
Requires: %name-core = %EVR
Requires: %libname = %EVR
Requires: pstoedit
%description karbon
Karbon is a vector drawing application with an user interface that is
easy to use, highly customizable and extensible. That makes Karbon a
great application for users starting to explore the world of vector
graphics as well as for artists wanting to create breathtaking vector
art.

Whether you want to create clipart, logos, illustrations or photorealistic
vector images - look no further, Karbon is the tool for you!

%package krita
Group: Graphics
Summary: A creative sketching and painting application
Provides: koffice-krita = %koffice_ver
Obsoletes: koffice-krita < %koffice_ver
Requires: %name-core = %EVR
Requires: %libname = %EVR
Requires: kde4-kross-python create-resources
%description krita
Krita is a creative sketching and painting application based on KOffice
technology. Whether you want to create art paintings, cartoons, concept
art or textures, Krita supports most graphics tablets out of the box.
Krita's vision statement is:
* Krita is a KDE program for sketching and painting, offering an end-to-end
  solution for creating digital painting files from scratch by masters.
* Fields of painting that Krita explicitly supports are concept art,
  creation of comics and textures for rendering.
* Modelled on existing real-world painting materials and workflows,
  Krita supports creative working by getting out of the way and with
  snappy response.

%package kexi
Group: Databases
Summary: An integrated environment for managing data
Provides: koffice-kexi = %koffice_ver
Obsoletes: koffice-kexi < %koffice_ver
Requires: %name-core = %EVR
Requires: %libname = %EVR
%description kexi
Kexi is an integrated data management application.  It can be used for
creating database schemas, inserting data, performing queries, and
processing data. Forms can be created to provide a custom interface to
your data. All database objects - tables, queries and forms - are
stored in the database, making it easy to share data and design.

For additional database drivers take a look at %name-kexi-driver-*

%package kformula
Group: Office
Summary: A powerful formula editor
Provides: koffice-kformula = %koffice_ver
Obsoletes: koffice-kformula < %koffice_ver
Requires: %name-core = %EVR
Requires: %libname = %EVR
#Requires: fonts-ttf-latex-xft fonts-ttf-dejavu-lgc
%description kformula
%summary.

%package plan
Group: Office
Summary: A project planner
Provides: koffice-kplato = %koffice_ver
Obsoletes: koffice-kplato < %koffice_ver
Requires: %name-core = %EVR
Requires: %libname = %EVR
%description plan
Plan is a project management application. It is intended for managing
moderately large projects with multiple resources.

%package okular-odf
Group: Graphics
Summary: OpenDocument formats support for okular
Provides: koffice-okular-odp = %koffice_ver
Obsoletes: koffice-okular-odp < %koffice_ver
Provides: calligra-okular-odp = %EVR
Obsoletes: calligra-okular-odp < %EVR
Requires: %libname = %EVR
Requires: %name-stage = %EVR
Requires: kde4-okular
%description okular-odf
%summary.

%package -n %libname
Summary: %name libraries
Group: System/Libraries
Requires: %name-common = %EVR
%description -n %libname
%name libraries


%prep
%setup
%patch1 -p1
#%patch101 -p1
%patch102 -p1
%patch103 -p1
cp -ar %SOURCE1 cmake/modules/

%build
%K4cmake \
    -DCALLIGRA_SHOULD_BUILD_PRODUCTS=ALL \
    -DCALLIGRA_SHOULD_BUILD_PRODUCTS=ALL \
    -DNEPOMUK=OFF \
    -DPACKAGERS_BUILD=OFF \
    -DKDE4_BUILD_TESTS=OFF \
    #
%K4make

%install
%K4install

# move files back
#mv %buildroot/%_K4srv/calligra/* %buildroot/%_K4srv/
mv %buildroot/%_K4srv/ServiceMenus/calligra/* %buildroot/%_K4srv/ServiceMenus/
#mv %buildroot/%_K4xdg_apps/calligra/* %buildroot/%_K4xdg_apps/


%files
%files common
%dir %_K4srv/calligra/
%doc AUTHORS README

%files devel
%_K4bindir/cstester
%_K4bindir/cstrunner
%_K4bindir/visualimagecompare
%_K4apps/cmake/modules/FindCalligraLibs.cmake
%_K4link/lib*.so
%_K4includedir/calligra/
#%_K4includedir/kexi/
%_K4includedir/krita/
%_K4includedir/stage/
%_K4includedir/sheets/
%_K4includedir/words/
#%_K4includedir/*.h

%files core
%dir %_K4libdir/calligra/
%dir %_K4libdir/calligra/imports
%dir %_K4libdir/calligra/imports/org/
%dir %_K4libdir/calligra/imports/org/calligra/
%dir %_K4libdir/calligra/imports/Calligra/
%dir %_K4libdir/calligra/imports/Calligra/Gemini/
%_K4bindir/calligra
%_K4doc/en/calligra/
%_K4bindir/calligraconverter
%_K4lib/calligra_textediting_autocorrect.so
%_K4lib/calligra_tool_basicflakes.so
%_K4lib/calligra_textediting_changecase.so
%_K4lib/calligra_tool_defaults.so
%_K4lib/calligra_docker_defaults.so
#%_K4lib/calligragoogledocs.so
%_K4lib/calligrathumbnail.so
%_K4lib/calligradocinfopropspage.so
%_K4lib/kopabackgroundtool.*
%_K4lib/kolcmsengine.*
%_K4lib/koreport_barcodeplugin.so
%_K4lib/koreport_chartplugin.so
%_K4lib/koreport_webplugin.so
%_K4srv/calligra/koreport_webplugin.desktop
%_K4lib/calligra_filter_eps2svgai.so
%_K4lib/calligra_filter_pdf2svg.so
%_K4lib/calligra_filter_kpr2odp.so
%_K4lib/calligra_textediting_spellcheck.so
%_K4lib/calligra_textinlineobject_variables.so
%_K4lib/calligra_textediting_thesaurus.so
%_K4lib/calligra_shape_artistictext.so
%_K4lib/calligra_shape_chart.so
%_K4lib/calligra_shape_formular.so
%_K4lib/calligra_shape_music.so
%_K4lib/calligra_shape_picture.so
%_K4lib/calligra_shape_plugin.so
%_K4lib/calligra_shape_spreadsheet.so
%_K4lib/calligra_shape_text.so
%_K4lib/calligra_shape_vector.so
%_K4lib/calligra_shape_video.so
%_K4lib/calligraimagethumbnail.so
#%_K4lib/threedshape.so
%_K4lib/plugins/imageformats/*.so
%_K4libdir/calligra/imports/org/calligra/CalligraComponents/
%_K4apps/calligra/
%_K4apps/koproperty/
%_K4xdg_mime/msooxml-all.xml
%_K4xdg_mime/calligra_svm.xml
%_K4iconsdir/hicolor/*/*/*
%_K4iconsdir/oxygen/*/*/*
#%_K4xdg_apps/calligra.desktop
%_K4srv/calligra/calligra_textediting_autocorrect.desktop
%_K4srv/calligra/calligra_tool_basicflakes.desktop
%_K4srv/calligra/calligra_docker_defaults.desktop
%_K4srv/calligra/calligrastageeventactions.desktop
%_K4srv/calligra/calligrastagetoolanimation.desktop
%_K4srv/calligra/calligra_textediting_changecase.desktop
%_K4srv/calligra/calligra_tool_defaults.desktop
%_K4srv/calligra/calligradocinfopropspage.desktop
%_K4srv/calligra/kolcmsengine.desktop
%_K4srv/calligra/kopabackgroundtool.desktop
%_K4srv/calligra/koreport_barcodeplugin.desktop
%_K4srv/calligra/koreport_chartplugin.desktop
%_K4srv/calligra/calligra_filter_eps2svgai.desktop
%_K4srv/calligra/calligra_filter_pdf2svg.desktop
%_K4srv/calligra/calligra_filter_kpr2odp.desktop
%_K4srv/calligra/calligra_textediting_spellcheck.desktop
%_K4srv/calligra/calligra_textinlineobject_variables.desktop
%_K4srv/calligra/calligra_textediting_thesaurus.desktop
%_K4srv/calligra_odg_thumbnail.desktop
%_K4srv/qimageioplugins/*.desktop
#%_K4srv/threedshape.desktop
%_K4srvtyp/calligradb_driver.desktop
%_K4srvtyp/calligra_application.desktop
%_K4srvtyp/calligra_deferred_plugin.desktop
%_K4srvtyp/calligra_filter.desktop
%_K4srvtyp/calligra_part.desktop
%_K4srvtyp/calligradocker.desktop
#%_K4srvtyp/calligrapart.desktop
%_K4srvtyp/filtereffect.desktop
%_K4srvtyp/flake*.desktop
%_K4srvtyp/inlinetextobject.desktop
#%_K4srvtyp/kochart.desktop
#%_K4srvtyp/koplugin.desktop
%_K4srvtyp/koreport_itemplugin.desktop
%_K4srvtyp/texteditingplugin.desktop
#%_K4srvtyp/textvariableplugin.desktop
%_K4srvtyp/widgetfactory.desktop
%_K4srvtyp/kopa_tool.desktop
%_K4srv/calligra/calligra_shape_artistictext.desktop
%_K4srv/calligra/calligra_shape_chart.desktop
#%_K4srv/kchartpart.desktop
%_K4srv/calligra/kformulapart.desktop
#%_K4srv/kexirelationdesignshape.desktop
%_K4srv/calligra/calligra_shape_formular.desktop
%_K4srv/calligra/calligra_shape_music.desktop
%_K4srv/calligra/calligra_shape_picture.desktop
%_K4srv/calligra/calligra_shape_plugin.desktop
%_K4srv/calligra/calligra_shape_spreadsheet.desktop
%_K4srv/calligra/calligra_shape_text.desktop
%_K4srv/calligra/calligra_shape_vector.desktop
%_K4srv/calligra/calligra_shape_video.desktop
%_K4apps/formulashape/
%_K4apps/musicshape/
%_K4srvtyp/pigment*.desktop
%_K4lib/calligra_shape_paths.so
%_K4srv/calligra/calligra_shape_paths.desktop
#%_K4srvtyp/kofilter*.desktop

%files active
%_K4bindir/calligraactive
%_K4xdg_apps/calligraactive.desktop
%_datadir/calligraactive/qml/

%files braindump
%_K4bindir/braindump
%_K4xdg_apps/braindump.desktop
%_K4apps/braindump/
%_K4srvtyp/braindump_extensions.desktop
%_K4lib/braindump_shape_state.so
%_K4lib/braindump_shape_web.so
%_K4apps/stateshape/
%_K4srv/calligra/braindump_shape_state.desktop
%_K4srv/calligra/braindump_shape_web.desktop

%files reports-map-element
%_K4lib/koreport_mapsplugin.so
%_K4srv/calligra/koreport_mapsplugin.desktop

%files sheets
%_K4bindir/calligrasheets
%_K4libdir/libkdeinit4_calligrasheets.so
%_K4lib/calligrasheets*.so
%_K4lib/kspread*module.so
%_K4lib/krossmodulesheets.so
%_K4lib/calligra_filter_*sheets*.so
%_K4lib/calligra_filter_*kspread*.so
%_K4lib/calligra_filter_xls*.so
%_K4lib/sheetssolver.so
%_K4lib/kspread_plugin_tool_calendar.so
%_K4lib/calligra_shape_spreadsheet-deferred.so
%_K4apps/sheets/
%_K4srv/calligra/krossmodulesheets.desktop
%_K4srv/calligra/calligra_filter_*kspread*.desktop
%_K4srv/calligra/calligra_filter_xls*.desktop
%_K4srv/sheets_*_thumbnail.desktop
%_K4srv/ServiceMenus/sheets_print.desktop
%_K4conf/sheetsrc
%_K4cfg/sheets.kcfg
%_K4srv/calligra/kspread_plugin_tool_calendar.desktop
%_K4srv/calligra/kspread*module.desktop
%_K4srv/calligra/calligra_filter_*sheets*.desktop
%_K4srv/calligra/calligra_shape_spreadsheet-deferred.desktop
%_K4srv/calligra/sheetsscripting.desktop
%_K4srv/calligra/sheetssolver.desktop
%_K4srv/calligra/sheetspart.desktop
%_K4srvtyp/sheets_plugin.desktop
%_K4srvtyp/sheets_viewplugin.desktop
%_K4tmpl/SpreadSheet.*
%_K4tmpl/.source/SpreadSheet.*
%_K4xdg_apps/sheets.desktop
%_K4doc/en/sheets/

%files stage
%doc stage/AUTHORS stage/CHANGES
%_K4bindir/calligrastage
%_K4libdir/libkdeinit4_calligrastage.so
%_K4lib/*stage*.*
%_K4lib/kprvariables.so
%_K4lib/kpr_pageeffect_*.so
%_K4lib/kpr_shapeanimation_*.so
#%_K4lib/Filterkpr2odf.so
%_K4lib/calligra_filter_ppt2odp.so
%_K4lib/calligra_filter_pptx2odp.so
%_K4lib/calligra_filter_key2odp.so
%_K4apps/stage/
%_K4conf/stagerc
%_K4doc/en/stage/
%_K4srv/calligra/kpr*.desktop
%_K4srv/calligra/calligra_filter_ppt2odp.desktop
%_K4srv/calligra/calligra_filter_pptx2odp.desktop
%_K4srv/calligra/calligra_filter_key2odp.desktop
%_K4srvtyp/kpr*.desktop
%_K4srvtyp/presentationeventaction.desktop
%_K4srvtyp/scripteventaction.desktop
%_K4tmpl/Presentation.*
%_K4tmpl/.source/Presentation.*
%_K4xdg_apps/*stage.desktop
#%_K4srv/Filterkpr2odf.desktop
%_K4srv/calligra/stagepart.desktop
%_K4srv/stage_*_thumbnail.desktop
%_K4srv/ServiceMenus/stage_print.desktop
%_K4xdg_mime/x-iwork-keynote-sffkey.xml

%files karbon
%_K4bindir/karbon
%_K4conf/karbonrc
%_K4libdir/libkdeinit4_karbon.so
%_K4lib/*karbon*.*
%_K4lib/calligra_filter_wmf2svg.so
%_K4lib/calligra_filter_xfig2odg.so
%_K4apps/karbon/
%_K4srv/karbon*.desktop
%_K4srv/calligra/karbon*.desktop
%_K4srv/calligra/calligra_filter_*karbon*.desktop
%_K4srv/calligra/calligra_filter_wmf2svg.desktop
%_K4srv/calligra/calligra_filter_xfig2odg.desktop
%_K4srvtyp/karbon_*.desktop
%_K4tmpl/Illustration.*
%_K4tmpl/.source/Illustration.*
%_K4xdg_apps/*karbon.desktop
#_K4doc/en/karbon/
%_K4srv/ServiceMenus/karbon_print.desktop

%files krita
%doc krita/AUTHORS krita/ChangeLog krita/README
%_K4bindir/gmicparser
%_K4bindir/krita
#%_K4bindir/kritagemini
#%_K4bindir/kritasketch
%_K4conf/kritarc
#%_K4libdir/libkdeinit4_krita.so
%_K4lib/*krita*.*
%_K4libdir/calligra/imports/org/krita/
%_K4apps/krita/
%_K4apps/kritagemini/
%_K4apps/kritasketch/
%_K4apps/kritaanimation/
%_K4conf/krita*.knsrc
#%_K4conf/kritagemini*
#%_K4conf/kritasketch*
%_K4srv/calligra/krita*.desktop
%_K4srv/krita_kra_thumbnail.desktop
%_K4srvtyp/krita*.desktop
%_K4srv/ServiceMenus/krita_print.desktop
%_K4xdg_apps/*krita*.desktop
%_K4xdg_mime/krita_ora.xml
%_K4apps/kritaplugins/
%_K4apps/color-schemes/Krita*.colors
%_datadir/color/icc/krita/
%_K4xdg_mime/krita.xml
#
%dir %_datadir/appdata
%_datadir/appdata/krita.appdata.xml
#
%_K4bindir/calligragemini*
%_K4apps/calligragemini/
%_K4libdir/calligra/imports/Calligra/Gemini/
%_K4xdg_apps/calligragemini.desktop

%files kexi
%doc kexi/CHANGES kexi/README
%_K4apps/kexi/
%_K4bindir/kexi*
%_K4lib/kformdesigner_*.so
%_K4lib/kexihandler_*.so
%_K4lib/krossmodulekexidb.so
%_K4lib/kexidb_*driver.so
%_K4lib/kexidb_sqlite3_icu.so
%_K4lib/keximigrate_*.so
#%_K4lib/kexirelationdesignshape.so
%_K4xdg_apps/*kexi.desktop
%_K4conf/kexirc
%_K4srvtyp/kexi*.desktop
%_K4srv/calligra/kexicsv_importexporthandler.desktop
%_K4srv/calligra/kexiformhandler.desktop
%_K4srv/calligra/keximigrationhandler.desktop
%_K4srv/calligra/kexiqueryhandler.desktop
#%_K4srv/calligra/kexirelationdesignshape.desktop
%_K4srv/calligra/kexireporthandler.desktop
%_K4srv/calligra/kexiscripthandler.desktop
%_K4srv/calligra/kexitablehandler.desktop
%_K4srv/calligra/kexidb_*driver.desktop
%_K4srv/calligra/keximigrate_*.desktop
%_K4srv/calligra/kformdesigner_*.desktop
%_K4doc/en/kexi/

%files flow
%doc flow/AUTHORS flow/CHANGE* flow/NOTES flow/README
%_K4bindir/calligraflow
%_K4libdir/libkdeinit4_calligraflow.so
%_K4lib/*flow*.*
%_K4lib/calligra_filter_vsdx2odg.so
%_K4apps/flow/
#_K4doc/en/flow/
%_K4conf/flow_stencils.knsrc
%_K4srv/flow*.desktop
%_K4srv/calligra/flow*.desktop
%_K4srv/calligra/calligra_filter_vsdx2odg.desktop
%_K4xdg_apps/flow.desktop
%_K4conf/flowrc
%_K4srv/ServiceMenus/flow_print.desktop
%_K4srvtyp/flow_dock.desktop

%files plan
%doc plan/CHANGELOG plan/TODO
%_K4bindir/calligraplan
%_K4bindir/calligraplanwork
%_K4conf/planrc
%_K4conf/planworkrc
%_K4libdir/libkdeinit4_calligraplan.so
%_K4libdir/libkdeinit4_calligraplanwork.so
%_K4lib/kplatorcpsscheduler.so
%_K4lib/planpart.*
%_K4lib/planworkpart.so
%_K4lib/planicalexport.*
%_K4lib/plankplatoimport.*
%_K4lib/krossmoduleplan.so
%_K4lib/plantjscheduler.so
#%_K4lib/planconvert/
%_K4srvtyp/plan_schedulerplugin.desktop
%_K4srvtyp/plan_viewplugin.desktop
%_K4srv/calligra/krossmoduleplan.desktop
%_K4apps/plan/
%_K4apps/planwork/
%_K4cfg/plansettings.kcfg
%_K4cfg/planworksettings.kcfg
%_K4srv/calligra/plan*.desktop
#%_K4srv/calligra_filter_mpp2plan.desktop
#%_K4srv/calligra_filter_planner2plan.desktop
%_K4xdg_apps/plan.desktop
%_K4xdg_apps/planwork.desktop
#%_K4xdg_mime/calligra_planner_mpp.xml

%files words
%_K4bindir/calligrawords
%_K4conf/wordsrc
%_K4libdir/libkdeinit4_calligrawords.so
%_K4lib/wordspart.*
%_K4apps/words/
%_K4tmpl/TextDocument.*
%_K4tmpl/.source/TextDocument.*
%_K4xdg_apps/words.desktop
%_K4xdg_apps/calligrawords_ascii.desktop
%_K4srv/calligra/wordspart.desktop
%_K4lib/calligra_filter_applixword2odt.so
%_K4lib/calligra_filter_ascii2words.so
%_K4lib/calligra_filter_doc2odt.so
%_K4lib/calligra_filter_docx2odt.so
%_K4lib/calligra_filter_html2ods.so
%_K4lib/calligra_filter_odt2ascii.so
%_K4lib/calligra_filter_odt2epub2.so
%_K4lib/calligra_filter_odt2html.so
%_K4lib/calligra_filter_odt2mobi.so
%_K4lib/calligra_filter_rtf2odt.so
%_K4lib/calligra_filter_wpd2odt.so
%_K4lib/calligra_filter_wpg2svg.so
%_K4lib/calligra_filter_wpg2odg.so
%_K4lib/calligra_filter_wps2odt.so
%_K4lib/calligra_filter_odt2docx.so
%_K4lib/calligra_filter_odt2wiki.so
%_K4srv/calligra/calligra_filter_applixword2odt.desktop
%_K4srv/calligra/calligra_filter_ascii2words.desktop
%_K4srv/calligra/calligra_filter_doc2odt.desktop
%_K4srv/calligra/calligra_filter_docx2odt.desktop
%_K4srv/calligra/calligra_filter_html2ods.desktop
%_K4srv/calligra/calligra_filter_odt2ascii.desktop
%_K4srv/calligra/calligra_filter_odt2epub2.desktop
%_K4srv/calligra/calligra_filter_odt2html.desktop
%_K4srv/calligra/calligra_filter_odt2mobi.desktop
%_K4srv/calligra/calligra_filter_rtf2odt.desktop
%_K4srv/calligra/calligra_filter_wpd2odt.desktop
%_K4srv/calligra/calligra_filter_wpg2svg.desktop
%_K4srv/calligra/calligra_filter_wpg2odg.desktop
%_K4srv/calligra/calligra_filter_wps2odt.desktop
%_K4srv/calligra/calligra_filter_odt2docx.desktop
%_K4srv/calligra_filter_odt2wiki.desktop
%_K4srv/words_*_thumbnail.desktop
%_K4srv/ServiceMenus/words_print.desktop
%_K4xdg_mime/wiki-format.xml
# author
%_K4bindir/calligraauthor
%_K4libdir/libkdeinit4_calligraauthor.so
%_K4lib/authorpart.so
%_K4xdg_apps/author.desktop
%_K4apps/author/
%_K4conf/authorrc
%_K4srv/calligra/authorpart.desktop

%files okular-odf
%_K4lib/okularGenerator_*.so
%_K4xdg_apps/okularApplication_*.desktop
%_K4srv/libokularGenerator_*.desktop
%_K4srv/okular*.desktop

%files -n %libname
%_K4libdir/lib*.so.*
#%_K4libdir/libkritasketchlib.so
%_K4libdir/libkritacolord.so

%changelog
* Tue Jan 19 2016 Sergey V Turchin <zerg@altlinux.org> 0:2.9.10-alt2
- rebuild with new okular

* Mon Jan 18 2016 Sergey V Turchin <zerg@altlinux.org> 0:2.9.10-alt1
- new version

* Mon Nov 09 2015 Sergey V Turchin <zerg@altlinux.org> 0:2.9.9-alt1
- new version

* Fri Sep 04 2015 Sergey V Turchin <zerg@altlinux.org> 0:2.9.7-alt1
- new version

* Tue Jun 30 2015 Sergey V Turchin <zerg@altlinux.org> 0:2.9.5-alt2
- rebuild with new exiv2

* Fri Jun 19 2015 Sergey V Turchin <zerg@altlinux.org> 0:2.9.5-alt1
- new version

* Tue Jun 16 2015 Gleb F-Malinovskiy <glebfm@altlinux.org> 0:2.9.2-alt2.1
- Rebuilt for gcc5 C++11 ABI.

* Thu Apr 23 2015 Sergey V Turchin <zerg@altlinux.org> 0:2.9.2-alt2
- rebuild with new marble

* Wed Apr 15 2015 Sergey V Turchin <zerg@altlinux.org> 0:2.9.2-alt1
- new version

* Thu Mar 26 2015 Sergey V Turchin <zerg@altlinux.org> 0:2.9.1-alt1
- new version

* Wed Mar 04 2015 Sergey V Turchin <zerg@altlinux.org> 0:2.9.0-alt1
- new version

* Wed Jan 28 2015 Sergey V Turchin <zerg@altlinux.org> 0:2.8.7-alt3
- rebuild with new okular

* Thu Dec 25 2014 Sergey V Turchin <zerg@altlinux.org> 0:2.8.7-alt2
- split Calligra Active to separate package
- rebuilt with new poppler

* Tue Dec 09 2014 Sergey V Turchin <zerg@altlinux.org> 0:2.8.7-alt1
- new version

* Thu Nov 27 2014 Sergey V Turchin <zerg@altlinux.org> 0:2.8.6-alt1
- new version

* Mon Sep 15 2014 Sergey V Turchin <zerg@altlinux.org> 0:2.8.5-alt3
- rebuild

* Fri Aug 15 2014 Sergey V Turchin <zerg@altlinux.org> 0:2.8.5-alt2
- rebuilt with new KDE

* Mon Jul 07 2014 Sergey V Turchin <zerg@altlinux.org> 0:2.8.5-alt1
- new version

* Fri Jun 06 2014 Alexey Shabalin <shaba@altlinux.ru> 0:2.8.3-alt2
- switch to librevenge-based import libs

* Thu May 22 2014 Sergey V Turchin <zerg@altlinux.org> 0:2.8.3-alt0.M70P.1
- built for M70P

* Thu May 22 2014 Sergey V Turchin <zerg@altlinux.org> 0:2.8.3-alt1
- new version

* Thu Apr 24 2014 Sergey V Turchin <zerg@altlinux.org> 0:2.8.2-alt0.M70P.1
- built for M70P

* Wed Apr 23 2014 Sergey V Turchin <zerg@altlinux.org> 0:2.8.2-alt1
- new version

* Thu Apr 03 2014 Sergey V Turchin <zerg@altlinux.org> 0:2.8.1-alt0.M70P.1
- built for M70P

* Wed Apr 02 2014 Sergey V Turchin <zerg@altlinux.org> 0:2.8.1-alt1
- new version

* Wed Apr 02 2014 Sergey V Turchin <zerg@altlinux.org> 0:2.8.0-alt0.M70P.1
- built for M70P

* Tue Mar 11 2014 Sergey V Turchin <zerg@altlinux.org> 0:2.8.0-alt1
- new version

* Tue Feb 04 2014 Sergey V Turchin <zerg@altlinux.org> 0:2.7.5-alt4
- rebuilt

* Fri Dec 20 2013 Sergey V Turchin <zerg@altlinux.org> 0:2.7.5-alt3
- require stage for okular odp

* Thu Dec 19 2013 Sergey V Turchin <zerg@altlinux.org> 0:2.7.5-alt2
- move ppt import modules into core subpackage

* Mon Dec 09 2013 Sergey V Turchin <zerg@altlinux.org> 0:2.7.5-alt1
- new version

* Fri Nov 01 2013 Sergey V Turchin <zerg@altlinux.org> 0:2.7.4-alt1
- new version

* Mon Sep 16 2013 Sergey V Turchin <zerg@altlinux.org> 0:2.7.3-alt1
- new version

* Wed Sep 11 2013 Sergey V Turchin <zerg@altlinux.org> 0:2.7.2-alt1
- new version

* Thu Aug 01 2013 Sergey V Turchin <zerg@altlinux.org> 0:2.7.1-alt1
- new version

* Tue Jul 30 2013 Sergey V Turchin <zerg@altlinux.org> 0:2.6.4-alt1.M70P.1
- built for M70P

* Tue Jul 30 2013 Sergey V Turchin <zerg@altlinux.org> 0:2.6.4-alt2
- fix build requires

* Mon Jul 29 2013 Sergey V Turchin <zerg@altlinux.org> 0:2.6.4-alt1
- new version

* Tue May 21 2013 Sergey V Turchin <zerg@altlinux.org> 0:2.6.3-alt1
- new version

* Wed Apr 24 2013 Sergey V Turchin <zerg@altlinux.org> 0:2.6.1-alt4
- rebuild with new poppler

* Mon Apr 08 2013 Sergey V Turchin <zerg@altlinux.org> 0:2.6.1-alt3
- rebuild with new poppler
- fix requires

* Thu Feb 28 2013 Sergey V Turchin <zerg@altlinux.org> 0:2.6.1-alt2
- built with opengtl

* Fri Feb 22 2013 Sergey V Turchin <zerg@altlinux.org> 0:2.6.1-alt1
- new version

* Thu Feb 07 2013 Sergey V Turchin <zerg@altlinux.org> 0:2.6.0-alt1
- new version

* Sun Jan 27 2013 Sergey V Turchin <zerg@altlinux.org> 0:2.5.5-alt2
- don't split libs
- fix requires

* Thu Jan 24 2013 Sergey V Turchin <zerg@altlinux.org> 0:2.5.5-alt1
- new version

* Tue Dec 18 2012 Sergey V Turchin <zerg@altlinux.org> 0:2.5.4-alt3
- rebuilt with new marble

* Sun Dec 16 2012 Sergey V Turchin <zerg@altlinux.org> 0:2.5.4-alt1.M60P.1
- built for M60P

* Sun Dec 16 2012 Sergey V Turchin <zerg@altlinux.org> 0:2.5.4-alt2
- don't obsolete kivio by flow

* Thu Dec 13 2012 Sergey V Turchin <zerg@altlinux.org> 0:2.5.4-alt1
- new version

* Fri Nov 02 2012 Sergey V Turchin <zerg@altlinux.org> 0:2.5.3-alt1
- new version

* Wed Oct 31 2012 Sergey V Turchin <zerg@altlinux.org> 4:2.5.2-alt1
- new version

* Thu May 03 2012 Sergey V Turchin <zerg@altlinux.org> 4:2.4.1-alt1
- initial build
