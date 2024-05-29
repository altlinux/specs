%define _unpackaged_files_terminate_build 1

%define bash_completionsdir %_datadir/bash-completion/completions
%define fish_completionsdir %_datadir/fish/vendor_completions.d
%define zsh_completionsdir %_datadir/zsh/site-functions

%global import_path k8s.io/minikube

Name: minikube
Version: 1.33.1
Release: alt1

Summary: Run Kubernetes locally
License: Apache-2.0
Group: System/Configuration/Other
Url: https://minikube.sigs.k8s.io
Vcs: https://github.com/kubernetes/minikube

ExclusiveArch: %go_arches

Source0: %name-%version.tar
Source1: vendor.tar

BuildRequires(pre): rpm-build-golang

%description
minikube implements a local Kubernetes cluster on macOS, Linux, and Windows.
minikube's primary goals are to be the best tool for local Kubernetes
application development and to support all Kubernetes features that fit.

%prep
%setup -a1

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

mkdir -p %buildroot%bash_completionsdir
mkdir -p %buildroot%fish_completionsdir
mkdir -p %buildroot%zsh_completionsdir

%buildroot%_bindir/%name completion bash > %buildroot%bash_completionsdir/%name
%buildroot%_bindir/%name completion fish > %buildroot%fish_completionsdir/%name.fish
%buildroot%_bindir/%name completion zsh > %buildroot%zsh_completionsdir/_%name

%files
%_bindir/%name
%bash_completionsdir/%name
%fish_completionsdir/%name.fish
%zsh_completionsdir/_%name

%changelog
* Wed May 29 2024 Alexander Stepchenko <geochip@altlinux.org> 1.33.1-alt1
- 1.32.0 -> 1.31.1

* Mon Jan 22 2024 Alexander Stepchenko <geochip@altlinux.org> 1.32.0-alt1
- 1.31.2 -> 1.32.0 (ALT #49047)
- Drop the %%__mkdir_p macro.

* Wed Sep 13 2023 Anton Zhukharev <ancieg@altlinux.org> 1.31.2-alt1
- Updated to 1.31.2.
- Stopped packaging shell completions subpackages.
- Packaged fish shell completions.

* Thu Nov 17 2022 Anton Zhukharev <ancieg@altlinux.org> 1.28.0-alt3
- build completions for bash and zsh

* Thu Nov 17 2022 Anton Zhukharev <ancieg@altlinux.org> 1.28.0-alt2
- provide version

* Sun Nov 13 2022 Anton Zhukharev <ancieg@altlinux.org> 1.28.0-alt1
- initial build for Sisyphus
