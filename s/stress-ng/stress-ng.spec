# SPDX-License-Identifier: GPL-2.0-only
%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1
%ifnarch ppc64le
%set_verify_elf_method strict,lint=relaxed
%endif

%def_with gpu

Name: stress-ng
Version: 0.18.01
Release: alt1
Summary: Stress test a computer system in various selectable ways
Group: System/Kernel and hardware
License: GPL-2.0-only
Url: https://github.com/ColinIanKing/stress-ng

Source: %name-%version.tar

BuildRequires(pre): rpm-macros-make
BuildRequires: banner
BuildRequires: libacl-devel
BuildRequires: libaio-devel
BuildRequires: libattr-devel
BuildRequires: libbsd-devel
BuildRequires: libcap-devel
BuildRequires: libgcrypt-devel
BuildRequires: libgmp-devel
BuildRequires: libjpeg-devel
BuildRequires: libjudy-devel
BuildRequires: libkeyutils-devel
BuildRequires: libkmod-devel
BuildRequires: liblksctp-devel
BuildRequires: libmpfr-devel
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

  * 320+ stress tests
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

stress-ng was originally intended to make a machine work hard and trip
hardware issues such as thermal overruns as well as operating system
bugs that only occur when a system is being thrashed hard. Use stress-ng
with caution as some of the tests can make a system run hot on poorly
designed hardware and also can cause excessive system thrashing which
may be difficult to stop.

stress-ng can also measure test throughput rates; this can be useful to
observe performance changes across different operating system releases
or types of hardware. However, it has never been intended to be used as
a precise benchmark test suite, so do NOT use it in this manner.

%prep
%setup
%ifarch %e2k
# lcc 1.23 can't do string attribute form (1.24.03 will; mcst#4061)
sed -ri 's,"-O([0123])",\1,' stress-ng.h
%endif

%build
%ifarch ppc64le
# Disable LTO as is does not build on ppc64:
#   https://github.com/ColinIanKing/stress-ng/issues/273
#   {standard input}: Assembler messages:
#   {standard input}:20240: Error: unrecognized opcode: `darn'
%define optflags_lto %nil
%endif
%make_build_ext --no-print-directory --output-sync=none VERBOSE=1

%install
%makeinstall_std

install -pD kernel-coverage.sh %buildroot%_datadir/stress-ng/kernel-coverage.sh
install -pDm644 syscalls.txt   %buildroot%_datadir/stress-ng/syscalls.txt
install -pD debian/tests/fast-test-all %buildroot%_datadir/stress-ng/fast-test-all
install -pD debian/tests/lite-test     %buildroot%_datadir/stress-ng/lite-test

%check
# Cache test for a long time hanging ALT beekeeper for a unknown reason.
sed -i '/STRESSORS/s/ cache / /g' debian/tests/lite-test

banner lite-test
time timeout 300 make lite-test V=1
banner done

%files
%define _customdocdir %_docdir/%name
%doc COPYING README.md mascot/stress-ng.svg debian/changelog
%_bindir/stress-ng
%_datadir/bash-completion/completions/stress-ng
%_datadir/stress-ng
%_mandir/man1/stress-ng.1*

%changelog
* Thu Jul 04 2024 Vitaly Chikunov <vt@altlinux.org> 0.18.01-alt1
- Update to V0.18.01 (2024-07-03).

* Thu Jun 06 2024 Vitaly Chikunov <vt@altlinux.org> 0.18.00-alt1
- Update to V0.18.00 (2024-06-06).

* Thu May 02 2024 Vitaly Chikunov <vt@altlinux.org> 0.17.08-alt1
- Update to V0.17.08 (2024-05-02).

* Fri Apr 05 2024 Vitaly Chikunov <vt@altlinux.org> 0.17.07-alt1
- Update to V0.17.07 (2024-04-04).

* Wed Mar 06 2024 Vitaly Chikunov <vt@altlinux.org> 0.17.06-alt1
- Update to V0.17.06 (2024-03-05).

* Sat Feb 03 2024 Vitaly Chikunov <vt@altlinux.org> 0.17.05-alt1
- Update to V0.17.05 (2024-02-01).
- Enable libacl support.

* Sat Jan 06 2024 Vitaly Chikunov <vt@altlinux.org> 0.17.04-alt1
- Update to V0.17.04 (2024-01-05).

* Sun Dec 10 2023 Vitaly Chikunov <vt@altlinux.org> 0.17.03-alt1
- Update to V0.17.03 (2023-12-09).

* Sat Dec 09 2023 Vitaly Chikunov <vt@altlinux.org> 0.17.02-alt1
- Update to V0.17.02 (2023-12-07).

* Fri Nov 10 2023 Vitaly Chikunov <vt@altlinux.org> 0.17.01-alt1
- Update to V0.17.01 (2023-11-09).

* Wed Oct 11 2023 Vitaly Chikunov <vt@altlinux.org> 0.17.00-alt1
- Update to V0.17.00 (2023-10-08).

* Tue Sep 05 2023 Vitaly Chikunov <vt@altlinux.org> 0.16.05-alt1
- Update to V0.16.05 (2023-09-05).

* Mon Aug 14 2023 Vitaly Chikunov <vt@altlinux.org> 0.16.04-alt1
- Update to V0.16.04 (2023-08-13).

* Sat Aug 12 2023 Vitaly Chikunov <vt@altlinux.org> 0.16.03-alt1
- Update to V0.16.03 (2023-08-11).

* Fri Jul 14 2023 Vitaly Chikunov <vt@altlinux.org> 0.16.02-alt1
- Update to V0.16.02 (2023-07-13).

* Thu Jul 13 2023 Vitaly Chikunov <vt@altlinux.org> 0.16.01-alt1
- Update to V0.16.01 (2023-07-11).

* Sun Jul 09 2023 Vitaly Chikunov <vt@altlinux.org> 0.16.00-alt1
- Update to V0.16.00 (2023-07-07).

* Thu Jun 15 2023 Vitaly Chikunov <vt@altlinux.org> 0.15.10-alt1
- Update to V0.15.10 (2023-06-15).

* Mon May 22 2023 Vitaly Chikunov <vt@altlinux.org> 0.15.08-alt1
- Update to V0.15.08 (2023-05-21).

* Sat Apr 15 2023 Vitaly Chikunov <vt@altlinux.org> 0.15.07-alt1
- Update to V0.15.07 (2023-04-13).

* Fri Mar 17 2023 Vitaly Chikunov <vt@altlinux.org> 0.15.06-alt1
- Update to V0.15.06 (2023-03-16).

* Sat Mar 11 2023 Vitaly Chikunov <vt@altlinux.org> 0.15.05-alt1
- Update to V0.15.05 (2023-03-09).

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
