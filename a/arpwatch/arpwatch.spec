Name: arpwatch
Version: 2.1a15
Release: alt7
Epoch: 2

%define arpwatch_user _arpwd
%define arpwatch_group _arpwd

Summary: Network monitoring tools for tracking IP addresses on the network
Summary(ru_RU.KOI8-R): Утилиты для отслеживания соответствия IP адресов в сети
Group: Monitoring
License: BSD
Url: ftp://ftp.ee.lbl.gov
Packager: Dmitry V. Levin <ldv@altlinux.org>

# %url/%name-%version.tar.gz
Source: arpwatch-%version.tar
Source1: arpwatch.init
Source2: arpwatch.sysconfig

Patch: arpwatch-%version-%release.patch

Requires: MTA
PreReq: shadow-utils

# Automatically added by buildreq on Tue Oct 31 2006
BuildRequires: libpcap-devel

%define _vararpwatch %_localstatedir/%name

%description
The %name package contains %name and arpsnmp.  Arpwatch and arpsnmp
are both network monitoring tools.  Both utilities monitor Ethernet or
FDDI network traffic and build databases of Ethernet/IP address pairs,
and can report certain changes via email.

Install the %name package if you need networking monitoring devices
which will automatically keep traffic of the IP addresses on your
network.

%prep
%setup -q
%patch -p1

%build
export ac_cv_path_V_SENDMAIL=%_sbindir/sendmail
autoreconf -fisv
%configure

%make_build ARPDIR=%_vararpwatch

%install
mkdir -p %buildroot{%_vararpwatch,%_sbindir,%_man8dir,%_initdir}
mkdir -p %buildroot/etc/sysconfig
%make_install DESTDIR=%buildroot install install-man

install -pm755 arp2ethers massagevendor %buildroot%_vararpwatch/
install -pm644 *.awk *.dat %buildroot%_vararpwatch/

install -pm755 %_sourcedir/arpwatch.init %buildroot%_initdir/%name
install -pm644 %_sourcedir/arpwatch.sysconfig %buildroot/etc/sysconfig/%name

%pre
%_sbindir/groupadd -r -f %arpwatch_group
%_sbindir/useradd -r -g %arpwatch_group -c 'The arpwatch daemon' \
	-d %_vararpwatch -s /dev/null %arpwatch_user >/dev/null 2>&1 ||:

%post
%post_service %name

%preun
%preun_service %name

%files
%_sbindir/*
%_mandir/man?/*
%config(noreplace) %_initdir/%name
%config(noreplace) /etc/sysconfig/%name
%attr(1775,root,%arpwatch_group) %dir %_vararpwatch
%attr(644,%arpwatch_user,%arpwatch_group) %config(noreplace) %_vararpwatch/arp.dat
%_vararpwatch/ethercodes.dat
%_vararpwatch/*.awk
%_vararpwatch/arp2ethers
%_vararpwatch/massagevendor
%doc README CHANGES

%changelog
* Thu Mar 04 2010 Dmitry V. Levin <ldv@altlinux.org> 2:2.1a15-alt7
- Sorted ethercodes.dat using C collation.
- Cleaned up specfile a bit.

* Wed Mar 03 2010 Anton Protopopov <aspsk@altlinux.org> 2:2.1a15-alt6
- Update arpwatch/ethercodes.dat (ALT 23063)

* Mon Jun 01 2009 Anton Protopopov <aspsk@altlinux.org> 2:2.1a15-alt5
- Add possibility to listen to "any" interface

* Mon Mar 12 2007 Dmitry V. Levin <ldv@altlinux.org> 2:2.1a15-alt4
- Gearified.
- Cleaned up droppriv patch.
- Fixed /var/lib/arpwatch permissions.
- Fixed %pre script and package dependencies.
- Fixed build, fixed compilation warnings.
- Updated ethercodes.dat from http://standards.ieee.org/regauth/oui/oui.txt
- Fixed daemonize.
- Fixed syslogging.
- Changed pseudouser name to _arpwd.
- Changed arpwatch daemon to switch user by default.
- arpwatch.init: Disabled daemon by default.

* Wed Nov 15 2006 Serhii Hlodin <hlodin@altlinux.ru> 2:2.1a15-alt3
- Fixes bug #10265 (permissions on %_vararpwatch)

* Tue Oct 31 2006 Serhii Hlodin <hlodin@altlinux.ru> 2:2.1a15-alt1
- New version 2.1a15
- Add and porting patches from RedHat:
- add droproot patch, some --usage and man page fixes
- separate droproot patch from a more generic man/usage fix one
- added arpwatch options to specify sender and recipient
- added man page descriptions for the new parameters
- added arpsnmp options to specify sender and recipient
  and corrected arpwatch and arpsnmp man pages

* Mon Jan 16 2006 Michael Shigorin <mike@altlinux.org> 2:2.1a13-alt1.1
- NMU: add sysconfig support
- spec cleanup

* Mon Mar 01 2004 Stanislav Ievlev <inger@altlinux.org> 2:2.1a13-alt1
- 2.1a13

* Thu Nov 13 2003 Stanislav Ievlev <inger@altlinux.org> 2:2.1a11-alt6
- new init script

* Wed Nov 27 2002 Stanislav Ievlev <inger@altlinux.ru> 2:2.1a11-alt5
- fix deps on csh

* Mon Nov 18 2002 Stanislav Ievlev <inger@altlinux.ru> 2:2.1a11-alt4
- rebuild
- use {post/preun}_server macros

* Wed May 15 2002 Dmitry V. Levin <ldv@altlinux.org> 2:2.1a11-alt3
- Updated dependencies (smtpdaemon --> MTA).

* Tue Apr 09 2002 Dmitry V. Levin <ldv@alt-linux.org> 2:2.1a11-alt2
- Rebuilt with libpcap-0.7.1.
- Updated dependencies.

* Fri Jan 04 2002 Rider <rider@altlinux.ru> 2.1a11-alt1
- 2.1a11

* Tue Jan 09 2001 Dmitry V. Levin <ldv@fandra.org> 2.1a10-ipl2mdk
- Rebuilt with libpcap-0.6.1.

* Tue Oct 17 2000 Dmitry V. Levin <ldv@fandra.org> 2.1a10-ipl1mdk
- 2.1a10
- Split from tcpdump.
