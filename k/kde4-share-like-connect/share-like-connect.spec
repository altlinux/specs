%define _kde_alternate_placement 1

%define rname share-like-connect
Name: kde4-share-like-connect
Version: 0.2
Release: alt1

Group: Graphical desktop/KDE
Summary: Social-Semantic Features for Active
Url: http://plasma.kde.org
License: GPLv2 / LGPLv2.1+ / BSD

#Requires: kde4base-workspace-core

Source: %rname-%version.tar

# Automatically added by buildreq on Wed Feb 08 2012 (-bi)
# optimized out: automoc cmake cmake-modules elfutils fontconfig fontconfig-devel glibc-devel-static kde4libs kde4libs-devel libICE-devel libSM-devel libX11-devel libXScrnSaver-devel libXau-devel libXcomposite-devel libXcursor-devel libXdamage-devel libXdmcp-devel libXext-devel libXfixes-devel libXft-devel libXi-devel libXinerama-devel libXpm-devel libXrandr-devel libXrender-devel libXt-devel libXtst-devel libXv-devel libXxf86misc-devel libXxf86vm-devel libdbus-devel libdbusmenu-qt2 libfreetype-devel libgst-plugins libpng-devel libqt4-core libqt4-dbus libqt4-declarative libqt4-devel libqt4-gui libqt4-network libqt4-opengl libqt4-script libqt4-sql libqt4-svg libqt4-uitools libqt4-webkit libqt4-xml libqt4-xmlpatterns libsoprano-devel libssl-devel libstdc++-devel libxkbfile-devel phonon-devel pkg-config python-base ruby shared-desktop-ontologies-devel soprano-backend-redland soprano-backend-virtuoso xorg-kbproto-devel xorg-xf86miscproto-devel xorg-xproto-devel zlib-devel
#BuildRequires: gcc-c++ glib2-devel kde4-kactivities-devel kde4base-runtime-devel libicu libqt3-devel python-module-distribute rpm-build-ruby soprano zlib-devel-static
BuildRequires: gcc-c++ glib2-devel kde4-kactivities-devel kde4base-runtime-devel
BuildRequires: soprano-backend-redland soprano-backend-virtuoso soprano
BuildRequires: kde-common-devel

%description
Share * Like * Connect Social-Semantic Features for Plasma Active

Authors:
--------
    Aaron Seigo, Marco Martin

%package -n libsharelikeconnect4
Summary: Library for share-like-connect
Group: System/Libraries
%description -n libsharelikeconnect4
Contains the libary to use share-like-connect in applications


%package devel
Group: System/Libraries
Summary: Development files for share-like-connect
Requires: libsharelikeconnect4
%description devel
Developmet files and headers for share-like-connect


%prep
%setup -qn %rname-%version
sed -i 's|^\(include.*KDE4Defaults.*\)|\1\ninclude(SopranoAddOntology)|' CMakeLists.txt

%build
%K4build

%install
%K4install

%files
%_K4lib/imports/org/kde/plasma/slccomponents/
%_K4lib/plasma_dataengine_sharelikeconnect.so
%_K4lib/sharelikeconnect_provider_activities.so
%_K4lib/sharelikeconnect_provider_bookmarks.so
%_K4lib/sharelikeconnect_provider_rating.so
%_K4lib/sharelikeconnect_provider_sendbyemail.so

%_K4apps/plasma/plasmoids/
%_K4apps/plasma/services/*
%_K4apps/plasma/slcmenuitems/
%_K4srv/*
%_K4srvtyp/*

%files -n libsharelikeconnect4
%_K4libdir/libsharelikeconnect.so

%files devel
%_K4includedir/activecontentservice

%changelog
* Wed Feb 08 2012 Sergey V Turchin <zerg@altlinux.org> 0.2-alt1
- initial specfile
