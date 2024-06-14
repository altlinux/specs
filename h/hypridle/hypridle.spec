Name: hypridle
Version: 0.1.2
Release: alt1
License: BSD-3-Clause

Summary: Hyprland's idle daemon
Summary(ru_RU.UTF-8): Служба управления простоями для Hyprland

Group: Graphical desktop/Other

Url: https://github.com/hyprwm/hypridle
Vcs: https://github.com/hyprwm/hypridle.git

Source0: %name-%version.tar

BuildRequires(pre): rpm-macros-cmake

BuildRequires: gcc-c++ cmake
BuildRequires: libsdbus-cpp-devel libhyprlang-devel
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
subst "s|lib/systemd/user|%_unitdir|" CMakeLists.txt

%build
%cmake
%cmake_build

%install
%cmake_install

%files
%_bindir/%name
%_unitdir/%name.service

%changelog
* Fri Jun 14 2024 Kirill Unitsaev <fiersik@altlinux.org> 0.1.2-alt1
- Initial build
