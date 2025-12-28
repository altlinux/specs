%define _unpackaged_files_terminate_build 1

%define appname com.milosmkv.MiLua

Name: milua
Version: 0.1.0
Release: alt1

Summary: Lightweight integrated development environment for Lua programming language.
License: GPL-3.0-or-later
Group: Development/Tools
Url: https://github.com/milos-mkv/MiLua

Source: %name-%version.tar

BuildRequires(pre): rpm-macros-meson
BuildRequires(pre): rpm-build-vala

BuildRequires: meson
BuildRequires: cmake
BuildRequires: vala-tools
BuildRequires: pkgconfig(lua)
BuildRequires: pkgconfig(gtk4)
BuildRequires: pkgconfig(gtksourceview-5)
BuildRequires: pkgconfig(gee-0.8)
BuildRequires: pkgconfig(libadwaita-1)
BuildRequires: pkgconfig(json-glib-1.0)
BuildRequires: pkgconfig(webkitgtk-6.0)
BuildRequires: vapi(webkitgtk-6.0)

%description
Lua IDE designed to make development smoother and more enjoyable.

It includes several powerful features:

* Custom Debugger

  A fully integrated debugger built specifically for Lua, giving you
  control over breakpoints, stepping, and inspecting runtime values.

* Project Management System

  Organize, manage, and navigate Lua projects with ease. The IDE provides
  tools for handling multiple files, folders, and project-level settings.

* Built-in Lua Documentation

  Directly access Lua 5.4 documentation within the IDE - no need to
  switch to the browser. Helpful for quick lookups while coding.
* User-Friendly Interface

  A clean, modern UI designed with productivity in mind.
  Built using Gtk 4 and libadwaita, it follows modern GNOME design
  principles and integrates naturally into Linux desktops.

%prep
%setup
sed -i "s|imgs/||" README.md
sed -i "s|lua5.4|lua|" src/meson.build
sed -i "s|Categories=.*|Categories=GTK;Development;Building;Debugger;IDE;|" data/com.milosmkv.MiLua.desktop.in

%build
%meson
%meson_build

%install
%meson_install

%check
%meson_test

%files
%doc COPYING README.md imgs/banner.png
%_bindir/milua
%_desktopdir/%{appname}.desktop
%_datadir/dbus-1/services/%{appname}.service
%_datadir/glib-2.0/schemas/%{appname}.gschema.xml
%_datadir/gtksourceview-5/styles/my-dark.xml
%_datadir/gtksourceview-5/styles/yaru-dark.xml
%_datadir/gtksourceview-5/styles/yaru.xml
%_iconsdir/hicolor/scalable/apps/%{appname}.png
%_iconsdir/hicolor/scalable/apps/lua.svg
%_iconsdir/hicolor/symbolic/apps/%{appname}-symbolic.png
%_iconsdir/hicolor/symbolic/apps/debug-symbolic.svg
%_iconsdir/hicolor/symbolic/apps/forward.svg
%_iconsdir/hicolor/symbolic/apps/logo4.png
%_iconsdir/hicolor/symbolic/apps/lua-symbolic.svg
%_iconsdir/hicolor/symbolic/apps/manual.svg
%_iconsdir/hicolor/symbolic/apps/right.svg
%_datadir/metainfo/%{appname}.metainfo.xml

%changelog
* Sun Dec 28 2025 Nikolay Strelkov <snk@altlinux.org> 0.1.0-alt1
- Initial build for Sisyphus
