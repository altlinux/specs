Name: powermgmt-base
Version: 1.38
Release: alt1

Summary: Common utils for power management
License: GPL-2.0-or-later
BuildArch: noarch
Group: System/Base
# http://deb.debian.org/debian/pool/main/p/powermgmt-base/powermgmt-base_%version.tar.xz
Source: %name-%version.tar
Patch: %name-%version-%release.patch


%define _unpackaged_files_terminate_build 1

%description
This package ships the following scripts:
 * on_ac_power: determine whether the system is powered from battery or
   an abundant supply
 * lspower: list power sources the system knows about, and their status

%prep
%setup
%patch -p1

%build

%install
for script in on_ac_power lspower; do
	install -pDm755 "$script" %buildroot%_bindir/"$script"
	install -pDm644 man/"$script".1 %buildroot%_man1dir/"$script".1
done

%files
%doc power_supply.txt
%_bindir/*
%_man1dir/*

%changelog
* Thu Sep 04 2025 Mikhail Efremov <sem@altlinux.org> 1.38-alt1
- lspower: Use 'echo -e'.
- lspower: Don't try to read non-existent files.
- Updated to 1.38 (package resurrected).

* Fri Apr 19 2013 Dmitry V. Levin (QA) <qa_ldv@altlinux.org> 1.22-alt1.qa1
- NMU: rebuilt for debuginfo.

* Sat Jun 11 2005 Dmitry V. Levin <ldv@altlinux.org> 1.22-alt1
- Updated to 1.21.
- scripts.d/hwclock: do nothing if clock is in synced mode.

* Mon Sep 06 2004 Dmitry V. Levin <ldv@altlinux.org> 1.21-alt1
- Updated to 1.21.
- Disabled console script (#4725).

* Mon Apr 19 2004 Dmitry V. Levin <ldv@altlinux.org> 1.20-alt1
- Imported from Debian.
- Implemented several basic apm scripts.
