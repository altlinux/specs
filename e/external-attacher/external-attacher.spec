%global _unpackaged_files_terminate_build 1
%global import_path github.com/kubernetes-csi/external-attacher/v4

# binary filename
%define bname csi-attacher

Name:    external-attacher
Version: 4.11.0
Release: alt1

Summary: Sidecar container that watches Kubernetes VolumeAttachment objects and triggers ControllerPublish/Unpublish against a CSI endpoint 
License: Apache-2.0
Group:   Other
Url:     https://github.com/kubernetes-csi/external-attacher

Source: %name-%version.tar

BuildRequires(pre): rpm-build-golang
BuildRequires: golang

%description
The external-attacher is a sidecar container that attaches volumes to nodes 
by calling ControllerPublish and ControllerUnpublish functions of CSI drivers. 
It is necessary because internal Attach/Detach controller running in Kubernetes controller-manager
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

%files
%doc README.md LICENSE
%_bindir/%bname

%changelog
* Tue Mar 24 2026 Ivan Pepelyaev <fl0pp5@altlinux.org> 4.11.0-alt1
- Initial build for ALT.
