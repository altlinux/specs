Name: liri-settings
Version: 0.9.0
Release: alt2

Summary: Settings application and modules for Liri desktop
License: GPLv3
Group: Graphical desktop/Other
Url: https://github.com/lirios/settings

Source: %name-%version-%release.tar

BuildRequires: gcc-c++ cmake cmake-modules-liri qt5-tools-devel
BuildRequires: pkgconfig(Qt5Core)
BuildRequires: pkgconfig(Qt5Qml)
BuildRequires: pkgconfig(Qt5QuickControls2)
BuildRequires: pkgconfig(Qt5AccountsService)
BuildRequires: pkgconfig(Liri1Core)
BuildRequires: pkgconfig(polkit-agent-1)
BuildRequires: pkgconfig(xkeyboard-config)
BuildRequires: qml(Fluid.Controls)

%description
%summary

%prep
%setup

%build
%cmake
%cmake_build

%install
%cmakeinstall_std

%files
%_bindir/liri-settings
%_libdir/qt5/qml/Liri/Settings
%_datadir/applications/io.liri.Settings.desktop
%_datadir/dbus-1/services/io.liri.Settings.service
%_datadir/liri-settings

%changelog
* Tue Aug 10 2021 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.9.0-alt2
- v0.9.0-227-g2ded515

* Mon Oct 14 2019 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.9.0-alt1
- initial
