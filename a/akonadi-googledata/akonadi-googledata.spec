#define _kde_alternate_placement 1

%add_findpackage_path %_kde4_bindir

Name: akonadi-googledata
Version: 1.2.0
Release: alt2

Group: Graphical desktop/KDE
Summary: Google contacts and calendar akonadi resource
Url: http://code.google.com/p/libgcal/downloads/list
License: GPL

Source: %name-%version.tar
# SuSE
Patch1: fix_events.diff

# Automatically added by buildreq on Mon Oct 31 2011 (-bi)
# optimized out: automoc cmake cmake-modules elfutils fontconfig fontconfig-devel glibc-devel-static kde-common-devel kde4libs kde4libs-devel kde4pimlibs libICE-devel libSM-devel libX11-devel libXScrnSaver-devel libXau-devel libXcomposite-devel libXcursor-devel libXdamage-devel libXdmcp-devel libXext-devel libXfixes-devel libXft-devel libXi-devel libXinerama-devel libXpm-devel libXrandr-devel libXrender-devel libXt-devel libXtst-devel libXv-devel libXxf86misc-devel libXxf86vm-devel libdbus-devel libdbusmenu-qt2 libfreetype-devel libgpg-error libpng-devel libqt4-core libqt4-dbus libqt4-devel libqt4-gui libqt4-network libqt4-sql libqt4-svg libqt4-xml libssl-devel libstdc++-devel libxkbfile-devel phonon-devel pkg-config xorg-kbproto-devel xorg-xf86miscproto-devel xorg-xproto-devel zlib-devel
#BuildRequires: boost-devel-headers gcc-c++ glib2-devel kde4pimlibs-devel libgcal-devel libqt3-devel xsltproc zlib-devel-static
BuildRequires: boost-devel gcc-c++ glib2-devel kde4pimlibs-devel libgcal-devel libqt3-devel xsltproc zlib-devel kde-common-devel

%description
Google contacts and calendar akonadi resource
Adenilson Cavalcanti

%prep
%setup -q
%patch1 -p0

%build
%Kbuild

%install
%Kinstall
%K4find_lang --with-kde akonadi_gcal_resource

%files -f akonadi_gcal_resource.lang
%doc ChangeLog README
%_bindir/*
%_datadir/akonadi/agents/*

%changelog
* Tue Nov 01 2011 Sergey V Turchin <zerg@altlinux.org> 1.2.0-alt2
- add patch from SuSE to fix calendar events

* Mon Oct 31 2011 Sergey V Turchin <zerg@altlinux.org> 1.2.0-alt0.M60P.1
- built for M60P

* Mon Oct 31 2011 Sergey V Turchin <zerg@altlinux.org> 1.2.0-alt1
- new version

* Wed Dec 23 2009 Grigory Milev <week@altlinux.ru> 1.0.1-alt1
- Initial build for ALT Linux
