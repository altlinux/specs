Name: liri-calc
Version: 1.3.0
Release: alt1

Summary: Calculator for the Liri desktop.
License: GPLv3
Group: Graphical desktop/Other
Url: https://github.com/lirios/calculator

Source: %name-%version-%release.tar

BuildRequires: cmake cmake-modules-liri
BuildRequires: pkgconfig(Qt5Core)
BuildRequires: pkgconfig(Qt5Qml)
BuildRequires: pkgconfig(Qt5QuickControls2)
BuildRequires: pkgconfig(Qt5Svg)
BuildRequires: qml(Fluid.Core)
BuildRequires: qt5-tools-devel

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
%_bindir/liri-calculator
%_datadir/applications/io.liri.Calculator.desktop
%_datadir/liri-calculator
%_iconsdir/*/*/*/*.png

%changelog
* Wed Aug 19 2020 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.3.0-alt1
- initial
