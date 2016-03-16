Name: iodine
Version: 0.7.0
Release: alt1

Summary: IPv4 tunnel through a DNS server

License: ISC
Group: Networking/Other
Url: http://code.kryo.se/iodine/

Packager: Vladimir D. Seleznev <vseleznv@altlinux.org>
Source: %name-%version.tar.gz
Source1: %name.init
Source2: %{name}d.init
Source3: %name.service
Source4: %{name}d.service
Source5: README.ALT-ru_RU.UTF-8

Requires: %name-common = %EVR
Requires: net-tools

# Automatically added by buildreq on Sat Feb 13 2016
BuildRequires: zlib-devel

%description
iodine lets you tunnel IPv4 data through a DNS server. This can be
usable in different situations where internet access is firewalled, but
DNS queries are allowed.
It runs on Linux, Mac OS X, FreeBSD, NetBSD, OpenBSD and Windows and
needs a TUN/TAP device. The bandwidth is asymmetrical with limited
upstream and up to 1 Mbit/s downstream.

%package client
Summary: IPv4 tunnel through a DNS server (client)
Group: Networking/Other
Requires: %name-common = %EVR
Requires: net-tools

%description client
iodine lets you tunnel IPv4 data through a DNS server. This can be
usable in different situations where internet access is firewalled, but
DNS queries are allowed.
It runs on Linux, Mac OS X, FreeBSD, NetBSD, OpenBSD and Windows and
needs a TUN/TAP device. The bandwidth is asymmetrical with limited
upstream and up to 1 Mbit/s downstream.

(This package contains client files.)

%package common
Summary: IPv4 tunnel through a DNS server (common)
Group: Networking/Other

%description common
iodine lets you tunnel IPv4 data through a DNS server. This can be
usable in different situations where internet access is firewalled, but
DNS queries are allowed.
It runs on Linux, Mac OS X, FreeBSD, NetBSD, OpenBSD and Windows and
needs a TUN/TAP device. The bandwidth is asymmetrical with limited
upstream and up to 1 Mbit/s downstream.

(This package contains common files.)

%package server
Summary: IPv4 tunnel through a DNS server (server)
Group: System/Servers
Requires: %name-common = %EVR
Requires: net-tools

%description server
iodine lets you tunnel IPv4 data through a DNS server. This can be
usable in different situations where internet access is firewalled, but
DNS queries are allowed.
It runs on Linux, Mac OS X, FreeBSD, NetBSD, OpenBSD and Windows and
needs a TUN/TAP device. The bandwidth is asymmetrical with limited
upstream and up to 1 Mbit/s downstream.

(This package contains server files.)

%prep
%setup
cp -- %SOURCE5 README.ALT-ru_RU.UTF-8

%build
export CFLAGS="%optflags"
make

%install
make DESTDIR=%buildroot prefix=%prefix install

pushd %buildroot%_man8dir
for file in iodine.8*; do
	link=`echo $file | sed -e 's/iodine/iodined/'`
	cp $file $link
done
popd

install -pD -m755 %SOURCE1 %buildroot%_initdir/%name
install -pD -m755 %SOURCE2 %buildroot%_initdir/%{name}d
install -pD -m644 %SOURCE3 %buildroot%_unitdir/%name.service
install -pD -m644 %SOURCE4 %buildroot%_unitdir/%{name}d.service

mkdir -p %buildroot%_sysconfdir/sysconfig
cat << __EOF__ > %buildroot%_sysconfdir/sysconfig/iodine
IODINE_NAMESERVER=""
IODINE_TOPDOMAIN="my.domain"
# should be set
IODINE_PASS="password"
IODINE_ARGS="-u _iodine -t /var/empty"
__EOF__

cat << __EOF__ > %buildroot%_sysconfdir/sysconfig/iodined
IODINED_TOPDOMAIN="my.domain"
IODINED_TUNNEL_IP="172.16.1.1/24"
# should be set
IODINED_PASS="password"
IODINED_ARGS="-u _iodine -t /var/empty"
__EOF__

%pre common
%_sbindir/groupadd -r -f _%name 2>/dev/null ||:
%_sbindir/useradd  -r -g _%name -c 'IPv4 tunnel through a DNS' \
         -s /dev/null -d /dev/null _%name 2>/dev/null ||:

%post client
%post_service %name

%post server
%post_service %{name}d

%preun client
%preun_service %name

%preun server
%preun_service %{name}d

%files client
%attr(600, root, root) %config(noreplace) %_sysconfdir/sysconfig/%name
%config %_initdir/%name
%config %_unitdir/%name.service
%_sbindir/%name
%_man8dir/%name.8.*

%files common
%doc README
%doc README.ALT-ru_RU.UTF-8

%files server
%attr(600, root, root) %config(noreplace) %_sysconfdir/sysconfig/%{name}d
%config %_initdir/%{name}d
%config %_unitdir/%{name}d.service
%_sbindir/%{name}d
%_man8dir/%{name}d.8.*

%changelog
* Tue Mar 8 2016 Vladimir D. Seleznev <vseleznv@altlinux.org> 0.7.0-alt1
- Initial build.
