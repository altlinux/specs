%global import_path github.com/elves/elvish
Name:    elvish
Version: 0.21.0
Release: alt1

Summary: Powerful scripting language & versatile interactive shell
License: BSD-2-Clause
Group:   Other
Url:     https://github.com/elves/elvish

Packager: Mikhail Gordeev <obirvalger@altlinux.org>

Source: %name-%version.tar

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
%golang_build cmd/elvish

%install
export BUILDDIR="$PWD/.build"
export IGNORE_SOURCES=1

%golang_install

%files
%doc *.md
%_bindir/*

%changelog
* Thu Nov 07 2024 Mikhail Gordeev <obirvalger@altlinux.org> 0.21.0-alt1
- Initial build for Sisyphus
