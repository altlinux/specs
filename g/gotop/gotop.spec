%global import_path github.com/cjbassi/gotop
Name:     gotop
Version:  2.0.0
Release:  alt1

Summary:  A terminal based graphical activity monitor inspired by gtop and vtop
License:  AGPL-3.0
Group:    Other
Url:      https://github.com/cjbassi/gotop

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
%golang_build .

%install
export BUILDDIR="$PWD/.build"
export IGNORE_SOURCES=1

%golang_install

%files
%_bindir/*
%doc *.md

%changelog
* Tue Feb 05 2019 Mikhail Gordeev <obirvalger@altlinux.org> 2.0.0-alt1
- Initial build for Sisyphus
