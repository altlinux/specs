%define import_path github.com/cilium/hubble-ui/backend
%define _unpackaged_files_terminate_build 1
%define installdir %webserver_webappsdir/%name

Name: hubble-ui
Version: 0.13.5
Release: alt1
Summary: Hubble UI is an open-source user interface for Cilium Hubble
License: Apache-2.0
Group: System/Servers
Url: https://github.com/cilium/hubble-ui
Vcs: https://github.com/cilium/hubble-ui.git

Source0: %name-%version.tar
Source1: %name-%version-node_modules.tar

ExclusiveArch: %go_arches

BuildRequires(pre): rpm-macros-webserver-common rpm-macros-golang
BuildRequires: npm rpm-build-golang

%description
%summary.

%package frontend
Summary: Hubble UI frontend
BuildArch: noarch
Group: System/Servers

%description frontend
%summary.

%package backend
Summary: Hubble UI backend
Group: System/Servers

%description backend
%summary.

%prep
%setup -a1

%build
NODE_ENV=production npm run build

export BUILDDIR="$PWD/.build"
export IMPORT_PATH="%import_path"
export GOPATH="$BUILDDIR:%go_path"
%golang_prepare
%golang_build backend

%install
mkdir -p %buildroot%installdir
cp -rp server/public/* %buildroot%installdir/

export BUILDDIR="$PWD/.build"
export IGNORE_SOURCES=1
%golang_install
mv -f %buildroot%_bindir/backend %buildroot%_bindir/%name-backend

%files frontend
%installdir

%files backend
%_bindir/%name-backend

%changelog
* Wed Apr 29 2026 Nadezhda Fedorova <fedor@altlinux.org> 0.13.5-alt1
- 0.13.3 -> 0.13.5.

* Thu Oct 30 2025 Maxim Slipenko <maks1ms@altlinux.org> 0.13.3-alt1
- Initial build.
