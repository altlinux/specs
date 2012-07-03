Name: ksmtuned
Version: 1.0
Release: alt2

Summary: KSM
License: GPLv3
Group: Emulators

Url: http://gitorious.org/ksm-control-scripts/ksm-control-scripts/trees/master
Packager: Slava Dubrovskiy <dubrsl@altlinux.org>
BuildArch: noarch

Source: %name-%version.tar

%description
The Kernel Samepage Merging control Daemon is a simple script that controls whether (and with what vigor) should ksm search duplicated memory pages.

%prep
%setup

%install
install -pD -m644 ksm.sysconfig %buildroot%_sysconfdir/sysconfig/ksm
install -pD -m644 ksmtuned.conf %buildroot%_sysconfdir/ksmtuned.conf
install -pD -m755 ksm.init.alt %buildroot%_initdir/ksm
install -pD -m755 ksmtuned.init.alt %buildroot%_initdir/ksmtuned
install -pD -m755 ksmtuned %buildroot%_sbindir/ksmtuned

%files
%_sbindir/*
%_initdir/*
%_sysconfdir/sysconfig/*
%_sysconfdir/ksmtuned.conf


%post
%post_service %name
%post_service ksm

%preun
%preun_service %name
%preun_service ksm

%changelog
* Tue Jan 25 2011 Slava Dubrovskiy <dubrsl@altlinux.org> 1.0-alt2
- Rebuild and merge with upstream

* Sat Dec 27 2010 Viacheslav Biriukov <sample@altlinux.org> 1.0-alt1
- bild for ALT
