Name: plasma-applet-netspeed-widget
Version: 3.1
Release: alt1

Summary: Plasma widget that displays the currently used network bandwidth
License: GPL-2.0
Group: Graphical desktop/KDE

Url: https://github.com/dfaust/plasma-applet-netspeed-widget
Vcs: https://github.com/dfaust/plasma-applet-netspeed-widget

Source: %name-%version.tar

BuildArch: noarch

BuildRequires(pre): rpm-build-kf6
BuildRequires: cmake extra-cmake-modules gcc-c++ qt6-base-devel 
BuildRequires: plasma6-lib-devel pkgconfig(Qt6Qml) kf6-kpackage-devel
BuildRequires: kf6-kcoreaddons-devel kf6-kwindowsystem-devel

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
%_datadir/metainfo/*.xml
%_datadir/plasma/plasmoids/org.kde.netspeedWidget/*
%doc README.md

%changelog
* Wed Apr 02 2025 Aleksandr Shamaraev <shad@altlinux.org> 3.1-alt1
- Initial build for ALT Linux.

