%define commit 49c154a4
%define date 20241007

%global import_path github.com/arduino/arduino-cli
Name:    arduino-cli
Version: 1.1.0
Release: alt2

Summary: Arduino command line tool
License: GPL-3.0
Group:   Other
Url:     https://github.com/arduino/arduino-cli

Packager: Andrey Cherepanov <cas@altlinux.org>

Source: %name-%version.tar
Source1: vendor.tar

BuildRequires(pre): rpm-build-golang
BuildRequires: golang

%description
Arduino CLI is an all-in-one solution that provides Boards/Library Managers,
sketch builder, board detection, uploader, and many other tools needed to use
any Arduino compatible board and platform from command line or machine
interfaces.

%prep
%setup
subst 's/defaultVersionString *= .*/defaultVersionString = "%version"/' version/version.go
subst 's/commit *= .*/commit = "%commit"/' version/version.go
subst 's/date *= .*/date = "%date"/' version/version.go
tar xf %SOURCE1

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
%doc *.md
%_bindir/*

%changelog
* Tue Nov 19 2024 Andrey Cherepanov <cas@altlinux.org> 1.1.0-alt2
- Set application version.

* Mon Nov 18 2024 Andrey Cherepanov <cas@altlinux.org> 1.1.0-alt1
- Initial build for Sisyphus.
