%define nameL org.kde.kgeotag

Name: kgeotag
Version: 2.0.0
Release: alt1

Summary: Photo geotagging program
License: CC0-1.0 and BSD-2-Clause and BSD-3-Clause and GPL-3.0-only and CC-BY-SA-4.0 and ODbL-1.0
Group: Graphics

Url: https://kgeotag.kde.org
Vcs: https://invent.kde.org/graphics/kgeotag

ExcludeArch: i586

Source: %name-%version.tar

Patch0: GeoDataModel-1.8.0-alt-build.patch
Patch1: MapWidget-1.8.0-alt-build.patch
Patch2: TracksLayer-1.8.0-alt-build.patch
Patch3: MapWidgetcpp-1.8.0-alt-build.patch
Patch4: ImagesLayer-1.8.0-alt-build.patch
Patch5: SearchPlacesWidget-2.0.0-alt-build.patch

Requires: marble

BuildRequires(pre): rpm-macros-cmake
BuildRequires: cmake clang libstdc++-devel extra-cmake-modules qt6-base-devel
BuildRequires: kf6-kcoreaddons-devel kf6-ki18n-devel kf6-kxmlgui-devel
BuildRequires: kf6-kconfigwidgets-devel kf6-kcrash-devel kf6-kdoctools-devel
BuildRequires: qt6-declarative-devel kf6-kcolorscheme-devel kde6-libkexiv2-devel
BuildRequires: marble-devel qt6-5compat-devel qt6-webengine-devel

%description
%summary

%package docs
Summary: %name docs package
Group: Documentation
ExcludeArch: i586
Requires: %name = %EVR
%description docs
%name docs package

%package addon-maps
Summary: %name addon-maps
Group: Graphics
ExcludeArch: i586
Requires: %name = %EVR
Requires: marble-addon-maps
%description addon-maps
%name addon maps package

%prep
%setup

%autopatch -p0
subst 's|<marble/LayerInterface.h>|<KF6/marble/LayerInterface.h>|' src/ImagesLayer.h
subst 's|<marble/GeoDataCoordinates.h>|<KF6/marble/GeoDataCoordinates.h>|' src/GpxEngine.cpp
subst 's|<marble/GeoPainter.h>|<KF6/marble/GeoPainter.h>|' src/TracksLayer.cpp
subst 's|<marble/GeoDataCoordinates.h>|<KF6/marble/GeoDataCoordinates.h>|' src/GeoDataModel.cpp

%build
export CC=clang
export CXX=clang++
%cmake \
        -DBUILD_WITH_QT6=ON \
        -DINCLUDE_INSTALL_DIR:PATH=/usr/include
%cmake_build

%install
%cmake_install

%find_lang %name --with-kde --all-name

%files -f %name.lang
%doc *.md LICENSES
%_bindir/%name
%_datadir/applications/%nameL.desktop
%_iconsdir/hicolor/*/apps/%name.png
%_datadir/%name
%_datadir/metainfo/%nameL.appdata.xml
%exclude %_datadir/doc/HTML

%files docs
%_defaultdocdir/HTML/*/%name

%files addon-maps

%changelog
* Sat Mar 14 2026 Aleksandr Shamaraev <shad@altlinux.org> 2.0.0-alt1
- 1.8.0 -> 2.0.0

* Sat Nov 22 2025 Aleksandr Shamaraev <shad@altlinux.org> 1.8.0-alt4
- added: subpackage with unappropriave maps

* Sat Aug 02 2025 Aleksandr Shamaraev <shad@altlinux.org> 1.8.0-alt3
- Group changed.

* Mon Jul 28 2025 Aleksandr Shamaraev <shad@altlinux.org> 1.8.0-alt2
- Fix Url in spec.

* Fri Jun 06 2025 Aleksandr Shamaraev <shad@altlinux.org> 1.8.0-alt1
- Initial build for ALT Linux.
