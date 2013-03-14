%define _kde_alternate_placement 1

Name: polkit-kde-agent-1
Version: 0.99.1
Release: alt1

Group: System/Libraries
Summary: PolicyKit authentication agent for KDE
Url: https://projects.kde.org/projects/extragear/base/polkit-kde-agent-1
# ftp://ftp.kde.org/pub/kde/stable/apps/KDE4.x/admin/
License: GPLv2 / LGPLv2.1+

#Requires: polkit-kde-kcmmodules-1
Conflicts: kde4base-workspace-core <= 4.10.1-alt1
Provides: policykit-kde = 4.10
Obsoletes: policykit-kde < 4.10

Source: %name-%version.tar

# Automatically added by buildreq on Wed Mar 13 2013 (-bi)
# optimized out: automoc cmake cmake-modules elfutils fontconfig fontconfig-devel glibc-devel-static kde4libs libICE-devel libSM-devel libX11-devel libXScrnSaver-devel libXau-devel libXcomposite-devel libXcursor-devel libXdamage-devel libXdmcp-devel libXext-devel libXfixes-devel libXft-devel libXi-devel libXinerama-devel libXpm-devel libXrandr-devel libXrender-devel libXt-devel libXtst-devel libXv-devel libXxf86vm-devel libdbus-devel libdbusmenu-qt2 libfreetype-devel libpng-devel libpolkit-qt-agent-1 libpolkit-qt-core-1 libpolkit-qt-gui-1 libqt4-core libqt4-dbus libqt4-devel libqt4-gui libqt4-network libqt4-svg libqt4-xml libssl-devel libstdc++-devel libsystemd-daemon libsystemd-login libxkbfile-devel phonon-devel pkg-config python-base xorg-kbproto-devel xorg-xproto-devel zlib-devel
#BuildRequires: gcc-c++ glib2-devel kde4libs-devel libicu libqt3-devel polkit-qt-1-devel ruby ruby-stdlibs xorg-xf86miscproto-devel zlib-devel-static
BuildRequires: gcc-c++ glib2-devel kde4libs-devel polkit-qt-1-devel

%description
Provides Policy Kit Authentication Agent that nicely fits to KDE.

%prep
%setup

%build
%K4cmake
%K4make

%install
%K4install
#K4find_lang --output=%name.lang polkit-kde-authentication-agent-1

%files
%_K4start/polkit-kde-authentication-agent-1.desktop
%_K4exec/polkit-kde-authentication-agent-1
%_K4apps/policykit1-kde/

%changelog
* Wed Mar 13 2013 Sergey V Turchin <zerg@altlinux.org> 0.99.1-alt1
- built separatly with kde4base-workspace

