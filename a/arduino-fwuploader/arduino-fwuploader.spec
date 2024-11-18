%global import_path github.com/arduino/arduino-fwuploader
Name:    arduino-fwuploader
Version: 2.4.1
Release: alt1

Summary: A Command Line Tool made to update the firmware and/or add SSL certificates for any Arduino board equipped with WINC or NINA Wi-Fi module.
License: AGPL-3.0
Group:   Other
Url:     https://github.com/arduino/arduino-fwuploader

Packager: Andrey Cherepanov <cas@altlinux.org>

Source: %name-%version.tar
Source1: vendor.tar

BuildRequires(pre): rpm-build-golang
BuildRequires: golang

%description
%summary

%prep
%setup
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
* Mon Nov 18 2024 Andrey Cherepanov <cas@altlinux.org> 2.4.1-alt1
- Initial build for Sisyphus.
