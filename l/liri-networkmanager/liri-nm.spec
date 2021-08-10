Name: liri-networkmanager
Version: 0.0.20210810
Release: alt1

Summary: NetworkManager support for Liri
License: GPLv3
Group: Graphical desktop/Other
Url: https://github.com/lirios/networkmanager

Source0: %name-%version-%release.tar

BuildRequires: gcc-c++ cmake cmake-modules-liri qt5-tools-devel
BuildRequires: pkgconfig(Qt5Core)
BuildRequires: pkgconfig(Qt5Qml)
BuildRequires: pkgconfig(Liri1Core)
BuildRequires: qml(Fluid.Controls)
BuildRequires: kf5-networkmanager-qt-devel
BuildRequires: kf5-modemmanager-qt-devel
BuildRequires: ModemManager-devel

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
%_libdir/qt5/qml/Liri/NetworkManager
%_datadir/liri-settings/modules/networkmanager
%_datadir/liri-settings/translations/modules/*.qm
%_datadir/liri-shell/statusarea/networkmanager

%changelog
* Tue Aug 10 2021 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.0.20210810-alt1
- initial
