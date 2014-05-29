%define _kde_alternate_placement 1
%define sover 1
%define libkdeconnect libkdeconnect%sover

%define rname kdeconnect-kde
Name: kde4-connect
Version: 0.5.2.1
Release: alt1

Group: Communications
Summary: KDE Connect client for communication with smartphones
Url: https://projects.kde.org/projects/playground/base/kdeconnect-kde
License: GPLv2+

Provides: %rname = %version
Provides: kde-connect = %version

Source: %rname-%version.tar

# Automatically added by buildreq on Thu May 29 2014 (-bi)
# optimized out: automoc cmake cmake-modules elfutils fontconfig fontconfig-devel glibc-devel-static kde4libs libICE-devel libSM-devel libX11-devel libXScrnSaver-devel libXau-devel libXcomposite-devel libXcursor-devel libXdamage-devel libXdmcp-devel libXext-devel libXfixes-devel libXft-devel libXi-devel libXinerama-devel libXpm-devel libXrandr-devel libXrender-devel libXt-devel libXtst-devel libXv-devel libXxf86vm-devel libcloog-isl4 libdbus-devel libdbusmenu-qt2 libfreetype-devel libpng-devel libqt4-core libqt4-dbus libqt4-declarative libqt4-devel libqt4-gui libqt4-network libqt4-script libqt4-sql libqt4-svg libqt4-test libqt4-xml libqt4-xmlpatterns libsoprano-devel libstdc++-devel libxkbfile-devel phonon-devel pkg-config python-base ruby ruby-stdlibs xorg-kbproto-devel xorg-xf86miscproto-devel xorg-xproto-devel zlib-devel
#BuildRequires: gcc-c++ glib2-devel kde4libs-devel libXxf86misc-devel libicu50 libqca2-devel libqt3-devel python-module-protobuf qjson-devel qt4-designer rpm-build-ruby zlib-devel-static
BuildRequires: gcc-c++ kde4libs-devel libqca2-devel qjson-devel kde-common-devel

%description
KDE Connect adds communication between KDE and your smartphone.

Currently, you can pair with your Android devices over Wifi using the
KDE Connect app from Albert Vaka which you can obtain via Google Play, F-Droid
or the project website.

%package -n %libkdeconnect
Summary: %name libraries
Group: System/Libraries
#Requires: %name-common = %EVR
%description -n %libkdeconnect
%name libraries


%prep
%setup -n %rname-%version


%build
%K4build


%install
%K4install
%find_lang --all-name --with-kde %name



%files -f %name.lang
%doc README

%_K4exec/kdeconnectd

%_K4lib/kcm_kdeconnect.so
%_kde4_xdg_apps/kdeconnect.desktop
%_K4srv/kcm_kdeconnect.desktop

#%_K4lib/kio_kdeconnect.so
#%_K4srv/kdeconnect.protocol

%_K4lib/imports/org/kde/kdeconnect/
%_K4lib/kded_kdeconnect.so

%_K4dbus_interfaces/org.kde.kdeconnect.daemon.xml
%_K4dbus_interfaces/org.kde.kdeconnect.device.battery.xml
%_K4dbus_interfaces/org.kde.kdeconnect.device.notifications.notification.xml
%_K4dbus_interfaces/org.kde.kdeconnect.device.notifications.xml
%_K4dbus_interfaces/org.kde.kdeconnect.device.xml
%_K4dbus_interfaces/org.kde.kdeconnect.device.sftp.xml
%_K4dbus_interfaces/org.kde.kded.kdeconnect.xml

%_K4lib/kdeconnect_*.so
%_K4apps/kdeconnect/
%_K4apps/plasma/plasmoids/kdeconnect/

%_K4srv/kdeconnect_*.desktop
%_K4srv/kded/kdeconnect.desktop
%_K4srv/plasma-kdeconnect.desktop
%_K4srvtyp/kdeconnect_plugin.desktop

%_kde4_iconsdir/hicolor/*/apps/kdeconnect.*

%files -n %libkdeconnect
%_K4libdir/libkdeconnect.so.%sover
%_K4libdir/libkdeconnect.so.%sover.*

%changelog
* Thu May 29 2014 Sergey V Turchin <zerg@altlinux.org> 0.5.2.1-alt1
- initial build
