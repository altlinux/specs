%define _unpackaged_files_terminate_build 1

Name: update-kernel
Version: 1.5
Release: alt1
Summary: Update kernel and modules
License: GPL-2.0-or-later
Group: System/Kernel and hardware
Url: https://www.altlinux.org/update-kernel

Source: %name-%version.tar
BuildArch: noarch
%{?!_without_check:%{?!_disable_check:
BuildRequires: shellcheck
}}

Requires: apt
Requires: /usr/bin/rpmevrcmp
# May use rpm -q with an Epoch in the pkg argument (as well as Buildtime and
# Disttag -- but these are dependent on the output from APT, and APT cares
# about the correct dependencies on such features).
Requires: RPMQ(EPOCH)

%description
This package contains a script to conveniently update kernel and
modules.

It operates by installing a new package set in conjunction with your
existing kernel, ensuring that you do not lose the ability to boot your
reliable old kernel. By default, it searches for the most recent package
of the same flavor (e.g. "std-def") and aims to install all the same
modules that are already installed for that flavor.

This is recommended way of upgrading kernel for ALT Linux.

%prep
%setup

%install
mkdir -p %buildroot%_sbindir
install -pm755 update-kernel %buildroot%_sbindir/
install -pm755 remove-old-kernels %buildroot%_sbindir/
install -pm755 analyze-kmodules %buildroot%_sbindir/
install -Dp update-kernel.8 -t %buildroot%_man8dir/
install -Dp update-kernel.8.ru %buildroot%_mandir/ru/man8/update-kernel.8
install -Dp bash_completion %buildroot/usr/share/bash-completion/completions/update-kernel
ln -sf update-kernel %buildroot/usr/share/bash-completion/completions/remove-old-kernels

%check
make check

%files
%_sbindir/update-kernel
%_sbindir/remove-old-kernels
%_sbindir/analyze-kmodules
%_man8dir/*.8*
%_mandir/ru/man8/*.8*
%_datadir/bash-completion/completions/*

%changelog
* Thu Feb 09 2023 Vitaly Chikunov <vt@altlinux.org> 1.5-alt1
- Rephrase some messages. Small speedup improvement. Add Url.

* Wed Oct 05 2022 Vitaly Chikunov <vt@altlinux.org> 1.4-alt3
- Add simple bash_completion support.

* Tue Oct 04 2022 Vitaly Chikunov <vt@altlinux.org> 1.4-alt2
- Add update-kernel(8) man page (Anton Shevtsov, ALT#43934).

* Sat Jul 16 2022 Vitaly Chikunov <vt@altlinux.org> 1.4-alt1
- update-kernel: Only check booted kernel for external modules compatibility
  and remove red colored warnings.

* Thu Jun 30 2022 Vitaly Chikunov <vt@altlinux.org> 1.3.1-alt1
- Output some minor warnings in yellow instead of red.
- remove-old-kernels: Do not keep backup kernel with '-B' (reproducing old
  behavior.)

* Sun Jun 26 2022 Vitaly Chikunov <vt@altlinux.org> 1.3-alt1
- remove-old-kernels: Show list of kernel that won't be removed and why.
- remove-old-kernels: Add colors to improve UI (for a dark background).
- remove-old-kernels: Do not remove previous kernel with good uptime (backup
  kernel) as safeguarding measure. (ALT#43062)
- remove-old-kernels: Slightly change confirmation logic (do not leave
  confirmation to apt-get.)
- remove-old-kernels: Add -A option to attempt to remove other flavours
  completely (which was previously impossible).

* Sun Jun 19 2022 Vitaly Chikunov <vt@altlinux.org> 1.2.2-alt1
- update-kernel: Add --add (-A) option(s) to install external module.

* Mon May 23 2022 Vitaly Chikunov <vt@altlinux.org> 1.2.1-alt2
- update-kernel: Minor spelling fixes.

* Tue Apr 12 2022 Vitaly Chikunov <vt@altlinux.org> 1.2.1-alt1
- update-kernel: Do not suggest fresher flavour. (ALT#42400)

* Sun Apr 10 2022 Vitaly Chikunov <vt@altlinux.org> 1.2-alt1
- Improve wording of some messages.
- Add experimental analyze-kmodules tool.

* Sun Apr 10 2022 Vitaly Chikunov <vt@altlinux.org> 1.1.1-alt1
- Minor improvements.

* Fri Apr 08 2022 Vitaly Chikunov <vt@altlinux.org> 1.1-alt1
- Add '--headers' option to update-kernel to install kernel-headers.
- Check presence of external modules in the selected kernel.

* Fri Apr 08 2022 Vitaly Chikunov <vt@altlinux.org> 1.0.1-alt1
- Rework interactive mode UI (ALT#42321).
- '-i' can be used at any time to add new modules to the system.
- Interactive module selection happen before kernel install.
- Install kernel-headers and external modules together with the kernel in one
  transaction.
- Colorize & brighten some important messages.
- Call sync after install.

* Mon Apr 04 2022 Vitaly Chikunov <vt@altlinux.org> 0.9.21-alt1
- Tools cannot be used under user anymore because sudo sub-invocation is
  removed (call them under root instead).
- Require explicit yes or enter to start installation (previously any key work
  work except no).
- Improve package version comparison (ALT#42149).
- Do not show epoch and disttag in package names.
- Warn user if installed package (1 month) or APT database (1 day) are stalled.
- Do not require install of 'apt-scripts' for package availability mark in
  list mode.
- Show package age in list mode.

* Thu Nov 19 2020 Vitaly Chikunov <vt@altlinux.org> 0.9.20-alt1
- update-kernel: Fix and improve -r option (closes: #39041).
- update-kernel: Add --list option.

* Mon Aug 03 2020 Sergey Novikov <sotor@altlinux.org> 0.9.19-alt1
- update-kernel: fix incorrect comparison of versions of duplicate modules
  (closes: #38772)

* Wed Feb 12 2020 Vitaly Chikunov <vt@altlinux.org> 0.9.18-alt1
- Support for single word kernel flavours (closes: #36835).
- Update license tag to be more specific.

* Mon Dec 30 2019 Sergey Novikov <sotor@altlinux.org> 0.9.17-alt1
- update-kernel: remove duplicates modules entries (Closes: #37690)

* Fri Dec 20 2019 Oleg Solovyov <mcpain@altlinux.org> 0.9.16-alt1
- NMU: do not call apt when there are no kernels to remove

* Thu Dec 19 2019 Oleg Solovyov <mcpain@altlinux.org> 0.9.15-alt1
- NMU: protect latest kernel from removing (Closes: #34314)
- NMU: add "-a|--all" option to remove kernels with all flavours
  (Closes: #34141)

* Wed Jun 05 2019 Ivan Zakharyaschev <imz@altlinux.org> 0.9.14-alt1
- update-kernel: fixed in the presence of disttags in package IDs
  printed by APT (apt-cache pkgnames).

* Tue May 28 2019 Ivan Zakharyaschev <imz@altlinux.org> 0.9.13-alt1
- remove-old-kernels: APT invocation (to remove installed pkgs) rewritten in
  a more portable way. (A preparation for APT with support for disttags.)

* Wed May 15 2019 Ivan Zakharyaschev <imz@altlinux.org> 0.9.12-alt1
- APT invocation (to install the modules) rewritten in a more robust way.
  (A preparation for APT with support for disttags.)

* Mon Apr 01 2019 Ivan Zakharyaschev <imz@altlinux.org> 0.9.11-alt2
- Rewritten with another bashism that doesn't require /proc/.
- Requires: apt (important not for real systems, but for testing in hasher).

* Wed Aug 22 2018 Vitaly Lipatov <lav@altlinux.ru> 0.9.11-alt1
- add -y option as alias for -f (force operation) (ALT bug 35283)

* Fri Aug 04 2017 Vitaly Lipatov <lav@altlinux.ru> 0.9.10-alt1
- force select newest kernel module package (ALT bug 22572)

* Sun Apr 24 2016 Vitaly Lipatov <lav@altlinux.ru> 0.9.9-alt1
- remove-old-kernels: check only current flavour (or used with -t) (ALT bug #30717)
- remove-old-kernels: do not delete current or newest kernel(s)

* Sat Jan 23 2016 Terechkov Evgenii <evg@altlinux.org> 0.9.8-alt1
- Add help/force/dry-run options to remove-old-kernels

* Sun Aug 23 2015 Vitaly Lipatov <lav@altlinux.ru> 0.9.7-alt1
- check if we already have latest kernel package (alt bug #26715)

* Thu Jul 11 2013 Vitaly Lipatov <lav@altlinux.ru> 0.9.6-alt1
- skip install if the latest kernel is already installed (ALT bug #26715)

* Tue Dec 25 2012 Terechkov Evgenii <evg@altlinux.org> 0.9.5-alt1
- Add --download-only (--dry-run/-n) support (ALT#25300)

* Thu Dec 16 2010 Anton V. Boyarshinov <boyarsh@altlinux.ru> 0.9.4-alt2
- don't try to install unexistent modules

* Thu Dec 09 2010 Anton Protopopov <aspsk@altlinux.org> 0.9.4-alt1
- Install kernel and modules together

* Tue Sep 28 2010 Vladimir V. Kamarzin <vvk@altlinux.org> 0.9.3-alt1
[Dmitriy Kulik]
- Add interactive mode (-i)
- Add option -a|--all for installing all modules (Closes: #22271)

* Sat Oct 17 2009 Michael Shigorin <mike@altlinux.org> 0.9.2-alt1
- removed warning on x11setupdrv absence due to its obsolescence
  (closes: #21872)

* Mon Aug 31 2009 Michael Shigorin <mike@altlinux.org> 0.9.1-alt1
- added one-liner to fix path to x11presetdrv (closes: #21301)

* Thu Mar 05 2009 Vladimir V. Kamarzin <vvk@altlinux.org> 0.9-alt1
- Add x11presetdrv calling (mike)
- Add ldconfig call after x11setupdrv (mike)
- Remove message about updating kernel-headers and kernel-headers-modules

* Thu Feb 26 2009 Vladimir V. Kamarzin <vvk@altlinux.org> 0.8.1-alt1
- update_kernel: run x11setupdrv only if Xorg present

* Sun Dec 28 2008 Vladimir V. Kamarzin <vvk@altlinux.org> 0.8-alt1
- update_kernel: update kernel-headers and kernel-headers-modules also
  (me, kipruss) (Closes: #18259)
- Add new script remove-old-kernels. It removes all kernels except current
  (Closes: #14764)

* Mon Nov 24 2008 Vladimir V. Kamarzin <vvk@altlinux.org> 0.7-alt1
- Use rpmevrcmp instead of rpmvercmp
- Use only serial/epoch+version+release when comparing versions

* Mon Sep 22 2008 Vladimir V. Kamarzin <vvk@altlinux.org> 0.6-alt1
- Run x11setupdrv if needed (mike)
- Spelling fixes (mike)

* Mon Sep 01 2008 Vladimir V Kamarzin <vvk@altlinux.org> 0.5-alt1
- Fix module-names calculation (Closes: #16946)

* Tue Apr 22 2008 Vladimir V Kamarzin <vvk@altlinux.ru> 0.4-alt1
- Rewrite modules upgrading procedure (Closes: #15380)

* Tue Apr 15 2008 Vladimir V Kamarzin <vvk@altlinux.ru> 0.3-alt4
- update_kernel: bugfix in options parser

* Fri Apr 11 2008 Vladimir V Kamarzin <vvk@altlinux.ru> 0.3-alt3
- Set dependency on /usr/bin/rpmvercmp instead of rpm-utils

* Thu Mar 13 2008 Vladimir V Kamarzin <vvk@altlinux.ru> 0.3-alt2
- Add dependency on rpm-utils

* Wed Mar 12 2008 Vladimir V Kamarzin <vvk@altlinux.ru> 0.3-alt1
- update-kernel:
  + use rpmvercmp(1) for getting newest kernel package name
  + old code for manual choosing of kernel flavour/release replaced with
  options -t/-r

* Mon Mar 03 2008 Vladimir V Kamarzin <vvk@altlinux.ru> 0.2-alt1
- update-kernel:
  + implemented "force" mode
  + recode script to utf8
  + update copyright header

* Mon Feb 18 2008 Michael Shigorin <mike@altlinux.org> 0.1-alt2
- clarified License: (with lav@)
- noarch

* Sun Feb 17 2008 Michael Shigorin <mike@altlinux.org> 0.1-alt1
- initial package
- many thanks to Vitaly Lipatov (lav@) and Anatoly Kitouwaykin (cetus)
  for writing and improving the script -- I just had to package it

