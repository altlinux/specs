%define _unpackaged_files_terminate_build 1
%global import_path github.com/stakater/Reloader

Name: k8s-reloader
Version: 1.4.10
Release: alt1
Summary: Automated Pod rollout on ConfigMap and Secret changes
License: Apache-2.0
Group: System/Configuration/Other
Url: https://github.com/stakater/Reloader
Source: %name-%version.tar

BuildRequires(pre): rpm-macros-golang
BuildRequires: rpm-build-golang

%description
Reloader is a Kubernetes controller that automatically triggers
rollouts of workloads (like Deployments, StatefulSets, and more)
whenever referenced Secrets or ConfigMaps are updated.

%prep
%setup

%build
export BUILDDIR="$PWD/.build"
export IMPORT_PATH="%import_path"
export GOFLAGS="-buildmode=pie"
export LDFLAGS="-X github.com/stakater/Reloader/pkg/common.Version=%version"

%golang_prepare

cd .build/src/%import_path
%golang_build .

%install
export BUILDDIR="$PWD/.build"
export IGNORE_SOURCES=1

%golang_install

mv \
    %buildroot%_bindir/Reloader \
    %buildroot%_bindir/%name

%files
%doc LICENSE README.md docs/
%_bindir/%name

%changelog
* Tue Nov 18 2025 Vladislav Tsarev <tyaplyapych@altlinux.org> 1.4.10-alt1
- initial build
