%define sover 0
%define libpolkitkdekcmodulesprivate libpolkitkdekcmodulesprivate%sover

Name: polkit-kde-kcmmodules-1
Version: 0.98.1
Release: alt1

Group: System/Configuration/Other
Summary: PolicyKit authentication systemsettings modules for KDE
Url: https://projects.kde.org/projects/extragear/base/polkit-kde-kcmodules-1
# ftp://ftp.kde.org/pub/kde/stable/apps/KDE4.x/admin/
License: GPLv2 / LGPLv2.1+

Requires: polkit-kde-agent-1

Source: %name-%version.tar

# Automatically added by buildreq on Fri Apr 12 2013 (-bi)
# optimized out: automoc cmake cmake-modules elfutils fontconfig fontconfig-devel glibc-devel-static kde4libs libICE-devel libSM-devel libX11-devel libXScrnSaver-devel libXau-devel libXcomposite-devel libXcursor-devel libXdamage-devel libXdmcp-devel libXext-devel libXfixes-devel libXft-devel libXi-devel libXinerama-devel libXpm-devel libXrandr-devel libXrender-devel libXt-devel libXtst-devel libXv-devel libXxf86vm-devel libdbus-devel libdbusmenu-qt2 libfreetype-devel libpng-devel libpolkit-qt-core-1 libqt4-core libqt4-dbus libqt4-devel libqt4-gui libqt4-network libqt4-svg libqt4-xml libssl-devel libstdc++-devel libsystemd-login libxkbfile-devel phonon-devel pkg-config python-base ruby ruby-stdlibs xorg-kbproto-devel xorg-xproto-devel zlib-devel
#BuildRequires: gcc-c++ glib2-devel kde4libs-devel libicu libqt3-devel polkit-qt-1-devel python-module-distribute rpm-build-ruby xorg-xf86miscproto-devel zlib-devel-static
BuildRequires: gcc-c++ kde4libs-devel polkit-qt-1-devel kde-common-devel

%package -n %libpolkitkdekcmodulesprivate
Summary: %name library
Group: System/Libraries
#Requires: %name-common = %version-%release
%description -n %libpolkitkdekcmodulesprivate
%name library

%description
Provides Policy Kit Authentication systemsettings that nicely fits to KDE.

%prep
%setup

%build
%K4build

%install
%K4install

%files
%config %_K4dbus_system/org.kde.polkitkde1.helper.conf
%_K4exec/polkitkde1helper
%_K4lib/kcm_polkit*.so
%_K4srv/kcm_polkitactions.desktop
%_K4srv/kcm_polkitconfig.desktop
%_K4srv/settings-system-policies.desktop
%_K4dbus_sys_services/org.kde.polkitkde1.helper.service
%_datadir/polkit-1/actions/org.kde.polkitkde1.policy

%files -n %libpolkitkdekcmodulesprivate
%_libdir/libpolkitkdekcmodulesprivate.so.%sover
%_libdir/libpolkitkdekcmodulesprivate.so.%sover.*

%changelog
* Fri Apr 12 2013 Sergey V Turchin <zerg@altlinux.org> 0.98.1-alt1
- initial build
- update code from master branch
