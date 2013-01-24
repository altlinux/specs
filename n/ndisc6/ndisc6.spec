Name: ndisc6
Version: 1.0.2
Release: alt2.git20121003

Summary: IPv6 diagnostic tools
License: %gpl2plus
Group: System/Configuration/Networking

URL: http://www.remlab.net/ndisc6/
Source: %name-%version.tar
Source1: rdnssd.init
Source2: rdnssd.tmpfiles
Source3: rdnssd.service
Patch: %name-%version-%release.patch

BuildRequires(pre): rpm-build-licenses

%description
This package gathers a few diagnostic tools for IPv6 networks:
 - ndisc6, which performs ICMPv6 Neighbor Discovery in userland,
 - rdisc6, which performs ICMPv6 Router Discovery in userland,
 - rltraceroute6, yet another IPv6 implementation of traceroute,
 - tcptraceroute6, a TCP/IPv6-based traceroute implementation,
 - tracert6, a ICMPv6 Echo Request based traceroute,
 - tcpspray6, a TCP/IP Discard/Echo bandwidth metter.


%package -n rdnssd
Summary: Recursive DNS Servers discovery Daemon
Group: System/Configuration/Networking

%description -n rdnssd
rdnssd autoconfigures the list of DNS servers through slateless IPv6
autoconfiguration (RFC5006).

%prep
%setup
%patch -p1

%build
ln -s %_datadir/gettext/intl/gettext.h include/gettext.h
%autoreconf
CFLAGS="%optflags -fno-strict-aliasing" \
%configure \
	--localstatedir=%_var \
	--disable-suid-install

%make_build

%install
%makeinstall_std
%find_lang %name
touch %buildroot/%_runtimedir/rdnssd/resolv.conf
install -Dm0755 %SOURCE1 %buildroot%_initdir/rdnssd
install -Dm0644 %SOURCE2 %buildroot%_sysconfdir/tmpfiles.d/rdnssd.conf
install -Dm0644 %SOURCE3 %buildroot%systemd_unitdir/rdnssd.service

%pre -n rdnssd
groupadd -r -f rdnssd
useradd -r -g rdnssd -d %_runtimedir/rdnssd -s /dev/null -N rdnssd >/dev/null 2>&1 ||:

%post -n rdnssd
%post_service rdnssd

%preun -n rdnssd
%preun_service rdnssd

%files -f %name.lang
%doc NEWS README
%_sbindir/*
%_bindir/*
%_man1dir/*
%_man8dir/*
%exclude %_sbindir/rdnssd
%exclude %_man8dir/rdnssd.8.*

%files -n rdnssd
%_initdir/rdnssd
%_sysconfdir/tmpfiles.d/rdnssd.conf
%systemd_unitdir/rdnssd.service
%_sysconfdir/rdnssd
%_sbindir/rdnssd
%_man8dir/rdnssd.8.*
%attr(755,rdnssd,rdnssd) %dir %_runtimedir/rdnssd
%ghost %_runtimedir/rdnssd/resolv.conf

%changelog
* Thu Jan 24 2013 Mikhail Efremov <sem@altlinux.org> 1.0.2-alt2.git20121003
- Added rdnssd.service for systemd.
- Fix owner of /var/run/rdnssd directory (closes: #28430).

* Fri Oct 12 2012 Mikhail Efremov <sem@altlinux.org> 1.0.2-alt1.git20121003
- Updated from upstream git.

* Tue Jul 17 2012 Mikhail Efremov <sem@altlinux.org> 1.0.2-alt1.git20120603
- rdnssd: Add resolvconf support.
- Initial build.

