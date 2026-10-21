%define commit 39d5728d41b70840342ddc116a59125b337fbde2
%global shortcommit %(c=%{commit}; echo ${c:0:7})

Name:    joycond
Version: 0.1.0
Release: alt1.git%shortcommit

Summary: Userspace daemon to combine joy-cons from the hid-nintendo kernel driver
License: GPL-3.0
Group:   Other
Url:     https://github.com/DanielOgorchock/joycond

# Source-url: https://github.com/DanielOgorchock/joycond/archive/%commit/joycond-%commit.tar.gz
Source: %name-%version.tar

BuildRequires(pre): rpm-macros-cmake
BuildRequires: cmake gcc-c++
BuildRequires: libevdev-devel libudev-devel

Requires: acl
Requires: udev

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
install -Dpm0644 doc/%name.1 %buildroot%_man1dir/%name.1
mkdir -p %buildroot%_modulesloaddir/
mv %buildroot/etc/modules-load.d/%name.conf %buildroot%_modulesloaddir/%name.conf

%files
%doc LICENSE README.md
%_bindir/%name
%_man1dir/%name.1*
%_unitdir/%name.service
%_udevrulesdir/72-%name.rules
%_udevrulesdir/89-%name.rules
%_modulesloaddir/%name.conf
%dir %_datadir/metainfo
%_datadir/metainfo/com.github.DanielOgorchock.joycond.metainfo.xml

%changelog
* Wed Oct 21 2026 Sergey Palcheh <minergenon@altlinux.org> 0.1.0-alt1.git39d5728
- new git snapshot 39d5728 (2025-04-12)

* Tue Mar 04 2025 Sergey Palcheh <minergenon@altlinux.org> 0.1.0-alt1.git9d1f509
- initial build for ALT Sisyphus

