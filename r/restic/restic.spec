%global import_path github.com/restic/restic
Name:     restic
Version:  0.9.4
Release:  alt1

Summary:  Fast, secure, efficient backup program
License:  BSD-2-Clause
Group:    Other
Url:      https://github.com/restic/restic

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
%golang_build cmd/restic

%install
export BUILDDIR="$PWD/.build"
export IGNORE_SOURCES=1

%golang_install

%files
%_bindir/*
%doc *.md

%changelog
* Fri Mar 15 2019 Vitaly Chikunov <vt@altlinux.org> 0.9.4-alt1
- Initial build for Sisyphus
