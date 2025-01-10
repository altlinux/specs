Name: hyprsysteminfo
Version: 0.1.2
Release: alt1
License: BSD-3-Clause

Summary: A tiny qt6/qml application to display information about the running system
Summary(ru_RU.UTF-8): Крошечное приложение qt6/qml для отображения информации о запущенной системе

Group: Graphical desktop/Other

Url: https://github.com/hyprwm/hyprsysteminfo
Vcs: https://github.com/hyprwm/hyprsysteminfo.git

ExcludeArch: %ix86
Source: %name-%version.tar

BuildRequires(pre): rpm-build-kf6

BuildRequires: gcc-c++ cmake

BuildRequires: pkgconfig(hyprutils)

BuildRequires: pkgconfig(Qt6WaylandClient) 

BuildRequires: extra-cmake-modules qt6-base-devel
BuildRequires: qt6-declarative-devel qt6-tools-devel
BuildRequires: kf6-qqc2-desktop-style-devel

Requires: kf6-kirigami libqt6-quickcontrols2 kf6-qqc2-desktop-style

%description
A tiny qt6/qml application to display information about
the running system, or copy diagnostics data, without the terminal.

%description -l ru_RU.UTF-8
Небольшое приложение qt6/qml для отображения информации о запущенной
системе или копирования диагностических данных без терминала.

%prep
%setup

%build
%K6build

%install
%K6install

%files
%_bindir/hyprsysteminfo
%_desktopdir/hyprsysteminfo.desktop

%changelog
* Sat Jan 04 2025 Kirill Unitsaev <fiersik@altlinux.org> 0.1.2-alt1
- Initial build
