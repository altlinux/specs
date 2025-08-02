%define _unpackaged_files_terminate_build 1
%global import_path github.com/ent/ent

Name: ent
Version: 0.14.5
Release: alt1
Summary: An entity framework for Go
License: Apache-2.0
Group: Networking/Remote access
Url: https://github.com/ent/ent

Source0: %name-%version.tar
Source1: vendor.tar
Patch0: %name-%version-%release.patch
Patch1: alt-i586.patch

BuildRequires(pre): rpm-build-golang
BuildRequires: golang

%description
Simple, yet powerful entity framework for Go, that makes it easy
to build and maintain applications with large data-models.

%prep
%setup -a 1
%autopatch -p1

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
* Sat Aug 02 2025 Pavel Shilov <zerospirit@altlinux.org> 0.14.5-alt1
- 0.14.0 -> 0.14.5

* Thu Jul 24 2025 Pavel Shilov <zerospirit@altlinux.org> 0.14.0-alt1
- 0.13.1 -> 0.14.0

* Thu Sep 12 2024 Pavel Shilov <zerospirit@altlinux.org> 0.13.1-alt1
- initial build for Sisyphus
