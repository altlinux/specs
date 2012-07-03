%define _kde_alternate_placement 1
%define rname kopete-antispam-kde4

Name: kde4-kopete-antispam
Version: 0.5
Release: alt1

Group: Networking/Instant messaging
Summary: Kopete Antispam Plugin
Url: http://kopeteantispam.sourceforge.net
License: GPLv2

Source: %rname-%version.tar.bz2
# upstream
Patch1: kopete-antispam-4-0.5-findautomoc.patch
Patch2: kopete-antispam-0.5-pref-ui.patch

# Automatically added by buildreq on Tue Jul 05 2011 (-bi)
# optimized out: automoc cmake cmake-modules elfutils fontconfig fontconfig-devel glibc-devel-static kde4libs kde4libs-devel kde4pimlibs libICE-devel libSM-devel libX11-devel libXScrnSaver-devel libXau-devel libXcomposite-devel libXcursor-devel libXdamage-devel libXdmcp-devel libXext-devel libXfixes-devel libXft-devel libXi-devel libXinerama-devel libXpm-devel libXrandr-devel libXrender-devel libXt-devel libXtst-devel libXv-devel libXxf86misc-devel libXxf86vm-devel libdbus-devel libdbusmenu-qt2 libfreetype-devel libpng-devel libqt4-core libqt4-dbus libqt4-devel libqt4-gui libqt4-network libqt4-qt3support libqt4-sql libqt4-svg libqt4-xml libssl-devel libstdc++-devel libxkbfile-devel phonon-devel pkg-config python-base ruby xorg-kbproto-devel xorg-xf86miscproto-devel xorg-xproto-devel zlib-devel
#BuildRequires: gcc-c++ glib2-devel kde4network-devel libqt3-devel rpm-build-ruby zlib-devel-static
BuildRequires: gcc-c++ kde4libs-devel kde4network-devel zlib-devel

%description
Kopete Antispam Plugin helps to protect kopete messenger from various spammers
by using simple answer/question scheme: potential spammers receive a simple
question, and they are ignored until they answers question.

Authors:
--------
    Alexey Noskov <alexey.noskov@gmail.com>

%prep
%setup -n %rname-%version
%patch1 -p0
%patch2 -p0

%build
%K4build

%install
%K4install

%files
%doc ChangeLog
%_K4lib/*.so
%_K4srv/kopete_antispam.desktop
%_K4srv/kconfiguredialog/kopete_antispam_config.desktop
%_K4cfg/kopeteantispamconfig.kcfg

%changelog
* Mon Jul 04 2011 Sergey V Turchin <zerg@altlinux.org> 0.5-alt1
- initial build
