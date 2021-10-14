Name: amavis
Version: 2.12.2
Release: alt1
Epoch: 1

Summary: Amavis is a high-performance email content filter framework written in Perl
License: BSD-2-Clause and GPL-2.0
Group: Networking/Mail
Url: https://gitlab.com/amavis/amavis
Packager: Andrey Cherepanov <cas@altlinux.org>

Source: %name-%version.tar
Source1: amavisd.init
Source2: amavisd-new-notify.tar.gz
Source3: conf.d.tar.gz
Source6: amavisd-new-README.postfix.ALT.KOI8-R
Source7: amavisd-new-README.postfix.ALT.UTF8
Source8: %name.cron
Source10: amavisd-av-control
Source11: amavisd-spam-control
Source12: %name.tmpfiles.conf
Source13: amavisd.service
Source14: amavisd-snmp.service

Patch1: amavisd-skipsomedeps.patch
Patch2: amavis-2.12.0-conf.patch

BuildArch: noarch
Provides: amavisd
Provides: amavisd-new = %EVR
Obsoletes: amavisd-new < %EVR

Requires: file
Requires: perl-Archive-Zip >= 1.14
Requires: perl-BerkeleyDB 
Requires: perl-Convert-UUlib
Requires: perl-Convert-TNEF
Requires: perl-IO-stringy
Requires: perl-IO-Zlib
Requires: perl-MailTools
Requires: perl-Mail-DKIM >= 0.31
Requires: perl-IO-Socket-INET6

BuildRequires: perl-BerkeleyDB
BuildRequires: perl-IO-stringy
BuildRequires: perl-Unix-Syslog
BuildRequires: perl-Compress-Zlib
BuildRequires: perl-MIME-tools
BuildRequires: perl-Net-Server
BuildRequires: perl-Net-LibIDN
BuildRequires: perl-Digest-SHA
BuildRequires: perl-SNMP

%description
amavis is a high-performance and reliable interface between mailer
(MTA) and one or more content checkers: virus scanners, and/or
Mail::SpamAssassin Perl module. It is written in Perl, assuring high
reliability, portability and maintainability. It talks to MTA via (E)SMTP
or LMTP, or by using helper programs. No timing gaps exist in the design
which could cause a mail loss.

%package snmp
Summary: Exports amavis SNMP data
Group: Networking/Mail
Requires: %name

%description snmp
This package contains the program amavisd-snmp-subagent, which can be
used as a SNMP AgentX, exporting amavisd statistical counters database
(snmp.db) as well as a child process status database (nanny.db) to a
SNMP daemon supporting the AgentX protocol (RFC 2741), such as NET-SNMP.

It is similar to combined existing utility programs amavisd-agent and
amavisd-nanny, but instead of writing results as text to stdout, it
exports data to a SNMP server running on a host (same or remote), making
them available to SNMP clients (such a Cacti or mrtg) for monitoring or
alerting purposes.

%package utils
Summary: Utils package for amavisd-new.
Group: Networking/Mail
Requires: %name
Provides: amavisd-new-utils = %EVR
Obsoletes: amavisd-new-utils < %EVR

%description utils
This package contains amavisd-new utils: snmp-agent, nanny, release.

%package smtpd
Summary: Virtual package for amavisd-new with MTA.
Group: Networking/Mail
Requires: %name
Requires: smtpdaemon
Provides: amavisd-new-smtpd = %EVR
Obsoletes: amavisd-new-smtpd < %EVR

%description smtpd
This package contains require MTA daemon. If you use postfix, sendmail or exim
you will need to install %name-smtpd.

%package cron
Summary: Cron package for clean quarantine.
Group: Networking/Mail
Requires: %name
Requires: stmpclean
Requires: crontabs
Provides: amavisd-new-cron = %EVR
Obsoletes: amavisd-new-cron < %EVR

%description cron
This package contains cron script for clean quarantine.

%package spamassassin
Summary: Virtual package for amavisd-new with SpamAssassin.
Group: Networking/Mail
Requires: %name
Requires: perl-Mail-SpamAssassin
Requires: spamassassin >= 2.60
Provides: amavisd-new-spamassassin = %EVR
Obsoletes: amavisd-new-spamassassin < %EVR

%description spamassassin
This package contains require SpamAssassin perl module.
If you use SpamAssassin, you will need to install %name-spamassassin.

%package razor
Summary: Virtual package for amavisd-new with razor.
Group: Networking/Mail
Requires: %name
Requires: perl-Razor
Provides: amavisd-new-razor = %EVR
Obsoletes: amavisd-new-razor < %EVR

%description razor
This package contains require razor. If you use razor,
you will need to install %name-razor.

%package clamav
Summary: Virtual package for amavisd-new with clamav antivirus.
Group: Networking/Mail
Requires: %name
Requires: clamav
Provides: amavisd-new-clamav = %EVR
Obsoletes: amavisd-new-clamav < %EVR

%description clamav
This package contains require razor. If you use razor,
you will need to install %name-clamav.

%package ext-archives
Summary: Virtual package for amavisd-new with external archives.
Group: Networking/Mail
Requires: %name
Requires: bzip2
Requires: lha
Requires: lzop
Requires: ncompress
#Requires:	nomarch
#Requires:	arc
Requires: unace
Requires: unarj
Requires: unrar
#Requires:	zoo
Provides: amavisd-new-ext-archives = %EVR
Obsoletes: amavisd-new-ext-archives < %EVR

%description ext-archives
This package contains require external archives.

%package mysql
Summary: Virtual package is supported lookups in mysql.
Group: Networking/Mail
Requires: %name
Requires: perl-DBD-mysql
Provides: amavisd-new-mysql = %EVR
Obsoletes: amavisd-new-mysql < %EVR

%description mysql
Amavisd-new is supported for storing information
about processed mail (logging/reporting) and optionally for quarantining
to a SQL database.

%package postgresql
Summary: Virtual package SQL is supported lookups in PostgreSQL.
Group: Networking/Mail
Requires: %name
Requires: perl-DBD-Pg
Provides: amavisd-new-postgresql = %EVR
Obsoletes: amavisd-new-postgresql < %EVR

%description postgresql
Amavisd-new is supported for storing information
about processed mail (logging/reporting) and optionally for quarantining
to a SQL database.

%package ldap-client
Summary: Virtual package is supported lookups in LDAP.
Group: Networking/Mail
Requires: %name
Requires: perl-ldap >= 0.32
Provides: amavisd-new-ldap-client = %EVR
Obsoletes: amavisd-new-ldap-client < %EVR

%description ldap-client
Amavisd-new is supported lookups multiple search attributes in LDAP.

%package ldap-server
Summary: Package is supported lookups in LDAP.
Group: Networking/Mail
Requires: openldap-servers
Provides: amavisd-new-ldap-server = %EVR
Obsoletes: amavisd-new-ldap-server < %EVR

%description ldap-server
Amavisd-new is supported lookups multiple search attributes in LDAP.

%package p0f
Summary: Virtual package for amavisd-new with p0f.
Group: Networking/Mail
Requires: %name
Requires: p0f
Provides: amavisd-new-p0f = %EVR
Obsoletes: amavisd-new-p0f < %EVR

%description p0f
This package contains require p0f and perl script p0f-analyzer.pl. If you use
p0f, you will need to install %name-p0f.

%package complete
Summary: Package contein all subpackages amavisd-new.
Group: Networking/Mail
Requires: %name
Requires: %name-utils
Requires: %name-cron
Requires: %name-spamassassin
Requires: %name-razor
Requires: %name-clamav
Requires: %name-ext-archives
Requires: %name-mysql
Requires: %name-postgresql
Requires: %name-ldap-client
Requires: %name-smtpd
Requires: %name-ldap-server
Requires: %name-p0f
Provides: amavisd-new-complete = %EVR
Obsoletes: amavisd-new-complete < %EVR

%description complete
All subpackages Amavisd-new.

%prep
%setup -q
%patch1 -p2
%patch2 -p1

%install
mkdir -p \
	%buildroot%_initdir \
	%buildroot%_sysconfdir/amavisd \
	%buildroot%_tmpfilesdir \
	%buildroot%_sbindir \
	%buildroot%_bindir \
	%buildroot%_spooldir/amavisd \
	%buildroot%_spooldir/amavisd/db \
	%buildroot%_spooldir/amavisd/quarantine \
	%buildroot%_spooldir/amavisd/tmp \
	%buildroot%_var/run/amavisd \
        %buildroot%_sysconfdir/cron.daily \
        %buildroot%_sysconfdir/openldap/schema \
        %buildroot%_controldir

install -m 755 %SOURCE1 %buildroot%_initdir/amavisd
install -m 640 amavisd.conf %buildroot%_sysconfdir/amavisd/amavisd.conf
install -m 640 amavisd.conf-default %buildroot%_sysconfdir/amavisd/amavisd.conf-default
install -m 700 %SOURCE8 %buildroot%_sysconfdir/cron.daily/%name
install -m 755 amavisd %buildroot%_sbindir/amavisd
install -m 755 amavisd-snmp-subagent %buildroot%_sbindir/amavisd-snmp-subagent
install -m 755 amavisd-agent %buildroot%_bindir/amavisd-agent
install -m 755 amavisd-nanny %buildroot%_bindir/amavisd-nanny
install -m 755 amavisd-release %buildroot%_bindir/amavisd-release
install -m 755 p0f-analyzer.pl %buildroot%_bindir/p0f-analyzer.pl

install -m444 LDAP.schema %buildroot%_sysconfdir/openldap/schema/amavisd-new.schema

tar -xzf %SOURCE2 -C %buildroot%_sysconfdir/amavisd/
tar -xzf %SOURCE3 -C %buildroot%_sysconfdir/amavisd/

###
## Install Attention README
###
install -m 0644 %SOURCE6 README.ALT.KOI8-R
install -m 0644 %SOURCE7 README.ALT.UTF

install -m 755 %SOURCE10 %buildroot%_controldir/amavisd-av
install -m 755 %SOURCE11 %buildroot%_controldir/amavisd-spam

install -m 644 %SOURCE12 %buildroot%_tmpfilesdir/amavisd.conf
install -Dpm 644 %SOURCE13 %buildroot%_unitdir/amavisd.service
install -Dpm 644 %SOURCE14 %buildroot%_unitdir/amavisd-smnp.service

%pre
getent group amavis > /dev/null || %_sbindir/groupadd -r amavis
getent passwd amavis > /dev/null || \
  %_sbindir/useradd -r -g amavis -d %_spooldir/amavisd -s /sbin/nologin \
  -c "User for amavis" amavis
exit 0

%post
%post_service amavisd

%preun
%preun_service amavisd

%post snmp
%post_service amavisd-snmp

%preun snmp
%preun_service amavisd-snmp

%files
%doc AAAREADME.first INSTALL LICENSE README_FILES RELEASE_NOTES test-messages
%doc LDAP.schema TODO
%doc README.ALT.UTF README.ALT.KOI8-R
%config %_initdir/amavisd
%config %_unitdir/amavisd.service
%config %_tmpfilesdir/amavisd.conf
%attr(640,root,amavis) %config(noreplace) %_sysconfdir/amavisd/amavisd.conf
%_controldir/amavisd-*
%attr(750,root,amavis) %dir %_sysconfdir/amavisd/conf.d
%attr(640,root,amavis) %config(noreplace) %_sysconfdir/amavisd/conf.d/*
%attr(640,root,amavis) %_sysconfdir/amavisd/amavisd.conf-*
%attr(640,root,amavis) %_sysconfdir/amavisd/notify_*
%_sbindir/amavisd
%attr(775,amavis,amavis) %dir %_spooldir/amavisd
%attr(770,amavis,amavis) %dir %_spooldir/amavisd/db
%attr(750,amavis,amavis) %dir %_spooldir/amavisd/quarantine
%attr(750,amavis,amavis) %dir %_spooldir/amavisd/tmp
%attr(775,amavis,amavis) %dir %_var/run/amavisd

%files snmp
%doc AMAVIS-MIB.txt
%config %_unitdir/amavisd-smnp.service
%_sbindir/amavisd-snmp-subagent

%files utils
%_bindir/amavisd-agent 
%_bindir/amavisd-nanny
%_bindir/amavisd-release

%files cron
%_sysconfdir/cron.daily/%name

%files spamassassin
%files razor
%files clamav
%files ext-archives
%files mysql
%files postgresql
%files ldap-client
%files smtpd
%files ldap-server
%attr(644,root,ldap) %_sysconfdir/openldap/schema/amavisd-new.schema
%files p0f
%_bindir/p0f-analyzer.pl

%files complete

%changelog
* Wed Oct 13 2021 Andrey Cherepanov <cas@altlinux.org> 1:2.12.2-alt1
- New version.

* Sat Nov 14 2020 Andrey Cherepanov <cas@altlinux.org> 1:2.12.1-alt1
- New version.

* Thu Oct 15 2020 Andrey Cherepanov <cas@altlinux.org> 1:2.12.0-alt1
- New version.
- Build from git repository https://gitlab.com/amavis/amavis.
- Rename to amavis.
- Add service files.
- New package amavis-snmp.
- Package default config file.
- Move configuration to /etc/amavisd.

* Wed Sep 02 2020 Andrey Cherepanov <cas@altlinux.org> 1:2.11.1-alt2
- Requires perl-IO-Socket-INET6 (ALT #38859).

* Tue Aug 25 2020 Andrey Cherepanov <cas@altlinux.org> 1:2.11.1-alt1
- New version (ALT #27110).
- Fix /var/run/amavis permissions (ALT #37488).
- Fix License tag according to SPDX.

* Sun Oct 14 2018 Igor Vlasenko <viy@altlinux.ru> 1:2.6.6-alt3.qa1
- NMU: applied repocop patch

* Sun Sep 22 2013 Vladimir Lettiev <crux@altlinux.ru> 1:2.6.6-alt3
- fixed amavisd-new with Perl 5.18
- enable auto requires

* Wed Oct 05 2011 Alexey Shabalin <shaba@altlinux.ru> 1:2.6.6-alt2
- fix perm for config dir

* Thu Jun 09 2011 Alexey Shabalin <shaba@altlinux.ru> 1:2.6.6-alt1
- 2.6.6
- cleanup spec
- add LSB header to init script
- add tmpfiles config for systemd

* Mon Sep 07 2009 Alexey Shabalin <shaba@altlinux.ru> 1:2.6.4-alt1
- 2.6.4
- update altlinux mailing list emails in 35-ruleslisting.conf

* Fri Mar 27 2009 Alexey Borovskoy <alb@altlinux.ru> 1:2.6.2-alt0.M40.1
- 2.6.2.
- DKIM disabled in config file.
- Disable third-party AV's in config. Enable it manually if needed.
- Small spec cleanup. Replace patches with git branches.

* Thu Dec 13 2007 Alexey Shabalin <shaba@altlinux.ru> 1:2.5.3-alt1
- 2.5.3

* Thu Nov 08 2007 Alexey Shabalin <shaba@altlinux.ru> 1:2.5.2-alt1
- 2.5.2
- update russian template notify_sender.txt

* Sat Jun 02 2007 Alexey Shabalin <shaba@altlinux.ru> 1:2.5.1-alt1
- 2.5.1
- revised config files
- Warning! Add suffix "conf" for config files in /etc/amavis/conf.d (bugs read *.rpmsave,*.rpmnew)
- Remove Requires: amavisd-new-ldap-client in amavisd-new-ldap-server (#11783)

* Mon Apr 30 2007 Alexey Shabalin <shaba@altlinux.ru> 1:2.5.0-alt1
- 2.5.0
- drop support for Archive::Tar
- drop the use of libnet (modules Net::SMTP and Net::Cmd)

* Tue Apr 03 2007 Alexey Shabalin <shaba@altlinux.ru> 1:2.4.5-alt2
- add Requires: perl-MIME-tools >= 1:5.417 (#11104)

* Thu Feb 01 2007 Alexey Shabalin <shaba@altlinux.ru> 1:2.4.5-alt1
- 2.4.5

* Wed Dec 06 2006 Alexey Shabalin <shaba@altlinux.ru> 1:2.4.4-alt2
- bugfix - no remove old conf.d/*
- fix config patch in amavisd daemon (patch3)
- fix $sockname in amavisd-release
- fix $unix_socketname in conf.d/15-mta

* Fri Nov 24 2006 Alexey Shabalin <shaba@altlinux.ru> 1:2.4.4-alt1
- 2.4.4
- add control facility for enabled/disabled anti-virus and anti-spam check
- update README.ALT
- rename amavisd-new-README.postfix.ALT to README.ALT.KOI8-R and README.ALT.UTF
- starting amavisd before postfix (#10241)

* Thu Nov 02 2006 Alexey Shabalin <shaba@altlinux.ru> 1:2.4.3-alt1
- 2.4.3
- WARNING! New scheme configs
- default disabled anti-spam and anti-virus check, to enabled edit /etc/amavis/conf.d/01-disable

* Mon Jul 31 2006 Alexey Shabalin <shaba@altlinux.ru> 1:2.4.2-alt2
- AutoReq: noperl, no requires perl/SAVI

* Fri Jul 14 2006 Alexey Shabalin <shaba@altlinux.ru> 1:2.4.2-alt1
- 2.4.1
- add  package p0f
- update patch

* Wed May 17 2006 Alexey Shabalin <shaba@altlinux.ru> 1:2.4.1-alt1
- 2.4.1

* Mon Apr 17 2006 Alexey Shabalin <shaba@altlinux.ru> 1:2.4.0-alt1
- new version (2.4.0)
- require minimal versions of module Net::Server 0.91

* Mon Nov 28 2005 Alexey Shabalin <shaba@altlinux.ru> 1:2.3.3-alt2
- fix summary
- add packages amavisd-new-{utils,ldap-server,cron}
- add virtual packages amavisd-new-{spamassassin,razor,clamav,mysql,postgresql,ldap-client,smtpd}
- package ldap-server require perl-ldap >= 0.32 (#8552)
- package utils contain amavisd-release utility (#8550)

* Wed Sep 14 2005 Alexey Shabalin <shaba@altlinux.ru> 1:2.3.3-alt1
- update 2.3.3
- require minimal versions of module Compress::Zlib 1.35

* Tue Jul 19 2005 Alexey Shabalin <shaba@altlinux.ru> 1:2.3.2-alt2
- Remove Requires: clamav (#4683) 

* Wed Jun 29 2005 Alexey Shabalin <shaba@altlinux.ru> 1:2.3.2-alt1
- update 2.3.2
- require minimal versions of module Archive::Zip 1.14 

* Tue May 24 2005 Alexey Shabalin <shaba@altlinux.ru> 1:2.3.1-alt1
- update 2.3.1
- add depend perl-IO-Zlib
- add cron.daily script for clean quarantine

* Thu Apr 28 2005 Alexey Shabalin <shaba@altlinux.ru> 1:2.3.0-alt1
- update to relise 2.3.0

* Wed Oct 20 2004 Alexey Shabalin <shaba@altlinux.ru> 1:2.1.2-alt1.1
- fix init script - amavisd status (bug #5361)

* Thu Oct 07 2004 Alexey Shabalin <shaba@altlinux.ru> 1:2.1.2-alt1
- update to relise 2.1.2

* Thu Jun 24 2004 Alexey Shabalin <shaba@altlinux.ru> 20030616-alt9.2
- remove script create alias virusalert (#4135)
- Change default email in virus_admin from virusalert to postmaster (#4135)

* Sun May 09 2004 Alexey Shabalin <shaba@altlinux.ru> 20030616-alt9.1
- Update amavisd-new-20030616-p9
- Remove Requires:postfix

* Fri Mar 12 2004 Alexey Shabalin <shaba@altlinux.ru> 20030616-alt8.1
- Update amavisd-new-20030616-p8
- Disable Russian notify by default (for enable edit amavisd.conf)
- Remove amavisd-checkcfg, amavisd-mboxlearnham, amavisd-mboxlearnspam
- Add  amavisd-new-README.postfix.ALT
- Initial build for Sisyphus.

* Thu Dec 11 2003 Alexey Shabalin <shaba@altlinux.ru> 20030616-alt0.1
- First relise for Daedalus
