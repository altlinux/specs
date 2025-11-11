%global import_path github.com/brancz/kube-rbac-proxy
%define _unpackaged_files_terminate_build 1

Name:    kube-rbac-proxy
Version: 0.20.0
Release: alt1

Summary: Kubernetes RBAC authorizing HTTP proxy for a single upstream
License: Apache-2.0
Group:   Other
Url:     https://github.com/brancz/kube-rbac-proxy

Source: %name-%version.tar
Patch0: %name-%version.patch

BuildRequires(pre): rpm-macros-golang
BuildRequires: rpm-build-golang
BuildRequires: golang
BuildRequires: /proc

%description
In Kubernetes clusters without NetworkPolicies any Pod can
perform requests to every other Pod in the cluster. This proxy
was developed in order to restrict requests to only those Pods,
that present a valid and RBAC authorized token or client TLS
certificate.

%prep
%setup
%patch0 -p1

%build
export BUILDDIR="$PWD/.build"
export IMPORT_PATH="%import_path"
export GOPATH="$BUILDDIR:%go_path"

%golang_prepare

%golang_build ./cmd/%name

%install
export BUILDDIR="$PWD/.build"
export IGNORE_SOURCES=1

%golang_install

%files
%doc *.md
%_bindir/%name

%changelog
* Mon Nov 10 2025 Nadezhda Fedorova <fedor@altlinux.org> 0.20.0-alt1
- Initial build for ALTLinux.
