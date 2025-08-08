%global import_path github.com/shadowsocks/v2ray-plugin

# git rev-list --count v%version..master
%define commit_count 5
# git rev-parse --short master
%define commit_hash e9af1cdd2549

Name: v2ray-plugin
Version: 1.3.2
Release: alt1.%commit_count.%commit_hash

Summary: A SIP003 plugin based on v2ray
License: MIT
Group: Security/Networking
Url: https://github.com/shadowsocks/v2ray-plugin
Vcs: https://github.com/shadowsocks/v2ray-plugin

Source: %name-%version.tar
Source1: vendor.tar

Patch: master-snapshot.patch

BuildRequires(pre): rpm-build-golang
BuildRequires: golang

%description
Yet another SIP003 plugin for shadowsocks, based on v2ray

%prep
%setup -a 1
%patch -p1

%build
export BUILDDIR="$PWD/.build"
export IMPORT_PATH="%import_path"
export GOPATH="$BUILDDIR:%go_path"

%golang_prepare

cd .build/src/%import_path
%golang_build .

%install
export BUILDDIR="$PWD/.build"
export IGNORE_SOURCES=1

%golang_install

%files
%doc *.md
%_bindir/v2ray-plugin

%changelog
* Fri Aug 08 2025 Alexander Stepchenko <geochip@altlinux.org> 1.3.2-alt1.5.e9af1cdd2549
- Initial build for ALT
