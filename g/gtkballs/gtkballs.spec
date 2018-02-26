Name: gtkballs
Version: 3.1.5
Release: alt4

Summary: A simple logic game like Lines
License: GPL
Group: Games/Puzzles

Url: http://gtkballs.antex.ru
Source0: %name-%version.tar.gz
Source1: gtkballs.desktop
Packager: Michael Shigorin <mike@altlinux.org>

Summary(fr): Un simple jeu de logique
Summary(ru_RU.UTF-8): Простая и увлекательная логическая игра вроде Lines
Summary(uk_UA.UTF-8): Проста та цікава логічна гра на кшталт Lines

# Automatically added by buildreq on Tue Sep 09 2008
BuildRequires: libgtk+2-devel

%description
GtkBalls is a simple logic game. The goal of
the game is to make the maximum number of lines
with balls of the same color. A line is made of
five balls. Each time you don't do a line, extra
balls appear on the grid. You loose when the
grid is full.

%description -l fr
GtkBalls est un simple jeu de logique. Le but du
jeu est de faire le nombre maximum de lignes avec
des balles de la mЙme couleur. Une ligne est
constituИe de cinq balles. A chaque fois que vous
ne faites pas une ligne, des balles suplИmentaires
apparaissent sur la grille. Vous perdez lorsque
la grille est pleine.

%description -l ru_RU.UTF-8
GtkBalls -- это простая логическая игра.  Цель
игры -- составлять линии максимальной длины из
шариков одинакового цвета.  Минимальная длина линии
за которую дают очки -- 5 шариков.  Если вы не
составили линию за ход, то на следующем ходу
появляются новые шарики.  Игра заканчивается,
когда на поле не остается места для новых шариков.

%description -l uk_UA.UTF-8
GtkBalls -- проста логічна гра, ціль якої --
складати рядки максимальної довжини з кульок одного
кольору.  Мінімальна довжина лінії, за яку надаються
бали -- 5 кульок.  Якщо ви не склали лінію за хід,
то перед наступним ходом з'являться нові кульки.
Гра закінчується, коли не залишається місця для
нових кульок.

%prep
%setup

%build
%configure \
	--datadir=%_datadir \
	--localstatedir=%_localstatedir/games \
	--bindir=%_gamesbindir
%make_build

%install
%makeinstall \
	datadir=%buildroot%_datadir \
	localstatedir=%buildroot%_localstatedir/games \
	bindir=%buildroot%_gamesbindir
install -pDm644 %SOURCE1 %buildroot%_desktopdir/%name.desktop
%find_lang %name

%files -f %name.lang
%attr(2711,root,games)%_gamesbindir/*
%_datadir/%name
%_man6dir/*
%_desktopdir/%name.desktop
%ghost %_localstatedir/games/gtkballs-scores

%post
if [ ! -f %_localstatedir/games/gtkballs-scores ]; then
	touch %_localstatedir/games/gtkballs-scores
fi
chgrp games %_localstatedir/games/gtkballs-scores
chmod 0664 %_localstatedir/games/gtkballs-scores

%changelog
* Thu Jul 30 2009 Michael Shigorin <mike@altlinux.org> 3.1.5-alt4
- fixed desktop file (repocop), moved it into a separate source
- minor spec cleanup

* Wed Dec 03 2008 Michael Shigorin <mike@altlinux.org> 3.1.5-alt3
- applied repocop patch

* Tue Sep 09 2008 Michael Shigorin <mike@altlinux.org> 3.1.5-alt2
- fixed build (buildreq)
- replaced Debian menu file with a desktop file based on PLD one
- description translations converted to utf-8
- me as a Packager:
- spec cleanup

* Tue Nov 16 2004 drF_ckoff <dfo@altlinux.ru> 3.1.5-alt1
- New version

* Tue Oct 26 2004 drF_ckoff <dfo@altlinux.ru> 3.1.4-alt1
- New version

* Fri Jul  2 2004 drF_ckoff <dfo@altlinux.ru> 3.1.3-alt2
- Menu entry changed from Amusement/Strategy to Amusement/Puzzles

* Wed May 26 2004 drF_ckoff <dfo@altlinux.ru> 3.1.3-alt1
- New version

* Fri Feb  6 2004 drF_ckoff <dfo@altlinux.ru> 3.1.2-alt1
- New version

* Fri Feb  6 2004 drF_ckoff <dfo@altlinux.ru> 3.1.1-alt1
- New version

* Mon Feb  2 2004 drF_ckoff <dfo@altlinux.ru> 3.1.0-alt5
- build fixes

* Fri Jan 30 2004 drF_ckoff <dfo@altlinux.ru> 3.1.0-alt4
- hasher build fixes

* Thu Jan 29 2004 drF_ckoff <dfo@altlinux.ru> 3.1.0-alt3
- changed @antex.ru to @altlinux.ru to make stupid hasher happy

* Wed Jan 28 2004 drF_ckoff <dfo@antex.ru> 3.1.0-alt2
- small compilation and .spec fixed

* Thu Jan 22 2004 drF_ckoff <dfo@antex.ru> 3.1.0-alt1
- 3.1.0
- fix scorefile installation

* Mon Feb 11 2002 Rider <rider@altlinux.ru> 2.1.1-alt1
- 2.1.1
- specfile cleanup

* Sun Oct 14 2001 Rider <rider@altlinux.ru> 2.0-alt1
- first build for ALT Linux

* Wed Sep  1 1999 Eugene Morozov <jmv@lucifer.dorms.spbu.ru>
- Changed my Email address because I check yahoo mail seldom.
  Added installation of gnome icon.
  Fixed several bugs in the spec file.

