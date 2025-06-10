%define commit 9d1f5098b716681d087cca695ad714218a18d4e8
%global shortcommit %(c=%{commit}; echo ${c:0:7})

Name:    joycond
Version: 0.1.0
Release: alt1.git%shortcommit

Summary: userspace daemon to combine joy-cons from the hid-nintendo kernel driver
License: GPL-3.0
Group:   Other
Url:     https://github.com/DanielOgorchock/joycond

# Source-url: https://github.com/DanielOgorchock/joycond/archive/%commit/joycond-%commit.tar.gz
Source: %name-%version.tar

BuildRequires(pre): rpm-macros-cmake
BuildRequires: cmake gcc-c++
BuildRequires: libevdev-devel libudev-devel

%description
joycond is a linux daemon which uses the evdev devices provided by
hid-nintendo (formerly known as hid-joycon) to implement joycon pairing.

%prep
%setup

%build
%cmake
%cmake_build

%install
%cmake_install
mkdir -p %buildroot%_modulesloaddir/
mkdir -p %buildroot%_unitdir/
mkdir -p %buildroot%_udevrulesdir/
mv %buildroot/etc/modules-load.d/%name.conf %buildroot%_modulesloaddir/%name.conf
mv %buildroot/etc/systemd/system/%name.service %buildroot%_unitdir/%name.service
mv %buildroot/lib/udev/rules.d/{72,89}-joycond.rules %buildroot%_udevrulesdir/

%files
%doc LICENSE README.md
%_bindir/%name
%_unitdir/%name.service
%_udevrulesdir/72-%name.rules
%_udevrulesdir/89-%name.rules
%_modulesloaddir/%name.conf

%changelog
* Tue Mar 04 2025 Sergey Palcheh <minergenon@altlinux.org> 0.1.0-alt1.git9d1f509
- initial build for ALT Sisyphus

