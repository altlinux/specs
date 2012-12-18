
%add_findreq_skiplist %_K4apps/*/scripts/*/*.py
%add_findreq_skiplist %_K4apps/*/scripts/*/*.rb

%define sover_common 10
%define sover_kowv2 9
# obsileted koffice version
%define koffice_ver 4:2.3.70
%def_disable map_shape

%def_disable GTL

Name: calligra
Version: 2.5.4
Release: alt3
Serial: 0

Group: Office
Summary: An integrated office suite
Url: http://www.calligra-suite.org/
License: GPLv2+ / LGPLv2+

Provides: koffice = %koffice_ver
Obsoletes: koffice < %koffice_ver

Requires: %name-braindump = %serial:%version-%release
%if_enabled map_shape
Requires: %name-map-shape = %serial:%version-%release
%endif
Requires: %name-reports-map-element = %serial:%version-%release
Requires: %name-words = %serial:%version-%release
Requires: %name-sheets = %serial:%version-%release
Requires: %name-stage = %serial:%version-%release
Requires: %name-flow = %serial:%version-%release
Requires: %name-karbon = %serial:%version-%release
Requires: %name-krita = %serial:%version-%release
Requires: %name-kexi = %serial:%version-%release
Requires: %name-plan = %serial:%version-%release
Requires: %name-okular-odp = %serial:%version-%release

Source: http://download.kde.org/stable/calligra-%version/calligra-%version.tar
Source1: FindOkular.cmake

# Automatically added by buildreq on Fri Nov 02 2012 (-bi)
# optimized out: automoc cmake cmake-modules docbook-dtds docbook-style-xsl elfutils fontconfig fontconfig-devel glibc-devel-static ilmbase-devel kde4libs kde4libs-devel kde4pimlibs libGL-devel libGLU-devel libICE-devel libSM-devel libX11-devel libXScrnSaver-devel libXau-devel libXcomposite-devel libXcursor-devel libXdamage-devel libXdmcp-devel libXext-devel libXfixes-devel libXft-devel libXi-devel libXinerama-devel libXpm-devel libXrandr-devel libXrender-devel libXt-devel libXtst-devel libXv-devel libXxf86misc-devel libXxf86vm-devel libdbus-devel libdbusmenu-qt2 libfreetype-devel libgpg-error libgst-plugins libjpeg-devel libpng-devel libpoppler-devel libpoppler4-qt4 libpq-devel libqt4-core libqt4-dbus libqt4-declarative libqt4-devel libqt4-gui libqt4-network libqt4-opengl libqt4-qt3support libqt4-script libqt4-sql libqt4-svg libqt4-test libqt4-uitools libqt4-webkit libqt4-xml libqt4-xmlpatterns libsoprano-devel libssl-devel libstdc++-devel libtiff-devel libxkbfile-devel openssh-common phonon-devel pkg-config python-base rpm-build-gir ruby shared-desktop-ontologies-devel shared-mime-info soprano-backend-redland soprano-backend-virtuoso xml-common xml-utils xorg-kbproto-devel xorg-xf86miscproto-devel xorg-xproto-devel zlib-devel
#BuildRequires: attica-devel boost-devel-headers cups-filters cvs eigen2 gcc-c++ git-core glib2-devel jdkgcj kde4-okular-devel kde4edu-devel kde4pimlibs-devel libexiv2-devel libfftw3-devel libfreetds-devel libglew-devel libgsl-devel libicu-devel libkdcraw4-devel liblcms2-devel libmysqlclient-devel libopenjpeg-devel libpoppler-qt4-devel libqca2-devel libqt3-devel libsqlite3-devel libxbase-devel mercurial openexr-devel postgresql-devel pstoedit python-module-distribute rpm-build-ruby soprano sqlite3 subversion valgrind zlib-devel-static
BuildRequires: attica-devel boost-devel eigen2 gcc-c++ glib2-devel rpm-build-python rpm-build-ruby
BuildRequires: kde4-okular-devel kde4edu-devel kde4pimlibs-devel libkdcraw4-devel kde-common-devel
BuildRequires: libexiv2-devel libfftw3-devel libfreetds-devel libglew-devel libgsl-devel libicu-devel
BuildRequires: liblcms2-devel libmysqlclient-devel libopenjpeg-devel libpoppler-qt4-devel
BuildRequires: libqca2-devel libsqlite3-devel sqlite3 libxbase-devel openexr-devel postgresql-devel
BuildRequires: soprano-backend-redland soprano-backend-virtuoso soprano
%if_enabled GTL
BuildRequires: pkgconfig(GTLCore) >= 0.9.16
BuildRequires: pkgconfig(QtGTL)
%endif

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
Requires: %name-common = %serial:%version-%release
Requires: fonts-ttf-latex-xft
Requires: kde4base-runtime-core
%description core
%summary.

%package devel
Group: Development/KDE and QT
Summary: Header files and libraries needed for %name development
Requires: kde4libs-devel
Conflicts: libflake-devel
%description devel
Header files and libraries needed for %name development

%package braindump
Group: Office
Summary: Notes and idea gathering
Requires: %name-core = %serial:%version-%release
%description braindump
%summary.

%package map-shape
Group: System/Libraries
Summary: Map shape for Calligra applications
Requires: %name-core = %serial:%version-%release
Requires: kde4edu-marble
%description map-shape
%summary.

%package reports-map-element
Group: System/Libraries
Summary: Map element for Calligra Reports
Requires: %name-core = %serial:%version-%release
Requires: kde4edu-marble
%description reports-map-element
%summary.

%package words
Group: Office
Summary: An intuitive word processor application with desktop publishing features
Provides: koffice-kword = %koffice_ver
Obsoletes: koffice-kword < %koffice_ver
Requires: %name-core = %serial:%version-%release
%description words
KWord is an intuitive word processor and desktop publisher application.
With it, you can create informative and attractive documents with
pleasure and ease.

%package sheets
Group: Office
Summary: A fully-featured spreadsheet application
Provides: koffice-kspread = %koffice_ver
Obsoletes: koffice-kspread < %koffice_ver
Provides: calligra-tables = %version-%release
Requires: %name-core = %serial:%version-%release
%description sheets
Tables is a fully-featured calculation and spreadsheet tool.  Use it to
quickly create and calculate various business-related spreadsheets, such
as income and expenditure, employee working hours...

%package stage
Group: Office
Summary: A full-featured presentation program
Provides: koffice-kpresenter = %koffice_ver
Obsoletes: koffice-kpresenter < %koffice_ver
Requires: %name-core = %serial:%version-%release
%description stage
Stage is a powerful and easy to use presentation application. You
can dazzle your audience with stunning slides containing images, videos,
animation and more.

%package flow
Group: Office
Summary: A diagramming and flowcharting application
#Provides: koffice-kivio = %koffice_ver
#Obsoletes: koffice-kivio < %koffice_ver
Requires: %name-core = %serial:%version-%release
%description flow
Flow is an easy to use diagramming and flowcharting application with
tight integration to the other KOffice applications. It enables you to
create network diagrams, organisation charts, flowcharts and more.

%package karbon
Group: Graphics
Summary: A vector drawing application
Provides: koffice-karbon = %koffice_ver
Obsoletes: koffice-karbon < %koffice_ver
Requires: %name-core = %serial:%version-%release
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
Requires: %name-core = %serial:%version-%release
Requires: kde4-kross-python
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
Requires: %name-core = %serial:%version-%release
Requires: kde4edu-marble
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
Requires: %name-core = %serial:%version-%release
#Requires: fonts-ttf-latex-xft fonts-ttf-dejavu-lgc
%description kformula
%summary.

%package plan
Group: Office
Summary: A project planner
Provides: koffice-kplato = %koffice_ver
Obsoletes: koffice-kplato < %koffice_ver
Requires: %name-core = %serial:%version-%release
%description plan
Plan is a project management application. It is intended for managing
moderately large projects with multiple resources.

%package okular-odp
Group: Graphics
Summary: OpenDocument presenter support for okular
Provides: koffice-okular-odp = %koffice_ver
Obsoletes: koffice-okular-odp < %koffice_ver
Requires: %name-stage = %version-%release
Requires: kde4-okular
%description okular-odp
%summary.

%package -n libbraindumpcore%sover_common
Summary: %name core library
Group: System/Libraries
Requires: %name-common = %serial:%version-%release
%description -n libbraindumpcore%sover_common
%name core library

%package -n libcalligrasheetscommon%sover_common
Summary: %name core library
Group: System/Libraries
Requires: %name-common = %serial:%version-%release
%description -n libcalligrasheetscommon%sover_common
%name core library

%package -n libcalligrasheetsodf%sover_common
Summary: %name core library
Group: System/Libraries
Requires: %name-common = %serial:%version-%release
%description -n libcalligrasheetsodf%sover_common
%name core library

%package -n libcalligrastageprivate%sover_common
Summary: %name core library
Group: System/Libraries
Requires: %name-common = %serial:%version-%release
%description -n libcalligrastageprivate%sover_common
%name core library

%package -n libchartshapelib%sover_common
Summary: %name core library
Group: System/Libraries
Requires: %name-common = %serial:%version-%release
%description -n libchartshapelib%sover_common
%name core library

%package -n libflake%sover_common
Summary: %name core library
Group: System/Libraries
Requires: %name-common = %serial:%version-%release
%description -n libflake%sover_common
%name core library

%package -n libflowprivate%sover_common
Summary: %name core library
Group: System/Libraries
Requires: %name-common = %serial:%version-%release
%description -n libflowprivate%sover_common
%name core library

%package -n libkarboncommon%sover_common
Summary: %name core library
Group: System/Libraries
Requires: %name-common = %serial:%version-%release
%description -n libkarboncommon%sover_common
%name core library

%package -n libkarbonui%sover_common
Summary: %name core library
Group: System/Libraries
Requires: %name-common = %serial:%version-%release
%description -n libkarbonui%sover_common
%name core library

%package -n libkdchart%sover_common
Summary: %name core library
Group: System/Libraries
Requires: %name-common = %serial:%version-%release
%description -n libkdchart%sover_common
%name core library

%package -n libkexicore%sover_common
Summary: %name core library
Group: System/Libraries
Requires: %name-common = %serial:%version-%release
%description -n libkexicore%sover_common
%name core library

%package -n libkexidatatable%sover_common
Summary: %name core library
Group: System/Libraries
Requires: %name-common = %serial:%version-%release
%description -n libkexidatatable%sover_common
%name core library

%package -n libkexidataviewcommon%sover_common
Summary: %name core library
Group: System/Libraries
Requires: %name-common = %serial:%version-%release
%description -n libkexidataviewcommon%sover_common
%name core library

%package -n libkexidb%sover_common
Summary: %name core library
Group: System/Libraries
Requires: %name-common = %serial:%version-%release
%description -n libkexidb%sover_common
%name core library

%package -n libkexiextendedwidgets%sover_common
Summary: %name core library
Group: System/Libraries
Requires: %name-common = %serial:%version-%release
%description -n libkexiextendedwidgets%sover_common
%name core library

%package -n libkexiformutils%sover_common
Summary: %name core library
Group: System/Libraries
Requires: %name-common = %serial:%version-%release
%description -n libkexiformutils%sover_common
%name core library

%package -n libkexiguiutils%sover_common
Summary: %name core library
Group: System/Libraries
Requires: %name-common = %serial:%version-%release
%description -n libkexiguiutils%sover_common
%name core library

%package -n libkeximain%sover_common
Summary: %name core library
Group: System/Libraries
Requires: %name-common = %serial:%version-%release
%description -n libkeximain%sover_common
%name core library

%package -n libkeximigrate%sover_common
Summary: %name core library
Group: System/Libraries
Requires: %name-common = %serial:%version-%release
%description -n libkeximigrate%sover_common
%name core library

%package -n libkexirelationsview%sover_common
Summary: %name core library
Group: System/Libraries
Requires: %name-common = %serial:%version-%release
%description -n libkexirelationsview%sover_common
%name core library

%package -n libkexiutils%sover_common
Summary: %name core library
Group: System/Libraries
Requires: %name-common = %serial:%version-%release
%description -n libkexiutils%sover_common
%name core library

%package -n libkformdesigner%sover_common
Summary: %name core library
Group: System/Libraries
Requires: %name-common = %serial:%version-%release
%description -n libkformdesigner%sover_common
%name core library

%package -n libkformulalib%sover_common
Summary: %name core library
Group: System/Libraries
Requires: %name-common = %serial:%version-%release
%description -n libkformulalib%sover_common
%name core library

%package -n libkochart%sover_common
Summary: %name core library
Group: System/Libraries
Requires: %name-common = %serial:%version-%release
%description -n libkochart%sover_common
%name core library

%package -n libkokross%sover_common
Summary: %name core library
Group: System/Libraries
Requires: %name-common = %serial:%version-%release
%description -n libkokross%sover_common
%name core library

%package -n libkomain%sover_common
Summary: %name core library
Group: System/Libraries
Requires: %name-common = %serial:%version-%release
%description -n libkomain%sover_common
%name core library

%package -n libkoodf%sover_common
Summary: %name core library
Group: System/Libraries
Requires: %name-common = %serial:%version-%release
%description -n libkoodf%sover_common
%name core library

%package -n libkopageapp%sover_common
Summary: %name core library
Group: System/Libraries
Requires: %name-common = %serial:%version-%release
%description -n libkopageapp%sover_common
%name core library

%package -n libkoplugin%sover_common
Summary: %name core library
Group: System/Libraries
Requires: %name-common = %serial:%version-%release
%description -n libkoplugin%sover_common
%name core library

%package -n libkoproperty%sover_common
Summary: %name core library
Group: System/Libraries
Requires: %name-common = %serial:%version-%release
%description -n libkoproperty%sover_common
%name core library

%package -n libkoreport%sover_common
Summary: %name core library
Group: System/Libraries
Requires: %name-common = %serial:%version-%release
%description -n libkoreport%sover_common
%name core library

%package -n libkotext%sover_common
Summary: %name core library
Group: System/Libraries
Requires: %name-common = %serial:%version-%release
%description -n libkotext%sover_common
%name core library

%package -n libkowidgets%sover_common
Summary: %name core library
Group: System/Libraries
Requires: %name-common = %serial:%version-%release
%description -n libkowidgets%sover_common
%name core library

%package -n libkowv2%sover_kowv2
Summary: %name core library
Group: System/Libraries
Requires: %name-common = %serial:%version-%release
%description -n libkowv2%sover_kowv2
%name core library

%package -n libkplatokernel%sover_common
Summary: %name core library
Group: System/Libraries
Requires: %name-common = %serial:%version-%release
%description -n libkplatokernel%sover_common
%name core library

%package -n libkplatomodels%sover_common
Summary: %name core library
Group: System/Libraries
Requires: %name-common = %serial:%version-%release
%description -n libkplatomodels%sover_common
%name core library

%package -n libkplatoui%sover_common
Summary: %name core library
Group: System/Libraries
Requires: %name-common = %serial:%version-%release
%description -n libkplatoui%sover_common
%name core library

%package -n libkritaimage%sover_common
Summary: %name core library
Group: System/Libraries
Requires: %name-common = %serial:%version-%release
%description -n libkritaimage%sover_common
%name core library

%package -n libkritalibbrush%sover_common
Summary: %name core library
Group: System/Libraries
Requires: %name-common = %serial:%version-%release
%description -n libkritalibbrush%sover_common
%name core library

%package -n libkritalibpaintop%sover_common
Summary: %name core library
Group: System/Libraries
Requires: %name-common = %serial:%version-%release
%description -n libkritalibpaintop%sover_common
%name core library

%package -n libkritaui%sover_common
Summary: %name core library
Group: System/Libraries
Requires: %name-common = %serial:%version-%release
%description -n libkritaui%sover_common
%name core library

%package -n libkundo2%sover_common
Summary: %name core library
Group: System/Libraries
Requires: %name-common = %serial:%version-%release
%description -n libkundo2%sover_common
%name core library

%package -n liblibwmf%sover_common
Summary: %name core library
Group: System/Libraries
Requires: %name-common = %serial:%version-%release
%description -n liblibwmf%sover_common
%name core library

%package -n libmsooxml%sover_common
Summary: %name core library
Group: System/Libraries
Requires: %name-common = %serial:%version-%release
%description -n libmsooxml%sover_common
%name core library

%package -n libpigmentcms%sover_common
Summary: %name core library
Group: System/Libraries
Requires: %name-common = %serial:%version-%release
%description -n libpigmentcms%sover_common
%name core library

%package -n libplanprivate%sover_common
Summary: %name core library
Group: System/Libraries
Requires: %name-common = %serial:%version-%release
%description -n libplanprivate%sover_common
%name core library

%package -n libplanworkapp%sover_common
Summary: %name core library
Group: System/Libraries
Requires: %name-common = %serial:%version-%release
%description -n libplanworkapp%sover_common
%name core library

%package -n libplanworkfactory%sover_common
Summary: %name core library
Group: System/Libraries
Requires: %name-common = %serial:%version-%release
%description -n libplanworkfactory%sover_common
%name core library

%package -n librcps_plan%sover_common
Summary: %name core library
Group: System/Libraries
Requires: %name-common = %serial:%version-%release
%description -n librcps_plan%sover_common
%name core library

%package -n librtfreader%sover_common
Summary: %name core library
Group: System/Libraries
Requires: %name-common = %serial:%version-%release
%description -n librtfreader%sover_common
%name core library

%package -n libtextlayout%sover_common
Summary: %name core library
Group: System/Libraries
Requires: %name-common = %serial:%version-%release
%description -n libtextlayout%sover_common
%name core library

%package -n libwordsprivate%sover_common
Summary: %name core library
Group: System/Libraries
Requires: %name-common = %serial:%version-%release
%description -n libwordsprivate%sover_common
%name core library

%prep
%setup
cp -ar %SOURCE1 cmake/modules/

%build
%K4cmake \
  -DEIGEN2_INCLUDE_DIR:PATH=%_includedir/eigen2 \
  -DBUILD_koabstraction:BOOL=OFF \
  -DBUILD_cstester:BOOL=OFF \
  -DKDE4_BUILD_TESTS:BOOL=OFF \
  -DIHAVEPATCHEDQT:BOOL=ON
%K4make

%install
%K4install


%files
%files common

%files devel
%_K4apps/cmake/modules/FindCalligraLibs.cmake
%_K4includedir/*.h
%_K4includedir/*.cpp
%_K4link/lib*.so
%_K4includedir/changetracker/
%_K4includedir/kexi/
%_K4includedir/stage/
%_K4includedir/styles/
%_K4includedir/sheets/
%_K4includedir/words/

%files core
%doc AUTHORS COPYING COPYING.LIB README
%_K4bindir/calligra
%_K4bindir/calligraactive
%_K4doc/en/calligra/
%_K4bindir/calligraconverter
%_K4lib/autocorrect.so
%_K4lib/changecase.so
%_K4lib/defaulttools.so
%_K4lib/calligradockers.so
%_K4lib/calligragoogledocs.so
%_K4lib/calligrathumbnail.so
%_K4lib/kodocinfopropspage.*
%_K4lib/kopabackgroundtool.*
%_K4lib/kolcmsengine.*
%_K4lib/koreport_barcodeplugin.so
%_K4lib/koreport_chartplugin.so
%_K4lib/koreport_webplugin.so
%_K4srv/koreport_webplugin.desktop
%_K4lib/spellcheck.so
%_K4lib/textvariables.so
%_K4lib/thesaurustool.so
%_K4lib/artistictextshape.so
%_K4lib/chartshape.so
%_K4lib/commentshape.so
%_K4lib/musicshape.so
%_K4lib/pictureshape.so
%_K4lib/pluginshape.so
%_K4lib/spreadsheetshape.so
%_K4lib/textshape.so
%_K4lib/vectorshape.so
%_K4lib/videoshape.so
%_K4lib/webshape.so
%_K4apps/calligra/
%_K4apps/koproperty/
%_K4xdg_mime/msooxml-all.xml
%_K4iconsdir/hicolor/*/*/*
%_K4iconsdir/oxygen/*/*/*
%_K4xdg_apps/calligra.desktop
%_desktopdir/calligraactive.desktop
%_K4srv/autocorrect.desktop
%_K4srv/calligradockers.desktop
%_K4srv/calligrastageeventactions.desktop
%_K4srv/calligrastagetoolanimation.desktop
%_K4srv/calligrathumbnail.desktop
%_K4srv/changecase.desktop
%_K4srv/defaulttools.desktop
%_K4srv/kodocinfopropspage.desktop
%_K4srv/kolcmsengine.desktop
%_K4srv/kopabackgroundtool.desktop
%_K4srv/koreport_barcodeplugin.desktop
%_K4srv/koreport_chartplugin.desktop
%_K4srv/spellcheck.desktop
%_K4srv/textvariables.desktop
%_K4srv/thesaurustool.desktop
%_K4srvtyp/calligra_application.desktop
%_K4srvtyp/calligra_deferred_plugin.desktop
%_K4srvtyp/calligradocker.desktop
%_K4srvtyp/calligrapart.desktop
%_K4srvtyp/filtereffect.desktop
%_K4srvtyp/flake*.desktop
%_K4srvtyp/inlinetextobject.desktop
%_K4srvtyp/kochart.desktop
%_K4srvtyp/koplugin.desktop
%_K4srvtyp/koreport_itemplugin.desktop
%_K4srvtyp/texteditingplugin.desktop
%_K4srvtyp/textvariableplugin.desktop
%_K4srvtyp/widgetfactory.desktop
%_K4srv/artistictextshape.desktop
%_K4srv/chartshape.desktop
%_K4srv/kchartpart.desktop
%_K4srv/commentshape.desktop
%_K4srv/formulashape.desktop
%_K4srv/kformulapart.desktop
%_K4srv/kexirelationdesignshape.desktop
%_K4srv/musicshape.desktop
%_K4srv/pictureshape.desktop
%_K4srv/pluginshape.desktop
%_K4srv/spreadsheetshape.desktop
%_K4srv/textshape.desktop
%_K4srv/vectorshape.desktop
%_K4srv/videoshape.desktop
%_K4srv/webshape.desktop
%_K4apps/formulashape/
%_K4lib/formulashape.*
%_K4apps/musicshape/
%_datadir/color/icc/pigment/
%if_enabled GTL
%_K4apps/pigmentcms/
%endif
%_K4srvtyp/pigment*.desktop
%_K4lib/pathshapes.so
%_K4srv/pathshapes.desktop
#%_K4lib/xsltimport.*
#%_K4lib/xsltexport.*
#%_K4apps/xsltfilter/
#%_K4srv/xslt*.desktop
%_K4srvtyp/kofilter*.desktop
%_datadir/calligraactive/qml/

%files braindump
%_K4bindir/braindump
%_K4xdg_apps/braindump.desktop
%_K4apps/braindump/
%_K4srvtyp/braindump_extensions.desktop
%_K4lib/stateshape.so
%_K4conf/braindumprc
%_K4apps/stateshape/
%_K4srv/stateshape.desktop

%if_enabled map_shape
%files map-shape
%_K4lib/mapshape.so
%_K4srv/mapshape.desktop
%endif

%files reports-map-element
%_K4lib/koreport_mapsplugin.so
%_K4srv/koreport_mapsplugin.desktop

%files sheets
%_K4bindir/calligrasheets
%_K4libdir/libkdeinit4_calligrasheets.so
#%_K4libdir/libcalligrasheetsodf.so
%_K4lib/calligrasheets*.so
%_K4lib/applixspreadimport.*
%_K4lib/csvexport.*
%_K4lib/csvimport.*
%_K4lib/dbaseimport.*
%_K4lib/excelimporttodoc.*
%_K4lib/gnumericexport.*
%_K4lib/gnumericimport.*
%_K4lib/kspread*import.*
%_K4lib/kspread*export.*
%_K4lib/kspread*module.so
%_K4lib/opencalcexport.*
%_K4lib/opencalcimport.*
%_K4lib/qproimport.*
%_K4lib/xlsximport.*
%_K4lib/krossmodulekspread.so
%_K4lib/kspread_plugin_tool_calendar.so
%_K4lib/kspreadsolver.so
%_K4lib/spreadsheetshape-deferred.so
%_K4apps/sheets/
%_K4apps/tables/

%_K4conf/sheetsrc
%_K4cfg/sheets.kcfg
%_K4srv/krossmodulekspread.desktop
%_K4srv/kspread_plugin_tool_calendar.desktop
%_K4srv/kspread*module.desktop
%_K4srv/kspread_*_export.desktop
%_K4srv/kspread_*_import.desktop
%_K4srv/spreadsheetshape-deferred.desktop
%_K4srv/sheetspart.desktop
%_K4srvtyp/sheets_plugin.desktop
%_K4tmpl/SpreadSheet.*
%_K4tmpl/.source/SpreadSheet.*
%_K4xdg_apps/sheets.desktop
%_K4doc/en/sheets/
%_K4srv/ServiceMenus/kspread_konqi.desktop

%files stage
%doc stage/AUTHORS stage/CHANGES
%_K4bindir/calligrastage
%_K4libdir/libkdeinit4_calligrastage.so
%_K4lib/*stage*.*
%_K4lib/kprvariables.so
%_K4lib/kpr_pageeffect_*.so
%_K4lib/kpr_shapeanimation_*.so
%_K4lib/Filterkpr2odf.so
%_K4lib/powerpointimport.*
%_K4lib/pptximport.*
%_K4apps/stage/
%_K4conf/stagerc
%_K4doc/en/stage/
%_K4srv/kpr*.desktop
%_K4srvtyp/kpr*.desktop
%_K4srvtyp/presentationeventaction.desktop
%_K4srvtyp/scripteventaction.desktop
%_K4tmpl/Presentation.*
%_K4tmpl/.source/Presentation.*
%_K4xdg_apps/*stage.desktop
%_K4srv/Filterkpr2odf.desktop
%_K4srv/stagepart.desktop
%_K4srv/ServiceMenus/kpresenter_konqi.desktop

%files karbon
%_K4bindir/karbon
%_K4conf/karbonrc
%_K4libdir/libkdeinit4_karbon.so
%_K4lib/*karbon*.*
%_K4lib/wmfexport.*
%_K4lib/wmfimport.*
%_K4apps/karbon/
%_K4srv/karbon*
%_K4srvtyp/karbon_module.desktop
%_K4tmpl/Illustration.*
%_K4tmpl/.source/Illustration.*
%_K4xdg_apps/*karbon.desktop
#_K4doc/en/karbon/
%_K4srv/ServiceMenus/karbon_konqi.desktop

%files krita
%doc krita/AUTHORS krita/ChangeLog krita/README
%_K4bindir/krita
%_K4conf/kritarc
%_K4libdir/libkdeinit4_krita.so
%_K4lib/*krita*.*
%_K4apps/krita/
%_K4conf/krita*.knsrc
%_K4srv/krita*.desktop
%_K4srvtyp/krita*.desktop
%_K4xdg_apps/*krita*.desktop
%_K4xdg_mime/krita_ora.xml
%_K4apps/kritaplugins/
%_K4apps/color-schemes/Krita*.colors
%_datadir/color/icc/krita/
%_K4srv/ServiceMenus/krita_konqi.desktop

%files kexi
%doc kexi/CHANGES kexi/README
%_K4apps/kexi/
%_K4bindir/kexi*
%_K4lib/kformdesigner_containers.so
%_K4lib/kformdesigner_kexidbwidgets.so
%_K4lib/kformdesigner_mapbrowser.so
%_K4lib/kformdesigner_stdwidgets.so
%_K4lib/kformdesigner_webbrowser.so
%_K4lib/kexihandler_*.so
%_K4lib/krossmodulekexidb.so
%_K4lib/kexidb_*driver.so
%_K4lib/kexidb_sqlite3_icu.so
%_K4lib/keximigrate_*.so
%_K4lib/kexirelationdesignshape.so
%_K4xdg_apps/*kexi.desktop
%_K4conf/kexirc
%_K4srvtyp/kexi*.desktop
%_K4srv/kexi/
%_K4srv/kexidb_*driver.desktop
%_K4srv/keximigrate_*.desktop
%_K4srv/kformdesigner/kformdesigner_containers.desktop
%_K4srv/kformdesigner/kformdesigner_kexidbfactory.desktop
%_K4srv/kformdesigner/kformdesigner_stdwidgets.desktop
%_K4srv/kformdesigner/kformdesigner_webbrowser.desktop
%_K4doc/en/kexi/
#
%_K4lib/kformdesigner_mapbrowser.so
%_K4srv/kformdesigner/kformdesigner_mapbrowser.desktop

%files flow
%doc flow/AUTHORS flow/CHANGE* flow/NOTES flow/README
%_K4bindir/calligraflow
%_K4libdir/libkdeinit4_calligraflow.so
%_K4lib/*flow*.*
%_K4apps/flow/
#_K4doc/en/flow/
%_K4conf/flow_stencils.knsrc
%_K4srv/flow*.desktop
%_K4xdg_apps/flow.desktop
%_K4conf/flowrc
%_K4srv/ServiceMenus/flow_konqi.desktop
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
%_K4srvtyp/plan_schedulerplugin.desktop
%_K4srv/krossmoduleplan.desktop
%_K4apps/plan/
%_K4apps/planwork/
%_K4cfg/plansettings.kcfg
%_K4cfg/planworksettings.kcfg
%_K4srv/plan*.desktop
%_K4xdg_apps/plan.desktop
%_K4xdg_apps/planwork.desktop

%files words
%_K4bindir/calligrawords
%_K4conf/wordsrc
%_K4libdir/libkdeinit4_calligrawords.so
%_K4lib/wordspart.*
%_K4apps/words/
%_K4tmpl/TextDocument.*
%_K4tmpl/.source/TextDocument.*
%_K4xdg_apps/words.desktop
%_K4srv/ServiceMenus/words_konqi.desktop
%_K4srv/wordspart.desktop
%_K4lib/applixwordimport.*
%_K4lib/asciiimport.so
%_K4lib/docximport.*
%_K4lib/htmlodf_export.*
%_K4lib/mswordodf_import.*
%_K4lib/rtfimport.*
%_K4srv/html-odf_export.desktop
%_K4srv/words_*_import.desktop

%files okular-odp
%_K4lib/okularGenerator_odp.so
%_K4xdg_apps/okularApplication_odp.desktop
%_K4srv/libokularGenerator_odp.desktop
%_K4srv/okularOdp.desktop

%files -n libbraindumpcore%sover_common
%_K4libdir/libbraindumpcore.so.%sover_common
%_K4libdir/libbraindumpcore.so.%sover_common.*
%files -n libcalligrasheetscommon%sover_common
%_K4libdir/libcalligrasheetscommon.so.%sover_common
%_K4libdir/libcalligrasheetscommon.so.%sover_common.*
%files -n libcalligrasheetsodf%sover_common
%_K4libdir/libcalligrasheetsodf.so.%sover_common
%_K4libdir/libcalligrasheetsodf.so.%sover_common.*
%files -n libcalligrastageprivate%sover_common
%_K4libdir/libcalligrastageprivate.so.%sover_common
%_K4libdir/libcalligrastageprivate.so.%sover_common.*
%files -n libchartshapelib%sover_common
%_K4libdir/libchartshapelib.so.%sover_common
%_K4libdir/libchartshapelib.so.%sover_common.*
%files -n libflake%sover_common
%_K4libdir/libflake.so.%sover_common
%_K4libdir/libflake.so.%sover_common.*
%files -n libflowprivate%sover_common
%_K4libdir/libflowprivate.so.%sover_common
%_K4libdir/libflowprivate.so.%sover_common.*
%files -n libkarboncommon%sover_common
%_K4libdir/libkarboncommon.so.%sover_common
%_K4libdir/libkarboncommon.so.%sover_common.*
%files -n libkarbonui%sover_common
%_K4libdir/libkarbonui.so.%sover_common
%_K4libdir/libkarbonui.so.%sover_common.*
%files -n libkdchart%sover_common
%_K4libdir/libkdchart.so.%sover_common
%_K4libdir/libkdchart.so.%sover_common.*
%files -n libkexicore%sover_common
%_K4libdir/libkexicore.so.%sover_common
%_K4libdir/libkexicore.so.%sover_common.*
%files -n libkexidatatable%sover_common
%_K4libdir/libkexidatatable.so.%sover_common
%_K4libdir/libkexidatatable.so.%sover_common.*
%files -n libkexidataviewcommon%sover_common
%_K4libdir/libkexidataviewcommon.so.%sover_common
%_K4libdir/libkexidataviewcommon.so.%sover_common.*
%files -n libkexidb%sover_common
%_K4libdir/libkexidb.so.%sover_common
%_K4libdir/libkexidb.so.%sover_common.*
%files -n libkexiextendedwidgets%sover_common
%_K4libdir/libkexiextendedwidgets.so.%sover_common
%_K4libdir/libkexiextendedwidgets.so.%sover_common.*
%files -n libkexiformutils%sover_common
%_K4libdir/libkexiformutils.so.%sover_common
%_K4libdir/libkexiformutils.so.%sover_common.*
%files -n libkexiguiutils%sover_common
%_K4libdir/libkexiguiutils.so.%sover_common
%_K4libdir/libkexiguiutils.so.%sover_common.*
%files -n libkeximain%sover_common
%_K4libdir/libkeximain.so.%sover_common
%_K4libdir/libkeximain.so.%sover_common.*
%files -n libkeximigrate%sover_common
%_K4libdir/libkeximigrate.so.%sover_common
%_K4libdir/libkeximigrate.so.%sover_common.*
%files -n libkexirelationsview%sover_common
%_K4libdir/libkexirelationsview.so.%sover_common
%_K4libdir/libkexirelationsview.so.%sover_common.*
%files -n libkexiutils%sover_common
%_K4libdir/libkexiutils.so.%sover_common
%_K4libdir/libkexiutils.so.%sover_common.*
%files -n libkformdesigner%sover_common
%_K4libdir/libkformdesigner.so.%sover_common
%_K4libdir/libkformdesigner.so.%sover_common.*
%files -n libkformulalib%sover_common
%_K4libdir/libkformulalib.so.%sover_common
%_K4libdir/libkformulalib.so.%sover_common.*
%files -n libkochart%sover_common
%_K4libdir/libkochart.so.%sover_common
%_K4libdir/libkochart.so.%sover_common.*
%files -n libkokross%sover_common
%_K4libdir/libkokross.so.%sover_common
%_K4libdir/libkokross.so.%sover_common.*
%files -n libkomain%sover_common
%_K4libdir/libkomain.so.%sover_common
%_K4libdir/libkomain.so.%sover_common.*
%files -n libkoodf%sover_common
%_K4libdir/libkoodf.so.%sover_common
%_K4libdir/libkoodf.so.%sover_common.*
%files -n libkopageapp%sover_common
%_K4libdir/libkopageapp.so.%sover_common
%_K4libdir/libkopageapp.so.%sover_common.*
%files -n libkoplugin%sover_common
%_K4libdir/libkoplugin.so.%sover_common
%_K4libdir/libkoplugin.so.%sover_common.*
%files -n libkoproperty%sover_common
%_K4libdir/libkoproperty.so.%sover_common
%_K4libdir/libkoproperty.so.%sover_common.*
%files -n libkoreport%sover_common
%_K4libdir/libkoreport.so.%sover_common
%_K4libdir/libkoreport.so.%sover_common.*
%files -n libkotext%sover_common
%_K4libdir/libkotext.so.%sover_common
%_K4libdir/libkotext.so.%sover_common.*
%files -n libkowidgets%sover_common
%_K4libdir/libkowidgets.so.%sover_common
%_K4libdir/libkowidgets.so.%sover_common.*
%files -n libkowv2%sover_kowv2
%_K4libdir/libkowv2.so.%sover_kowv2
%_K4libdir/libkowv2.so.%sover_kowv2.*
%files -n libkplatokernel%sover_common
%_K4libdir/libkplatokernel.so.%sover_common
%_K4libdir/libkplatokernel.so.%sover_common.*
%files -n libkplatomodels%sover_common
%_K4libdir/libkplatomodels.so.%sover_common
%_K4libdir/libkplatomodels.so.%sover_common.*
%files -n libkplatoui%sover_common
%_K4libdir/libkplatoui.so.%sover_common
%_K4libdir/libkplatoui.so.%sover_common.*
%files -n libkritaimage%sover_common
%_K4libdir/libkritaimage.so.%sover_common
%_K4libdir/libkritaimage.so.%sover_common.*
%files -n libkritalibbrush%sover_common
%_K4libdir/libkritalibbrush.so.%sover_common
%_K4libdir/libkritalibbrush.so.%sover_common.*
%files -n libkritalibpaintop%sover_common
%_K4libdir/libkritalibpaintop.so.%sover_common
%_K4libdir/libkritalibpaintop.so.%sover_common.*
%files -n libkritaui%sover_common
%_K4libdir/libkritaui.so.%sover_common
%_K4libdir/libkritaui.so.%sover_common.*
%files -n libkundo2%sover_common
%_K4libdir/libkundo2.so.%sover_common
%_K4libdir/libkundo2.so.%sover_common.*
%files -n liblibwmf%sover_common
%_K4libdir/liblibwmf.so.%sover_common
%_K4libdir/liblibwmf.so.%sover_common.*
%files -n libmsooxml%sover_common
%_K4libdir/libmsooxml.so.%sover_common
%_K4libdir/libmsooxml.so.%sover_common.*
%files -n libpigmentcms%sover_common
%_K4libdir/libpigmentcms.so.%sover_common
%_K4libdir/libpigmentcms.so.%sover_common.*
%files -n libplanprivate%sover_common
%_K4libdir/libplanprivate.so.%sover_common
%_K4libdir/libplanprivate.so.%sover_common.*
%files -n libplanworkapp%sover_common
%_K4libdir/libplanworkapp.so.%sover_common
%_K4libdir/libplanworkapp.so.%sover_common.*
%files -n libplanworkfactory%sover_common
%_K4libdir/libplanworkfactory.so.%sover_common
%_K4libdir/libplanworkfactory.so.%sover_common.*
%files -n librcps_plan%sover_common
%_K4libdir/librcps_plan.so.%sover_common
%_K4libdir/librcps_plan.so.%sover_common.*
%files -n librtfreader%sover_common
%_K4libdir/libRtfReader.so.%sover_common
%_K4libdir/libRtfReader.so.%sover_common.*
%files -n libtextlayout%sover_common
%_K4libdir/libtextlayout.so.%sover_common
%_K4libdir/libtextlayout.so.%sover_common.*
%files -n libwordsprivate%sover_common
%_K4libdir/libwordsprivate.so.%sover_common
%_K4libdir/libwordsprivate.so.%sover_common.*

%changelog
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
