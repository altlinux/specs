%global _unpackaged_files_terminate_build 1
%global import_path github.com/kubernetes-csi/node-driver-registrar

# binary filename
%define bname csi-node-driver-registrar

Name:    node-driver-registrar
Version: 2.16.0
Release: alt1

Summary: Sidecar container that registers a CSI driver with the kubelet using the kubelet plugin registration mechanism
License: Apache-2.0
Group:   Other
Url:     https://github.com/kubernetes-csi/node-driver-registrar

Source: %name-%version.tar

BuildRequires(pre): rpm-build-golang
BuildRequires: golang

%description
The node-driver-registrar is a sidecar container that registers the CSI driver
with Kubelet using the kubelet plugin registration mechanism.

This is necessary because Kubelet is responsible for issuing CSI NodeGetInfo,
NodeStageVolume, NodePublishVolume calls. The node-driver-registrar registers your CSI
driver with Kubelet so that it knows which Unix domain socket to issue the CSI calls on.

%prep
%setup

%build
export BUILDDIR="$PWD/.build"
export IMPORT_PATH="%import_path"
export GOPATH="$BUILDDIR:%go_path"

%golang_prepare

cd .build/src/%import_path
%golang_build cmd/%bname

%install
export BUILDDIR="$PWD/.build"
export IGNORE_SOURCES=1

%golang_install

%files
%doc README.md LICENSE
%_bindir/%bname

%changelog
* Tue Mar 24 2026 Ivan Pepelyaev <fl0pp5@altlinux.org> 2.16.0-alt1
- Initial build for ALT.
