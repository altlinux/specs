# -*- coding: utf-8; mode: rpm-spec -*-
# $Id: crossfire-maps-bigworld.spec,v 1.2 2006/07/15 15:55:25 eugene Exp $

%define maps_name maps-bigworld
%define maps_version 1.11.0
%define maps_release alt1

Name: crossfire-%maps_name
Version: %maps_version
Release: %maps_release.qa1.1.1
Summary: Bigworld maps for crossfire
Summary(ru_RU.UTF-8): Карты большого мира для crossfire
Group: Games/Adventure
License: GPL
Url: http://crossfire.real-time.com

Packager: Eugene Vlasov <eugvv@altlinux.ru>

BuildArch: noarch

Requires: crossfire
Provides: crossfire-maps

%add_python_req_skip CFBank CFBoard CFGamble CFGuilds CFCampfire CFLog
%add_python_req_skip CFItemBroker CFMail Crossfire CFWorld Crossfire_Type

Source0: crossfire-%version.maps.tar.bz2
Source1: %name.alternatives

Patch0: maps-1.11-python_syntax_fix.patch

# Automatically added by buildreq on Fri Mar 10 2006
BuildRequires: alternatives

%description
crossfire is a multiplayer graphical arcade and adventure game made for
the X-Windows environment.  It runs on a client/server model.
The client runs with X11, GTK, or  SDL within a gtk window.

It has certain flavours from other games, especially Gauntlet (TM)
and Nethack/Moria.

Any number of players can move around in their own window, finding
and using items and battle monsters.  They can choose to cooperate
or compete in the same "world".

This package contains bigworld maps for crossfire server.

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

Этот пакет содержит карты большого мира для сервера crossfire.

%prep
%setup -q -c maps
%patch0 -p0

%install
mkdir -p %buildroot%_altdir
install -p -m644 %SOURCE1 %buildroot%_altdir/%name
mkdir -p %buildroot%_gamesdatadir/crossfire/%maps_name
cp -R maps/* %buildroot%_gamesdatadir/crossfire/%maps_name
cp maps/.emergency %buildroot%_gamesdatadir/crossfire/%maps_name
mkdir -p %buildroot%_localstatedir/games/crossfire/players-%maps_name

%files
%_gamesdatadir/crossfire/%maps_name/
%_altdir/%name
%dir %attr(775, games, games) %_localstatedir/games/crossfire/players-%maps_name


%changelog
* Tue Oct 25 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.11.0-alt1.qa1.1.1
- Rebuild with Python-2.7

* Tue Dec 01 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.11.0-alt1.qa1.1
- Rebuilt with python 2.6

* Tue Nov 10 2009 Repocop Q. A. Robot <repocop@altlinux.org> 1.11.0-alt1.qa1
- NMU (by repocop): the following fixes applied:
  * obsolete-call-in-post-alternatives-0.3 for crossfire-maps-bigworld
  * postclean-05-filetriggers for spec file

* Sat Feb 16 2008 Eugene Vlasov <eugvv@altlinux.ru> 1.11.0-alt1
- New version
- Removed old fix for plugin script python syntax, added new one

* Fri Feb 08 2008 Grigory Batalov <bga@altlinux.ru> 1.10.0-alt2.1
- Rebuilt with python-2.5.

* Fri Jan 04 2008 Eugene Vlasov <eugvv@altlinux.ru> 1.10.0-alt2
- Fixed plugin script python syntax

* Thu Jun 07 2007 Eugene Vlasov <eugvv@altlinux.ru> 1.10.0-alt1
- New version
- Removed %%__ macro

* Sat Jul 15 2006 Eugene Vlasov <eugvv@altlinux.ru> 1.9.1-alt1
- New version

* Fri Mar 10 2006 Eugene Vlasov <eugvv@altlinux.ru> 1.9.0-alt1
- Build maps package from separate source

