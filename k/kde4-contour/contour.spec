%define _kde_alternate_placement 1

%define rname contour
Name: kde4-contour
Version: 0.1.2
Release: alt1

Group: Graphical desktop/KDE
Summary: Contour data server
License: GPLv2.1 / GPLv3
Url: http://kde.org/

Requires: qt4-mobility

Source: %rname-%version.tar
Source1: FindQtMobility.cmake

# Automatically added by buildreq on Wed Feb 08 2012 (-bi)
# optimized out: automoc cmake cmake-modules elfutils fontconfig fontconfig-devel glibc-devel-static kde-common-devel kde4-kactivities-devel kde4base-runtime-core kde4libs kde4libs-devel libICE-devel libSM-devel libX11-devel libXScrnSaver-devel libXau-devel libXcomposite-devel libXcursor-devel libXdamage-devel libXdmcp-devel libXext-devel libXfixes-devel libXft-devel libXi-devel libXinerama-devel libXpm-devel libXrandr-devel libXrender-devel libXt-devel libXtst-devel libXv-devel libXxf86misc-devel libXxf86vm-devel libdbus-devel libdbusmenu-qt2 libfreetype-devel libgst-plugins libpng-devel libqt4-contacts libqt4-core libqt4-dbus libqt4-declarative libqt4-devel libqt4-gui libqt4-location libqt4-network libqt4-opengl libqt4-script libqt4-sensors libqt4-sql libqt4-svg libqt4-uitools libqt4-webkit libqt4-xml libqt4-xmlpatterns libsoprano-devel libssl-devel libstdc++-devel libxkbfile-devel phonon-devel pkg-config python-base rpm-build-gir ruby shared-desktop-ontologies shared-desktop-ontologies-devel soprano-backend-redland soprano-backend-virtuoso xorg-kbproto-devel xorg-xf86miscproto-devel xorg-xproto-devel zlib-devel
#BuildRequires: gcc-c++ glib2-devel kde4base-workspace-devel libicu libqt3-devel python-module-distribute qt4-mobility-devel rpm-build-ruby soprano zlib-devel-static
BuildRequires: gcc-c++ glib2-devel kde4base-workspace-devel qt4-mobility-devel
BuildRequires: kde4base-runtime-core
BuildRequires: shared-desktop-ontologies soprano-backend-redland soprano-backend-virtuoso soprano
BuildRequires: kde-common-devel

%description
Contour data server


%prep
%setup -qn %rname-%version
mkdir -p cmake/modules/
install -m 0644 %SOURCE1 cmake/modules/
sed -i \
    's|\(^set(CMAKE_MODULE_PATH.*\)$|\1\nset(CMAKE_MODULE_PATH ${CMAKE_MODULE_PATH} ${CMAKE_CURRENT_SOURCE_DIR}/cmake/modules )|' \
    CMakeLists.txt
sed -i 's|^\(include.*KDE4Defaults.*\)|\1\ninclude(SopranoAddOntology)|' CMakeLists.txt


%build
export XDG_DATA_DIRS="%_K4datadir:%_datadir"
%K4build

%install
%K4install
%K4find_lang --with-kde %rname

%files -f %rname.lang
%_kde4_bindir/contour
%_K4lib/contour_recommendationengine_documents.so
%_K4lib/plasma_engine_recommendations.so
%_K4apps/contour/
%_K4apps/plasma/packages/org.kde.contour.*
%_K4apps/plasma/services/recommendations.operations
%_K4start/contour.desktop
%_K4srv/contour-*.desktop
%_K4srv/*-recommendations.desktop
%_K4srvtyp/contour-*.desktop

%changelog
* Wed Feb 08 2012 Sergey V Turchin <zerg@altlinux.org> 0.1.2-alt1
- initial specfile
