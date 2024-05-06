%define _unpackaged_files_terminate_build 1

Name: usbguard-notifier
Version: 2.1
Release: alt1

Summary: Notification module for usbguard

License: GPL-2.0-only
Group: System/Configuration/Hardware
Url: https://gitlab.basealt.space/fomchenkovda/usbguard-notifier

Source: %name-%version.tar

BuildRequires: cmake
BuildRequires: rpm-build-systemd
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
%cmake_install

%post
%systemd_user_post %name.service

%preun
%systemd_user_preun %name.service

%postun
%systemd_user_postun %name.service

%files
%_bindir/%name
%_datadir/%name
%_libexecdir/systemd/user/%name.service

%changelog
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
