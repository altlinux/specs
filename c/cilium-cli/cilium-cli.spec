%global import_path github.com/cilium/cilium-cli
%global _unpackaged_files_terminate_build 1

Name:    cilium-cli
Version: 0.19.2
Release: alt1

Summary: CLI to install, manage & troubleshoot Kubernetes clusters running Cilium
License: Apache-2.0
Group:   Other
Url:     https://github.com/cilium/cilium-cli

Source: %name-%version.tar

BuildRequires(pre):  rpm-macros-golang
BuildRequires:  rpm-build-golang
BuildRequires:  golang
BuildRequires:  /proc

%description
%summary

%prep
%setup

%build
export BUILDDIR="$PWD/.build"
export GOFLAGS="-mod=vendor"
export GOBIN="$BUILDDIR/bin"
export IMPORT_PATH="%import_path"
export GOPATH="$BUILDDIR:%go_path"
export LDFLAGS="-X github.com/cilium/cilium/cilium-cli/defaults.CLIVersion=v%version"

%golang_prepare

mkdir $GOBIN
pushd $BUILDDIR/src/%import_path
%golang_build cmd/cilium/
popd

%install
export BUILDDIR="$PWD/.build"
export IGNORE_SOURCES=1

%golang_install

%files
%doc *.md
%_bindir/*

%changelog
* Wed Mar 25 2026 Nadezhda Fedorova <fedor@altlinux.org> 0.19.2-alt1
- New version 0.19.2.

* Fri Dec 05 2025 Nadezhda Fedorova <fedor@altlinux.org> 0.18.9-alt1
- Initial build for ALTLinux.
