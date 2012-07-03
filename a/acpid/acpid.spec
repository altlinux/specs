Name: acpid
Version: 2.0.15
Release: alt1
Epoch: 1
Summary: ACPI kernel daemon and control utility
License: GPL
Group: System/Servers
Url: http://www.tedfelix.com/linux/acpid-netlink.html
Packager: Valery Inozemtsev <shrek@altlinux.ru>

PreReq: sysvinit-utils

Source0: %name-%version.tar.xz
Source1: %name.init
Source2: %name.service

%description
The ACPI specification defines power and system management functions
for each computer, in a generic manner.  The ACPI daemon coordinates
the management of power and system functions when ACPI kernel
support is enabled (kernel 2.3.x or later).

%package events-power
Summary: Power event config
Group: System/Servers
PreReq: acpid = %version
Conflicts: acpid < 2.0.8

%description events-power
Power event config for acpid

%prep
%setup

%build
%autoreconf
%configure
%make_build

%install
%make DESTDIR=%buildroot install

install -pD -m755 %SOURCE1 %buildroot%_initdir/%name
install -pD -m644 %SOURCE2 %buildroot%systemd_unitdir/acpid.service

mkdir -p %buildroot%_sysconfdir/acpi/events
cat << __EOF__ > %buildroot%_sysconfdir/acpi/events/power
event=button/power
action=/sbin/poweroff
__EOF__

mkdir -p %buildroot%_sysconfdir/sysconfig
cat << __EOF__ > %buildroot%_sysconfdir/sysconfig/acpid
ACPID_ARGS="-n"
__EOF__

%post
if pidof %name >/dev/null 2>&1; then
	[ -f %_var/run/%name.pid ] || pidof %name > %_var/run/%name.pid
fi
%post_service %name

%preun
%preun_service %name

%files
%doc Changelog README TODO
%dir %_sysconfdir/acpi
%dir %_sysconfdir/acpi/events
%config(noreplace) %_sysconfdir/sysconfig/acpid
%_initdir/%name
%systemd_unitdir/acpid.service
%_bindir/*
%_sbindir/*
%_man8dir/*.8*

%files events-power
%config(noreplace) %_sysconfdir/acpi/events/power

%changelog
* Tue Mar 20 2012 Valery Inozemtsev <shrek@altlinux.ru> 1:2.0.15-alt1
- 2.0.15

* Wed Dec 28 2011 Valery Inozemtsev <shrek@altlinux.ru> 1:2.0.14-alt1
- 2.0.14

* Wed Nov 23 2011 Valery Inozemtsev <shrek@altlinux.ru> 1:2.0.13-alt1
- 2.0.13

* Fri Aug 19 2011 Valery Inozemtsev <shrek@altlinux.ru> 1:2.0.12-alt1
- 2.0.12

* Sun Aug 07 2011 Valery Inozemtsev <shrek@altlinux.ru> 1:2.0.11-alt1
- 2.0.11

* Fri May 27 2011 Valery Inozemtsev <shrek@altlinux.ru> 1:2.0.10-alt1
- 2.0.10

* Mon Apr 18 2011 Valery Inozemtsev <shrek@altlinux.ru> 1:2.0.9-alt1
- 2.0.9
- added systemd support (closes: #25461)

* Wed Mar 02 2011 Valery Inozemtsev <shrek@altlinux.ru> 1:2.0.8-alt1
- 2.0.8
- new subpackage acpid-events-power (closes: #25018)

* Sun Dec 05 2010 Valery Inozemtsev <shrek@altlinux.ru> 1:2.0.7-alt1
- 2.0.7

* Sun Sep 26 2010 Valery Inozemtsev <shrek@altlinux.ru> 1:2.0.6-alt1
- 2.0.6

* Fri Jun 25 2010 Valery Inozemtsev <shrek@altlinux.ru> 1:2.0.4-alt2
- renamed /etc/acpi/events/power.conf to /etc/acpi/events/power (closes: #23657)
- added /etc/sysconfig/acpid config

* Tue Apr 27 2010 Valery Inozemtsev <shrek@altlinux.ru> 1:2.0.4-alt1
- 2.0.4:
  + force netlink/input layer mode

* Thu Apr 23 2009 Valery Inozemtsev <shrek@altlinux.ru> 1:1.0.10-alt1
- 1.0.10

* Fri Mar 13 2009 Valery Inozemtsev <shrek@altlinux.ru> 1:1.0.8-alt3
- changed chkconfig 2345 35 65 -> 2345 10 65

* Mon Dec 15 2008 Valery Inozemtsev <shrek@altlinux.ru> 1:1.0.8-alt2
- drop acpid-1.0.8-alt-lockfile.patch

* Sat Dec 13 2008 Valery Inozemtsev <shrek@altlinux.ru> 1:1.0.8-alt1
- 1.0.8

* Sun Oct 26 2008 Andrey Rahmatullin <wrar@altlinux.ru> 1:1.0.6-alt3
- fix build

* Thu Oct 25 2007 Andrey Rahmatullin <wrar@altlinux.ru> 1:1.0.6-alt2
- remove logrotate script (thanks to raorn@)

* Sun Jul 01 2007 Andrey Rahmatullin <wrar@altlinux.ru> 1:1.0.6-alt1
- 1.0.6

* Thu Oct 20 2005 Andrey Rahmatullin <wrar@altlinux.ru> 1:1.0.4-alt6
- fix file descriptor leak (#8303)

* Thu Sep 08 2005 Andrey Rahmatullin <wrar@altlinux.ru> 1:1.0.4-alt5
- change service start/stop order (#7849)

* Sat Jul 23 2005 Andrey Rahmatullin <wrar@altlinux.ru> 1:1.0.4-alt4
- fix permissions on logrotate script and default event config
- fix Url
- fix building with gcc4 (just in case)

* Mon Mar 21 2005 Andrey Rahmatullin <wrar@altlinux.ru> 1:1.0.4-alt3
- fix logrotate script

* Wed Dec 29 2004 Andrey Rahmatullin <wrar@altlinux.ru> 1:1.0.4-alt2
- add logrotate config (#5425)

* Tue Dec 14 2004 Andrey Rahmatullin <wrar@altlinux.ru> 1:1.0.4-alt1
- 1.0.4
- spec cleanup

* Fri Sep 12 2003 Albert R. Valiev <darkstar@altlinux.ru> 1:1.0.2-alt3
- Fixed pidfile creation #2970

* Mon Aug 18 2003 Albert R. Valiev <darkstar@altlinux.ru> 1:1.0.2-alt2
- Added pid file creation to daemon

* Mon Jul 07 2003 Albert R. Valiev <darkstar@altlinux.ru> 1:1.0.2-alt1
- New version (get from orphaned)

* Mon Nov 26 2001 Konstantin Volckov <goldhead@altlinux.ru> 1.0-alt2
- Added man page

* Tue Nov 20 2001 Konstantin Volckov <goldhead@altlinux.ru> 1.0-alt1
- 1.0.0

* Thu Jun 14 2001 Konstantin Volckov <goldhead@altlinux.ru> 20010510-alt1
- New version of acpid daemon
- Added powertools utilities
- Fixed documentation

* Tue Mar 20 2001 Kostya Timoshenko <kt@petr.kz> 071100-ipl7mdk
- build for RE
