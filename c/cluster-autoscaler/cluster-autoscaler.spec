%define _unpackaged_files_terminate_build 1
%define import_path k8s.io/autoscaler/cluster-autoscaler

Name: cluster-autoscaler
Version: 1.35.0
Release: alt1

Group: Development/Other
Summary: Adjust the size of k8s cluster

License: Apache-2.0
Url: https://github.com/kubernetes/autoscaler

Source: %name-%version.tar
Patch: %name-%version-%release.patch

ExclusiveArch: %go_arches

BuildRequires(pre): rpm-macros-golang
BuildRequires: rpm-build-golang golang >= 1.26.0

%description
A component that automatically adjusts the size of a Kubernetes Cluster
so that all pods have a place to run and there are no unneeded nodes.

%prep
%setup
%patch -p1

%build
pushd cluster-autoscaler/
export BUILDDIR="$PWD/.build"
export IMPORT_PATH="%import_path"
export GOPATH="$BUILDDIR:%go_path"
%golang_prepare
CGO_ENABLED=0 %golang_build .
popd

%install
export GOPATH="%go_path"
export IGNORE_SOURCES=1

pushd cluster-autoscaler/
export BUILDDIR="$PWD/.build"
%golang_install
popd

%check
pushd cluster-autoscaler
go list ./... | grep -v "cloudprovider" | xargs %gotest
popd

%files
%doc cluster-autoscaler/*.md cluster-autoscaler/OWNERS
%_bindir/cluster-autoscaler

%changelog
* Wed Sep 23 2026 Nikita Stavtsev <nst@altlinux.org> 1.35.0-alt1
- Initial build
