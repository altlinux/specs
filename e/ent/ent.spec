%define _unpackaged_files_terminate_build 1
%global import_path github.com/ent/ent

Name: ent
Version: 0.13.1
Release: alt1
Summary: An entity framework for Go
License: Apache-2.0
Group: Networking/Remote access
Url: https://github.com/ent/ent

Source0: %name-%version.tar

BuildRequires(pre): rpm-build-golang
BuildRequires: golang

%description
Simple, yet powerful entity framework for Go, that makes it easy
to build and maintain applications with large data-models.

%prep
%setup -q

%build
export BUILDDIR="$PWD/.gopath"
export IMPORT_PATH="%import_path"
export GOPATH="$BUILDDIR:%go_path"
export GOFLAGS="-mod=vendor"

%golang_prepare

%golang_build cmd/%name

%install
export BUILDDIR="$PWD/.gopath"
export IMPORT_PATH="%import_path"
export GOPATH="$BUILDDIR:%go_path"
export IGNORE_SOURCES=1
%golang_install

%files
%doc README.md
%_bindir/%name

%changelog
* Thu Sep 12 2024 Pavel Shilov <zerospirit@altlinux.org> 0.13.1-alt1
- initial build for Sisyphus
