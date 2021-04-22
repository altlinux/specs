%define _unpackaged_files_terminate_build 1

Name: owamp
Version: 4.3.4
Release: alt2
Summary: A tool for performing one-way or two-way active measurements

License: Apache-2.0
Group: Networking/Other
Url: http://e2epi.internet2.edu/owamp/
# git: https://github.com/perfsonar/owamp

Source: %name-%version.tar

Patch0: owamp-alt-daemon-path.patch
Patch1: owamp-alt-datadir.patch

Requires: %name-client, %name-server, %name-doc

BuildRequires: libI2util-devel
BuildRequires: groff-base

%description
OWAMP is a client/server package that allows one to measure the latency between
hosts. Unlike ping, which can only measure the bidirectional delay, OWAMP
enables you to measure the unidirectional delay between two hosts.

%package client
Summary: Client for performing one-way or two-way active measurements
Group: Networking/Other
# Needed for owping_conn_opts of owping(1), owfetch(1), owup(1); powstream(1):a
Requires: I2util-tools
# Running ntpds (with "synchronized" configuration) are needed for reasonable operation
# on both ends: owamp-server and owamp-client.
# TODO: It also prefers STA_NANO (which our ntpds seem not to be setting...)
Requires: ntp-server
%description client
owamp command line utilities for performing owamp measurements with an owamp
server.

%package server
Summary: Server for performing one-way or two-way active measurements
Group: Networking/Other
# Needed for owampd.pfs(5):
Requires: I2util-tools
# Requires the Debian shell command/function: log_daemon_msg:
Requires: lsb-init >= 4.0-alt4
# Running ntpds (with "synchronized" configuration) are needed for reasonable operation
# on both ends: owamp-server and owamp-client.
# TODO: It also prefers STA_NANO (which our ntpds seem not to be setting...)
Requires: ntp-server
%description server
owamp server

#%package devel
#Group: Development/Libraries
#Summary: owamp library headers
#%description devel
#This package includes header files, and static link libraries for building
#applications that use the owamp library.

%package doc
Summary: Documentation for one-way and two-way delay tester
Group: Networking/Other
BuildArch: noarch
%description doc
The general documentation concerning OWAMP architecture.

%prep
%setup
%patch0 -p1
%patch1 -p1

%build
%autoreconf
%configure --with-I2util=no PATCH_LEVEL=%release
%make_build

%install
%makeinstall

%__install -D -p -m 0644 conf/owampd.service %buildroot%_unitdir/owamp-server.service
%__install -D -p -m 0755 conf/owampd.init %buildroot%_initdir/owamp-server
%__install -D -p -m 0755 conf/owampd.limits %buildroot%_sysconfdir/owamp-server/owamp-server.limits
%__install -D -p -m 0755 conf/owampd.rpm.conf %buildroot%_sysconfdir/owamp-server/owamp-server.conf
%__install -D -p -m 0755 conf/owampd.limits %buildroot%_sysconfdir/owamp-server/owamp-server.limits.default
%__install -D -p -m 0755 conf/owampd.rpm.conf %buildroot%_sysconfdir/owamp-server/owampd.conf.default

%__install -D -p -m 0644 conf/twampd.service %buildroot%_unitdir/twamp-server.service
%__install -D -p -m 0755 conf/twampd.init %buildroot%_initdir/twamp-server
%__install -D -p -m 0755 conf/twampd.limits %buildroot%_sysconfdir/twamp-server/twamp-server.limits
%__install -D -p -m 0755 conf/twampd.rpm.conf %buildroot%_sysconfdir/twamp-server/twamp-server.conf
%__install -D -p -m 0755 conf/twampd.limits %buildroot%_sysconfdir/twamp-server/twamp-server.limits.default
%__install -D -p -m 0755 conf/twampd.rpm.conf %buildroot%_sysconfdir/twamp-server/twampd.conf.default

# a ghost:
mkdir -p %buildroot%_sysconfdir/owamp-server/
touch %buildroot%_sysconfdir/owamp-server/owamp-server.pfs

mkdir -p %buildroot%_sysconfdir/twamp-server/
touch %buildroot%_sysconfdir/twamp-server/twamp-server.pfs

# a default:
mkdir -p %buildroot%_sysconfdir/default
echo "#DAEMON_ARGS='-c /etc/owamp-server -R /var/run'" >%buildroot%_sysconfdir/default/owamp-server
echo "#DAEMON_ARGS='-c /etc/twamp-server -R /var/run'" >%buildroot%_sysconfdir/default/twamp-server
mkdir -p %buildroot%_localstatedir/owamp
mkdir -p %buildroot%_localstatedir/twamp

# Move daemons to sbin:
mkdir -p %buildroot%_sbindir
mv -v %buildroot%_bindir/owampd -t %buildroot%_sbindir/
mv -v %buildroot%_bindir/twampd -t %buildroot%_sbindir/

# A static library used (only) to build these tools
rm -v %buildroot%_libdir/lib%name.a

%pre server
/usr/sbin/groupadd -rf owamp
/usr/sbin/groupadd -rf twamp

/usr/sbin/useradd  -rM -c "OWAMP User" -g owamp -s /dev/null -d %_localstatedir/owamp owamp &>/dev/null
/usr/sbin/useradd  -rM -c "TWAMP User" -g twamp -s /dev/null -d %_localstatedir/twamp twamp &>/dev/null
if [ -d %_localstatedir/owamp ]; then
	chown -R owamp:owamp %_localstatedir/owamp
fi

if [ -d %_localstatedir/twamp ]; then
	chown -R twamp:twamp %_localstatedir/twamp
fi


%post server
%post_service owamp-server
%post_service twamp-server

%preun server
%preun_service owamp-server
%preun_service twamp-server

%files

%files client
%doc README
%doc LICENSE
%_bindir/owfetch
%_bindir/owping
%_bindir/owstats
%_bindir/owup
%_bindir/powstream
%_bindir/twping
%_mandir/man1/owfetch.1.*
%_mandir/man1/owping.1.*
%_mandir/man1/owstats.1.*
%_mandir/man1/owup.1.*
%_mandir/man1/powstream.1.*
%_mandir/man1/twping.1.*

%files doc
%doc doc/draft-shalunov-reordering-definition-02.txt
%doc doc/*.html doc/*.png doc/*.pdf

%files server
%doc README
%doc LICENSE
%_sbindir/owampd
%_sbindir/twampd
%_mandir/man5/*
%_mandir/man8/*
%config(noreplace) %_sysconfdir/owamp-server
%config(noreplace) %_sysconfdir/twamp-server
%exclude %_sysconfdir/owamp-server/owamp-server.pfs
%exclude %_sysconfdir/twamp-server/twamp-server.pfs
%_unitdir/*
%_initdir/*
%ghost %config(noreplace) %_sysconfdir/owamp-server/owamp-server.pfs
%ghost %config(noreplace) %_sysconfdir/twamp-server/twamp-server.pfs
# And the unpriviledged dir:
%attr(0750,owamp,owamp) %dir %_localstatedir/owamp
%attr(0750,twamp,twamp) %dir %_localstatedir/twamp
# An optional conf for the service:
%config(noreplace) %_sysconfdir/default/owamp-server
%config(noreplace) %_sysconfdir/default/twamp-server

#%files devel
#%_libdir/libbwlib.a
#%_includedir/owamp/*

%changelog
* Thu Apr 22 2021 Egor Ignatov <egori@altlinux.org> 4.3.4-alt2
- add %files section to create owamp packagep

* Wed Apr 21 2021 Egor Ignatov <egori@altlinux.org> 4.3.4-alt1
- new version
- cleanup spec and .gear/rules

* Thu Oct  6 2016 Ivan Zakharyaschev <imz@altlinux.org> 3.5.0-alt2
- Running ntpds (with "synchronized" configuration) are needed for
  reasonable operation on both ends: owamp-server and owamp-client.
  TODO: OWAMP also prefers STA_NANO (which our ntpds seem not to be setting...)

* Fri Sep 23 2016 Ivan Zakharyaschev <imz@altlinux.org> 3.5.0-alt1
- Initial build for ALT Sisyphus
- RFC3550 jitter calculations for owping
  (received from Alexey Seriy a dot seriy at in-line ru)

* Thu Mar 26 2009 aaron@internet2.edu 1.0-4
- Make upgrading work more seamlessly

* Thu Mar 26 2009 aaron@internet2.edu 1.0-3
- Make sure that /var/lib/owamp is created on install

* Fri Feb 02 2009 aaron@internet2.edu 1.0-2
- Fix the example owampd.limits location

* Fri Aug 22 2008 aaron@internet2.edu 1.0-1
- Initial RPM
