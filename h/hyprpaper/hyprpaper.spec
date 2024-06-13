Name: hyprpaper
Version: 0.7.0
Release: alt1
License: BSD-3-Clause

Summary: A blazing fast wayland wallpaper utility
Summary(ru_RU.UTF-8): Невероятно быстрая утилита для создания обоев wayland

Group: Graphical desktop/Other

Url: https://github.com/hyprwm/hyprpaper
Vcs: https://github.com/hyprwm/hyprpaper.git

Source0: %name-%version.tar

BuildRequires(pre): rpm-macros-cmake

BuildRequires: gcc-c++ cmake file
BuildRequires: libpango-devel libcairo-devel
BuildRequires: wayland-devel wayland-protocols
BuildRequires: libhyprlang-devel libglvnd-devel
BuildRequires: libwebp-devel libjpeg-devel libmagic-devel
BuildRequires: libwayland-client-devel libwayland-cursor-devel

%description
Hyprpaper is a blazing fast wayland wallpaper utility with IPC controls.

%description -l ru_RU.UTF-8
Невероятно быстрая утилита для создания обоев wayland с элементами управления IPC.

%prep
%setup

%build
%cmake
%cmake_build

%install
%cmake_install

%files
%doc README.md LICENSE
%_bindir/%name

%changelog
* Thu Jun 13 2024 Kirill Unitsaev <fiersik@altlinux.org> 0.7.0-alt1
- Initial build
