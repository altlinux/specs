Name: qstat
Version: 2.11
Release: alt1
Summary: Game server browsing utility
License: Artistic
Group: Networking/Other
URL: http://sourceforge.net/projects/qstat

Packager: Pavlov Konstantin <thresh@altlinux.ru>
Source: %name-%version.tar.gz

%description 
QStat is a command-line program that displays information about
Internet game servers. The servers are either down, non-responsive,
or running a game. For servers running a game, the server name, map
name, current number of players, and response time are displayed.
Server rules and player information may also be displayed.                                                                            
Games supported include Quake, QuakeWorld, Hexen II, Quake II,
HexenWorld, Unreal, Half-Life, Sin, Shogo, Tribes, Tribes 2,
Quake III: Arena, BFRIS, Kingpin, and Heretic II, Unreal Tournament,
Soldier of Fortune, Rogue Spear, Redline, Turok II, Blood 2,
Descent 3, Drakan, KISS, Nerf Arena Blast, Rally Master,
Terminous, Wheel of Time, and Daikatana.

%prep
%setup -q

%build
%configure --enable-dump

%make_build

%install
%__mkdir -p %buildroot{%_sysconfdir,%_bindir}

%__install -m755 qstat %buildroot%_bindir
%__install -m644 qstat.cfg %buildroot%_sysconfdir
%__cat contrib.cfg >> %buildroot%_sysconfdir/qstat.cfg

%files
%doc *.txt *.html *.cfg template
%config %_sysconfdir/qstat.cfg
%_bindir/qstat

%changelog
* Mon Nov 13 2006 Pavlov Konstantin <thresh@altlinux.ru> 2.11-alt1
- 2.11 release.
- Added packager field.

* Sun Nov 06 2005 Pavlov Konstantin <thresh@altlinux.ru> 2.10-alt1
- 2.10 release.
- enabling packet dump.

* Mon Apr 04 2005 Pavlov Konstantin <thresh@altlinux.ru> 2.8-alt1
- 2.8 release.

* Thu Jan 20 2005 Pavlov Konstantin <thresh@altlinux.ru> 2.7-alt1
- 2.7 release.

* Wed Jun 18 2003 Sir Raorn <raorn@altlinux.ru> 2.5c-alt1
- [2.5c]

* Sun Oct 20 2002 Sir Raorn <raorn@altlinux.ru> 2.5b-alt1
- [2.5b]

* Wed Mar 06 2002 Sir Raorn <raorn@altlinux.ru> 2.4e-alt1
- Built for Sisyphus

