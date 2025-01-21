%define prog_name image-automation-controller
%global import_path github.com/fluxcd/%prog_name/

Name: flux2-%prog_name
Version: 0.38.0
Release: alt1
Summary: Container cluster management

Group: System/Configuration/Other
License: Apache-2.0

Url: https://github.com/fluxcd/image-automation-controller
Source0: %name-%version.tar

ExclusiveArch:  %go_arches
BuildRequires(pre): rpm-build-golang
BuildRequires(pre): golang > 1.21
BuildRequires: /proc

%description
This controller automates updates to YAML
when new container images are available.

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
* Sat Nov 02 2024 Alexey Kostarev <kaf@altlinux.org> 0.38.0-alt1
- Initial build.
