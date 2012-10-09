
%define rname kaffeine
Name: kde4-%rname
Version: 1.2.2
Release: alt2

Group: Video
Summary: Multimedia Player
Url: http://kaffeine.sourceforge.net/
License: GPLv2

Requires: libqt4-sql-sqlite
Conflicts: kaffeine <= 0.8.8-alt4

# svn.kde.org/home/kde/trunk/extragear/multimedia/kaffeine
Source0: %rname-%version.tar.bz2
Patch1: alt-gcc47.patch

BuildRequires: gcc-c++ kde4libs-devel libxine-devel

%description
Kaffeine plays all files and devices supported by Xine. For example,
MPEG files, AVI (if the codec being used is supported by Xine), MP3,
and Ogg Vorbis. It also handles Video CDs, DVDs, and DVB cards.


%prep
%setup -q -n %rname-%version
%patch1 -p1
echo "X-KDE4-InitialPreference=30" >> src/kaffeine.desktop

%build
%K4cmake
%K4make


%install
%K4install
%K4find_lang %rname


%files -f %rname.lang
%doc Changelog NOTES
%_K4bindir/kaffeine
%_K4bindir/kaffeine-xbu
#%_K4lib/kaffeinedvb.so
%_K4apps/kaffeine/
%_K4iconsdir/hicolor/*/*/*.*
%_K4iconsdir/oxygen/*/*/*.*
%_K4apps/solid/actions/kaffeine_*.desktop
%_K4apps/profiles/kaffeine.profile.xml
%_K4xdg_apps/kaffeine.desktop

%changelog
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

