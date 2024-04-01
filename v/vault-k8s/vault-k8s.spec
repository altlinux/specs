%global import_path github.com/hashicorp/vault-k8s

Name:    vault-k8s
Version: 1.4.0
Release: alt1

Summary: First-class support for Vault and Kubernetes
License: MPL-2.0
Group:   Other
Url:     https://github.com/hashicorp/vault-k8s

Source: %name-%version.tar

BuildRequires(pre): rpm-build-golang
BuildRequires: golang

%description
%summary

%prep
%setup

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

%files
%doc *.md
%_bindir/*

%changelog
* Thu Mar 14 2024 Nikolay Burykin <bne@altlinux.org> 1.4.0-alt1
- Initial build for ALT

