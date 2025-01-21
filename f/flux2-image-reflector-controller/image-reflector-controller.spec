%define prog_name image-reflector-controller
%global import_path github.com/fluxcd/image-reflector-controller/

Name: flux2-%prog_name
Version: 0.32.0
Release: alt1
Summary: Container cluster management

Group: System/Configuration/Other
License: Apache-2.0

Url: https://github.com/fluxcd/image-reflector-controller
Source0: %name-%version.tar

ExclusiveArch:  %go_arches
BuildRequires(pre): rpm-build-golang
BuildRequires(pre): golang > 1.21
BuildRequires: /proc

%description
This is a controller that reflects container image metadata into a Kubernetes cluster.
It pairs with the image update automation controller to drive automated config updates.

%prep
%setup

%build
export BUILDDIR="$PWD/.build"
export IMPORT_PATH="%import_path"
export GOPATH="$BUILDDIR:%go_path"
%golang_prepare
%golang_build .

%install
export BUILDDIR="$PWD/.build"
export IGNORE_SOURCES=1
%golang_install

%files
%_bindir/%prog_name
%doc *.md
%doc docs/*

%changelog
* Thu Oct 31 2024 Alexey Kostarev <kaf@altlinux.org> 0.32.0-alt1
- Initial build.
