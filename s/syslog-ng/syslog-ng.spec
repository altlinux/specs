#!TODO
# systemd support (trivial)
# chroot support
# improve modules packaging (add config examples)

%def_enable	geoip
%def_enable	smtp
%def_enable	json
%def_disable	amqp
%def_enable	mongodb
%def_enable	curl
%def_enable	systemd

Name: syslog-ng
Version: 3.13.2
Release: alt1

Summary: syslog-ng daemon
Group: System/Kernel and hardware
License: %gpllgpl2only
URL: https://syslog-ng.org
Provides: syslogd-daemon
Prereq:	syslog-common
Conflicts: klogd < 1.4.1-alt7

Provides: libeventlog = %EVR
Obsoletes: libeventlog < %EVR

Source: %name-%version.tar
# VCS git
#https://github.com/balabit/syslog-ng.git

Patch1: %name-%version.patch

BuildRequires: rpm-build-licenses

# Automatically added by buildreq on Fri Apr 19 2013 (-bi)
# optimized out: elfutils libcom_err-devel libkrb5-devel pkg-config python-base python-modules
# base config:
# + SSL/TLS
# + PCRE
# + SQL
BuildRequires: flex autoconf-archive glib2-devel libcap-devel libdbi-devel
BuildRequires: libnet2-devel libpcre-devel libpopt-devel
BuildRequires: libssl-devel libuuid-devel libwrap-devel libivykis-devel
BuildRequires: xsltproc docbook-style-xsl python-devel

%{?_enable_geoip:BuildRequires: libGeoIP-devel}
%{?_enable_json:BuildRequires: libjson-c-devel}
%{?_enable_smtp:BuildRequires: libesmtp-devel}
%{?_enable_amqp:BuildRequires: librabbitmq-c-devel}
%{?_enable_mongodb:BuildRequires: libmongoc-devel}
%{?_enable_curl:BuildRequires: libcurl-devel}
%{?_enable_systemd:BuildRequires: libsystemd-devel}

%description
syslog-ng, as the name shows, is a syslogd replacement, but with new
functionality for the new generation. The original syslogd allows
messages only to be sorted based on priority/facility pairs; syslog-ng
adds the possibility to filter based on message contents using regular
expressions. The new configuration scheme is intuitive and powerful.
Forwarding logs over TCP and remembering all forwarding hops makes it
ideal for firewalled environments.

%package libdbi
Summary: libdbi support for %{name}
Group: System/Libraries

%description libdbi
This module supports a large number of database systems via libdbi.

%package geoip
Summary: GeoIP support for %{name}
Group: System/Libraries

%description geoip
This module provides a function to get GeoIP info from an IPv4 address.

%package smtp
Summary: SMTP destination support for %{name}
Group: System/Libraries

%description smtp
This module provides SMTP destination support for %{name}.

%package json
Summary: JSON support for %{name}
Group: System/Libraries

%description json
This module provides JSON parsing & formatting support for %{name}.

%package amqp
Summary: AMQP support for %{name}
Group: System/Libraries

%description amqp
This module provides AMQP destination support for %{name}.

%package mongodb
Summary: mongodb support for %{name}
Group: System/Libraries

%description mongodb
This module supports the mongodb database via libmongoc

%package http
Summary: http support for %{name}
Group: System/Libraries
Provides: %name-curl = %EVR
Obsoletes: %name-curl < %EVR

%description http
The http destination can send the log as HTTP requests to an HTTP server.
It supports setting url, method, headers, user\_agent, authentication
and body. Only PUT and POST method is supported so far. If the method is
not set, POST will be used.

%package journal
Summary: Systemd journal support for %{name}
Group: System/Libraries

%description journal
This module provides JSON parsing & formatting support for %{name}.

%package python
Summary: Python destination support for syslog-ng
Requires: %name = %version-%release
Group: System/Libraries

%description python
This package provides python destination support for syslog-ng

%package -n python-module-%name-debuggercli
Summary: Debug bundle generator script
Requires: %name-python = %version-%release
Group: System/Libraries
BuildArch: noarch

%description -n python-module-%name-debuggercli
This package provides debug bundle generator script for
collecting debug related information.

%package devel
Summary: Development files for %name
Group: Development/C
Requires: %name = %version-%release  libivykis-devel
Provides: libeventlog-devel = %EVR
Obsoletes: libeventlog-devel < %EVR

%description devel
The %name-devel package contains libraries and header files for
developing applications that use %name.

%package devel-test
Summary: Test helper package for %name modules
Group: Development/C
Requires: %name = %version-%release

%description devel-test
The %name-devel-test package contains library for testing modules

%prep
%setup -q
%patch1 -p1
%if_enabled amqp
pushd modules/afamqp/rabbitmq-c
tar -xf ../../../altlinux/rabbitmq-c-v0.3.0-80-gc9f6312.tar.gz
autoreconf -i
popd
%endif

# copied from "syslog-ng-3.6.1/autogen.sh"
libtoolize --force --copy
aclocal -I m4 --install
#sed -i -e 's/PKG_PROG_PKG_CONFIG(\[0\.16\])/PKG_PROG_PKG_CONFIG([0.14])/g' aclocal.m4
autoheader
automake --foreign --add-missing --copy
autoconf

# fix perl path
%{__sed} -i 's|^#!/usr/local/bin/perl|#!%{__perl}|' contrib/relogger.pl

%build
skip_submodules=1 ./autogen.sh
#add_optflags -levtlog -livykis -lgmodule-2.0 -lglib-2.0 -lpcre

# configure is searching libmongoc instead of libmongoc-1.0 via pkg-config
#export LIBMONGO_CFLAGS="-I%_includedir/libmongoc-1.0 -I%_includedir/libbson-1.0"
#export LIBMONGO_LIBS="-lsasl2 -lssl -lcrypto -lrt -lmongoc-1.0 -lbson-1.0"

%configure \
 --sbindir=/sbin \
 --sysconfdir=%_sysconfdir/%name \
 --localstatedir=/var/lib/syslog-ng \
 --datadir=%_datadir \
 --mandir=%_mandir \
 --with-ivykis=system \
 --with-pidfile-dir=/var/run \
 --with-module-dir=%_libdir/%name \
 --with-systemdsystemunitdir=%_unitdir \
 --enable-ipv6 \
 --enable-dynamic-linking \
 --enable-tcp-wrapper \
 --enable-spoof-source \
 --with-embedded-crypto \
 --enable-manpages \
 %{subst_enable geoip} \
 %{subst_enable smtp} \
 %{subst_enable json} \
 %{subst_enable amqp} \
 %{subst_enable systemd} \
%if_enabled mongodb
 %{subst_enable mongodb} \
 --with-mongoc=system
%endif

##
# disabled while auto* from autogen.sh is used
## fixed libraries path in RPATH
#sed -i 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' libtool
#sed -i 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' libtool
##

%make_build XSL_STYLESHEET=/usr/share/xml/docbook/xsl-stylesheets/manpages/docbook.xsl

%install
mkdir -p %buildroot%_initdir
make DESTDIR=%buildroot sbindir=/sbin sysconfdir=%_sysconfdir/%name \
  mandir=%_mandir prefix=%prefix install

install -m755 -D -p altlinux/%name.init %buildroot%_initdir/%name
install -m640 -D -p altlinux/%name.conf %buildroot%_sysconfdir/%name/%name.conf
install -m640 -D -p altlinux/%name.sysconfig %buildroot%_sysconfdir/sysconfig/%name
install -m644 -D -p altlinux/%name.service %buildroot%_unitdir/%name.service
rm -f %buildroot%_unitdir/%{name}@.service

install -m644 -p config.h %buildroot%_includedir/%name

mkdir -p %buildroot%_localstatedir/%name
mkdir -p %buildroot%_sysconfdir/%name/conf.d 

# installation of xsd  broken in 3.6.3
install -c -m 644 doc/xsd/patterndb-1.xsd doc/xsd/patterndb-2.xsd doc/xsd/patterndb-3.xsd doc/xsd/patterndb-4.xsd \
    %buildroot%_datadir/%name/xsd

find %buildroot -name "*.la" -exec rm -f {} +

%post
%post_service %name
if [ $1 = 1 ]; then
    [ -x /sbin/syslogd ] && /sbin/chkconfig --level 2345 syslogd off ||:
    [ -x /sbin/klogd ] && /sbin/chkconfig --level 2345 klogd off ||:
fi

%triggerpostun -- %name <= 3.0.10-alt1
if [ -f %_sysconfdir/%name.conf.rpmsave ]; then
	echo "legacy configuration detected, new config moved to %_sysconfdir/%name"
	echo "please review and apply local changes from %_sysconfdir/%name.conf.rpmsave config!"
fi

%preun
%preun_service %name
if [ $1 = 0 ]; then
    [ -x /sbin/syslogd ] && /sbin/chkconfig --level 2345 syslogd on ||:
    [ -x /sbin/klogd ] && /sbin/chkconfig --level 2345 klogd on ||:
fi

%files
%doc AUTHORS COPYING NEWS.md README.md
%doc doc/security/*.txt
%doc contrib/{syslog2ng,syslog-ng.vim,relogger.pl,syslog-ng.conf.doc}

%dir %_sysconfdir/%name
%dir %_sysconfdir/%name/patterndb.d
%dir %_sysconfdir/%name/conf.d
%config(noreplace) %_sysconfdir/%name/%name.conf
%config(noreplace) %_sysconfdir/%name/scl.conf
%config(noreplace) %_sysconfdir/sysconfig/%name
%_initdir/%name
%_unitdir/%name.service

/sbin/%name
/sbin/%name-ctl
# Exclude package debug bundle generator for avoid many requirements
%exclude /sbin/%name-debun
%_bindir/loggen
%_bindir/pdbtool
%_bindir/update-patterndb
%_bindir/dqtool

%dir %_libdir/%name
# basic plugin set
%_libdir/%name/libaffile.so
%_libdir/%name/libafprog.so
%_libdir/%name/libafsocket.so
%_libdir/%name/libafstomp.so
%_libdir/%name/libafuser.so
%_libdir/%name/libbasicfuncs.so
%_libdir/%name/libconfgen.so
%_libdir/%name/libcryptofuncs.so
%_libdir/%name/libcsvparser.so
%_libdir/%name/libdbparser.so
%_libdir/%name/libgraphite.so
%_libdir/%name/liblinux-kmsg-format.so
%_libdir/%name/libpseudofile.so
%_libdir/%name/libsyslogformat.so
%_libdir/%name/libsystem-source.so
%_libdir/%name/libkvformat.so
# added in 3.8
%_libdir/%name/libadd-contextual-data.so
%_libdir/%name/libcef.so
%_libdir/%name/libdate.so
%_libdir/%name/libdisk-buffer.so
# added in 3.12
%_libdir/%name/libmap-value-pairs.so
%_libdir/%name/libsnmptrapd-parser.so
%_libdir/%name/libstardate.so
%_libdir/%name/libtags-parser.so
%_libdir/%name/libtfgetent.so
%_libdir/%name/libxml.so
# added in 3.13
%_libdir/%name/libappmodel.so
 
%_libdir/lib%name-*.so.*
%_libdir/libevtlog-*.so.*

%dir %_datadir/%name
%dir %_datadir/%name/include
%dir %_datadir/%name/xsd
%_datadir/%name/include/*
%_datadir/%name/xsd/*

%_man1dir/*
%_man5dir/*
%_man8dir/*

%dir %_localstatedir/%name

%files libdbi
%_libdir/%name/libafsql.so

%if_enabled geoip
%files geoip
%_libdir/%name/libgeoip-plugin.so
%endif

%if_enabled smtp
%files smtp
%_libdir/%name/libafsmtp.so
%endif

%if_enabled json
%files json
%_libdir/%name/libjson-plugin.so
%endif

%if_enabled amqp
%files amqp
%_libdir/%name/libafamqp.so
%endif

%if_enabled mongodb
%files mongodb
%_libdir/%name/libafmongodb.so
%endif

%if_enabled curl
%files http
%_libdir/%name/libhttp.so
%endif

%if_enabled systemd
%files journal
%_libdir/%name/libsdjournal.so
%endif

%files python
%_libdir/%name/libmod-python.so

%files -n python-module-%name-debuggercli
%dir %python_sitelibdir_noarch/syslogng/
%python_sitelibdir_noarch/syslogng/*.py*
%python_sitelibdir_noarch/syslogng-1.0-py2.7.egg-info

%dir %python_sitelibdir_noarch/syslogng/debuggercli
%python_sitelibdir_noarch/syslogng/debuggercli/*.py*

%files devel
%dir %_includedir/%name
#_includedir/%name/*.h
%_includedir/%name/*

%dir %_datadir/%name/tools
%_datadir/%name/tools/*

%_libdir/lib%name.so
%_pkgconfigdir/%name.pc

%_libdir/libevtlog.so

%_pkgconfigdir/%name-native-connector.pc
%_libdir/libsyslog-ng-native-connector.a

%_pkgconfigdir/%name-add-contextual-data.pc

%files devel-test
%dir %_libdir/%name/libtest
%_libdir/%name/libtest/libsyslog-ng-test.a
%_pkgconfigdir/%name-test.pc

%changelog
* Mon Dec 11 2017 Alexey Shabalin <shaba@altlinux.ru> 3.13.2-alt1
- 3.13.2
- Exclude package debug bundle generator for avoid many requirements (ATL #34311)

* Mon Dec 04 2017 Alexey Shabalin <shaba@altlinux.ru> 3.13.1-alt1
- 3.13.1
- add condition for build with systemd journal support
- split package for systemd journal support
- simplify confitions for BR:

* Fri Dec 01 2017 Alexey Shabalin <shaba@altlinux.ru> 3.12.1-alt1
- 3.12.1
- build with new libmongoc-1.0 (1.8.2)
- build with systemd support

* Mon Oct 16 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 3.8.1-alt2
- Rebuilt with libdbi-0.9.0.

* Fri Jun 23 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 3.8.1-alt1.2
- Update syslong-ng-json dependencies

* Tue May 02 2017 Andrey Cherepanov <cas@altlinux.org> 3.8.1-alt1.1
- Rebuild with new version of libjson

* Wed Aug 24 2016 Sergey Y. Afonin <asy@altlinux.ru> 3.8.1-alt1
- 3.8.1

* Mon May 23 2016 Sergey Y. Afonin <asy@altlinux.ru> 3.7.3-alt1
- 3.7.3

* Thu Jun 25 2015 Sergey Y. Afonin <asy@altlinux.ru> 3.6.3-alt2
- changed default configuration:
  + removed "unix-dgram ("/var/lib/klogd/dev/log");"
    (/var/lib/klogd/dev/log is a part of klogd package)
  + changed "_" to "-" in names of options

* Sun Jun 21 2015 Sergey Y. Afonin <asy@altlinux.ru> 3.6.3-alt1
- 3.6.3

* Sat Dec 06 2014 Sergey Y. Afonin <asy@altlinux.ru> 3.6.1-alt1
- 3.6.1 (ALT #30325)
- new subpackage devel-test
- added disabling/enabling klogd in post/preun (ALT #28895#c12)

* Thu Dec 26 2013 Sergey Y. Afonin <asy@altlinux.ru> 3.4.7-alt1
- 3.4.7 (git20131225)

* Thu Dec 05 2013 Sergey Y. Afonin <asy@altlinux.ru> 3.4.6-alt1.git20131204
- 3.4.6 (git20131204)

* Wed Sep 11 2013 Sergey Y. Afonin <asy@altlinux.ru> 3.4.3-alt2.git20130813
- changed default permissions (ALT #29312)

* Thu Aug 15 2013 L.A. Kostis <lakostis@altlinux.ru> 3.4.3-alt1.git20130813
- Updated to v3.0.10-1507-g64d670f GIT.

* Sun Jun 02 2013 L.A. Kostis <lakostis@altlinux.ru> 3.4.1-alt1.git20130528
- packaging changes (see TODO for full list):
  + .conf: sync config file with RedHat/upstream changes.
  + .spec: notify about configuration changes.
  + .spec: enhance doc section.
  + .spec: split plugins to separate packages.
  + .spec: fix rpath issue..
  + .spec: fix module_dir.

* Tue May 28 2013 L.A. Kostis <lakostis@altlinux.ru> 3.4.1-alt0.git20130528
- Prepare for first build.
- Use GIT 20130528 snapshot.

* Mon Apr 15 2013 Sergey Y. Afonin <asy@altlinux.ru> 3.4.1-alt0
- 3.4.1 (some parts of 3.4.1-1.fc19 spec used)

* Mon Jan 31 2011 Sergey Alembekov <rt@altlinux.ru> 3.0.10-alt1
- 3.0.10

* Tue Dec 07 2010 Igor Vlasenko <viy@altlinux.ru> 3.0.5-alt2.1.1
- rebuild with new openssl and/or boost by request of git.alt administrator

* Tue Mar 09 2010 Sergey Alembekov <rt@altlinux.ru> 3.0.5-alt2.1
- #23070 again :)

* Mon Mar 08 2010 Sergey Alembekov <rt@altlinux.ru> 3.0.5-alt2
- new syntax for default configuration; (#23070)
- fix pid creation (#23071)

* Thu Jan 28 2010 Sergey Alembekov <rt@altlinux.ru> 3.0.5-alt1
- 3.0.5

* Mon Jan 12 2009 Dmitry Lebkov <dlebkov@altlinux.ru> 2.1.3-alt1
- 2.1.3

* Sun Apr 06 2008 Dmitry Lebkov <dlebkov@altlinux.ru> 2.0.9-alt1
- 2.0.9
- init-script changes:
  + add 'check' action -- validate syslog-ng.conf syntax;
  + validate syslog-ng.conf syntax before start|restart|reload;
- change default configuration:
  + 'MARK' message every 5 min.;
  + 'STATS' message every 1 hour (#14686)

* Fri Feb 01 2008 Dmitry Lebkov <dlebkov@altlinux.ru> 2.0.8-alt1
- 2.0.8

* Thu Jan 10 2008 Dmitry Lebkov <dlebkov@altlinux.ru> 2.0.7-alt1
- 2.0.7

* Fri Jul 27 2007 Dmitry Lebkov <dlebkov@altlinux.ru> 2.0.5-alt1
- 2.0.5
- add '--enable-tcp-wrapper' and '--enable-spoof-source'
  configure flags


* Sun Apr 01 2007 Dmitry Lebkov <dlebkov@altlinux.ru> 2.0.3-alt1
- fix path for syslog-ng.persist

* Tue Mar 27 2007 Dmitry Lebkov <dlebkov@altlinux.ru> 2.0.3-alt0
- 2.0.3

* Sat Feb 03 2007 Dmitry Lebkov <dlebkov@altlinux.ru> 2.0.2-alt0
- 2.0.2

* Tue Jan 09 2007 Dmitry Lebkov <dlebkov@altlinux.ru> 2.0.1-alt0
- 2.0.1

* Tue Apr 13 2004 Stanislav Ievlev <inger@altlinux.org> 1.6.2-alt2
- require resent libol (#3823)

* Wed Mar 10 2004 Stanislav Ievlev <inger@altlinux.org> 1.6.2-alt1
- 1.6.2

* Tue Sep 30 2003 Stanislav Ievlev <inger@altlinux.ru> 1.4.17-alt1.1
- don't made static link with libol
- update init-script
- fix building in hasher

* Thu Oct 31 2002 Nikita Gergel <fc@altlinux.ru> 1.4.17-alt1
- 1.4.17

* Sun Oct 27 2002 Nikita Gergel <fc@altlinux.ru> 1.4.16-alt2
- syslog-ng.conf patch

* Fri Oct 25 2002 Nikita Gergel <fc@altlinux.ru> 1.4.16-alt1
- 1.4.16

* Fri Oct 11 2002 Stanislav Ievlev <inger@altlinux.ru> 1.4.15-alt3
- security fix

* Thu Sep 19 2002 Stanislav Ievlev <inger@altlinux.ru> 1.4.15-alt2
- rebuild with gcc3

* Sat May 18 2002 Stanislav Ievlev <inger@altlinux.ru> 1.4.15-alt1
- 1.4.15

* Tue Feb 05 2002 Stanislav Ievlev <inger@altlinux.ru> 1.4.14-alt2
- sync with chrooted klogd

* Thu Dec 20 2001 Stanislav Ievlev <inger@altlinux.ru> 1.4.14-alt1
- 1.4.14

* Tue Sep 25 2001 Stanislav Ievlev <inger@altlinux.ru> 1.4.12-alt2
- added PreReq for syslog-common - general package for all syslogs.
- added some documentation

* Fri Jul 27 2001 Stanislav Ievlev <inger@altlinux.ru> 1.4.12-alt1
- 1.4.12

* Tue Jul 24 2001 Stanislav Ievlev <inger@altlinux.ru> 1.4.10-alt1
- Initial release for ALT Linux.

* Wed Jan 17 2001 Lenny Cartier <lenny@mandrakesoft.com> 1.4.10-1mdk
- used srpm from John Johnson <jjohnson@linux-mandrake.com> :
	- Updated syslog-ng to version 1.4.

* Mon Nov 13 2000 Vincent Danen <vdanen@mandrakesoft.com> 1.4.8-2mdk
- specfile cleaning, use macros
- rewrote init file
- wrote proper syslog-ng.conf file based on syslog.conf
- patch so config goes in /etc not /etc/syslog-ng
- syslog-ng goes in /sbin not /usr/sbin

* Wed Nov 8 2000 John Johnson <jjohnson@linux-mandrake.com> 1.4.8-1mdk
- Made Mandrake rpm
