Summary: Visual brick construction tool for kids
Summary (ru_RU.UTF-8): Детский конструктор, использующий блоки с шипами
Name: leocad
Version: 0.79.3
Release: alt1

License: GPL
Url: http://www.leocad.org
Source: %name-%version-src.tgz
Group: Games/Puzzles
Packager: Fr. Br. George <george@altlinux.ru>

Source1: %name.desktop

Patch1: %name-longint.patch
Patch2: %name-gcc44.patch
Patch3: %name-0.79.3-alt-DSO.patch

BuildRequires: gcc-c++ libgtk+2-devel libjpeg-devel unzip libpng-devel libGL-devel
BuildRequires: desktop-file-utils, ImageMagick

Requires: %name-data > 3000

%description
LeoCAD is a CAD program that uses bricks similar to those found in many
toys (but they don't represent any particular brand). Currently it has
a library of more than 1000 different pieces. LEGO is a trademark of the
LEGO Group of companies which does not sponsor, authorize or endorse
this software.

%description -l ru_RU.UTF-8
LeoCAD -- программа для конструирования чего угодно из блоков с шипами.
В прилагаемой библиотеке таких блоков содержится более 1000 различных
видов. Блоки похожи на те, что используются некоторыми фирмами,
производящими разборные игрушки. LEGO -- торговая марка группы компаний
LEGO, которые не спонсируют и не курируют LeoCAD, а также не имеют
авторских прав на эту программу.

%prep
%setup -n %name
%patch2 -p1
%patch3 -p2

%build
%make PREFIX=/usr

%install
%makeinstall DESTDIR=%buildroot

for f in tools/icon/icon*.png; do
  size=${f##icon}; size=${size##.png}
  install -D $f %buildroot%_iconsdir/hicolor/${size}x$size/apps/%name.png
done
install -D tools/icon/icon.svg %buildroot%_iconsdir/hicolor/scalable/apps/%name.svg

desktop-file-install \
   --dir %buildroot%_desktopdir \
   --vendor="" \
   %SOURCE1

%files
%_bindir/*
%_iconsdir/*/*/*/*
%_man1dir/%name.*
%_desktopdir/%name.desktop
%_xdgmimedir/packages/*
%_datadir/%name
%_pixmapsdir/*

%changelog
* Mon Mar 25 2013 Fr. Br. George <george@altlinux.ru> 0.79.3-alt1
- Autobuild version bump to 0.79.3
- Fix build

* Fri Sep 28 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.75-alt5.2
- Rebuilt with libpng15

* Wed Jun 13 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.75-alt5.1
- Fixed build

* Wed May 25 2011 Igor Vlasenko <viy@altlinux.ru> 0.75-alt5
- fixed build:  added libGL-devel to BR:
- .desktop file cleanup

* Sun Mar 27 2011 Igor Vlasenko <viy@altlinux.ru> 0.75-alt4.1
- completely useless work (thanks to at@)

* Mon Mar 21 2011 Igor Vlasenko <viy@altlinux.ru> 0.75-alt4
- added libpng-devel to BuildRequires: (thanks to at@)

* Tue Sep 21 2010 Fr. Br. George <george@altlinux.ru> 0.75-alt3
- [Igor Vlasenko] updated source from 0.75 branch (closes #22831)

* Sat Nov 14 2009 Repocop Q. A. Robot <repocop@altlinux.org> 0.75-alt2.qa1
- NMU (by repocop): the following fixes applied:
  * obsolete-call-in-post-gtk-update-icon-cache for leocad
  * postclean-05-filetriggers for spec file

* Mon May 25 2009 Fr. Br. George <george@altlinux.ru> 0.75-alt2
- GCC4.4 build fixup

* Sun Oct 07 2007 Fr. Br. George <george@altlinux.ru> 0.75-alt1
- Initial build for ALT

