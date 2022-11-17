%define _unpackaged_files_terminate_build 1

%global import_path k8s.io/minikube

Name: minikube
Version: 1.28.0
Release: alt3

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

%package -n bash-completion-%name
Summary: Bash completions for minikube
Group: Shells
BuildArch: noarch

%description -n bash-completion-%name
%summary.

%package -n zsh-completion-%name
Summary: Zsh completion for minikube
Group: Shells
BuildArch: noarch

%description -n zsh-completion-%name
%summary.

%prep
%setup

%build
export BUILDDIR="$PWD/.build"
export IMPORT_PATH="%import_path"
export GOPATH="$BUILDDIR:%go_path"
%golang_prepare

cd .build/src/%import_path
export PKGPATH="%import_path/pkg"
export VERSION="$PKGPATH/version.version=%version"
export ISOVERSION="$PKGPATH/version.isoVersion=%version"
export STORAGEPROVISIONERVERSION="$PKGPATH/version.storageProvisionerVersion=5"
export LDFLAGS="-X $VERSION -X $ISOVERSION -X $STORAGEPROVISIONERVERSION"
%golang_build cmd/minikube

%install
export BUILDDIR="$PWD/.build"
export IGNORE_SOURCES=1
%golang_install

mkdir -p %buildroot%_datadir/bash-completion/completions
mkdir -p %buildroot%_datadir/zsh/site-functions

%buildroot%_bindir/%name completion bash > %buildroot%_datadir/bash-completion/completions/minikube
%buildroot%_bindir/%name completion zsh > %buildroot%_datadir/zsh/site-functions/_minikube

%files
%_bindir/*

%files -n bash-completion-%name
%_datadir/bash-completion/completions/%name

%files -n zsh-completion-%name
%_datadir/zsh/site-functions/_%name

%changelog
* Thu Nov 17 2022 Anton Zhukharev <ancieg@altlinux.org> 1.28.0-alt3
- build completions for bash and zsh

* Thu Nov 17 2022 Anton Zhukharev <ancieg@altlinux.org> 1.28.0-alt2
- provide version

* Sun Nov 13 2022 Anton Zhukharev <ancieg@altlinux.org> 1.28.0-alt1
- initial build for Sisyphus
