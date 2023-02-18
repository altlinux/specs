# SPDX-License-Identifier: GPL-2.0-only
%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1
%ifnarch ppc64le
%set_verify_elf_method strict,lint=relaxed
%endif

%def_with gpu

Name: stress-ng
Version: 0.15.04
Release: alt1
Summary: Stress test a computer system in various selectable ways
Group: System/Kernel and hardware
License: GPL-2.0-only
Url: http://colinianking.github.io/stress-ng/
Vcs: https://github.com/ColinIanKing/stress-ng/

Source: %name-%version.tar

BuildRequires(pre): rpm-macros-make
BuildRequires: banner
BuildRequires: libaio-devel
BuildRequires: libattr-devel
BuildRequires: libbsd-devel
BuildRequires: libcap-devel
BuildRequires: libgcrypt-devel
BuildRequires: libjpeg-devel
BuildRequires: libjudy-devel
BuildRequires: libkeyutils-devel
BuildRequires: libkmod-devel
BuildRequires: liblksctp-devel
BuildRequires: libseccomp-devel
BuildRequires: libxxhash-devel
BuildRequires: zlib-devel
%if_with gpu
BuildRequires: libEGL-devel
BuildRequires: libgbm-devel
BuildRequires: libglvnd-devel
%endif

%description
stress-ng will stress test a computer system in various selectable
ways. It was designed to exercise various physical subsystems
of a computer as well as the various operating system kernel
interfaces. Stress-ng features:

  * 290+ stress tests
  * 80+ CPU specific stress tests that exercise floating point, integer,
    bit manipulation and control flow
  * 20+ virtual memory stress tests
  * 40+ file system stress tests
  * 30+ memory/CPU cache stress tests
  * portable: builds on Linux (Debian, Devuan, RHEL, Fedora, Centos, Slackware
    OpenSUSE, Ubuntu, etc..), Solaris, FreeBSD, NetBSD, OpenBSD, DragonFlyBSD,
    Minix, Android, MacOS X, Serenity OS, GNU/Hurd, Haiku, Windows Subsystem
    for Linux and SunOs/Dilos/Solaris.
    with gcc, clang, icc, tcc and pcc.
  * tested on alpha, armel, armhf, arm64, hppa, i386, m68k, mips32, mips64,
    power32, ppc64el, risc-v, sh4, s390x, sparc64, x86-64

%prep
%setup
%ifarch %e2k
# lcc 1.23 can't do string attribute form (1.24.03 will; mcst#4061)
sed -ri 's,"-O([0123])",\1,' stress-ng.h
%endif

%build
%make_build_ext --no-print-directory --output-sync=none VERBOSE=1

%install
%makeinstall_std

install -pD kernel-coverage.sh %buildroot%_datadir/stress-ng/kernel-coverage.sh
install -pDm644 syscalls.txt   %buildroot%_datadir/stress-ng/syscalls.txt
install -pD debian/tests/fast-test-all %buildroot%_datadir/stress-ng/fast-test-all
install -pD debian/tests/lite-test     %buildroot%_datadir/stress-ng/lite-test

%check
# getrandom test does not work in sborotschnitza:
#   getrandom using flags GRND_INSECURE failed, errno=22 (Invalid argument)
sed -i '/STRESSORS/s/getrandom //g' debian/tests/lite-test
# Cache test for a long time hanging ALT beekeeper for a unknown reason.
sed -i '/STRESSORS/s/ cache / /g' debian/tests/lite-test

banner lite-test
time timeout 300 make lite-test
banner done

%files
%define _customdocdir %_docdir/%name
%doc COPYING README.md mascot/stress-ng.svg debian/changelog
%_bindir/stress-ng
%_datadir/bash-completion/completions/stress-ng
%_datadir/stress-ng
%_mandir/man1/stress-ng.1*

%changelog
* Sun Feb 19 2023 Vitaly Chikunov <vt@altlinux.org> 0.15.04-alt1
- Update to V0.15.04 (2023-02-15).

* Sat Jan 21 2023 Vitaly Chikunov <vt@altlinux.org> 0.15.03-alt1
- Update to V0.15.03 (2023-01-19).

* Mon Jan 16 2023 Vitaly Chikunov <vt@altlinux.org> 0.15.02-alt1
- Update to V0.15.02 (2023-01-12).

* Mon Dec 19 2022 Vitaly Chikunov <vt@altlinux.org> 0.15.01-alt1
- Update to V0.15.01 (2022-12-13).

* Sat Nov 19 2022 Vitaly Chikunov <vt@altlinux.org> 0.15.00-alt1
- Update to V0.15.00 (2022-11-18).

* Mon Oct 03 2022 Vitaly Chikunov <vt@altlinux.org> 0.14.06-alt1
- Update to V0.14.06 (2022-09-27).
- Enable GPU stressors.

* Sun Sep 04 2022 Vitaly Chikunov <vt@altlinux.org> 0.14.03-alt2
- Workaround ALT beekeeper rebuild failure.

* Sun Jul 24 2022 Vitaly Chikunov <vt@altlinux.org> 0.14.03-alt1
- Update to V0.14.03 (2022-07-20).
- Change docdir /usr/share/doc/stress-ng-%%version -> /usr/share/doc/stress-ng.

* Mon Jun 13 2022 Vitaly Chikunov <vt@altlinux.org> 0.14.02-alt1
- Update to V0.14.02 (2022-06-12).

* Wed May 18 2022 Vitaly Chikunov <vt@altlinux.org> 0.14.01-alt1
- Update to V0.14.01 (2022-05-05).

* Fri Sep 17 2021 Vitaly Chikunov <vt@altlinux.org> 0.13.03-alt1
- Update to V0.13.03 (2021-09-17).

* Fri Sep 03 2021 Vitaly Chikunov <vt@altlinux.org> 0.13.01-alt1
- Update to V0.13.01 (2021-09-01).

* Mon Aug 09 2021 Vitaly Chikunov <vt@altlinux.org> 0.13.00-alt1
- Update to V0.13.00 (2021-08-02).

* Thu Jul 15 2021 Vitaly Chikunov <vt@altlinux.org> 0.12.12-alt1
- Update to V0.12.12 (2021-07-09).

* Fri Jul 02 2021 Vitaly Chikunov <vt@altlinux.org> 0.12.11-alt1
- Update to V0.12.11 (2021-06-24).

* Mon Jun 14 2021 Vitaly Chikunov <vt@altlinux.org> 0.12.10-alt1
- Update to V0.12.10 (2021-06-07).

* Wed Jun 02 2021 Vitaly Chikunov <vt@altlinux.org> 0.12.09-alt1
- Update to V0.12.09 (2021-05-22).

* Mon May 10 2021 Vitaly Chikunov <vt@altlinux.org> 0.12.08-alt1
- Update to V0.12.08 (2021-05-06).

* Fri Apr 30 2021 Vitaly Chikunov <vt@altlinux.org> 0.12.07-alt1
- Update to V0.12.07 (2021-04-21).

* Fri Mar 26 2021 Vitaly Chikunov <vt@altlinux.org> 0.12.06-alt1
- Update to V0.12.06 (2021-03-24).

* Mon Mar 15 2021 Vitaly Chikunov <vt@altlinux.org> 0.12.05-alt1
- Update to V0.12.05 (2021-03-12).

* Fri Feb 26 2021 Vitaly Chikunov <vt@altlinux.org> 0.12.04-alt1
- Update to V0.12.04 (2021-02-25) with update (2021-02-26).

* Thu Feb 18 2021 Vitaly Chikunov <vt@altlinux.org> 0.12.03-alt2
- spec: Disable cache test in %%check for ALT beekeeper.

* Mon Feb 15 2021 Vitaly Chikunov <vt@altlinux.org> 0.12.03-alt1
- Update to V0.12.03 (2021-02-13).

* Tue Jan 26 2021 Vitaly Chikunov <vt@altlinux.org> 0.12.02-alt2
- spec: Use libSegFault directly instead of catchsegv.

* Mon Jan 25 2021 Vitaly Chikunov <vt@altlinux.org> 0.12.02-alt1
- spec: Timeout and catchsegv for %%check.
- Update to V0.12.02 (2021-01-21).

* Thu Nov 12 2020 Vitaly Chikunov <vt@altlinux.org> 0.11.23-alt1
- Update to V0.11.23 (2020-10-30).
- spec: Add %%check section.

* Sat Jul 13 2019 Michael Shigorin <mike@altlinux.org> 0.09.60-alt2
- E2K: fix build with lcc 1.23

* Mon Jul 01 2019 Nikolai Kostrigin <nickel@altlinux.org> 0.09.60-alt1
- New version
- Spec: cleanup

* Sat Aug 11 2018 Vitaly Chikunov <vt@altlinux.org> 0.09.36-alt2
- First package for ALT
