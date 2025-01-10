%define _libexecdir %prefix/libexec

Name: polkit-hyprland
Version: 0.1.1
Release: alt1
License: BSD-3-Clause

Summary: A polkit authentication agent written in QT/QML
Summary(ru_RU.UTF-8): Агент аутентификации polkit, написанный на QT/QML

%K6init

Group: Graphical desktop/Other

Url: https://github.com/hyprwm/hyprpolkitagent
Vcs: https://github.com/hyprwm/hyprpolkitagent.git

ExcludeArch: %ix86
Source: %name-%version.tar

BuildRequires(pre): rpm-build-kf6

BuildRequires: gcc-c++ cmake

BuildRequires: pkgconfig(hyprutils)
BuildRequires: pkgconfig(polkit-agent-1)
BuildRequires: pkgconfig(polkit-qt6-1)

BuildRequires: extra-cmake-modules qt6-base-devel
BuildRequires: qt6-declarative-devel qt6-tools-devel
BuildRequires: kf6-qqc2-desktop-style-devel

Requires: kf6-kirigami libqt6-quickcontrols2 kf6-qqc2-desktop-style libkf6sonnetui

%description
A simple polkit authentication agent for Hyprland, written in QT/QML.

%description -l ru_RU.UTF-8
Простой агент аутентификации polkit для Hyprland, написанный на QT/QML.

%prep
%setup

%build
%K6build

%install
%K6install

%files
%_userunitdir/hyprpolkitagent.service
%_libexecdir/hyprpolkitagent
%_datadir/dbus-1/services/*.service

%changelog
* Sat Dec 28 2024 Kirill Unitsaev <fiersik@altlinux.org> 0.1.1-alt1
- Initial build
