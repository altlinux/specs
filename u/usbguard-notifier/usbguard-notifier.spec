%define _unpackaged_files_terminate_build 1

Name: usbguard-notifier
Version: 2.0
Release: alt1

Summary: Notification module for usbguard

License: GPLv2
Group: System/Configuration/Hardware
Url: https://gitlab.basealt.space/fomchenkovda/usbguard-notifier

Source: %name-%version.tar

BuildRequires: cmake
BuildRequires: gcc-c++
BuildRequires: qt5-tools-devel
Requires: usbguard-dbus

%description
Notification module for usbguard.

%prep
%setup

%build
%cmake
%cmake_build

%install
%cmakeinstall_std

%files
%_bindir/%name
%_datadir/%name
%_libexecdir/systemd/user/%name.service

%changelog
* Mon Oct 02 2023 Dmitrii Fomchenkov <sirius@altlinux.org> 2.0-alt1
- Change the way data is received from the bus
- Fix interface extraction
- Update translation

* Mon Sep 25 2023 Dmitrii Fomchenkov <sirius@altlinux.org> 1.0-alt1
- Initial build for ALT Linux
