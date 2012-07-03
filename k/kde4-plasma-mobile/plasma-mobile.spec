%define _kde_alternate_placement 1

%define rname plasma-mobile
Name: kde4-plasma-mobile
Version: 0.3
Release: alt1

Group: Graphical desktop/KDE
Summary: KDE mobile environment
License: GPLv2 / LGPLv2 / LGPLv2.1
Url: http://kde.org/

Source: plasma-mobile-%version.tar
Patch1: plasma-mobile-0.3-alt-find-kactivities.patch

# Automatically added by buildreq on Tue Jan 31 2012 (-bi)
# optimized out: automoc cmake cmake-modules elfutils fontconfig fontconfig-devel glibc-devel-static kde-common-devel kde4-kactivities-devel kde4libs kde4libs-devel libGL-devel libICE-devel libSM-devel libX11-devel libXScrnSaver-devel libXau-devel libXcomposite-devel libXcursor-devel libXdamage-devel libXdmcp-devel libXext-devel libXfixes-devel libXft-devel libXi-devel libXinerama-devel libXpm-devel libXrandr-devel libXrender-devel libXt-devel libXtst-devel libXv-devel libXxf86misc-devel libXxf86vm-devel libdbus-devel libdbusmenu-qt2 libfreetype-devel libgst-plugins libpng-devel libqt4-core libqt4-dbus libqt4-declarative libqt4-devel libqt4-gui libqt4-network libqt4-opengl libqt4-script libqt4-sql libqt4-svg libqt4-uitools libqt4-webkit libqt4-xml libqt4-xmlpatterns libsoprano-devel libssl-devel libstdc++-devel libxkbfile-devel phonon-devel pkg-config python-base rpm-build-gir ruby shared-desktop-ontologies shared-desktop-ontologies-devel soprano-backend-redland soprano-backend-virtuoso xorg-kbproto-devel xorg-renderproto-devel xorg-xf86miscproto-devel xorg-xproto-devel zlib-devel
#BuildRequires: gcc-c++ glib2-devel kde4base-runtime-core kde4base-workspace-devel libicu libqt3-devel python-module-distribute rpm-build-ruby soprano zlib-devel-static
BuildRequires: gcc-c++ glib2-devel kde4base-workspace-devel zlib-devel-static
BuildRequires: soprano-backend-redland soprano-backend-virtuoso soprano
BuildRequires: kde4base-runtime-devel
BuildRequires: kde-common-devel

%description
KDE mobile environment


%prep
%setup -qn %rname-%version
%patch1 -p1
sed -i \
    's|\(^cmake_minimum_required.*\)$|\1\n\nset(CMAKE_MODULE_PATH ${CMAKE_MODULE_PATH} ${CMAKE_CURRENT_SOURCE_DIR}/cmake/modules )|' \
    CMakeLists.txt

%build
%K4build
#    -DKDE4_INCLUDE_DIR:PATH=%_K4includedir \
#    -DKDE4_LIB_DIR:PATH=%_K4link

%install
%K4install
%K4find_lang --with-kde %rname


%files -f %rname.lang
%_kde4_bindir/active-*
%_kde4_bindir/plasma-*
%_K4exec/*
%_qt4dir/plugins/inputmethods/plasmainputcontextplugin.so
%_K4libdir/libkdeinit4_plasma-*.so
%_K4lib/imports/org/kde/*
%_K4lib/*.so
%_kde4_xdg_apps/*.desktop
%_kde4_iconsdir/plasmamobilemouse
%_kde4_iconsdir/hicolor/*/*/*.*
%_K4wall/*
%_K4apps/*
%_K4start/*
%_K4srv/*
%_K4srvtyp/*
%_K4dbus_system/org.kde.active.clockconfig.conf
%_K4dbus_sys_services/org.kde.active.clockconfig.service
%_datadir/polkit-1/actions/org.kde.active.clockconfig.policy


%changelog
* Wed Feb 08 2012 Sergey V Turchin <zerg@altlinux.org> 0.3-alt1
- initial specfile
