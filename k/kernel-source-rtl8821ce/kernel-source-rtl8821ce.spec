Name: kernel-source-rtl8821ce
Version: 5.5.2
Release: alt11.gita478095
Summary: Source for the rtl8821ce driver
License: GPLv2
Group: Development/Kernel
URL: https://github.com/tomaspinho/rtl8821ce.git
Packager: Kernel Maintainer Team <kernel@packages.altlinux.org>

Source: %name-%version.tar
Source1: blacklist-rtl8821ce.conf

BuildArch: noarch
BuildPreReq: kernel-build-tools

%description
Linux rtl8821ce driver for Realtek's Wi-Fi cards

%package -n rtl8821ce-blacklist
Summary: Blacklist modules for rtl8821ce
Group: System/Kernel and hardware

%description -n rtl8821ce-blacklist
Blacklist modules for correctly working module rtl8821ce

%prep
%setup -c

%install
mkdir -p %kernel_srcdir
tar -cjf %kernel_srcdir/%name-%version.tar.bz2 %name-%version
install -Dpm0644 %SOURCE1 %buildroot%_sysconfdir/modprobe.d/blacklist-rtl8821ce.conf

%files
%attr(0644,root,root) %kernel_src/%name-%version.tar.bz2

%files -n rtl8821ce-blacklist
%dir %_sysconfdir/modprobe.d
%config %_sysconfdir/modprobe.d/blacklist-rtl8821ce.conf

%changelog
* Wed Sep 13 2023 Andrey Cherepanov <cas@altlinux.org> 5.5.2-alt11.gita478095
- added package with blacklist rules for rtl8821ce.

* Thu May 25 2023 Andrey Cherepanov <cas@altlinux.org> 5.5.2-alt10.gita478095
- fixes for Linux 6.3

* Fri Jan 27 2023 Andrey Cherepanov <cas@altlinux.org> 5.5.2-alt9.gita3e2f7c
- fixes for Linux 6.1

* Wed Apr 20 2022 Andrey Cherepanov <cas@altlinux.org> 5.5.2-alt8.gitdce62b9
- fixes for Linux 5.17

* Tue Jan 25 2022 Andrey Cherepanov <cas@altlinux.org> 5.5.2-alt7.gitca204c6
- fixes for Linux 5.15

* Wed Aug 11 2021 Andrey Cherepanov <cas@altlinux.org> 5.5.2-alt6.gitf93db73
- fixes for Linux 5.12

* Wed Dec 16 2020 Valery Inozemtsev <shrek@altlinux.ru> 5.5.2-alt5
- fixes for Linux 5.10

* Wed Sep 02 2020 Valery Inozemtsev <shrek@altlinux.ru> 5.5.2-alt4
- fixes for Linux 5.8

* Thu Apr 30 2020 Valery Inozemtsev <shrek@altlinux.ru> 5.5.2-alt3
- v5.5.2_34066.20200325_COEX20180712-3232

* Mon Nov 25 2019 Valery Inozemtsev <shrek@altlinux.ru> 5.5.2-alt2
- fixes for Linux 5.3

* Mon Sep 30 2019 Valery Inozemtsev <shrek@altlinux.ru> 5.5.2-alt1
- v5.5.2

* Fri Mar 29 2019 Valery Inozemtsev <shrek@altlinux.ru> 5.2.5.1-alt1
- initial release

