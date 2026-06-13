%define _unpackaged_files_terminate_build 1
%def_with check

Name: wireproxy
Version: 1.1.2
Release: alt1

Summary: Wireguard client that exposes itself as a socks5 proxy
License: ISC
Group: System/Configuration/Other
VCS: https://github.com/windtf/wireproxy
Url: https://github.com/windtf/wireproxy

Source0: %name-%version.tar
Source1: %name-%version-vendor.tar

BuildRequires(pre): rpm-build-golang

%description
wireproxy is  a completely  userspace application that  connects to  a wireguard
peer, and  exposes a socks5/http  proxy or tunnels on  the machine. This  can be
useful if you need  to connect to certain sites via a  wireguard peer, but can't
be bothered to setup a new network interface for whatever reasons.

%prep
%setup -a1

sed -i 's|/opt/wireproxy/wireproxy|%_bindir/wireproxy|' systemd/wireproxy.service

%build
LDFLAGS="-w -X 'main.version=%version-%release'"
%gobuild ./cmd/wireproxy

%install
install -Dpm 755 ./wireproxy %buildroot%_bindir/wireproxy
install -Dpm 644 systemd/wireproxy.service %buildroot%_unitdir/wireproxy.service

install -Dpm 600 /dev/null  %buildroot%_sysconfdir/wireproxy.conf

cp -f systemd/README.md systemd/README.systemd.md

%check
%gotest

%files
%doc LICENSE README.md UseWithVPN.md systemd/README.systemd.md
%_bindir/wireproxy
%_unitdir/wireproxy.service
%ghost %config(noreplace) %attr(600,root,root) %_sysconfdir/wireproxy.conf

%changelog
* Fri Jun 12 2026 Egor Ignatov <egori@altlinux.org> 1.1.2-alt1
- First build for ALT.
