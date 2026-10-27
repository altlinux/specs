%global import_path sigs.k8s.io/cluster-api-provider-kubevirt
%global _unpackaged_files_terminate_build 1

Name:    capk-manager
Version: 0.10.0
Release: alt1

Summary: Cluster API Provider Manager for KubeVirt
License: Apache-2.0
Group:   Other
Url:     https://github.com/kubernetes-sigs/cluster-api-provider-kubevirt

Source: %name-%version.tar
Source1: vendor.tar

BuildRequires(pre): rpm-build-golang
BuildRequires: golang >= 1.23.6

ExcludeArch: %ix86

%description
The Cluster API brings declarative Kubernetes-style APIs to cluster
creation, configuration and management. The API itself is shared across
multiple infrastructure providers, allowing for true hybrid deployments
of Kubernetes.

This package provides the Cluster API infrastructure provider for
KubeVirt (CAPK) controller manager.

%prep
%setup -a 1

%build
export BUILDDIR="$PWD/.build"
export IMPORT_PATH="%import_path"
export GOPATH="$BUILDDIR:%go_path"
export CGO_ENABLED=0

%golang_prepare

cd .build/src/%import_path
%gobuild -o "$BUILDDIR/bin/%name" .

%install
export BUILDDIR="$PWD/.build"
export IGNORE_SOURCES=1

%golang_install

%check
export CGO_ENABLED=0
%gotest -v `go list ./... | grep -Ev "e2e|clusterkubevirtadm"`

%files
%doc README.md
%_bindir/%name

%changelog
* Tue Oct 27 2026 Ivan Pepelyaev <fl0pp5@altlinux.org> 0.10.0-alt1
- Initial build for ALT.

