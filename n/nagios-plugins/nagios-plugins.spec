# TODO:
#  - generate old style command definitions for NRPE?

%define nagios_plugdir %_libexecdir/nagios/plugins
%define plugins_cmddir %_sysconfdir/nagios/commands
%define nagios_usr nagios
%define nagios_grp nagios

Name: nagios-plugins
Version: 1.4.15
Release: alt1

Summary: Host/service/network monitoring plug-ins for Nagios(R)
Summary(ru_RU.UTF-8): Модули мониторинга (plug-ins) хостов/сервисов/сети для Nagios(R)

License: GPL
Group: Monitoring
URL: http://nagiosplug.sourceforge.net

Packager: Dmitry Lebkov <dlebkov@altlinux.ru>

Source0: http://prdownloads.sf.net/nagiosplug/nagiosplug/%version/%name-%version.tar
Source1: notify_via_jabber
Source2: nagios-plugins-README.ALT.UTF-8

# Commands definitions for Nagios
Source10: nagios-plugins.cfg
Source11: nagios-plugins-local.cfg
Source12: nagios-plugins-network.cfg
Source13: nagios-plugins-ldap.cfg
Source14: nagios-plugins-mysql.cfg
Source15: nagios-plugins-pgsql.cfg
Source16: nagios-plugins-radius.cfg
Source17: nagios-plugins-samba.cfg
Source18: nagios-plugins-perl.cfg
Source19: nagios-plugins-snmp.cfg
Source20: nagios-plugins-extra.cfg

Patch0: %name-1.4.11-alt-perlfix.patch
Patch1: %name-1.4.14-alt-makefile.patch
# add needed packages to requires
#Patch2: %name-1.4.13-alt-configure.patch
Patch3: %name-1.4.12-alt-pgsql.patch
Patch4: %name-1.4.13-alt-hasher-hack.patch

# patches from Fedora
Patch101: nagios-plugins-0001-Do-not-use-usr-local-for-perl.patch
Patch102: nagios-plugins-0002-Remove-assignment-of-not-parsed-to-jitter.patch
Patch103: nagios-plugins-0003-Fedora-specific-fixes-for-searching-for-diff-and-tai.patch
Patch105: nagios-plugins-0005-Patch-for-check_linux_raid-with-on-linear-raid0-arra.patch
Patch106: nagios-plugins-0006-Prevent-check_swap-from-returning-OK-if-no-swap-acti.patch


%define _perl_lib_path %nagios_plugdir

Requires: nagios-plugins-common = %version-%release
Requires: iputils procps

# Automatically added by buildreq on Tue Aug 12 2008
BuildRequires: libMySQL-devel libldap-devel libradiusclient-ng-devel libpq-devel libssl-devel postgresql-devel zlib-devel perl-Math-BigInt perl-Net-SNMP

# checked in configure checking
BuildRequires: iputils procps fping qstat bind-utils net-snmp-clients openssh-clients sendmail-common glibc-utils samba-client

# for correct ps detection
BuildRequires: /proc

%description
Nagios is a program that will monitor hosts and services on your
network, and to email or page you when a problem arises or is
resolved. Nagios runs on a unix server as a background or daemon
process, intermittently running checks on various services that you
specify. The actual service checks are performed by separate "plugin"
programs which return the status of the checks to Nagios.

This package contains the basic plugins necessary for use with the
Nagios package.  This package should install cleanly on almost any
RPM-based system.

%package common
Summary: Common files for Nagios(R) plug-ins
Group: Monitoring
PreReq: nagios-daemon

%description common
Common files for Nagios(R) plugi-ins.


%package local
Summary: Nagios(R) plug-ins for checking local services and resources
Group: Monitoring
Requires: nagios-plugins-common = %version-%release
Requires: procps

%description local
Nagios(R) plugi-ins for checking local services and resources.


%package network
Summary: Nagios(R) plug-ins for checking remote hosts and services
Group: Monitoring
Requires: nagios-plugins-common = %version-%release
Requires: openssh-clients bind-utils fping iputils ntpdate

%description network
Nagios(R) plugi-ins for checking remote hosts and services.


%package ldap
Summary: Nagios(R) plug-in for checking LDAP-server
Group: Monitoring
Requires: nagios-plugins-common = %version-%release

%description ldap
Nagios(R) plugi-in for checking LDAP server.


%package mysql
Summary: Nagios(R) plug-in for checking MySQL server
Group: Monitoring
Requires: nagios-plugins-common = %version-%release

%description mysql
Nagios(R) plugi-in for checking MySQL server.


%package pgsql
Summary: Nagios(R) plug-in for checking PostgreSQL server
Group: Monitoring
Requires: nagios-plugins-common = %version-%release

%description pgsql
Nagios(R) plugi-in for checking PostgreSQL server.


%package radius
Summary: Nagios(R) plug-in for checking RADIUS server
Group: Monitoring
Requires: nagios-plugins-common = %version-%release

%description radius
Nagios(R) plugi-in for checking RADIUS server.


%package perl
Summary: Nagios(R) plug-ins written in Perl language.
Group: Monitoring
Requires: nagios-plugins-common = %version-%release
Requires: sendmail-common glibc-utils

%description perl
Variaous Nagios(R) plugi-ins, writen in Perl language.

%package samba
Summary: Nagios(R) samba plug-in written in Perl language.
Group: Monitoring
Requires: nagios-plugins-common = %version-%release
Requires: samba-client

%description samba
Samba Nagios(R) plug-in, writen in Perl language.

%package snmp
Summary: Nagios(R) plug-ins for SNMP checks
Group: Monitoring
Requires: nagios-plugins-common = %version-%release
Requires: net-snmp-clients

%description snmp
Nagios(R) plug-ins for SNMP checks

%package extra
Summary: Nagios(R) plug-ins which depend on the presence of other software
Group: Monitoring
Requires: nagios-plugins-common = %version-%release
Requires: qstat lm_sensors

%description extra
This package contains plugins which use additional software libraries that
are not installed on all systems.

%prep
%setup -n %name-%version
%patch0 -p1 -b .p0
%patch1 -p2 -b .p1
#patch2 -p1 -b .p2
%patch3 -p1 -b .p3
%patch4 -p1 -b .p4

%patch101 -p1 -b .p101
%patch102 -p1 -b .p102
%patch103 -p1 -b .p103
%patch105 -p1 -b .p105
%patch106 -p1 -b .p106

# fix ps checking
%__subst "s|\[UCOMAND\]+|COMMAND|g" configure*

%build
# configure searches some root only commands
PATH=$PATH:/usr/sbin
%configure \
	--libexecdir=%nagios_plugdir \
	--with-cgiurl=/nagios/cgi-bin \
	--with-gnutls=/usr \
	--with-pgsql=/usr \
	--with-mysql=/usr \
	--with-openssl=/usr \
	--with-libiconv-prefix=/usr \
	--without-included-gettext \
	--with-libintl-prefix=/usr \
	--without-ipv6 \
	--with-ping-command='/bin/ping -n -U -w %%d -c %%d %%s' \
	--with-proc-loadavg='/proc/loadavg' \
	--with-proc-meminfo='/proc/meminfo' \
	--disable-rpath
%make_build

%install
chmod 0644 command.cfg
%makeinstall_std AM_INSTALL_PROGRAM_FLAGS=

# install Nagios commands deinitions 
mkdir -p %buildroot/%plugins_cmddir
install -m 644 %SOURCE10 %buildroot/%plugins_cmddir/
install -m 644 %SOURCE11 %buildroot/%plugins_cmddir/
install -m 644 %SOURCE12 %buildroot/%plugins_cmddir/
install -m 644 %SOURCE13 %buildroot/%plugins_cmddir/
install -m 644 %SOURCE14 %buildroot/%plugins_cmddir/
install -m 644 %SOURCE15 %buildroot/%plugins_cmddir/
install -m 644 %SOURCE16 %buildroot/%plugins_cmddir/
install -m 644 %SOURCE17 %buildroot/%plugins_cmddir/
install -m 644 %SOURCE18 %buildroot/%plugins_cmddir/
install -m 644 %SOURCE19 %buildroot/%plugins_cmddir/
install -m 644 %SOURCE20 %buildroot/%plugins_cmddir/


# install contrib add-ons
mkdir -p %buildroot%_docdir/%name-extra-%version/contrib
for i in `ls contrib/tarballs/*.gz`; do
 install -m 644 $i %buildroot%_docdir/%name-extra-%version/contrib
done

pushd contrib
 tar -cvzf %buildroot%_docdir/%name-extra-%version/contrib/contrib-misc.tar.gz \
  `find ./ -maxdepth 1 -type f -print0 | xargs -r0`
popd

install -m 644 contrib/README.TXT %buildroot%_docdir/%name-extra-%version/contrib
install -m 644 %SOURCE1 %buildroot%_docdir/%name-extra-%version/contrib

mkdir -p %buildroot%_docdir/%name-%version
install -pm644 ACKNOWLEDGEMENTS AUTHORS BUGS FAQ LEGAL NEWS README REQUIREMENTS SUPPORT THANKS command.cfg \
	%buildroot%_docdir/%name-%version/
install -pm644 %SOURCE2 %buildroot%_docdir/%name-%version/README.ALT.UTF-8

%find_lang %name

%files common -f %name.lang
%dir %nagios_plugdir
#common files
%nagios_plugdir/negate
%nagios_plugdir/utils.sh
%nagios_plugdir/utils.pm
%nagios_plugdir/urlize

%files
%plugins_cmddir/nagios-plugins.cfg
%nagios_plugdir/check_ping
%nagios_plugdir/check_nagios
%nagios_plugdir/check_load
%nagios_plugdir/check_procs
%dir %_docdir/%name-%version
%_docdir/%name-%version/*

%files local
%plugins_cmddir/nagios-plugins-local.cfg
%nagios_plugdir/check_apt
%nagios_plugdir/check_disk
%nagios_plugdir/check_ide_smart
%nagios_plugdir/check_dummy
%nagios_plugdir/check_file_age
%nagios_plugdir/check_log
%nagios_plugdir/check_mrtg
%nagios_plugdir/check_mrtgtraf
%nagios_plugdir/check_swap
%nagios_plugdir/check_users

%files network
%plugins_cmddir/nagios-plugins-network.cfg
%nagios_plugdir/check_by_ssh
%nagios_plugdir/check_clamd
%nagios_plugdir/check_cluster
%nagios_plugdir/check_dig
%nagios_plugdir/check_dns
%nagios_plugdir/check_dhcp
%nagios_plugdir/check_fping
%nagios_plugdir/check_ftp
%nagios_plugdir/check_http
%nagios_plugdir/check_icmp
%nagios_plugdir/check_imap
%nagios_plugdir/check_jabber
%nagios_plugdir/check_nntp
%nagios_plugdir/check_nntps
%nagios_plugdir/check_nt
%nagios_plugdir/check_ntp
%nagios_plugdir/check_ntp_peer
%nagios_plugdir/check_ntp_time
%nagios_plugdir/check_nwstat
%nagios_plugdir/check_overcr
%nagios_plugdir/check_pop
%nagios_plugdir/check_real
%nagios_plugdir/check_simap
%nagios_plugdir/check_smtp
%nagios_plugdir/check_ssmtp
%nagios_plugdir/check_spop
%nagios_plugdir/check_ssh
%nagios_plugdir/check_tcp
%nagios_plugdir/check_time
%nagios_plugdir/check_udp
%nagios_plugdir/check_ups

%files ldap
%plugins_cmddir/nagios-plugins-ldap.cfg
%nagios_plugdir/check_ldap
%nagios_plugdir/check_ldaps

%files mysql
%plugins_cmddir/nagios-plugins-mysql.cfg
%nagios_plugdir/check_mysql
%nagios_plugdir/check_mysql_query

%files pgsql
%plugins_cmddir/nagios-plugins-pgsql.cfg
%nagios_plugdir/check_pgsql

%files radius
%plugins_cmddir/nagios-plugins-radius.cfg
%nagios_plugdir/check_radius

%files samba
%plugins_cmddir/nagios-plugins-samba.cfg
%nagios_plugdir/check_disk_smb

%files perl
%plugins_cmddir/nagios-plugins-perl.cfg
%nagios_plugdir/check_ifoperstatus
%nagios_plugdir/check_ifstatus
%nagios_plugdir/check_ircd
%nagios_plugdir/check_mailq
%nagios_plugdir/check_rpc

%files snmp
%plugins_cmddir/nagios-plugins-snmp.cfg
%nagios_plugdir/check_breeze
%nagios_plugdir/check_hpjd
%nagios_plugdir/check_snmp
%nagios_plugdir/check_wave

%files extra
%plugins_cmddir/nagios-plugins-extra.cfg
%nagios_plugdir/check_flexlm
%nagios_plugdir/check_game
%nagios_plugdir/check_oracle
%nagios_plugdir/check_sensors
%dir %_docdir/%name-extra-%version
%_docdir/%name-extra-%version/*

%changelog
* Mon Jun 04 2012 Vitaly Lipatov <lav@altlinux.ru> 1.4.15-alt1
- new version 1.4.15 (with rpmrb script)
- cleanup spec, fix requires (ALT bug #26314)
- add some Fedora patches
- fix check_disk arg order (ALT bug #22598)

* Thu Jul 14 2011 Dmitry V. Levin <ldv@altlinux.org> 1.4.13-alt3
- Fixed interpackage dependencies.
- Updated build dependencies.

* Mon Dec 06 2010 Igor Vlasenko <viy@altlinux.ru> 1.4.13-alt2.1.1
- rebuild with new libmysqlclient by request of libmysqlclient maintainer

* Thu Sep 24 2009 ALT QA Team Robot <ldv@altlinux.org> 1.4.13-alt2.1
- Automated blind dumb rebuild with libldap-devel-2.4.16-alt4.4.

* Thu May 28 2009 Dmitry Lebkov <dlebkov@altlinux.ru> 1.4.13-alt2
- fix package against last libtool:
  + add 'libtoolize --install --force' before configure

* Mon Jan 12 2009 Dmitry Lebkov <dlebkov@altlinux.ru> 1.4.13-alt1
- 1.4.13

* Tue Aug 12 2008 Dmitry Lebkov <dlebkov@altlinux.ru> 1.4.12-alt1
- 1.4.12
- use GnuTLS instead of OpenSSL

* Thu May 01 2008 Dmitry Lebkov <dlebkov@altlinux.ru> 1.4.11-alt3
- move check_ntp from -perl to -network subpackage -- now this is a binary executable;
- add commands definitions for each subpackage -- see /etc/nagios/commands/

* Sat Apr 26 2008 Dmitry Lebkov <dlebkov@altlinux.ru> 1.4.11-alt2
- check_pgsql: fix compiling with postgresql-8.3

* Sat Mar 15 2008 Dmitry Lebkov <dlebkov@altlinux.ru> 1.4.11-alt1
- 1.4.11
- return check_radius

* Sun May 06 2007 Dmitry Lebkov <dlebkov@altlinux.ru> 1.4.8-alt1
- 1.4.8
- remove check_radius:
   API incompatibility between libradiusclinet and libradiusclient-ng

* Fri Dec 29 2006 ALT QA Team Robot <qa-robot@altlinux.org> 1.4.5-alt1.1
- Rebuilt due to libcrypto.so.4 -> libcrypto.so.6 soname change.

* Thu Nov 30 2006 Dmitry Lebkov <dlebkov@altlinux.ru> 1.4.5-alt1
- 1.4.5

* Sun Jul 02 2006 Dmitry Lebkov <dlebkov@altlinux.ru> 1.4.3-alt1
- 1.4.3
- README.ALT - add note about SUID plug-ins
- add nagios-plugins-snmp package (ALT bug id #9617)

* Sat Dec 24 2005 Dmitry Lebkov <dlebkov@altlinux.ru> 1.4.2-alt0
- 1.4.2

* Sat Dec 17 2005 Dmitry Lebkov <dlebkov@altlinux.ru> 1.4-alt2
- fix BuildRequires

* Mon May 30 2005 Dmitry Lebkov <dlebkov@altlinux.ru> 1.4-alt1
- 1.4 release
- subpackages reordering

* Sat Jan 08 2005 Dmitry Lebkov <dlebkov@altlinux.ru> 1.4-alt0.beta1.1
- new beta

* Sat Nov 13 2004 ALT QA Team Robot <qa-robot@altlinux.org> 1.3.1-alt5.1.1
- Rebuilt with openldap-2.2.18-alt3.

* Wed May 12 2004 ALT QA Team Robot <qa-robot@altlinux.org> 1.3.1-alt5.1
- Rebuilt with openssl-0.9.7d.

* Wed Mar 10 2004 Denis Smirnov <mithraen@altlinux.ru> 1.3.1-alt5
- move smb support to nagios-plugins-samba

* Wed Dec 17 2003 Dmitry Lebkov <dlebkov@altlinux.ru> 1.3.1-alt4
- nagios-plugins-radius: real rebuild with new libradiusclient

* Wed Oct 29 2003 Dmitry Lebkov <dlebkov@altlinux.ru> 1.3.1-alt3
- nagios-plugins-radius: rebuild with new libradiusclient

* Wed Oct 01 2003 Dmitry Lebkov <dlebkov@altlinux.ru> 1.3.1-alt2
- spec-file fixes

* Mon Sep 01 2003 Dmitry Lebkov <dlebkov@altlinux.ru> 1.3.1-alt1
- new version released -- 1.3.1
- nagios-plugins-perl requires changed from
  samba-client to samba3-client.
- nagios-plugins-extra: many contributed scripts placed
  into /usr/share/doc/nagios-plugins-extra/contrib

* Thu Jul 03 2003 Dmitry Lebkov <dlebkov@altlinux.ru> 1.3.0-alt5
- spec-file fixes

* Sat Apr 05 2003 Dmitry Lebkov <dlebkov@altlinux.ru> 1.3.0-alt4
- fix more checks in the configure.in file

* Thu Apr 03 2003 Dmitry Lebkov <dlebkov@altlinux.ru> 1.3.0-alt3
- fix checks in the configure.in file

* Tue Apr 01 2003 Dmitry Lebkov <dlebkov@altlinux.ru> 1.3.0-alt2
- fix 'BuildRequires' section

* Sun Mar 30 2003 Dmitry Lebkov <dlebkov@altlinux.ru> 1.3.0-alt1
- split nagios-plugins package into the small pices, according
  to plug-ins functionality and dependencies

* Mon Mar 17 2003 Dmitry Lebkov <dlebkov@altlinux.ru> 1.3.0-alt0.2
- new version released -- 1.3.0

* Wed Jan 22 2003 Dmitry Lebkov <dlebkov@altlinux.ru> 1.3.0-alt0.1beta2
- inital build for ALT Linux
