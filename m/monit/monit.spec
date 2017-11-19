#define beta _beta7
%define beta %nil
%def_enable optimized
%def_with pam

Name: monit
Version: 5.25.1
Release: alt1

Summary: Process monitor and restart utility
License: AGPLv3
Group: Monitoring

Url: http://mmonit.com/monit
Source0: %url/dist/%name-%version%beta.tar.gz
Source1: %name.sysconfig
Source2: monit.init
Source3: monitrc
Source4: %name.cnf
Source5: README.Certificate-Creation
Source6: monitrc.d.tar.gz
Source7: monit.service
Source100: monit.watch
Packager: Michael Shigorin <mike@altlinux.org>

PreReq: openssl
Requires(post,preun): chkconfig
Requires: %name-base = %version-%release
Requires(post,preun): service >= 0.5-alt1

# Automatically added by buildreq on Fri Apr 06 2012
# optimized out: libcom_err-devel libkrb5-devel
BuildRequires: flex libpam-devel libssl-devel zlib-devel

%define _ssldir %_var/lib/ssl
%define _pemdir %_ssldir/certs

Summary(ru_RU.UTF-8): Утилита для мониторинга запущенных процессов
Summary(uk_UA.UTF-8): Утиліта для моніторингу процесів у системі

%package base
Summary: Directory for monit configuration files
Summary(ru_RU.UTF-8): Каталог для конфигурационных файлов monit
Summary(uk_UA.UTF-8): Тека для конфігураційних файлів monit
Group: System/Servers
Provides: /etc/monitrc.d
BuildArch: noarch

%description
monit is an utility for monitoring services or similar programs running on
a Unix system. It will start specified programs if they are not running
and restart programs not responding.  Many checks can be performed:
  - process existence
  - connectability
  - protocol-level (SMTP,POP3,IMAP,NNTP,HTTP,SSH,FTP,SIP)
  - resource usage (cpu/ram)
  - process interdependencies

%description -l ru_RU.UTF-8
Monit предназначен для слежения за выполнением процессов (обычно сервисов),
запущенных в системе UNIX. Monit может следить за несколькими параметрами:
  - существование процесса
  - возможность установления соединения(ий)
  - работоспособность протокола (SMTP,POP3,IMAP,NNTP,HTTP,SSH,FTP,SIP)
  - использование процессом памяти и вычислительных ресурсов
  - зависимости между процессами

%description -l uk_UA.UTF-8
Monit застосовується для стеження за виконанням процесів (зазвичай сервісів),
що запущені у системі UNIX. Monit може слідкувати за декількома параметрами:
  - існування процесу
  - можливість встановлення з'єднання
  - роботоздатність протоколу (SMTP,POP3,IMAP,NNTP,HTTP,SSH,FTP,SIP)
  - використання процесом пам'яті та обчислювальних ресурсів
  - залежності між процесами

%description base
Directory for monit configuration files

%description -l ru_RU.UTF-8 base
Каталог для конфигурационных файлов monit

%description -l uk_UA.UTF-8 base
Тека для конфігураційних файлів monit

%prep
%setup -n %name-%version%beta
sed -i \
	-e 's,allow localhost,use address 127.0.0.1,' \
	-e 's,admin:monit,monit:secretword,' monitrc

%build
sh bootstrap
%autoreconf
%configure \
	%{subst_with pam}

%make_build

%install
%makeinstall_std

# see also #27990
install -pD %buildroot{%_bindir,/bin}/monit
ln -sf ../../bin/monit %buildroot%_bindir/monit

mkdir -p %buildroot%_sysconfdir/sysconfig/
install -pDm644 %SOURCE1 %buildroot%_sysconfdir/sysconfig/%name

cat %SOURCE3 >>monitrc
install -pDm755 %SOURCE2  %buildroot%_initdir/%name
install -pDm600 monitrc %buildroot%_sysconfdir/monitrc
install -pDm644 %SOURCE4  %buildroot%_ssldir/%name.cnf
install -pDm644 %SOURCE7 %buildroot%_unitdir/%name.service

#mkdir -p %buildroot%_sysconfdir/monitrc.d/available/
mkdir -p %buildroot%_sysconfdir/monitrc.d/
mkdir -p %buildroot%_pemdir
touch %buildroot%_pemdir/%name.pem

tar xpf %SOURCE6
cp -a monitrc.d/templates/ %buildroot%_sysconfdir/monitrc.d/
mv monitrc.d examples
ln -s %_docdir/%name-%version/examples %buildroot%_sysconfdir/monitrc.d/EXAMPLES
ln -s monitrc.d %buildroot%_sysconfdir/monit.d

%post
cd %_pemdir
if [ ! -f %name.pem ]; then
	umask 077
	echo -e '\n.\n.\n.\n.\n.\n' |
	openssl req -newkey rsa:1024 -x509 -days 365 -nodes \
		-config %_ssldir/%name.cnf \
		-keyout %name.pem -out %name.pem &>/dev/null
fi

grep -qs '^    allow localhost ' /etc/monitrc && {
  echo "** WARNING: replace 'allow localhost' with 'use address 127.0.0.1'"
  echo "            in /etc/monitrc"; } >&2 ||:

grep -qs '^    allow admin:monit ' /etc/monitrc && {
  echo "** WARNING: replace 'allow admin:monit' with another login:password"
  echo "            in /etc/monitrc"; } >&2 ||:

if ! grep -qs '^set pidfile ' /etc/monitrc /etc/monitrc.d/*; then
  echo "** WARNING: adding 'set pidfile /var/run/monit.pid' to /etc/monitrc" >&2
  {
    echo
    echo "# added by monit-5.17.1-alt3 package upgrade"
    echo "set pidfile /var/run/monit.pid"
  } >> /etc/monitrc
fi

%post_service %name

%preun
%preun_service %name

%files
%doc README* examples/
%config %_initdir/%name
%_unitdir/%name.service
%ghost %attr(600,root,root) %config(noreplace,missingok) %_pemdir/*
%dir %_sysconfdir/monitrc.d/templates/
%config(noreplace) %_sysconfdir/monitrc.d/templates/*
%config(noreplace) %_sysconfdir/monitrc
%config(noreplace) %_ssldir/%name.cnf
%config(noreplace) %_sysconfdir/sysconfig/%name
%_sysconfdir/monitrc.d/EXAMPLES
%_sysconfdir/monit.d
%_man1dir/%name.1.*
%_bindir/%name
/bin/monit

%files base
%dir %_sysconfdir/monitrc.d
#dir %_sysconfdir/monitrc.d/available

# TODO:
# - move to cert-sh-functions for certificate generation?
# - add rsync, oracle tns config snippets (proto checks present)
# - each "check file" += "every 48 cycles"

%changelog
* Sun Nov 19 2017 Michael Shigorin <mike@altlinux.org> 5.25.1-alt1
- new version (watch file uupdate)

* Mon Nov 13 2017 Michael Shigorin <mike@altlinux.org> 5.25.0-alt1
- new version (watch file uupdate)

* Mon Sep 25 2017 Michael Shigorin <mike@altlinux.org> 5.24.0-alt1
- new version (watch file uupdate)

* Fri Jun 16 2017 Michael Shigorin <mike@altlinux.org> 5.23.0-alt1
- new version (watch file uupdate)

* Fri Apr 21 2017 Michael Shigorin <mike@altlinux.org> 5.22.0-alt1
- new version (watch file uupdate)

* Thu Mar 09 2017 Michael Shigorin <mike@altlinux.org> 5.21.0-alt1
- new version (watch file uupdate)

* Sat Oct 22 2016 Michael Shigorin <mike@altlinux.org> 5.20.0-alt1
- new version (watch file uupdate)

* Tue Aug 16 2016 Terechkov Evgenii <evg@altlinux.org> 5.19.0-alt2
- add systemd unit (closes: #32374)

* Thu Aug 11 2016 Michael Shigorin <mike@altlinux.org> 5.19.0-alt1
- new version (watch file uupdate)

* Thu May 26 2016 Michael Shigorin <mike@altlinux.org> 5.18-alt1
- new version (watch file uupdate)

* Wed May 11 2016 Michael Shigorin <mike@altlinux.org> 5.17.1-alt3
- changed "set pidfile" from notice to action (closes: #32086)

* Thu May 05 2016 Michael Shigorin <mike@altlinux.org> 5.17.1-alt2
- tweaked monitrc addition to avoid dups (closes: #30577)
  + added corresponding warning to %%post

* Thu Mar 10 2016 Michael Shigorin <mike@altlinux.org> 5.17.1-alt1.1
- tweaked filesystems, mdadm examples

* Wed Mar 09 2016 Michael Shigorin <mike@altlinux.org> 5.17.1-alt1
- new version (watch file uupdate)

* Sat Mar 05 2016 Michael Shigorin <mike@altlinux.org> 5.17-alt1
- new version (watch file uupdate)

* Fri Feb 05 2016 Michael Shigorin <mike@altlinux.org> 5.16.1-alt1
- new version (watch file uupdate)

* Fri Oct 23 2015 Michael Shigorin <mike@altlinux.org> 5.15-alt1
- new version (watch file uupdate)

* Mon Jun 15 2015 Michael Shigorin <mike@altlinux.org> 5.14-alt1
- new version (watch file uupdate)

* Wed May 06 2015 Michael Shigorin <mike@altlinux.org> 5.13-alt1
- new version (watch file uupdate)

* Tue Mar 24 2015 Michael Shigorin <mike@altlinux.org> 5.12.2-alt1
- new version (watch file uupdate)

* Sun Mar 22 2015 Michael Shigorin <mike@altlinux.org> 5.12.1-alt1
- new version (watch file uupdate)

* Fri Feb 27 2015 Michael Shigorin <mike@altlinux.org> 5.12-alt1
- new version (watch file uupdate)
- NB: replace 'allow localhost' with 'use address 127.0.0.1',
      see also https://bitbucket.org/tildeslash/monit/issue/133/

* Thu Dec 25 2014 Michael Shigorin <mike@altlinux.org> 5.11-alt1
- new version (watch file uupdate)

* Thu Oct 30 2014 Michael Shigorin <mike@altlinux.org> 5.10-alt1
- new version (watch file uupdate)

* Tue Sep 23 2014 Michael Shigorin <mike@altlinux.org> 5.9-alt1
- new version (watch file uupdate)

* Tue May 13 2014 Michael Shigorin <mike@altlinux.org> 5.8.1-alt1
- new version (watch file uupdate)

* Fri Mar 28 2014 Michael Shigorin <mike@altlinux.org> 5.8-alt1
- new version (watch file uupdate)
- seems it's now requisite set pidfile location explicitly

* Mon Mar 17 2014 Michael Shigorin <mike@altlinux.org> 5.7-alt2
- fixes/enhancements by icesik@:
  + converted spec to utf8 (closes: #28406)
  + added sample sysconfig file (closes: #28407)
  + dropped ancient style initscript (for ALM2.2 and before)
  + do not build with explicit optimization to fix debuginfo subpackage
    (closes: #28408)

* Wed Feb 26 2014 Michael Shigorin <mike@altlinux.org> 5.7-alt1
- new version (watch file uupdate)

* Wed Sep 04 2013 Michael Shigorin <mike@altlinux.org> 5.6-alt1
- new version (watch file uupdate)
- dropped libssl detection patch, hooray!

* Wed Jun 05 2013 Michael Shigorin <mike@altlinux.org> 5.5.1-alt1
- new version (watch file uupdate)

* Thu Nov 22 2012 Michael Shigorin <mike@altlinux.org> 5.5-alt3
- relocated monit binary from %_bindir to /bin (closes: #27990)

* Sat Sep 08 2012 Michael Shigorin <mike@altlinux.org> 5.5-alt2
- added apache2 and rsyslog config snippet examples

* Tue Sep 04 2012 Michael Shigorin <mike@altlinux.org> 5.5-alt1
- new version (watch file uupdate)

* Wed May 09 2012 Michael Shigorin <mike@altlinux.org> 5.4-alt2
- added watch file

* Tue May 08 2012 Michael Shigorin <mike@altlinux.org> 5.4-alt1
- 5.4
  + process uptime test added
  + uCLibc support
  + content match test rate fixed
  + /proc files content match test fixed
  + dynamic process state check interval

* Fri Apr 06 2012 Michael Shigorin <mike@altlinux.org> 5.3.2-alt2
- explicitly enabled PAM by default (closes: #27178)
- fixed License: which is AGPLv3, not GPLv3
- buildreq

* Wed Dec 21 2011 Michael Shigorin <mike@altlinux.org> 5.3.2-alt1
- 5.3.2
  + minor bugfixes

* Wed Oct 26 2011 Michael Shigorin <mike@altlinux.org> 5.3.1-alt1
- 5.3.1
  + a feature and bugfix release
- dropped patch (merged upstream)

* Mon Oct 17 2011 Michael Shigorin <mike@altlinux.org> 5.3-alt5
- changed default start/stop priority to 99/01 (see also #26466)

* Mon Oct 03 2011 Michael Shigorin <mike@altlinux.org> 5.3-alt4
- added a patch to fix MySQL protocol check (by lav@)
- added a knob for optimized builds (on by default)

* Thu Sep 22 2011 Michael Shigorin <mike@altlinux.org> 5.3-alt3
- fixed thinko in proposed rootrc (closes: #26315)

* Wed Sep 21 2011 Michael Shigorin <mike@altlinux.org> 5.3-alt2
- rootrc: checksum test failure now results in an alert event
  instead of unmonitor one (closes: #26315)
- EXAMPLES: added dovecot, fail2ban, mdadm, spawn-fcgi, unbound,
  also courtesy of Gulay Boris (closes: #25303)

* Tue Sep 13 2011 Michael Shigorin <mike@altlinux.org> 5.3-alt1
- 5.3
  + 'check program' statement (for exit status)
  + crontab style support for individual services
  + connection retry option
  + protocol connection errors in alerts
  + misc other enhancements and bugfixes
- rediffed the patch

* Sun Apr 03 2011 Michael Shigorin <mike@altlinux.org> 5.2.5-alt2
- base subpackage made noarch

* Mon Mar 28 2011 Michael Shigorin <mike@altlinux.org> 5.2.5-alt1
- 5.2.5

* Tue Feb 22 2011 Michael Shigorin <mike@altlinux.org> 5.2.4-alt1
- 5.2.4

* Mon Feb 14 2011 Michael Shigorin <mike@altlinux.org> 5.2.3-alt2
- fixed dhcpd snippet (dhcpd_rc corresponds to rootstrict template
  currently, not to rootrc)

* Sat Dec 18 2010 Michael Shigorin <mike@altlinux.org> 5.2.3-alt1
- 5.2.3
  + mysql protocol test supports mysql 5.5.x and newer now

* Tue Oct 12 2010 Michael Shigorin <mike@altlinux.org> 5.2.1-alt1.1
- rebuilt against openssl-1.0.0a

* Sat Sep 25 2010 Michael Shigorin <mike@altlinux.org> 5.2.1-alt1
- 5.2.1
  + bugfix for specific HTTP protocol tests, see CHANGES.txt

* Fri Sep 24 2010 Michael Shigorin <mike@altlinux.org> 5.2-alt1
- 5.2
  + added support for:
    - monitoring processes without pidfile using pattern matching
    - swap monitoring
  + allow to override the default action when service doesn't exist
  + added memcache protocol test
  + added openssl FIPS to Monit httpd
  + the 'check system' can now use start/stop program statements too
  + added the option to set the "Reply-To" mail header in mail-format
  + bunch of bugfixes
- updated patch (thanks damir@ yet again for help back then)

* Wed Sep 22 2010 Michael Shigorin <mike@altlinux.org> 5.1.1-alt1.1.1
- disabled port probe in mysql example by default
  (mysqld runs with skip-networking unless reconfigured)

* Fri Jul 23 2010 Michael Shigorin <mike@altlinux.org> 5.1.1-alt1.1
- mail "root@localhost" by default, "+monit" suffix might not work

* Tue Feb 23 2010 Michael Shigorin <mike@altlinux.org> 5.1.1-alt1
- 5.1.1
- removed upstream patch (released)

* Mon Feb 22 2010 Michael Shigorin <mike@altlinux.org> 5.1-alt2
- applied upstream patch for a minor nuisance

* Sat Feb 20 2010 Michael Shigorin <mike@altlinux.org> 5.1-alt1
- 5.1
- rediffed patch
- buildreq

* Fri Oct 30 2009 Michael Shigorin <mike@altlinux.org> 5.0.3-alt4
- added ejabberd and cyrus snippets proposed by dkr@
  (closes: #20358)

* Sun Jun 07 2009 Michael Shigorin <mike@altlinux.org> 5.0.3-alt3
- added "with start delay 60" to default /etc/monitrc
  (so that a minute would be available for services
  to initialize before monit looks down at the system)
- added "include /etc/monitrc.d/*.auto" (disabled by default)
  so that auto-added packaged configuration snippets could be
  enabled all at once

* Fri Jun 05 2009 Michael Shigorin <mike@altlinux.org> 5.0.3-alt2
- largely reworked example configuration snippets:
  + dropped atd (part of vixie-cron now)
  + added cupsd, postgresql, proftpd, system, unfsd, xfs
  + added/fixed/adjusted/dropped groups, should be better now
  + use tabs instead of spaces everywhere
  + uniformly use "localhost" instead of "127.0.0.1"
  + a bunch of *bin/*rc additions
  + misc fixes/cleanups too
- call for server packagers: http://www.altlinux.org/Monit

* Fri May 29 2009 Michael Shigorin <mike@altlinux.org> 5.0.3-alt1
- 5.0.3
  + dropped cvs patch

* Tue May 26 2009 Michael Shigorin <mike@altlinux.org> 5.0.2-alt4
- added upstream CVS patch to fix an issue reported by lav@;
  should be a part of 5.0.3 (fixes: #20158)
- spec cleanup

* Tue May 19 2009 Michael Shigorin <mike@altlinux.org> 5.0.2-alt2
- adapted openvpn config snippet from
  http://www.mcpressonline.com/tips-techniques/system-administration/
  /techtip-monit-the-unix-system-service-watch-dog.html

* Tue May 12 2009 Michael Shigorin <mike@altlinux.org> 5.0.2-alt1
- 5.0.2

* Thu Apr 16 2009 Michael Shigorin <mike@altlinux.org> 5.0-alt1
- 5.0: more than 50 new features and bugfixes

* Fri Feb 27 2009 Michael Shigorin <mike@altlinux.org> 5.0-alt0.7
- 5.0_beta7

* Thu Dec 25 2008 Michael Shigorin <mike@altlinux.org> 5.0-alt0.6
- 5.0_beta6:
  + added idfile (/var/run/monit.id) to stock /etc/monitrc
- fixed pidfile path in slapd example
- updated Url:

* Sat Nov 15 2008 Michael Shigorin <mike@altlinux.org> 5.0-alt0.4
- 5.0_beta4

* Sat Aug 23 2008 Michael Shigorin <mike@altlinux.org> 5.0-alt0.3
- 5.0_beta3
- fixed typo in sshd example: sshd_dsa_key would check
  /etc/openssh/ssh_host_rsa_key not /etc/openssh/ssh_host_dsa_key
  (#16818; thanks naf@ for spotting this)

* Sat Aug 09 2008 ALT QA Team Robot <qa-robot@altlinux.org> 5.0-alt0.1.1
- Automated rebuild due to libssl.so.6 -> libssl.so.7 soname change.

* Sat Apr 19 2008 Michael Shigorin <mike@altlinux.org> 5.0-alt0.1
- 5.0beta1
- incompatible changes:
  + cpu usage test renamed to totalcpu (checks process+children
    memory consumption); new cpu checks only the process itself
    (just like totalmemory/memory was behaving already)
- features:
  + m/mmonit (web interface)
  + SIP protocol test
  + mail notifications hostname setting
  + sync start (wait for parent service before starting children)
  + start/stop timeouts (30 seconds by default)
  + device service test renamed to filesystem
- bugfixes:
  + restart of a slow-starter no longer may start two instances
  + a few crash or unjustified bail-out conditions fixed
- details: http://tildeslash.com/monit/dist/beta/CHANGES.txt
- strict version requirement for monit-base
- install /etc/monitrc.d/templates/* by default
- fixed #11313 (/etc/monit.d -> monitrc.d FC/SuSE compat symlink)
- removed stale patches
- rediffed/submitted upstream the remaining patch

* Fri Apr 11 2008 Michael Shigorin <mike@altlinux.org> 4.10.1-alt5
- fixed Group:

* Fri Mar 14 2008 Michael Shigorin <mike@altlinux.org> 4.10.1-alt4
- applied patch against monitored service double startup due to
  overly fast process status check:
  http://lists.gnu.org/archive/html/monit-dev/2008-03/msg00015.html

* Wed Jan 09 2008 Michael Shigorin <mike@altlinux.org> 4.10.1-alt3
- updated postfix config snippet
- added nginx config snippet (from bliki.rimuhosting.com)

* Mon Dec 31 2007 Michael Shigorin <mike@altlinux.org> 4.10.1-alt2
- fixed typo in spamd configuration snippet (#13832),
  thanks naf@

* Wed Nov 28 2007 Michael Shigorin <mike@altlinux.org> 4.10.1-alt1
- 4.10.1 (minor bugfixes)

* Tue Nov 06 2007 Michael Shigorin <mike@altlinux.org> 4.10-alt1
- 4.10

* Mon Sep 10 2007 Michael Shigorin <mike@altlinux.org> 4.9-alt5
- added monit configuration validity check to initscript
  (on start/restart/reload)

* Mon Jun 25 2007 Michael Shigorin <mike@altlinux.org> 4.9-alt4
- fixed initscript not to overlap two status handlers
  (the more verbose and specific one is now "summary");
  thanks enp@ for buggin' me (#12133)
- modified default monitrc and initscript to point out that
  web interface is used for status/summary too

* Fri Mar 09 2007 Michael Shigorin <mike@altlinux.org> 4.9-alt3
- updated samba config (pidfiles in /var/lock); thanks ab@

* Thu Mar 08 2007 Michael Shigorin <mike@altlinux.org> 4.9-alt2
- updated postfix configuration snippet (moved to libexec: #10965,
  thanks Slava Dubrovskiy (dubrsl@) for notification)
- added configuration (will likely need manual editing) for:
  amavisd, apcupsd, nscd, privoxy, proftpd, sendmail, slapd, snmpd, spamd
- NB: samba example needs an update (regarding pidfiles at least)

* Tue Feb 20 2007 Michael Shigorin <mike@altlinux.org> 4.9-alt1
- 4.9 (minor feature enhancements)
- removed patch2 (was from CVS so already included)
- fixed summary in Russian, added in Ukrainian

* Thu Dec 28 2006 Michael Shigorin <mike@altlinux.org> 4.8.2-alt4
- monit-base now provides /etc/monitrc.d (fixes: #10559)

* Fri Dec 22 2006 Michael Shigorin <mike@altlinux.org> 4.8.2-alt3
- service off by default, see also [ru]:
  http://lists.altlinux.org/pipermail/devel/2006-December/039909.html

* Mon Dec 04 2006 Michael Shigorin <mike@altlinux.org> 4.8.2-alt2
- added CVS patch to fix "-l" option, see 
  http://lists.gnu.org/archive/html/monit-dev/2006-12/msg00004.html

* Mon Nov 20 2006 Michael Shigorin <mike@altlinux.org> 4.8.2-alt1
- 4.8.2
- spec cleanup (including lots of cruft and M22 support)
- updated Packager:

* Fri Sep 01 2006 Michael Shigorin <mike@altlinux.org> 4.8.1-alt1
- 4.8.1
- fixed #9910 (default monitrc needed an update);
  thanks hiddenman@

* Thu May 04 2006 Michael Shigorin <mike@altlinux.org> 4.8-alt1
- 4.8

* Sun Mar 19 2006 Michael Shigorin <mike@altlinux.org> 4.7-alt7
- spec fixes to (hopefully) enable changes in 4.7-alt6
  (thanks damir@ again; I can't verify x86_64 build myself)

* Sat Mar 18 2006 Michael Shigorin <mike@altlinux.org> 4.7-alt6
- added configure patch by Damir Shayhutdinov (damir@)
  to fix build (particularly on x86_64)

* Thu Mar 09 2006 Michael Shigorin <mike@altlinux.org> 4.7-alt5
- fixed monitrc not to mention external domains -- currently
  from: was referring nonexistant as of today domain name
  and what's worse, alert destination mentioned existing
  domain with quite possibly existing user name; as was proposed
  earlier and is implemented now, "root@localhost" is more safe
  and robust default

* Fri Mar 03 2006 Michael Shigorin <mike@altlinux.org> 4.7-alt4
- fixed #9173 (incorrect sample configuration for
  ntpd monitoring), thanks gns@

* Fri Jan 27 2006 Michael Shigorin <mike@altlinux.org> 4.7-alt3
- added: clamd, clamsmtpd, jabberd2, mysqld (fixed #7169)

* Mon Jan 23 2006 Michael Shigorin <mike@altlinux.org> 4.7-alt2
- fixed DOS EOLs in monitrc too (thanks to abulava@ for alerting)

* Fri Jan 13 2006 Michael Shigorin <mike@altlinux.org> 4.7-alt1
- 4.7

* Tue Jan 10 2006 Michael Shigorin <mike@altlinux.org> 4.6-alt1
- rebuilt for Sisyphus

* Thu Nov 24 2005 Michael Shigorin <mike@altlinux.org> 4.6-alt0.M24.1
- 4.6

* Wed Aug 24 2005 Michael Shigorin <mike@altlinux.org> 4.5.1-alt0.M24.1
- built for ALM2.4
- conf split: syslogd -> syslogd + klogd (for vservers)
- run dos2unix on config snippets (*yuck*)
- repackaged monitrc.d as tar.bz2 instead of cpio.bz2

* Mon Apr 18 2005 Alexey Beleckiy <sinister@emt.com.ua> 4.5.1-alt1
- 4.5.1

* Thu Feb 24 2005 Michael Shigorin <mike@altlinux.ru> 4.4-alt2.1
- added patch regarding memory stats based on SuSE's 4.3 package
  (thanks homyakov@)

* Thu Feb 17 2005 Igor Homyakov <homyakov at altlinux dot ru> 4.4-alt2
- package splited into monit and monit-base

* Thu Feb 17 2005 Igor Homyakov <homyakov at altlinux dot ru> 4.4-alt1
- 4.4
- update spec

* Mon May 10 2004 ALT QA Team Robot <qa-robot@altlinux.org> 4.1.1-alt1.1
- Rebuilt with openssl-0.9.7d.

* Tue Mar 02 2004 Igor Homyakov <homyakov at altlinux dot ru> 4.2-alt20040302cvs
- cvs snapshot 2004-03-02

* Tue Feb 17 2004 Igor Homyakov <homyakov at altlinux dot ru> 4.2-alt20040217cvs
- cvs snapshot 2004-02-17

* Mon Feb 16 2004 Igor Homyakov <homyakov at altlinux dot ru> 4.2-alt20040216cvs
- cvs snapshot 2004-02-16
- added %_sysconfdir/%{name}rc.d directory

* Fri Feb 13 2004 Igor Homyakov <homyakov at altlinux dot ru> 4.1.1-alt1
- 4.1.1
- move daemon to %_bindir directory
- new SysV startup script
- update default config file
- s!%_sysconfdir/init.d/!/sbin/service !
- fixed forbiden requires for fileutils

* Wed Dec 25 2002 Igor Homyakov <homyakov at altlinux dot ru> 3.1-alt1
- 3.1
- cleanups for ALT package policy
- update system config file
- add ssl files
- add patch from CVS (calculation of the daylight saving)

* Tue Sep 17 2002 Igor Homyakov <homyakov at altlinux dot ru> 3.0-alt1
- 3.0-alt1
- fixed little bug in config file
- strict permissions to config file

* Wed Jul 18 2002 Igor Homyakov <homyakov at altlinux dot ru> 2.5-alt1
- build package for ALT Linux distribution
- added ALT specific config file and startup script

* Wed Jul 10 2002 Rory Toma <rory@digeo.com>
- Upgraded to monit-2.4.3

* Mon Feb 05 2001 Clinton Work <work@scripty.com>
- Upgraded to monit 1.2
- Use chkconfig to add monit to the rc.d startup scripts
- Use the example monitrc instead of my custom monit.conf
- Fixed the monit homepage URL

* Thu Feb 01 2001 Clinton Work <work@scripty.com>
- Create the inital spec file
- Created a sample config file and a rc startup script
