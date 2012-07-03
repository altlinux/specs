Name:		net-scripts
Version:	0.5.6
Release:	alt1
Summary:	The system network scripts
Summary(ru_RU.KOI8-R): Системные сценарии для управления сетью
License:	GPL
Group:		System/Base
Packager:	Denis Ovsienko <pilot@altlinux.ru>
Source:		%name-%version.tar
PreReq:		setup >= 0:2.1.9-ipl18mdk, service, startup >= 0:0.9.3-alt1, chkconfig, control
Requires:	iproute2
Conflicts:	initscripts < 1:5.49.1-alt1, ppp-common < 0:0.3
Conflicts:	ppp < 0:2.3.9, wvdial < 0:1.40
BuildRequires:	glib-devel libpopt-devel
Provides:	network-config-subsystem

%description
This package contains the basic system scripts that activate
and deactivate most network interfaces.

%description -l ru_RU.KOI8-R
Этот пакет содержит базовые системные сценарии, которые
активируют и деактивируют большинство сетевых интерфейсов.

%prep
%setup -q

%build
make -C src

%install
rln()
{
	local target=$1 && shift
	local source=$1 && shift
	target=`relative "$target" "$source"`
	ln -snf "$target" "%buildroot$source"
}

%make_install install -C src DESTDIR=%buildroot

mkdir -p %buildroot%_sysconfdir
cp -a rc.d sysconfig %buildroot%_sysconfdir/
for n in ifup ifdown; do 
	mv %buildroot%_sysconfdir/sysconfig/network-scripts/$n \
		%buildroot/sbin/
	rln /sbin/$n %_sysconfdir/sysconfig/network-scripts/
done

touch %buildroot%_sysconfdir/sysconfig/network
chmod -R +x %buildroot{/sbin,%_sysconfdir/{rc.d,sysconfig/network-scripts}}
rln %_docdir/%name-%version/README \
	%_sysconfdir/sysconfig/network-scripts/

mkdir -p %buildroot/var/{log,run/netreport}

%pre
if [ $1 -ge 2 ]; then
	/usr/sbin/control-dump usernetctl
fi

%post
if [ $1 -ge 2 ]; then
	/usr/sbin/control-restore usernetctl
else
	/sbin/chkconfig --add network
fi

%preun
if [ $1 -eq 0 ]; then
	/sbin/chkconfig --del network
fi

%triggerpostun -- initscripts < 1:5.49.1-alt1
for f in %_sysconfdir/sysconfig/{network,vlan}; do
	if [ ! -f "$f" ]; then
	        if [ -f "$f".rpmsave ]; then
	                %__cp -pf "$f".rpmsave "$f"
	        elif [ -f "$f".rpmnew ]; then
	                %__cp -pf "$f".rpmnew "$f"
	        fi
	fi
done
/sbin/chkconfig --add network

%files
%config(noreplace) %verify(not md5 mtime size) %_sysconfdir/sysconfig/network
%config(noreplace) %verify(not md5 mtime size) %_sysconfdir/sysconfig/vlan
%config %_sysconfdir/rc.d/init.d/*
%config /etc/control.d/facilities/usernetctl
# TODO: those two can produce 2 dead links in sbin
%config /sbin/ifup
%config /sbin/ifdown
%dir %_sysconfdir/sysconfig/network-scripts
%config %_sysconfdir/sysconfig/network-scripts/ifcfg-*
%config %_sysconfdir/sysconfig/network-scripts/sysctl.conf
%_sysconfdir/sysconfig/network-scripts/ifdown*
%_sysconfdir/sysconfig/network-scripts/ifup*
%_sysconfdir/sysconfig/network-scripts/network-functions*
%doc %_sysconfdir/sysconfig/network-scripts/README

/bin/*
/sbin/ppp-watch
%attr(2711,root,netwatch) /sbin/netreport
%attr(700,root,root) %_sbindir/usernetctl
%dir %attr(730,root,netwatch) /var/run/netreport
%_mandir/man?/*

%doc README ifcfg-iptun0.example ifcfg-plip0.example ifcfg-ipsectun0.example
%doc ifcfg-pentanet0.example config-pentanet0.example

%changelog
* Mon Jan 22 2007 Dmitry V. Levin <ldv@altlinux.org> 0.5.6-alt1
- Removed -Werror from CFLAGS.
- Replaced absolute symlinks with relative.

* Thu Aug 04 2005 Denis Ovsienko <pilot@altlinux.ru> 0.5.5-alt1
- resolv.conf modification code migrates to ppp-common
- added default /etc/sysconfig/network

* Fri Mar 11 2005 Denis Ovsienko <pilot@altlinux.ru> 0.5.4-alt2
- now we _really_ have a separate sysctl.conf

* Thu Mar 10 2005 Denis Ovsienko <pilot@altlinux.ru> 0.5.4-alt1
- 0.5.4:
 + default ifcfg-lo now contains BOOTPROTO=static
 + now we have a separate sysctl.conf (#5857)
 + /etc/init.d/netfs moves to startup package

* Thu Feb 10 2005 Denis Ovsienko <pilot@altlinux.ru> 0.5.3-alt2
- lo static hotfix

* Tue Feb 08 2005 Denis Ovsienko <pilot@altlinux.ru> 0.5.3-alt1
- new version (fixes #5891 and #5559)

* Mon Feb 07 2005 Denis Ovsienko <pilot@altlinux.ru> 0.5.2-alt1
- new version (fixes #5964)

* Mon Jan 03 2005 Denis Ovsienko <pilot@altlinux.ru> 0.5.1-alt1
- merged pentanet-tools scripts
- moved /etc/ppp/* from net-scripts into ppp-common

* Sun Nov 14 2004 Denis Ovsienko <pilot@altlinux.ru> 0.5.0-alt1
- merged ipsecadm scripts into net-scripts

* Thu Nov 11 2004 Denis Ovsienko <pilot@altlinux.ru> 0.4.9.1-alt2
- new network-config-subsystem provides

* Mon Jul 05 2004 Denis Ovsienko <pilot@altlinux.ru> 0.4.9.1-alt1
- fix for #4332 (conflict with hotplug)
- updated README

* Thu Jun 24 2004 Denis Ovsienko <pilot@altlinux.ru> 0.4.9-alt1
- fix stuck "# ppp temp entry" lines (#2589, #4249)
- updated README

* Sun Jun 20 2004 Denis Ovsienko <pilot@altlinux.ru> 0.4.8.1-alt1
- *.rpm* and *~ are ignored now for aliases
- more info in changelog

* Sat May 22 2004 Denis Ovsienko <pilot@altlinux.ru> 0.4.8-alt1
- new features (FORWARDING, LOG_MARTIANS and RP_FILTER per interface,
  ifup-pre-local, ifup-post-local, ifdown-pre-local and ifdown-post-local)
- fixed some minor bugs
- corrected typos
- ethernet link test is now off by default

* Sat May 15 2004 Denis Ovsienko <pilot@altlinux.ru> 0.4.7-alt1
- fixed #3522 (DHCP_HOSTNAME)
- updated #3695 (bonding patch)
- fixed #635 (ppp-watch bug)

* Sun May 09 2004 Denis Ovsienko <pilot@altlinux.ru> 0.4.6-alt1
- ifplugstatus constraint
- removed extra mount
- added ONBOOT handling for aliases and alias ranges (#3717)

* Sat Apr 24 2004 Denis Ovsienko <pilot@altlinux.ru> 0.4.5-alt1
- fixed ifstatus/ifplugstatus

* Sun Mar 28 2004 Denis Ovsienko <pilot@altlinux.ru> 0.4.4-alt1
- new version (minor improvements)
- merged #3893 (dead link detection patch), #3696 (bonding patch)
- zcip is not required

* Tue Mar 23 2004 Denis Ovsienko <pilot@altlinux.ru> 0.4.3-alt1
- moved iptun example config to docdir
- spec cleanup

* Sun Mar 21 2004 Denis Ovsienko <pilot@altlinux.ru> 0.4.2-alt1
- merged #3695 and fixed the patch itself
- fixed #3430
- added MULTICAST interface parameter

* Sun Mar 14 2004 Denis Ovsienko <pilot@altlinux.ru> 0.4-alt2
- removed *~

* Sat Mar 13 2004 Denis Ovsienko <pilot@altlinux.ru> 0.4-alt1
- fixed bugs:
 + #3700 (typo)
 + #3724/2784 (PLIP handling)
 + #1637 (IP tunnel support)
- Russian tags

* Thu May 29 2003 Dmitry V. Levin <ldv@altlinux.org> 0.3-alt1
- Added README, based on
  /usr/share/doc/initscripts-5.49.1/sysconfig.txt,
  with minor corrections (closes #0002561, #0002617).
- ipcalc: updated code and manpage from RH.

* Fri May 23 2003 Dmitry V. Levin <ldv@altlinux.org> 0.2-alt1
- Fixed typo introduced in previous release.

* Tue May 20 2003 Dmitry V. Levin <ldv@altlinux.org> 0.1-alt1
- Provides: %_sysconfdir/ppp/ip-up.d, %_sysconfdir/ppp/ip-down.d
- Use new functions from service package.

* Mon Apr 21 2003 Dmitry V. Levin <ldv@altlinux.org> 0.0.1-alt1
- Removed all but network scripts and packaged them separately.

* Sat Apr 19 2003 Dmitry V. Levin <ldv@altlinux.org> 5.49-ipl54mdk
- %_initdir/sound: don't sort aliases in LoadModule (#0001802).
- %_initdir/clock: test $HWCLOCK_ADJUST also for "true" value (#0002351).
- %_initdir/functions:
  + fixed check logic in daemon() a bit (#0002407).
  + fixed return code in killproc() (#0002412).
- %_initdir/outformat: check argumnets being passed to tput (#0002450).
- /etc/sysctl.conf:
  + set "net.ipv4.icmp_echo_ignore_broadcasts = 1" by default (#0002472);
  + added comments from Owl's sysctl.conf file.
- usernetctl: support variable definitions quoted with single quotes.
