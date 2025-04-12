%define nameL org.kde.olib.thermalmonitor

Name: plasma-applet-thermalmonitor
Version: 0.2.6
Release: alt1

Summary: A KDE Plasmoid for showing system temperatures
License: MIT
Group: Graphical desktop/KDE

Url: https://invent.kde.org/olib/thermalmonitor
Vcs: https://invent.kde.org/olib/thermalmonitor

Source: %name-%version.tar

BuildArch: noarch

Provides: plasma-applet-thermal-monitor = %EVR
Obsoletes: plasma-applet-thermal-monitor < %EVR

BuildRequires(pre): rpm-build-kf6
BuildRequires: cmake extra-cmake-modules gcc-c++ pkgconfig(Qt6Qml)
BuildRequires: plasma6-lib-devel kf6-kpackage-devel kf6-kcoreaddons-devel
BuildRequires: kf6-kwindowsystem-devel

%description
%summary

%prep
%setup

%build
%K6cmake
%K6make

%install
%K6install

%files
%doc *.md *.txt
%_datadir/metainfo/%nameL.appdata.xml
%_datadir/plasma/plasmoids/%nameL/*

%changelog
* Sun Apr 12 2025 Aleksandr Shamaraev <shad@altlinux.org> 0.2.6-alt1
- Initial build for ALT Linux.
