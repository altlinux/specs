%define _unpackaged_files_terminate_build 1

%def_with check

%define appname com.github.maoschanz.DynamicWallpaperEditor

Name: dynamic-wallpaper-editor
Version: 2.99
Release: alt1.git.6bf092c

Summary: Create or edit dynamic wallpapers for GNOME Shell, Cinnamon and MATE
License: GPL-3.0-or-later
Group: Graphical desktop/Other
Url: https://github.com/maoschanz/dynamic-wallpaper-editor

Source: %name-%version.tar

BuildRequires(pre): meson
BuildRequires(pre): rpm-build-python3

BuildRequires: cmake
BuildRequires: /usr/bin/glib-compile-schemas
BuildRequires: /usr/bin/itstool
BuildRequires: pkgconfig(gio-2.0)

%if_with check
BuildRequires: /usr/bin/desktop-file-validate
BuildRequires: /usr/bin/appstream-util
%endif

BuildArch: noarch

Requires: libgtk+3-gir

%description
Dynamic Wallpaper Editor is a simple utility to create or edit dynamic
wallpapers for the GNOME Shell, Cinnamon and MATE desktop.

The duration of each picture and each transition can be set separately or
globally. The wallpaper will fit the daylight if its total duration is
exactly 24 hours.

%prep
%setup
sed -i "s/'validate'/'validate', '--nonet'/" data/meson.build
sed -i "s/org.mate.desktop.background/org.mate.background/" src/main.py
sed -i "s/Categories=.*/Categories=GTK;Graphics;2DGraphics;/" data/com.github.maoschanz.DynamicWallpaperEditor.desktop.in

%build
%meson
%meson_build

%install
%meson_install

%find_lang %name --with-gnome

%check
%meson_test

%files -f %{name}.lang
%doc LICENSE README.md
%_bindir/%name
%_desktopdir/%{appname}.desktop
%dir %_datadir/%name
%_datadir/%name/*
%_datadir/glib-2.0/schemas/%{appname}.gschema.xml
%_iconsdir/hicolor/scalable/apps/%{appname}-symbolic.svg
%_iconsdir/hicolor/scalable/apps/%{appname}.svg
%_datadir/metainfo/%{appname}.appdata.xml

%changelog
* Wed Apr 22 2026 Nikolay Strelkov <snk@altlinux.org> 2.99-alt1.git.6bf092c
- Initial build for Sisyphus
