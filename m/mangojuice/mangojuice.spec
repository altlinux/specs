%define _unpackaged_files_terminate_build 1
%define APP_ID io.github.radiolamp.mangojuice

Name: mangojuice
Version: 0.8.2
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
BuildRequires: vala
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
%find_lang --with-gnome %name

%files -f %name.lang
%_bindir/%name
%_desktopdir/%APP_ID.desktop
%_iconsdir/hicolor/*/apps/%{APP_ID}*.svg
%_iconsdir/hicolor/scalable/apps/*.svg

%changelog
* Sat Mar 01 2025 Oleg Shchavelev <oleg@altlinux.org> 0.8.2-alt1
- New version 0.8.2
- Enable strict mode for unpackaged files
- Add scalable icons to package files list

* Sat Feb 01 2025 Oleg Shchavelev <oleg@altlinux.org> 0.8.1-alt1
- New version 0.8.1
- Changed macro variable for searching language files

* Fri Jan 10 2025 Oleg Shchavelev <oleg@altlinux.org> 0.8.0-alt1
- New version 0.8.0

* Sat Jan 04 2025 Oleg Shchavelev <oleg@altlinux.org> 0.7.9-alt1
- New version 0.7.9

* Fri Nov 08 2024 Oleg Shchavelev <oleg@altlinux.org> 0.7.8-alt1
- New version 0.7.8

* Fri Nov 01 2024 Oleg Shchavelev <oleg@altlinux.org> 0.7.7-alt1
- New version 0.7.7

* Sun Oct 27 2024 Oleg Shchavelev <oleg@altlinux.org> 0.7.5-alt1
- New version 0.7.5
- Optimize BuildRequires

* Mon Oct 21 2024 Oleg Shchavelev <oleg@altlinux.org> 0.7.1-alt1
- New version 0.7.1
- Updated `Group` from `Graphics/Utilities` to `Graphics`

* Thu Oct 17 2024 Oleg Shchavelev <oleg@altlinux.org> 0.7.0-alt1
- Initial build
