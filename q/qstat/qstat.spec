%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1
%set_verify_elf_method strict

Name: qstat
Version: 2.17
Release: alt1
Summary: Game server browsing utility
License: Artistic-2.0
Group: Networking/Other
URL: https://github.com/multiplay/qstat

Source: %name-%version.tar

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
%setup

%build
%add_optflags -D_FILE_OFFSET_BITS=64
export QSTAT_VERSION=v%version
%autoreconf
%configure --enable-dump

%make_build

%install
%__mkdir -p %buildroot{%_sysconfdir,%_bindir}
%__install -m755 qstat %buildroot%_bindir
%__install -m644 qstat.cfg %buildroot%_sysconfdir
%__cat contrib.cfg >> %buildroot%_sysconfdir/qstat.cfg
#Remove Makefile from Doc directory
rm -f template/Makefile*

%files
%doc *.txt *.md *.html *.cfg template
%config %_sysconfdir/qstat.cfg
%_bindir/qstat

%changelog
* Wed Oct 13 2021 Konstantin Rybakov <kastet@altlinux.org> 2.17-alt1
- Updated to upstream version 2.17. 

* Wed Aug 25 2021 Aleksei Nikiforov <darktemplar@altlinux.org> 2.16-alt1
- Updated to upstream version 2.16.

* Fri Dec 04 2020 Aleksei Nikiforov <darktemplar@altlinux.org> 2.14-alt2.git.502167b
- Updated to latest upstream commit.
- Updated license.

* Fri Feb 08 2019 Konstantin Rybakov <kastet@altlinux.org> 2.14-alt1.85fbecb
- New version from upstream Git repository

* Mon Jul 17 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 2.11-alt2
- Fixed build with new toolchain

* Mon Apr 15 2013 Dmitry V. Levin (QA) <qa_ldv@altlinux.org> 2.11-alt1.qa1
- NMU: rebuilt for debuginfo.

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

