%global import_path github.com/fluxcd/flux2/
%define version 2.3.0

Name: flux2
Version: 2.3.0
Release: alt1
Summary: Container cluster management

Group: System/Configuration/Other
License: Apache-2.0

Url: https://github.com/fluxcd/flux2/
Source0: %name-%version.tar

ExclusiveArch:  %go_arches
BuildRequires(pre): rpm-build-golang
BuildRequires(pre): golang > 1.21
BuildRequires: /proc

%description
Flux is a tool for keeping Kubernetes clusters in sync with sources of
configuration (like Git repositories and OCI artifacts), and automating updates
to  configuration when there is new code to deploy.

%prep
export BUILDDIR="$PWD/.build"
export IMPORT_PATH="%import_path"
%setup
%golang_prepare
for file in ./cmd/flux/manifests/*-controller.yaml
do
  sed -e "s|image: fluxcd|image: registry.altlinux.org/%_priority_distbranch/flux2|" -i $file
done

%build
export BUILDDIR="$PWD/.build"
export IMPORT_PATH="%import_path"
export GOPATH="$BUILDDIR:%go_path"
%golang_prepare
LDFLAGS="-w -X main.VERSION=%version" %golang_build ./cmd/flux

%install
export BUILDDIR="$PWD/.build"
export IGNORE_SOURCES=1
%golang_install

%files
%_bindir/flux
%doc *.md
%doc docs/*

%changelog
* Thu Oct 31 2024 Alexey Kostarev <kaf@altlinux.org> 2.3.0-alt1
- Initial build.
