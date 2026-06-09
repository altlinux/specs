%global import_path github.com/go-acme/lego
%global _unpackaged_files_terminate_build 1

Name: lego
Version: 5.2.2
Release: alt1
Summary: Let's Encrypt/ACME client and library written in Go

Group: Development/Tools
License: MIT

Url: https://go-acme.github.io/lego/
Vcs: https://github.com/go-acme/lego.git

Source0: %name-%version.tar
Source1: %name-%version-vendor.tar

ExclusiveArch: %go_arches

BuildRequires(pre): rpm-macros-golang
BuildRequires: rpm-build-golang golang >= 1.24.0
BuildPreReq: /proc

%description
Let's Encrypt/ACME client and library written in Go.

%prep
%setup -a1

%build
export BUILDDIR="$PWD/.build"
export IMPORT_PATH="%import_path"
export GOPATH="$BUILDDIR:%go_path"
export GOFLAGS="-mod=vendor"
export LDFLAGS="-extldflags '-static'"
export CGO_ENABLED=0

%golang_prepare

%golang_build .

%install
export BUILDDIR="$PWD/.build"
export IGNORE_SOURCES=1

%golang_install

%files
%doc docs/content/*
%_bindir/*

%changelog
* Tue Jun 09 2026 Alexey Romanyuta <r9odt@altlinux.org> 5.2.2-alt1
- New version 5.2.2.

* Fri Mar 06 2026 Alexey Romanyuta <r9odt@altlinux.org> 4.32.0-alt1
- New version v4.32.0

* Sat Jul 05 2025 Alexey Romanyuta <r9odt@altlinux.org> 4.24.0-alt1
- Initial build v4.24.0
