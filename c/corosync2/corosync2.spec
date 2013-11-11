Name: corosync2
Summary: The Corosync Cluster Engine and Application Programming Interfaces
Version: 2.3.2
Release: alt1
License: BSD
Group: System/Base
Url: http://ftp.corosync.org

Source0:%name-%version.tar
Source1: corosync-init
Source2: corosync-notifyd-init
Patch: %name-%version-alt.patch

Conflicts: corosync

BuildRequires: gcc-c++ doxygen nss-devel libqb-devel libstatgrab-devel libibverbs-devel librdmacm-devel libnet-snmp-devel libdbus-devel systemd-devel libxslt-devel libaugeas-devel

%define _localstatedir %_var

%description
This package contains the Corosync Cluster Engine Executive, several
default APIs and libraries, default configuration files, and an init
script.


%package -n lib%name
Summary: The Corosync Cluster Engine Libraries
Group: System/Libraries
Conflicts: libcorosync

%description -n lib%name
This package contains corosync libraries.


%package -n lib%name-devel
Summary: The Corosync Cluster Engine Development Kit
Group: Development/C
Requires: libcorosync2 = %version-%release
#Requires: pkgconfig

%description -n lib%name-devel
This package contains include files and man pages used to develop using
The Corosync Cluster Engine APIs.

%package cts
Summary: Cluster Test System
Group: System/Libraries
Requires: %name = %version-%release augeas pacemaker
BuildArch: noarch

%description cts
The CTS uses a test driver node(TDN) to drive the execution of the test
software.  The CTS also uses 2 or more test target nodes(TTN) to run the test
cases.  The CTS software requires atleast 3 nodes 1 of which acts as a TDN and
the remaining acting as TTNs.

%prep
%setup
%patch -p1

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
	--enable-augeas \
	--with-initwrappersdir=%_initdir \
	--with-systemddir=%_unitdir

%make_build

%install
%makeinstall_std
%makeinstall_std -C init

cp %buildroot%_sysconfdir/corosync/corosync.conf.example %buildroot%_sysconfdir/corosync/corosync.conf

install -p -D -m644 %_builddir/%name-%version/conf/corosync-signals.conf %buildroot/%_sysconfdir/dbus-1/system.d/corosync-signals.conf

#Initscripts
install -p -D -m755 %SOURCE1 %buildroot%_initdir/corosync
install -p -D -m755 %SOURCE2 %buildroot%_initdir/corosync-notifyd

mkdir -p %buildroot%_datadir/corosync/tests/cts
cp cts/corolab.py %buildroot%_datadir/corosync/tests/cts
cp cts/corosync.py %buildroot%_datadir/corosync/tests/cts
cp cts/corotests.py %buildroot%_datadir/corosync/tests/cts


## tree fixup
# drop static libs
rm -f %buildroot%_libdir/*.a
# drop docs and html docs for now
rm -rf %buildroot%_docdir/*

%check
%make check

%post
%post_service corosync
%post_service corosync-notifyd

%preun
%preun_service corosync
%preun_service corosync-notifyd

%files
%doc AUTHORS SECURITY README* TODO LICENSE
%_bindir/*
%_sbindir/*
%dir %_sysconfdir/corosync
%dir %_sysconfdir/corosync/service.d
%dir %_sysconfdir/corosync/uidgid.d
%config(noreplace) %_sysconfdir/corosync/corosync.conf
%config(noreplace) %_sysconfdir/corosync/corosync.conf.example
%config(noreplace) %_sysconfdir/corosync/corosync.conf.example.udpu
%config(noreplace) %_sysconfdir/corosync/corosync.xml.example
%systemd_unitdir/*
%_sysconfdir/dbus-1/system.d/corosync-signals.conf
%_initdir/corosync*
%_datadir/corosync
%_datadir/snmp/mibs/COROSYNC-MIB.txt
%_datadir/augeas/lenses/*
%dir %_localstatedir/lib/corosync
%attr(700, root, root) %_localstatedir/log/cluster
%_mandir/man8/*
%_mandir/man5/*

%exclude %_datadir/corosync/tests

%files -n lib%name
%_libdir/*.so.*

%files -n lib%name-devel
%_includedir/corosync
%_libdir/*.so
%_pkgconfigdir/*
%_mandir/man3/*

%files cts
%_datadir/corosync/tests

%changelog
* Mon Nov 11 2013 Slava Dubrovskiy <dubrsl@altlinux.org> 2.3.2-alt1
- New version

* Mon Aug 12 2013 Slava Dubrovskiy <dubrsl@altlinux.org> 2.3.1-alt1
- New version

* Tue Feb 19 2013 Slava Dubrovskiy <dubrsl@altlinux.org> 2.3.0-alt1
- New version

* Sun Sep 20 2011 Gleb F-Malinovskiy <glebfm@altlinux.org> 1.4.1-alt1
- Initial build (using Fedora spec)
