%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1
%global import_path github.com/Diniboy1123/usque

Name: usque
Version: 4.2.1
Release: alt1
Summary: Open-source reimplementation of the Cloudflare WARP client's MASQUE protocol
License: MIT
Group: Networking/Remote access

Url: https://github.com/Diniboy1123/usque
Vcs: https://github.com/Diniboy1123/usque

ExclusiveArch: %go_arches

BuildRequires(pre): rpm-build-golang
BuildRequires: /proc

Source0: %name-%version.tar
Source1: %name-vendor.tar
Source2: %name.service
Source3: %name.sysconfig

%description
Usque is an open-source reimplementation of the Cloudflare WARP client's MASQUE
mode. It leverages the Connect-IP (RFC 9484) protocol and comes with many
operation modes including a native tunnel, SOCKS5 and HTTP proxies, and faster
TCP-only L4 proxy variants.

%prep
%setup -a1

export CGO_CFLAGS=$CFLAGS
export BUILDDIR="$PWD/.gopath"
export IMPORT_PATH="%import_path"
export GOPATH="$BUILDDIR:%go_path"
export GOFLAGS="-mod=vendor"
export GOROOT="%_libexecdir/golang"

%golang_prepare
pushd .gopath/src/%import_path
%golang_build .
popd

%install
export BUILDDIR="$PWD/.gopath"
export IMPORT_PATH="%import_path"
export GOPATH="$BUILDDIR:%go_path:$PWD"
export RELEASE_VERSION=v%version
export RELEASE_NUMBER=%version

pushd $BUILDDIR
mkdir -p %buildroot{%_unitdir,%_sbindir,%_sysconfdir/%name,%_sysconfdir/sysconfig}
touch %buildroot%_sysconfdir/%name/config.json
install -pm755 bin/%name %buildroot%_sbindir/
install -pm644 %SOURCE2 %buildroot%_unitdir/
install -pm644 %SOURCE3 %buildroot%_sysconfdir/sysconfig/%name

%files
%doc *.md
%attr(700,root,root) %_sysconfdir/%name
%config(noreplace) %_sysconfdir/sysconfig/%name
%ghost %attr(600,root,root) %config(noreplace) %_sysconfdir/%name/config.json
%_unitdir/%name.service
%_sbindir/%name

%changelog
* Fri Oct 30 2026 L.A. Kostis <lakostis@altlinux.ru> 4.2.1-alt1
- Initial build for ALTLinux.
