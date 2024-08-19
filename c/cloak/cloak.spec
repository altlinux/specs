Name: cloak
Version: 2.9.0
Release: alt1

Summary: Cloak
License: GPL-3.0
Group: System/Servers

Url: https://github.com/cbeuw/Cloak
Packager: Nazarov Denis <nenderus@altlinux.org>

# https://github.com/cbeuw/Cloak/archive/v%version/Cloak-%version.tar.gz
Source0: Cloak-%version.tar
# go mod vendor
Source1: vendor.tar

#BuildRequires: golang
#BuildRequires: python3

# Automatically added by buildreq on Mon Aug 19 2024 (-bi)
# optimized out: debugedit elfutils golang-src libctf-nobfd0 libgpg-error python3-base rpm-build-file sh5
BuildRequires: golang python3

%description
Cloak is a pluggable transport that enhances traditional proxy tools like OpenVPN to evade sophisticated censorship and data discrimination.

Cloak is not a standalone proxy program. Rather, it works by masquerading proxied traffic as normal web browsing activities. In contrast to traditional tools which have very prominent traffic fingerprints and can be blocked by simple filtering rules, it's very difficult to precisely target Cloak with little false positives. This increases the collateral damage to censorship actions as attempts to block Cloak could also damage services the censor state relies on.

To any third party observer, a host running Cloak server is indistinguishable from an innocent web server. Both while passively observing traffic flow to and from the server, as well as while actively probing the behaviours of a Cloak server. This is achieved through the use a series of cryptographic steganography techniques.

Cloak can be used in conjunction with any proxy program that tunnels traffic through TCP or UDP, such as Shadowsocks, OpenVPN and Tor. Multiple proxy servers can be running on the same server host and Cloak server will act as a reverse proxy, bridging clients with their desired proxy end.

Cloak multiplexes traffic through multiple underlying TCP connections which reduces head-of-line blocking and eliminates TCP handshake overhead. This also makes the traffic pattern more similar to real websites.

Cloak provides multi-user support, allowing multiple clients to connect to the proxy server on the same port (443 by default). It also provides traffic management features such as usage credit and bandwidth control. This allows a proxy server to serve multiple users even if the underlying proxy software wasn't designed for multiple users

Cloak also supports tunneling through an intermediary CDN server such as Amazon Cloudfront. Such services are so widely used, attempts to disrupt traffic to them can lead to very high collateral damage for the censor.

%package client
Summary: Cloak client
Group: System/Servers

%description client
Cloak is a pluggable transport that enhances traditional proxy tools like OpenVPN to evade sophisticated censorship and data discrimination.

Cloak is not a standalone proxy program. Rather, it works by masquerading proxied traffic as normal web browsing activities. In contrast to traditional tools which have very prominent traffic fingerprints and can be blocked by simple filtering rules, it's very difficult to precisely target Cloak with little false positives. This increases the collateral damage to censorship actions as attempts to block Cloak could also damage services the censor state relies on.

To any third party observer, a host running Cloak server is indistinguishable from an innocent web server. Both while passively observing traffic flow to and from the server, as well as while actively probing the behaviours of a Cloak server. This is achieved through the use a series of cryptographic steganography techniques.

Cloak can be used in conjunction with any proxy program that tunnels traffic through TCP or UDP, such as Shadowsocks, OpenVPN and Tor. Multiple proxy servers can be running on the same server host and Cloak server will act as a reverse proxy, bridging clients with their desired proxy end.

Cloak multiplexes traffic through multiple underlying TCP connections which reduces head-of-line blocking and eliminates TCP handshake overhead. This also makes the traffic pattern more similar to real websites.

Cloak provides multi-user support, allowing multiple clients to connect to the proxy server on the same port (443 by default). It also provides traffic management features such as usage credit and bandwidth control. This allows a proxy server to serve multiple users even if the underlying proxy software wasn't designed for multiple users

Cloak also supports tunneling through an intermediary CDN server such as Amazon Cloudfront. Such services are so widely used, attempts to disrupt traffic to them can lead to very high collateral damage for the censor.

%package server
Summary: Cloak server
Group: System/Servers

%description server
Cloak is a pluggable transport that enhances traditional proxy tools like OpenVPN to evade sophisticated censorship and data discrimination.

Cloak is not a standalone proxy program. Rather, it works by masquerading proxied traffic as normal web browsing activities. In contrast to traditional tools which have very prominent traffic fingerprints and can be blocked by simple filtering rules, it's very difficult to precisely target Cloak with little false positives. This increases the collateral damage to censorship actions as attempts to block Cloak could also damage services the censor state relies on.

To any third party observer, a host running Cloak server is indistinguishable from an innocent web server. Both while passively observing traffic flow to and from the server, as well as while actively probing the behaviours of a Cloak server. This is achieved through the use a series of cryptographic steganography techniques.

Cloak can be used in conjunction with any proxy program that tunnels traffic through TCP or UDP, such as Shadowsocks, OpenVPN and Tor. Multiple proxy servers can be running on the same server host and Cloak server will act as a reverse proxy, bridging clients with their desired proxy end.

Cloak multiplexes traffic through multiple underlying TCP connections which reduces head-of-line blocking and eliminates TCP handshake overhead. This also makes the traffic pattern more similar to real websites.

Cloak provides multi-user support, allowing multiple clients to connect to the proxy server on the same port (443 by default). It also provides traffic management features such as usage credit and bandwidth control. This allows a proxy server to serve multiple users even if the underlying proxy software wasn't designed for multiple users

Cloak also supports tunneling through an intermediary CDN server such as Amazon Cloudfront. Such services are so widely used, attempts to disrupt traffic to them can lead to very high collateral damage for the censor.

%prep
%setup -n Cloak-%version -a 1

%build
%make_build

%install
%__mkdir_p %buildroot{%_bindir,%_sysconfdir/%name}

%__install -Dp -m0755 build/ck-client %buildroot%_bindir/
%__install -Dp -m0755 build/ck-server %buildroot%_bindir/

%__install -Dp -m0644 example_config/ckclient.json %buildroot%_sysconfdir/%name/
%__install -Dp -m0644 example_config/ckserver.json %buildroot%_sysconfdir/%name/

%files client
%doc README.md
%_bindir/ck-client
%dir %_sysconfdir/%name
%config %_sysconfdir/%name/ckclient.json

%files server
%doc README.md
%_bindir/ck-server
%dir %_sysconfdir/%name
%config %_sysconfdir/%name/ckserver.json

%changelog
* Mon Aug 19 2024 Nazarov Denis <nenderus@altlinux.org> 2.9.0-alt1
- Initial build for ALT Linux
