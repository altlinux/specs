%define base_name apt-conf
%define distro sisyphus
%define Distro Sisyphus

Name: %base_name-%distro
Version: 5.2
Release: alt1

Summary: A set of apt configuration files for %distribution %Distro
License: GPL
Group: System/Configuration/Packaging
Packager: Dmitry V. Levin <ldv@altlinux.org>

Source: %name-%version.tar

Provides: %base_name = %version-%release, %_sysconfdir/apt/pkgpriorities
PreReq: coreutils
Conflicts: apt <= 0:0.5.15cnc6-alt14
%{expand:%%global o_list apt-conf < 0:4.0 %(for n in Castle Compact Junior Master Spring branch desktop hpc junior master office-server platform5 school server terminal; do echo -n "apt-conf-$n "; done)}
%{?o_list:Obsoletes: %o_list}

%description
This package contains default apt configuration for %distribution %Distro.

%prep
%setup

%build
%make_build REPOSITORIES=sisyphus

%install
%makeinstall

%triggerpostun -- apt < 0.3.19cnc51-alt3 %{?o_list:%o_list}
f=%_sysconfdir/apt/sources.list
if [ ! -f "$f" ]; then
	if [ -f "$f".rpmsave ]; then
		cp -pf "$f".rpmsave "$f"
	elif [ -f "$f".rpmnew ]; then
		cp -pf "$f".rpmnew "$f"
	fi
fi

%files
%config(noreplace) %_sysconfdir/apt

%changelog
* Wed Apr 14 2010 Dmitry V. Levin <ldv@altlinux.org> 5.2-alt1
- Updated mirrors.

* Tue Jan 26 2010 Dmitry V. Levin <ldv@altlinux.org> 5.1-alt1
- Updated mirrors.

* Fri Feb 13 2009 Stanislav Ievlev <inger@altlinux.org> 5.0-alt5
- update database

* Fri Feb 06 2009 Stanislav Ievlev <inger@altlinux.org> 5.0-alt4
- publish list of compatible repositories

* Tue Feb 03 2009 Stanislav Ievlev <inger@altlinux.org> 5.0-alt3
- convert mirror and repository database to new format
- publish mirror and repository database for using in other programs

* Thu Nov 13 2008 Dmitry V. Levin <ldv@altlinux.org> 5.0-alt2
- Updated descriptions, updated obsoletes list.

* Thu Nov 13 2008 Stanislav Ievlev <inger@altlinux.org> 5.0-alt1
- Switched to new infrastructure.
- Updated mirrors list.

* Sun Jan 06 2008 Dmitry V. Levin <ldv@altlinux.org> 4.0-alt3
- Updated conflicts list (#12168).
- Removed dead mirrors: anyhost.ru, elterrus.org.
- Added new mirrors:
  distrib-coffee.ipsl.jussieu.fr (Institut Pierre Simon Laplace, France),
  ftp.heanet.ie (HEAnet, Ireland),
  mirror.yandex.ru (Yandex Linux mirror, Moscow).
- Added http:// mirrors.
- vendors.list.d/alt.list:
  + Created separate "security" and "updates" identities.
  + Removed "updates" from "alt" group.
  + Added "security" to "updates" group.

* Thu Apr 26 2007 Dmitry V. Levin <ldv@altlinux.org> 4.0-alt1
- Added sources.list.d/README.sisyphus file (mike@).
- vendors.list.d/alt.list:
  + Removed old security key.
  + Added updates and backports keys.

* Wed Apr 18 2007 Dmitry V. Levin <ldv@altlinux.org> 2.2-alt1
- Added Server to obsolete list.
- Removed dead mirrors: aiya, nluug.

* Mon Feb 27 2006 Dmitry V. Levin <ldv@altlinux.org> 2.1-alt1
- Commented out source entries in sisyphus.alt.list (#9048).
- Since we lost ibiblio and all its mirrors,
  removed stale files from sources.list.d.

* Thu Feb 02 2006 Dmitry V. Levin <ldv@altlinux.org> 2.0-alt1
- vendors.list:
  + Added security@ key [80EF7625].
  + Renamed to vendors.list.d/alt.list.
- sources.list:
  + Removed all non-Sisyphus sources.
  + Split by origin and placed to sources.list.d/ (#5327).
  + Added noarch sources (#7400).
  + Added mirrors:
    mirror.aiya.ru, ftp.anyhost.ru, ftp.unixcenter.ru.
- Build the package for each architecture since APT sources
  are arch-dependent.

* Tue Aug 16 2005 Alexey Gladkov <legion@altlinux.ru> 1.17-alt2
- spec bugfix:
  + conflict to previos apt version added.

* Wed Jul 20 2005 Alexey Gladkov <legion@altlinux.ru> 1.17-alt1
- vendors.list:
  + added incominger@ gpg key to able sign sisyphus hashs.

* Fri Aug 13 2004 Dmitry V. Levin <ldv@altlinux.org> 1.16-alt1
- sources.list:
  + added sisyphus.irkutsk.ru mirror.

* Mon May 24 2004 Dmitry V. Levin <ldv@altlinux.org> 1.15-alt1
- pkgpriorities:
  + added: python-modules-tkinter;
- sources.list:
  + removed urls for old distros;
  + added urls for new distros.

* Thu May 20 2004 Dmitry V. Levin <ldv@altlinux.org> 1.14-alt1
- pkgpriorities:
  + added: python-dev, maxima-bin-gcl.

* Tue Oct 21 2003 Dmitry V. Levin <ldv@altlinux.org> 1.13-alt1
- sources.list:
  + added urls for Compact 2.3.

* Fri Oct 03 2003 Dmitry V. Levin <ldv@altlinux.org> 1.12-alt1
- pkgpriorities:
  + added: kernel-doc, postfix.

* Fri Sep 26 2003 Dmitry V. Levin <ldv@altlinux.org> 1.11-alt1
- pkgpriorities:
  + removed all from "Standard" level;
  + added: libpam0, libpam0-devel.

* Wed Aug 20 2003 Dmitry V. Levin <ldv@altlinux.org> 1.10-alt1
- pkgpriorities:
  + added: libtool_1.5
  + removed: kernel24-headers

* Tue Mar 04 2003 Dmitry V. Levin <ldv@altlinux.org> 1.9-alt1
- sources.list:
  + added urls for master22 and junior22.

* Sun Dec 29 2002 Dmitry V. Levin <ldv@altlinux.org> 1.8-alt1
- sources.list:
  + added emacs support (#0001068);
  + added updates urls for upcoming master and junior;
  + reworked file generation logic.

* Thu Dec 19 2002 Dmitry V. Levin <ldv@altlinux.org> 1.7-alt2
- apt-conf-sisyphus: obsoletes apt-conf-* (again).

* Wed Dec 18 2002 Dmitry V. Levin <ldv@altlinux.org> 1.7-alt1
- pkgpriorities: added kernel24-headers.
- Added mirrors:
  ftp-linux.cc.gatech.edu (Georgia Tech Software Library);
  ftp.nluug.nl (Netherlands LUG);
  ftp.impb.psn.ru (Pushchino Scientific Center);
  linux4u.jinr.ru (Joint Institute for Nuclear Research, Dubna);
  ftp.mobicomk.ru (MegaFonGSM, Caucasus);
  ftp.ilim.ru (Ust-Ilimsk)
  elterrus.org (Elterrus Network Group, Israel).

* Wed Dec 04 2002 Dmitry V. Levin <ldv@altlinux.org> 1.6-alt2
- Packaged %_sysconfdir/apt directory.
- Added %_sysconfdir/apt/pkgpriorities.
- Added mirror: ftp.leo.org.
- apt-conf-sisyphus: obsoletes apt-conf-*.

* Sat Jul 20 2002 Dmitry V. Levin <ldv@altlinux.org> 1.5-alt1
- Changed BuildArch to "noarch".
- Added urls for "i686" repository (#0001068).
- Changed default repository component for sisyphus to "classic".

* Wed Jun 19 2002 Dmitry V. Levin <ldv@altlinux.org> 1.4-alt1
- Updated urls for sisyphus repositories.

* Mon Jun 03 2002 Dmitry V. Levin <ldv@altlinux.org> 1.3-alt1
- Added urls for contrib and classic repositories.

* Tue May 07 2002 Dmitry V. Levin <ldv@alt-linux.org> 1.2-alt1
- Updated urls for new Junior.

* Tue Apr 16 2002 Dmitry V. Levin <ldv@alt-linux.org> 1.1-alt1
- Added urls for new Master.
- Added new mirrors.

* Thu Mar 21 2002 Dmitry V. Levin <ldv@alt-linux.org> 1.0-alt2
- Fixed %%triggerpostun script.
- Uncomment only official sources.

* Wed Aug 01 2001 Dmitry V. Levin <ldv@altlinux.ru> 1.0-alt1
- Initial revision.
