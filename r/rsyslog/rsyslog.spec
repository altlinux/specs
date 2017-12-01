%def_enable gssapi
%def_enable liblogging_stdlog
%def_enable rfc3195
%def_disable mmcount
%def_disable guardtime
%def_disable ksi_ls12
%def_disable omamqp1
%def_enable omhiredis
%def_enable ommongodb
%def_enable omhttpfs
%def_enable elasticsearch

Name: rsyslog
Version: 8.31.0
Release: alt1%ubt

Summary: Enhanced system logging and kernel message trapping daemon
License: GPLv3+ ASL2.0
Group: System/Kernel and hardware
Url: http://www.rsyslog.com
Source: %name-%version.tar
Patch: %name-%version.patch

BuildRequires(pre): rpm-build-ubt
BuildRequires: flex
BuildRequires: zlib-devel
BuildRequires: libdbi-devel
BuildRequires: libmysqlclient-devel
BuildRequires: postgresql-devel
BuildRequires: libkrb5-devel
BuildRequires: librelp-devel >= 1.2.14
BuildRequires: libgnutls-devel libgcrypt-devel
BuildRequires: libnet-snmp-devel
BuildRequires: libnet-devel
BuildRequires: libestr-devel >= 0.1.9
BuildRequires: libfastjson-devel >= 0.99.7
BuildRequires: libuuid-devel
%{?_enable_liblogging_stdlog:BuildRequires: liblogging-devel >= 1.0.3}
%{?_enable_rfc3195:BuildRequires: liblogging-devel >= 1.0.1}
%{?_enable_guardtime:BuildRequires: libgt-devel >= 0.3.1}
%{?_enable_ksi_ls12:BuildRequires: libksi-devel >= 3.16.0}
%{?_enable_omamqp1:BuildRequires: libqpid-proton-devel >= 0.9}
BuildRequires: liblognorm-devel >= 2.0.3
%{?_enable_ommongodb:BuildRequires: libmongoc-devel}
%{?_enable_elasticsearch:BuildRequires: libcurl-devel}
%{?_enable_omhttpfs:BuildRequires: libcurl-devel >= 7.0.0}
%{?_enable_omhiredis:BuildRequires: libhiredis-devel >= 0.10.1}
BuildRequires: libsystemd-devel >= 209
BuildRequires: iproute2
BuildRequires: /usr/bin/rst2man
BuildRequires: /usr/bin/lsb_release

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
 o imkmsg.so   - /dev/kmsg Log Input Module
 o immark.so   - This is the implementation of the build-in mark message input
                 module.
 o imfile.so   - This is the input module for reading text file data.

%package classic
Summary: Classic configuration
Group: System/Kernel and hardware
BuildArch: noarch
Requires: %name = %version-%release
Provides: syslogd-daemon
Provides: /etc/rsyslog.d
PreReq: syslog-common
Conflicts: syslogd klogd
Conflicts: syslog-ng

%description classic
This package containes a classic syslog configuration with logging to /var/log.

%package crypto
Summary: Encryption support
Group: System/Kernel and hardware
Requires: %name = %version-%release

%description crypto
This package containes a module providing log file encryption and a
command line tool to process encrypted logs.

%package journal
Summary: Systemd journal support for rsyslog
Group: System/Kernel and hardware
Requires: %name = %version-%release

%description journal
The rsyslog-journal package contains a dynamic shared object that will add
systemd journal support to rsyslog.

 o imjournal.so - This is the implementation of the systemd journal input module.
 o omjournal.so - This is the implementation of the systemd journal output module.

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
The rsyslog-mongo package contains a dynamic shared object that will add
mongo database support to rsyslog.

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

%package mmaudit
Summary: Message modification module supporting Linux audit format
Group: System/Kernel and hardware
Requires: %name = %version-%release

%description mmaudit
The rsyslog-mmaudit package contains a dynamic shared object that will add
message modification supporting Linux audit format in various settings.

 o mmaudit.so - This module provides message modification supporting Linux audit format.

%package mmcount
Summary: Message counting support for rsyslog
Group: System/Kernel and hardware
Requires: %name = %version-%release

%description mmcount
This module provides the capability to count log messages by severity
or json property of given app-name.  The count value is added into the
log message in json property named 'mmcount'

%package mmjsonparse
Summary: JSON enhanced logging support
Group: System/Kernel and hardware
Requires: %name = %version-%release

%description mmjsonparse
The rsyslog-mmjsonparse package contains a dynamic shared object that will add
capability to recognize and parse JSON enhanced syslog messages.

 o mmjsonparse.so - This module provides the capability to recognize and parse JSON enhanced
syslog messages.

%package mmnormalize
Summary: Log normalization support for rsyslog
Group: System/Kernel and hardware
Requires: %name = %version-%release

%description mmnormalize
The rsyslog-mmnormalize package contains a dynamic shared object that will add
normalize log messages via liblognorm.

 o mmnormalize.so  - This module provides the capability to normalize log messages via liblognorm.
 o pmnormalize.so        - Parser module that uses liblognorm to parse incoming messages.

%package mmanon
Summary: mmanon output module for rsyslog
Group: System/Kernel and hardware
Requires: %name = %version-%release

%description mmanon
IP Address Anonimization Module (mmanon).
It is a message modification module that actually changes the IP address
inside the message, so after calling mmanon, the original message can
no longer be obtained. Note that anonymization will break digital
signatures on the message, if they exist.


%package elasticsearch
Summary: ElasticSearch output module for rsyslog
Group: System/Kernel and hardware
Requires: %name = %version-%release

%description elasticsearch
The rsyslog-elasticsearch package contains a dynamic shared object that will add
feed logs directly into Elasticsearch.

 o omelasticsearch.so - This module provides the capability for rsyslog to feed logs directly into
Elasticsearch.

%package hiredis
Summary: Redis support for rsyslog
Group: System/Kernel and hardware
Requires: %name = %version-%release

%description hiredis
The rsyslog-hiredis package contains a dynamic shared object that will add
feed logs directly into hiredis.

 o omhiredis.so - This module provides output to Redis.

%package extra
Summary: Extra support for rsyslog
Group: System/Kernel and hardware
Requires: %name = %version-%release

%description extra
The rsyslog-extra package contains a dynamic shared object that will add
all other functions:

 o imptcp.so             - This is a native implementation of plain tcp input module with epool.
 o omprog.so             - This output plugin enables rsyslog to execute a program and
                           feed it the message stream as standard input.
 o omuxsock.so           - This is the implementation of datgram unix domain socket forwarding.
 o pmaixforwardedfrom.so - This detects logs sent by AIX.
 o pmcisconames.so       - This detects logs sent by Cisco devices.
 o pmciscoios.so         - Parser supporting various Cisco IOS formats
 o pmlastmsg.so          - This is a parser module specifically for those horrible
                           "<PRI>last message repeated n times" messages notoriously
                           generated by some syslog implementations.
 o pmsnare.so            - This detects logs sent by Snare.
 o pmpanngfw             - Module to detect and transform PAN-OS NGFW logs into a format compatible with mmnormalize
 o mmsnmptrapd.so        - This is a message modification module. It takes messages generated
                           from snmptrapd and modifies them so that the look like they
                           originated from the real originator.
 o imdiag.so             - The testing module, which enables to talk to the rsyslog core at runtime
 o impstats.so           - Input Module to Generate Periodic Statistics of Internal Counters
 o omstdout.so           - stdout output module (stdout)
 o mmexternal.so         - external message modification modules


%prep
%setup -q
%patch -p1

%build
%autoreconf
# the hiredis-devel package doesn't provide a pkg-config file
export HIREDIS_CFLAGS=-I/usr/include/hiredis
export HIREDIS_LIBS=-lhiredis
%configure \
	--sbindir=/sbin \
	--libdir=/%_lib \
	--disable-static \
	--disable-testbench \
	%{subst_enable elasticsearch} \
	%{subst_enable mmcount} \
	--enable-gnutls \
	%{?_enable_gssapi:--enable-gssapi-krb5} \
	--enable-imdiag \
	--enable-imfile \
	--enable-imjournal \
	--enable-impstats \
	--enable-imptcp \
	--enable-inet \
	--enable-klog \
	--enable-kmsg \
	--enable-largefile \
	--enable-libdbi \
	%{subst_enable guardtime} \
	%{?_enable_ksi_ls12:--enable-ksi-ls12} \
	%{?_enable_liblogging_stdlog:--enable-liblogging-stdlog} \
	%{subst_enable rfc3195} \
	--enable-mail \
	--enable-mmanon \
	--enable-mmaudit \
	--enable-mmjsonparse \
	--enable-mmnormalize \
	--enable-mmsnmptrapd \
	--enable-mysql \
	%{subst_enable omhttpfs} \
	%{subst_enable omamqp1} \
	%{subst_enable omhiredis} \
	--enable-omjournal \
	%{subst_enable ommongodb} \
	--enable-omprog \
	--enable-omruleset \
	--enable-omstdout \
	--enable-omudpspoof \
	--enable-omuxsock \
	--enable-pgsql \
	--enable-pmaixforwardedfrom \
	--enable-pmcisconames \
	--enable-pmciscoios \
	--enable-pmnull \
	--enable-pmnormalize \
	--enable-pmlastmsg \
	--enable-pmsnare \
	--enable-pmpanngfw \
	--enable-regexp \
	--enable-relp \
	--enable-snmp \
	--enable-unlimited-select \
	--enable-usertools \
	--enable-generate-man-pages \
	--with-systemdsystemunitdir=%_unitdir

%make_build

%install
%makeinstall_std
rm -f %buildroot%mod_dir/*.la

mkdir -p %buildroot{%_sysconfdir/{sysconfig,%name.d},%_initdir,%_var/spool/%name}

install -m640 rsyslog.conf.alt %buildroot%_sysconfdir/%name.conf
install -m640 rsyslogd.alt %buildroot%_sysconfdir/sysconfig/rsyslogd
install -m755 rsyslogd.init %buildroot%_initdir/rsyslogd
install -m640 *_*.conf %buildroot%_sysconfdir/rsyslog.d/
install -m640 syslog.conf %buildroot%_sysconfdir/syslog.conf
install -m755 rsyslog-systemd.prestart %buildroot%_unitdir/../altlinux-rsyslog-extrasockets
touch %buildroot%_sysconfdir/rsyslog.d/00_extrasockets.conf

# add aliase rsyslogd to rsyslog for systemd
ln -s rsyslog.service %buildroot%_unitdir/rsyslogd.service
# add default start for systemd
mkdir -p %buildroot%_unitdir/syslog.target.wants
ln -s ../rsyslog.service %buildroot%_unitdir/syslog.target.wants/rsyslog.service
mkdir -p %buildroot%_unitdir/rsyslog.service.d
install -m644 rsyslog.classic.conf.d %buildroot%_unitdir/rsyslog.service.d/classic.conf

%post
%post_service rsyslogd

%preun
%preun_service rsyslogd

%files
%doc AUTHORS ChangeLog README
%config(noreplace) %attr(640,root,adm) %_sysconfdir/%name.conf
%dir %_sysconfdir/%name.d/
%dir %_var/spool/%name
%config(noreplace) %attr(640,root,adm) %_sysconfdir/rsyslog.d/*_common.conf
%config(noreplace) %_sysconfdir/sysconfig/rsyslogd
%config %_initdir/rsyslogd
%dir %_unitdir/rsyslog.service.d
%_unitdir/*.service
%_unitdir/syslog.target.wants/rsyslog.service
%dir %mod_dir
%mod_dir/imfile.so
%mod_dir/imklog.so
%mod_dir/imkmsg.so
%mod_dir/immark.so
%mod_dir/imtcp.so
%mod_dir/im3195.so
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

%files classic
%config(noreplace) %attr(640,root,adm) %_sysconfdir/rsyslog.d/*_classic.conf
%config(noreplace) %attr(640,root,adm) %_sysconfdir/syslog.conf
%config(noreplace) %verify(not md5 size mtime) %attr(640,root,adm)  %ghost %_sysconfdir/rsyslog.d/00_extrasockets.conf
%_unitdir/../altlinux-rsyslog-extrasockets
%_unitdir/rsyslog.service.d/classic.conf

%files crypto
%_bindir/rscryutil
%mod_dir/lmcry_gcry.so
%_man1dir/rscryutil.*

%files journal
%config(noreplace) %attr(640,root,adm) %_sysconfdir/rsyslog.d/*_journal.conf
%mod_dir/imjournal.so
%mod_dir/omjournal.so

%files mysql
%doc plugins/ommysql/createDB.sql
%config(noreplace) %attr(640,root,adm) %_sysconfdir/rsyslog.d/*_mysql.conf
%mod_dir/ommysql.so

%files pgsql
%doc plugins/ompgsql/createDB.sql
%config(noreplace) %attr(640,root,adm) %_sysconfdir/rsyslog.d/*_pgsql.conf
%mod_dir/ompgsql.so

%files mongo
%_bindir/logctl
%config(noreplace) %attr(640,root,adm) %_sysconfdir/rsyslog.d/*_mongo.conf
%mod_dir/ommongodb.so

%if_enabled gssapi
%files gssapi
%config(noreplace) %attr(640,root,adm) %_sysconfdir/rsyslog.d/*_gssapi.conf
%mod_dir/omgssapi.so
%mod_dir/imgssapi.so
%mod_dir/lmgssutil.so
%endif

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

%files mmaudit
%mod_dir/mmaudit.so

%if_enabled mmcount
%files mmcount
%mod_dir/mmcount.so
%endif

%files mmjsonparse
%mod_dir/mmjsonparse.so

%files mmnormalize
%mod_dir/mmnormalize.so
%mod_dir/pmnormalize.so

%files mmanon
%mod_dir/mmanon.so

%files elasticsearch
%mod_dir/omelasticsearch.so

%files hiredis
%mod_dir/omhiredis.so

%files extra
%mod_dir/imdiag.so
%mod_dir/imptcp.so
%mod_dir/impstats.so
%mod_dir/omhttpfs.so
%mod_dir/omprog.so
%mod_dir/omtesting.so
%mod_dir/omstdout.so
%mod_dir/omuxsock.so
%mod_dir/pmaixforwardedfrom.so
%mod_dir/pmcisconames.so
%mod_dir/pmciscoios.so
%mod_dir/pmnull.so
%mod_dir/pmlastmsg.so
%mod_dir/pmsnare.so
%mod_dir/pmpanngfw.so
%mod_dir/mmexternal.so
%mod_dir/mmsnmptrapd.so

%changelog
* Fri Dec 01 2017 Alexey Shabalin <shaba@altlinux.ru> 8.31.0-alt1%ubt
- 8.31.0
- update systemd drop-in config (ALT#32812)

* Wed Nov 08 2017 Alexey Shabalin <shaba@altlinux.ru> 8.30.0-alt1%ubt
- 8.30.0

* Mon Oct 16 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 8.28.0-alt2
- Rebuilt with libdbi-0.9.0.

* Mon Sep 18 2017 Gordeev Mikhail <obirvalger@altlinux.org> 8.28.0-alt1.1
- Rebuild with libhiredis 1.13.3

* Tue Jul 11 2017 Alexey Shabalin <shaba@altlinux.ru> 8.28.0-alt1
- 8.28.0

* Thu Jun 15 2017 Alexey Shabalin <shaba@altlinux.ru> 8.27.0-alt1
- 8.27.0

* Wed Feb 22 2017 Alexey Shabalin <shaba@altlinux.ru> 8.25.0-alt1
- 8.25.0

* Fri Jan 13 2017 Alexey Shabalin <shaba@altlinux.ru> 8.24.0-alt1
- 8.24.0

* Wed Apr 20 2016 Alexey Shabalin <shaba@altlinux.ru> 8.18.0-alt1
- 8.18.0

* Thu Feb 25 2016 Alexey Shabalin <shaba@altlinux.ru> 8.16.0-alt3
- add load imuxsock module to rsyslog-classic config
- upadte altlinux-rsyslog-extrasockets script
- move altlinux-rsyslog-extrasockets script to rsyslog-classic
- add drop-in config rsyslog.service.d/classic.conf to rsyslog-classic
- drop $IncludeConfig /etc/syslog.conf from rsyslog.conf (in 00_classic.conf now)

* Wed Feb 24 2016 Eugene Prokopiev <enp@altlinux.ru> 8.16.0-alt2
- extract rsyslog-classic
- comment all input modules and add commented imjournal
- unit cleanup

* Tue Jan 26 2016 Alexey Shabalin <shaba@altlinux.ru> 8.16.0-alt1
- 8.16.0
- add pmpanngfw to extra package

* Tue Nov 17 2015 Alexey Shabalin <shaba@altlinux.ru> 8.14.0-alt1
- 8.14.0

* Mon Aug 17 2015 Alexey Shabalin <shaba@altlinux.ru> 8.12.0-alt1
- 8.12.0

* Thu Jul 02 2015 Alexey Shabalin <shaba@altlinux.ru> 8.11.0-alt1
- 8.11.0

* Thu Apr 09 2015 Alexey Shabalin <shaba@altlinux.ru> 8.9.0-alt1
- 8.9.0

* Wed Jan 14 2015 Alexey Shabalin <shaba@altlinux.ru> 8.7.0-alt1
- 8.7.0

* Fri Dec 05 2014 Alexey Shabalin <shaba@altlinux.ru> 8.6.0-alt1
- 8.6.0

* Thu Oct 09 2014 Alexey Shabalin <shaba@altlinux.ru> 8.4.2-alt1
- 8.4.2 (v8-stable)
- fixed CVE-2014-3634, CVE-2014-3683

* Wed Jun 04 2014 Alexey Shabalin <shaba@altlinux.ru> 8.2.2-alt2
- build with libjson-c-devel

* Wed Jun 04 2014 Alexey Shabalin <shaba@altlinux.ru> 8.2.2-alt1
- 8.2.2

* Thu Apr 24 2014 Alexey Shabalin <shaba@altlinux.ru> 8.2.1-alt1
- 8.2.1

* Fri Jan 10 2014 Alexey Shabalin <shaba@altlinux.ru> 7.4.8-alt3
- drop SysSock.Unlink=off option (ALT#29666)

* Fri Jan 10 2014 Alexey Shabalin <shaba@altlinux.ru> 7.4.8-alt2
- fixed run for SysV

* Thu Jan 09 2014 Alexey Shabalin <shaba@altlinux.ru> 7.4.8-alt1
- 7.4.8

* Tue Dec 10 2013 Alexey Shabalin <shaba@altlinux.ru> 7.4.7-alt1
- 7.4.7

* Thu Nov 07 2013 Alexey Shabalin <shaba@altlinux.ru> 7.4.6-alt1
- 7.4.6

* Tue Oct 22 2013 Alexey Shabalin <shaba@altlinux.ru> 7.4.5-alt1
- 7.4.5

* Wed Jul 31 2013 Alexey Shabalin <shaba@altlinux.ru> 7.4.3-alt1
- 7.4.3

* Thu Jul 11 2013 Alexey Shabalin <shaba@altlinux.ru> 7.4.1-alt1
- 7.4.1
- add journal subpackage
- add crypto subpackage

* Fri Apr 26 2013 Alexey Shabalin <shaba@altlinux.ru> 7.2.7-alt1
- 7.2.7

* Thu Mar 14 2013 Alexey Shabalin <shaba@altlinux.ru> 7.2.6-alt1
- 7.2.6

* Thu Jan 17 2013 Alexey Shabalin <shaba@altlinux.ru> 7.2.5-alt1
- 7.2.5

* Mon Dec 10 2012 Alexey Shabalin <shaba@altlinux.ru> 7.2.4-alt1
- 7.2.4

* Thu Dec 06 2012 Alexey Shabalin <shaba@altlinux.ru> 7.2.3-alt1
- snapshot v7-stable branch
- add imkmsg.so plugin to base package
- add imdiag.so, impstats.so, omstdout.so, pmrfc3164sd.so to extra package
- add packages:
  + mongo (ommongodb plugin)
  + mmaudit
  + mmjsonparse
  + elasticsearch
  + hiredis
- move mmnormalize.so from extra package to separate mmnormalize package

* Fri Oct 12 2012 Alexey Shabalin <shaba@altlinux.ru> 6.4.2-alt2
- fix logging chrooted services - add imuxsock module to generated config

* Thu Sep 20 2012 Alexey Shabalin <shaba@altlinux.ru> 6.4.2-alt1
- 6.4.2

* Wed Sep 19 2012 Alexey Shabalin <shaba@altlinux.ru> 6.4.1-alt1
- 6.4.1 new stable release

* Tue Jul 17 2012 Alexey Shabalin <shaba@altlinux.ru> 6.2.2-alt2
- fix unit file for systemd-186

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
