%define import_path github.com/spiffe/spire
%define _unpackaged_files_terminate_build 1

Name: spire
Version: 1.15.0
Release: alt1
Summary: The SPIFFE Runtime Environment
License: Apache-2.0
Group: System/Servers
Url: https://github.com/spiffe/spire
Vcs: https://github.com/spiffe/spire.git

Source0: %name-%version.tar
Source1: %name-%version-vendor.tar

ExclusiveArch: %go_arches

BuildRequires(pre): rpm-macros-golang
BuildRequires: rpm-build-golang

%description
%summary.

%package agent
Summary: SPIRE Agent
Group: System/Servers

%description agent
%summary.

%package server
Summary: SPIRE Server
Group: System/Servers

%description server
%summary.

%prep
%setup -a1

%build
export BUILDDIR="$PWD/.build"
export IMPORT_PATH="%import_path"
export GOPATH="$BUILDDIR:%go_path"
export LDFLAGS="-X %import_path/pkg/version.BuildVersion=%version"
%golang_prepare
%golang_build cmd/*

%install
export BUILDDIR="$PWD/.build"
export IGNORE_SOURCES=1
%golang_install

%files agent
%_bindir/%name-agent

%files server
%_bindir/%name-server

%changelog
* Wed May 27 2026 Maxim Slipenko <maks1ms@altlinux.org> 1.15.0-alt1
- New version 1.15.0.

* Fri Oct 24 2025 Maxim Slipenko <maks1ms@altlinux.org> 1.12.4-alt1
- Initial build

