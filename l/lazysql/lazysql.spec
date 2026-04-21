%define _unpackaged_files_terminate_build 1

%global import_path github.com/jorgerojas26/lazysql

Name:    lazysql
Version: 0.4.8
Release: alt1

Summary: A cross-platform TUI database management tool written in Go.
License: MIT
Group:   Databases
Url:     https://github.com/jorgerojas26/lazysql

Source0: %name-%version.tar
Source1: vendor.tar

BuildRequires(pre): rpm-build-golang
BuildRequires: golang

%description
%summary.

%prep
%setup -a 1

%build
export BUILDDIR="$PWD/.build"
export IMPORT_PATH="%import_path"
export GOPATH="$BUILDDIR:%go_path"
export GOFLAGS=-mod=vendor

%golang_prepare

cd .build/src/%import_path
%golang_build .

%install
export BUILDDIR="$PWD/.build"
export IGNORE_SOURCES=1

%golang_install

%files
%doc *.md
%_bindir/%name

%changelog
* Mon Apr 20 2026 Nikita Shmatko <nash@altlinux.org> 0.4.8-alt1
- New version 0.4.8.

* Mon Jan 19 2026 Nikita Shmatko <nash@altlinux.org> 0.4.6-alt1
- New version 0.4.6.

* Wed Nov 26 2025 Nikita Shmatko <nash@altlinux.org> 0.4.3-alt1
- Initial build for Sisyphus.
