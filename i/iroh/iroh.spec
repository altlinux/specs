%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1

%define iroh_relay_user _iroh-relay
%define iroh_relay_group _iroh-relay
%define iroh_relay_home %_localstatedir/iroh-relay/

%define iroh_dns_server_user _iroh-dns-server
%define iroh_dns_server_group _iroh-dns-server
%define iroh_dns_server_home %_localstatedir/iroh-dns/

Name: iroh
Version: 1.0.0
Release: alt1

Summary: IP addresses break, dial keys instead. Modular networking stack in Rust
License: Apache-2.0 or MIT
Group: Networking/Other
Url: https://www.iroh.computer/
Vcs: https://github.com/n0-computer/iroh.git

Source: %name-%version.tar
Source1: vendor.tar
Source2: conf.tar

# .cargo/config.toml forces use of cross-compiler on aarch64.
Patch: iroh-1.0.0-alt-build_aarch64_natively.patch

BuildRequires(pre): rpm-build-rust
BuildRequires: clang

%description
Iroh gives you an API for dialing by public key. You say "connect to
that phone", iroh will find & maintain the fastest connection for you,
regardless of where it is.

Hole-punching:
The fastest route is a direct connection, so if necessary, iroh tries
to hole-punch. Should this fail, it can fall back to an open ecosystem
of public relay servers. To ensure these connections are as fast as
possible, we continuously measure iroh.

Built on QUIC:
Iroh uses noq to establish QUIC connections between endpoints. This way
you get authenticated encryption, concurrent streams with stream
priorities, a datagram transport and avoid head-of-line-blocking out of
the box.

%package common
Summary: Common files and directories for iroh
Group: Networking/Other
BuildArch: noarch

%description common
%summary.

%package relay
Summary: A fully-fledged iroh relay server over HTTP or HTTPS
License: (Apache-2.0 or MIT) and BSD-3-Clause
Group: Networking/Other
Requires: %name-common

%description relay
A fully-fledged relay server over HTTP or HTTPS. Optionally will also
expose a QAD endpoint and metrics.

%package dns-server
Summary: A server that functions as a pkarr relay and DNS server
Group: Networking/Other
Requires: %name-common

%description dns-server
The server will expose the following services:

1. A DNS server listening on UDP and TCP for DNS queries
2. A HTTP and/or HTTPS server which provides the following routes:
      /pkarr: GET and PUT for pkarr signed packets
      /dns-query: Answer DNS queries over DNS-over-HTTPS

All received and valid pkarr signed packets will be served over DNS. The pkarr packet origin will be appended with the origin as configured by this server.

%prep
%setup -a1 -a2
%autopatch -p2
# .cargo/config.toml misses trailing newline
echo >> .cargo/config.toml
%rust_prep

%build
export RUSTFLAGS="-C debuginfo=full"
%rust_build --bin iroh-dns-server --bin iroh-relay -F server

%install
%rust_install iroh-dns-server iroh-relay

mkdir -pv %buildroot{"%_sysconfdir/iroh/","%_unitdir/","%iroh_relay_home","%iroh_dns_server_home"}
install -m644 conf/iroh-dns-server.toml conf/iroh-relay.toml "%buildroot%_sysconfdir/iroh/"
install -m644 conf/iroh-dns-server.service conf/iroh-relay.service "%buildroot%_unitdir/"

%pre relay
groupadd -r -f "%iroh_relay_group" 2>/dev/null || :
useradd -r -g "%iroh_relay_group" -c "Iroh Relay Service User" -M -d "%iroh_relay_home" -s /dev/null "%iroh_relay_user" > /dev/null 2>&1 ||:

%post relay
%post_service iroh-relay

%preun relay
%preun_service iroh-relay

%pre dns-server
groupadd -r -f "%iroh_dns_server_group" 2>/dev/null || :
useradd -r -g "%iroh_dns_server_group" -c "Iroh DNS Service User" -M -d "%iroh_dns_server_home" -s /dev/null "%iroh_dns_server_user" > /dev/null 2>&1 ||:

%post dns-server
%post_service iroh-dns-server

%preun dns-server
%preun_service iroh-dns-server

%files common
%dir %_sysconfdir/iroh/

%files relay
%doc LICENSE-MIT iroh-relay/LICENSE-BSD3 iroh-relay/README.md
%_bindir/iroh-relay
%config(noreplace) %_sysconfdir/iroh/iroh-relay.toml
%config %_unitdir/iroh-relay.service
%dir %attr(0770,root,%iroh_relay_group) %iroh_relay_home

%files dns-server
%doc LICENSE-MIT iroh-dns-server/README.md
%_bindir/iroh-dns-server
%config(noreplace) %_sysconfdir/iroh/iroh-dns-server.toml
%config %_unitdir/iroh-dns-server.service
%dir %attr(0770,root,%iroh_dns_server_group) %iroh_dns_server_home

%changelog
* Wed Jun 17 2026 Sergey Zhidkih <rx1513@altlinux.org> 1.0.0-alt1
- Initial build.
