%define _unpackaged_files_terminate_build 1
%global import_path github.com/sagernet/sing-box

Name: sing-box
Version: 1.14.3
Release: alt1
Summary: The universal proxy platform.
License: GPL-3.0-or-later
Group: System/Servers
Url: https://sing-box.sagernet.org/
VCS: https://github.com/SagerNet/sing-box
ExclusiveArch: %go_arches

Source: %name-%version.tar
Source1: vendor.tar

BuildRequires(pre): rpm-macros-golang
BuildRequires: rpm-build-golang

%description
%summary.

%prep
%setup -a1

%build
export DEFAULT_TAGS=$(cat release/DEFAULT_BUILD_TAGS_OTHERS)
export DEFAULT_LDFLAGS=$(cat release/LDFLAGS)
# singbox-lx features
export LX_TAGS="with_xhttp,with_awg"

export BUILDDIR=$PWD/.build
export IMPORT_PATH=%import_path
export GOPATH=$BUILDDIR:%go_path
export TAGS="$DEFAULT_TAGS,$LX_TAGS"
export LDFLAGS="-X github.com/sagernet/sing-box/constant.Version=%version $DEFAULT_LDFLAGS"

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
* Sun Oct 11 2026 Vasiliy Doylov <neko@altlinux.org> 1.14.3-alt1
- New version.
- Add sing-box-lx features.

* Tue Mar 24 2026 Vasiliy Doylov <neko@altlinux.org> 1.13.3-alt1
- Initial build for ALT.
