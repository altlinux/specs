%global import_path github.com/cpuguy83/go-md2man
Name:     go-md2man
Version:  1.0.9
Release:  alt1

Summary:  Process markdown into manpages
License:  MIT
Group:    Other
Url:      https://github.com/cpuguy83/go-md2man

Packager: Mikhail Gordeev <obirvalger@altlinux.org>

Source:   %name-%version.tar

BuildRequires(pre): rpm-build-golang
BuildRequires: golang

Conflicts: golang-github-cpuguy83-go-md2man

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
%golang_build .

%install
export BUILDDIR="$PWD/.build"
export IGNORE_SOURCES=1

%golang_install

%files
%_bindir/*
%doc *.md

%changelog
* Thu Mar 14 2019 Mikhail Gordeev <obirvalger@altlinux.org> 1.0.9-alt1
- Initial build for Sisyphus
