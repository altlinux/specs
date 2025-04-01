%define _unpackaged_files_terminate_build 1
%define xdg_name org.adishatz.Screenshot

Name: screenshot
Version: 0.7.1
Release: alt2

Summary: A screenshot app for GNOME based desktops
License: GPL-3.0
Group: Graphical desktop/GNOME
Url: https://gitlab.gnome.org/gnumdk/screenshot
VCS: https://gitlab.gnome.org/gnumdk/screenshot

Source0: %name-%version.tar

BuildRequires(pre): rpm-macros-meson
BuildRequires: meson
BuildRequires: blueprint-compiler
BuildRequires: desktop-file-utils
BuildRequires: libgtk4-devel
BuildRequires: libadwaita-gir-devel
BuildRequires: libadwaita-devel
BuildRequires: libportal-devel
BuildRequires: libportal-gtk4-devel

%description
%summary.

%prep
%setup

%build
%meson
%meson_build

%install
%meson_install
%find_lang %name

%files -f %name.lang
%_bindir/%xdg_name
%_datadir/glib-2.0/schemas/%xdg_name.gschema.xml
%_desktopdir/%xdg_name.desktop
%_datadir/metainfo/%xdg_name.metainfo.xml
%_iconsdir/hicolor/*/apps/*.svg

%changelog
* Tue Apr 01 2025 Alexey Volkov <qualimock@altlinux.org> 0.7.1-alt2
- remove unused BR: cmake

* Thu Jan 23 2025 Alexey Volkov <qualimock@altlinux.org> 0.7.1-alt1
- New version 0.7.1

* Sun Sep 15 2024 Alexey Volkov <qualimock@altlinux.org> 0.6.0-alt1
- Initial build for ALT
