%global import_path github.com/tailscale/tailscale
%define _unpackaged_files_terminate_build 1
%define optflags_lto %nil

Name: tailscale
Version: 1.82.5
Release: alt1

Summary: A mesh VPN that makes it easy to connect your devices, wherever they are.
License: BSD-3-Clause
Group: System/Servers

Url: https://tailscale.com/
Vcs: https://{%import_path}.git
Source0: %name-%version.tar
Source1: %name-vendor.tar

ExclusiveArch:  %go_arches
BuildRequires(pre): rpm-macros-golang
BuildRequires: rpm-build-golang golang
BuildRequires: /proc

%description
Tailscale is a mesh VPN (Virtual Private Network) service that streamlines
connecting devices and services securely across different networks. It enables
encrypted point-to-point connections using the open source WireGuard protocol,
which means only devices on your private network can communicate with each other.

Unlike traditional VPNs, which tunnel all network traffic through a central
gateway server, Tailscale creates a peer-to-peer mesh network
(known as a tailnet). However, you can still use Tailscale like
a traditional VPN by routing all traffic through an exit node.

%prep
%setup -a1
sed -i 's|/etc/default/tailscaled|/etc/sysconfig/tailscaled|' ./cmd/tailscaled/tailscaled.service

%build
export BUILDDIR="$PWD/.gopath"
export IMPORT_PATH="%import_path"
export GOPATH="$BUILDDIR:%go_path"
export TAGS="netgo,builtinassets"
    
export LDFLAGS="-X github.com/tailscale/common/version.Version=%version  \
         -X github.com/prometheus/common/version.Revision=%release \
         -X github.com/prometheus/common/version.Branch=main      \
         -X github.com/prometheus/common/version.BuildDate=$(date -u +%%Y%%m%%d)"

%golang_prepare
%golang_build ./cmd/tailscale
%golang_build ./cmd/tailscaled

%install
export BUILDDIR="$PWD/.gopath"
export IGNORE_SOURCES=1
%golang_install
mkdir %buildroot%_sbindir
mv -vf -- %buildroot%_bindir/tailscaled %buildroot%_sbindir/tailscaled

install -Dm644 cmd/tailscaled/tailscaled.service %buildroot%_unitdir/tailscaled.service
install -Dm644 cmd/tailscaled/tailscaled.defaults %buildroot%_sysconfdir/sysconfig/tailscaled

%post
%systemd_post tailscaled.service

%preun
%systemd_preun tailscaled.service

%files
%_bindir/tailscale
%_sbindir/tailscaled
%_unitdir/tailscaled.service
%_sysconfdir/sysconfig/tailscaled
%doc README.md AUTHORS LICENSE PATENTS

%changelog
* Thu May 01 2025 Semen Fomchenkov <armatik@altlinux.org> 1.82.5-alt1
- Initial build for Sisyphus.
