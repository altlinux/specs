%global import_path github.com/kubernetes/dashboard

%define _unpackaged_files_terminate_build 1

Name: kind
Version: 0.30.0
Release: alt1

Summary: Kubernetes IN Docker - local clusters for testing Kubernetes
License: Apache-2.0
Group: System/Configuration/Other
Url: https://kind.sigs.k8s.io
Vcs: https://github.com/kubernetes-sigs/kind

Source0: %name-%version.tar
Source1: vendor.tar

BuildRequires(pre): rpm-macros-golang
BuildRequires: rpm-build-golang golang >= 1.17

%description
kind is a tool for running local Kubernetes clusters using Docker container
"nodes". kind was primarily designed for testing Kubernetes itself, but may
be used for local development or CI.

%prep
%setup -a 1

%build
export BUILDDIR="$PWD/.build"
export IMPORT_PATH="%import_path"
export GOPATH="$BUILDDIR:%go_path"

%golang_prepare

cd .build/src/%import_path
%golang_build .

%install
export BUILDDIR="$PWD/.build"
export IGNORE_SOURCES=1

%golang_install

install -d -m0755 \
    %buildroot%_datadir/bash-completion/completions \
    %buildroot%_datadir/zsh/site-functions \
    %buildroot%_datadir/fish/vendor_completions.d

%buildroot%_bindir/kind completion bash > %buildroot%_datadir/bash-completion/completions/kind
%buildroot%_bindir/kind completion zsh > %buildroot%_datadir/zsh/site-functions/_kind
%buildroot%_bindir/kind completion fish > %buildroot%_datadir/fish/vendor_completions.d/kind.fish

%files
%doc *.md
%_bindir/kind
%_datadir/bash-completion/completions/kind
%_datadir/zsh/site-functions/_kind
%_datadir/fish/vendor_completions.d/kind.fish

%changelog
* Thu Oct 23 2025 Alexander Stepchenko <geochip@altlinux.org> 0.30.0-alt1
- Initial build.
