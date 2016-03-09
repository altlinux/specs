%define sover 1
%define libname libkfbapi%sover

Name: libkfbapi
Version: 1.0
Release: alt2

Group: System/Libraries
Summary: A library for accessing Facebook services
Url: https://projects.kde.org/projects/extragear/libs/%name
License: LGPLv2 / LGPLv3

#Requires: kde4pimlibs

Source: %name-%version.tar
Patch1: libkfbapi-1.0-alt-pkgconfig.patch

# Automatically added by buildreq on Wed Mar 09 2016 (-bi)
# optimized out: automoc boost-devel-headers cmake cmake-modules elfutils fontconfig fontconfig-devel glibc-devel-static kde4libs kde4libs-devel libICE-devel libSM-devel libX11-devel libXScrnSaver-devel libXau-devel libXcomposite-devel libXcursor-devel libXdamage-devel libXdmcp-devel libXext-devel libXfixes-devel libXft-devel libXi-devel libXinerama-devel libXpm-devel libXrandr-devel libXrender-devel libXt-devel libXtst-devel libXv-devel libXxf86vm-devel libakonadi4-calendar libakonadi4-contact libakonadi4-kabc libakonadi4-kcal libakonadi4-kde libakonadi4-kmime libakonadi4-notes libakonadi4-socialutils libakonadi4-xml libdbus-devel libdbusmenu-qt2 libfreetype-devel libgpg-error libgpgmexx4-pthread libgst-plugins1.0 libpng-devel libqt4-core libqt4-dbus libqt4-devel libqt4-gui libqt4-location libqt4-network libqt4-opengl libqt4-sensors libqt4-svg libqt4-webkit libqt4-xml libstdc++-devel libxkbfile-devel phonon-devel pkg-config python-base python3 python3-base ruby ruby-stdlibs xorg-kbproto-devel xorg-xf86miscproto-devel xorg-xproto-devel zlib-devel
#BuildRequires: gcc-c++ glib2-devel kde4pimlibs-devel libXxf86misc-devel libicu50 libqt3-devel libqt4-webkit-devel qjson-devel qt4-designer rpm-build-python3 rpm-build-ruby xsltproc zlib-devel-static
BuildRequires(pre): kde-common-devel
BuildRequires: gcc-c++ glib2-devel kde4pimlibs-devel libXxf86misc-devel libqt4-webkit-devel qjson-devel xsltproc zlib-devel boost-devel

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
* Wed Mar 09 2016 Sergey V Turchin <zerg@altlinux.org> 1.0-alt2
- fix build requires

* Fri Oct 04 2013 Sergey V Turchin <zerg@altlinux.org> 1.0-alt0.M70P.1
- built for M70P

* Fri Sep 06 2013 Sergey V Turchin <zerg@altlinux.org> 1.0-alt1
- initial build

