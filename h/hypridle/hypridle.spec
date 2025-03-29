Name: hypridle
Version: 0.1.6
Release: alt1
License: BSD-3-Clause

Summary: Hyprland's idle daemon
Summary(ru_RU.UTF-8): Служба управления простоями для Hyprland

Group: Graphical desktop/Other

Url: https://github.com/hyprwm/hypridle
Vcs: https://github.com/hyprwm/hypridle.git

ExcludeArch: i586
Source: %name-%version.tar

BuildRequires(pre): rpm-macros-cmake

BuildRequires: gcc-c++ cmake

BuildRequires: pkgconfig(hyprwayland-scanner)
BuildRequires: pkgconfig(hyprland-protocols)
BuildRequires: pkgconfig(hyprutils)
BuildRequires: pkgconfig(hyprlang)

BuildRequires: pkgconfig(sdbus-c++)
BuildRequires: wayland-protocols wayland-devel libwayland-client-devel

%description
Hypridle supports commands to lock, unlock, and go
to sleep using dbus and loginctl.
Configuration takes place via the hypridle.conf file.

%description -l ru_RU.UTF-8
Hypridle поддерживает команды блокировки, разблокировки и перехода
в сон с помощью dbus и loginctl.
Конфигурирование происходит через файл hypridle.conf.

%prep
%setup

%build
%cmake
%cmake_build

%install
%cmake_install

%files
%_bindir/%name
%_userunitdir/%name.service
%_datadir/hypr/%name.conf

%changelog
* Sat Mar 29 2025 Kirill Unitsaev <fiersik@altlinux.org> 0.1.6-alt1
- new version 0.1.6 (with rpmrb script)
- added support for hyprland-lock-notify protocol
- drop i586 support

* Wed Mar 26 2025 Kirill Unitsaev <fiersik@altlinux.org> 0.1.5-alt1
- new version 0.1.5 (with rpmrb script)
- pack base config

* Thu Sep 19 2024 Kirill Unitsaev <fiersik@altlinux.org> 0.1.2-alt2
- Fix the systemd service path (ALT bug 51488)

* Fri Jun 14 2024 Kirill Unitsaev <fiersik@altlinux.org> 0.1.2-alt1
- Initial build
