%define _unpackaged_files_terminate_build 1
%global import_path github.com/sagernet/sing-box

Name: sing-box
Version: 1.13.3
Release: alt1
Summary: The universal proxy platform.
License: GPL-3.0-or-later
Group: System/Servers
Url: https://sing-box.sagernet.org/
VCS: https://github.com/SagerNet/sing-box
ExclusiveArch: %go_arches

Source: %name-%version.tar

BuildRequires(pre): rpm-macros-golang
BuildRequires: rpm-build-golang

%description
%summary.

%prep
%setup

%build
export BUILDDIR=$PWD/.build
export IMPORT_PATH=%import_path
export GOPATH=$BUILDDIR:%go_path
export LDFLAGS="-X github.com/sagernet/sing-box/constant.Version=%version -checklinkname=0"
export TAGS="with_gvisor,with_quic,with_dhcp,with_wireguard,with_utls,with_acme,with_clash_api,with_tailscale,with_ccm,with_ocm,badlinkname,tfogo_checklinkname0"
%golang_prepare
%golang_build cmd/sing-box


%install
export BUILDDIR="$PWD/.build"
export GOPATH="%go_path"
export IGNORE_SOURCES=1
%golang_install

%files
%_bindir/sing-box
%doc README.md

%changelog
* Tue Mar 24 2026 Vasiliy Doylov <neko@altlinux.org> 1.13.3-alt1
- Initial build for ALT.
