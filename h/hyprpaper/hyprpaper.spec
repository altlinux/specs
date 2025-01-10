Name: hyprpaper
Version: 0.7.3
Release: alt1
License: BSD-3-Clause

Summary: A blazing fast wayland wallpaper utility
Summary(ru_RU.UTF-8): Невероятно быстрая утилита для создания обоев wayland

Group: Graphical desktop/Other

Url: https://github.com/hyprwm/hyprpaper
Vcs: https://github.com/hyprwm/hyprpaper.git

ExcludeArch: i586
Source: %name-%version.tar

BuildRequires(pre): rpm-macros-cmake

BuildRequires: gcc-c++ cmake

BuildRequires: pkgconfig(hyprwayland-scanner)
BuildRequires: pkgconfig(hyprgraphics)
BuildRequires: pkgconfig(hyprutils) >= 0.2.4
BuildRequires: pkgconfig(hyprlang) >= 0.6.0

BuildRequires: pkgconfig(wayland-client)
BuildRequires: pkgconfig(wayland-cursor)
BuildRequires: pkgconfig(wayland-protocols)

BuildRequires: pkgconfig(libmagic)
BuildRequires: pkgconfig(cairo)
BuildRequires: pkgconfig(pango)
BuildRequires: pkgconfig(pangocairo)
BuildRequires: pkgconfig(libjpeg)
BuildRequires: pkgconfig(libwebp)

BuildRequires: pkgconfig(libjxl)
BuildRequires: pkgconfig(libjxl_cms)
BuildRequires: pkgconfig(libjxl_threads)

BuildRequires: libglvnd-devel

%description
Hyprpaper is a blazing fast wayland wallpaper utility with IPC controls.

%description -l ru_RU.UTF-8
Невероятно быстрая утилита для создания обоев wayland с элементами управления IPC.

%prep
%setup

%build
%cmake -DCMAKE_INSTALL_LIBDIR=lib
%cmake_build

%install
%cmake_install

%files
%doc README.md LICENSE
%_bindir/%name
%_userunitdir/%name.service

%changelog
* Fri Jan 10 2025 Kirill Unitsaev <fiersik@altlinux.org> 0.7.3-alt1
- new version 0.7.3 (with rpmrb script)
- add a systemd service
- cleanup spec

* Sat Aug 17 2024 Kirill Unitsaev <fiersik@altlinux.org> 0.7.1-alt1
- new version 0.7.1 (with rpmrb script)
- drop i586 support

* Thu Jun 13 2024 Kirill Unitsaev <fiersik@altlinux.org> 0.7.0-alt1
- Initial build
