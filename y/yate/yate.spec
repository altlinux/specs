Name: yate
Version: 6.1.0
Release: alt3

Summary: Yet Another Telephony Engine

License: GPL
Group: System/Servers
Url: http://yate.null.ro/

Packager: Denis Smirnov <mithraen@altlinux.ru>

# Source-url: http://yate.null.ro/tarballs/yate6/yate-%version-1.tar.gz
Source: %name-%version.tar
Source2: yate.init

Patch: yate-aarch64.patch
Patch1: yate-6.1.0-alt-mysql8-transition.patch
Patch3500: yate-loongarch64.patch

BuildRequires: gcc-c++ doxygen kdoc
BuildRequires: dahdi-linux-headers libalsa-devel libgsm-devel liblksctp-devel libmysqlclient-devel
# obsoleted
# libcoredumper-devel 
# TODO: use H323Plus
#BuildRequires: libopenh323_1.19-devel libpt-devel
BuildRequires: libqt4-network libqt4-devel libspandsp6-devel libspeex-devel zlib-devel postgresql-devel

%package all
Summary: Metapackage for Yate
Group: System/Servers
Requires: %name = %version-%release
Requires: %name-alsa = %version-%release
Requires: %name-gsm = %version-%release
Requires: %name-speex = %version-%release
#Requires: %name-h323 = %version-%release
Requires: %name-isdn = %version-%release
Requires: %name-lksctp = %version-%release
Requires: %name-openssl = %version-%release
Requires: %name-zlib = %version-%release
Requires: %name-mysql = %version-%release
Requires: %name-pgsql = %version-%release
Requires: %name-qt4 = %version-%release
Requires: %name-scripts = %version-%release
Requires: %name-faxchan = %version-%release

%description all
Metapackage for Yate

%package alsa
Summary: ALSA sound driver for Yate
Group: System/Servers
Provides: %name-audiodevice
Requires: %name = %version-%release

%description alsa
Advanced Linux Sound Architecture audio driver for Yate. This is the
recommended audio interface for using the client under Linux.


%package client-common
Summary: Common files for all Yate clients
Group: System/Servers
Requires: %name = %version-%release

%description client-common
This package includes the common files needed to use Yate as a VoIP
client.


%package devel
Summary: Development package for Yate
Group: Development/Other
Requires: %name = %version-%release
Requires: %name-qt4 = %version-%release

%description devel
The yate-devel package includes the libraries and header files for
Yate that can be used to build and install new modules.


%package devel-doc
Summary: Development package for Yate
Group: Development/Other
BuildArch: noarch
Requires: %name = %version-%release

%description devel-doc
The yate-devel-doc package includes documentation for yate API


%package faxchan
Summary: Fax support for Yate
Group: System/Servers
Requires: %name = %version-%release

%description faxchan
Fax support for Yate

%package gsm
Summary: GSM audio codec for Yate
Group: System/Servers
Requires: %name = %version-%release

%description gsm
European GSM 06.10 audio codec for Yate. This is a low CPU usage codec
that provides moderate compression and good voice quality.


%package h323
Summary: H.323 protocol driver for Yate
Group: System/Servers
Requires: %name = %version-%release

%description h323
Yate driver for the ITU-T H.323 VoIP protocol based on the OpenH323
library.


%package isdn
Summary: ISDN PRI card and protocol drivers for Yate
Group: System/Servers
Requires: %name = %version-%release

%description isdn
Yate drivers for ISDN PRI cards supported by the Zaptel or Wanpipe
kernel interfaces.


%package lksctp
Summary: Linux Kernel based SCTP support for Yate
Group: System/Servers
Provides: %name-sctp
Requires: %name = %version-%release

%description lksctp
This package provides SCTP sockets support for Yate based on the Linux
Kernel implementation. These are needed for standard SIGTRAN
interfaces.


%package mysql
Summary: MySQL database driver for Yate
Group: System/Servers
Provides: %name-database
Requires: %name = %version-%release

%description mysql
This package allows Yate to connect to a MySQL database server. All
modules that support database access will be able to use MySQL.


%package openssl
Summary: OpenSSL based encryption support for Yate
Group: System/Servers
Provides: %name-ssl
Provides: %name-crypto
Requires: %name = %version-%release

%description openssl
This package provides SSL/TLS encrypted communication support for Yate
as well as cryptographic routines used for other purposes.


%package pgsql
Summary: PostgreSQL database driver for Yate
Group: System/Servers
Provides: %name-database
Requires: %name = %version-%release

%description pgsql
This package allows Yate to connect to a PostgreSQL database server.
All modules that support database access will be able to use
PostgreSQL.


%package qt4
Summary: Qt-4 client package for Yate
Group: System/Servers
Provides: %name-client
Requires: %name-client-common = %version-%release
Requires: %name = %version-%release

%description qt4
The yate-qt4 package includes the files needed to use Yate as a VoIP
client with a Qt version 4 graphical interface.


%package scripts
Summary: External scripting package for Yate
Group: System/Servers
Requires: %name = %version-%release

%description scripts
The yate-scripts package includes libraries for using external scripts
with Yate.


%package speex
Summary: Speex audio codec for Yate
Group: System/Servers
Requires: %name = %version-%release

%description speex
Speex audio codec for Yate. Speex is based on CELP  and is designed to
compress voice at bitrates ranging from 2 to 44 kbps.


%package zlib
Summary: Zlib compression support for Yate
Group: System/Servers
Provides: %name-compression
Requires: %name = %version-%release

%description zlib
This package provides Zlib data compression for Yate.


%description
Yate is a telephony engine designed to implement PBX and IVR solutions
for small to large scale projects.


%prep
%setup
%patch -p2
%patch1 -p1
%patch3500 -p1

%build
%configure --enable-sctp --enable-tdmcard --enable-dahdi --without-coredumper
%make_build || %make

%install
%makeinstall_std
mkdir -p %buildroot%_initddir/
install -D -m755 -p %SOURCE2 %buildroot%_initddir/yate
mkdir -p %buildroot%_sysconfdir/logrotate.d/
cp -p packing/yate.logrotate %buildroot%_sysconfdir/logrotate.d/yate

%files
%dir %_docdir/yate-%version
%doc %_docdir/yate-%version/README
%doc %_docdir/yate-%version/COPYING
%doc %_docdir/yate-%version/ChangeLog
%doc %_docdir/yate-%version/WebRTC-LICENSE
%doc %_docdir/yate-%version/WebRTC-LICENSE_THIRD_PARTY
%doc %_docdir/yate-%version/WebRTC-PATENTS
%doc %_docdir/yate-%version/iLBC-LICENSE.txt
%_libdir/libyate.so.*
%_libdir/libyatejabber.so.*
%_libdir/libyatesig.so.*
%_libdir/libyatemgcp.so.*
%_libdir/libyateasn.so.*
%_libdir/libyateradio.so.*
%_libdir/libyatescript.so.*
%_bindir/yate
%_mandir/*/yate.*
%_initdir/yate
%dir %_datadir/yate/data
%_datadir/yate/data/*
%dir %_libdir/yate
%dir %_libdir/yate/client
%dir %_libdir/yate/jabber
%dir %_libdir/yate/server
%dir %_libdir/yate/sip
%dir %_libdir/yate/radio
%dir %_libdir/yate/sig

%_libdir/yate/cdrbuild.yate
%_libdir/yate/cdrfile.yate
%_libdir/yate/regexroute.yate
%_libdir/yate/server/regfile.yate
%_libdir/yate/server/accfile.yate
%_libdir/yate/server/register.yate
%_libdir/yate/tonegen.yate
%_libdir/yate/tonedetect.yate
%_libdir/yate/wavefile.yate
%_libdir/yate/conference.yate
%_libdir/yate/moh.yate
%_libdir/yate/callgen.yate
%_libdir/yate/analyzer.yate
%_libdir/yate/rmanager.yate
%_libdir/yate/msgsniff.yate
%_libdir/yate/mux.yate
%_libdir/yate/pbx.yate
%_libdir/yate/dumbchan.yate
%_libdir/yate/callfork.yate
%_libdir/yate/extmodule.yate
%_libdir/yate/filetransfer.yate
%_libdir/yate/ysipchan.yate
%_libdir/yate/yrtpchan.yate
%_libdir/yate/ystunchan.yate
%_libdir/yate/ysockschan.yate
%_libdir/yate/yiaxchan.yate
%_libdir/yate/yjinglechan.yate
%_libdir/yate/enumroute.yate
%_libdir/yate/ilbccodec.yate
%_libdir/yate/cdrcombine.yate
%_libdir/yate/fileinfo.yate
%_libdir/yate/gvoice.yate
%_libdir/yate/ilbcwebrtc.yate
%_libdir/yate/isaccodec.yate
%_libdir/yate/javascript.yate

%_libdir/yate/server/cache.yate
%_libdir/yate/server/eventlogs.yate
%_libdir/yate/server/dbwave.yate
%_libdir/yate/server/dbpbx.yate
%_libdir/yate/server/pbxassist.yate
%_libdir/yate/server/park.yate
%_libdir/yate/server/queues.yate
%_libdir/yate/server/lateroute.yate
%_libdir/yate/server/callcounters.yate
%_libdir/yate/server/yradius.yate
%_libdir/yate/server/sipfeatures.yate
%_libdir/yate/server/queuesnotify.yate
%_libdir/yate/server/heartbeat.yate
%_libdir/yate/server/clustering.yate
%_libdir/yate/server/mgcpca.yate
%_libdir/yate/server/mgcpgw.yate
%_libdir/yate/server/mrcpspeech.yate
%_libdir/yate/server/ysigchan.yate
%_libdir/yate/server/ciscosm.yate
%_libdir/yate/server/sigtransport.yate
#%_libdir/yate/server/isupmangler.yate
%_libdir/yate/server/analog.yate
%_libdir/yate/server/analogdetect.yate
%_libdir/yate/server/users.yate
%_libdir/yate/server/presence.yate
%_libdir/yate/server/subscription.yate
%_libdir/yate/server/cpuload.yate
%_libdir/yate/server/ccongestion.yate
%_libdir/yate/server/monitoring.yate
%_libdir/yate/server/ysnmpagent.yate

%_libdir/yate/client/osschan.yate
%_libdir/yate/client/jabberclient.yate
%_libdir/yate/jabber/jabberserver.yate
%_libdir/yate/jabber/jbfeatures.yate
%_libdir/yate/sip/sip_cnam_lnp.yate
%_libdir/yate/radio/dummyradio.yate
%_libdir/yate/radio/radiotest.yate
%_libdir/yate/sig/camel_map.yate
%_libdir/yate/sig/isupmangler.yate
%_libdir/yate/sig/ss7_lnp_ansi.yate

%dir %_sysconfdir/yate
%config(noreplace) %_sysconfdir/yate/accfile.conf
%config(noreplace) %_sysconfdir/yate/cdrbuild.conf
%config(noreplace) %_sysconfdir/yate/cdrfile.conf
%config(noreplace) %_sysconfdir/yate/callcounters.conf
%config(noreplace) %_sysconfdir/yate/dbpbx.conf
%config(noreplace) %_sysconfdir/yate/dsoundchan.conf
%config(noreplace) %_sysconfdir/yate/enumroute.conf
%config(noreplace) %_sysconfdir/yate/sipfeatures.conf
%config(noreplace) %_sysconfdir/yate/callfork.conf
%config(noreplace) %_sysconfdir/yate/extmodule.conf
%config(noreplace) %_sysconfdir/yate/filetransfer.conf
%config(noreplace) %_sysconfdir/yate/moh.conf
%config(noreplace) %_sysconfdir/yate/mux.conf
%config(noreplace) %_sysconfdir/yate/pbxassist.conf
%config(noreplace) %_sysconfdir/yate/queues.conf
%config(noreplace) %_sysconfdir/yate/queuesnotify.conf
%config(noreplace) %_sysconfdir/yate/lateroute.conf
%config(noreplace) %_sysconfdir/yate/regexroute.conf
%config(noreplace) %_sysconfdir/yate/regfile.conf
%config(noreplace) %_sysconfdir/yate/register.conf
%config(noreplace) %_sysconfdir/yate/tonegen.conf
%config(noreplace) %_sysconfdir/yate/rmanager.conf
%config(noreplace) %_sysconfdir/yate/yate.conf
%config(noreplace) %_sysconfdir/yate/yiaxchan.conf
%config(noreplace) %_sysconfdir/yate/yradius.conf
%config(noreplace) %_sysconfdir/yate/yrtpchan.conf
%config(noreplace) %_sysconfdir/yate/ysockschan.conf
%config(noreplace) %_sysconfdir/yate/ystunchan.conf
%config(noreplace) %_sysconfdir/yate/ysipchan.conf
%config(noreplace) %_sysconfdir/yate/yjinglechan.conf
%config(noreplace) %_sysconfdir/yate/heartbeat.conf
%config(noreplace) %_sysconfdir/yate/clustering.conf
%config(noreplace) %_sysconfdir/yate/mgcpca.conf
%config(noreplace) %_sysconfdir/yate/mgcpgw.conf
%config(noreplace) %_sysconfdir/yate/analog.conf
%config(noreplace) %_sysconfdir/yate/ysigchan.conf
%config(noreplace) %_sysconfdir/yate/ciscosm.conf
%config(noreplace) %_sysconfdir/yate/sigtransport.conf
%config(noreplace) %_sysconfdir/yate/isupmangler.conf
%config(noreplace) %_sysconfdir/yate/cpuload.conf
%config(noreplace) %_sysconfdir/yate/ccongestion.conf
%config(noreplace) %_sysconfdir/yate/monitoring.conf
%config(noreplace) %_sysconfdir/yate/ysnmpagent.conf
%config(noreplace) %_sysconfdir/yate/users.conf
%config(noreplace) %_sysconfdir/yate/presence.conf
%config(noreplace) %_sysconfdir/yate/subscription.conf
%config(noreplace) %_sysconfdir/yate/jabberclient.conf
%config(noreplace) %_sysconfdir/yate/jabberserver.conf
%config(noreplace) %_sysconfdir/yate/jbfeatures.conf
%config(noreplace) %_sysconfdir/yate/sip_cnam_lnp.conf

%config(noreplace) %_sysconfdir/yate/amrnbcodec.conf
%config(noreplace) %_sysconfdir/yate/cache.conf
%config(noreplace) %_sysconfdir/yate/camel_map.conf
%config(noreplace) %_sysconfdir/yate/dummyradio.conf
%config(noreplace) %_sysconfdir/yate/eventlogs.conf
%config(noreplace) %_sysconfdir/yate/fileinfo.conf
%config(noreplace) %_sysconfdir/yate/gvoice.conf
%config(noreplace) %_sysconfdir/yate/h323chan.conf
%config(noreplace) %_sysconfdir/yate/javascript.conf
%config(noreplace) %_sysconfdir/yate/lksctp.conf
%config(noreplace) %_sysconfdir/yate/radiotest.conf
%config(noreplace) %_sysconfdir/yate/sqlitedb.conf
%config(noreplace) %_sysconfdir/yate/ss7_lnp_ansi.conf
%config(noreplace) %_sysconfdir/yate/ybladerf.conf

%config %_sysconfdir/logrotate.d/yate

%files all

%files alsa
%_libdir/yate/client/alsachan.yate

%files client-common
%_pixmapsdir/null_team-*.png
%dir %_datadir/yate/skins
%_datadir/yate/skins/*
%dir %_datadir/yate/sounds
%_datadir/yate/sounds/*
%dir %_datadir/yate/help
%_datadir/yate/help/*
%config(noreplace) %_sysconfdir/yate/providers.conf

%files devel
%_includedir/*
%_libdir/lib*.so
%_bindir/yate-config
%_mandir/*/yate-config.*
%_pkgconfigdir/yate.pc

%files devel-doc
%doc %_docdir/yate-%version/*.html
%doc %_docdir/yate-%version/api/*

%files faxchan
%_libdir/yate/faxchan.yate

%files gsm
%_libdir/yate/gsmcodec.yate

#%files h323
#%_libdir/yate/h323chan.yate
#%config(noreplace) %_sysconfdir/yate/h323chan.conf

%files isdn
%config(noreplace) %_sysconfdir/yate/wpcard.conf
%_libdir/yate/server/zapcard.yate
%config(noreplace) %_sysconfdir/yate/zapcard.conf
%config(noreplace) %_sysconfdir/yate/tdmcard.conf

%files lksctp
%_libdir/yate/server/lksctp.yate

%files mysql
%_libdir/yate/server/mysqldb.yate
%config(noreplace) %_sysconfdir/yate/mysqldb.conf

%files openssl
%_libdir/yate/openssl.yate
%config(noreplace) %_sysconfdir/yate/openssl.conf

%files pgsql
%_libdir/yate/server/pgsqldb.yate
%config(noreplace) %_sysconfdir/yate/pgsqldb.conf

%files qt4
%_bindir/yate-qt4
%_libdir/libyateqt4.so.*
%_libdir/yate/qt4/*.yate
%_menudir/yate-qt4.menu
%_desktopdir/yate-qt4.desktop
%config(noreplace) %_sysconfdir/yate/yate-qt4.conf

%files scripts
%dir %_datadir/yate/scripts
%_datadir/yate/scripts/*.*

%files speex
%_libdir/yate/speexcodec.yate

%files zlib
%_libdir/yate/zlibcompress.yate
%config(noreplace) %_sysconfdir/yate/zlibcompress.conf

%changelog
* Sun Nov 05 2023 Alexey Sheplyakov <asheplyakov@altlinux.org> 6.1.0-alt3
- NMU: fixed FTBFS on LoongArch

* Mon Jan 14 2019 Nikolai Kostrigin <nickel@altlinux.org> 6.1.0-alt2
- fix FTBFS due to transition to libmysqlclient21

* Wed Sep 26 2018 Sergey Bolshakov <sbolshakov@altlinux.ru> 6.1.0-alt1
- 6.1.0 released

* Sun Jun 24 2018 Vitaly Lipatov <lav@altlinux.ru> 6.0.0-alt1
- new version (6.0.0) with rpmgs script
- cleanup spec, fix build on aarch64
- do not use coredumper
- disable h323 build

* Mon Apr 11 2016 Ivan Zakharyaschev <imz@altlinux.org> 3.3.2-alt5
- It fails during parallel builds randomly (sometimes); therefore: NPROCS=1

* Fri Feb 01 2013 Denis Smirnov <mithraen@altlinux.ru> 3.3.2-alt4
- repocop fix for arch-dep-package-consists-of-usr-share

* Sat Jan 26 2013 Denis Smirnov <mithraen@altlinux.ru> 3.3.2-alt3
- remove devel doc from devel subpackage

* Fri Jan 25 2013 Denis Smirnov <mithraen@altlinux.ru> 3.3.2-alt2
- fix subpackage requires
- move devel docs to devel-doc subpackage

* Fri Jul 08 2011 Denis Smirnov <mithraen@altlinux.ru> 3.3.2-alt1
- first build for Sisyphus

