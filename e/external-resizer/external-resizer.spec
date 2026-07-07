%global import_path github.com/kubernetes-csi/external-resizer/v2
%global _unpackaged_files_terminate_build 1

Name: external-resizer
Version: 2.2.0
Release: alt1
Summary: Sidecar container that watches Kubernetes PersistentVolumeClaims objects

Group: System/Servers
License: Apache-2.0
Url: https://kubernetes-csi.github.io/docs/volume-expansion.html
Vcs: https://github.com/kubernetes-csi/external-resizer.git
Source: %name-%version.tar
Patch: %name-%version-%release.patch

ExclusiveArch: %go_arches

BuildRequires(pre): rpm-macros-golang
BuildRequires: rpm-build-golang

%description
A storage provider that allows volume expansion after creation,
may choose to implement volume expansion either via a control-plane
CSI RPC call or via node CSI RPC call or both as a two step process.
The external-resizer is an external-controller that watches Kubernetes
API server for PersistentVolumeClaim modifications and triggers CSI
calls for control-plane volume-expansion.

%prep
%setup
%patch -p1

%build
export BUILDDIR="$PWD/.build"
export IMPORT_PATH="%import_path"
export GOPATH="$BUILDDIR:%go_path"
export LDFLAGS="-X main.version=%version"
%golang_prepare
%golang_build cmd/csi-resizer

%install
export BUILDDIR="$PWD/.build"
export IGNORE_SOURCES=1
%golang_install

%files
%doc *.md OWNERS OWNERS_ALIASES SECURITY_CONTACTS
%_bindir/csi-resizer

%changelog
* Thu Jun 04 2026 Nikita Stavtsev <nst@altlinux.org> 2.2.0-alt1
- Initial build
