Name: irqbalance
Version: 1.9.2
Release: alt1

Summary: Evenly distribute interrupt load across CPUs
License: GPLv2
Group: System/Kernel and hardware

Url: https://github.com/Irqbalance/irqbalance
Source: %name-%version.tar

BuildRequires: gccmakedep glib2-devel libcap-ng-devel libncurses-devel
%ifnarch armh
BuildRequires: libnuma-devel
%endif

%define sysconfig %_sysconfdir/sysconfig/%name

%description
irqbalance distributes interrupts over the processors and cores
you have in your computer system. The design goal of irqbalance
is to do find a balance between power savings and optimal
performance. To a large degree, the work irqbalance does is
invisible to you; if irqbalance performs its job right, nobody
will ever notice it's there or want to turn it off.

%prep
%setup
sed -i "s|/path/to/irqbalance.env|%sysconfig|g" misc/%name.service

%build
mkdir -p m4
%autoreconf
%configure
%make_build

%install
%makeinstall_std
install -pDm755 %name.init %buildroot%_initdir/%name
install -pDm644 misc/%name.env %buildroot%sysconfig
install -pDm644 misc/%name.service %buildroot%systemd_unitdir/%name.service

%preun
%preun_service %name

%post
%post_service %name

%files
%doc AUTHORS COPYING
%_sbindir/%name
%_sbindir/%name-ui
%config(noreplace) %sysconfig
%_initdir/%name
%_man1dir/%name.1*
%_man1dir/%name-ui.1*
%systemd_unitdir/%name.service

%changelog
* Tue Nov 01 2022 Anton Farygin <rider@altlinux.ru> 1.9.2-alt1
- 1.9.2

* Fri Oct 21 2022 Anton Farygin <rider@altlinux.ru> 1.9.1-alt1
- 1.9.1

* Thu Jun 23 2022 Anton Farygin <rider@altlinux.ru> 1.9.0-alt1
- 1.9.0

* Fri Apr 16 2021 Anton Farygin <rider@altlinux.ru> 1.8.0-alt1
- 1.8.0

* Mon Oct 12 2020 Anton Farygin <rider@altlinux.ru> 1.7.0-alt1
- 1.7.0

* Sun Jun 28 2020 Anton Farygin <rider@altlinux.ru> 1.6.0-alt1
- 1.6.0

* Wed May 01 2019 Anton Farygin <rider@altlinux.ru> 1.5.0-alt1
- 1.5.0

* Fri Oct 30 2015 Michael Shigorin <mike@altlinux.org> 1.0.9-alt1
- 1.0.9
- updated Url:
- minor spec cleanup

* Sat Dec 28 2013 Slava Dubrovskiy <dubrsl@altlinux.org> 1.0.7-alt1
- new version

* Mon Oct 07 2013 Slava Dubrovskiy <dubrsl@altlinux.org> 1.0.6-alt1
- new version

* Sun Jan 20 2013 Slava Dubrovskiy <dubrsl@altlinux.org> 1.0.5-alt1
- new version

* Wed Sep 05 2012 Slava Dubrovskiy <dubrsl@altlinux.org> 1.0.4-alt1
- new version

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
