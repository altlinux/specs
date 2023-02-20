%global import_path github.com/OpenPrinting/ipp-usb
Name:    ipp-usb
Version: 0.9.23
Release: alt1

Summary: ipp-usb -- HTTP reverse proxy, backed by IPP-over-USB connection to device
License: BSD-2-Clause
Group:   Other
Url:     https://github.com/OpenPrinting/ipp-usb

Packager: Mikhail Gordeev <obirvalger@altlinux.org>

Source: %name-%version.tar

BuildRequires(pre): rpm-build-golang
BuildRequires: golang pkgconfig(libusb-1.0) pkgconfig(avahi-client)

%description
%summary.

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
%doc *.md
%_bindir/*

%changelog
* Sun Feb 19 2023 Mikhail Gordeev <obirvalger@altlinux.org> 0.9.23-alt1
- Initial build for Sisyphus
