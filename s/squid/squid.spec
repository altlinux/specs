%def_disable poll
%def_enable epoll

# epoll is enabled by default, so disable it if plain poll is enabled
%if_enabled poll
%force_disable epoll
%endif

Name: squid
Version: 3.1.19
Release: alt2

Summary: The Squid proxy caching server
Summary(ru_RU.KOI8-R): Кэширующий прокси-сервер Squid
License: GPL-2
Group: System/Servers

Url: http://www.squid-cache.org/
Packager: Squid Development Team <squid@packages.altlinux.org>

Source: %url/Versions/v2/%name-%version.tar
Source2: %name.init
Source3: %name.logrotate
Source4: wbinfo_group.sh
Source5: %name.sysconfig
Source6: %name.pam
Source7: %name.service

Obsoletes: %name-novm

BuildConflicts: bind-devel
BuildPreReq: rpm-build >= 4.0.4-alt10

# Automatically added by buildreq on Mon May 18 2009
BuildRequires: cppunit-devel gcc-c++ libdb4-devel libldap-devel libpam-devel libssl-devel libkrb5-devel libcap-devel libltdl-devel perl-Pod-Parser libsasl2-devel

# Used by smb_auth.pl,pop3.pl and squid_db_auth, required on find-requires stage:
BuildRequires: perl-Authen-Smb perl-libnet perl-DBI

Patch1: squid-3.1.7-kerb_auth-link-alt.patch
Patch2: squid-3.1.7-install-pinger-alt.patch
Patch3: squid-3.1.0.9-location.patch
Patch4: squid-3.1.7-default-logrotate-alt.patch
Patch5: squid-3.1.13-default-paths-in-var-alt.patch

Requires: %name-common = %version-%release, %name-server = %version-%release, %name-helpers = %version-%release, %name-helpers-perl = %version-%release, %name-cachemgr = %version-%release

%description
Squid is a high-performance proxy caching server for Web clients,
supporting FTP, gopher, and HTTP data objects. Unlike traditional
caching software, Squid handles all requests in a single,
non-blocking, I/O-driven process. Squid keeps meta data and especially
hot objects cached in RAM, caches DNS lookups, supports non-blocking
DNS lookups, and implements negative caching of failed requests.
Install squid if you need a proxy caching server.

%description -l ru_RU.KOI8-R
Squid --- высокопроизводительный кэширующий прокси-сервер для web-клиентов
с поддержкой протоколов FTP, gopher и HTTP. В отличие от традиционного кэширующего
ПО Squid обрабатывает все запросы в едином неблокирующем процессе. Squid хранит
метаданные и особенно часто запрашиваемые объекты в ОЗУ, кэширует DNS-запросы,
поддерживает неблокирующие DNS-запросы и реализует негативное кэширование
неудачных запросов.
Установите squid, если вам необходим кэширующий прокси-сервер.



%package conf-default
Summary: default %name config
Group: System/Servers
Requires: %name-common
Provides: %name-conf = %version-%release, %_sysconfdir/%name/%name.conf
%{expand:%%global o_list %(for n in host2cat; do echo -n "%name-conf-$n "; done)}
%{?o_list:Conflicts: %o_list}
BuildArch: noarch

%description conf-default
This package contains default %name config



%package server
Summary: main Squid server and its necessary files
Summary(ru_RU.KOI8-R): главный сервер Squid и необходимые ему файлы
Group: System/Servers
PreReq: net-snmp-mibs
Requires: %name-common, %name-conf, %_sysconfdir/%name/%name.conf
Conflicts: %name <= 2.5.STABLE9-alt3
Obsoletes: %name-pinger

%description server
This package contains Squid main server and its necessary files
as well as pinger, unlinkd and diskd.
Install squid package to get all Squid parts.

%description -l ru_RU.KOI8-R server
Этот пакет содержит главный сервер Squid и необходимые для его работы файлы,
а также pinger, unlinkd и diskd.
Установите пакет squid, чтобы получить все компоненты Squid.



%package cachemgr
Summary: Squid CGI cache manager
Summary(ru_RU.KOI8-R): CGI-диспетчер для Squid
Group: Networking/WWW
Requires: %name-common
Conflicts: %name <= 2.5.STABLE9-alt3

%description cachemgr
This package contains Squid cache manager. It is a standalone CGI application which
can be used to manage Squid processes remotely over HTTP.
Install squid package to get all Squid parts.

%description -l ru_RU.KOI8-R cachemgr
Этот пакет содержит диспетчер для Squid. Это самостоятельное приложение CGI, которое
может быть использовано для управления процессами Squid удалённо через HTTP.
Установите пакет squid, чтобы получить все компоненты Squid.



%package common
Summary: Squid common files
Summary(ru_RU.KOI8-R): общие файлы для Squid
Group: System/Servers
PreReq: shadow-groups
Conflicts: %name <= 2.5.STABLE9-alt3
BuildArch: noarch

%description common
This package contains common Squid files.
Install squid package to get all Squid parts.

%description -l ru_RU.KOI8-R common
Этот пакет содержит файлы, необходимые для squid-server и squid-cachemgr.
Установите пакет squid, чтобы получить все компоненты Squid.


%package helpers
Summary: Squid helpers
Summary(ru_RU.KOI8-R): вспомогательные программы для squid-server
Group: System/Servers
Requires: %name-common
Conflicts: %name <= 2.5.STABLE9-alt3

%description helpers
This package contains Squid helpers for different kinds of authentication.
Install squid package to get all Squid parts.

%description -l ru_RU.KOI8-R helpers
Этот пакет содержит вспомогательные программы для squid-server, поддерживающие
различные виды аутентификации.
Установите пакет squid, чтобы получить все компоненты Squid.

%package helpers-perl
Summary: Squid Perl helpers
Summary(ru_RU.KOI8-R): вспомогательные Perl-программы для squid-server
Group: System/Servers
Requires: %name-common
Conflicts: %name <= 2.5.STABLE9-alt3
BuildArch: noarch

%description helpers-perl
This package contains Perl Squid helpers for different kinds of authentication.
Install squid package to get all Squid parts.

%description -l ru_RU.KOI8-R helpers-perl
Этот пакет содержит вспомогательные Perl-программы для squid-server, поддерживающие
различные виды аутентификации.
Установите пакет squid, чтобы получить все компоненты Squid.

%prep
%setup -q

%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p2
%patch5 -p1

find . -type f -name '*.pl' -print0 | \
	xargs -r0 sed -ie 's,/usr/local/bin/perl,/usr/bin/perl,g'

%build
%configure \
	--bindir=%_sbindir \
	--libexecdir=%_libexecdir/%name \
	--localstatedir=%_var \
	--sysconfdir=%_sysconfdir/%name \
	--datadir=%_datadir/%name \
	%{subst_enable poll} \
	%{subst_enable epoll} \
	--enable-snmp \
	--enable-removal-policies="lru heap" \
	--enable-delay-pools \
	--enable-icmp \
	--enable-htcp \
	--enable-async-io=16 \
	--enable-wccp \
	--enable-wccpv2 \
	--enable-arp-acl \
	--enable-ssl \
	--enable-forw-via-db \
	--enable-useragent-log \
	--enable-referer-log \
	--enable-ident-lookups \
	--enable-carp \
	--enable-ntlm-fail-open \
	--enable-cache-digests \
	--enable-x-accelerator-vary \
	--enable-auth="basic ntlm digest negotiate" \
	--enable-basic-auth-helpers="DB LDAP MSNT NCSA PAM POP3 SASL SMB YP getpwnam multi-domain-NTLM squid_radius_auth" \
	--enable-ntlm-auth-helpers="smb_lm fakeauth no_check" \
	--enable-digest-auth-helpers="ldap password eDirectory" \
	--enable-negotiate-auth-helpers="squid_kerb_auth" \
	--enable-external-acl-helpers="ip_user ldap_group unix_group session wbinfo_group" \
	--enable-storeio="aufs diskd ufs" \
	--enable-disk-io="AIO Blocking DiskDaemon DiskThreads" \
	--enable-default-err-language="English" \
	--enable-icap-client \
	--enable-linux-netfilter \
	--with-large-files \
	--with-filedescriptors=16384 \
	--with-default-user="%name"

%make_build
%make_build check

%install
%make_build install DESTDIR=%buildroot
%make_build install-pinger DESTDIR=%buildroot

install -pD -m755 %SOURCE2 %buildroot%_initdir/%name
install -pD -m644 %SOURCE3 %buildroot%_sysconfdir/logrotate.d/%name

mkdir -p %buildroot%_logdir/%name
mkdir -p %buildroot%_spooldir/%name

install -p -m644 helpers/basic_auth/PAM/pam_auth.8 %buildroot%_man8dir
install -p -m644 helpers/external_acl/ldap_group/squid_ldap_group.8 %buildroot%_man8dir
install -p -m644 helpers/basic_auth/LDAP/squid_ldap_auth.8 %buildroot%_man8dir
install -p -m644 helpers/external_acl/unix_group/squid_unix_group.8 %buildroot%_man8dir
install -p -m644 doc/squid.8 %buildroot%_man8dir
install -p -m644 doc/cachemgr.cgi.8 %buildroot%_man8dir

install -pD -m644 helpers/basic_auth/SMB/COPYING-2.0 helpers/doc/SMB.COPYING-2.0
install -pD -m644 helpers/basic_auth/SMB/README helpers/doc/SMB.README
install -pD -m644 helpers/basic_auth/SMB/smb_auth.sh helpers/doc/smb_auth.sh
install -pD -m644 helpers/basic_auth/SMB/ChangeLog helpers/doc/SMB.ChangeLog
install -pD -m644 helpers/basic_auth/LDAP/README helpers/doc/LDAP.README
install -pD -m644 helpers/basic_auth/MSNT/COPYING-2.0 helpers/doc/MSNT.COPYING-2.0
install -pD -m644 helpers/basic_auth/MSNT/README.html helpers/doc/MSNT.README.html
install -pD -m644 helpers/basic_auth/MSNT/msntauth.conf.default helpers/doc/msntauth.conf.default
install -pD -m644 helpers/basic_auth/SASL/README helpers/doc/SASL.README
install -pD -m644 helpers/basic_auth/SASL/squid_sasl_auth helpers/doc/squid_sasl_auth
install -pD -m644 helpers/basic_auth/SASL/squid_sasl_auth.conf helpers/doc/squid_sasl_auth.conf
install -pD -m644 helpers/basic_auth/SMB/README helpers/doc/SASL.README
install -pD -m644 helpers/basic_auth/multi-domain-NTLM/README.txt helpers/doc/NTLM.README.txt
install -pD -m644 helpers/external_acl/ip_user/README helpers/doc/ip_user.README
install -pD -m644 helpers/external_acl/ip_user/example-deny_all_but.conf helpers/doc/ip_user.example-deny_all_but.conf
install -pD -m644 helpers/external_acl/ip_user/example.conf helpers/doc/ip_user.example.conf
install -pD -m644 helpers/external_acl/unix_group/README helpers/doc/unix_group.README
install -pD -m644 helpers/external_acl/unix_group/README helpers/doc/unix_group.README
install -pD -m644 helpers/ntlm_auth/no_check/README.no_check_ntlm_auth helpers/doc/README.no_check_ntlm_auth

install -p -m755 %SOURCE4 %buildroot%_libexecdir/%name/
mkdir -p %buildroot%_datadir/snmp/mibs
mv %buildroot%_datadir/%name/mib.txt %buildroot%_datadir/snmp/mibs/SQUID-MIB.txt

install -D -m644 %SOURCE5 %buildroot%_sysconfdir/sysconfig/%name
install -D -m644 %SOURCE6 %buildroot%_sysconfdir/pam.d/%name
install -D -m644 %SOURCE7 %buildroot%systemd_unitdir/%name.service

%pre common
%_sbindir/groupadd -r -f %name
%_sbindir/useradd -r -n -g %name -d %_spooldir/%name -s /dev/null %name >/dev/null 2>&1 ||:
# fixing #6321, step 1/2
%_bindir/gpasswd -a squid shadow

%pre server
chown %name:%name %_logdir/%name/*.log >/dev/null 2>&1 ||:
chmod 660 %_logdir/%name/*.log >/dev/null 2>&1 ||:

%post server
%post_service %name

%preun server
%preun_service %name

%triggerpostun server -- squid < 2.4.STABLE4-alt1
[ $2 -gt 0 ] || exit 0
chown -R %name:%name %_spooldir/%name >/dev/null 2>&1 ||:

%files
%doc COPYRIGHT README ChangeLog QUICKSTART RELEASENOTES.html SPONSORS
%doc doc/debug-sections.txt

%files conf-default
%config(noreplace) %_sysconfdir/%name/%name.conf

%files server
%config(noreplace) %_sysconfdir/%name/%name.conf.default
%config(noreplace) %_sysconfdir/%name/%name.conf.documented
%config(noreplace) %_sysconfdir/%name/mime.conf
%config(noreplace) %_sysconfdir/%name/mime.conf.default
%config(noreplace) %_sysconfdir/%name/errorpage.css
%config(noreplace) %_sysconfdir/%name/errorpage.css.default
%config(noreplace) %_sysconfdir/sysconfig/%name
%_initdir/%name
%systemd_unitdir/%name.service
%config %_sysconfdir/logrotate.d/%name
%dir %_datadir/%name
%_datadir/%name/errors
%_datadir/%name/icons
%_datadir/snmp/mibs/SQUID-MIB.txt
%_sbindir/%name
%_sbindir/squidclient
%_man8dir/squid.*
%_man1dir/squidclient.*
%attr(4710,root,%name) %_libexecdir/%name/pinger
%_libexecdir/%name/unlinkd
%_libexecdir/%name/diskd
%attr(3770,root,%name) %dir %_logdir/%name
%attr(2770,root,%name) %dir %_spooldir/%name

%files helpers
%doc helpers/doc/*
%config(noreplace) %_sysconfdir/%name/msntauth.conf
%config(noreplace) %_sysconfdir/%name/msntauth.conf.default
%_libexecdir/%name/digest_pw_auth
%_libexecdir/%name/fakeauth_auth
%_libexecdir/%name/getpwname_auth
%_libexecdir/%name/ip_user_check
%_libexecdir/%name/msnt_auth
%_libexecdir/%name/ncsa_auth
%_libexecdir/%name/ntlm_smb_lm_auth
%attr(640,root,auth) %config(noreplace) %_sysconfdir/pam.d/%name
# fixing #6321, step 2/2
%attr(2711,root,auth) %_libexecdir/%name/pam_auth
%_libexecdir/%name/sasl_auth
%_libexecdir/%name/smb_auth
%_libexecdir/%name/smb_auth.sh
%_libexecdir/%name/squid_ldap_auth
%_libexecdir/%name/squid_ldap_group
%_libexecdir/%name/squid_unix_group
%_libexecdir/%name/digest_ldap_auth
%_libexecdir/%name/squid_session
%_libexecdir/%name/digest_edir_auth
%_libexecdir/%name/squid_kerb_auth
#%_libexecdir/%name/wb_auth
#%_libexecdir/%name/wb_group
#%_libexecdir/%name/wb_ntlmauth
%_libexecdir/%name/wbinfo_group.sh
%_libexecdir/%name/yp_auth
%_libexecdir/%name/squid_radius_auth
%_libexecdir/%name/negotiate_kerb_auth
%_libexecdir/%name/negotiate_kerb_auth_test
%_libexecdir/%name/squid_kerb_auth_test

%_man8dir/pam_auth.*
%_man8dir/ncsa_auth.*
%_man8dir/squid_ldap_auth.*
%_man8dir/squid_ldap_group.*
%_man8dir/squid_unix_group.*
%_man8dir/squid_session.*
%_man8dir/squid_radius_auth.*

%files helpers-perl
%doc scripts/*.pl
%_libexecdir/%name/no_check.pl
%_libexecdir/%name/smb_auth.pl
%_libexecdir/%name/wbinfo_group.pl
%_libexecdir/%name/pop3.pl
%_libexecdir/%name/squid_db_auth
%_man8dir/squid_db_auth.*

%files cachemgr
%config(noreplace) %_sysconfdir/%name/cachemgr.conf
%config(noreplace) %_sysconfdir/%name/cachemgr.conf.default
%_libexecdir/%name/cachemgr.cgi
%_man8dir/cachemgr.cgi.*

%files common
%attr(750,root,%name) %dir %_sysconfdir/%name
%attr(750,root,%name) %dir %_libexecdir/%name


%changelog
* Fri May 04 2012 Vitaly Kuznetsov <vitty@altlinux.ru> 3.1.19-alt2
- Add systemd unit file

* Mon Apr 23 2012 Vitaly Kuznetsov <vitty@altlinux.ru> 3.1.19-alt1
- 3.1.19

* Thu Dec 08 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 3.1.18-alt1
- 3.1.18

* Mon Oct 17 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 3.1.16-alt1
- 3.1.16

* Wed Sep 07 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 3.1.15-alt1
- 3.1.15 (with CVE-2011-3205 fix)

* Tue Jul 26 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 3.1.14-alt1
- 3.1.14

* Fri Jul 01 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 3.1.13-alt1
- 3.1.13

* Mon Apr 11 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 3.1.12-alt1
- 3.1.12

* Wed Mar 23 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 3.1.11-alt2
- repair build

* Tue Feb 08 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 3.1.11-alt1
- 3.1.11

* Fri Dec 24 2010 Vitaly Kuznetsov <vitty@altlinux.ru> 3.1.10-alt1
- 3.1.10

* Mon Nov 15 2010 Vitaly Kuznetsov <vitty@altlinux.ru> 3.1.9-alt2
- fix build

* Tue Oct 26 2010 Vitaly Kuznetsov <vitty@altlinux.ru> 3.1.9-alt1
- 3.1.9

* Sun Oct 03 2010 Vitaly Kuznetsov <vitty@altlinux.ru> 3.1.8-alt2
- rebuild with openssl-1.0.0a

* Tue Sep 14 2010 Vitaly Kuznetsov <vitty@altlinux.ru> 3.1.8-alt1
- 3.1.8

* Tue Aug 31 2010 Vitaly Kuznetsov <vitty@altlinux.ru> 3.1.7-alt1
- 3.1.7

* Fri Sep 25 2009 Grigory Batalov <bga@altlinux.ru> 3.0.STABLE19-alt1
- New upstream release.

* Mon Aug 24 2009 Grigory Batalov <bga@altlinux.ru> 3.0.STABLE18-alt2
- Export Kerberos keytab name (ALT #20413).

* Wed Aug 05 2009 Grigory Batalov <bga@altlinux.ru> 3.0.STABLE18-alt1
- Bugfix for previous release.

* Tue Aug 04 2009 Grigory Batalov <bga@altlinux.ru> 3.0.STABLE17-alt1
- New upstream release, including SQUID-2009:2 fix.
- squid_unix_group: new -K switch to strip kerberos realm
  from username (ALT #20840).
- Require exact sub-packages version by squid umbrella (ALT #20723).

* Thu Jul 02 2009 Grigory Batalov <bga@altlinux.ru> 3.0.STABLE16-alt1
- New upstream release.
- Include PAM config for pam_auth helper (#20665).

* Fri Jun 26 2009 Grigory Batalov <bga@altlinux.ru> 3.0.STABLE15-alt2
- Helpers were moved to %%_libexecdir according to GNU Coding Standards.
- KRB5_KTNAME was set in the initscript and in the /etc/sysconfig/squid.

* Mon May 18 2009 Grigory Batalov <bga@altlinux.ru> 3.0.STABLE15-alt1
- New upstream release.
- Fix building with gcc-4.4.

* Fri May 15 2009 Grigory Batalov <bga@altlinux.ru> 3.0.STABLE13-alt4
- Set default http_port to 3128.

* Fri May 08 2009 Grigory Batalov <bga@altlinux.ru> 3.0.STABLE13-alt3
- Enable Linux netfilter.

* Mon Apr 13 2009 Grigory Batalov <bga@altlinux.ru> 3.0.STABLE13-alt2
- Default config is separated.

* Tue Apr 07 2009 Grigory Batalov <bga@altlinux.ru> 3.0.STABLE13-alt1
- New upstream release.
- Obsolete FAQ is removed.
- squid_radius_auth helper is enabled.

* Mon Nov 10 2008 Grigory Batalov <bga@altlinux.ru> 2.6.STABLE22-alt1
- New upstream release.

* Wed May 21 2008 Grigory Batalov <bga@altlinux.ru> 2.6.STABLE20-alt1
- New upstream release.

* Sat Feb 16 2008 Grigory Batalov <bga@altlinux.ru> 2.6.STABLE18-alt1
- New upstream release.

* Sun Jan 27 2008 Dmitry V. Levin <ldv@altlinux.org> 2.6.STABLE17-alt2
- Fixed build with fresh autotools.

* Sun Dec 02 2007 Grigory Batalov <bga@altlinux.ru> 2.6.STABLE17-alt1
- New upstream release.
  + security fix for SQUID-2007:2
- Post-install scripts were moved to common and server packages.

* Fri Sep 28 2007 Grigory Batalov <bga@altlinux.ru> 2.6.STABLE16-alt1
- New upstream release (#12920).
- Cumulative patch from git.
- Prefer epoll to poll (#12919).
- More authentication helpers.
- Specfile cleanup.

* Sun May 13 2007 Grigory Batalov <bga@altlinux.ru> 2.6.STABLE13-alt1
- New upstream release.
- ICAP patch cleaned up.

* Wed Apr 11 2007 Grigory Batalov <bga@altlinux.ru> 2.6.STABLE12-alt3
- Reload service in a safe manner.

* Thu Mar 29 2007 Grigory Batalov <bga@altlinux.ru> 2.6.STABLE12-alt2
- Provide %_datadir/%name directory.

* Wed Mar 21 2007 Grigory Batalov <bga@altlinux.ru> 2.6.STABLE12-alt1
- New upstream release
  + includes security fix SQUID-2007:1.
- Official ICAP patch updated and cleaned up.
- DrWeb's ICAP patch obsoleted (disabled).

* Thu Feb 22 2007 Grigory Batalov <bga@altlinux.ru> 2.6.STABLE9-alt2
- Remove extra access_log directive from config.
- Export default port settings into separate patch.

* Thu Feb 08 2007 Grigory Batalov <bga@altlinux.ru> 2.6.STABLE9-alt1
- New upstream release
 + includes NTLM authentication DoS fix, see squid bug #1873.
- Official ICAP patch updated.

* Mon Dec 25 2006 Grigory Batalov <bga@altlinux.ru> 2.6.STABLE6-alt3
- Set absolute link to chpasswd.cgi tarball.
- Applied:
 + DrWeb's ICAP patch
 + Config updated: redirector template
 + ACL max_body_size

* Wed Dec 20 2006 Grigory Batalov <bga@altlinux.ru> 2.6.STABLE6-alt2
- Don't ban underscores in hostname.
- By default use poll.

* Wed Dec 13 2006 Grigory Batalov <bga@altlinux.ru> 2.6.STABLE6-alt1
- New upstream release.
- Applied:
 + ICAP support
 + correct file location in QUICKSTART
 + config-driven maximum file descriptor number
 + build with HTCP, WCCPv2, SNMP but disable in config
 + open rsync, snews, CUPS, SWAT by default
 + prevent appending local domain to localhost
 + update smb_auth.sh
 + run unlinkd on diskd and ufs only
 + helpers list update
 + get back default port to listen to
 + get back default access logging
 + use epoll instead of poll
 + allow X-Forwarded-For following
 + allow forward_log config directive
 + allow Referer logging
 + allow Ident (RFC931) lookups
 + allow multicast notification of cache misses
 + suggest -c option to digest auth helper
 + squid-pinger obsoleted by squid-server
 + add libdb4-devel to BuildRequires
 + quote percent sign (%%) in changelog
- Included into upstream:
 + squid-2.5.STABLE13-libaio-2.patch
 + squid-2.5.STABLE13-header_leak.patch
 + squid-2.5.STABLE13-ident_leak.patch
 + squid-2.5.STABLE13-htcp_leak.patch
 + squid-2.5.STABLE13-icons.patch
 + squid-2.5.STABLE13-hostnamelen.patch
 + squid-2.5.STABLE13-stable13.patch
- Obsoleted:
 + squid-2.4.STABLE6-alt-without-bind.patch
 + squid-2.5-automake.patch
 + squid-2.5.STABLE10-alt-perlreq.patch

* Wed May 17 2006 Denis Ovsienko <pilot@altlinux.ru> 2.5.STABLE13-alt1
- STABLE13
- applied:
 + 2006-05-13 13:16 (Minor) On some systems POSIX AIO functions are in libaio
 + 2006-05-14 15:41 (Medium) Memory leak in header processing related to external_acl or custom log formats
 + 2006-05-14 15:41 (Major) memory leak in ident processing
 + 2006-05-14 15:41 (Medium) Memleak in HTCP client code
 + 2006-05-14 15:41 (Minor) Mime icons are not displayed when viewing ftp sites when
 + 2006-05-14 15:41 (Cosmetic) SQUIDHOSTNAMELEN issues
 + 2006-05-14 15:41 (Cosmetic) Current release is STABLE13, not 12..
- updated FAQ to v 1.263 2006/03/16

* Sun Oct 30 2005 Denis Ovsienko <pilot@altlinux.ru> 2.5.STABLE12-alt1
- STABLE12
- applied:
 + 2005-10-26 20:31 (Minor) fails to compile with undefined reference to setenv

* Wed Sep 28 2005 Denis Ovsienko <pilot@altlinux.ru> 2.5.STABLE11-alt2
- applied:
 + 2005-09-27 22:29 (Major) Truncated responses when using delay pools

* Sun Sep 25 2005 Denis Ovsienko <pilot@altlinux.ru> 2.5.STABLE11-alt1
- STABLE11 includes all patches issued for STABLE10
- replaced max filedescriptors override trick with configure option
- updated FAQ to v 1.253 2005/09/07

* Fri Sep 16 2005 Denis Ovsienko <pilot@altlinux.ru> 2.5.STABLE10-alt6
- applied:
 + 2005-09-13 02:59 (Minor) Solaris 10 SPARC transparent proxy build problem with ipfilter
 + 2005-09-03 09:41 (Minor) E-mail sent when cache dies is blocked from many antispam rules
 + 2005-09-11 00:57 (Minor) LDAP helpers does not work with TLS (-Z option)
 + 2005-09-11 01:21 (Cosmetic) Incorrect store dir selection debug message on objects >2G
 + 2005-09-11 01:21 (Cosmetic) enums can not be assumed to be signed ints
 + 2005-09-11 01:42 (Cosmetic) Allow leaving core dumps on Linux
 + 2005-09-11 01:53 (Medium) Clients bypassing delay pools by faking a cache hit
 + 2005-09-13 23:59 (Minor) Transparent proxy problem with IP Filter
 + 2005-09-15 09:56 (Medium) Odd results on pipelined CONNECT requests
 + 2005-09-16 11:10 (Major) FATAL: Incorrect scheme in auth header

* Sat Sep 03 2005 Denis Ovsienko <pilot@altlinux.ru> 2.5.STABLE10-alt5
- applied:
 + 2005-08-14 17:05 (Cosmetic) New 'mail_program' configuration option in squid.conf 
 + 2005-08-19 09:31 (Minor) sync redeclarations when support for ARP acls
 + 2005-09-01 20:27 (Major) Segmentation fault in sslConnectTimeout
 + 2005-09-01 21:56 (Medium) assertion failed: StatHist.c:93: ((int) floor(0.99L + statHistVal(H, 0) - min)) == 0
 + 2005-09-01 22:09 (Minor) More chroot_dir and squid -k reconfigure issues
 + 2005-09-01 22:18 (Cosmetic) Odd URLs when failing to forward request via parent and several error messages inconsistent in reported request details
 + 2005-09-01 22:26 (Cosmetic) Fails to compile with glibc -D_FORTIFY_SOURCE=2
 + 2005-09-01 22:31 (Minor) Some odd FTP servers respond with 250 where 226 is expected
 + 2005-09-01 22:39 (Cosmetic) Greek translation of error messages
 + 2005-09-01 22:44 (Major) assertion failed: store.c:523: "e->store_status == STORE_PENDING"
 + 2005-09-01 22:49 (Minor) squid_ldap_auth -U does not work
 + 2005-09-01 22:57 (Minor) snmo cacheClientTable fails on "long" IP addresses

* Thu Aug 11 2005 Denis Ovsienko <pilot@altlinux.ru> 2.5.STABLE10-alt4
- fixed #2713 (wrong SAMBAPREFIX)
- applied:
 + 2005-07-03 08:24 (Cosmetic) "make all" gives many warnings
 + 2005-07-09 08:58 (Cosmetic) Allow wb_ntlm_auth to run more silent
 + 2005-07-11 00:46 (Cosmetic) The new --with-build-environment=... option doesn't work

* Thu Jun 30 2005 Denis Ovsienko <pilot@altlinux.ru> 2.5.STABLE10-alt3
- pinger, diskd and unlinkd move to squid-server
- updated:
 + 2005-06-27 21:24 (Minor) squid -k fails in combination with chroot after patch for bug 1157
 + 2005-06-30 08:49 (Minor) Core dump with --enable-ipf-transparent if access to NAT device not granted
- applied:
 + 2005-06-29 20:36 (Minor) wbinfo_group.pl only looks into the first group specified

* Wed Jun 29 2005 Denis Ovsienko <pilot@altlinux.ru> 2.5.STABLE10-alt2
- impoving #6321 resolution

* Fri Jun 24 2005 Denis Ovsienko <pilot@altlinux.ru> 2.5.STABLE10-alt1
- new version
- #6321 fix
- #1491 and associated cleanups
- #6307 fix
- #7062 fix
- eliminated pinger package
- applied:
 + 2005-05-25 23:01 (Cosmetic) Double content-length often harmless
 + 2005-06-06 21:38 (Cosmetic) Updated Spanish error messages
 + 2005-06-09 08:01 (Minor) Squid internal icons served up with slightly incorrect HTTP headers
 + 2005-06-13 22:55 (Minor) squid -k fails in combination with chroot after patch for bug 1157
 + 2005-06-13 22:55 (Minor) Core dump with --enable-ipf-transparent if access to NAT device not granted
 + 2005-06-13 22:55 (Minor) httpd_accel_signle_host incompatible with redireection
 + 2005-06-19 09:39 (Minor) squid -k reconfigure internal corruption if the type of a cache_dir is changed
 + 2005-06-19 21:03 (Minor) SNMP GETNEXT fails if the given OID is outside the Squid MIB
 + 2005-06-22 10:45 (Cosmetic) Title in FTP listings somewhat messed up
 + 2005-06-21 22:28 (Minor) FTP listings uses "BASE HREF" much more than it needs to

* Thu May 12 2005 Denis Ovsienko <pilot@altlinux.ru> 2.5.STABLE9-alt3
- applied:
 + 2005-04-20 14:59 (Medium) Fails to process requests for files larger than 2GB in size
 + 2005-03-26 23:53 (Minor) rename() related cleanup
 + 2005-03-29 09:52 (Cosmetic) New cachemgr pending_objects and client_objects actions
 + 2005-03-30 22:51 (Cosmetic) external acls requiring authentication does not request new credentials on access denials like proxy_auth does.
 + 2005-04-26 04:42 (Cosmetic) should syslog to daemon facility not local4
 + 2005-04-20 21:36 (Cosmetic) Error template substitution for authenitcated user name
 + 2005-04-21 10:46 (Cosmetic) Missing newlines in debug statements
 + 2005-04-20 21:55 (Minor) fix transparent proxying when squid listens on NATed non-80 port
 + 2005-04-20 21:55 (Minor) Unable to run "squid -k" when hostname cannot be determined
 + 2005-04-21 10:31 (Cosmetic) Correctly read DOS/Windows formatted config files with CRLF as line terminator
 + 2005-04-22 20:21 (Minor) Unrecognized cache-control directives are silently dropped
 + 2005-04-24 16:35 (Minor) Make the use of the %%m error page to return auth info messages
 + 2005-04-22 20:48 (Cosmetic) PID file check fails when chrooting
 + 2005-04-26 04:30 (Minor Security) Fix for CVE-1999-0710: cachemgr malicouse use
 + 2005-04-25 16:36 (Cosmetic) Minor aufs improvements
 + 2005-04-30 12:58 (Medium) Poor hot object cache hit ratio and sporadic assertion failed: store_swapin.c: e->mem_status == NOT_IN_MEMORY
 + 2005-05-01 10:58 (Cosmetic) Cosmetic change to DISKD statistics
 + 2005-05-04 18:09 (Minor) SNMP Agent updates to support SNMP Version 2 and bulk requests
 + 2005-05-08 14:01 (Cosmetic) Minor arp ACL improvements
 + 2005-05-09 01:51 (Minor) Allow dstdomain and dstdom_regex to match IP based hosts
 + 2005-05-11 19:19 (Security issue) DNS lookups unreliable on untrusted networks
 + 2005-05-10 22:33 (Medium) assertion failed: store_client.c:343: "storeSwapOutObjectBytesOnDisk(mem) > sc->copy_offset"
 + 2005-05-10 23:11 (Cosmetic) Extended documentation of the always_direct directive
- updated:
 + 2005-04-19 22:46 (Cosmetic) LDAP helpers fails to compile with SUN LDAP SDK
 + 2005-03-29 08:45 (Minor) Several minor aufs issues
- updated FAQ to v 1.250 2005/04/22
- enabled 2GB+ files support
- disabled aa patch for now

* Tue Mar 22 2005 Denis Ovsienko <pilot@altlinux.ru> 2.5.STABLE9-alt2
- applied:
 + 2005-03-03 02:26 (Minor Security) Race condition related to Set-Cookie header 
 + 2005-03-04 11:55 (Minor) Fails to parse the EPLF FTP directory format
 + 2005-03-04 11:55 (Minor) Links in FTP listings without / fails due to missing BASE HREF
 + 2005-03-04 22:48 (Cosmetic Security) Unexpected access control results on configuration errors
 + 2005-03-09 15:46 (Minor) Handle odd date formats
 + 2005-03-09 15:46 (Minor) reload_into_ims fails to revalidate negatively cached entries
 + 2005-03-09 15:46 (Cosmetic) Clarify delay_access function
 + 2005-03-09 15:46 (Cosmetic) Check several squid.conf directives for int overflows
 + 2005-03-09 15:46 (Minor) bzero is a non-standard function not available on all platforms
 + 2005-03-15 04:27 (Minor) compile warnings due to pid_t not being an int
 + 2005-03-10 23:38 (Minor) Incorrect use of ctype functions
 + 2005-03-09 15:46 (Cosmetic) Defer digest fetch if the peer is not allowed to be used
 + 2005-03-09 15:46 (Cosmetic) Duplicate content-length headers logged as conflicting with relaxed_header_parser off
 + 2005-03-09 15:46 (Cosmetic) Extend relaxed_header_parser to work around "excess data from" errors from many major web servers.
 + 2005-03-19 11:42 (Minor) Several minor aufs issues
 + 2005-03-19 00:25 (Minor) Basic authentication fails with very long login or password
 + 2005-03-21 20:44 (Minor) CONNECT requests truncated if client side disconnects first assertion failed: comm.c:430: "quot;ntohs(address->sin_port) != 0"quot;
 + 2005-03-19 01:11 (Cosmetic) LDAP helpers fail to compile with SUN LDAP SDK
 + 2005-03-19 01:35 (Minor) --disable-hostname-checks not working
 + 2005-03-19 23:57 (Cosmetic) aufs warning about open event filedescriptors on shutdown
- updated FAQ to v 1.246 2005/03/04 23:49:39

* Tue Mar 01 2005 Denis Ovsienko <pilot@altlinux.ru> 2.5.STABLE9-alt1
- upstream merged:
 + 2005-02-20 10:47 (Minor) Relax header parsing slightly again to work around broken web servers
 + 2005-02-20 19:11 (Cosmetic) GCC4 warnings
 + 2005-02-21 01:38 (Cosmetic) Doesn't work specifying the AR variable to configure
 + 2005-02-21 02:58 (Minor) Peer related memory leaks on "squid -k reconfigure"
 + 2005-02-21 03:38 (Cosmetic) Display FTP URLs in decoded format to allow for sane display of national characters etc
 + 2005-02-21 17:02 (Minor) fqdn lookups with spaces may confuse redirectors
 + 2005-02-23 00:11 (Medium) Should not automatically retry request on 403 and other server errors
- upstream updated and merged:
 + 2005-02-20 11:03 (Cosmetic) Cross-platform format fixes
- updated FAQ to v 1.245 2005/02/24 23:29:59

* Wed Feb 16 2005 Denis Ovsienko <pilot@altlinux.ru> 2.5.STABLE8-alt1
- upstream merged:
 + 2005-02-04 11:41 (Minor) WCCP easily disturbed by forged packets 
 + 2005-02-06 00:57 (Cosmetic) Improve password handling in FTP gatewaying of ftp://user@host URLs
 + 2005-02-11 10:59 (Major) Data corruption when HTTP reply headers is split in several packets
- upstream updated and merged:
 + 2005-01-31 01:50 (Security issue) Strengthen Squid from HTTP response splitting cache pollution attack
 + 2005-02-10 10:14 (Security issue) Reject malformed HTTP requests and responses that conflict with the HTTP specifications
- applied new:
 + 2005-02-13 05:58 (Major) Assertion failure on certain odd DNS responses
 + 2005-02-15 00:03 (Cosmetic) Cross-platform format fixes
 + 2005-02-15 01:07 (Cosmetic) Allow high characters in generated FTP and Gopher directory listings
 + 2005-02-15 02:14 (Cosmetic) FTP URL cleanups


* Fri Feb 04 2005 Denis Ovsienko <pilot@altlinux.ru> 2.5.STABLE7-alt8
- libpam-devel -> libpam0-devel
- Russian description
- applied:
 + 2005-01-31 22:50 (Security issue) Correct handling of oversized reply headers
 + 2005-02-03 23:17 (Minor) LDAP helpers sends slightly malformed search requests
 + 2005-02-03 23:27 (Minor) Sporadic segmentation fault when using ntlm authentication
 + 2005-02-04 00:12 (Major) Segmentation fault on failed PUT/POST request
 + 2005-02-04 00:33 (Medium) Persistent connection trouble on failed PUT/POST requests

* Sat Jan 29 2005 Denis Ovsienko <pilot@altlinux.ru> 2.5.STABLE7-alt7
- updated squid-2.5.STABLE7-header_parsing.patch once more
- applied:
 + 2005-01-28 23:16 (Security issue) Buffer overflow in WCCP recvfrom() call

* Mon Jan 24 2005 Denis Ovsienko <pilot@altlinux.ru> 2.5.STABLE7-alt6
- applied current patches:
 + 2005-01-21 12:43 (Security issue) Strengthen Squid from HTTP response splitting cache pollution attack
 + 2005-01-21 12:10 (Minor) Icons fails to load on non-anonymous FTP when using short_icons_url directive
 + 2005-01-21 12:10 (Minor) FTP data connection fails on some FTP servers when requesting directory without a trailing slash
 + 2005-01-21 12:10 (Minor) Disable Path-MTU discovery on intercepted requests
 + 2005-01-24 14:29 (Security issue) Reject malformed HTTP requests and responses that conflict with the HTTP specifications
 + 2005-01-17 04:29 (Minor Secuity issue) Sanity check usernames in squid_ldap_auth
 + 2005-01-17 02:52 (Minor) FQDN names truncated on compressed DNS responses
 + 2005-01-17 02:52 (Minor) Internal DNS memory leak on malformed responses

* Thu Jan 13 2005 Denis Ovsienko <pilot@altlinux.ru> 2.5.STABLE7-alt5
- applied current patches:
 + 2005-01-12 17:21 (Security issue) Denial of service with forged WCCP messages
 + 2005-01-12 17:19 (Security issue) buffer overflow bug in gopherToHTML()
 + 2005-01-08 03:13 (Medium) fakeauth_auth memory leak and NULL pointer access
 + 2004-12-28 12:55 (Minor) Don't close "other" filedescriptors on startup
 + 2004-12-21 17:50 (Minor Security) Confusing results on empty acl declarations
 + 2004-12-08 00:00 (Minor) PURGE is allowed to delete internal objects
- fix for #5767 (config patch and initgroups)
- fix for #5616 (squid MIB)
- fix for #5707 (wbinfo_group.pl and spaces)
- updated FAQ to 1.240 2005/01/08 00:16:21
- used macro instead of env var for rpm build root

* Thu Dec 09 2004 Denis Ovsienko <pilot@altlinux.ru> 2.5.STABLE7-alt4
- applied current patches:
 + 2004-12-08 01:03 (Minor) cachemgr vm_objects segfault
 + 2004-12-08 00:47 (Minor) httpd_accel_port 0 (virtual) not working correctly
 + 2004-12-07 23:45 (Cosmetic / Minor Security issue) Random error messages in response to malformed host name

* Sat Dec 04 2004 Denis Ovsienko <pilot@altlinux.ru> 2.5.STABLE7-alt3
- applied current patches:
 + 2004-11-07 23:37 (Minor) Squid fails to close TCP connection after blank HTTP response
 + 2004-11-06 21:42 (Minor) 100%% CPU on startup on new/experimental Linux kernels due to O_NONBLOCK
 + 2004-11-06 15:28 (Minor) Failure to shut down busy helpers on -k rotate/reconfigure
 + 2004-10-20 23:23 (Minor) The new req_header and resp_header acls segfaults immediately on parse of squid.conf
 + 2004-10-19 10:09 (Cosmetic) Document -v (protocol version) option to LDAP helpers
 + 2004-10-14 22:48 (Minor) 100%% CPU usage on half-closed PUT/POST requests

* Sun Nov 14 2004 Dmitry V. Levin <ldv@altlinux.org> 2.5.STABLE7-alt2
- Cleaned up build dependencies, was too superfluous
  since 2.5.STABLE6-alt1.
- Rebuilt with openldap-2.2.18-alt3.

* Tue Oct 12 2004 Denis Ovsienko <pilot@altlinux.ru> 2.5.STABLE7-alt1
- 2.5.STABLE7 (security fix)
- updated FAQ to 1.235 2004/10/04
- rediffed patches

* Sat Sep 04 2004 Denis Ovsienko <pilot@altlinux.ru> 2.5.STABLE6-alt3
- more patches

* Tue Aug 17 2004 Denis Ovsienko <pilot@altlinux.ru> 2.5.STABLE6-alt2
- Updated FAQ to 2004-08-10
- Added and rediffed official patches up to 2004-08-14
- build with 16384 file descriptors

* Fri Jul 23 2004 Konstantin Timoshenko <kt@altlinux.ru> 2.5.STABLE6-alt1
- 2.5.STABLE6
- Official bugfixes from www.%name-cache.org.
- add patch-aa.patch: makes squid write info in access.log by pieces as far as the
  receipt of data but not after downloading whole file. See -x options.

* Thu Jun 10 2004 Konstantin Timoshenko <kt@altlinux.ru> 2.5.STABLE5-alt4
- Official bugfixes from www.%name-cache.org.
- fix bugs id #4330

* Wed May 26 2004 Konstantin Timoshenko <kt@altlinux.ru> 2.5.STABLE5-alt3
- fix bugs id #1629

* Fri May 14 2004 Konstantin Timoshenko <kt@altlinux.ru> 2.5.STABLE5-alt2
- build with 8192 file descriptors
- Official bugfixes from www.%name-cache.org.

* Wed May 12 2004 ALT QA Team Robot <qa-robot@altlinux.org> 2.5.STABLE5-alt1.1
- Rebuilt with openssl-0.9.7d.

* Wed Mar 03 2004 Konstantin Timoshenko <kt@altlinux.ru> 2.5.STABLE5-alt1
- 2.5.STABLE5

* Thu Dec 18 2003 Konstantin Timoshenko <kt@altlinux.ru> 2.5.STABLE4-alt5
- fix build with libsasl2

* Mon Dec 08 2003 Konstantin Timoshenko <kt@altlinux.ru> 2.5.STABLE4-alt4
- Official bugfixes from www.%name-cache.org.
- cosmetics spec file

* Tue Nov 04 2003 Konstantin Timoshenko <kt@altlinux.ru> 2.5.STABLE4-alt3
- Fixed %%pre script.

* Tue Oct 21 2003 Konstantin Timoshenko <kt@altlinux.ru> 2.5.STABLE4-alt2
- Official bugfixes from www.%name-cache.org.
- disable default ICP setup.

* Fri Sep 26 2003 Konstantin Timoshenko <kt@altlinux.ru> 2.5.STABLE4-alt1
- 2.5.STABLE4

* Mon Jul 21 2003 Konstantin Timoshenko <kt@altlinux.ru> 2.5.STABLE3-alt3
- fix errors in squid init file.

* Mon Jul 14 2003 Konstantin Timoshenko <kt@altlinux.ru> 2.5.STABLE3-alt2
- Added Belarusian error pages by Vital Khilko (dojlid@mova.org)

* Fri Jul 11 2003 Konstantin Timoshenko <kt@altlinux.ru> 2.5.STABLE3-alt1
- 2.5.STABLE3
- fix bugs id #0002717
- Official bugfixes from www.%name-cache.org.
- Rewritten start/stop script to new rc scheme.

* Thu Nov 28 2002 Konstantin Timoshenko <kt@altlinux.ru> 2.5.STABLE1-alt5
- fix build support for the authentication schemes
- Official bugfixes from www.%name-cache.org.

* Mon Nov 25 2002 Konstantin Timoshenko <kt@altlinux.ru> 2.5.STABLE1-alt4
- fix documentations and manuals path

* Fri Nov 01 2002 Konstantin Timoshenko <kt@altlinux.ru> 2.5.STABLE1-alt3
- fix documentation

* Thu Oct 24 2002 Konstantin Timoshenko <kt@altlinux.ru> 2.5.STABLE1-alt2
- Fixed path on directories: %_var/run, %_logdir/%name and %_spooldir/%name.

* Tue Oct 22 2002 Konstantin Timoshenko <kt@altlinux.ru> 2.5.STABLE1-alt1
- 2.5.STABLE1
- misc adaptions

* Thu Aug 29 2002 Konstantin Timoshenko <kt@altlinux.ru> 2.4.STABLE7-alt4
- buildprereq autoconf = 2.13
- adding --enable-storeio

* Sun Jul 07 2002 Konstantin Timoshenko <kt@altlinux.ru> 2.4.STABLE7-alt3
- Official bugfixes from www.%name-cache.org.

* Thu Jul 04 2002 Stanislav Ievlev <inger@altlinux.ru> 2.4.STABLE7-alt2
- Relocated "chown" cleanup code from %%pre to %%triggerpostun (#1051).

* Wed Jul 03 2002 Konstantin Timoshenko <kt@altlinux.ru> 2.4.STABLE7-alt1
- 2.4.STABLE7

* Fri Jun 28 2002 Dmitry V. Levin <ldv@altlinux.org> 2.4.STABLE6-alt4
- Official bugfixes from www.%name-cache.org.

* Thu Jun 27 2002 Dmitry V. Levin <ldv@altlinux.org> 2.4.STABLE6-alt3
- Official bugfixes from www.%name-cache.org.

* Wed Apr 03 2002 Dmitry V. Levin <ldv@alt-linux.org> 2.4.STABLE6-alt2
- Build without bind-devel.

* Fri Mar 22 2002 Dmitry V. Levin <ldv@alt-linux.org> 2.4.STABLE6-alt1
- 2.4.STABLE6.

* Wed Mar 06 2002 Konstantin Timoshenko <kt@altlinux.ru> 2.4.STABLE4-alt2
- adding subpackage pinger.
- remove link to errors dir.

* Wed Feb 20 2002 Dmitry V. Levin <ldv@alt-linux.org> 2.4.STABLE4-alt1
- 2.4.STABLE4-alt1
- Fixed permissions on directories:
  %_sysconfdir/%name, %_libdir/%name, %_logdir/%name and %_spooldir/%name.

* Mon Feb 18 2002 Dmitry V. Levin <ldv@alt-linux.org> 2.4.STABLE3-alt2
- Added official patches for 2.4.STABLE3:
  + "htcp_port 0" fails to disable the HTCP port
  + Coredup on certain ftp:// style URL's
  + SNMP memory leaks
- Fixed %%pre script.

* Fri Feb 15 2002 Konstantin Timoshenko <kt@altlinux.ru> 2.4.STABLE3-alt1
- 2.4.STABLE3

* Mon Sep 24 2001 Kostya Timoshenko <kt@altlinux.ru> 2.4.STABLE2-alt1
- enable auth-modules LDAP, MSNT, NCSA, PAM, SMB, YP, getpwnam
- bugfix patches

* Mon Apr 16 2001 Kostya Timoshenko <kt@altlinux.ru> 2.4.STABLE1-ipl2mdk
- enable wccp, gnu-regex, cache-digests

* Mon Mar 26  2001 Kostya Timoshenko <kt@petr.kz> 2.4.STABLE1-ipl1mdk
- 2.4.STABLE1

* Mon Feb  5 2001 Kostya Timoshenko <kt@petr.kz> 2.3.STABLE4-ipl4mdk
- enable useragen log, icmp, async-io

* Wed Jan 17 2001 Kostya Timoshenko <kt@petr.kz>
- security fix for tmpfile problems (patch#20)

* Wed Jan  3 2001 Kostya Timoshenko <kt@petr.kz>
- fixed squid.init

* Wed Dec 27 2000 Kostya Timoshenko <kt@petr.kz>
- Rebuild for RE

* Sun Nov 12 2000 Geoffrey Lee <snailtalk@mandrakesoft.com> 2.3.STABLE4-1mdk
- shiny version.
- comment out already applied patches.

* Tue Sep  5 2000 Etienne Faure  <etienne@mandraksoft.com> 2.3.STABLE2-3mdk
- rebuilt with %%doc macro
- added noreplace tag for config files

* Tue May  2 2000 Jean-Michel Dault <jmdault@mandrakesoft.com> 2.3.STABLE2-2mdk
- fixed %post script
- three more bugfix patches from the squid people
- buildprereq jade, sgmltools

* Fri Apr  7 2000 Jean-Michel Dault <jmdault@mandrakesoft.com> 2.3.STABLE2-1mdk
- merged with redhat again

* Sun Mar 26 2000 Florian La Roche <Florian.LaRoche@redhat.com>
- make %pre more portable

* Thu Mar 16 2000 Bill Nottingham <notting@redhat.com>
- bugfix patches
- fix dependency on /usr/local/bin/perl

* Sat Mar  4 2000 Bill Nottingham <notting@redhat.com>
- 2.3.STABLE2

* Mon Feb 14 2000 Bill Nottingham <notting@redhat.com>
- Yet More Bugfix Patches

* Tue Feb  8 2000 Bill Nottingham <notting@redhat.com>
- add more bugfix patches
- --enable-heap-replacement

* Mon Jan 31 2000 Cristian Gafton <gafton@redhat.com>
- rebuild to fix dependencies

* Fri Jan 28 2000 Bill Nottingham <notting@redhat.com>
- grab some bugfix patches

* Mon Jan 10 2000 Bill Nottingham <notting@redhat.com>
- 2.3.STABLE1 (whee, another serial number)

* Tue Dec 21 1999 Bernhard Rosenkraenzer <bero@redhat.com>
- Fix compliance with ftp RFCs
  (http://www.wu-ftpd.org/broken-clients.html)
- Work around a bug in some versions of autoconf
- BuildPrereq sgml-tools - we're using sgml2html

* Mon Oct 18 1999 Bill Nottingham <notting@redhat.com>
- add a couple of bugfix patches

* Wed Oct 13 1999 Bill Nottingham <notting@redhat.com>
- update to 2.2.STABLE5.
- update FAQ, fix URLs.

* Sat Sep 11 1999 Cristian Gafton <gafton@redhat.com>
- transform restart in reload and add restart to the init script

* Tue Aug 31 1999 Bill Nottingham <notting@redhat.com>
- add squid user as user 23.

* Mon Aug 16 1999 Bill Nottingham <notting@redhat.com>
- initscript munging
- fix conflict between logrotate & squid -k (#4562)

* Wed Jul 28 1999 Bill Nottingham <notting@redhat.com>
- put cachemgr.cgi back in /usr/lib/squid

* Wed Jul 14 1999 Bill Nottingham <notting@redhat.com>
- add webdav bugfix patch (#4027)

* Mon Jul 12 1999 Bill Nottingham <notting@redhat.com>
- fix path to config in squid.init (confuses linuxconf)

* Wed Jul  7 1999 Bill Nottingham <notting@redhat.com>
- 2.2.STABLE4

* Wed Jun 9 1999 Dale Lovelace <dale@redhat.com>
- logrotate changes
- errors from find when /var/spool/squid or
- /var/log/squid didn't exist

* Thu May 20 1999 Bill Nottingham <notting@redhat.com>
- 2.2.STABLE3

* Thu Apr 22 1999 Bill Nottingham <notting@redhat.com>
- update to 2.2.STABLE.2

* Sun Apr 18 1999 Bill Nottingham <notting@redhat.com>
- update to 2.2.STABLE1

* Thu Apr 15 1999 Bill Nottingham <notting@redhat.com>
- don't need to run groupdel on remove
- fix useradd

* Mon Apr 12 1999 Bill Nottingham <notting@redhat.com>
- fix effective_user (bug #2124)

* Mon Apr  5 1999 Bill Nottingham <notting@redhat.com>
- strip binaries

* Thu Apr  1 1999 Bill Nottingham <notting@redhat.com>
- duh. adduser does require a user name.
- add a serial number

* Tue Mar 30 1999 Bill Nottingham <notting@redhat.com>
- add an adduser in %pre, too

* Thu Mar 25 1999 Bill Nottingham <notting@redhat.com>
- oog. chkconfig must be in %preun, not %postun

* Wed Mar 24 1999 Bill Nottingham <notting@redhat.com>
- switch to using group squid
- turn off icmp (insecure)
- update to 2.2.DEVEL3
- build FAQ docs from source

* Tue Mar 23 1999 Bill Nottingham <notting@redhat.com>
- logrotate changes

* Sun Mar 21 1999 Cristian Gafton <gafton@redhat.com>
- auto rebuild in the new build environment (release 4)

* Wed Feb 10 1999 Bill Nottingham <notting@redhat.com>
- update to 2.2.PRE2

* Wed Dec 30 1998 Bill Nottingham <notting@redhat.com>
- cache & log dirs shouldn't be world readable
- remove preun script (leave logs & cache @ uninstall)

* Tue Dec 29 1998 Bill Nottingham <notting@redhat.com>
- fix initscript to get cache_dir correct

* Fri Dec 18 1998 Bill Nottingham <notting@redhat.com>
- update to 2.1.PATCH2
- merge in some changes from RHCN version

* Sat Oct 10 1998 Cristian Gafton <gafton@redhat.com>
- strip binaries
- version 1.1.22

* Sun May 10 1998 Cristian Gafton <gafton@redhat.com>
- don't make packages conflict with each other...

* Sat May 02 1998 Cristian Gafton <gafton@redhat.com>
- added a proxy auth patch from Alex deVries <adevries@engsoc.carleton.ca>
- fixed initscripts

* Thu Apr 09 1998 Cristian Gafton <gafton@redhat.com>
- rebuilt for Manhattan

* Fri Mar 20 1998 Cristian Gafton <gafton@redhat.com>
- upgraded to 1.1.21/1.NOVM.21

* Mon Mar 02 1998 Cristian Gafton <gafton@redhat.com>
- updated the init script to use reconfigure option to restart squid instead
  of shutdown/restart (both safer and quicker)

* Sat Feb 07 1998 Cristian Gafton <gafton@redhat.com>
- upgraded to 1.1.20
- added the NOVM package and tryied to reduce the mess in the spec file

* Wed Jan 7 1998 Cristian Gafton <gafton@redhat.com>
- first build against glibc
- patched out the use of setresuid(), which is available only on kernels
  2.1.44 and later
