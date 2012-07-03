Name: irqbalance
Version: 1.0.3
Release: alt1

Summary: Evenly distribute interrupt load across CPUs
License: GPLv2
Group: System/Kernel and hardware

Url: https://code.google.com/p/irqbalance
Source: %name-%version.tar
Packager: Dmitry Lebkov <dlebkov@altlinux.ru>

BuildRequires: gccmakedep glib2-devel libcap-ng-devel libnuma-devel

%description
irqbalance distributes interrupts over the processors and cores
you have in your computer system. The design goal of irqbalance
is to do find a balance between power savings and optimal
performance. To a large degree, the work irqbalance does is
invisible to you; if irqbalance performs its job right, nobody
will ever notice it's there or want to turn it off.

%prep
%setup

%build
%autoreconf
%configure
%make_build

%install
install -pDm755 irqbalance %buildroot/%_sbindir/%name
install -pDm755 %name.init %buildroot/%_initdir/%name
install -pDm644 %name.sysconfig %buildroot/%_sysconfdir/sysconfig/%name
install -pDm644 %name.1 %buildroot/%_man1dir/%name.1
install -pDm644 misc/%name.service %buildroot/%systemd_unitdir/%name.service

%preun
%preun_service %name
%post
%post_service %name

%files
%doc AUTHORS COPYING
%_sbindir/%name
%config(noreplace) %_sysconfdir/sysconfig/%name
%_initdir/%name
%_man1dir/%name.1*
%systemd_unitdir/%name.service

%changelog
* Sun Feb 19 2012 Slava Dubrovskiy <dubrsl@altlinux.org> 1.0.3-alt1
- new version from new URL location
- migrate to git source, update spec
- add BuildRequires for libcap-ng-devel libnuma-devel
- add service for systemd
- fix (ALT #26959 26962)

* Sat Nov 19 2011 Anton Farygin <rider@altlinux.ru> 0.56-alt1
- new version

* Tue Feb 02 2010 Michael Shigorin <mike@altlinux.org> 0.55-alt4
- spec cleanup
- cleaned up and sent upstream the patch
- extended package description
- buildreq
- fixed License:

* Fri May 15 2009 Dmitry Lebkov <dlebkov@altlinux.ru> 0.55-alt3
- add LSB headers to init-script

* Mon Jun 30 2008 Dmitry Lebkov <dlebkov@altlinux.ru> 0.55-alt2
- fix BuiuldRequires

* Sun May 13 2007 Dmitry Lebkov <dlebkov@altlinux.ru> 0.55-alt1
- 0.55

* Sat Feb 25 2006 Dmitry Lebkov <dlebkov@altlinux.ru> 0.12-alt0
- inital package for ALT (based on RHEL4 kernel-utils)
