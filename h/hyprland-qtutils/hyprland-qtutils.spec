Name: hyprland-qtutils
Version: 0.1.2
Release: alt1
License: BSD-3-Clause

Summary: Hyprland QT/qml utility apps
Summary(ru_RU.UTF-8): Полезные приложения Hyprland QT/qml

%K6init

Group: Graphical desktop/Other

Url: https://github.com/hyprwm/hyprland-qtutils
Vcs: https://github.com/hyprwm/hyprland-qtutils.git

ExcludeArch: i586
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
Qt/qml utilities that might be used by various hypr* apps.

%description -l ru_RU.UTF-8
Утилиты qt/qml, которые могут использоваться различными приложениями hypr*.

%prep
%setup

%build
%K6build

%install
%K6install

%files
%_bindir/hyprland-dialog
%_bindir/hyprland-update-screen

%changelog
* Wed Jan 08 2025 Kirill Unitsaev <fiersik@altlinux.org> 0.1.2-alt1
- Initial build
