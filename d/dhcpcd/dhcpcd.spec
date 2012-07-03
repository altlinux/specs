Name: dhcpcd
Epoch: 1
Version: 5.5.6
Release: alt1

Summary: DHCP Client
License: %bsdstyle
Group: System/Servers

URL: http://roy.marples.name/projects/%name
Source: %name-%version.tar
Source2: 70-vendor-encap
Patch0: %name-%version-%release.patch
AutoReq: yes, noshell

BuildRequires: rpm-build-licenses

Conflicts: etcnet < 0.9.10-alt6

%description
dhcpcd is an implementation of the DHCP client specified in RFC2131.

It gets the host information (IP address, netmask, broadcast address, etc.)
from a DHCP server and configures the network interface of the machine on
which it is running. It also tries to renew the lease time according to RFC2131.

%prep
%setup -q
%patch0 -p1

%build
%configure \
        --sbindir=/sbin \
        --rundir=/var/run \
        --libexecdir=/lib/%name \
        --dbdir=%_localstatedir/%name \
        --serviceexists='[ -x %_initdir/"$1" ]' \
        --servicecmd='/sbin/service "$1" >/dev/null 2>&1' \
        --with-hook=ntp.conf
%make_build

%install
%makeinstall_std BINMODE=0755
install -m 0644 %SOURCE2 %buildroot/lib/%name/%name-hooks/

%triggerpostun -- %name < 1:5.0.0
if grep -qs '^[[:blank:]]*clientid' %_sysconfdir/%name.conf; then
	echo "WARNING: *clientid* option is detected in %_sysconfdir/%name.conf."
	echo "The behavior of this option was changed since dhcpcd-5."
	echo "Now it means TO SEND clientid to the server."
fi

%files
/sbin/*
%_man8dir/*
%_man5dir/*
%config(noreplace) %_sysconfdir/%name.conf
%dir %_localstatedir/%name
%dir /lib/%name
%dir /lib/%name/%name-hooks
/lib/%name/%name-hooks/*
/lib/%name/%name-run-hooks

%changelog
* Thu Mar 29 2012 Mikhail Efremov <sem@altlinux.org> 1:5.5.6-alt1
- Updated to 5.5.6.

* Thu Feb 16 2012 Mikhail Efremov <sem@altlinux.org> 1:5.5.4-alt2
- Fix dhcpcd permissions (closes: #26939).

* Wed Feb 08 2012 Mikhail Efremov <sem@altlinux.org> 1:5.5.4-alt1
- Updated to 5.5.4.

* Thu Feb 02 2012 Mikhail Efremov <sem@altlinux.org> 1:5.5.1-alt1
- Updated to 5.5.1.

* Wed Oct 26 2011 Mikhail Efremov <sem@altlinux.org> 1:5.2.12-alt1
- config: Disable vendor-encap hook.
- Updated to 5.2.12.

* Wed Apr 27 2011 Mikhail Efremov <sem@altlinux.org> 1:4.0.15-alt5
- Allow both domain-name and domain-search options.
- Allow RFC violating search in domain.
- Fix support multiple domains in search (closes: #25521).

* Thu Apr 07 2011 Mikhail Efremov <sem@altlinux.org> 1:4.0.15-alt4
- Escape | and & characters when passing to the shell
    (fixes CVE-2011-996, backport from dhcpcd-5).

* Tue Aug 03 2010 Mikhail Efremov <sem@altlinux.org> 1:4.0.15-alt3
- drop Packager from spec.
- Don't use fixed buffer for netlink messages (backport from dhcpcd-5)
- fix hostname check.

* Mon Dec 28 2009 Mikhail Efremov <sem@altlinux.org> 1:4.0.15-alt2
- Not request the options that are given with --nooption
    (closes #22574).

* Tue Sep 29 2009 Mikhail Efremov <sem@altlinux.org> 1:4.0.15-alt1
- 4.0.15

* Sat Aug 15 2009 Mikhail Efremov <sem@altlinux.org> 1:4.0.14-alt2
- minor changes in vendor-encap hook script.
- update-chrooted hook script is removed.
- use update_chrooted in resolv.conf hook script if needed.
- don't install dhcpcd-compat hook script.

* Fri Aug 14 2009 Mikhail Efremov <sem@altlinux.org> 1:4.0.14-alt1
- 4.0.14

* Wed Apr 22 2009 Mikhail Efremov <sem@altlinux.org> 1:4.0.13-alt2
- added 70-vendor-encap hook script.
- fixed interface name truncation in log messages.

* Mon Apr 20 2009 Mikhail Efremov <sem@altlinux.org> 1:4.0.13-alt1
- 4.0.13
- minor changes in 50-ntp.conf.

* Mon Apr 06 2009 Mikhail Efremov <sem@altlinux.org> 1:4.0.12-alt5
- fixed ntpd restart

* Fri Apr 03 2009 Mikhail Efremov <sem@altlinux.org> 1:4.0.12-alt4
- write info files in /var/lib/dhcpcd.

* Tue Mar 17 2009 Mikhail Efremov <sem@altlinux.org> 1:4.0.12-alt3
- Don't run update_chrooted if resolvconf is installed.

* Mon Mar 02 2009 Mikhail Efremov <sem@altlinux.org> 1:4.0.12-alt2
- fixed License

* Fri Feb 27 2009 Mikhail Efremov <sem@altlinux.org> 1:4.0.12-alt1
- 4.0.12
- fixed URL.

* Fri Feb 20 2009 Mikhail Efremov <sem@altlinux.org> 1:4.0.11-alt1
- 4.0.11
- pack source as tar instead tar.gz

* Sun Feb 15 2009 Mikhail Efremov <sem@altlinux.org> 1:4.0.10-alt3
- add 'noarp' option in dhcpcd.conf (close ALT bug #18703)

* Thu Feb 12 2009 Mikhail Efremov <sem@altlinux.org> 1:4.0.10-alt2
- install lookup-hostname hook script, but disable it by default

* Wed Feb 04 2009 Mikhail Efremov <sem@altlinux.org> 1:4.0.10-alt1
- version 4.0.10

* Mon Feb 02 2009 Mikhail Efremov <sem@altlinux.org> 1:4.0.7-alt3
- use "servers" keyword instead "server" in ntpd.conf

* Wed Jan 28 2009 Mikhail Efremov <sem@altlinux.org> 1:4.0.7-alt2
- handle POLLERR (fix segfault when device is removed).

* Mon Jan 26 2009 Mikhail Efremov <sem@altlinux.org> 1:4.0.7-alt1
- fixes from led@ spec:
    fixed URL
    fixed License
    fixed paths

* Wed Jan 21 2009 Mikhail Efremov <sem@altlinux.org> 4.0.7-alt0.4
- applied led@ patches:   
    dhcpcd-4.0.1-alt-hooks.patch
    dhcpcd-4.0.1-alt-linux.patch.
- build both ntpd.conf and ntp.conf if them is exists.

* Tue Dec 09 2008 Mikhail Efremov <sem@altlinux.org> 4.0.7-alt0.3
- add noipv4ll option to config file.
- install ntp.conf hook script.
- ntp.conf hook script fixed for work with openntp.

* Mon Dec 08 2008 Mikhail Efremov <sem@altlinux.org> 4.0.7-alt0.2
- install dhcpcd-compat hook script

* Thu Dec 04 2008 Mikhail Efremov <sem@altlinux.org> 4.0.7-alt0.1
- version 4.0.7

* Mon Aug 18 2008 Mikhail Efremov <sem@altlinux.org> 4.0.0-alt0.1.rc5
- 4.0.0-rc5
- dhcpcd-4.0.0-alt-hostname_hook.patch removed  (obsolete)

* Mon Jul 28 2008 Mikhail Efremov <sem@altlinux.org> 4.0.0-alt0.1.rc4
- 4.0.0-rc4
- dhcpcd-4.0.0-alt-makefile.patch and dhcpcd-4.0.0-alt-noipv4ll_option_fix.patch
  removed (obsolete)

* Mon Jul 28 2008 Mikhail Efremov <sem@altlinux.org> 4.0.0-alt0.1.rc3
- version 4.0.0-rc3

* Fri Mar 28 2008 Michael Shigorin <mike@altlinux.org> 1:3.0.17-alt4
- rollback to 3.0.17 for there are too many regressions (seemingly
  specific to us as no upstream problems are spotted) and I'm unable
  to reliably reproduce the problem; see also #15042 and #15131
- if anyone needs 3.2.x features please look into Daedalus and 
  preferably help with finding out the trouble source (or patch)

* Thu Mar 06 2008 Michael Shigorin <mike@altlinux.org> 3.0.17-alt2.M40.1
- built for M40 (reportedly good enough and tested, see #14643)
- spec cleanup

* Tue Feb 26 2008 Michael Shigorin <mike@altlinux.org> 3.2.3-alt0.2
- added a configure.c patch by shrek@ (mentioned in #14643)
- seems tested & working

* Mon Feb 25 2008 Michael Shigorin <mike@altlinux.org> 3.2.3-alt0.1
- NMU: 3.2.3 (#14643)
- spec macro abuse cleanup
- updated patch1, patch2, patch3
- removed patch4 (obsolete)
- fixed %%config(noreplace) typo in %%files

* Mon May 21 2007 Stanislav Ievlev <inger@altlinux.org> 3.0.17-alt3
- fix -H option (backport from 3.1.0 with fixes)

* Mon May 14 2007 Stanislav Ievlev <inger@altlinux.org> 3.0.17-alt2
- ignore -D option (for backward compatibility with previous installations)

* Tue May 08 2007 Stanislav Ievlev <inger@altlinux.org> 3.0.17-alt1
- 3.0.17

* Mon Apr 16 2007 ALT QA Team Robot <qa-robot@altlinux.org> 1.3.22pl4-alt3.0
- Automated rebuild.

* Thu Apr 21 2005 Denis Ovsienko <pilot@altlinux.ru> 1.3.22pl4-alt3
- improved alt-config patch to fix #6133

* Thu Jul 01 2004 Dmitry V. Levin <ldv@altlinux.org> 1.3.22pl4-alt2
- %_sysconfdir/dhcpc/%name.exe:
  + added wlan* interface support (#4348);
  + minor fixes (#4158).

* Mon Oct 20 2003 Dmitry V. Levin <ldv@altlinux.org> 1.3.22pl4-alt1
- Updated to 1.3.22pl4, rediffed patches.
- Install %_sysconfdir/dhcpc/%name.exe by default;
  Patch %_sysconfdir/dhcpc/%name.exe to run update_chrooted.
  (should address #2406).

* Fri Nov 15 2002 Dmitry V. Levin <ldv@altlinux.org> 1.3.22pl3-alt1
- 1.3.22pl3.

* Thu Jul 11 2002 Dmitry V. Levin <ldv@altlinux.org> 1.3.22pl1-alt1
- 1.3.22pl1.
- Fixed ntp driftfile location.
- Avoid false config files renaming.
- Added PidDir option support, /var/run by default (mdk).

* Mon Nov 05 2001 Konstantin Volckov <goldhead@altlinux.ru> 1.3.21pl1-alt1
- 1.3.21pl1.
- Removed patch0 - now it's outdated

* Sun Feb 25 2001 Dmitry V. Levin <ldv@fandra.org> 1.3.19pl7-ipl1mdk
- 1.3.19pl7.

* Wed Jan 17 2001 Dmitry V. Levin <ldv@fandra.org> 1.3.19pl6-ipl1mdk
- RE adaptions.
- Feature: execute scripts on interface up/down.

* Thu Dec 21 2000 Geoffrey Lee <snailtalk@mandrakesoft.com> 1.3.19pl4-1mdk
- new and shiny source.

* Thu Oct 19 2000 Chmouel Boudjnah <chmouel@mandrakesoft.com> 1.3.19pl1-2mdk
- Add patch for gcc2.96(rh).

* Tue Aug 08 2000 Geoffrey Lee <snailtalk@mandrakesoft.com> 1.3.19pl1-1mdk
- rebuild to use _sysconfdir
- s|1.3.18pl5|1.3.19pl1|

* Fri Jul 28 2000 Vincent Saugey <vince@mandrakesoft.com> 1.3.18pl5-3mdk
- BM, macros

* Tue Apr 18 2000 Vincent Saugey <vince@mandrakesoft.com> 1.3.18pl5-2mdk
- Add patch for dynamic build
- remove bzip and strip file

* Fri Mar 31 2000 Vincent Saugey <vince@mandrakesoft.com> 1.3.18pl5-1mdk
- Correct group
- Update to 1.3.18-pl5

* Sun Nov  7 1999 Chmouel Boudjnah <chmouel@mandrakesoft.com>
- 1.3.18-pl3
- add /etc/dhcpc

* Sun Jul 18 1999 Bernhard Rosenkraenzer <bero@mandrakesoft.com>
- 1.3.17pl9

* Tue May 11 1999 Bernhard Rosenkraenzer <bero@mandrakesoft.com>
- Mandrake adaptions

* Mon Apr 19 1999 Bill Nottingham <notting@redhat.com>
- build for 6.0

* Wed Dec 23 1998 Jeff Johnson <jbj@redhat.com>
- mark default route up.

* Sun Jun  7 1998 Jeff Johnson <jbj@redhat.com>
- Fix packet alignment problems on sparc.
- build root.

* Mon Jun 01 1998 Prospector System <bugs@redhat.com>
- translations modified for de

* Wed May  6 1998 Alan Cox
- fixed some potential buffer exploits reported by Chris Evans

* Mon Apr 27 1998 Prospector System <bugs@redhat.com>
- translations modified for de, fr, tr

* Sun Oct 19 1997 Erik Troan <ewt@redhat.com>
- spec file cleanups

* Tue Jul 08 1997 Erik Troan <ewt@redhat.com>
- built against glibc, updated to 0.65

* Mon Apr 21 1997 Otto Hammersmith <otto@redhat.com>
- fixed summary line... was a summary for tar.
