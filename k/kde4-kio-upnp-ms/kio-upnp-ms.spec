%define _kde_alternate_placement 1

%define rname kio-upnp-ms
Name: kde4-%rname
Version: 1.0.0
Release: alt0.1

Group: Graphical desktop/KDE
Summary: KIO-Slave to show system information
Url: http://www.kde.org/
License: GPLv2

Source: %rname-%version.tar
Patch1: kdelibs-4.7.1-alt-find-hupnp.patch

# Automatically added by buildreq on Mon Nov 07 2011 (-bi)
# optimized out: automoc cmake cmake-modules elfutils fontconfig fontconfig-devel glibc-devel-static kde4libs libICE-devel libSM-devel libX11-devel libXScrnSaver-devel libXau-devel libXcomposite-devel libXcursor-devel libXdamage-devel libXdmcp-devel libXext-devel libXfixes-devel libXft-devel libXi-devel libXinerama-devel libXpm-devel libXrandr-devel libXrender-devel libXt-devel libXtst-devel libXv-devel libXxf86misc-devel libXxf86vm-devel libdbus-devel libdbusmenu-qt2 libfreetype-devel libpng-devel libqt4-core libqt4-dbus libqt4-devel libqt4-gui libqt4-network libqt4-svg libqt4-xml libssl-devel libstdc++-devel libxkbfile-devel phonon-devel pkg-config python-base ruby xorg-kbproto-devel xorg-xf86miscproto-devel xorg-xproto-devel zlib-devel
#BuildRequires: gcc-c++ glib2-devel herqq-devel kde4libs-devel libqt3-devel rpm-build-ruby zlib-devel-static
BuildRequires: gcc-c++ glib2-devel herqq-devel kde4libs-devel zlib-devel

%description
This KIO slave enables KDE applications to access
files over the UPnP MediaServer protocol. It currently
supports both Browse and Search operations depending on
what the server supports.


%prep
%setup -qn %rname-%version
%patch1 -p1

%build
%K4cmake
%K4make


%install
%K4install


%files
%_K4lib/kio_upnp_ms.so
%_K4srv/kio_upnp_ms.protocol

%changelog
* Mon Nov 07 2011 Sergey V Turchin <zerg@altlinux.org> 1.0.0-alt0.1
- initial build
- use 20111102 snapshot
