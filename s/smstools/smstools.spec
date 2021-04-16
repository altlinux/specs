Name: smstools
Version: 3.1.21
Release: alt2

Summary: SMS Gateway software which can send and receive short messages through GSM modems and mobile phones
License: GPL-2.0+
Group: Communications

Url: http://smstools3.kekekasvi.com
Source0: http://smstools3.kekekasvi.com/packages/smstools3-%version.tar.gz
Source1: smsd.init
Source2: smsd.logrotate
Source3: smsd.conf

Patch1: enable-statistics.patch
Patch2: fix-makefile-override.patch
Patch3: gawk-path-fix.patch
Patch4: hardening.patch
Patch5: spelling.patch
Patch6: gcc10.patch

BuildRequires: libmm-devel

%description
The SMS server tools allow setting up a central SMS gateway. It sends and
receives SMS messages using a simple file-based interface. It can accommodate
up to 20,000 messages a month.

It supports an event-handler option that allows calling customized programs or
scripts after sending or receiving SMS messages.

The SMS Server Tools use one or more (max. 32) GSM modems to send and receive
SMS messages. Some modems may be equipped with SIM cards such as Vodafone or
Telmi ones.  All messages are sorted in queues by the provider. If one modem
fails, it will be deactivated for one hour before the software retries, while
other modems run without any restriction. The status information and alarms are
logged with syslog.

%prep
%setup -q
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1

# build with debug info
subst '/ggdb/ s/^#//' src/Makefile
# correct mode for html docs
find doc -type f -exec chmod 644 {} \;

%build
%make_build

%install
mkdir -p %buildroot%_spooldir/sms/{checked,failed,incoming,outgoing,sent}
mkdir -p %buildroot%_logdir/smsd/smsd_stats
mkdir -p %buildroot%_initdir
mkdir -p %buildroot%_sbindir
mkdir -p %buildroot%_logrotatedir
cp %SOURCE1 %buildroot%_initdir/smsd
cp %SOURCE2 %buildroot%_logrotatedir/smsd
cp %SOURCE3 %buildroot%_sysconfdir
cp src/smsd %buildroot%_sbindir

%pre
/usr/sbin/groupadd -r -f smsd
/usr/sbin/useradd -r -n -g smsd -d /dev/null -s /dev/null -c SMSd -G uucp,smsd smsd >/dev/null 2>&1 ||:

%post
%post_service smsd

%preun
%preun_service smsd

%files
%attr(0640,root,smsd) %config(noreplace) %_sysconfdir/smsd.conf
%attr(0640,root,root) %config(noreplace) %_logrotatedir/smsd
%attr(0755,root,root) %_initdir/smsd
%attr(0755,root,root) %_sbindir/smsd
%dir %attr(770,root,smsd) %_spooldir/sms
%dir %attr(770,root,smsd) %_spooldir/sms/checked
%dir %attr(770,root,smsd) %_spooldir/sms/failed
%dir %attr(770,root,smsd) %_spooldir/sms/incoming
%dir %attr(770,root,smsd) %_spooldir/sms/outgoing
%dir %attr(770,root,smsd) %_spooldir/sms/sent
%dir %attr(770,root,smsd) %_logdir/smsd
%dir %attr(770,root,smsd) %_logdir/smsd/smsd_stats
%doc README LICENSE examples doc

%changelog
* Fri Apr 16 2021 Andrey Cherepanov <cas@altlinux.org> 3.1.21-alt2
- Apply patches from Debian.

* Mon Jul 01 2019 Andrey Cherepanov <cas@altlinux.org> 3.1.21-alt1
- New version (ALT #36961).
- Enable statistics.

* Tue Oct 02 2012 Vladimir Lettiev <crux@altlinux.ru> 3.1.14-alt1
- initial build
