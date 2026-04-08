%global _unpackaged_files_terminate_build 1
%global import_path github.com/kubernetes-csi/external-health-monitor

# binary filename
%define bname csi-external-health-monitor-controller

Name:    external-health-monitor
Version: 0.17.0
Release: alt1

Summary: A sidecar controller and agent for volume health monitoring
License: Apache-2.0
Group:   Other
Url:     https://github.com/kubernetes-csi/external-health-monitor

Source: %name-%version.tar

BuildRequires(pre): rpm-build-golang
BuildRequires: golang

%description
%summary.
The Volume Health Monitor is part of Kubernetes implementation of Container Storage Interface (CSI).

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
* Tue Mar 24 2026 Ivan Pepelyaev <fl0pp5@altlinux.org> 0.17.0-alt1
- Initial build for ALT.
