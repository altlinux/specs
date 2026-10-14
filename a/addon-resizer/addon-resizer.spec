%define _unpackaged_files_terminate_build 1
%define import_path k8s.io/autoscaler/addon-resizer

Name: addon-resizer
Version: 1.8.21
Release: alt1

Group: Development/Other
Summary: A simplified version of vertical pod autoscaler

License: Apache-2.0
Url: https://github.com/kubernetes/autoscaler

Source: %name-%version.tar
Patch: %name-%version-%release.patch

ExclusiveArch: %go_arches
ExcludeArch: i586

BuildRequires(pre): rpm-macros-golang
BuildRequires: rpm-build-golang golang >= 1.26.0

%description
A simplified version of vertical pod autoscaler that modifies resource requests
of a deployment based on the number of nodes in the Kubernetes Cluster.

%prep
%setup
%patch -p1

%build
pushd addon-resizer/
export BUILDDIR="$PWD/.build/"
export IMPORT_PATH="%import_path"
export GOPATH="$BUILDDIR:%go_path"
export LDFLAGS="-X k8s.io/autoscaler/addon-resizer/nanny.AddonResizerVersion=%version"
%golang_prepare
mkdir -p "$BUILDDIR/bin"
CGO_ENABLED=0 %gobuild -o "$BUILDDIR/bin/pod_nanny" ./nanny/main/pod_nanny.go
popd

%install
export GOPATH="%go_path"
export IGNORE_SOURCES=1

pushd addon-resizer/
export BUILDDIR="$PWD/.build"
%golang_install
popd

%check
pushd addon-resizer
%gotest ./...
popd

%files
%doc addon-resizer/README.md addon-resizer/OWNERS
%_bindir/pod_nanny

%changelog
* Wed Sep 23 2026 Nikita Stavtsev <nst@altlinux.org> 1.8.21-alt1
- Initial build
