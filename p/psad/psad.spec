%define psadlibdir %_libdir/%name
%define psadlogdir /var/log/psad
%define psadrundir /var/run/psad
%define psadvarlibdir /var/lib/psad

Name: psad
Version: 2.1.7
Release: alt1

Summary: psad analyzes iptables log messages for suspect traffic
License: GPL
Group: System/Servers

URL: http://www.cipherdyne.org/psad/
Source0: http://www.cipherdyne.org/psad/download/psad-%version.tar.bz2
Source1: psad.init

Requires: iptables

%description
Port Scan Attack Detector (psad) is a collection of three lightweight
system daemons written in Perl and in C that are designed to work with Linux
iptables firewalling code to detect port scans and other suspect traffic.  It
features a set of highly configurable danger thresholds (with sensible
defaults provided), verbose alert messages that include the source,
destination, scanned port range, begin and end times, tcp flags and
corresponding nmap options, reverse DNS info, email and syslog alerting,
automatic blocking of offending ip addresses via dynamic configuration of
iptables rulesets, and passive operating system fingerprinting.  In addition,
psad incorporates many of the tcp, udp, and icmp signatures included in the
snort intrusion detection system (http://www.snort.org) to detect highly
suspect scans for various backdoor programs (e.g. EvilFTP, GirlFriend,
SubSeven), DDoS tools (mstream, shaft), and advanced port scans (syn, fin,
xmas) which are easily leveraged against a machine via nmap.  psad can also
alert on snort signatures that are logged via fwsnort
(http://www.cipherdyne.org/fwsnort/), which makes use of the
iptables string match module to detect application layer signatures.

%prep
%setup -q

%build
### build psad binaries (kmsgsd and psadwatchd)
make OPTS="$RPM_OPT_FLAGS"

%install
### log directory
mkdir -p %buildroot%psadlogdir
### dir for psadfifo
mkdir -p %buildroot%psadvarlibdir
### dir for pidfiles
mkdir -p %buildroot%psadrundir

### whois_psad binary
mkdir -p %buildroot%_bindir
mkdir -p %buildroot%_mandir/man8
mkdir -p %buildroot%_mandir/man1
mkdir -p %buildroot%_sbindir
### psad config
mkdir -p %buildroot%_sysconfdir/%name
### psad init script
mkdir -p %buildroot/etc/rc.d/init.d

### the 700 permissions mode is fixed in the
### %post phase
install -m 700 psad %buildroot%_sbindir/
install -m 700 kmsgsd %buildroot%_sbindir/
install -m 700 psadwatchd %buildroot%_sbindir/
install -m 500 fwcheck_psad.pl %buildroot%_sbindir/fwcheck_psad
ln -snf whois %buildroot/usr/bin/whois_psad
install -m 755 nf2csv %buildroot/usr/bin/nf2csv
install -m 755 %SOURCE1 %buildroot/etc/rc.d/init.d/psad
install -m 644 psad.conf %buildroot%_sysconfdir/%name/
install -m 644 signatures %buildroot%_sysconfdir/%name/
install -m 644 icmp_types %buildroot%_sysconfdir/%name/
install -m 644 ip_options %buildroot%_sysconfdir/%name/
install -m 644 auto_dl %buildroot%_sysconfdir/%name/
install -m 644 snort_rule_dl %buildroot%_sysconfdir/%name/
install -m 644 pf.os %buildroot%_sysconfdir/%name/
install -m 644 posf %buildroot%_sysconfdir/%name/
install -m 644 *.8 %buildroot%_mandir/man8/
install -m 644 nf2csv.1 %buildroot%_mandir/man1/

### install snort rules files
cp -r deps/snort_rules %buildroot%_sysconfdir/%name

%pre
#if [ ! -p /var/lib/psad/psadfifo ];
#then [ -e /var/lib/psad/psadfifo ] && /bin/rm -f /var/lib/psad/psadfifo
#fi
#/bin/mknod -m 600 /var/lib/psad/psadfifo p
#chown root.root /var/lib/psad/psadfifo
#chmod 0600 /var/lib/psad/psadfifo

%post
### put the current hostname into the psad C binaries
### (kmsgsd and psadwatchd).
perl -p -i -e 'use Sys::Hostname; my $hostname = hostname(); s/HOSTNAME(\s+)_?CHANGE.?ME_?/HOSTNAME${1}$hostname/' %_sysconfdir/%name/psad.conf
perl -p -i -e 'use Sys::Hostname; my $hostname = hostname(); s/HOSTNAME(\s+)_?CHANGE.?ME_?/HOSTNAME${1}$hostname/' %_sysconfdir/%name/psadwatchd.conf

/bin/touch %psadlogdir/fwdata
chown root.root %psadlogdir/fwdata
chmod 0500 %_sbindir/psad
chmod 0500 %_sbindir/kmsgsd
chmod 0500 %_sbindir/psadwatchd
chmod 0600 %psadlogdir/fwdata
if [ ! -p %psadvarlibdir/psadfifo ];
then [ -e %psadvarlibdir/psadfifo ] && /bin/rm -f %psadvarlibdir/psadfifo
/bin/mknod -m 600 %psadvarlibdir/psadfifo p
fi
chown root.root %psadvarlibdir/psadfifo
chmod 0600 %psadvarlibdir/psadfifo
### make psad start at boot
/sbin/chkconfig --add psad
if [ -f /etc/syslog.conf ];
then [ -f /etc/syslog.conf.orig ] || cp -p /etc/syslog.conf /etc/syslog.conf.orig
    ### add the psadfifo line to /etc/syslog.conf if necessary
    if ! grep -v "#" /etc/syslog.conf | grep -q psadfifo;
    then echo "[+] Adding psadfifo line to /etc/syslog.conf"
    echo "kern.info |/var/lib/psad/psadfifo" >> /etc/syslog.conf
    fi
    if [ -e /var/run/syslogd.pid ];
    then
    echo "[+] Restarting syslogd "
    kill -HUP `cat /var/run/syslogd.pid`
    fi
fi
if grep -q "EMAIL.*root.*localhost" /etc/psad/psad.conf;
then
echo "[+] You can edit the EMAIL_ADDRESSES variable in /etc/psad/psad.conf"
echo "    /etc/psad/psadwatchd.conf to have email alerts sent to an address"
echo "    other than root\@localhost"
fi

if grep -q "HOME_NET.*CHANGEME" /etc/psad/psad.conf;
then
echo "[+] Be sure to edit the HOME_NET variable in /etc/psad/psad.conf"
echo "    to define the internal network(s) attached to your machine."
fi

%preun
#%%_preun_service psad

%files
%dir %psadlogdir
%dir %psadvarlibdir
%dir %psadrundir
/etc/rc.d/init.d/psad
%_sbindir/*
%_bindir/*
%_mandir/man8/*
%_mandir/man1/*

%dir %_sysconfdir/%name
%config(noreplace) %_sysconfdir/%name/*.conf
%config(noreplace) %_sysconfdir/%name/signatures
%config(noreplace) %_sysconfdir/%name/auto_dl
%config(noreplace) %_sysconfdir/%name/ip_options
%config(noreplace) %_sysconfdir/%name/snort_rule_dl
%config(noreplace) %_sysconfdir/%name/posf
%config(noreplace) %_sysconfdir/%name/pf.os
%config(noreplace) %_sysconfdir/%name/icmp_types

%dir %_sysconfdir/%name/snort_rules
%config(noreplace) %_sysconfdir/%name/snort_rules/*

%changelog
* Thu Oct 20 2011 Alexey Tourbin <at@altlinux.ru> 2.1.7-alt1
- 2.0.5 -> 2.1.7
- bundled perl modules not packaged

* Sun Nov 07 2010 Vladimir Lettiev <crux@altlinux.ru> 2.0.5-alt1.1
- rebuilt with perl 5.12

* Fri Mar 23 2007 Denis Kuznetsov <dek@altlinux.ru> 2.0.5-alt1
- Build for ALTLinux. 

* Thu Mar 01 2007 Michael Rash <mbr@cipherdyne.org>
- psad-2.0.5 release
- Removed all config files except for psad.conf since the psad daemons now all
  reference the same config file (psad.conf).

* Sat Jan 27 2007 Michael Rash <mbr@cipherdyne.org>
- psad-2.0.4 release

* Sun Dec 31 2006 Michael Rash <mbr@cipherdyne.org>
- psad-2.0.3 release
- Removed Psad.pm perl module and kmsgsd.pl and psadwatchd.pl scripts.  This
  is a major change that allows psad to be more flexible and completely derive
  its config from the psad.conf file and from the command line.  In the
  previous scheme, psad imported its config with a function within Psad.pm,
  and this required that psad imported the Psad perl module before reading its
  config.  A consequence is that the PSAD_LIBS_DIR var could not be specified
  usefully within the config file.

* Sat Dec 23 2006 Michael Rash <mbr@cipherdyne.org>
- psad-2.0.2 release

* Mon Dec 12 2006 Michael Rash <mbr@cipherdyne.org>
- psad-2.0.1 release

* Sun Dec 10 2006 Michael Rash <mbr@cipherdyne.org>
- psad-2.0 release.
- Added ip_options file for the Snort ipopts rule keyword.
- Added nf2csv so that normal users can get CSV output from
  Netfilter log messages.

* Sun Oct 15 2006 Michael Rash <mbr@cipherdyne.org>
- psad-1.4.8 release.

* Sun Sep 10 2006 Michael Rash <mbr@cipherdyne.org>
- psad-1.4.7 release.

* Sat Sep 02 2006 Michael Rash <mbr@cipherdyne.org>
- Added updates from Mate Wierdl to get psad RPM building on x86_64
  platforms.

* Tue Jun 13 2006 Michael Rash <mbr@cipherdyne.org>
- Added installation of snort_rule_dl file.
- psad-1.4.6 release.

* Fri Jan 13 2006 Michael Rash <mbr@cipherdyne.org>
- psad-1.4.5 release.

* Sun Nov 27 2005 Michael Rash <mbr@cipherdyne.org>
- psad-1.4.4 release.

* Tue Nov 22 2005 Michael Rash <mbr@cipherdyne.org>
- Removed smtpdaemon dependency since psad can be run without sending
  email alerts by configuring /etc/psad/alert.conf appropriately.

* Tue Jul 12 2005 Michael Rash <mbr@cipherdyne.org>
- Updated to only update syslog.conf if it actually exists. psad
  is now comptable with other syslog daemons, and also with ulogd.

* Thu Mar 10 2005 Michael Rash <mbr@cipherdyne.org>
- Updated to new IPTables-Parse and IPTables-ChainMgr modules.
- psad-1.4.1 release.

* Fri Nov 26 2004 Michael Rash <mbr@cipherdyne.org>
- Added ps.os file.
- psad-1.4.0 release.

* Sun Oct 17 2004 Michael Rash <mbr@cipherdyne.org>
- psad-1.3.4 release.

* Sat Sep 25 2004 Michael Rash <mbr@cipherdyne.org>
- Added Bit::Vector back since not having it causes dependency
  problems with Date::Calc even though psad does not require any
  Date::Calc functions that require Bit::Vector functions.

* Mon Sep 06 2004 Michael Rash <mbr@cipherdyne.org>
- Updated to psad-1.3.3.
- Fixed path to psad-init.redhat (Mate Wierdl)

* Thu Jun 24 2004 Michael Rash <mbr@cipherdyne.org>
- Updated to psad-1.3.2 (added fwcheck_psad.pl and fw_search.conf
  installation).

* Mon Oct 14 2003 Michael Rash <mbr@cipherdyne.org>
- Removed ipchains text from description.
- Added test and config warning message for HOME_NET variable.
- Updated to version 1.3

* Mon Oct 14 2003 Michael Rash <mbr@cipherdyne.org>
- Removed diskmond since psad handles disk space thresholds
  directly.

* Sat Oct 11 2003 Michael Rash <mbr@cipherdyne.org>
- Updated spec file to build properly on both Red Hat 7.2 and
  Red Hat 9 systems.

* Tue Sep 23 2003 Lenny Cartier <lenny@mandrakesoft.com> 1.2.3-1mdk
- mandrakized specfile

* Fri Sep 12 2003 Michael Rash <mbr@cipherdyne.org>
- Added interface tracking for scans.
- Bugfix for not opening /etc/hosts.deny the right way in
  tcpwr_block().
- Bugfix for psadfifo path in syslog-ng config.
- Better format for summary stats section in email alerts.
- Bugfix for INIT_DIR path on non-RedHat systems.
- Bugfix for gzip path.
- Make Psad.pm installed last of all perl modules installed
  by psad.
- Added additional call to incr_syscall_ctr() in psadwatchd.c

* Mon Jul 28 2003 Michael Rash <mbr@cipherdyne.org>
- Initial version.
