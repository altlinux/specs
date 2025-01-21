%define prog_name helm-controller
%global import_path github.com/fluxcd/%prog_name/

Name: flux2-%prog_name
Version: 1.0.1
Release: alt1
Summary: Container cluster management

Group: System/Configuration/Other
License: Apache-2.0

Url: https://github.com/fluxcd/helm-controller
Source0: %name-%version.tar

ExclusiveArch:  %go_arches
BuildRequires(pre): rpm-build-golang
BuildRequires(pre): golang > 1.21
BuildRequires: /proc

%description
The helm-controller is a Kubernetes operator,
allowing one to declaratively manage Helm chart releases.
It is part of a composable GitOps toolkit and depends on source-controller
to acquire the Helm charts from Helm repositories.

%prep
%setup

%build
export BUILDDIR="$PWD/.build"
export IMPORT_PATH="%import_path"
export GOPATH="$BUILDDIR:%go_path"
%golang_prepare
%golang_build  .

%install
export BUILDDIR="$PWD/.build"
export IGNORE_SOURCES=1
%golang_install

%files
%_bindir/%prog_name
%doc *.md
%doc docs/*

%changelog
* Sat Nov 02 2024 Alexey Kostarev <kaf@altlinux.org> 1.0.1-alt1
- Initial build.
