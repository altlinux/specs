%def_disable ommongodb

Name: rsyslog
Version: 6.2.2
Release: alt1

Summary: Enhanced system logging and kernel message trapping daemon
License: GPLv3+
Group: System/Kernel and hardware
Url: http://www.rsyslog.com
Provides: syslogd-daemon
Provides: /etc/rsyslog.d
PreReq: syslog-common

Conflicts: syslogd klogd
Conflicts: syslog-ng

Source: %name-%version.tar
Source2: mongo-c-driver.tar
Patch: %name-%version-%release.patch

BuildRequires: zlib-devel
BuildRequires: libdbi-devel
BuildRequires: libmysqlclient-devel
BuildRequires: postgresql-devel
BuildRequires: libkrb5-devel
BuildRequires: librelp-devel
BuildRequires: libgnutls-devel libgcrypt-devel
BuildRequires: libnet-snmp-devel
BuildRequires: libnet-devel
BuildRequires: libestr-devel libee-devel
BuildRequires: liblognorm-devel

%define mod_dir /%_lib/%name

%description
Rsyslog is an enhanced multi-threaded syslogd supporting, among others, MySQL,
PostgreSQL, syslog/tcp, RFC 3195, permitted sender lists, filtering on any
message part, and fine grain output format control. It is quite compatible to
stock sysklogd and can be used as a drop-in replacement. Its advanced features
make it suitable for enterprise-class, encryption protected syslog relay chains
while  at the same time being very easy to setup for the novice user.

 o lmnet.so    - Implementation of network related stuff.
 o lmregexp.so - Implementation of regexp related stuff.
 o lmtcpclt.so - This is the implementation of TCP-based syslog clients.
 o lmtcpsrv.so - Common code for plain TCP based servers.
 o imtcp.so    - This is the implementation of the TCP input module.
 o imudp.so    - This is the implementation of the UDP input module.
 o imuxsock.so - This is the implementation of the Unix sockets input module.
 o imklog.so   - The kernel log input module for Linux.
 o immark.so   - This is the implementation of the build-in mark message input
                 module.
 o imfile.so   - This is the input module for reading text file data.

%package mysql
Summary: MySQL support for rsyslog
Group: System/Kernel and hardware
Requires: %name = %version-%release

%description mysql
The rsyslog-mysql package contains a dynamic shared object that will add
MySQL database support to rsyslog.

 o ommysql.so - This is the implementation of the build-in output module for
                MySQL.

%package pgsql
Summary: PostgreSQL support for rsyslog
Group: System/Kernel and hardware
Requires: %name = %version-%release

%description pgsql
The rsyslog-pgsql package contains a dynamic shared object that will add
PostgreSQL database support to rsyslog.

 o ompgsql.so - This is the implementation of the build-in output module for
                PgSQL.

%package mongo
Summary: MongoDB support for rsyslog
Group: System/Kernel and hardware
Requires: %name = %version-%release

%description mongo
The rsyslog-mysql package contains a dynamic shared object that will add
MySQL database support to rsyslog.

 o ommongodb.so - This is the implementation of the build-in output module for
                MongoDB.

%package gssapi
Summary: GSS-API support for rsyslog
Group: System/Kernel and hardware
Requires: %name = %version-%release

%description gssapi
The rsyslog-gssapi package contains dynamic shared objects that will add
GSS-API support to rsyslog.

 o lmgssutil.so - This is a miscellaneous helper class for gss-api features.
 o imgssapi.so  - This is the implementation of the GSSAPI input module.
 o omgssapi.so  - This is the implementation of the build-in forwarding output
                  module.

%package gnutls
Summary: GNUTLS support for rsyslog
Group: System/Kernel and hardware
Requires: %name = %version-%release

%description gnutls
The rsyslog-gnutls package contains dynamic shared objects that will add
GNUTLS support to rsyslog.

 o lmnsd_gtls.so - This is a miscellaneous helper class for gnutls features.

%package relp
Summary: RELP support for rsyslog
Group: System/Kernel and hardware
Requires: %name = %version-%release

%description relp
The rsyslog-relp package contains a dynamic shared object that will add
RELP support to rsyslog.

 o imrelp.so - This is the implementation of the RELP input module.
 o omrelp.so - This is the implementation of the RELP output module.

%package dbi
Summary: Dbi support for rsyslog
Group: System/Kernel and hardware
Requires: %name = %version-%release

%description dbi
The rsyslog-dbi package contains a dynamic shared object that will add
dbi driver support to rsyslog.

 o omlibdbi.so - This is the implementation of the dbi output module.

%package snmp
Summary: SNMP support for rsyslog
Group: System/Kernel and hardware
Requires: %name = %version-%release

%description snmp
The rsyslog-snmp package contains a dynamic shared object that will add
SNMP support to rsyslog.

 o omsnmp.so - This module sends an snmp trap.

%package udpspoof
Summary: UDP forwarder with spoof the sender address for rsyslog
Group: System/Kernel and hardware
Requires: %name = %version-%release

%description udpspoof
The rsyslog-udpspoof package contains a dynamic shared object that will add
UDP forwarder, but permits to spoof the sender address.

 o omudpspoof.so - This module permits to spoof the sender address.

%package extra
Summary: Extra support for rsyslog
Group: System/Kernel and hardware
Requires: %name = %version-%release

%description extra
The rsyslog-extra package contains a dynamic shared object that will add
all other functions:

 o imptcp.so             - This is a native implementation of plain tcp input module with epool.
 o imttcp.so             - This is a native implementation of plain tcp input module with multiple thread.
 o omprog.so             - This output plugin enables rsyslog to execute a program and
                           feed it the message stream as standard input.
 o omuxsock.so           - This is the implementation of datgram unix domain socket forwarding.
 o pmaixforwardedfrom.so - This detects logs sent by AIX.
 o pmcisconames.so       - This detects logs sent by Cisco devices.
 o pmlastmsg.so          - This is a parser module specifically for those horrible
                           "<PRI>last message repeated n times" messages notoriously
                           generated by some syslog implementations.
 o pmsnare.so            - This detects logs sent by Snare.
 o mmsnmptrapd.so        - This is a message modification module. It takes messages generated
                           from snmptrapd and modifies them so that the look like they
                           originated from the real originator.
 o mmnormalize.so        - This is a message modification module. It normalizes the input message with
                           the help of liblognorm. The messages EE event structure is updated.

%package docs-html
Summary: HTML documentation for rsyslog
Group: System/Kernel and hardware
BuildArch: noarch

%description docs-html
This package contains the HTML documentation for rsyslog.


%prep
%setup -q
%patch -p1
pushd plugins/ommongodb
tar -xvf %SOURCE2
popd

%build
%autoreconf
%configure \
	--disable-static \
	--disable-testbench \
	--sbindir=/sbin \
	--libdir=/%_lib \
	--with-moddirs=%mod_dir \
	--enable-largefile \
	--enable-regexp \
	--enable-zlib \
	--enable-pthreads \
	--enable-klog \
	--enable-inet \
	--enable-gnutls \
	--enable-gssapi-krb5 \
	--enable-imfile \
	--enable-imptcp \
	--enable-imttcp \
	--enable-libdbi \
	--enable-mail \
	--enable-mysql \
	--enable-omprog \
	--enable-omudpspoof \
	--enable-omuxsock \
	--enable-omruleset \
	%{subst_enable ommongodb} \
	--enable-pmcisconames \
	--enable-pmaixforwardedfrom \
	--enable-pmlastmsg \
	--enable-pmsnare \
	--enable-pgsql \
	--enable-relp \
	--enable-snmp \
	--enable-unlimited-select \
	--enable-mmsnmptrapd \
	--enable-mmnormalize \
	--with-systemdsystemunitdir=%systemd_unitdir

%make_build

%install
%makeinstall_std
rm -f %buildroot%mod_dir/*.la

mkdir -p %buildroot{%_sysconfdir/{sysconfig,%name.d},%_initdir,%_var/spool/%name}

# fix html docs
rm -rf html_docs; mkdir -p html_docs
cp doc/*.html doc/*.jpg html_docs/
chmod 644 html_docs/*

install -m640 rsyslog.conf.alt %buildroot%_sysconfdir/%name.conf
install -m640 rsyslogd.alt %buildroot%_sysconfdir/sysconfig/rsyslogd
install -m755 rsyslogd.init %buildroot%_initdir/rsyslogd
install -m640 *_*.conf %buildroot%_sysconfdir/rsyslog.d/
install -m640 syslog.conf %buildroot%_sysconfdir/syslog.conf
install -m755 rsyslog-systemd.prestart %buildroot%systemd_unitdir/../altlinux-rsyslog-extrasockets
touch %buildroot%_sysconfdir/rsyslog.d/00_extrasockets.conf

# add aliase rsyslogd to rsyslog for systemd
ln -s rsyslog.service %buildroot%systemd_unitdir/rsyslogd.service
# add default start for systemd
mkdir -p %buildroot%systemd_unitdir/syslog.target.wants
ln -s ../rsyslog.service %buildroot%systemd_unitdir/syslog.target.wants/rsyslog.service

%post
%post_service rsyslogd

%preun
%preun_service rsyslogd

%files
%doc AUTHORS ChangeLog README  doc/rsyslog-example.conf
%config(noreplace) %attr(640,root,adm) %_sysconfdir/%name.conf
%config(noreplace) %attr(640,root,adm) %_sysconfdir/syslog.conf
%dir %_sysconfdir/%name.d/
%dir %_var/spool/%name
%config(noreplace) %attr(640,root,adm) %_sysconfdir/rsyslog.d/*_common.conf
%config(noreplace) %verify(not md5 size mtime) %attr(640,root,adm)  %ghost %_sysconfdir/rsyslog.d/00_extrasockets.conf
%config(noreplace) %_sysconfdir/sysconfig/rsyslogd
%config %_initdir/rsyslogd
%systemd_unitdir/*.service
%systemd_unitdir/../altlinux-rsyslog-extrasockets
%systemd_unitdir/syslog.target.wants/rsyslog.service
%dir %mod_dir
%mod_dir/imfile.so
%mod_dir/imklog.so
%mod_dir/immark.so
%mod_dir/imtcp.so
%mod_dir/imudp.so
%mod_dir/imuxsock.so
%mod_dir/lmnet.so
%mod_dir/lmnetstrms.so
%mod_dir/lmnsd_ptcp.so
%mod_dir/lmregexp.so
%mod_dir/lmstrmsrv.so
%mod_dir/lmtcpclt.so
%mod_dir/lmzlibw.so
%mod_dir/lmtcpsrv.so
%mod_dir/ommail.so
%mod_dir/omruleset.so

/sbin/rsyslogd
%_mandir/man?/rsyslog*

%files mysql
%doc plugins/ommysql/createDB.sql plugins/ommysql/contrib/delete_mysql
%config(noreplace) %attr(640,root,adm) %_sysconfdir/rsyslog.d/*_mysql.conf
%mod_dir/ommysql.so

%files pgsql
%doc plugins/ompgsql/createDB.sql
%config(noreplace) %attr(640,root,adm) %_sysconfdir/rsyslog.d/*_pgsql.conf
%mod_dir/ompgsql.so

%if_enabled ommongodb
%files mongo
%config(noreplace) %attr(640,root,adm) %_sysconfdir/rsyslog.d/*_mongo.conf
%mod_dir/ommongodb.so
%endif

%files gssapi
%config(noreplace) %attr(640,root,adm) %_sysconfdir/rsyslog.d/*_gssapi.conf
%mod_dir/omgssapi.so
%mod_dir/imgssapi.so
%mod_dir/lmgssutil.so

%files gnutls
%mod_dir/lmnsd_gtls.so

%files relp
%config(noreplace) %attr(640,root,adm) %_sysconfdir/rsyslog.d/*_relp.conf
%mod_dir/imrelp.so
%mod_dir/omrelp.so

%files dbi
%config(noreplace) %attr(640,root,adm) %_sysconfdir/rsyslog.d/*_dbi.conf
%mod_dir/omlibdbi.so

%files snmp
%config(noreplace) %attr(640,root,adm) %_sysconfdir/rsyslog.d/*_snmp.conf
%mod_dir/omsnmp.so

%files udpspoof
%config(noreplace) %attr(640,root,adm) %_sysconfdir/rsyslog.d/*_udpspoof.conf
%mod_dir/omudpspoof.so

%files extra
%mod_dir/imptcp.so
%mod_dir/imttcp.so
%mod_dir/omprog.so
%mod_dir/omtesting.so
%mod_dir/omuxsock.so
%mod_dir/pmaixforwardedfrom.so
%mod_dir/pmcisconames.so
%mod_dir/pmlastmsg.so
%mod_dir/pmsnare.so
%mod_dir/mmsnmptrapd.so
%mod_dir/mmnormalize.so

%files docs-html
%doc html_docs/*

%changelog
* Fri Jun 22 2012 Alexey Shabalin <shaba@altlinux.ru> 6.2.2-alt1
- 6.2.2

* Fri May 11 2012 Alexey Shabalin <shaba@altlinux.ru> 6.2.1-alt1
- 6.2.1

* Fri Mar 02 2012 Alexey Shabalin <shaba@altlinux.ru> 6.2.0-alt1
- 6.2.0 new stable release
- add plugins imttcp and mmnormalize to extra

* Fri Mar 02 2012 Alexey Shabalin <shaba@altlinux.ru> 5.8.7-alt1
- 5.8.7

* Fri Oct 21 2011 Alexey Shabalin <shaba@altlinux.ru> 5.8.6-alt1
- 5.8.6

* Wed Sep 14 2011 Alexey Shabalin <shaba@altlinux.ru> 5.8.5-alt1
- 5.8.5

* Wed Aug 10 2011 Alexey Shabalin <shaba@altlinux.ru> 5.8.4-alt1
- 5.8.4

* Thu Jul 28 2011 Alexey Shabalin <shaba@altlinux.ru> 5.8.3-alt1
- 5.8.3

* Wed Jun 29 2011 Alexey Shabalin <shaba@altlinux.ru> 5.8.2-alt1
- 5.8.2
- add dir /var/spool/rsyslog for spool

* Thu May 19 2011 Alexey Shabalin <shaba@altlinux.ru> 5.8.1-alt1
- 5.8.1
- add mmsnmptrapd module to extra package
- do not unlink sockets files in ALTLinux
- revert generate 00_extrasockets.conf in init script, but without option enable/disable
- update systemd.service for run generate 00_extrasockets.conf

* Tue May 10 2011 Alexey Shabalin <shaba@altlinux.ru> 5.8.0-alt2
- revert function reload to init script
- add reload for systemd
- add touch/rm lock in systemd-service file, needed for /sbin/reload-syslog

* Thu Apr 21 2011 Alexey Shabalin <shaba@altlinux.ru> 5.8.0-alt1
- 5.8.0
- update BR:
- update configure options
- add {post,preun}_service
- package docs as noarch
- add more subpackages
- copy syslog.conf from sysklog package
- add configs from mandriva
- use configs from /etc/rsyslog.d/ and syslog.conf
- package systemd service file
- add aliase rsyslogd to rsyslog for systemd
- add autostart for systemd
- change permition for config files
- update init script
- add conflicts to syslogd and klogd
- drop Packager
- Don't create database in scripts

* Tue Jan 13 2009 Ivan Fedorov <ns@altlinux.org> 3.20.2-alt2
- add configs & init-script
- update from upstream
- extract pgsql support to subpackage

* Sat Dec 20 2008 Ivan Fedorov <ns@altlinux.org> 3.20.2-alt1
- 3.20.2
  + security fix
- change prefix from /usr to /.

* Fri Nov 07 2008 Ivan Fedorov <ns@altlinux.org> 3.20.0-alt1
- 3.20.0

* Sun Nov 02 2008 Ivan Fedorov <ns@altlinux.org> 3.18.5-alt1
- Initial build for ALT Linux
