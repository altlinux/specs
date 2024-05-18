# SPDX-License-Identifier: GPL-2.0-only
%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1
%set_verify_elf_method strict

Name: stalld
Version: 1.19.3
Release: alt1
Summary: Daemon that finds starving tasks and gives them a temporary boost

License: GPL-2.0-only
Group: System/Kernel and hardware
Url: https://gitlab.com/rt-linux-tools/stalld
# Presentation: https://linuxplumbersconf.org/event/7/contributions/769/
# Video: https://youtu.be/JHE_3iU9nTs?t=10608
# Slides: https://linuxplumbersconf.org/event/7/contributions/769/attachments/572/1010/OSnoise-RT.pdf

Source: %name-%version.tar

%description
The stalld program monitors the set of system threads, looking for threads
that are ready-to-run but have not been given processor time for some threshold
period. When a starving thread is found, it is given a temporary boost using
the SCHED_DEADLINE policy. The default is to allow 10 microseconds of runtime
for 1 second of clock time.

%prep
%setup
%ifarch %e2k
# What is the reason for using hardcoded syscall numbers?
sed -i "1i #include <sys/syscall.h>" src/stalld.h
%endif
sed -i s/-lpthread/-pthread/ Makefile
sed -i /README.md/d Makefile
sed -i '1s!/usr/bin/bash!/bin/bash!' scripts/throttlectl.sh

%build
%add_optflags %(getconf LFS_CFLAGS)
# USE_BPF=0: https://gitlab.com/rt-linux-tools/stalld/-/issues/17
%make_build CFLAGS='%optflags -DVERSION=\"%version\"' USE_BPF=0

%install
%makeinstall_std UNITDIR=%_unitdir USE_BPF=0
rm %buildroot/usr/share/licenses/stalld/gpl-2.0.txt

%check
./stalld --version | grep -Fx '%version'
# Not much to test.
# https://gitlab.com/rt-linux-tools/stalld/-/issues/23

%post
%post_service stalld.service

%preun
%preun_service stalld.service

%files
%doc README.md gpl-2.0.txt
%config(noreplace) %_sysconfdir/sysconfig/stalld
%_bindir/stalld
%_bindir/throttlectl
%_unitdir/stalld.service
%_man8dir/stalld.8*

%changelog
* Sat May 18 2024 Vitaly Chikunov <vt@altlinux.org> 1.19.3-alt1
- Update to v1.19.3 (2024-05-16).

* Wed Dec 28 2022 Vitaly Chikunov <vt@altlinux.org> 1.17.2-alt1
- Update to v1.17.2 (2022-12-21).

* Sun Dec 04 2022 Ilya Kurdyukov <ilyakurdyukov@altlinux.org> 1.17.1-alt1.1
- Fixed build for Elbrus.

* Wed Oct 19 2022 Vitaly Chikunov <vt@altlinux.org> 1.17.1-alt1
- Update to v1.17.1 (2022-10-14).

* Wed Aug 17 2022 Vitaly Chikunov <vt@altlinux.org> 1.17.0-alt1
- Update to v1.17.0 (2022-07-14).

* Mon Aug 31 2020 Vitaly Chikunov <vt@altlinux.org> 1.0-alt1
- First build for ALT.
