%global _unpackaged_files_terminate_build 1
%global import_path github.com/kubernetes-csi/external-provisioner/v5

# binary filename
%define bname csi-provisioner

Name:    external-provisioner
Version: 6.2.0
Release: alt1

Summary: Sidecar container that watches Kubernetes PersistentVolumeClaim objects and triggers CreateVolume/DeleteVolume against a CSI endpoint 
License: Apache-2.0
Group:   Other
Url:     https://github.com/kubernetes-csi/external-provisioner

Source: %name-%version.tar

BuildRequires(pre): rpm-build-golang
BuildRequires: golang

%description
The external-provisioner is a sidecar container that dynamically provisions volumes
by calling CreateVolume and DeleteVolume functions of CSI drivers.
It is necessary because internal persistent volume controller running in Kubernetes controller-manager
does not have any direct interfaces to CSI drivers.

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

%check
%ifarch %ix86
%gotest ./cmd/...
%else
%gotest ./cmd/... -race
%endif

%files
%doc README.md LICENSE
%_bindir/%bname

%changelog
* Tue Mar 24 2026 Ivan Pepelyaev <fl0pp5@altlinux.org> 6.2.0-alt1
- Initial build for ALT.
