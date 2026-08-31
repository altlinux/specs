%global _unpackaged_files_terminate_build 1
%global import_path github.com/cozystack/etcd-operator

Name:    cozystack-etcd-operator
Version: 0.5.5
Release: alt1

Summary: A Kubernetes operator for running etcd clusters
License: Apache-2.0
Group:   Other
Url:     https://etcd.aenix.io
Vcs:     https://github.com/cozystack/etcd-operator

Source:  %name-%version.tar
Source1: vendor.tar

BuildRequires(pre): rpm-build-golang

%description
etcd-operator is a Kubernetes operator for deploying and managing etcd
clusters. It manages clusters through two custom resources: EtcdCluster,
which captures user intent (replica count, etcd version, storage size),
and EtcdMember, one per etcd member, which owns its Pod and PVC.

%package -n cozystack-kubectl-etcd
Summary: Cozystack kubectl plugin for managing etcd clusters
Group: Other
%description -n cozystack-kubectl-etcd
kubectl-etcd is a kubectl plugin that provides convenient commands
for inspecting and managing etcd clusters managed by cozystack-etcd-operator.

%package -n cozystack-etcd-migrate
Summary: Migration tool for etcd-operator v1alpha1 to v1alpha2
Group: Other
%description -n cozystack-etcd-migrate
etcd-migrate adopts running legacy etcd.aenix.io/v1alpha1 clusters onto
etcd-operator.cozystack.io/v1alpha2 in place without restarting etcd pods.

%prep
%setup -a 1

%build
export BUILDDIR="$PWD/.build"
export IMPORT_PATH="%import_path"
export GOPATH="$BUILDDIR:%go_path"
export GOFLAGS="-trimpath"
export LDFLAGS="-buildid="

%golang_prepare
%golang_build .
# set version for CLI tools only
export LDFLAGS="-X main.version=v%version $LDFLAGS"
%golang_build ./cmd/*

%install
export BUILDDIR="$PWD/.build"
export IGNORE_SOURCES=1
%golang_install

%check
%gotest -v ./...

%files
%doc LICENSE README.md
%_bindir/etcd-operator

%files -n cozystack-kubectl-etcd
%_bindir/kubectl-etcd

%files -n cozystack-etcd-migrate
%_bindir/etcd-migrate

%changelog
* Mon Aug 31 2026 Ivan Pepelyaev <fl0pp5@altlinux.org> 0.5.5-alt1
- Initial build for ALT.


