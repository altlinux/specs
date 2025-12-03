%define _unpackaged_files_terminate_build 1
%global import_path github.com/kubernetes-csi/external-snapshotter

Name: external-snapshotter
Version: 8.4.0
Release: alt1
Summary: Sidecar for managing CSI snapshots via Snapshot CRDs
License: Apache-2.0
Group: System/Configuration/Other
Url: https://github.com/kubernetes-csi/external-snapshotter
Source: %name-%version.tar

BuildRequires(pre): rpm-macros-golang
BuildRequires: rpm-build-golang

%description
The CSI snapshotter is part of Kubernetes implementation
of Container Storage Interface (CSI) and implements both the volume snapshot
and the volume group snapshot feature.

%package -n csi-snapshotter
Summary: CSI external snapshotter sidecar controller
Group: System/Configuration/Other

%description -n csi-snapshotter
%summary

%package -n snapshot-controller
Summary: Common snapshot controller for Kubernetes
Group: System/Configuration/Other

%description -n snapshot-controller
%summary

%package -n snapshot-conversion-webhook
Summary: Conversion webhook for snapshot API versions
Group: System/Configuration/Other

%description -n snapshot-conversion-webhook
%summary

%prep
%setup

%build
export BUILDDIR="$PWD/.build"
export IMPORT_PATH="%import_path"
export GOFLAGS="-buildmode=pie"
export LDFLAGS="-X github.com/kubernetes-csi/external-snapshotter/main.version=%version"

%golang_prepare

cd .build/src/%import_path
%golang_build cmd/*

%install
export BUILDDIR="$PWD/.build"
export IGNORE_SOURCES=1

%golang_install

%files -n csi-snapshotter
%doc *.md
%_bindir/csi-snapshotter

%files -n snapshot-controller
%doc *.md
%_bindir/snapshot-controller

%files -n snapshot-conversion-webhook
%doc *.md
%_bindir/snapshot-conversion-webhook

%changelog
* Fri Nov 28 2025 Vladislav Tsarev <tyaplyapych@altlinux.org> 8.4.0-alt1
- initial build
