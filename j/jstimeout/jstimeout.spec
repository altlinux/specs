%global import_path github.com/0x90shell/jstimeout

Name:    jstimeout
Version: 1.0.0
Release: alt1

Summary: Auto-disconnect idle Bluetooth gamepads after a configurable timeout
License: MIT
Group:   System/Configuration/Hardware
URL:     https://github.com/0x90shell/jstimeout

Source: %name-%version.tar

BuildRequires(pre): rpm-macros-golang
BuildRequires: rpm-build-golang

%description
jstimeout automatically disconnects idle Bluetooth gamepads after a
configurable timeout. It matches /dev/input devices with Bluetooth MAC
addresses and forces a disconnect. Originally written for DS3 controllers,
whose idle timeout cannot be configured without a PS3, but works with any
controller listed in the devices file.

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

mkdir -p %buildroot%_datadir/%name
install -pm 644 .jstimeout.devices %buildroot%_datadir/%name/devices.example

mkdir -p %buildroot%_userunitdir
install -pm 644 jstimeout.service %buildroot%_userunitdir/%name.service

%files
%doc LICENSE README.md
%_bindir/%name
%_datadir/%name
%_userunitdir/%name.service

%changelog
* Fri Aug 21 2026 Sergey Palcheh <minergenon@altlinux.org> 1.0.0-alt1
- Initial build for Sisyphus
