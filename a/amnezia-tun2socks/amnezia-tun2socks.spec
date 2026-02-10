%define git_short_commit 9fabebb
%define import_path github.com/amnezia-vpn/amnezia-tun2socks

Name: amnezia-tun2socks
Version: 2.5.4
Release: alt1

Summary: tun2socks - powered by gVisor TCP/IP stack
License: MIT
Group: System/Servers

Url: https://github.com/amnezia-vpn/%name
Vcs: https://github.com/amnezia-vpn/%name
Packager: Nazarov Denis <nenderus@altlinux.org>

# https://github.com/amnezia-vpn/%name/archive/v%version/%name-%version.tar.gz
Source0: %name-%version.tar
# go mod vendor
Source1: vendor.tar

BuildRequires: python3
BuildRequires: rpm-build-golang

%description
Features:
 - Proxy Everything: Handle all network traffic of any internet programs sent by the device through a proxy.
 - Proxy Protocols: HTTP/Socks4/Socks5/Shadowsocks with authentication support for remote connections.
 - Run Everywhere: Linux/macOS/Windows/FreeBSD/OpenBSD multi-platform support with specific optimization.
 - Gateway Mode: Act as a Layer 3 gateway to handle network traffic from other devices on the same network.
 - Full IPv6 Support: All functions work in IPv6, tunnel IPv4 connections through IPv6 proxy and vice versa.
 - Network Stack: Powered by the user-space TCP/IP stack from Google container application kernel gVisor.

%prep
%setup -a 1

%build
export BUILDDIR="$PWD/.build"
export IMPORT_PATH="%import_path"
export GOPATH="$BUILDDIR:%go_path"
export LDFLAGS="\
    -X github.com/amnezia-vpn/amnezia-tun2socks/v2/internal/version.Version=v%version \
    -X github.com/amnezia-vpn/amnezia-tun2socks/v2/internal/version.GitCommit=%git_short_commit \
    $LDFLAGS \
"

%golang_prepare

pushd .build/src/%import_path
%golang_build .
popd

%install
export BUILDDIR="$PWD/.build"
export IGNORE_SOURCES=1

%golang_install

%files
%doc README.md
%_bindir/%name

%changelog
* Tue Feb 10 2026 Nazarov Denis <nenderus@altlinux.org> 2.5.4-alt1
- Initial build for ALT Linux
