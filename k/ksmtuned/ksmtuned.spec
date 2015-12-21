Name: ksmtuned
Version: 1.0
Release: alt3

Summary: KSM
License: GPLv3
Group: Emulators

# dead site
Url: http://gitorious.org/ksm-control-scripts/ksm-control-scripts/trees/master
BuildArch: noarch

Source: %name-%version.tar

%description
The Kernel Samepage Merging control Daemon is a simple script that controls whether (and with what vigor) should ksm search duplicated memory pages.

%prep
%setup

%install
#ksm
#install -pD -m644 ksm.sysconfig %buildroot%_sysconfdir/sysconfig/ksm
#install -pD -m755 ksm.init %buildroot%_initdir/ksm
#install -pD -m644 ksm.service %buildroot%_unitdir/ksm.service

#ksmtuned
install -pD -m755 ksmtuned %buildroot%_sbindir/ksmtuned
install -pD -m644 ksmtuned.conf %buildroot%_sysconfdir/ksmtuned.conf
install -pD -m755 ksmtuned.init %buildroot%_initdir/ksmtuned
install -pD -m644 ksmtuned.service %buildroot%_unitdir/ksmtuned.service

%post
%post_service %name
# %post_service ksm

%preun
%preun_service %name
# %preun_service ksm

%files
%_sbindir/*
%_initdir/*
%_unitdir/*
# %config(noreplace) %_sysconfdir/sysconfig/*
%config(noreplace) %_sysconfdir/ksmtuned.conf

%changelog
* Mon Dec 21 2015 Alexey Shabalin <shaba@altlinux.ru> 1.0-alt3
- update initscript
- add systemd unit
- don't install ksm service

* Tue Jan 25 2011 Slava Dubrovskiy <dubrsl@altlinux.org> 1.0-alt2
- Rebuild and merge with upstream

* Sat Dec 27 2010 Viacheslav Biriukov <sample@altlinux.org> 1.0-alt1
- bild for ALT
