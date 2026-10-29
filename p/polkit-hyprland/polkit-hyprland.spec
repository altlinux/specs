%define _libexecdir %prefix/libexec

Name: polkit-hyprland
Version: 0.2.0
Release: alt1
License: BSD-3-Clause

Summary: A polkit authentication agent written in hyprtoolkit
Summary(ru_RU.UTF-8): Агент аутентификации polkit, написанный на hyprtoolkit

Group: Graphical desktop/Other

Url: https://github.com/hyprwm/hyprpolkitagent
Vcs: https://github.com/hyprwm/hyprpolkitagent.git

ExcludeArch: %ix86
Source: %name-%version.tar

BuildRequires: cmake
BuildRequires: clang libstdc++-devel

BuildRequires: pkgconfig(hyprtoolkit)
BuildRequires: pkgconfig(hyprutils)
BuildRequires: pkgconfig(hyprgraphics)
BuildRequires: pkgconfig(hyprlang)

BuildRequires: pkgconfig(sdbus-c++)
BuildRequires: pkgconfig(pixman-1)
BuildRequires: pkgconfig(libdrm)

BuildRequires: pkgconfig(xkbcommon)

%description
A simple polkit authentication agent for Hyprland, written in hyprtoolkit.

%description -l ru_RU.UTF-8
Простой агент аутентификации polkit для Hyprland, написанный на hyprtoolkit.

%prep
%setup

%build
%cmake -DCMAKE_CXX_COMPILER=clang++
%cmake_build

%install
%cmake_install

%files
%_userunitdir/hyprpolkitagent.service
%_libexecdir/hyprpolkitagent
%_datadir/dbus-1/services/*.service

%changelog
* Tue Oct 06 2026 Kirill Unitsaev <fiersik@altlinux.org> 0.2.0-alt1
- new version 0.2.0

* Fri Aug 01 2025 Kirill Unitsaev <fiersik@altlinux.org> 0.1.3-alt1
- new version 0.1.3 (with rpmrb script)

* Thu Jan 23 2025 Kirill Unitsaev <fiersik@altlinux.org> 0.1.2-alt2
- drop manual dependencies

* Sat Jan 11 2025 Kirill Unitsaev <fiersik@altlinux.org> 0.1.2-alt1
- new version 0.1.2 (with rpmrb script)

* Sat Dec 28 2024 Kirill Unitsaev <fiersik@altlinux.org> 0.1.1-alt1
- Initial build
