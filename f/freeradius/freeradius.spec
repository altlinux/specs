Summary: High-performance and highly configurable free RADIUS server
Name: freeradius
Version: 2.2.9
Release: alt2.1.1
License: GPLv2+ and LGPLv2+
Group: System/Servers
Url: http://www.freeradius.org/

# Cloned from git://git.freeradius.org/freeradius-server.git
Source0: %name-%version.tar
Source100: freeradius-radiusd-init
Source102: freeradius-logrotate
Source103: freeradius-pam-conf
Source104: freeradius-tmpfiles
Source105: freeradius-service

Patch1: %name-%version-%release.patch

BuildRequires: gcc-c++ libmysqlclient-devel libcom_err-devel libgdbm-devel libldap-devel libltdl-devel libpam-devel libreadline-devel libstdc++-devel-static libunixODBC-devel mailx net-snmp-utils perl-DBI perl-devel postgresql-devel python-devel slocate libssl-devel perl-DBM

# Server needs dicts and /etc/raddb to work:
Requires: %name-common

%description
The FreeRADIUS Server Project is a high performance and highly configurable
GPL'd free RADIUS server. The server is similar in some respects to
Livingston's 2.0 server.  While FreeRADIUS started as a variant of the
Cistron RADIUS server, they don't share a lot in common any more. It now has
many more features than Cistron or Livingston, and is much more configurable.

FreeRADIUS is an Internet authentication daemon, which implements the RADIUS
protocol, as defined in RFC 2865 (and others). It allows Network Access
Servers (NAS boxes) to perform authentication for dial-up users. There are
also RADIUS clients available for Web servers, firewalls, Unix logins, and
more.  Using RADIUS allows authentication and authorization for a network to
be centralized, and minimizes the amount of re-configuration which has to be
done when adding or deleting new users.

%package common
Group: System/Servers
Summary: FreeRADIUS common data
# For now this subpackage contains only dicts (arch-independent):
BuildArch: noarch
# Alias for convience:
Provides: %name-dictionary = %version-%release

%description common
The FreeRADIUS common data

%package libs
Group: System/Servers
Summary: FreeRADIUS shared libraries

%description libs
The FreeRADIUS shared library

%package utils
Group: System/Servers
Summary: FreeRADIUS utilities
Requires: %name-libs = %version-%release
# Radius client(s) need dicts to work:
Requires: %name-dictionary = %version-%release

%description utils
The FreeRADIUS server has a number of features found in other servers,
and additional features not found in any other server. Rather than
doing a feature by feature comparison, we will simply list the features
of the server, and let you decide if they satisfy your needs.

Support for RFC and VSA Attributes Additional server configuration
attributes Selecting a particular configuration Authentication methods

%package devel
Group: Development/C
Summary: FreeRADIUS Development Files
Requires: %name-libs = %version-%release

%description devel
These are the static libraries for the FreeRADIUS package.

%package ldap
Summary: LDAP support for freeradius
Group: System/Servers
Requires: %name-libs = %version-%release

%description ldap
This plugin provides the LDAP support for the FreeRADIUS server project.

%package krb5
Summary: Kerberos 5 support for freeradius
Group: System/Servers
Requires: %name-libs = %version-%release

%description krb5
This plugin provides the Kerberos 5 support for the FreeRADIUS server project.

%package perl
Summary: Perl support for freeradius
Group: System/Servers
Requires: %name-libs = %version-%release


%description perl
This plugin provides the Perl support for the FreeRADIUS server project.

%package python
Summary: Python support for freeradius
Group: System/Servers
Requires: %name-libs = %version-%release

%description python
This plugin provides the Python support for the FreeRADIUS server project.

%package mysql
Summary: MySQL support for freeradius
Group: System/Servers
Requires: %name-libs = %version-%release

%description mysql
This plugin provides the MySQL support for the FreeRADIUS server project.

%package postgresql
Summary: postgresql support for freeradius
Group: System/Servers
Requires: %name-libs = %version-%release

%description postgresql
This plugin provides the postgresql support for the FreeRADIUS server project.

%package unixODBC
Summary: unixODBC support for freeradius
Group: System/Servers
Requires: %name-libs = %version-%release

%description unixODBC
This plugin provides the unixODBC support for the FreeRADIUS server project.

%prep
%setup -q
%patch1 -p1

%build
%configure \
        --with-system-libtool \
        --with-system-libltdl \
        --localstatedir=/var \
        --libdir=%_libdir/freeradius \
        --disable-ltdl-install \
        --disable-static \
        --with-gnu-ld \
        --with-threads \
        --with-thread-pool \
        --with-docdir=%_docdir/freeradius-%version \
        --with-rlm-sql_postgresql-include-dir=/usr/include/pgsql \
        --with-rlm-sql-postgresql-lib-dir=%_libdir \
        --with-rlm-sql_mysql-include-dir=/usr/include/mysql \
        --with-mysql-lib-dir=%_libdir/mysql \
        --with-unixodbc-lib-dir=%_libdir \
        --with-rlm-dbm-lib-dir=%_libdir \
        --with-rlm-krb5-include-dir=/usr/include/krb5 \
        --without-rlm_eap_ikev2 \
        --without-rlm_sql_iodbc \
        --without-rlm_sql_firebird \
        --without-rlm_sql_db2 \
        --without-rlm_sql_oracle

%make_build

%install
make install R=%buildroot

# modify default configuration
RADDB=%buildroot%_sysconfdir/raddb
sed -i 's/^#user =.*$/user = radiusd/'   $RADDB/radiusd.conf
sed -i 's/^#group =.*$/group = radiusd/' $RADDB/radiusd.conf
# logs
mkdir -p %buildroot%_logdir/radius/radacct
touch %buildroot%_logdir/radius/{radutmp,radius.log}

mkdir -p %buildroot%_runtimedir/radiusd
mkdir -p %buildroot%_sysconfdir/{logrotate.d,pam.d,rc.d/init.d}
mkdir -p %buildroot%_tmpfilesdir
mkdir -p %buildroot%_unitdir
mkdir -p %buildroot%_localstatedir/radiusd
install -m 755 %SOURCE100 %buildroot%_initdir/radiusd
install -m 644 %SOURCE102 %buildroot%_sysconfdir/logrotate.d/radiusd
install -m 644 %SOURCE103 %buildroot%_sysconfdir/pam.d/radiusd
install -m 644 %SOURCE104 %buildroot%_tmpfilesdir/radiusd.conf
install -m 644 %SOURCE105 %buildroot%_unitdir/radiusd.service

# remove unneeded stuff
rm %buildroot%_sbindir/rc.radiusd
rm %buildroot%_libdir/freeradius/*.a
rm %buildroot%_libdir/freeradius/*.la
rm -r %buildroot%_sysconfdir/raddb/sql/mssql
rm -r %buildroot%_sysconfdir/raddb/sql/oracle

# remove unsupported config files
rm %buildroot/%_sysconfdir/raddb/experimental.conf

%pre common
/usr/sbin/groupadd -r -f radiusd
/usr/sbin/useradd -r -n -g radiusd -d /dev/null -s /dev/null -c RADIUS radiusd >/dev/null 2>&1 ||:

%post
%post_service radiusd
if [ $1 = 1 ]; then
    if [ ! -e /etc/raddb/certs/server.pem ]; then
        su -s "/bin/sh" -c "/etc/raddb/certs/bootstrap" radiusd > /dev/null 2>&1 || :
    fi
fi

%preun
%preun_service radiusd

%files
%doc %_docdir/freeradius-%version/
%config(noreplace) %_sysconfdir/pam.d/radiusd
%config(noreplace) %_sysconfdir/logrotate.d/radiusd
%config(noreplace) %_initdir/radiusd
%_unitdir/radiusd.service
%_tmpfilesdir/radiusd.conf
%dir %attr(775,root,radiusd) %_localstatedir/radiusd
# configs
%defattr(-,root,radiusd)
%config(noreplace) %_sysconfdir/raddb/acct_users
%config(noreplace) %_sysconfdir/raddb/attrs
%config(noreplace) %_sysconfdir/raddb/attrs.access_challenge
%config(noreplace) %_sysconfdir/raddb/attrs.access_reject
%config(noreplace) %_sysconfdir/raddb/attrs.accounting_response
%config(noreplace) %_sysconfdir/raddb/attrs.pre-proxy
%attr(640,root,radiusd) %config(noreplace) %_sysconfdir/raddb/clients.conf
%config(noreplace) %_sysconfdir/raddb/hints
%config(noreplace) %_sysconfdir/raddb/huntgroups
%attr(640,root,radiusd) %config(noreplace) %_sysconfdir/raddb/sqlippool.conf
%attr(640,root,radiusd) %config(noreplace) %_sysconfdir/raddb/preproxy_users
%attr(640,root,radiusd) %config(noreplace) %_sysconfdir/raddb/proxy.conf
%attr(640,root,radiusd) %config(noreplace) %_sysconfdir/raddb/radiusd.conf
%attr(640,root,radiusd) %config(noreplace) %_sysconfdir/raddb/sql.conf
%dir %attr(750,root,radiusd) %_sysconfdir/raddb/sql
%attr(640,root,radiusd) %config(noreplace) %_sysconfdir/raddb/users
%dir %attr(770,root,radiusd) %_sysconfdir/raddb/certs
%_sysconfdir/raddb/certs/Makefile
%_sysconfdir/raddb/certs/README
%_sysconfdir/raddb/certs/xpextensions
%attr(640,root,radiusd) %config(noreplace) %_sysconfdir/raddb/certs/*.cnf
%attr(750,root,radiusd) %_sysconfdir/raddb/certs/bootstrap
%dir %attr(750,root,radiusd) %_sysconfdir/raddb/sites-available
%attr(640,root,radiusd) %config(noreplace) %_sysconfdir/raddb/sites-available/*
%dir %attr(750,root,radiusd) %_sysconfdir/raddb/sites-enabled
%attr(640,root,radiusd) %config(noreplace) %_sysconfdir/raddb/sites-enabled/*
%attr(640,root,radiusd) %config(noreplace) %_sysconfdir/raddb/eap.conf
%attr(640,root,radiusd) %_sysconfdir/raddb/example.pl
%attr(640,root,radiusd) %config(noreplace) %_sysconfdir/raddb/policy.conf
%_sysconfdir/raddb/policy.txt
%attr(640,root,radiusd) %config(noreplace) %_sysconfdir/raddb/templates.conf
%dir %attr(750,root,radiusd) %_sysconfdir/raddb/modules
%attr(640,root,radiusd) %config(noreplace) %_sysconfdir/raddb/modules/acct_unique
%attr(640,root,radiusd) %config(noreplace) %_sysconfdir/raddb/modules/always
%attr(640,root,radiusd) %config(noreplace) %_sysconfdir/raddb/modules/attr_filter
%attr(640,root,radiusd) %config(noreplace) %_sysconfdir/raddb/modules/attr_rewrite
%attr(640,root,radiusd) %config(noreplace) %_sysconfdir/raddb/modules/cache
%attr(640,root,radiusd) %config(noreplace) %_sysconfdir/raddb/modules/chap
%attr(640,root,radiusd) %config(noreplace) %_sysconfdir/raddb/modules/checkval
%attr(640,root,radiusd) %config(noreplace) %_sysconfdir/raddb/modules/counter
%attr(640,root,radiusd) %config(noreplace) %_sysconfdir/raddb/modules/cui
%attr(640,root,radiusd) %config(noreplace) %_sysconfdir/raddb/modules/detail
%attr(640,root,radiusd) %config(noreplace) %_sysconfdir/raddb/modules/detail.example.com
%attr(640,root,radiusd) %config(noreplace) %_sysconfdir/raddb/modules/detail.log
%attr(640,root,radiusd) %config(noreplace) %_sysconfdir/raddb/modules/digest
%attr(640,root,radiusd) %config(noreplace) %_sysconfdir/raddb/modules/dynamic_clients
%attr(640,root,radiusd) %config(noreplace) %_sysconfdir/raddb/modules/echo
%attr(640,root,radiusd) %config(noreplace) %_sysconfdir/raddb/modules/etc_group
%attr(640,root,radiusd) %config(noreplace) %_sysconfdir/raddb/modules/exec
%attr(640,root,radiusd) %config(noreplace) %_sysconfdir/raddb/modules/expiration
%attr(640,root,radiusd) %config(noreplace) %_sysconfdir/raddb/modules/expr
%attr(640,root,radiusd) %config(noreplace) %_sysconfdir/raddb/modules/files
%attr(640,root,radiusd) %config(noreplace) %_sysconfdir/raddb/modules/inner-eap
%attr(640,root,radiusd) %config(noreplace) %_sysconfdir/raddb/modules/ippool
%attr(640,root,radiusd) %config(noreplace) %_sysconfdir/raddb/modules/logintime
%attr(640,root,radiusd) %config(noreplace) %_sysconfdir/raddb/modules/linelog
%attr(640,root,radiusd) %config(noreplace) %_sysconfdir/raddb/modules/mac2ip
%attr(640,root,radiusd) %config(noreplace) %_sysconfdir/raddb/modules/mac2vlan
%attr(640,root,radiusd) %config(noreplace) %_sysconfdir/raddb/modules/mschap
%attr(640,root,radiusd) %config(noreplace) %_sysconfdir/raddb/modules/ntlm_auth
%attr(640,root,radiusd) %config(noreplace) %_sysconfdir/raddb/modules/opendirectory
%attr(640,root,radiusd) %config(noreplace) %_sysconfdir/raddb/modules/otp
%attr(640,root,radiusd) %config(noreplace) %_sysconfdir/raddb/modules/pam
%attr(640,root,radiusd) %config(noreplace) %_sysconfdir/raddb/modules/pap
%attr(640,root,radiusd) %config(noreplace) %_sysconfdir/raddb/modules/perl
%attr(640,root,radiusd) %config(noreplace) %_sysconfdir/raddb/modules/passwd
%attr(640,root,radiusd) %config(noreplace) %_sysconfdir/raddb/modules/policy
%attr(640,root,radiusd) %config(noreplace) %_sysconfdir/raddb/modules/preprocess
%attr(640,root,radiusd) %config(noreplace) %_sysconfdir/raddb/modules/radrelay
%attr(640,root,radiusd) %config(noreplace) %_sysconfdir/raddb/modules/radutmp
%attr(640,root,radiusd) %config(noreplace) %_sysconfdir/raddb/modules/realm
%attr(640,root,radiusd) %config(noreplace) %_sysconfdir/raddb/modules/redis
%attr(640,root,radiusd) %config(noreplace) %_sysconfdir/raddb/modules/rediswho
%attr(640,root,radiusd) %config(noreplace) %_sysconfdir/raddb/modules/replicate
%attr(640,root,radiusd) %config(noreplace) %_sysconfdir/raddb/modules/smbpasswd
%attr(640,root,radiusd) %config(noreplace) %_sysconfdir/raddb/modules/smsotp
%attr(640,root,radiusd) %config(noreplace) %_sysconfdir/raddb/modules/soh
%attr(640,root,radiusd) %config(noreplace) %_sysconfdir/raddb/modules/sql_log
%attr(640,root,radiusd) %config(noreplace) %_sysconfdir/raddb/modules/sqlcounter_expire_on_login
%attr(640,root,radiusd) %config(noreplace) %_sysconfdir/raddb/modules/sradutmp
%attr(640,root,radiusd) %config(noreplace) %_sysconfdir/raddb/modules/unix
%attr(640,root,radiusd) %config(noreplace) %_sysconfdir/raddb/modules/wimax
%dir %attr(770,root,radiusd) %_runtimedir/radiusd/

%defattr(-,root,root)
# binaries
%_sbindir/checkrad
%_sbindir/raddebug
%_sbindir/radiusd
%_sbindir/radwatch
%_sbindir/radmin
# man-pages
%_man1dir/*
%_man5dir/*
%_man8dir/*
# logs
%dir %attr(1770,root,radiusd) %_logdir/radius/
%dir %attr(1770,root,radiusd) %_logdir/radius/radacct/
%config(noreplace) %attr(664,root,radiusd) %_logdir/radius/radutmp
%config(noreplace) %attr(660,radiusd,radiusd) %_logdir/radius/radius.log
# RADIUS Loadable Modules
%dir %_libdir/freeradius
%_libdir/freeradius/rlm_acct_unique.so
%_libdir/freeradius/rlm_acct_unique-%version.so
%_libdir/freeradius/rlm_acctlog.so
%_libdir/freeradius/rlm_acctlog-%version.so
%_libdir/freeradius/rlm_always.so
%_libdir/freeradius/rlm_always-%version.so
%_libdir/freeradius/rlm_attr_filter.so
%_libdir/freeradius/rlm_attr_filter-%version.so
%_libdir/freeradius/rlm_attr_rewrite.so
%_libdir/freeradius/rlm_attr_rewrite-%version.so
%_libdir/freeradius/rlm_cache.so
%_libdir/freeradius/rlm_cache-%version.so
%_libdir/freeradius/rlm_chap.so
%_libdir/freeradius/rlm_chap-%version.so
%_libdir/freeradius/rlm_checkval.so
%_libdir/freeradius/rlm_checkval-%version.so
%_libdir/freeradius/rlm_copy_packet.so
%_libdir/freeradius/rlm_copy_packet-%version.so
%_libdir/freeradius/rlm_counter.so
%_libdir/freeradius/rlm_counter-%version.so
%_libdir/freeradius/rlm_dbm.so
%_libdir/freeradius/rlm_dbm-%version.so
%_libdir/freeradius/rlm_detail.so
%_libdir/freeradius/rlm_detail-%version.so
%_libdir/freeradius/rlm_digest.so
%_libdir/freeradius/rlm_digest-%version.so
%_libdir/freeradius/rlm_dynamic_clients.so
%_libdir/freeradius/rlm_dynamic_clients-%version.so
%_libdir/freeradius/rlm_eap.so
%_libdir/freeradius/rlm_eap-%version.so
%_libdir/freeradius/rlm_eap_gtc.so
%_libdir/freeradius/rlm_eap_gtc-%version.so
%_libdir/freeradius/rlm_eap_leap.so
%_libdir/freeradius/rlm_eap_leap-%version.so
%_libdir/freeradius/rlm_eap_md5.so
%_libdir/freeradius/rlm_eap_md5-%version.so
%_libdir/freeradius/rlm_eap_mschapv2.so
%_libdir/freeradius/rlm_eap_mschapv2-%version.so
%_libdir/freeradius/rlm_eap_peap.so
%_libdir/freeradius/rlm_eap_peap-%version.so
%_libdir/freeradius/rlm_eap_sim.so
%_libdir/freeradius/rlm_eap_sim-%version.so
%_libdir/freeradius/rlm_eap_tls.so
%_libdir/freeradius/rlm_eap_tls-%version.so
%_libdir/freeradius/rlm_eap_ttls.so
%_libdir/freeradius/rlm_eap_ttls-%version.so
%_libdir/freeradius/rlm_exec.so
%_libdir/freeradius/rlm_exec-%version.so
%_libdir/freeradius/rlm_expiration.so
%_libdir/freeradius/rlm_expiration-%version.so
%_libdir/freeradius/rlm_expr.so
%_libdir/freeradius/rlm_expr-%version.so
%_libdir/freeradius/rlm_fastusers.so
%_libdir/freeradius/rlm_fastusers-%version.so
%_libdir/freeradius/rlm_files.so
%_libdir/freeradius/rlm_files-%version.so
%_libdir/freeradius/rlm_ippool.so
%_libdir/freeradius/rlm_ippool-%version.so
%_libdir/freeradius/rlm_linelog.so
%_libdir/freeradius/rlm_linelog-%version.so
%_libdir/freeradius/rlm_logintime.so
%_libdir/freeradius/rlm_logintime-%version.so
%_libdir/freeradius/rlm_mschap.so
%_libdir/freeradius/rlm_mschap-%version.so
%_libdir/freeradius/rlm_otp.so
%_libdir/freeradius/rlm_otp-%version.so
%_libdir/freeradius/rlm_pam.so
%_libdir/freeradius/rlm_pam-%version.so
%_libdir/freeradius/rlm_pap.so
%_libdir/freeradius/rlm_pap-%version.so
%_libdir/freeradius/rlm_passwd.so
%_libdir/freeradius/rlm_passwd-%version.so
%_libdir/freeradius/rlm_policy.so
%_libdir/freeradius/rlm_policy-%version.so
%_libdir/freeradius/rlm_preprocess.so
%_libdir/freeradius/rlm_preprocess-%version.so
%_libdir/freeradius/rlm_radutmp.so
%_libdir/freeradius/rlm_radutmp-%version.so
%_libdir/freeradius/rlm_realm.so
%_libdir/freeradius/rlm_realm-%version.so
%_libdir/freeradius/rlm_replicate.so
%_libdir/freeradius/rlm_replicate-%version.so
%_libdir/freeradius/rlm_soh.so
%_libdir/freeradius/rlm_soh-%version.so
%_libdir/freeradius/rlm_sql.so
%_libdir/freeradius/rlm_sql-%version.so
%_libdir/freeradius/rlm_sql_log.so
%_libdir/freeradius/rlm_sql_log-%version.so
%_libdir/freeradius/rlm_sqlcounter.so
%_libdir/freeradius/rlm_sqlcounter-%version.so
%_libdir/freeradius/rlm_sqlippool.so
%_libdir/freeradius/rlm_sqlippool-%version.so
%_libdir/freeradius/rlm_unix.so
%_libdir/freeradius/rlm_unix-%version.so
%_libdir/freeradius/rlm_wimax.so
%_libdir/freeradius/rlm_wimax-%version.so

%files common
%dir %attr(755,root,radiusd) %_sysconfdir/raddb
%attr(644,root,root) %config(noreplace) %_sysconfdir/raddb/dictionary
# dictionaries
%_datadir/freeradius

%files utils
%_bindir/*

%files libs
# RADIU shared libs
%_libdir/freeradius/lib*.so*

%files devel
%_includedir/freeradius

%files krb5
%_libdir/freeradius/rlm_krb5.so
%_libdir/freeradius/rlm_krb5-%version.so
%attr(640,root,radiusd) %config(noreplace) %_sysconfdir/raddb/modules/krb5

%files perl
%_libdir/freeradius/rlm_perl.so
%_libdir/freeradius/rlm_perl-%version.so

%files python
%_libdir/freeradius/rlm_python.so
%_libdir/freeradius/rlm_python-%version.so

%files mysql
%attr(640,root,radiusd) %config(noreplace) %_sysconfdir/raddb/modules/dhcp_sqlippool
%dir %attr(750,root,radiusd) %_sysconfdir/raddb/sql/mysql
%attr(640,root,radiusd) %config(noreplace) %_sysconfdir/raddb/sql/mysql/*
%dir %attr(750,root,radiusd) %_sysconfdir/raddb/sql/ndb
%attr(640,root,radiusd) %config(noreplace) %_sysconfdir/raddb/sql/ndb/*
%_libdir/freeradius/rlm_sql_mysql.so
%_libdir/freeradius/rlm_sql_mysql-%version.so

%files postgresql
%dir %attr(750,root,radiusd) %_sysconfdir/raddb/sql/postgresql
%attr(640,root,radiusd) %config(noreplace) %_sysconfdir/raddb/sql/postgresql/*
%_libdir/freeradius/rlm_sql_postgresql.so
%_libdir/freeradius/rlm_sql_postgresql-%version.so

%files ldap
%attr(640,root,radiusd) %config(noreplace) %_sysconfdir/raddb/ldap.attrmap
%_libdir/freeradius/rlm_ldap.so
%_libdir/freeradius/rlm_ldap-%version.so
%attr(640,root,radiusd) %config(noreplace) %_sysconfdir/raddb/modules/ldap

%files unixODBC
%_libdir/freeradius/rlm_sql_unixodbc.so
%_libdir/freeradius/rlm_sql_unixodbc-%version.so

%changelog
* Fri Dec 15 2017 Igor Vlasenko <viy@altlinux.ru> 2.2.9-alt2.1.1
- rebuild with new perl 5.26.1

* Fri Feb 03 2017 Igor Vlasenko <viy@altlinux.ru> 2.2.9-alt2.1
- rebuild with new perl 5.24.1

* Tue Jan 26 2016 Terechkov Evgenii <evg@altlinux.org> 2.2.9-alt2
- Move /etc/raddb to common subpackage (radius clients needs /etc/raddb/dictionary)
- Create user/group in common subpackage
- Allow everyone run radius clients with packaged dicts

* Tue Jan  5 2016 Terechkov Evgenii <evg@altlinux.org> 2.2.9-alt1
- 2.2.9

* Tue Jan  5 2016 Terechkov Evgenii <evg@altlinux.org> 2.2.0-alt5
- Change mode of /var/log/{radius,radius/radacct} to 1770 according to ALT Secure Packaging Policy
- Change owner of /var/log/radius/radius.log
- Do not rotate/replace radutmp (ALT#28653, RH#904578)
- Move tmpfiles manifest in right place (Thanks, repocop!)
- Send SIGHUP to radiusd after radius.log rotation (ALT#31044)
- Separate %_datadir/freeradius to common noarch subpackage (ALT#28477)
- Systemd unit file added (Thanks, repocop!)

* Wed Nov 25 2015 Igor Vlasenko <viy@altlinux.ru> 2.2.0-alt4.1.1
- rebuild with new perl 5.22.0

* Tue Dec 09 2014 Igor Vlasenko <viy@altlinux.ru> 2.2.0-alt4.1
- rebuild with new perl 5.20.1

* Thu Aug 29 2013 Vladimir Lettiev <crux@altlinux.ru> 2.2.0-alt4
- built for perl 5.18

* Fri Nov 09 2012 Vladimir Lettiev <crux@altlinux.ru> 2.2.0-alt3
- preserve files /etc/raddb/sites-available/* (Closes: #29750)

* Tue Nov 06 2012 Vladimir Lettiev <crux@altlinux.ru> 2.2.0-alt2
- fixed handling of relative path in $INCLUDE in users files (Closes: #27927)
- systemd compatibility (Closes: #27928)
- moved dhcp_sqlippool config to mysql subpackage

* Fri Sep 14 2012 Vladimir Lettiev <crux@altlinux.ru> 2.2.0-alt1
- 2.1.12 -> 2.2.0
- Security fixes: CVE-2012-3547
- Built with fresh libtool

* Tue Sep 04 2012 Vladimir Lettiev <crux@altlinux.ru> 2.1.12-alt2
- rebuilt for perl-5.16

* Wed Jul 18 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.1.12-alt1.2
- Fixed build

* Mon Nov 07 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 2.1.12-alt1.1.1
- Rebuild with Python-2.7

* Sat Oct 22 2011 Alexey Tourbin <at@altlinux.ru> 2.1.12-alt1.1
- Rebuilt for perl-5.14

* Thu Oct 20 2011 Vladimir Lettiev <crux@altlinux.ru> 2.1.12-alt1
- 2.1.12

* Fri Sep 30 2011 Vladimir Lettiev <crux@altlinux.ru> 2.1.10-alt4
- Fixed permissions for /etc/raddb/modules, /etc/raddb/sql/mysql,
  /etc/raddb/sql/postgresql dirs (640 -> 750)
- Dropped freeradius_rlm_perl_build_alt.patch

* Thu Apr 14 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 2.1.10-alt3
- repair build

* Sun Nov 28 2010 Vladimir Lettiev <crux@altlinux.ru> 2.1.10-alt2
- %_sysconfdir/raddb/certs/bootstrap started on initial install
  to create test cert %_sysconfdir/raddb/certs/server.pem

* Wed Nov 24 2010 Vladimir Lettiev <crux@altlinux.ru> 2.1.10-alt1
- New version 2.1.10
- Spec cleanup
- Fixed permissions
- Dropped freeradius-radiusd-conf.patch

* Fri Nov 05 2010 Vladimir Lettiev <crux@altlinux.ru> 2.1.3-alt3
- rebuilt with perl 5.12

* Thu Nov 12 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.1.3-alt2.3.1.1
- Rebuilt with python 2.6

* Thu Sep 24 2009 ALT QA Team Robot <ldv@altlinux.org> 2.1.3-alt2.3.1
- Automated blind dumb rebuild with libldap-devel-2.4.16-alt4.4.

* Tue May 12 2009 Denis Kuznetsov <dek@altlinux.ru> 2.1.3-alt2.3
- fixed build with new toolchain

* Mon Apr 27 2009 Denis Kuznetsov <dek@altlinux.ru> 2.1.3-alt2.2
- added %%set_libtool_version 1.5 build option

* Fri Mar 06 2009 Denis Kuznetsov <dek@altlinux.ru> 2.1.3-alt2.1
- Fixed build with as-need.

* Tue Feb 24 2009 Denis Kuznetsov <dek@altlinux.ru> 2.1.3-alt2
- Fixed requires for rlm_perl module

* Fri Feb 20 2009 Denis Kuznetsov <dek@altlinux.ru> 2.1.3-alt1
- Rebuild for ALTLinux

* Thu Dec  4 2008 John Dennis <jdennis@redhat.com> - 2.1.3-1
- upgrade to latest upstream release, upstream summary follows:
  The focus of this release is stability.
  Feature Improvements:
    * Allow running with "user=radiusd" and binding to secure sockets.
    * Start sending Status-Server "are you alive" messages earlier, which
      helps with proxying multiple realms to a home server.
    * Removed thread pool code from rlm_perl.  It's not necessary.
    * Added example Perl configuration to raddb/modules/perl
    * Force OpenSSL to support certificates with SHA256. This seems to be
      necessary for WiMAX certs.
  Bug fixes:
    * Fix Debian patch to allow it to build.
    * Fix potential NULL dereference in debugging mode on certain
      platforms for TTLS and PEAP inner tunnels.
    * Fix uninitialized memory in handling of vendor definitions
    * Fix parsing of quoted (but non-string) attributes in the "users" file.
    * Initialize uknown NAS IP to 255.255.255.255, rather than 0.0.0.0
    * use SUN_LEN in control socket, to avoid truncation on some platforms.
    * Correct internal handling of "debug condition" to prevent it from
      being over-written.
    * Check return code of regcomp in "unlang", so that invalid regular
      expressions are caught rather than mishandled.
    * Make rlm_sql use <ltdl.h>.  Addresses bug #610.
    * Document list "type = status" better.  Closes bug #580.
    * Set "default days" for certificates, because OpenSSL won't do it.
      This closes bug #615.
    * Reference correct list in example raddb/modules/ldap. Closes #596.
    * Increase default schema size for Acct-Session-Id to 64. Closes #540.
    * Fix use of temporary files in dialup-admin.  Closes #605 and
      addresses CVE-2008-4474.
    * Addressed a number of minor issues found by Coverity.
    * Added DHCP option 150 to the dictionary.  Closes #618.

* Wed Dec  3 2008 John Dennis <jdennis@redhat.com> - 2.1.1-8
- add --with-system-libtool to configure as a workaround for
undefined reference to lt__PROGRAM__LTX_preloaded_symbols

* Mon Dec  1 2008 John Dennis <jdennis@redhat.com> - 2.1.1-7
- add obsoletes tag for dialupadmin subpackages which were removed

* Mon Dec  1 2008 John Dennis <jdennis@redhat.com> - 2.1.1-5
- add readline-devel BuildRequires

* Fri Nov 21 2008 John Dennis <jdennis@redhat.com> - 2.1.1-3
- make spec file buildable on RHEL5.2 by making perl-devel a fedora only dependency.
- remove diaupadmin packages, it's not well supported and there are problems with it.

* Fri Sep 26 2008 John Dennis <jdennis@redhat.com> - 2.1.1-1
- Resolves: bug #464119 bootstrap code could not create initial certs in %_sysconfdir/raddb/certs because
  permissions were 750, radiusd running as euid radiusd could not write there, permissions now 770

* Thu Sep 25 2008 John Dennis <jdennis@redhat.com> - 2.1.1-1
- upgrade to new upstream 2.1.1 release

* Wed Jul 30 2008 John Dennis <jdennis@redhat.com> - 2.0.5-2
- Resolves: bug #453761: FreeRADIUS %%post should not include chown -R
  specify file attributes for %_sysconfdir/raddb/ldap.attrmap
  fix consistent use of tabs/spaces (rpmlint warning)

* Mon Jun  9 2008 John Dennis <jdennis@redhat.com> - 2.0.5-1
- upgrade to latest upstream, see Changelog for details,
  upstream now has more complete fix for bug #447545, local patch removed

* Wed May 28 2008 John Dennis <jdennis@redhat.com> - 2.0.4-1
- upgrade to latest upstream, see Changelog for details
- resolves: bug #447545: freeradius missing %_sysconfdir/raddb/sites-available/inner-tunnel

* Fri May 16 2008  <jdennis@redhat.com> - 2.0.3-3
- # Temporary fix for bug #446864, turn off optimization

* Fri Apr 18 2008 John Dennis <jdennis@redhat.com> - 2.0.3-2
- remove support for radrelay, it's different now
- turn off default inclusion of SQL config files in radiusd.conf since SQL
  is an optional RPM install
- remove mssql config files

* Thu Apr 17 2008 John Dennis <jdennis@redhat.com> - 2.0.3-1
- Upgrade to current upstream 2.0.3 release
- Many thanks to Enrico Scholz for his spec file suggestions incorporated here
- Resolve: bug #438665: Contains files owned by buildsystem
- Add dialupadmin-mysql, dialupadmin-postgresql, dialupadmin-ldap subpackages
  to further partition external dependencies.
- Clean up some unnecessary requires dependencies
- Add versioned requires between subpackages

* Tue Mar 18 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 2.0.2-2
- add Requires for versioned perl (libperl.so)

* Thu Feb 28 2008  <jdennis@redhat.com> - 2.0.2-1
- upgrade to new 2.0 release
- split into subpackages for more fine grained installation

* Tue Feb 19 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 1.1.7-4.4.ipa
- Autorebuild for GCC 4.3

* Thu Dec 06 2007 Release Engineering <rel-eng at fedoraproject dot org> - 1.1.7-3.4.ipa
- Rebuild for deps

* Sat Nov 10 2007  <jdennis@redhat.com> - 1.1.7-3.3.ipa
- add support in rlm_ldap for reading clients from ldap
- fix TLS parameter controling if a cert which fails to validate
  will be accepted (i.e. self-signed),
  rlm_ldap config parameter=tls_require_cert
  ldap LDAP_OPT_X_TLS_REQUIRE_CERT parameter was being passed to
  ldap_set_option() when it should have been ldap_int_tls_config()

* Sat Nov 3 2007  <jdennis@redhat.com> - 1.1.7-3.2.ipa
- add support in rlm_ldap for SASL/GSSAPI binds to the LDAP server

* Mon Sep 17 2007 Thomas Woerner <twoerner@redhat.com> 1.1.7-3.1
- made init script fully lsb conform

* Mon Sep 17 2007 Thomas Woerner <twoerner@redhat.com> 1.1.7-3
- fixed initscript problem (rhbz#292521)

* Tue Aug 28 2007 Thomas Woerner <twoerner@redhat.com> 1.1.7-2
- fixed initscript for LSB (rhbz#243671, rhbz#243928)
- fixed license tag

* Tue Aug  7 2007 Thomas Woerner <twoerner@redhat.com> 1.1.7-1
- new versin 1.1.7
- install snmp MIB files
- dropped LDAP_DEPRECATED flag, it is upstream
- marked config files for sub packages as config (rhbz#240400)
- moved db files to /var/lib/raddb (rhbz#199082)

* Fri Jun 15 2007 Thomas Woerner <twoerner@redhat.com> 1.1.6-2
- radiusd expects %_sysconfdir/raddb to not be world readable or writable
  %_sysconfdir/raddb now belongs to radiusd, post script sets permissions

* Fri Jun 15 2007 Thomas Woerner <twoerner@redhat.com> 1.1.6-1
- new version 1.1.6

* Fri Mar  9 2007 Thomas Woerner <twoerner@redhat.com> 1.1.5-1
- new version 1.1.5
  - no %_sysconfdir/raddb/otppasswd.sample anymore
  - build is pie by default, dropped pie patch
- fixed build requirement for perl (perl-devel)

* Fri Feb 23 2007 Karsten Hopp <karsten@redhat.com> 1.1.3-3
- remove trailing dot from summary
- fix buildroot
- fix post/postun/preun requirements
- use rpm macros

* Fri Dec  8 2006 Thomas Woerner <twoerner@redhat.com> 1.1.3-2.1
- rebuild for new postgresql library version

* Thu Nov 30 2006 Thomas Woerner <twoerner@redhat.com> 1.1.3-2
- fixed ldap code to not use internals, added LDAP_DEPRECATED compile time flag
  (#210912)

* Tue Aug 15 2006 Thomas Woerner <twoerner@redhat.com> 1.1.3-1
- new version 1.1.3 with lots of upstream bug fixes, some security fixes
  (#205654)

* Tue Aug 15 2006 Thomas Woerner <twoerner@redhat.com> 1.1.2-2
- commented out include for sql.conf in radiusd.conf (#202561)

* Wed Jul 12 2006 Jesse Keating <jkeating@redhat.com> - 1.1.2-1.1
- rebuild

* Thu Jun  1 2006 Thomas Woerner <twoerner@redhat.com> 1.1.2-1
- new version 1.1.2

* Wed May 31 2006 Thomas Woerner <twoerner@redhat.com> 1.1.1-1
- new version 1.1.1
- fixed incorrect rlm_sql globbing (#189095)
  Thanks to Yanko Kaneti for the fix.
- fixed chown syntax in post script (#182777)
- dropped gcc34, libdir and realloc-return patch
- spec file cleanup with additional libtool build fixes

* Fri Feb 10 2006 Jesse Keating <jkeating@redhat.com> - 1.0.5-1.2
- bump again for double-long bug on ppc(64)

* Tue Feb 07 2006 Jesse Keating <jkeating@redhat.com> - 1.0.5-1.1
- rebuilt for new gcc4.1 snapshot and glibc changes

* Tue Dec 13 2005 Thomas Woerner <twoerner@redhat.com> 1.0.5-1
- new version 1.0.5

* Fri Dec 09 2005 Jesse Keating <jkeating@redhat.com>
- rebuilt

* Sat Nov 12 2005 Tom Lane <tgl@redhat.com> - 1.0.4-5
- Rebuild due to mysql update.

* Wed Nov  9 2005 Tomas Mraz <tmraz@redhat.com> - 1.0.4-4
- rebuilt with new openssl
- fixed ignored return value of realloc

* Fri Sep 30 2005 Tomas Mraz <tmraz@redhat.com> - 1.0.4-3
- use include instead of pam_stack in pam config

* Wed Jul 20 2005 Thomas Woerner <twoerner@redhat.com> 1.0.4-2
- added missing build requires for libtool-ltdl-devel (#160877)
- modified file list to get a report for missing plugins

* Tue Jun 28 2005 Thomas Woerner <twoerner@redhat.com> 1.0.4-1
- new version 1.0.4
- droppend radrelay patch (fixed upstream)

* Thu Apr 14 2005 Warren Togami <wtogami@redhat.com> 1.0.2-2
- rebuild against new postgresql-libs

* Mon Apr  4 2005 Thomas Woerner <twoerner@redhat.com> 1.0.2-1
- new version 1.0.2

* Fri Nov 19 2004 Thomas Woerner <twoerner@redhat.com> 1.0.1-3
- rebuild for MySQL 4
- switched over to installed libtool

* Fri Nov  5 2004 Thomas Woerner <twoerner@redhat.com> 1.0.1-2
- Fixed install problem of radeapclient (#138069)

* Wed Oct  6 2004 Thomas Woerner <twoerner@redhat.com> 1.0.1-1
- new version 1.0.1
- applied radrelay CVS patch from Kevin Bonner

* Wed Aug 25 2004 Warren Togami <wtogami@redhat.com> 1.0.0-3
- BuildRequires pam-devel and libtool
- Fix errant text in description
- Other minor cleanups

* Wed Aug 25 2004 Thomas Woerner <twoerner@redhat.com> 1.0.0-2.1
- renamed %_sysconfdir/pam.d/radius to %_sysconfdir/pam.d/radiusd to match default
  configuration (#130613)

* Wed Aug 25 2004 Thomas Woerner <twoerner@redhat.com> 1.0.0-2
- fixed BuildRequires for openssl-devel (#130606)

* Mon Aug 16 2004 Thomas Woerner <twoerner@redhat.com> 1.0.0-1
- 1.0.0 final

* Mon Jul  5 2004 Thomas Woerner <twoerner@redhat.com> 1.0.0-0.pre3.2
- added buildrequires for zlib-devel (#127162)
- fixed libdir patch to prefer own libeap instead of installed one (#127168)
- fixed samba account maps in LDAP for samba v3 (#127173)

* Thu Jul  1 2004 Thomas Woerner <twoerner@redhat.com> 1.0.0-0.pre3.1
- third "pre" release of version 1.0.0
- rlm_ldap is using SASLv2 (#126507)

* Tue Jun 15 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Thu Jun  3 2004 Thomas Woerner <twoerner@redhat.com> 0.9.3-4.1
- fixed BuildRequires for gdbm-devel

* Tue Mar 30 2004 Harald Hoyer <harald@redhat.com> - 0.9.3-4
- gcc34 compilation fixes

* Tue Mar 02 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Tue Feb 24 2004 Thomas Woerner <twoerner@redhat.com> 0.9.3-3.2
- added sql scripts for rlm_sql to documentation (#116435)

* Fri Feb 13 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Thu Feb  5 2004 Thomas Woerner <twoerner@redhat.com> 0.9.3-2.1
- using -fPIC instead of -fpic for s390 ans s390x

* Thu Feb  5 2004 Thomas Woerner <twoerner@redhat.com> 0.9.3-2
- radiusd is pie, now

* Tue Nov 25 2003 Thomas Woerner <twoerner@redhat.com> 0.9.3-1
- new version 0.9.3 (bugfix release)

* Fri Nov  7 2003 Thomas Woerner <twoerner@redhat.com> 0.9.2-1
- new version 0.9.2

* Mon Sep 29 2003 Thomas Woerner <twoerner@redhat.com> 0.9.1-1
- new version 0.9.1

* Mon Sep 22 2003 Nalin Dahyabhai <nalin@redhat.com> 0.9.0-2.2
- modify default PAM configuration to remove the directory part of the module
  name, so that 32- and 64-bit libpam (called from 32- or 64-bit radiusd) on
  multilib systems will always load the right module for the architecture
- modify default PAM configuration to use pam_stack

* Mon Sep  1 2003 Thomas Woerner <twoerner@redhat.com> 0.9.0-2.1
- com_err.h moved to /usr/include/et

* Tue Jul 22 2003 Thomas Woerner <twoerner@redhat.com> 0.9.0-1
- 0.9.0 final

* Wed Jul 16 2003 Thomas Woerner <twoerner@redhat.com> 0.9.0-0.9.0
- new version 0.9.0 pre3

* Thu May 22 2003 Thomas Woerner <twoerner@redhat.com> 0.8.1-6
- included directory /var/log/radius/radacct for logrotate

* Wed May 21 2003 Thomas Woerner <twoerner@redhat.com> 0.8.1-5
- moved log and run dir to files section, cleaned up post

* Wed May 21 2003 Thomas Woerner <twoerner@redhat.com> 0.8.1-4
- added missing run dir in post

* Tue May 20 2003 Thomas Woerner <twoerner@redhat.com> 0.8.1-3
- fixed module load patch

* Fri May 16 2003 Thomas Woerner <twoerner@redhat.com>
- removed la files, removed devel package
- split into 4 packages: freeradius, freeradius-mysql, freeradius-postgresql,
    freeradius-unixODBC
- fixed requires and buildrequires
- create logging dir in post if it does not exist
- fixed module load without la files

* Thu Apr 17 2003 Thomas Woerner <twoerner@redhat.com>
- Initial build.
