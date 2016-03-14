
%define rname kaffeine
Name: kde4-%rname
Version: 1.3.1
Release: alt1

Group: Video
Summary: Multimedia Player
Url: http://kaffeine.sourceforge.net/
License: GPLv2

Requires: libqt4-sql-sqlite
Conflicts: kaffeine <= 0.8.8-alt4

# svn.kde.org/home/kde/trunk/extragear/multimedia/kaffeine
Source0: %rname-%version.tar

# Automatically added by buildreq on Mon Mar 14 2016 (-bi)
# optimized out: automoc cmake cmake-modules elfutils fontconfig fontconfig-devel glibc-devel-static kde4libs libICE-devel libSM-devel libX11-devel libXScrnSaver-devel libXau-devel libXcomposite-devel libXcursor-devel libXdamage-devel libXdmcp-devel libXext-devel libXfixes-devel libXft-devel libXi-devel libXinerama-devel libXpm-devel libXrandr-devel libXrender-devel libXt-devel libXtst-devel libXv-devel libXxf86vm-devel libdbus-devel libdbusmenu-qt2 libfreetype-devel libgpg-error libpng-devel libqt4-core libqt4-dbus libqt4-devel libqt4-gui libqt4-network libqt4-sql libqt4-svg libqt4-xml libstdc++-devel libxkbfile-devel phonon-devel pkg-config python-base python3 python3-base rpm-build-python3 xorg-kbproto-devel xorg-scrnsaverproto-devel xorg-xf86miscproto-devel xorg-xproto-devel zlib-devel
#BuildRequires: gcc-c++ glib2-devel kde4libs-devel libXxf86misc-devel libicu50 libqt3-devel libqt4-webkit-devel libvlc-devel python3.3-site-packages qt4-desi#gner ruby ruby-stdlibs zlib-devel-static
BuildRequires: gcc-c++ glib2-devel kde4libs-devel libXxf86misc-devel libqt4-webkit-devel libvlc-devel zlib-devel

%description
Kaffeine plays all files and devices supported by Xine. For example,
MPEG files, AVI (if the codec being used is supported by Xine), MP3,
and Ogg Vorbis. It also handles Video CDs, DVDs, and DVB cards.


%prep
%setup -q -n %rname-%version

%build
%K4cmake
%K4make


%install
%K4install
%K4find_lang %rname


%files -f %rname.lang
%doc Changelog NOTES
%_K4bindir/kaffeine
%_K4bindir/dtvdaemon
#%_K4lib/kaffeinedvb.so
%_K4apps/kaffeine/
%_K4iconsdir/hicolor/*/*/*.*
%_K4iconsdir/oxygen/*/*/*.*
%_K4apps/solid/actions/kaffeine_*.desktop
%_K4apps/profiles/kaffeine.profile.xml
%_K4xdg_apps/kaffeine.desktop

%changelog
* Mon Mar 14 2016 Sergey V Turchin <zerg@altlinux.org> 1.3.1-alt1
- new version

* Thu Jul 23 2015 Sergey V Turchin <zerg@altlinux.org> 1.2.2-alt3
- don't increase InitialPreference

* Tue Oct 09 2012 Sergey V Turchin <zerg@altlinux.org> 1.2.2-alt2
- fix to build with gcc 4.7

* Mon Apr 25 2011 Sergey V Turchin <zerg@altlinux.org> 1.2.2-alt1
- new version

* Fri Mar 18 2011 Sergey V Turchin <zerg@altlinux.org> 1.1-alt2
- move to standart place

* Mon Sep 13 2010 Sergey V Turchin <zerg@altlinux.org> 1.1-alt1
- new version

* Wed Jun 02 2010 Sergey V Turchin <zerg@altlinux.org> 1.0-alt0.M51.1
- built for M51

* Wed Jun 02 2010 Sergey V Turchin <zerg@altlinux.org> 1.0-alt1
- 1.0 release

* Wed Feb 03 2010 Sergey V Turchin <zerg@altlinux.org> 1.0-alt0.3.M51.1
- built for M51

* Mon Feb 01 2010 Sergey V Turchin <zerg@altlinux.org> 1.0-alt0.4
- 1.0-pre3

* Mon Aug 10 2009 Sergey V Turchin <zerg@altlinux.org> 1.0-alt0.2.M50.1
- built for M50

* Mon Aug 10 2009 Sergey V Turchin <zerg@altlinux.org> 1.0-alt0.3
- increase InitialPreference

* Mon Aug 10 2009 Sergey V Turchin <zerg@altlinux.org> 1.0-alt0.2.pre2
- 1.0-pre2

* Tue Jun 23 2009 Sergey V Turchin <zerg@altlinux.org> 1.0-alt0.1.pre1
- initial specfile

