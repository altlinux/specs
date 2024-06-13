Name: hyprpicker
Version: 0.3.0
Release: alt1
License: BSD-3-Clause

Summary: A wlroots-compatible Wayland color picker
Summary(ru_RU.UTF-8): Средство выбора цвета Wayland, совместимое с wlroots

Group: Graphics

Url: https://github.com/hyprwm/hyprpicker
Vcs: https://github.com/hyprwm/hyprpicker.git

ExcludeArch: i586
Source0: %name-%version.tar

BuildRequires(pre): rpm-macros-cmake

BuildRequires: gcc-c++ cmake
BuildRequires: wayland-protocols
BuildRequires: libxkbcommon-devel
BuildRequires: libjpeg-devel libglvnd-devel
BuildRequires: libcairo-devel libpango-devel
BuildRequires: libwayland-client-devel libwayland-cursor-devel
BuildRequires: pkgconfig(libffi) pkgconfig(bzip2)

%description
A wlroots-compatible Wayland color picker that does not suck.

%description -l ru_RU.UTF-8
Совместимый с wlroots инструмент выбора цвета для Wayland.

%prep
%setup

%build
%cmake -DCMAKE_INSTALL_MANDIR=%_mandir
%cmake_build

%install
%cmake_install

%files
%_man1dir/*.1.*
%_bindir/%name
%doc README.md LICENSE

%changelog
* Thu Jun 13 2024 Kirill Unitsaev <fiersik@altlinux.org> 0.3.0-alt1
- Initial build
