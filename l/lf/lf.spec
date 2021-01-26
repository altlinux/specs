%global import_path github.com/gokcehan/lf
Name:     lf
Version:  r19
Release:  alt1

Summary:  Terminal file manager
License:  MIT
Group:    File tools
Url:      https://github.com/gokcehan/lf

Packager: Nikita Ermakov <arei@altlinux.org>

Source:   %name-%version.tar

BuildRequires(pre): rpm-build-golang
BuildRequires: golang

%description
lf (as in "list files") is a terminal file manager written in Go. It is
heavily inspired by ranger with some missing and extra features. Some of the
missing features are deliberately omitted since they are better handled by
external tools.

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
%doc *.md

%changelog
* Tue Jan 26 2021 Nikita Ermakov <arei@altlinux.org> r19-alt1
- Initial build for Sisyphus
