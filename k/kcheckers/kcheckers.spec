
Name: kcheckers
Version: 0.8.1
Release: alt9

Group: Games/Boards
Summary: Classic boardgame - checkers
License: GPL-2.0-only
Url: http://qcheckers.sf.net/
#Url: http://kcheckers.org/
#http://www.kde-apps.org/content/show.php?content=14772
#http://kcheckers.wibix.de
#http://kcheckers.osdn.org.ua

Source: %name-%version.tar
Source1: %name.desktop
Source2: %name-16.png
Source3: %name-32.png
Source4: %name-48.png
Source10: kcheckers_ru.ts

Patch1: kcheckers-0.8.1-alt-prefix.patch
Patch2: kcheckers-0.8.1-alt-qt-translator.patch
Patch3: kcheckers-0.8.1-qt5.patch

BuildRequires(pre): qt5-base-devel
BuildRequires: qt5-tools

%description
Tish is classic boardgame "checkers".
This game is also known as "draughts".

%prep
%setup -q
%patch1 -p1
%patch2 -p1
%patch3 -p1
cat %SOURCE10 >i18n/kcheckers_ru.ts

export PATH=%_qt5_bindir/bin:$PATH
%qmake_qt5
%make clean

%build
export PATH=%_qt5_bindir/bin:$PATH
%make_build
lrelease-qt5 i18n/*.ts

%install
%installqt5
install -Dm 0644 i18n/*.qm %buildroot/%_datadir/%name/
rm -f %buildroot/%_datadir/%name/*.ts ||:
rm -f %buildroot/%_datadir/%name/{AUTHORS,COPYING,ChangeLog,README} ||:
install -Dm 0644 %SOURCE2 %buildroot/%_iconsdir/hicolor/16x16/apps/%name.png
install -Dm 0644 %SOURCE3 %buildroot/%_iconsdir/hicolor/32x32/apps/%name.png
install -Dm 0644 %SOURCE4 %buildroot/%_iconsdir/hicolor/48x48/apps/%name.png
mkdir -p %buildroot/%_desktopdir/
install -m0644 %SOURCE1 %buildroot/%_desktopdir/%name.desktop

%files
%_bindir/*
%_datadir/%name
%_desktopdir/%name.desktop
%_iconsdir/*/*/*/%name.png
%doc ChangeLog AUTHORS README

%changelog
* Fri Oct 20 2023 Sergey V Turchin <zerg@altlinux.org> 0.8.1-alt9
- install themes

* Fri Oct 20 2023 Sergey V Turchin <zerg@altlinux.org> 0.8.1-alt8
- move to %%_bindir

* Tue Jul 12 2022 Sergey V Turchin <zerg@altlinux.org> 0.8.1-alt7
- update russian translation

* Sat Jun 22 2019 Igor Vlasenko <viy@altlinux.ru> 0.8.1-alt6
- NMU: remove rpm-build-ubt from BR:

* Sat Jun 15 2019 Igor Vlasenko <viy@altlinux.ru> 0.8.1-alt5
- NMU: remove ubt tag from release

* Fri Apr 21 2017 Sergey V Turchin <zerg@altlinux.org> 0.8.1-alt4
- port to Qt5

* Wed Apr 17 2013 Dmitry V. Levin (QA) <qa_ldv@altlinux.org> 0.8.1-alt3.qa1
- NMU: rebuilt for debuginfo.

* Fri Feb 12 2010 Sergey V Turchin <zerg@altlinux.org> 0.8.1-alt3
- don't use deprecated macroses in specfile
- fix build requires

* Thu Dec 06 2007 Sergey V Turchin <zerg at altlinux dot org> 0.8.1-alt2
- fix GenericName in desktop-file

* Tue Oct 02 2007 Sergey V Turchin <zerg at altlinux dot org> 0.8.1-alt1
- new version
- add desktop-file
- fix requires/buildrequires

* Wed Dec 28 2005 Sergey V Turchin <zerg at altlinux dot org> 0.8-alt1
- new version

* Fri Jan 21 2005 Sergey V Turchin <zerg at altlinux dot org> 0.5-alt3
- rebuild with gcc3.4

* Mon Aug 23 2004 Sergey V Turchin <zerg at altlinux dot org> 0.5-alt2
- fix path to Qt and %name translations

* Mon Aug 23 2004 Sergey V Turchin <zerg at altlinux dot org> 0.5-alt1
- new version

* Sat Mar 20 2004 Sergey V Turchin <zerg at altlinux dot org> 0.4-alt2
- rebuild

* Wed Jan 15 2003 Sergey V Turchin <zerg@altlinux.ru> 0.4-alt1
- new version

* Thu Sep 19 2002 Sergey V Turchin <zerg@altlinux.ru> 0.3-alt1
- new version
- build with gcc3.2

* Fri Jun 14 2002 Sergey V Turchin <zerg@altlinux.ru> 0.2-alt1
- initial spec

