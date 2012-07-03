# -*- coding: utf-8; mode: rpm-spec -*-
# $Id: crossfire.spec,v 1.9 2006/07/15 15:53:50 eugene Exp $

Name: crossfire
Version: 1.11.0
Release: alt1.qa3
Summary: Multiplayer graphical role-playing game
Summary(ru_RU.UTF-8): Многопользовательская графическая ролевая игра
License: GPL
Group: Games/Adventure
Url: http://crossfire.real-time.com

Packager: Eugene Vlasov <eugvv@altlinux.ru>

Source0: %name-%version.tar.gz
Source4: %name.desktop
# Icons taken from crossfire-client
Source5: %name-16x16.png
Source6: %name-32x32.png
Source7: %name-48x48.png

Patch0: %name-1.9.0-bound_cond.patch

Provides: crossfire-server
Requires: crossfire-maps

BuildPreReq: perl-CGI

# Automatically added by buildreq on Fri Mar 10 2006
BuildRequires: alternatives flex gcc-c++ imake libICE-devel libSM-devel libX11-devel libXaw-devel libXext-devel libXmu-devel libXpm-devel libXt-devel libpng-devel libstdc++-devel ncompress python-base python-dev python-modules-encodings tetex-latex xorg-cf-files xorg-x11-proto-devel zlib-devel


%description
crossfire is a multiplayer graphical arcade and adventure game made for
the X-Windows environment.  It runs on a client/server model.
The client runs with X11, GTK, or  SDL within a gtk window.

It has certain flavours from other games, especially Gauntlet (TM)
and Nethack/Moria.

Any number of players can move around in their own window, finding
and using items and battle monsters.  They can choose to cooperate
or compete in the same "world".

This package contains crossfire server.

%description -l ru_RU.UTF-8
crossfire - многопользовательская графическая аркадная и
приключенческая игра, работающая в среде X-Windows. Делится на
клиентскую и серверную части. Доступны клиентские части с интерфейсом
X11, GTK, или SDL (в окне gtk).

Игра разработана под влиянием некоторых других игр, особенно Gauntlet
(TM) и Nethack/Moria.

Любое количество игроков может перемещатся в созданном ими мире,
находить и использовать предметы, уничтожать монстров. Игроки могут
сотрудничать или конкурировать в пределах одного "мира"

Этот пакет содержит сервер crossfire.


%package doc
Summary: Documentation for the crossfire game
Summary(ru_RU.UTF-8): Документация для игры crossfire
Group: Games/Adventure

Requires: crossfire-client

%description doc
crossfire is a multiplayer graphical arcade and adventure game made for
the X-Windows environment.  It runs on a client/server model.
The client runs with X11, GTK, or  SDL within a gtk window.

It has certain flavours from other games, especially Gauntlet (TM)
and Nethack/Moria.

Any number of players can move around in their own window, finding
and using items and battle monsters.  They can choose to cooperate
or compete in the same "world".

This package contains documentation for the crossfire game.

%description -l ru_RU.UTF-8 doc
crossfire - многопользовательская графическая аркадная и
приключенческая игра, работающая в среде X-Windows. Делится на
клиентскую и серверную части. Доступны клиентские части с интерфейсом
X11, GTK, или SDL (в окне gtk).

Игра разработана под влиянием некоторых других игр, особенно Gauntlet
(TM) и Nethack/Moria.

Любое количество игроков может перемещатся в созданном ими мире,
находить и использовать предметы, уничтожать монстров. Игроки могут
сотрудничать или конкурировать в пределах одного "мира"

Этот пакет содержит полный комплект документации для игры в crossfire.


%prep
%setup -q
# %patch0 -p1


%build
CFLAGS="${CFLAGS:-%optflags}" ./configure \
	--prefix=%_prefix \
	--mandir=%_mandir \
	--bindir=%_gamesbindir \
	--datadir=%_gamesdatadir \
	--localstatedir=%_localstatedir/games \
	--sysconfdir=%_sysconfdir
%make_build


%install
make DESTDIR=%buildroot install

# Documentation
install -d %buildroot%_defaultdocdir/%name-doc-%version
cp -R doc/* %buildroot%_defaultdocdir/%name-doc-%version
rm -f %buildroot%_defaultdocdir/%name-doc-%version/Developers/Makefile*
rm -rf %buildroot%_defaultdocdir/%name-doc-%version/playbook
rm -f %buildroot%_defaultdocdir/%name-doc-%version/playbook-html/Makefile*
rm -f %buildroot%_defaultdocdir/%name-doc-%version/playbook-html/*-extract
rm -f %buildroot%_defaultdocdir/%name-doc-%version/playbook-html/sorter
for shtm in \
    %buildroot%_defaultdocdir/%name-doc-%version/playbook-html/*.shtml;\
    do mv $shtm `echo $shtm|sed -e 's/\.shtml/\.html/'`;\
done
rm -rf %buildroot%_defaultdocdir/%name-doc-%version/scripts
rm -f %buildroot%_defaultdocdir/%name-doc-%version/spell-docs/Makefile*
rm -rf %buildroot%_defaultdocdir/%name-doc-%version/spoiler
rm -f %buildroot%_defaultdocdir/%name-doc-%version/spoiler-html/Makefile*
rm -f %buildroot%_defaultdocdir/%name-doc-%version/spoiler-html/*-extract
rm -f %buildroot%_defaultdocdir/%name-doc-%version/Makefile*
rm -f %buildroot%_defaultdocdir/%name-doc-%version/*.pl
gzip -f -9 ChangeLog

# Desktop entry
install -d %buildroot%_desktopdir
install -m 644 %SOURCE4 %buildroot%_desktopdir/%name.desktop
install -d %buildroot%_miconsdir
install -d %buildroot%_niconsdir
install -d %buildroot%_liconsdir
install -m 644 %SOURCE5 %buildroot%_miconsdir/%name.png
install -m 644 %SOURCE6 %buildroot%_niconsdir/%name.png
install -m 644 %SOURCE7 %buildroot%_liconsdir/%name.png

install -d %buildroot%_localstatedir/games/%name/datafiles

%files
%dir %_sysconfdir/%name
%config(noreplace) %_sysconfdir/%name/*
%_gamesbindir/*
%attr(2711, root, games) %_gamesbindir/%name
%_libexecdir/%name
%_man6dir/*
%dir %attr(775, games, games) %_localstatedir/games/%name
%config(noreplace) %attr(664, games, games) %_localstatedir/games/%name/*
%dir %attr(775, games, games) %_localstatedir/games/%name/maps
%dir %attr(775, games, games) %_localstatedir/games/%name/datafiles
%dir %attr(775, games, games) %_localstatedir/games/%name/unique-items
%dir %attr(775, games, games) %_localstatedir/games/%name/players
%dir %attr(775, games, games) %_localstatedir/games/%name/template-maps
%_gamesdatadir/%name
%doc AUTHORS ChangeLog.gz DEVELOPERS NEWS README TODO
%_desktopdir/%name.desktop
%_miconsdir/%name.png
%_niconsdir/%name.png
%_liconsdir/%name.png

%files doc
%_defaultdocdir/%name-doc-%version


%changelog
* Thu Feb 02 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.11.0-alt1.qa3
- Fixed build

* Sat Apr 09 2011 Igor Vlasenko <viy@altlinux.ru> 1.11.0-alt1.qa2
- NMU: .desktop file cleanup

* Tue Nov 17 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.11.0-alt1.qa1.1
- Rebuilt with python 2.6

* Tue Nov 10 2009 Repocop Q. A. Robot <repocop@altlinux.org> 1.11.0-alt1.qa1
- NMU (by repocop): the following fixes applied:
  * update_menus for crossfire
  * postclean-05-filetriggers for spec file

* Sat Feb 16 2008 Eugene Vlasov <eugvv@altlinux.ru> 1.11.0-alt1
- New version
- Removed unused menu entry (Source3)

* Thu Jan 24 2008 Grigory Batalov <bga@altlinux.ru> 1.10.0-alt1.1
- Rebuilt with python-2.5.

* Thu Jun 07 2007 Eugene Vlasov <eugvv@altlinux.ru> 1.10.0-alt1
- New version
- Removed %%__ macro

* Sat Jul 15 2006 Eugene Vlasov <eugvv@altlinux.ru> 1.9.1-alt1
- New version

* Fri Mar 10 2006 Eugene Vlasov <eugvv@altlinux.ru> 1.9.0-alt1
- New version
- Build maps package from separate source
- Added desktop entry and icons
- Updated BuildRequires
- Fixed CVE-2006-1236

* Sun Jan 29 2006 Eugene Vlasov <eugvv@altlinux.ru> 1.8.0-alt2
- Excluded INSTALL from docdir
- Fixed macro warnings

* Sun Aug 21 2005 Eugene Vlasov <eugvv@altlinux.ru> 1.8.0-alt1
- New version
- Fixed alternatives unregistration
- Build with only maps-bigworld, without unsupported maps-small
- Updated BuildRequires

* Sun Mar 13 2005 Eugene Vlasov <eugvv@altlinux.ru> 1.7.0-alt2
- Rebuild with python 2.4

* Fri Jan 28 2005 Eugene Vlasov <eugvv@altlinux.ru> 1.7.0-alt1
- New version
- Build crossfire-doc from crossfire-1.7.0-alt1.src
- Build server with python plugin

* Sun Dec 19 2004 Eugene Vlasov <eugvv@altlinux.ru> 1.6.0-alt2
- Switch player's save files together with maps

* Sun Nov 28 2004 Eugene Vlasov <eugvv@altlinux.ru> 1.6.0-alt1
- First build for Sisyphus

