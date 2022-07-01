%global import_path github.com/jsonnet-bundler/jsonnet-bundler
Name:     jsonnet-bundler
Version:  0.5.1
Release:  alt1

Summary:  A jsonnet package manager.
License:  Apache-2.0
Group:    Other
Url:      https://github.com/jsonnet-bundler/jsonnet-bundler

Packager: Mikhail Gordeev <obirvalger@altlinux.org>

Source:   %name-%version.tar

BuildRequires(pre): rpm-build-golang
BuildRequires: golang

%description
%summary

%prep
%setup

%build
export BUILDDIR="$PWD/.build"
export IMPORT_PATH="%import_path"
export GOPATH="$BUILDDIR:%go_path"

%golang_prepare

cd .build/src/%import_path
%golang_build cmd/jb

%install
export BUILDDIR="$PWD/.build"
export IGNORE_SOURCES=1

%golang_install

%files
%_bindir/*
%doc *.md

%changelog
* Fri Jul 01 2022 Mikhail Gordeev <obirvalger@altlinux.org> 0.5.1-alt1
- Initial build for Sisyphus
