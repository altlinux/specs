%define _unpackaged_files_terminate_build 1

%global import_path github.com/golangci/golangci-lint

Name: golangci-lint
Version: 1.52.2
Release: alt1

Summary: Fast linters Runner for Go
License: GPL-3.0
Group: Development/Tools
Url: https://golangci-lint.run
Vcs: https://github.com/golangci/golangci-lint

Source: %name-%version.tar

BuildRequires(pre): rpm-build-golang

ExclusiveArch: %go_arches

%description
golangci-lint is a fast Go linters runner. It runs linters in parallel,
uses caching, supports yaml config, has integrations with all major IDE
and has dozens of linters included.

%prep
%setup

%build
export BUILDDIR="$PWD/.build"
export IMPORT_PATH="%import_path"
export GOPATH="$BUILDDIR:%go_path"
%golang_prepare

cd .build/src/%import_path
%golang_build cmd/%name

%install
export BUILDDIR="$PWD/.build"
export IGNORE_SOURCES=1
%golang_install

%files
%_bindir/*

%changelog
* Tue Mar 28 2023 Anton Zhukharev <ancieg@altlinux.org> 1.52.2-alt1
- New version.

* Mon Nov 14 2022 Anton Zhukharev <ancieg@altlinux.org> 1.50.1-alt1
- initial build for Sisyphus

