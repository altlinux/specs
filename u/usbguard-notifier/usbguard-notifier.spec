%define _unpackaged_files_terminate_build 1

Name: usbguard-notifier
Version: 3.0
Release: alt1

Summary: Notification module for usbguard

License: GPL-2.0-only
Group: System/Configuration/Hardware
Url: https://gitlab.basealt.space/fomchenkovda/usbguard-notifier

Source: %name-%version.tar

BuildRequires(pre): rpm-build-xdg
BuildRequires: cmake
BuildRequires: qt6-tools-devel

Requires: usbguard-dbus

%description
Notification module for usbguard.

%prep
%setup

%build
%cmake
%cmake_build

%install
%cmake_install

%files
%_bindir/%name
%_datadir/%name/translations/*.qm
%_xdgconfigdir/autostart/%name.desktop

%changelog
* Thu Oct 31 2024 Dmitrii Fomchenkov <sirius@altlinux.org> 3.0-alt1
- don't use the systemd service
- update the doc
- migrate to qt6

* Mon May 06 2024 Dmitrii Fomchenkov <sirius@altlinux.org> 2.1-alt1
- Correct the service file
- Change the license format and macro for the build
- Add a service to startup

* Mon Oct 02 2023 Dmitrii Fomchenkov <sirius@altlinux.org> 2.0-alt1
- Change the way data is received from the bus
- Fix interface extraction
- Update translation

* Mon Sep 25 2023 Dmitrii Fomchenkov <sirius@altlinux.org> 1.0-alt1
- Initial build for ALT Linux
