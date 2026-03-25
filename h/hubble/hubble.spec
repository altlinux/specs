%global import_path github.com/cilium/hubble
%global _unpackaged_files_terminate_build 1
%global commit 95622e77ee29730d2ca662b759613ea17e3951f2

Name:    hubble
Version: 1.18.6
Release: alt1

Summary: Hubble - Network, Service & Security Observability for Kubernetes using eBPF
License: Apache-2.0
Group:   System/Configuration/Networking
Url:     https://github.com/cilium/hubble

Source: %name-%version.tar

BuildRequires(pre):  rpm-macros-golang
BuildRequires:  rpm-build-golang
BuildRequires:  golang
BuildRequires:  /proc

%description
Hubble is a fully distributed networking and security observability platform for cloud
native workloads. It is built on top of Cilium and eBPF to enable deep visibility into
the communication and behavior of services as well as the networking infrastructure in
a completely transparent manner.

%prep
%setup

%build
export BUILDDIR="$PWD/.build"
export GOFLAGS="-mod=vendor -buildmode=pie"
export GOBIN="$BUILDDIR/bin"
export IMPORT_PATH="%import_path"
export GOPATH="$BUILDDIR:%go_path"
export LDFLAGS="-X github.com/cilium/cilium/hubble/pkg.GitHash=%commit -X github.com/cilium/cilium/hubble/pkg.Version=%version"

%golang_prepare

mkdir $GOBIN
pushd $BUILDDIR/src/%import_path
%golang_build .
popd

%install
export BUILDDIR="$PWD/.build"
export IGNORE_SOURCES=1

%golang_install

%files
%doc *.md
%_bindir/%name

%changelog
* Wed Mar 25 2026 Nadezhda Fedorova <fedor@altlinux.org> 1.18.6-alt1
- New version 1.18.6.

* Fri Nov 14 2025 Nadezhda Fedorova <fedor@altlinux.org> 1.18.3-alt1
- Initial build for ALTLinux.
