%define _unpackaged_files_terminate_build 1

%global import_path github.com/swaggo/swag

Name: swag
Version: 2.0.0
Release: alt1.rc3

Summary: Automatically generate RESTful API doc with Swagger 2.0 for Go
License: MIT
Group: Development/Other
Url: https://pkg.go.dev/github.com/swaggo/swag
Vcs: https://github.com/swaggo/swag

ExclusiveArch: %go_arches

Source0: %name-%version.tar
Source1: vendor.tar

Requires: golang

BuildRequires(pre): rpm-build-golang

%description
Swag converts Go annotations to Swagger Documentation 2.0. We've created
a variety of plugins for popular Go web frameworks. This allows you to
quickly integrate with an existing Go project (using Swagger UI).

%prep
%setup -a1

%build
export BUILDDIR="$PWD/.build"
export IMPORT_PATH="%import_path"
export GOPATH="$BUILDDIR:%go_path"

%golang_prepare

cd .build/src/%import_path
%golang_build ./cmd/swag

%install
export BUILDDIR="$PWD/.build"
export IGNORE_SOURCES=1
%golang_install

%files
%doc README* example
%_bindir/*

%changelog
* Tue Jul 25 2023 Alexandr Shashkin <dutyrok@altlinux.org> 2.0.0-alt1.rc3
- Initial build for Sisyphus

