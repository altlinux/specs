%define req_ver_mlt 0.7.8

Name: kdenlive
Version: 0.9.2
Release: alt1

Summary: KDE Non Linear Video Editor
Summary(ru_RU.utf8): Редактор нелинейного видео монтажа для KDE
Summary(ru_UA.utf8): Редактор нелінійного монтажу для KDE
License: GPL
Group: Video
URL: http://sourceforge.net/projects/%name/

Requires: mlt-utils >= %req_ver_mlt frei0r-plugins /usr/bin/ffmpeg
Requires: recordmydesktop dvdauthor dvgrab genisoimage
Requires: icon-theme-oxygen

Source: %name-%version.tar
Source1: ru.po
Patch1: kdenlive-0.8-alt-mlt0.7.4.patch
Patch2: kdenlive-0.8.2.1-alt-fix-compile.patch

BuildRequires: cmake cmake-modules gcc-c++
BuildRequires: kde4base-workspace-devel libqt4-devel kde-common-devel qjson-devel
BuildRequires: libmlt-devel libmlt++-devel >= %req_ver_mlt
# Nepomuk
BuildRequires: soprano soprano-backend-virtuoso soprano-backend-redland libsoprano-devel

%description
Kdenlive is a non-linear video editor for GNU/Linux, which supports
DV, HDV and AVCHD(not complete yet) editing.

%description -l ru_RU.utf8
Редактор нелинейного видео монтажа для GNU/Linux

%description -l ru_UA.utf8
Редактор нелінійного монтажу для GNU/Linux

%prep
%setup -q
mv altlinux/po .
#cat %SOURCE1 > po/ru/kdenlive.po
#%patch1 -p1
%patch2 -p1

%build
%K4build

%install
%K4install
%K4find_lang --with-kde %name

%files -f %name.lang
%_bindir/*
%_K4xdg_apps/*
%_K4apps/%name
%_K4cfg/*
%_iconsdir/*/*/*/*.*
%_K4lib/*
%_K4srv/*
%_man1dir/*
%_K4conf/*
%_K4xdg_mime/*

%changelog
* Wed May 30 2012 Sergey V Turchin <zerg@altlinux.org> 0.9.2-alt1
- new version

* Thu May 17 2012 Sergey V Turchin <zerg@altlinux.org> 0.9-alt1
- new version

* Tue Mar 13 2012 Sergey V Turchin <zerg@altlinux.org> 0.8.2.1-alt3.M60P.1
- built for M60P

* Tue Mar 13 2012 Sergey V Turchin <zerg@altlinux.org> 0.8.2.1-alt4
- update russian translation; thanks azol@alt (ALT#27051)

* Sat Feb 04 2012 Sergey V Turchin <zerg@altlinux.org> 0.8.2.1-alt3
- fix requires

* Fri Feb 03 2012 Sergey V Turchin <zerg@altlinux.org> 0.8.2.1-alt2
- fix compile

* Thu Dec 29 2011 Sergey V Turchin <zerg@altlinux.org> 0.8.2.1-alt0.M60P.1
- built for M60P

* Mon Dec 12 2011 Sergey V Turchin <zerg@altlinux.org> 0.8.2.1-alt1
- new version (ATL#26350)

* Wed Aug 24 2011 Sergey V Turchin <zerg@altlinux.org> 0.8-alt1.M60P.1
- built for M60P

* Wed Aug 24 2011 Sergey V Turchin <zerg@altlinux.org> 0.8-alt2
- fix detect mlt-0.7.4

* Wed Apr 27 2011 Sergey V Turchin <zerg@altlinux.org> 0.8-alt1
- new version

* Wed Sep 29 2010 Sergey V Turchin <zerg@altlinux.org> 0.7.8-alt2
- fix requires (ATL#20019)

* Thu Sep 16 2010 Sergey V Turchin <zerg@altlinux.org> 0.7.8-alt0.M51.1
- built for M51

* Wed Sep 15 2010 Sergey V Turchin <zerg@altlinux.org> 0.7.8-alt1
- new version

* Thu Jun 17 2010 Sergey V Turchin <zerg@altlinux.org> 0.7.7.1-alt1.M51.1
- build for M51

* Thu Jun 17 2010 Sergey V Turchin <zerg@altlinux.org> 0.7.7.1-alt2
- build for sisyphus

* Wed Apr 14 2010 Maxim Ivanov <redbaron at altlinux.org> 0.7.7.1-alt1
- Update to 0.7.7.1

* Thu Nov 12 2009 Maxim Ivanov <redbaron at altlinux.org> 0.7.6-alt1
- Update to 0.7.6

* Sun Aug 30 2009 Maxim Ivanov <redbaron at altlinux.org> 0.7.5-alt2
- Rebuild with new mlt

* Sat Aug 29 2009 Maxim Ivanov <redbaron at altlinux.org> 0.7.5-alt1
- Update to 0.7.5 (ALT #21144)

* Mon Jul 20 2009 Maxim Ivanov <redbaron at altlinux.org> 0.7.4-alt1.git.ec1704579b6fh4
- Update to 0.7.4

* Sun Apr 19 2009 Maxim Ivaniv <redbaron at altlinux.org> 0.7.3-alt1.svn3320
- 0.7.3

* Thu Dec 11 2008 Valery Inozemtsev <shrek@altlinux.ru> 0.6-alt1
- 0.6

* Sun Nov 23 2008 Valery Inozemtsev <shrek@altlinux.ru> 0.5-alt6
- removed obsolete %%update_menus/%%clean_menus calls

* Sun Oct 26 2008 Valery Inozemtsev <shrek@altlinux.ru> 0.5-alt5
- fixed build with gcc4.3

* Mon Jan 28 2008 Valery Inozemtsev <shrek@altlinux.ru> 0.5-alt4
- fix crash on exit

* Thu Dec 20 2007 Valery Inozemtsev <shrek@altlinux.ru> 0.5-alt3
- rebuild for mlt-0.2.5
- fixed menu

* Mon Oct 29 2007 Alexey Morsov <swi@altlinux.ru> 0.5-alt2
- add russian translate (from Alexandra Panyukova)

* Mon Sep 03 2007 Alexey Morsov <swi@altlinux.ru> 0.5-alt1
- 0.5-1

* Wed Feb 14 2007 Alexey Morsov <swi@altlinux.ru> 0.4-alt0.2
- clean files section
- add summary, description for ru(ua) in utf8

* Tue Feb 13 2007 Led <led@altlinux.ru> 0.4-alt0.1
- initial build
