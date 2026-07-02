
%define rname calligra

%add_findreq_skiplist %_K6xdgapp/*/scripts/*/*.py
%add_findreq_skiplist %_K6xdgapp/*/scripts/*/*.rb

%define sover_gen 41
%define libname lib%name
%define libkookulargenerator_odp libkookulargenerator_odp%sover_gen
%define libkookulargenerator_odt libkookulargenerator_odt%sover_gen

Name: %rname
Version: 26.04.3
Release: alt1
#Epoch: 0
%K6init no_altplace

Group: Office
Summary: An integrated office suite
Url: http://www.calligra-suite.org/
License: GFDL-1.2-only AND GPL-2.0-or-later AND LGPL-2.1-or-later

ExcludeArch: %ix86

#Requires: %name-gemini
Requires: %name-words
Requires: %name-sheets
Requires: %name-stage
Requires: %name-karbon
Requires: %name-okular-generators

Source: http://download.kde.org/stable/calligra/%version/calligra-%version.tar
# upstream
# FC
Patch31: calligra-gcc11.patch
# SuSE
# ALT
Patch102: alt-find-ooo-sdk.patch
Patch103: alt-disable-products.patch
Patch104: alt-fix-saving-diff-formats.patch

BuildRequires(pre): rpm-build-kf6 rpm-macros-qt6-webengine
BuildRequires: kf6-attica-devel boost-devel eigen3 glib2-devel rpm-build-python3
BuildRequires: extra-cmake-modules
BuildRequires: libvulkan-devel libssl-devel libcups-devel
BuildRequires: qt6-svg-devel qt6-declarative-devel
%ifarch %qt6_qtwebengine_arches
BuildRequires: qt6-webengine-devel
%endif
BuildRequires: libqtkeychain-qt6-devel
BuildRequires: kf6-attica-devel kf6-kholidays-devel
BuildRequires: kf6-karchive-devel kf6-kcodecs-devel kf6-kcompletion-devel kf6-kconfig-devel kf6-kconfigwidgets-devel
BuildRequires: kf6-kcoreaddons-devel kf6-kdbusaddons-devel kf6-kdoctools-devel kf6-kguiaddons-devel kf6-ki18n-devel
BuildRequires: kf6-kiconthemes-devel kf6-kitemviews-devel kf6-kjobwidgets-devel kf6-kcmutils-devel
BuildRequires: kf6-kio-devel kf6-knotifications-devel kf6-knotifyconfig-devel kf6-kparts-devel kf6-sonnet-devel
BuildRequires: kf6-ktextwidgets-devel kf6-threadweaver-devel kf6-kwallet-devel kf6-kwidgetsaddons-devel kf6-kwindowsystem-devel kf6-kxmlgui-devel
BuildRequires: kf6-kcontacts-devel
BuildRequires: qt6-phonon-devel libqca-qt6-devel libpoppler-qt6-devel
BuildRequires: libexiv2-devel libfftw3-devel libfreetds-devel libGLEW-devel libgsl-devel libicu-devel libjpeg-devel libopenjpeg2.0-devel libtiff-devel pstoedit
BuildRequires: liblcms2-devel libmysqlclient-devel
BuildRequires: libsqlite3-devel sqlite3 libxbase-devel openexr-devel postgresql-devel
BuildRequires: libvisio-devel libwpg-devel libwpd10-devel libwps-devel libodfgen-devel libetonyek-devel libxml2-devel
BuildRequires: libdrm-devel libpng-devel libexpat-devel libspnav-devel
BuildRequires: plasma6-activities-devel
BuildRequires: kde6-kdiagram-devel
#BuildRequires: kf6-kreport-devel kf6-kproperty-devel
#BuildRequires: marble-devel
BuildRequires: kf6-kcalendarcore-devel akonadi-devel akonadi-contacts-devel
BuildRequires: okular-devel
#BuildRequires: LibreOffice-still-sdk
BuildRequires: fontconfig-devel libfreetype-devel

%description
%summary.

%package common
Summary: %name common package
Group: System/Configuration/Other
BuildArch: noarch
Requires: kf6-filesystem
%description common
%name common package

%package core
Group: System/Libraries
Summary: Core support files for %name
Requires: fonts-ttf-latex-xft
%description core
%summary.

%package devel
Group: Development/KDE and QT
Summary: Header files and libraries needed for %name development
Conflicts: libflake-devel
%description devel
Header files and libraries needed for %name development

%package words
Group: Office
Summary: An intuitive word processor application with desktop publishing features
Provides: kword = %version-%release
Requires: %name-core
%description words
KWord is an intuitive word processor and desktop publisher application.
With it, you can create informative and attractive documents with
pleasure and ease.

%package sheets
Group: Office
Summary: A fully-featured spreadsheet application
Provides: %name-tables = %EVR
Requires: %name-core
%description sheets
Tables is a fully-featured calculation and spreadsheet tool.  Use it to
quickly create and calculate various business-related spreadsheets, such
as income and expenditure, employee working hours...

%package stage
Group: Office
Summary: A full-featured presentation program
Requires: %name-core
%description stage
Stage is a powerful and easy to use presentation application. You
can dazzle your audience with stunning slides containing images, videos,
animation and more.

%package karbon
Group: Graphics
Summary: A vector drawing application
Provides: karbon = %version-%release
Requires: %name-core
Requires: pstoedit
%description karbon
Karbon is a vector drawing application with an user interface that is
easy to use, highly customizable and extensible. That makes Karbon a
great application for users starting to explore the world of vector
graphics as well as for artists wanting to create breathtaking vector
art.

Whether you want to create clipart, logos, illustrations or photorealistic
vector images - look no further, Karbon is the tool for you!

%package gemini
Group: Office
Summary: Office Suite
Requires: %name-core
%description gemini
The KDE Office suite for 2-in-1 devices.

%package  okular-generators
Group: Office
Summary:  OpenDocument text and presenter support for okular
#Requires: %name-stage
Requires: okular-core
Requires: %libkookulargenerator_odp >= %version
Requires: %libkookulargenerator_odt >= %version
Provides: calligra-okular-odp = %EVR
Obsoletes: calligra-okular-odp < %EVR
Provides: calligra-okular-odf = %EVR
Obsoletes: calligra-okular-odf < %EVR
%description okular-generators
%summary.

%package -n %libname
Summary: %name libraries
Group: System/Libraries
Requires: %name-common >= %EVR
%description -n %libname
%name libraries

%package -n %libkookulargenerator_odp
Summary: %name library
Group: System/Libraries
Requires: %name-common >= %EVR
Conflicts: calligra-okular-generators < 20
%description -n %libkookulargenerator_odp
%name library

%package -n %libkookulargenerator_odt
Summary: %name library
Group: System/Libraries
Requires: %name-common >= %EVR
Conflicts: calligra-okular-generators < 20
%description -n %libkookulargenerator_odt
%name library

%prep
%setup
#
%patch31 -p1
#
%patch102 -p1
%patch103 -p1
%patch104 -p1

# fix docs names
for subd in po/*/docs/{sheets,stage} ; do
    base_subd=`basename $subd`
    dir_subd=`dirname $subd`
    case "$base_subd" in
	sheets)
	    mv $subd $dir_subd/calligrasheets
	    ;;
	stage)
	    mv $subd $dir_subd/calligrastage
	    ;;
	*)
	    ;;
    esac
done

# remove duplicate templates
pushd words/templates/Wordprocessing >/dev/null
ls | grep -E ".A4" | xargs -I {} \
    echo 'sed -i "s|{}||" CMakeLists.txt; rm -f {}' | sh
popd >/dev/null

#subst "s|VERSION 3.16|VERSION 3.5|" CMakeLists.txt
#subst "s|cmake_policy(SET CMP0022 OLD)||" CMakeLists.txt

%build
%K6cmake \
    -DRELEASE_BUILD=ON \
    -DCMAKE_CXX_FLAGS="-DKDE_NO_DEBUG_OUTPUT" \
    -DCALLIGRA_SHOULD_BUILD_PRODUCTS=ALL \
    -DPACKAGERS_BUILD=OFF \
    -DBUILD_TESTING=OFF \
    -DTEMPLATES_INSTALL_DIR:PATH=%_K6tmpl \
    #
%K6make

%install
%K6install

## unpackaged files
rm -fv %buildroot%_datadir/mime/packages/{krita_ora,x-iwork-keynote-sffkey}.xml
rm -frv %buildroot/%_datadir/locale/x-test/

# remove InitialPreference
for f in %buildroot/%_K6xdgapp/*.desktop ; do
    sed -i '/^InitialPreference=/d' $f
done

%find_lang --with-kde --all-name %name

%files
%files common -f %name.lang
%doc AUTHORS README.md

%files devel
#%_K6bin/cstester
#%_K6bin/cstrunner
#%_K6bin/visualimagecompare
%_K6link/lib*.so

%files core
%dir %_K6plug/calligra/
%dir %_K6plug/calligra/colorspaces/
%dir %_K6plug/calligra/dockers/
%dir %_K6plug/calligra/formatfilters/
%dir %_K6plug/calligra/pageapptools/
%dir %_K6plug/calligra/shapefiltereffects/
%dir %_K6plug/calligra/shapes/
%dir %_K6plug/calligra/tools/
%dir %_K6plug/calligra/textediting/
%dir %_K6plug/calligra/textinlineobjects/
%_K6bin/calligralauncher
%_K6bin/calligraconverter
#%_K6qml/
%_K6data/calligra/
%_K6data/calligra_shape_music/fonts/Emmentaler-14.ttf
%_K6data/color/icc/calligra/
%_K6plug/calligra/textediting/calligra_textediting_autocorrect.so
%_K6plug/calligra/tools/calligra_tool_basicflakes.so
%_K6plug/calligra/textediting/calligra_textediting_changecase.so
%_K6plug/calligra/tools/calligra_tool_defaults.so
%_K6plug/calligra/dockers/calligra_docker_defaults.so
%_K6plug/calligra/dockers/calligra_docker_stencils.so
%_K6plug/kf6/thumbcreator/calligrathumbnail.so
%_K6plug/kf6/propertiesdialog/calligradocinfopropspage.so
%_K6plug/calligra/pageapptools/kopabackgroundtool.so
%_K6plug/calligra/colorspaces/kolcmsengine.so
%_K6plug/calligra/formatfilters/calligra_filter_eps2svgai.so
%_K6plug/calligra/formatfilters/calligra_filter_pdf2svg.so
%_K6plug/calligra/formatfilters/calligra_filter_kpr2odp.so
%_K6plug/calligra/formatfilters/calligra_filter_vsdx2odg.so
%_K6plug/calligra/textediting/calligra_textediting_spellcheck.so
%_K6plug/calligra/textinlineobjects/calligra_textinlineobject_variables.so
%_K6plug/calligra/textediting/calligra_textediting_thesaurus.so
%ifarch %qt6_qtwebengine_arches
%_K6plug/calligra/shapes/braindump_shape_web.so
%endif
%_K6plug/calligra/shapes/calligra_shape_artistictext.so
%_K6plug/calligra/shapes/calligra_shape_chart.so
%_K6plug/calligra/shapes/calligra_shape_formula.so
%_K6plug/calligra/shapes/calligra_shape_music.so
%_K6plug/calligra/shapes/calligra_shape_picture.so
%_K6plug/calligra/shapes/calligra_shape_plugin.so
%_K6plug/calligra/shapes/calligra_shape_text.so
%_K6plug/calligra/shapes/calligra_shape_vector.so
%_K6plug/calligra/shapes/calligra_shape_video.so
%_K6plug/calligra/shapes/calligra_shape_threed.so
%_K6plug/calligra/shapefiltereffects/calligra_filtereffects.so
%_K6plug/kf6/thumbcreator/calligraimagethumbnail.so
%_K6xdgapp/calligra.desktop
%_K6xdgapp/org.kde.calligra.desktop
%_K6xdgmime/calligra_svm.xml
%_K6icon/*/*/*/*
#%_K6srv/calligra_odg_thumbnail.desktop
#%_K6srv/calligradocinfopropspage.desktop
#%_K6srv/flow_vsdx_thumbnail.desktop
#%_K6srv/flow_wpg_thumbnail.desktop
%_K6plug/calligra/shapes/calligra_shape_paths.so
%_datadir/metainfo/org.kde.calligra.metainfo.xml

#%files gemini
#%_K6bin/calligragemini
#%_K6bin/calligrageminithumbnailhelper
#%_K6xdgapp/org.kde.calligra.gemini.desktop
#%_K6data/calligragemini/
#%_datadir/metainfo/org.kde.calligra.gemini.metainfo.xml

%files sheets
%config(noreplace) %_K6xdgconf/calligrasheetsrc
%_K6bin/calligrasheets
%_K6plug/calligra/*/calligrasheets*.so
%_K6plug/calligrasheets/*/kspread*module.so
%_K6plug/calligra/formatfilters/calligra_filter_*sheets*.so
%_K6plug/calligra/formatfilters/calligra_filter_*kspread*.so
%_K6plug/calligra/formatfilters/calligra_filter_xls*.so
%_K6plug/calligrasheets/extensions/sheetssolver.so
%_K6data/calligrasheets/
%_K6data/kxmlgui?/calligrasheets/
#%_K6srv/sheets_*_thumbnail.desktop
%_K6data/kio/servicemenus/sheets_*.desktop
%_K6cfg/calligrasheets.kcfg
%_K6tmpl/SpreadSheet.*
%_K6tmpl/.source/SpreadSheet.*
%_K6xdgapp/org.kde.calligra.sheets.desktop
%_datadir/metainfo/org.kde.calligra.sheets.metainfo.xml

%files stage
%config(noreplace) %_K6xdgconf/calligrastagerc
%doc stage/AUTHORS stage/CHANGES
%_K6bin/calligrastage
%_K6plug/calligra/*/*stage*.*
%_K6plug/calligra/textinlineobjects/kprvariables.so
%_K6plug/calligrastage/pageeffects/kpr_pageeffect_*.so
%_K6plug/calligrastage/shapeanimations/kpr_shapeanimation_*.so
%_K6plug/calligra/formatfilters/calligra_filter_ppt2odp.so
%_K6plug/calligra/formatfilters/calligra_filter_pptx2odp.so
%_K6plug/calligra/formatfilters/calligra_filter_key2odp.so
%_K6plug/calligrastage/tools/calligrastagetoolanimation.so
%_K6xdgapp/org.kde.calligra.stage.desktop
%_K6data/calligrastage/
%_K6data/kxmlgui?/calligrastage/
%_K6tmpl/Presentation.*
%_K6tmpl/.source/Presentation.*
#%_K6srv/stage_*_thumbnail.desktop
%_K6data/kio/servicemenus/stage_*.desktop
%_datadir/metainfo/org.kde.calligra.stage.metainfo.xml

%files karbon
%config(noreplace) %_K6xdgconf/karbonrc
%_K6bin/karbon
%_K6plug/karbon/extensions/*karbon*.*
%_K6plug/calligra/formatfilters/calligra_filter_wmf2svg.so
%_K6plug/calligra/formatfilters/calligra_filter_xfig2odg.so
%_K6plug/calligra/formatfilters/calligra_filter_karbon1x2karbon.so
%_K6plug/calligra/formatfilters/calligra_filter_karbon2image.so
%_K6plug/calligra/formatfilters/calligra_filter_karbon2svg.so
%_K6plug/calligra/formatfilters/calligra_filter_karbon2wmf.so
%_K6plug/calligra/formatfilters/calligra_filter_svg2karbon.so
%_K6plug/calligra/formatfilters/calligra_filter_pdf2odg.so
%_K6plug/calligra/parts/karbonpart.so
%_K6plug/calligra/tools/karbon_tools.so
%_K6data/karbon/
%_K6data/kxmlgui?/karbon/
#%_K6srv/karbon_*_thumbnail.desktop
%_K6tmpl/Illustration.*
%_K6tmpl/.source/Illustration.*
%_K6xdgapp/org.kde.calligra.karbon.desktop
%_K6data/kio/servicemenus/karbon_*.desktop
%_datadir/metainfo/org.kde.calligra.karbon.metainfo.xml

%files words
%config(noreplace) %_K6xdgconf/calligrawordsrc
%_K6bin/calligrawords
%_K6plug/calligra/parts/calligrawordspart.so
%_K6data/calligrawords/
%_K6data/kxmlgui?/calligrawords/
%_K6tmpl/TextDocument.*
%_K6tmpl/.source/TextDocument.*
%_K6xdgapp/org.kde.calligra.words.desktop
%_K6xdgapp/org.kde.calligrawords_ascii.desktop
%_K6plug/calligra/formatfilters/calligra_filter_applixword2odt.so
%_K6plug/calligra/formatfilters/calligra_filter_ascii2words.so
%_K6plug/calligra/formatfilters/calligra_filter_doc2odt.so
%_K6plug/calligra/formatfilters/calligra_filter_docx2odt.so
%_K6plug/calligra/formatfilters/calligra_filter_html2ods.so
%_K6plug/calligra/formatfilters/calligra_filter_odt2ascii.so
%_K6plug/calligra/formatfilters/calligra_filter_odt2epub2.so
%_K6plug/calligra/formatfilters/calligra_filter_odt2html.so
%_K6plug/calligra/formatfilters/calligra_filter_odt2mobi.so
%_K6plug/calligra/formatfilters/calligra_filter_rtf2odt.so
%_K6plug/calligra/formatfilters/calligra_filter_wpd2odt.so
%_K6plug/calligra/formatfilters/calligra_filter_wpg2svg.so
%_K6plug/calligra/formatfilters/calligra_filter_wpg2odg.so
%_K6plug/calligra/formatfilters/calligra_filter_wps2odt.so
%_K6plug/calligra/formatfilters/calligra_filter_odt2docx.so
%_K6plug/calligra/formatfilters/calligra_filter_odt2wiki.so
#%_K6srv/words_*_thumbnail.desktop
%_K6data/kio/servicemenus/words_*.desktop
%_K6xdgmime/wiki-format.xml
%_datadir/metainfo/org.kde.calligra.words.metainfo.xml

%files okular-generators
%_K6plug/okular_generators/okularGenerator_*_calligra.so
%_K6xdgapp/okularApplication_*_calligra.desktop
#%_K6srv/okular*_calligra.desktop

%files -n %libname
%_K6lib/lib*.so.*
%exclude %_K6lib/libkookularGenerator_odp.so*
%exclude %_K6lib/libkookularGenerator_odt.so*
%files -n %libkookulargenerator_odp
%_K6lib/libkookularGenerator_odp.so.%sover_gen
%_K6lib/libkookularGenerator_odp.so.*
%files -n %libkookulargenerator_odt
%_K6lib/libkookularGenerator_odt.so.%sover_gen
%_K6lib/libkookularGenerator_odt.so.*

%changelog
* Thu Jul 02 2026 Sergey V Turchin <zerg@altlinux.org> 26.04.3-alt1
- new version

* Wed May 20 2026 Dmitrii Fomchenkov <sirius@altlinux.org> 25.12.3-alt2
- fix saving created spreadsheet in different formats (closes: 49363)

* Mon Mar 16 2026 Sergey V Turchin <zerg@altlinux.org> 25.12.3-alt1
- new version

* Tue Nov 11 2025 Sergey V Turchin <zerg@altlinux.org> 25.08.3-alt1
- new version

* Wed Oct 22 2025 Sergey V Turchin <zerg@altlinux.org> 25.08.2-alt1
- new version

* Wed Sep 10 2025 Sergey V Turchin <zerg@altlinux.org> 25.04.3-alt1
- new version (closes: 55858)

* Thu Jul 03 2025 Aleksandr Shamaraev <shad@altlinux.org> 4.0.1-alt3
- NMU: Fix build with Qt 6.9

* Thu Apr 17 2025 Aleksandr Shamaraev <shad@altlinux.org> 4.0.1-alt2.1
- NMU:
  + fixed FTBFS

* Wed Feb 19 2025 Sergey V Turchin <zerg@altlinux.org> 4.0.1-alt2
- update build requires

* Tue Nov 26 2024 Sergey V Turchin <zerg@altlinux.org> 4.0.1-alt1
- new version

* Fri Jun 07 2024 Dmitrii Fomchenkov <sirius@altlinux.org> 0:3.2.1-alt7
- fix a crach when duplicating the bibliography (closes: 42875)
- remove duplicate templates (closes: 42876)

* Fri Aug 04 2023 Sergey V Turchin <zerg@altlinux.org> 0:3.2.1-alt6
- fix to show translated docs

* Thu Feb 02 2023 Sergey V Turchin <zerg@altlinux.org> 0:3.2.1-alt5
- add fix for new poppler

* Fri Apr 01 2022 Sergey V Turchin <zerg@altlinux.org> 0:3.2.1-alt4
- fix to build with new poppler
- add upstream fixes

* Mon Jul 19 2021 Sergey V Turchin <zerg@altlinux.org> 0:3.2.1-alt3
- fix to build with new cmake

* Mon Dec 07 2020 Sergey V Turchin <zerg@altlinux.org> 0:3.2.1-alt2
- clean build requries (closes: 39382)

* Wed Aug 26 2020 Sergey V Turchin <zerg@altlinux.org> 0:3.2.1-alt1
- new version

* Fri Jan 17 2020 Sergey V Turchin <zerg@altlinux.org> 0:3.1.0-alt10
- fix compile with new Poppler

* Wed Sep 18 2019 Sergey V Turchin <zerg@altlinux.org> 0:3.1.0-alt9
- fix compile with new Qt

* Thu Jul 04 2019 Sergey V Turchin <zerg@altlinux.org> 0:3.1.0-alt8
- set additional provides (ALT#16944)
- build without qtwebkit

* Sat Jun 22 2019 Igor Vlasenko <viy@altlinux.ru> 0:3.1.0-alt7
- NMU: remove rpm-build-ubt from BR:

* Mon Feb 18 2019 Sergey V Turchin <zerg@altlinux.org> 0:3.1.0-alt6
- fix build with poppler-0.72

* Thu Nov 08 2018 Sergey V Turchin <zerg@altlinux.org> 0:3.1.0-alt5
- fix build with poppler-0.71

* Tue Sep 11 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 0:3.1.0-alt4
- Fixed build with new Qt.

* Fri May 25 2018 Sergey V Turchin <zerg@altlinux.org> 0:3.1.0-alt3
- rebuild with new okular

* Tue Mar 13 2018 Sergey V Turchin <zerg@altlinux.org> 0:3.1.0-alt2
- rebuild with new okular

* Thu Mar 01 2018 Sergey V Turchin <zerg@altlinux.org> 0:3.1.0-alt1
- new version

* Tue Oct 31 2017 Sergey V Turchin <zerg@altlinux.org> 0:3.0.1-alt2
- move binaries to /usr/bin

* Wed Aug 30 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 0:3.0.1-alt1
- Updated to upstream version 3.0.1.

* Fri Apr 08 2016 Sergey V Turchin <zerg@altlinux.org> 0:2.9.11-alt2
- rebuild with new poppler

* Thu Feb 11 2016 Sergey V Turchin <zerg@altlinux.org> 0:2.9.11-alt1
- new version

* Tue Jan 19 2016 Sergey V Turchin <zerg@altlinux.org> 0:2.9.10-alt3
- remove InitialPreference from desktop-files

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
