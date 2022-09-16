%define _unpackaged_files_terminate_build 1

%global import_path golang.org/x/tools/gopls

Name: gopls
Version: 0.9.5
Release: alt1

Summary: The Go language server
License: BSD-3-Clause
Group: Development/Other
Url: https://pkg.go.dev/golang.org/x/tools/gopls

Source: %name-%version.tar

ExclusiveArch: %go_arches
BuildRequires(pre): rpm-build-golang

%description
A simple, modern and secure encryption tool (and Go library) with small
explicit keys, no config options, and UNIX-style composability.

%prep
%setup

%build
export BUILDDIR="$PWD/.build"
export IMPORT_PATH="%import_path"
export GOPATH="$BUILDDIR:%go_path"

%golang_prepare

cd .build/src/%import_path
%golang_build .

%install
export BUILDDIR="$PWD/.build"
export IGNORE_SOURCES=1
%golang_install

%files
%_bindir/*

%changelog
* Fri Sep 16 2022 Anton Zhukharev <ancieg@altlinux.org> 0.9.5-alt1
- initial build for Sisyphus

