%define rname marble

%define marblewidget_sover 28
%define libmarblewidget libmarblewidget-qt6_%marblewidget_sover

%{?optflags_lto:%global optflags_lto %optflags_lto -ffat-lto-objects}
%ifarch %qt6_qtwebengine_arches
%def_enable qtwebengine
%else
%def_disable qtwebengine
%endif

Name: %rname
Version: 26.04.2
Release: alt1
%K6init

Group: Education
Summary: A virtual globe and world atlas
Url: http://www.kde.org
License: LGPL-2.1-or-later

Provides:  kde5-marble = %EVR
Obsoletes: kde5-marble < %EVR

Source: %rname-%version.tar
Source2: naturalearth.tar
Patch1: alt-astro-static.patch
Patch2: alt-remove-country-data.patch
Patch3: alt-always-request-Russian-results.patch
Patch4: alt-dont-build-postal-code-plugin.patch
Patch5: alt-remove-address-details.patch

BuildRequires(pre): rpm-build-kf6 rpm-macros-qt6-webengine
BuildRequires: extra-cmake-modules qt6-declarative-devel qt6-positioning-devel qt6-svg-devel qt6-tools-devel qt6-serialport-devel qt6-5compat-devel
BuildRequires: libvulkan-devel
%if_enabled qtwebengine
BuildRequires: qt6-webengine-devel
%endif
BuildRequires: qt6-phonon-devel
#BuildRequires: libwlocate-devel
BuildRequires: libabseil-cpp-devel
BuildRequires: libgps-devel libshape-devel zlib-devel libprotobuf-devel protobuf-compiler
BuildRequires: kf6-kauth-devel kf6-kbookmarks-devel kf6-kcodecs-devel kf6-kcompletion-devel kf6-kconfig-devel
BuildRequires: kf6-kconfigwidgets-devel kf6-kcoreaddons-devel kf6-kcrash-devel kf6-kdoctools kf6-kdoctools-devel
BuildRequires: kf6-ki18n-devel kf6-kio-devel kf6-kitemviews-devel kf6-kjobwidgets-devel kf6-knewstuff-devel kf6-kpackage-devel
BuildRequires: kf6-kparts-devel kf6-krunner-devel kf6-kservice-devel kf6-ktextwidgets-devel kf6-kwallet-devel kf6-kwidgetsaddons-devel
BuildRequires: kf6-kxmlgui-devel kf6-solid-devel kf6-sonnet-devel
BuildRequires: plasma6-lib-devel

%description
Marble is a Virtual Globe and World Atlas that you can use to learn more
about Earth: You can pan and zoom around and you can look up places and
roads. A mouse click on a place label will provide the respective
Wikipedia article.

%package common
Summary: %name common package
Group: System/Configuration/Other
BuildArch: noarch
Requires: kf6-filesystem
Provides:  kde5-marble-common = %EVR
Obsoletes: kde5-marble-common < %EVR
%description common
%name common package

%package devel
Group: Development/KDE and QT
Summary: Development files for %name
%description devel
The %name-devel package contains libraries and header files for
developing applications that use %name.

%package addon-maps
Group: Education
Summary: Additional maps for %name
Requires: %name
Conflicts: kde5-marble < 6
%description addon-maps
Additional maps for %name.

%package -n %libmarblewidget
Group: System/Libraries
Summary: %name library
Requires: %name-common >= %EVR
Obsoletes: libmarblewidget-qt528 < %EVR
%description -n %libmarblewidget
%name library


%prep
%setup -n %rname-%version
rm -fv data/naturalearth/*.pn2
pushd data/
tar -xvf %SOURCE2 naturalearth/
popd
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
sed -i '/add_subdirectory(marble-qt)/d' src/apps/CMakeLists.txt

# disable krunners by default
for f in \
src/plasmarunner/plasma-runner-marble.json
do
    sed -i '/EnabledByDefault/s|true|false|' $f
done

%build
%K6build \
    -DKDE_INSTALL_INCLUDEDIR=%_K6inc \
    -DKDE_INSTALL_CONFDIR=%_K6xdgconf \
    -DBUILD_MARBLE_TOOLS=YES \
    -DBUILD_MARBLE_EXAMPLES=NO \
    -DMARBLE_DATA_PATH=%_K6data/marble \
    -DMARBLE_PRI_INSTALL_USE_QT_SYS_PATHS=YES \
    #


%install
%K6install
%K6install_move data marble config.kcfg icons knsrcfiles

# hide service files
for f in %buildroot/%_K6xdgapp/*_thumbnail_*.desktop ; do
    LC_ALL=en_US.UTF-8 desktop-file-install \
	--dir %buildroot/%_K6xdgapp \
	--set-key="NoDisplay" \
	--set-value="true" \
	$f ||:
done

mv %buildroot/%_K6xdgmime/geo{,-kde6}.xml

if [ "%_desktopdir" != "%_K6xdgapp" ] ;then
    mkdir -p %buildroot/%_K6xdgapp
    mv %buildroot/%_desktopdir/*.desktop %buildroot/%_K6xdgapp/ ||:
fi
if [ "%_includedir" != "%_K6inc" ] ;then
    mkdir -p %buildroot/%_K6inc
    mv %buildroot/%_includedir/marble %buildroot/%_K6inc/ ||:
fi


rm -rf %buildroot/%_datadir/locale/*/LC_MESSAGES/*_qt.qm
rm -rf %buildroot/%_K6i18n/*/LC_MESSAGES/*_qt.qm
%find_lang %name --with-kde --all-name

%files common -f %name.lang
%doc LICENSES/*
%_K6cfg/marble.kcfg
%_K6xdgmime/geo-kde6.xml

%files
#%_K6lib/libmarbledeclarative.so
%_K6bin/marble*
%_K6plug/*marble*.so
%_K6plug/kf6/thumbcreator/*marble*.so
%_K6plug/kf6/krunner/*marble*.so
%_K6data/plasma/plasmoids/org.kde.plasma.worldclock/
%_K6data/plasma//wallpapers/org.kde.plasma.worldmap/
%_K6lib/marble/
%_K6qml/org/kde/marble/
#%_K6srv/*.desktop
%_K6xdgapp/*marble*.desktop
%_K6icon/*/*/apps/*marble*.*
%_K6data/kxmlgui?/marble/
%_datadir/metainfo/*.xml
%_datadir/qlogging-categories?/*.*categories
%_K6data/marble/
%exclude %_K6data/marble/maps/earth/openstreetmap/
%exclude %_K6data/marble/maps/earth/vectorosm/
%exclude %_K6data/marble/maps/earth/political/

%files addon-maps
%_K6data/marble/maps/earth/openstreetmap/
%_K6data/marble/maps/earth/vectorosm/
%_K6data/marble/maps/earth/political/

%files devel
#%_K6plug/designer/*.so
#%_K6inc/astro/
%_K6inc/marble/
%_K6link/lib*.so
%_K6lib/cmake/Marble/
%_K6archdata/mkspecs/modules/qt_Marble.pri

%files -n %libmarblewidget
%_K6lib/libmarblewidget-qt6.so.%marblewidget_sover
%_K6lib/libmarblewidget-qt6.so.*

%changelog
* Tue Jun 09 2026 Sergey V Turchin <zerg@altlinux.org> 26.04.2-alt1
- new version

* Mon May 11 2026 Sergey V Turchin <zerg@altlinux.org> 26.04.1-alt1
- new version

* Mon May 11 2026 Ajrat Makhmutov <rauty@altlinux.org> 25.12.3-alt3
- don't build the postal-code plugin
- always request Russian results
- remove the Address Details context-menu entry

* Wed May 06 2026 Ajrat Makhmutov <rauty@altlinux.org> 25.12.3-alt2
- strip country from reverse-geocoded address

* Tue Mar 10 2026 Sergey V Turchin <zerg@altlinux.org> 25.12.3-alt1
- new version

* Sat Feb 07 2026 Sergey V Turchin <zerg@altlinux.org> 25.12.2-alt1
- new version

* Tue Jan 20 2026 Sergey V Turchin <zerg@altlinux.org> 25.12.1-alt1
- new version

* Wed Oct 22 2025 Sergey V Turchin <zerg@altlinux.org> 25.08.2-alt1
- new version

* Tue Jul 22 2025 Sergey V Turchin <zerg@altlinux.org> 25.04.3-alt1
- new version

* Fri Jun 06 2025 Sergey V Turchin <zerg@altlinux.org> 25.04.1-alt2
- put unappropriave maps to separate package

* Wed May 28 2025 Sergey V Turchin <zerg@altlinux.org> 25.04.1-alt1
- new version

* Mon Feb 24 2025 Sergey V Turchin <zerg@altlinux.org> 24.12.2-alt1
- new version

* Tue Dec 17 2024 Sergey V Turchin <zerg@altlinux.org> 24.11.90-alt2
- hide services from main menu (closes: 52455)

* Fri Dec 06 2024 Sergey V Turchin <zerg@altlinux.org> 24.11.90-alt1
- beta with KF6

* Fri Nov 08 2024 Sergey V Turchin <zerg@altlinux.org> 24.08.2-alt1
- new version

* Tue Feb 20 2024 Sergey V Turchin <zerg@altlinux.org> 23.08.5-alt1
- new version

* Tue Dec 12 2023 Sergey V Turchin <zerg@altlinux.org> 23.08.4-alt1
- new version

* Fri Nov 10 2023 Sergey V Turchin <zerg@altlinux.org> 23.08.3-alt1
- new version

* Thu Oct 26 2023 Sergey V Turchin <zerg@altlinux.org> 23.08.2-alt2
- fix package

* Thu Oct 19 2023 Sergey V Turchin <zerg@altlinux.org> 23.08.2-alt1
- new version

* Fri Jul 14 2023 Sergey V Turchin <zerg@altlinux.org> 23.04.3-alt1
- new version

* Tue Jun 13 2023 Sergey V Turchin <zerg@altlinux.org> 23.04.2-alt1
- new version

* Mon Mar 06 2023 Sergey V Turchin <zerg@altlinux.org> 22.12.3-alt1
- new version

* Fri Feb 03 2023 Sergey V Turchin <zerg@altlinux.org> 22.12.2-alt1
- new version

* Mon Jan 23 2023 Oleg Solovyov <mcpain@altlinux.org> 22.12.1-alt2
- remove country info from:
  + search results
  + search autocompletion

* Thu Jan 19 2023 Sergey V Turchin <zerg@altlinux.org> 22.12.1-alt1
- new version

* Mon Jan 09 2023 Oleg Solovyov <mcpain@altlinux.org> 22.08.3-alt2
- remove political map and country boundaries

* Mon Nov 07 2022 Sergey V Turchin <zerg@altlinux.org> 22.08.3-alt1
- new version

* Tue Oct 18 2022 Sergey V Turchin <zerg@altlinux.org> 22.08.2-alt1
- new version

* Wed Sep 21 2022 Sergey V Turchin <zerg@altlinux.org> 22.08.1-alt1
- new version

* Tue Jul 12 2022 Sergey V Turchin <zerg@altlinux.org> 22.04.3-alt1
- new version

* Fri Jun 10 2022 Sergey V Turchin <zerg@altlinux.org> 22.04.2-alt1
- new version

* Mon May 23 2022 Sergey V Turchin <zerg@altlinux.org> 22.04.1-alt1
- new version

* Sat Mar 05 2022 Sergey V Turchin <zerg@altlinux.org> 21.12.3-alt1
- new version

* Tue Feb 01 2022 Sergey V Turchin <zerg@altlinux.org> 21.12.1-alt2
- build without qtwebengine on e2k and ppc64le

* Tue Jan 18 2022 Sergey V Turchin <zerg@altlinux.org> 21.12.1-alt1
- new version

* Mon Nov 08 2021 Sergey V Turchin <zerg@altlinux.org> 21.08.3-alt1
- new version

* Fri Oct 08 2021 Sergey V Turchin <zerg@altlinux.org> 21.08.2-alt1
- new version

* Mon Sep 06 2021 Sergey V Turchin <zerg@altlinux.org> 21.08.1-alt1
- new version

* Fri Aug 27 2021 Sergey V Turchin <zerg@altlinux.org> 21.08.0-alt1
- new version

* Thu Jul 15 2021 Sergey V Turchin <zerg@altlinux.org> 21.04.3-alt2
- fix package service files

* Fri Jul 09 2021 Sergey V Turchin <zerg@altlinux.org> 21.04.3-alt1
- new version

* Tue May 25 2021 Sergey V Turchin <zerg@altlinux.org> 21.04.1-alt1
- new version

* Fri Mar 12 2021 Sergey V Turchin <zerg@altlinux.org> 20.12.3-alt1
- new version

* Wed Feb 17 2021 Sergey V Turchin <zerg@altlinux.org> 20.12.2-alt1
- new version

* Tue Dec 22 2020 Sergey V Turchin <zerg@altlinux.org> 20.12.0-alt1
- new version

* Wed Nov 25 2020 Sergey V Turchin <zerg@altlinux.org> 20.08.3-alt1
- new version

* Thu Oct 15 2020 Sergey V Turchin <zerg@altlinux.org> 20.08.2-alt1
- new version

* Wed Sep 23 2020 Sergey V Turchin <zerg@altlinux.org> 20.08.1-alt1
- new version

* Wed Aug 19 2020 Sergey V Turchin <zerg@altlinux.org> 20.04.3-alt1
- new version

* Thu Apr 02 2020 Sergey V Turchin <zerg@altlinux.org> 19.12.3-alt2
- disable krunner plugin by default

* Fri Mar 13 2020 Sergey V Turchin <zerg@altlinux.org> 19.12.3-alt1
- new version

* Thu Jan 23 2020 Sergey V Turchin <zerg@altlinux.org> 19.12.1-alt1
- new version

* Thu Jan 16 2020 Oleg Solovyov <mcpain@altlinux.org> 19.08.0-alt3
- fix build with gpsd>=3.20

* Thu Dec 05 2019 Oleg Solovyov <mcpain@altlinux.org> 19.08.0-alt2
- restore russian Crimea on maps (Closes: #33527)

* Thu Aug 29 2019 Sergey V Turchin <zerg@altlinux.org> 19.08.0-alt1
- new version

* Fri Jul 19 2019 Sergey V Turchin <zerg@altlinux.org> 19.04.3-alt1
- new version

* Thu Jun 06 2019 Sergey V Turchin <zerg@altlinux.org> 19.04.1-alt1
- new version

* Wed May 08 2019 Sergey V Turchin <zerg@altlinux.org> 19.04.0-alt1
- new version

* Thu Mar 21 2019 Sergey V Turchin <zerg@altlinux.org> 18.12.3-alt1
- new version

* Thu Feb 28 2019 Sergey V Turchin <zerg@altlinux.org> 18.12.2-alt2
- build with qtwebengine

* Thu Feb 28 2019 Sergey V Turchin <zerg@altlinux.org> 18.12.2-alt1
- new version

* Thu Jul 26 2018 Sergey V Turchin <zerg@altlinux.org> 18.04.3-alt1
- new version

* Thu Jul 05 2018 Sergey V Turchin <zerg@altlinux.org> 18.04.2-alt1
- new version

* Wed May 30 2018 Sergey V Turchin <zerg@altlinux.org> 18.04.1-alt2
- build without qtwebkit

* Fri May 25 2018 Sergey V Turchin <zerg@altlinux.org> 18.04.1-alt1
- new version

* Mon May 14 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 17.12.3-alt2
- NMU: rebuilt with new libshape.

* Tue Mar 13 2018 Sergey V Turchin <zerg@altlinux.org> 17.12.3-alt1
- new version

* Tue Nov 14 2017 Sergey V Turchin <zerg@altlinux.org> 17.08.3-alt1
- new version

* Thu Aug 31 2017 Sergey V Turchin <zerg@altlinux.org> 17.04.3-alt1
- new version

* Thu Aug 31 2017 Oleg Solovyov <mcpain@altlinux.org> 17.04.2-alt2
- fix political map

* Thu Jun 15 2017 Sergey V Turchin <zerg@altlinux.org> 17.04.2-alt1
- new version

* Wed Jun 07 2017 Sergey V Turchin <zerg@altlinux.org> 17.04.1-alt1
- new version

* Mon Jun 05 2017 Sergey V Turchin <zerg@altlinux.org> 16.12.3-alt2
- clean maps

* Thu Apr 06 2017 Sergey V Turchin <zerg@altlinux.org> 16.12.3-alt1
- new version

* Thu Sep 22 2016 Sergey V Turchin <zerg@altlinux.org> 16.08.1-alt1
- new version

* Mon Jul 04 2016 Sergey V Turchin <zerg@altlinux.org> 16.04.2-alt1
- new version

* Thu May 12 2016 Sergey V Turchin <zerg@altlinux.org> 16.04.1-alt1
- new version

* Thu Mar 17 2016 Sergey V Turchin <zerg@altlinux.org> 15.12.2-alt1
- initial build
