%define _unpackaged_files_terminate_build 1
%def_with check

%define import_path github.com/maximbaz/yubikey-touch-detector

Name:yubikey-touch-detector
Version: 1.13.0
Release: alt1

Summary: A tool to detect when your YubiKey is waiting for a touch
License: ISC
Group: System/Configuration/Other
VCS: https://github.com/max-baz/yubikey-touch-detector
Url: https://github.com/max-baz/yubikey-touch-detector

Source0: %name-%version.tar
Source1: %name-%version-vendor.tar

Patch0: %name-%version-alt.patch

BuildRequires(pre): rpm-build-golang
BuildRequires: libgpgme-devel
BuildRequires: scdoc

%description
This  is a  tool that  can  detect when  YubiKey is  waiting for  your
touch. It  is designed to  be integrated  with other UI  components to
display a visible indicator.

%prep
%setup -a1
%patch0 -p1

export BUILDDIR="$PWD/.build"
export IMPORT_PATH="%import_path"
export GOPATH="$BUILDDIR:%go_path"

%golang_prepare

%build
export BUILDDIR="$PWD/.build"
export IMPORT_PATH="%import_path"
export GOPATH="$BUILDDIR:%go_path"

%golang_build .

scdoc < ./yubikey-touch-detector.1.scd > yubikey-touch-detector.1

%install
export BUILDDIR="$PWD/.build"
export GOPATH="$BUILDDIR:%go_path"
export IGNORE_SOURCES=1

%golang_install

install -vDm 644 yubikey-touch-detector.service \
        %buildroot/%_userunitdir/yubikey-touch-detector.service

install -vDm 644 yubikey-touch-detector.socket \
        %buildroot/%_userunitdir/yubikey-touch-detector.socket

install -vDm 644 yubikey-touch-detector.1 \
        %buildroot/%_man1dir/yubikey-touch-detector.1

%check
%gotest

%files
%doc LICENSE README.md service.conf.example
%_bindir/yubikey-touch-detector
%_userunitdir/yubikey-touch-detector.service
%_userunitdir/yubikey-touch-detector.socket
%_man1dir/yubikey-touch-detector.1.*

%changelog
* Sun Dec 07 2025 Egor Ignatov <egori@altlinux.org> 1.13.0-alt1
- Initila build for ALT.
