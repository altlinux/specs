%define __kde4_alternate_placement 1

%define rname kio-mtp
Name: kde4-%rname
Version: 0.70
Release: alt2

Group: Networking/Remote access
Summary: KIO-Slave to acces newtwork shares via autofs
Url: http://www.kde.org/
License: GPLv2

Source: %rname-%version.tar

# Automatically added by buildreq on Mon Nov 19 2012 (-bi)
# optimized out: automoc cmake cmake-modules elfutils fontconfig fontconfig-devel glibc-devel-static kde4libs libICE-devel libSM-devel libX11-devel libXScrnSaver-devel libXau-devel libXcomposite-devel libXcursor-devel libXdamage-devel libXdmcp-devel libXext-devel libXfixes-devel libXft-devel libXi-devel libXinerama-devel libXpm-devel libXrandr-devel libXrender-devel libXt-devel libXtst-devel libXv-devel libXxf86misc-devel libXxf86vm-devel libdbus-devel libdbusmenu-qt2 libfreetype-devel libpng-devel libqt4-core libqt4-dbus libqt4-devel libqt4-gui libqt4-network libqt4-svg libqt4-xml libsoprano-devel libssl-devel libstdc++-devel libxkbfile-devel phonon-devel pkg-config python-base ruby xorg-kbproto-devel xorg-xf86miscproto-devel xorg-xproto-devel zlib-devel
#BuildRequires: gcc-c++ glib2-devel kde4libs-devel libicu libmtp-devel libqt3-devel python-module-distribute rpm-build-ruby zlib-devel-static
BuildRequires: gcc-c++ glib2-devel kde4libs-devel libmtp-devel kde-common-devel

%description
This KIO slave enables KDE applications to access
files stored on devices that provide access to them
via the MTP protocol.


%prep
%setup -q -n %rname-%version


%build
%K4build


%install
%K4install

%files
%_K4lib/kio_mtp.so
%_K4srv/mtp.protocol
%_K4apps/konqueror/dirtree/remote/mtp-network.desktop
%_K4apps/remoteview/mtp-network.desktop
%_K4apps/solid/actions/solid_mtp.desktop

%changelog
* Wed Feb 06 2013 Sergey V Turchin <zerg@altlinux.org> 0.70-alt2
- update from master branch

* Mon Nov 19 2012 Sergey V Turchin <zerg@altlinux.org> 0.70-alt1
- initial build
