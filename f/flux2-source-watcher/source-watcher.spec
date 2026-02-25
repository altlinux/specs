%define prog_name source-watcher
%global import_path github.com/fluxcd/%prog_name

Name: flux2-%prog_name
Version: 2.0.3
Release: alt1
Summary: Container cluster management

Group: System/Configuration/Other
License: Apache-2.0

Url: https://github.com/fluxcd/source-watcher
Source0: %name-%version.tar

ExclusiveArch:  %go_arches
BuildRequires(pre): rpm-build-golang
BuildRequires(pre): golang > 1.25
BuildRequires: /proc

%description
The source-watcher is a GitOps toolkit controller that extends
Flux with advanced source composition and decomposition patterns.

%prep
%setup

%build
export BUILDDIR="$PWD/.build"
export IMPORT_PATH="%import_path"
export GOPATH="$BUILDDIR:%go_path"
%golang_prepare
pushd $BUILDDIR/src/%import_path
%gobuild -o %prog_name ./cmd
popd

%install
export BUILDDIR="$PWD/.build"
mkdir -p %buildroot%_bindir
install -Dm 0755 $BUILDDIR/src/%import_path/%prog_name %buildroot%_bindir/%prog_name

%files
%_bindir/%prog_name
%doc *.md
%doc docs/*

%changelog
* Fri Feb 20 2026 Aleksandr Gamzin <gamzin@altlinux.org> 2.0.3-alt1
- Initial build for Sisyphus.
