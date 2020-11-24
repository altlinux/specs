%define distro Sisyphus
%define timestamp 20201124
%{expand: %%global code %([ -n '' ] && echo '' || echo %timestamp)}
%define dtext %distribution %distro
%define text_file %dtext (%code)
%{expand: %%global ldistro %(echo %distro |tr '[:upper:]' '[:lower:]')}
%define provide_list altlinux fedora redhat system
%define obsolete_list 4.0 4.1 5.0 5.1 c6 c7 c7.1 c8 c8.1 c9f1 c9m1 chainmail desktop homeros hpc icarus junior master office-server p5 p6 p7 p8 p9 school-server server sisyphus skif small_business t6 t7 terminal
%define conflicts_list Platform6-server-light alt-education alt-server alt-server-v alt-sisyphus alt-spserver alt-spworkstation alt-starterkit alt-tonk alt-workstation altlinux-backup-server altlinux-centaurus altlinux-desktop altlinux-gnome-desktop altlinux-kdesktop altlinux-lite altlinux-lxdesktop altlinux-office-desktop altlinux-office-server altlinux-p7 altlinux-school-server altlinux-sisyphus altlinux-spt altlinux-starterkit altlinux-tablet altlinux-workbench informika-schoolmaster ivk-chainmail lxde-desktop lxde-school-lite school-junior school-lite school-master school-server school-teacher school-terminal simply-linux sisyphus-server-light xalt-kworkstation

Name: altlinux-release-%ldistro
Version: %timestamp
Release: alt1

Summary: %dtext release files
License: GPLv2+
Group: System/Configuration/Other
BuildArch: noarch

Provides: %(for n in %provide_list; do echo -n "$n-release = %version-%release "; done)
Obsoletes: %(for n in %provide_list; do echo -n "$n-release < %version "; done)
Obsoletes: altlinux-4.0
Obsoletes: %(for n in %obsolete_list; do [ "$n" = "%ldistro" ] || echo -n "altlinux-release-$n "; done)
Conflicts: %(for n in %conflicts_list; do echo -n "branding-$n-release "; done)

%description
This package contains %dtext release files.

%install
install -pD -m644 /dev/null %buildroot%_sysconfdir/buildreqs/packages/ignore.d/%name
echo "%text_file" >%buildroot%_sysconfdir/altlinux-release
for n in fedora redhat system; do
	ln -s altlinux-release %buildroot%_sysconfdir/$n-release
done

cat > %buildroot%_sysconfdir/os-release <<-__EOF__
	NAME=%distro
	VERSION=%version
	ID=altlinux
	VERSION_ID=%version
	PRETTY_NAME="%dtext"
	ANSI_COLOR="1;33"
	CPE_NAME="cpe:/o:alt:%ldistro:%version"
	HOME_URL="https://www.altlinux.org"
	BUG_REPORT_URL="https://bugzilla.altlinux.org"
__EOF__

mkdir -p %buildroot%_rpmmacrosdir
cat > %buildroot%_rpmmacrosdir/altlinux-release <<-__EOF__
	%%_priority_distbranch	%ldistro
__EOF__

%define _unpackaged_files_terminate_build 1

%files
%_sysconfdir/*-*
%_sysconfdir/buildreqs/packages/ignore.d/*
%_rpmmacrosdir/altlinux-release

%changelog
* Tue Nov 24 2020 Dmitry V. Levin <ldv@altlinux.org> 20201124-alt1
- Fixed license tag.
- Updated Obsoletes list.
- Added conflicts with all known branding-*-release packages.
- Packaged /etc/os-release file (see #37565).
- Packaged %_rpmmacrosdir/altlinux-release file (see #37192).

* Mon Dec 22 2008 Dmitry V. Levin <ldv@altlinux.org> 20081222-alt1
- Updated Obsoletes list.

* Thu Dec 20 2007 Dmitry V. Levin <ldv@altlinux.org> 20071221-alt1
- Updated Obsoletes list.

* Thu Dec 06 2007 Dmitry V. Levin <ldv@altlinux.org> 20071206-alt1
- Updated Provides/Obsoletes lists and /etc/*-release symlinks.
- Renamed from altlinux-release to altlinux-release-sisyphus.

* Fri Feb 14 2003 Dmitry V. Levin <ldv@altlinux.org> Sisyphus-alt20030214
- Enhanced %%ifdef logic.

* Tue Dec 31 2002 Dmitry V. Levin <ldv@altlinux.org> Sisyphus-alt20021231
- Implemented %%ifdef logic.

* Wed Aug 14 2002 Dmitry V. Levin <ldv@altlinux.org> Sisyphus-alt20020814
- Added %_sysconfdir/buildreqs/packages/ignore.d/%name.

* Mon Apr 23 2001 Dmitry V. Levin <ldv@altlinux.ru> Sisyphus-alt20010423
- Renamed to altlinux-release.

* Wed Jan 10 2001 Dmitry V. Levin <ldv@fandra.org> 7.2-ipl0.20010111
- Renamed to %name.
- Implemented autoversioning.

* Wed Dec 27 2000 Dmitry V. Levin <ldv@fandra.org> 7.2-ipl0.20001227
- Set 8-digit timestamp number.

* Tue Dec 26 2000 AEN <aen@logic.ru>
- adopted for sisyphus

* Thu Oct  5 2000 Warly <warly@mandrakesoft.com> 7.2-1mdk
- Odyssey
