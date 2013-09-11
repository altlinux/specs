%define sover 1
%define libname libkfbapi%sover

Name: libkfbapi
Version: 1.0
Release: alt1

Group: System/Libraries
Summary: A library for accessing Facebook services
Url: https://projects.kde.org/projects/extragear/libs/%name
License: LGPLv2 / LGPLv3

#Requires: kde4pimlibs

Source: %name-%version.tar
Patch1: libkfbapi-1.0-alt-pkgconfig.patch

# Automatically added by buildreq on Fri Sep 06 2013 (-bi)
# optimized out: automoc cmake cmake-modules elfutils fontconfig fontconfig-devel kde4libs kde4libs-devel kde4pimlibs libICE-devel libSM-devel libX11-devel libXScrnSaver-devel libXau-devel libXcomposite-devel libXcursor-devel libXdamage-devel libXdmcp-devel libXext-devel libXfixes-devel libXft-devel libXi-devel libXinerama-devel libXpm-devel libXrandr-devel libXrender-devel libXt-devel libXtst-devel libXv-devel libXxf86vm-devel libdbus-devel libdbusmenu-qt2 libfreetype-devel libgst-plugins libpng-devel libqt4-core libqt4-dbus libqt4-devel libqt4-gui libqt4-network libqt4-svg libqt4-webkit libqt4-xml libsoprano-devel libssl-devel libstdc++-devel libxkbfile-devel phonon-devel pkg-config python-base ruby ruby-stdlibs xorg-kbproto-devel xorg-xproto-devel zlib-devel
#BuildRequires: boost-devel-headers gcc-c++ glib2-devel glibc-devel-static kde4-nepomuk-core-devel kde4pimlibs-devel python-module-distribute qjson-devel rpm-build-ruby xorg-xf86miscproto-devel xsltproc
BuildRequires: boost-devel gcc-c++ kde4-nepomuk-core-devel kde4pimlibs-devel qjson-devel xsltproc kde-common-devel

%description
%summary.

%package -n %libname
Group: System/Libraries
Summary: A library for accessing Facebook services
%description -n %libname
%summary.

%package devel
Group: Development/KDE and QT
Summary: Development files for %name
Requires: kde4pimlibs-devel
%description devel
%summary.

%prep
%setup -q
%patch1 -p1

%build
%K4build

%install
%K4install
%K4find_lang %name

%files -n %libname -f %name.lang
%_K4libdir/libkfbapi.so.%sover
%_K4libdir/libkfbapi.so.%sover.*

%files devel
%_K4includedir/libkfbapi/
%_K4libdir/cmake/LibKFbAPI/
%_K4link/libkfbapi.so
%_pkgconfigdir/LibKFbAPI.pc

%changelog
* Fri Sep 06 2013 Sergey V Turchin <zerg@altlinux.org> 1.0-alt1
- initial build

