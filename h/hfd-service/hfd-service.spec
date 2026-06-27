%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1

%define _libexecdir %_prefix/libexec

Name: hfd-service
Version: 0.2.4
Release: alt1

Summary: Tools to detect and configure human feedback devices
License: LGPL-3.0-only
Group: Graphical desktop/Other
Url: https://gitlab.com/ubports/development/core/hfd-service

Source: %name-%version.tar

BuildRequires(pre): rpm-build-cmake
BuildRequires(pre): rpm-macros-qt5

BuildRequires: cmake
BuildRequires: gcc-c++
BuildRequires: pkgconfig(udev)
BuildRequires: pkgconfig(deviceinfo)
BuildRequires: pkgconfig(dbus-1)
BuildRequires: pkgconfig(accountsservice)
BuildRequires: pkgconfig(Qt5Core)
BuildRequires: pkgconfig(libglibutil)
BuildRequires: pkgconfig(libgbinder)
BuildRequires: pkgconfig(Qt5Feedback)
BuildRequires: ayatana-cmake-modules
BuildRequires: qt5-declarative-devel
BuildRequires: pkgconfig(systemd)

%description
Human feedback device service is a Dbus activated service that manages
human feedback devices such as LEDs and vibrators on mobile devices.

This package contains tools for accessing the HFD service, Qt feedback
library extension for accessing the HFD service and the HFD system
service.

%prep
%setup

%build
%cmake \
       -Dqmlplugindump_exe=%_qt5_bindir/qmlplugindump
%cmake_build

%install
%cmake_install

%files
%doc AUTHORS ChangeLog README.md
%_sysconfdir/dbus-1/system.d/com.lomiri.hfd.conf
%_bindir/hfd-service-tools-leds
%_bindir/hfd-service-tools-vibrator
%_libdir/qt5/plugins/feedback/libqtfeedback_hfd.so
%_qt5_qmldir/Hfd/libhfd-qml.so
%_qt5_qmldir/Hfd/qmldir
%_libexecdir/hfd-service
%_unitdir/hfd-service.service
%_datadir/accountsservice/interfaces/com.lomiri.hfd.AccountsService.Settings.xml
%_datadir/dbus-1/interfaces/com.lomiri.hfd.AccountsService.Settings.xml
%_datadir/dbus-1/system-services/com.lomiri.hfd.service

%changelog
* Sat Jun 27 2026 Nikolay Strelkov <snk@altlinux.org> 0.2.4-alt1
- New version 0.2.4.

* Fri Jul 18 2025 Nikolay Strelkov <snk@altlinux.org> 0.2.3-alt1
- Initial build for Sisyphus
