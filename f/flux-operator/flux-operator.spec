%define import_path github.com/controlplaneio-fluxcd/flux-operator
%define _unpackaged_files_terminate_build 1

Name: flux-operator
Version: 0.30.0
Release: alt1
Summary: Flux Operator is a Kubernetes controller for managing the lifecycle of Flux CD
License: AGPL-3.0-or-later
Group: System/Servers
Url: https://fluxcd.control-plane.io/operator/
Vcs: https://github.com/controlplaneio-fluxcd/flux-operator.git

Source0: %name-%version.tar
Source1: %name-%version-vendor.tar
Patch: %name-%version-%release.patch

ExclusiveArch: %go_arches

BuildRequires(pre): rpm-macros-golang
BuildRequires: rpm-build-golang kustomize

%description
%summary.

%package cli
Summary: Flux Operator CLI
Group: System/Servers

%description cli
%summary.

%package manifests
Summary: Flux Operator Manifests
Group: System/Servers
BuildArch: noarch

%description manifests
%summary.

%prep
%setup -a1
%autopatch -p1

%build
export BUILDDIR="$PWD/.build"
export IMPORT_PATH="%import_path"
export GOPATH="$BUILDDIR:%go_path"
export LDFLAGS="-X main.VERSION=%version"
export CGO_ENABLED=0
export GOFIPS140=latest
%golang_prepare
%golang_build cmd/operator cmd/cli

%install
export BUILDDIR="$PWD/.build"
export IGNORE_SOURCES=1
%golang_install
mv -f %buildroot%_bindir/operator %buildroot%_bindir/%name-server
mv -f %buildroot%_bindir/cli %buildroot%_bindir/%name

mkdir -p %buildroot%_datadir/%name-manifests/{flux-operator,flux-operator-mcp}

cp -r ./config/data/* %buildroot%_datadir/%name-manifests
kustomize build config/default > %buildroot%_datadir/%name-manifests/flux-operator/install.yaml
kustomize build config/mcp > %buildroot%_datadir/%name-manifests/flux-operator-mcp/install.yaml

%files
%doc LICENSE README.md
%_bindir/%name-server

%files cli
%doc LICENSE cmd/cli/README.md
%_bindir/%name

%files manifests
%_datadir/%name-manifests

%changelog
* Tue Nov 11 2025 Maxim Slipenko <maks1ms@altlinux.org> 0.30.0-alt1
- Initial build

