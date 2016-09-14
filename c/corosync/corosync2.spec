Name: corosync
Summary: The Corosync Cluster Engine and Application Programming Interfaces
Version: 2.4.1
Release: alt1
License: BSD
Group: System/Base
Url: http://corosync.github.io/corosync/

# https://github.com/corosync/corosync.git
Source0: %name-%version.tar
Source1: corosync-init
Source2: corosync-notifyd-init
Source3: corosync-qdevice-init
Source4: corosync-qnetd-init

#fixed systemd units
Source11: corosync.service
Source12: corosync-qdevice.service

Provides: corosync2 = %version-%release
Obsoletes: corosync2 < %version-%release
Requires: lib%name = %version-%release

BuildRequires: doxygen nss-devel libqb-devel libstatgrab-devel libibverbs-devel librdmacm-devel libnet-snmp-devel libdbus-devel systemd-devel libxslt-devel libaugeas-devel
BuildRequires: augeas graphviz libsocket-devel zlib-devel

%define _localstatedir %_var

%description
This package contains the Corosync Cluster Engine Executive, several
default APIs and libraries, default configuration files, and an init
script.

%package -n lib%name
Summary: The Corosync Cluster Engine Libraries
Group: System/Libraries
Conflicts: libcorosync
Provides: libcorosync2 = %version-%release
Obsoletes: libcorosync2 < %version-%release

%description -n lib%name
This package contains corosync libraries.

%package -n lib%name-devel
Summary: The Corosync Cluster Engine Development Kit
Group: Development/C
Requires: lib%name = %version-%release
Provides: libcorosync2-devel = %version-%release
Obsoletes: libcorosync2-devel < %version-%release

%description -n lib%name-devel
This package contains include files and man pages used to develop using
The Corosync Cluster Engine APIs.

%package qdevice
Summary: The Corosync Cluster Engine Qdevice
Group: System/Base
Requires: %name = %version-%release
Requires: nss-utils

%description qdevice
This package contains the Corosync Cluster Engine Qdevice, script for creating
NSS certificates and an init script.

%package qnetd
Summary: The Corosync Cluster Engine Qdevice Network Daemon
Group: System/Base
Requires: nss-utils

%description qnetd
This package contains the Corosync Cluster Engine Qdevice Network Daemon, script for creating
NSS certificates and an init script.

%package cts
Summary: Cluster Test System
Group: System/Libraries
Requires: %name = %version-%release
Provides: corosync2-cts = %version-%release
Obsoletes: corosync2-cts < %version-%release

%description cts
The CTS uses a test driver node(TDN) to drive the execution of the test
software.  The CTS also uses 2 or more test target nodes(TTN) to run the test
cases.  The CTS software requires atleast 3 nodes 1 of which acts as a TDN and
the remaining acting as TTNs.

%prep
%setup

echo %version > .version
#if release version (= tarball)
#in checked-out repository it uses git describe
cp .version .tarball-version
mkdir -p m4

%build
%autoreconf

export ibverbs_CFLAGS=-I/usr/include/infiniband \
export ibverbs_LIBS=-libverbs \
export rdmacm_CFLAGS=-I/usr/include/rdma \
export rdmacm_LIBS=-lrdmacm \

%configure \
	--enable-testagents \
	--enable-watchdog \
	--enable-monitoring \
	--enable-snmp \
	--enable-dbus \
	--enable-rdma \
	--enable-systemd \
	--enable-xmlconf \
	--enable-qdevices \
	--enable-qnetd \
	--enable-augeas \
	--with-systemddir=%_unitdir \
	--with-tmpfilesdir=%_tmpfilesdir \
	--with-initwrappersdir=%_initdir


%make_build

%install
%makeinstall_std
%makeinstall_std -C init

install -p -D -m644 %buildroot%_sysconfdir/corosync/corosync.conf.example %buildroot%_sysconfdir/corosync/corosync.conf

install -p -D -m644 %_builddir/%name-%version/conf/corosync-signals.conf %buildroot/%_sysconfdir/dbus-1/system.d/corosync-signals.conf

#Initscripts
install -p -D -m755 %SOURCE1 %buildroot%_initdir/corosync
install -p -D -m755 %SOURCE2 %buildroot%_initdir/corosync-notifyd
install -p -D -m755 %SOURCE3 %buildroot%_initdir/corosync-qdevice
install -p -D -m755 %SOURCE4 %buildroot%_initdir/corosync-qnetd

#fixed native systemd units
install -p -D -m644 %SOURCE11 %buildroot%_unitdir/corosync.service
install -p -D -m644 %SOURCE12 %buildroot%_unitdir/corosync-qdevice.service

mkdir -p %buildroot%_datadir/corosync/tests/cts
cp cts/corolab.py %buildroot%_datadir/corosync/tests/cts
cp cts/corosync.py %buildroot%_datadir/corosync/tests/cts
cp cts/corotests.py %buildroot%_datadir/corosync/tests/cts


## tree fixup
# drop static libs
rm -f %buildroot%_libdir/*.a
# drop docs and html docs for now
rm -rf %buildroot%_docdir/*

mkdir -p %buildroot%_sysconfdir/sysconfig

# /etc/sysconfig/corosync-notifyd
install -m 644 tools/corosync-notifyd.sysconfig.example %buildroot%_sysconfdir/sysconfig/corosync-notifyd
# /etc/sysconfig/corosync
install -m 644 init/corosync.sysconfig.example %buildroot%_sysconfdir/sysconfig/corosync
# /etc/sysconfig/corosync-qdevice
install -m 644 init/corosync-qdevice.sysconfig.example %buildroot%_sysconfdir/sysconfig/corosync-qdevice
# /etc/sysconfig/corosync-qnetd
install -m 644 init/corosync-qnetd.sysconfig.example %buildroot%_sysconfdir/sysconfig/corosync-qnetd
sed -i -e 's/^#User=/User=/' %buildroot%_unitdir/corosync-qnetd.service
sed -i -e 's/root/coroqnetd/g' %buildroot%_tmpfilesdir/corosync-qnetd.conf
sed -i -e 's/^COROSYNC_QNETD_RUNAS=""$/COROSYNC_QNETD_RUNAS="coroqnetd"/' %buildroot%_sysconfdir/sysconfig/corosync-qnetd

%check
%make check

%pre qnetd
%_sbindir/groupadd -r -f coroqnetd 2> /dev/null ||:
%_sbindir/useradd -r -l -M -g coroqnetd -d /var/empty -s /dev/null -c "User for corosync-qnetd" coroqnetd 2> /dev/null ||:

%post
%post_service corosync
%post_service corosync-notifyd

%post qnetd
%post_service corosync-qnetd

%post qdevice
%post_service corosync-qdevice

%preun
%preun_service corosync
%preun_service corosync-notifyd

%preun qnetd
%preun_service corosync-qnetd

%preun qdevice
%preun_service corosync-qdevice

%files
%doc AUTHORS SECURITY README* LICENSE
%_bindir/*
%exclude %_bindir/*_test_agent
%exclude %_bindir/corosync-qnetd*
%_sbindir/*
%exclude %_sbindir/corosync-qdevice*
%dir %_sysconfdir/corosync
%dir %_sysconfdir/corosync/service.d
%dir %_sysconfdir/corosync/uidgid.d
%config(noreplace) %_sysconfdir/corosync/corosync.conf
%config(noreplace) %_sysconfdir/corosync/corosync.conf.example
%config(noreplace) %_sysconfdir/corosync/corosync.conf.example.udpu
%config(noreplace) %_sysconfdir/corosync/corosync.xml.example
%config(noreplace) %_sysconfdir/sysconfig/corosync-notifyd
%config(noreplace) %_sysconfdir/sysconfig/corosync
%config(noreplace) %_sysconfdir/logrotate.d/corosync
%_unitdir/corosync.service
%_unitdir/corosync-notifyd.service
%_sysconfdir/dbus-1/system.d/corosync-signals.conf
%_initrddir/corosync
%_initrddir/corosync-notifyd
%_datadir/corosync
%_datadir/snmp/mibs/COROSYNC-MIB.txt
%_datadir/augeas/lenses/*
%dir %_localstatedir/lib/corosync
%attr(700, root, root) %_localstatedir/log/cluster
%_man8dir/*
%exclude %_man8dir/*qdevice*
%exclude %_man8dir/*qnetd*
%_man5dir/*

%exclude %_datadir/corosync/tests

%files -n lib%name
%_libdir/*.so.*

%files -n lib%name-devel
%_includedir/corosync
%_libdir/*.so
%_pkgconfigdir/*
%_man3dir/*

%files qdevice
%dir %_sysconfdir/corosync/qdevice
%dir %config(noreplace) %_sysconfdir/corosync/qdevice/net
%dir %_localstatedir/run/corosync-qdevice
%_sbindir/corosync-qdevice*
%config(noreplace) %_sysconfdir/sysconfig/corosync-qdevice
%_unitdir/corosync-qdevice.service
%_initrddir/corosync-qdevice
%_man8dir/*qdevice*

%files qnetd
%dir %config(noreplace) %attr(750, root, coroqnetd) %_sysconfdir/corosync/qnetd
%dir %attr(770, root, coroqnetd) %_localstatedir/run/corosync-qnetd
%_bindir/corosync-qnetd*
%config(noreplace) %_sysconfdir/sysconfig/corosync-qnetd
%_unitdir/corosync-qnetd.service
%_tmpfilesdir/corosync-qnetd.conf
%_initrddir/corosync-qnetd
%_man8dir/*qnetd*

%files cts
%_datadir/corosync/tests
%_bindir/*_test_agent

%changelog
* Wed Sep 14 2016 Alexey Shabalin <shaba@altlinux.ru> 2.4.1-alt1
- 2.4.1
- rename to corosync

* Fri Sep 05 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.3.4-alt1
- Version 2.3.4

* Mon Nov 11 2013 Slava Dubrovskiy <dubrsl@altlinux.org> 2.3.2-alt1
- New version

* Mon Aug 12 2013 Slava Dubrovskiy <dubrsl@altlinux.org> 2.3.1-alt1
- New version

* Tue Feb 19 2013 Slava Dubrovskiy <dubrsl@altlinux.org> 2.3.0-alt1
- New version

* Sun Sep 20 2011 Gleb F-Malinovskiy <glebfm@altlinux.org> 1.4.1-alt1
- Initial build (using Fedora spec)
