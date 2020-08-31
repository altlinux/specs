# SPDX-License-Identifier: GPL-2.0-only
%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1

Name: stalld
Version: 1.0
Release: alt1
Summary: Daemon that finds starving tasks and gives them a temporary boost

License: GPL-2.0-only
Group: System/Kernel and hardware
Url: https://github.com/bristot/stalld
Vcs: https://github.com/bristot/stalld.git
# Presentation: https://linuxplumbersconf.org/event/7/contributions/769/
# Video: https://youtu.be/JHE_3iU9nTs?t=10608
# Slides: https://linuxplumbersconf.org/event/7/contributions/769/attachments/572/1010/OSnoise-RT.pdf
ExclusiveArch: x86_64

Source: %name-%version.tar

%description
The stalld program monitors the set of system threads, looking for threads
that are ready-to-run but have not been given processor time for some threshold
period. When a starving thread is found, it is given a temporary boost using
the SCHED_DEADLINE policy. The default is to allow 10 microseconds of runtime
for 1 second of clock time.

%prep
%setup
sed -i s/-lpthread/-pthread/ Makefile
sed -i /README.md/d Makefile

%build
%make_build

%install
%makeinstall_std
install -D -p -m 0644 redhat/stalld.service %buildroot%_unitdir/stalld.service
install -D -p -m 0644 redhat/stalld.conf %buildroot%_sysconfdir/systemd/stalld.conf

%post
%post_service stalld.service

%preun
%preun_service stalld.service

%files
%doc README.md
%config(noreplace) %_sysconfdir/systemd/stalld.conf
%_bindir/stalld
%_unitdir/stalld.service
%_man8dir/stalld.8*

%changelog
* Mon Aug 31 2020 Vitaly Chikunov <vt@altlinux.org> 1.0-alt1
- First build for ALT.
