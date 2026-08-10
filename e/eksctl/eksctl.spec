%define _unpackaged_files_terminate_build 1
%global import_path github.com/eksctl-io/eksctl

Name: eksctl
Version: 0.229.0
Release: alt1
Summary: The official CLI for Amazon EKS.
License: Apache-2.0
Group: Networking/Other
Url: https://eksctl.io/
Vcs: https://github.com/eksctl-io/eksctl

Source0: %name-%version.tar
Source1: vendor.tar
Patch: %name-%version-%release.patch

BuildRequires(pre): rpm-build-golang

%description
eksctl is a simple CLI tool for creating clusters on EKS -
Amazon's new managed Kubernetes service for EC2. It is written in Go,
and uses CloudFormation.

%prep
%setup -a 1
%patch -p1

%build
export BUILDDIR="$PWD/.gopath"
export IMPORT_PATH="%import_path"
export GOPATH="$BUILDDIR:%go_path"
export GOFLAGS="-mod=vendor"

%golang_prepare

%golang_build cmd/%name/

%install
export BUILDDIR="$PWD/.gopath"
export IMPORT_PATH="%import_path"
export GOPATH="$BUILDDIR:%go_path"
export IGNORE_SOURCES=1
%golang_install

# create the bash completion file
mkdir -p %buildroot%_datadir/bash-completion/completions/
%buildroot/%_bindir/%name completion bash > %buildroot%_datadir/bash-completion/completions/%name

# create the fish completion file
mkdir -p %buildroot%_datadir/fish/vendor_completions.d/
%buildroot/%_bindir/%name completion fish > %buildroot%_datadir/fish/vendor_completions.d/%name.fish

# create the zsh completion file
mkdir -p %buildroot%_datadir/zsh/site-functions/
%buildroot/%_bindir/%name completion zsh > %buildroot%_datadir/zsh/site-functions/_%name

%files
%doc *.md 
%_bindir/%name
%_datadir/bash-completion/completions/%name
%_datadir/fish/vendor_completions.d/%name.fish
%_datadir/zsh/site-functions/_%name

%changelog
* Mon Aug 10 2026 Pavel Shilov <zerospirit@altlinux.org> 0.229.0-alt1
- Initial build for Sisyphus.

