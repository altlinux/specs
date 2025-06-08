%define git_short_commit 4127937
%define import_path github.com/xjasonlyu/tun2socks

Name: tun2socks
Version: 2.6.0
Release: alt1

Summary: %name - powered by gVisor TCP/IP stack
License: MIT
Group: System/Servers

Url: https://github.com/xjasonlyu/%name
Packager: Nazarov Denis <nenderus@altlinux.org>

# https://github.com/xjasonlyu/%name/archive/v%version/%name-%version.tar.gz
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
    -X github.com/xjasonlyu/tun2socks/v2/internal/version.Version=%version \
    -X github.com/xjasonlyu/tun2socks/v2/internal/version.GitCommit=%git_short_commit \
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
* Sun Jun 08 2025 Nazarov Denis <nenderus@altlinux.org> 2.6.0-alt1
- Version 2.6.0

* Wed Aug 21 2024 Nazarov Denis <nenderus@altlinux.org> 2.5.2-alt0.gitc8c08cf
 - Initial build for ALT Linux
