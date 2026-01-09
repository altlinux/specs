%define _unpackaged_files_terminate_build 1

%define _libexecdir %_prefix/libexec

Name: hyprpolkitagent
Version: 0.1.3
Release: alt1

Summary: Polkit authentication agent written in QT/QML
License: BSD-3-Clause
Group: Graphical desktop/Other
URL: https://wiki.hyprland.org/Hypr-Ecosystem/hyprpolkitagent/
Vcs: https://github.com/hyprwm/hyprpolkitagent

Source: %name-%version.tar

BuildRequires(pre): rpm-macros-cmake
BuildRequires(pre): rpm-macros-systemd

BuildRequires: cmake
BuildRequires: gcc-c++
BuildRequires: pkgconfig(Qt6)
BuildRequires: pkgconfig(Qt6Quick)
BuildRequires: pkgconfig(hyprutils)
BuildRequires: pkgconfig(polkit-agent-1)
BuildRequires: pkgconfig(polkit-qt6-1)

%description
%summary.

%prep
%setup

%build
%cmake
%cmake_build

%install
%cmake_install

%files
%doc LICENSE README.md
%_userunitdir/%{name}.service
%_libexecdir/%name
%_datadir/dbus-1/services/org.hyprland.hyprpolkitagent.service

%changelog
* Fri Jan 09 2026 Nikolay Strelkov <snk@altlinux.org> 0.1.3-alt1
- Initial build for Sisyphus
