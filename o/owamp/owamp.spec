Name: owamp
Summary: one-way delay tester
Version: 3.5.0
Release: alt2
License: Apache License v2.0
Group: Networking/Other
URL: http://e2epi.internet2.edu/owamp/
Source: %{name}-%{version}.tar.gz
# A Debian source:
Source1: owamp-server.service
Source2: owamp-server.init
Patch0: %name-%version-configure-patch_level.patch
# Debian patches which may be useful and reasonable,
# but not applied (yet), because they might have no actual effect.
Patch2: man.diff
Patch100: owamp-3.4-a.seriy@in-line.ru-jitter-rfc3550.diff
Requires: %name-client, %name-server, %name-doc

BuildPreReq: patchutils
BuildRequires: libI2util-devel
BuildRequires: groff-base

%description
OWAMP is a client/server package that allows one to measure the latency between
hosts. Unlike ping, which can only measure the bidirectional delay, OWAMP
enables you to measure the unidirectional delay between two hosts.

%files


%package client
Summary: one-way delay tester client
Group: Networking/Other
# Needed for owping_conn_opts of owping(1), owfetch(1), owup(1); powstream(1):
Requires: I2util-tools
# Running ntpds (with "synchronized" configuration) are needed for reasonable operation
# on both ends: owamp-server and owamp-client.
# TODO: It also prefers STA_NANO (which our ntpds seem not to be setting...)
Requires: ntp-server
%description client
owamp command line utilities for performing owamp measurements with an owamp
server.

%package server
Summary: one-way delay tester server
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
Summary: one-way delay tester documentation
Group: Networking/Other
BuildArch: noarch
%description doc
The general documentation concerning OWAMP architecture.

# Thrulay and I2Util get installed, but really, shouldn't be instaled.
# Let's see what happens:
%define _unpackaged_files_terminate_build      1

%prep
%setup -q
filterdiff -p1 --exclude I2util <%PATCH0 \
| patch -p1
%patch100 -p2

%build

%autoreconf
%configure --with-I2util=no PATCH_LEVEL=%release
%make_build

%install
%makeinstall
# The upstream and Debian .service files differ only in the path to owampd:
#%{__install} -D -p -m 0644 conf/owampd.service %{buildroot}%{_unitdir}/owamp-server.service
%{__install} -D -p -m 0644 %SOURCE1 %{buildroot}%{_unitdir}/owamp-server.service
# The upstream is too RH-specific; the Debian one should work fine through lsb-init
# (and one our prospective user is Debian-oriented; they patch the script :( ):
#%{__install} -D -p -m 0755 conf/owampd.init %{buildroot}%{_sysconfdir}/rc.d/init.d/owamp-server
%{__install} -D -p -m 0755 %SOURCE2 %{buildroot}%{_initdir}/owamp-server
%{__install} -D -p -m 0755 conf/owampd.limits %{buildroot}%{_sysconfdir}/owamp-server/owamp-server.limits
%{__install} -D -p -m 0755 conf/owampd.rpm.conf %{buildroot}%{_sysconfdir}/owamp-server/owamp-server.conf
%{__install} -D -p -m 0755 conf/owampd.limits %{buildroot}%{_sysconfdir}/owamp-server/owamp-server.limits.default
%{__install} -D -p -m 0755 conf/owampd.rpm.conf %{buildroot}%{_sysconfdir}/owamp-server/owampd.conf.default

# a ghost:
mkdir -p %buildroot%_sysconfdir/%name-server/%name-server.pfs
touch %buildroot%_sysconfdir/%name-server/%name-server.pfs
# a default:
mkdir -p %buildroot%_sysconfdir/default
echo "#DAEMON_ARGS='-c /etc/owamp-server -R /var/run'" >%buildroot%_sysconfdir/default/%name-server
mkdir -p %buildroot%_localstatedir/%name

# A more correct place (like in Debian):
mkdir -p %buildroot%_sbindir
mv -v %buildroot%_bindir/owampd -t %buildroot%_sbindir/
# A test (not packaged in Debian, too):
rm -v %buildroot%_bindir/owtvec
# A static library used (only) to build these tools
# (and not packaged in Debian, too):
rm -v %buildroot%_libdir/lib%name.a

%pre server
# (Borrowed everything from openldap-servers.)
# Take care to only do ownership-changing if we're adding the user.
/usr/sbin/groupadd -rf %name
/usr/sbin/useradd  -rM -c "OWAMP User" -g %name -s /dev/null -d %_localstatedir/%name %name &>/dev/null
if [ -d %_localstatedir/%name ]; then
	chown -R %name:%name %_localstatedir/%name
fi

%post server
%post_service %name-server

%preun server
%preun_service %name-server

%files client
# Like in Debian (except for the docs):
%doc README
%doc LICENSE
%{_bindir}/owfetch
%{_bindir}/owping
%{_bindir}/owstats
%{_bindir}/owup
%{_bindir}/powstream
%{_mandir}/man1/owfetch.1.*
%{_mandir}/man1/owping.1.*
%{_mandir}/man1/owstats.1.*
%{_mandir}/man1/owup.1.*
%{_mandir}/man1/powstream.1.*

%files doc
%doc doc/draft-shalunov-reordering-definition-02.txt
# Extra docs (not packaged in Debian):
%doc doc/*.html doc/*.png doc/*.pdf

%files server
# Mostly like in Debian (except for some compat links):
%doc README
%doc LICENSE
%{_sbindir}/owampd
%{_mandir}/man5/*
%{_mandir}/man8/*
%config(noreplace) %{_sysconfdir}/owamp-server
%ghost %config(noreplace) %{_sysconfdir}/owamp-server/owamp-server.pfs
%{_unitdir}/owamp-server.service
%{_initdir}/owamp-server
# And the unpriviledged dir:
%attr(0750,owamp,owamp) %dir %_localstatedir/%name
# An optional conf for the service:
%config(noreplace) %_sysconfdir/default/%name-server
# BTW, shadow-utils-4.1.4.2-alt8 makes %_sysconfdir/default/ not readable by all? Why?

#%files devel
#%{_libdir}/libbwlib.a
#%{_includedir}/owamp/*

%changelog
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
