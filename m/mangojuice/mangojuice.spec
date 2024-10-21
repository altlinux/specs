%define APP_ID io.github.radiolamp.mangojuice

Name: mangojuice
Version: 0.7.1
Release: alt1

Summary: A graphical user interface for MangoHud configuration
License: GPL-3.0-or-later
Group: Graphics

Url: https://github.com/radiolamp/mangojuice
Vcs: https://github.com/radiolamp/mangojuice
Source: %name-%version.tar

Requires: mangohud
Requires: vulkan-tools
Requires: mesa-demos

BuildRequires(pre): rpm-macros-meson
BuildRequires: meson
BuildRequires: cmake
BuildRequires: vala-tools
BuildRequires: pkgconfig(libadwaita-1)
BuildRequires: pkgconfig(gee-0.8)

%description
MangoJuice is a graphical user interface application that allows users
to configure MangoHud, a Vulkan and OpenGL overlay for monitoring FPS,
temperature, CPU and GPU statistics, and more.

%prep
%setup

%build
%meson
%meson_build

%install
%meson_install
%find_lang --with-gnome %APP_ID

%files -f %APP_ID.lang
%_bindir/%name
%_desktopdir/%APP_ID.desktop
%_iconsdir/hicolor/scalable/apps/%{APP_ID}*.svg

%changelog
* Mon Oct 21 2024 Oleg Shchavelev <oleg@altlinux.org> 0.7.1-alt1
- New version 0.7.1
- Updated `Group` from `Graphics/Utilities` to `Graphics`

* Thu Oct 17 2024 Oleg Shchavelev <oleg@altlinux.org> 0.7.0-alt1
- Initial build
