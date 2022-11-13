%define _unpackaged_files_terminate_build 1

%global import_path k8s.io/minikube

Name: minikube
Version: 1.28.0
Release: alt1

Summary: Run Kubernetes locally
License: Apache-2.0
Group: System/Configuration/Other
Url: https://minikube.sigs.k8s.io
Vcs: https://github.com/kubernetes/minikube

Source: %name-%version.tar

BuildRequires(pre): rpm-build-golang

ExclusiveArch: %go_arches

%description
minikube implements a local Kubernetes cluster on macOS, Linux, and Windows.
minikube's primary goals are to be the best tool for local Kubernetes
application development and to support all Kubernetes features that fit.

%prep
%setup

%build
export BUILDDIR="$PWD/.build"
export IMPORT_PATH="%import_path"
export GOPATH="$BUILDDIR:%go_path"
%golang_prepare

cd .build/src/%import_path
%golang_build cmd/minikube

%install
export BUILDDIR="$PWD/.build"
export IGNORE_SOURCES=1
%golang_install

%files
%_bindir/*

%changelog
* Sun Nov 13 2022 Anton Zhukharev <ancieg@altlinux.org> 1.28.0-alt1
- initial build for Sisyphus
