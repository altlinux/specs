%define name fprobe-ulog
%define fprobedir %_localstatedir/%name
%define fuser _fprobe

Name: %name
Version: 1.1
Release: alt4
Summary: fprobe-ulog: a NetFlow probe
Group: Monitoring
License: GPL
Packager: Evgenii Terechkov <evg@altlinux.ru>
Url: http://fprobe.sourceforge.net
Source: %name-%version.tar.bz2
Source1: %name.init
Source2: %name.sysconfig

Patch0: %name-1.1-alt-omit-obsolete-setuser.patch

PreReq: shadow-utils

%description
fprobe-ulog - libipulog-based tool that collect network traffic data
and emit it as NetFlow flows towards the specified collector.

This daemon will be run in chroot()-ed environment as non-privileged
%fuser user.

Also note that package builded with security optimisation
(--with-hash=crc16). See included README for details.

%prep
%setup -q
%patch0 -p1

%build
%configure --sbindir=%_sbindir --with-piddir=/ --with-hash=crc16 --enable-messages
%make

%install
%makeinstall

mkdir -p %buildroot%_initdir
install %SOURCE1 %buildroot%_initdir/%name

mkdir -p %buildroot%_sysconfdir/sysconfig
install %SOURCE2 %buildroot%_sysconfdir/sysconfig/%name

mkdir -p %buildroot%fprobedir

%pre
/usr/sbin/useradd -r -d %fprobedir -s /dev/null %fuser >/dev/null 2>&1 ||:

%post
%post_service %name

%preun
%preun_service %name

%files
%_initdir/%name
%_sbindir/*
%_man8dir/*
%doc AUTHORS ChangeLog NEWS README COPYING TODO

%config(noreplace) %_sysconfdir/sysconfig/%name

%dir %attr(1775,root,%fuser) %fprobedir

%changelog
* Tue Sep 02 2008 Terechkov Evgenii <evg@altlinux.ru> 1.1-alt4
- Patch0 by lioka@ added (fixes #14162)

* Sat Dec  1 2007 Terechkov Evgenii <evg@altlinux.ru> 1.1-alt3.1
- Dir permission fixed according policy (see http://docs.altlinux.ru/alt/devel/ch01s03.html#id2884290)

* Sun Oct  7 2007 Terechkov Evgenii <evg@altlinux.ru> 1.1-alt3
- Repacked with security optimisation (--with-hash=crc16) and debug output of non-fatal runtime errors
- Init script (Source1) updated to workaround stale pidfile problem
- Minor spec changes and cleanups

* Tue Jun 12 2007 Terechkov Evgenii <evg@altlinux.ru> 1.1-alt2
- Startup race with flow-capture fixed

* Sat Sep 23 2006 Terechkov Evgenii <evg@altlinux.ru> 1.1-alt1
- Build for Sisyphus
- chroot-related aspects improved. Now will NOT run not-chrooted without hacking.
- pseudouser added instead nobody

* Mon Aug 21 2006 Terechkov Evgenii <evg@altlinux.ru> 1.1-alt0.C30.1
- Initial build for C30
