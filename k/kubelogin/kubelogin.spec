%define _unpackaged_files_terminate_build 1

%global import_path github.com/int128/kubelogin

Name: kubelogin
Version: 1.35.2
Release: alt1

Summary: kubectl plugin for Kubernetes OpenID Connect authentication (kubectl oidc-login)
License: Apache-2.0
Group: Other
Url: https://github.com/int128/kubelogin
Vcs: https://github.com/int128/kubelogin

Source0: %name-%version.tar
Source1: vendor.tar

BuildRequires(pre): rpm-macros-golang
BuildRequires: rpm-build-golang

%description
This is a kubectl plugin for Kubernetes OpenID Connect (OIDC) authentication,
also known as kubectl oidc-login.

Kubelogin is designed to run as a client-go credential plugin.
When you run kubectl, kubelogin opens the browser and you can log in
to the provider. Then kubelogin gets a token from the provider and kubectl
access Kubernetes APIs with the token.

%prep
%setup -a 1

%build
export BUILDDIR="$PWD/.build"
export IMPORT_PATH="%import_path"
export GOPATH="$BUILDDIR:%go_path"

export LDFLAGS="-X main.version=%version"

%golang_prepare

cd .build/src/%import_path
%golang_build .

mv "$BUILDDIR/bin/kubelogin" "$BUILDDIR/bin/kubectl-oidc_login"

%install
export BUILDDIR="$PWD/.build"
export IGNORE_SOURCES=1

%golang_install

%files
%doc *.md
%_bindir/kubectl-oidc_login

%changelog
* Wed Feb 25 2026 Alexander Stepchenko <geochip@altlinux.org> 1.35.2-alt1
- Initial build.
