%define qtdir %_qt4dir

Name: kcheckers
Version: 0.8.1
Release: alt3

Group: Games/Boards
Summary: Classic boardgame - checkers
License: GPL
Url: http://qcheckers.sf.net/
#Url: http://kcheckers.org/
#http://www.kde-apps.org/content/show.php?content=14772
#http://kcheckers.wibix.de
#http://kcheckers.osdn.org.ua

Requires: libqt4-core >= %{get_version libqt4-core}

Source: %name-%version.tar
Source1: %name.desktop
Source2: %name-16.png
Source3: %name-32.png
Source4: %name-48.png

Patch1: kcheckers-0.8.1-alt-prefix.patch
Patch2: kcheckers-0.8.1-alt-qt-translator.patch

BuildRequires(pre): libqt4-devel
BuildRequires: gcc-c++

%description
Tish is classic boardgame "checkers".
This game is also known as "draughts".

%prep
%setup -q
%patch1 -p1
%patch2 -p1

export QTDIR=%qtdir PATH=%qtdir/bin:$PATH
qmake
%make clean

%build
export QTDIR=%qtdir PATH=%qtdir/bin:$PATH
%add_optflags -D_REENTRANT -DQT_NO_DEBUG -DQT_GUI_LIB -DQT_CORE_LIB
%make_build CFLAGS="%optflags" CXXFLAGS="%optflags"
lrelease i18n/*.ts

%install
mkdir -p %buildroot/%_gamesbindir
install -m 0755 %name %buildroot/%_gamesbindir

mkdir -p %buildroot/%_desktopdir/
install -m0644 %SOURCE1 %buildroot/%_desktopdir/%name.desktop

mkdir -p %buildroot/%_datadir/%name/
install -Dm 0644 i18n/*.qm %buildroot/%_datadir/%name/
install -Dm 0644 %SOURCE2 %buildroot/%_iconsdir/hicolor/16x16/apps/%name.png
install -Dm 0644 %SOURCE3 %buildroot/%_iconsdir/hicolor/32x32/apps/%name.png
install -Dm 0644 %SOURCE4 %buildroot/%_iconsdir/hicolor/48x48/apps/%name.png

%files
%_gamesbindir/*
%_datadir/%name
%_desktopdir/%name.desktop
%_iconsdir/*/*/*/%name.png
%doc ChangeLog AUTHORS

%changelog
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

