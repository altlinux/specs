%define _unpackaged_files_terminate_build 1

%def_with check

Name: mate-screenruler
Version: 1.0.0
Release: alt1

Summary: A screen ruler utility for MATE Desktop
License: GPL-3.0-or-later
Group: Graphical desktop/Other
Url: https://github.com/KeremSoke/mate-screenruler

Source: %name-%version.tar

BuildRequires(pre): rpm-macros-meson

BuildRequires: meson
BuildRequires: cmake
BuildRequires: pkgconfig(gtk+-3.0)

%description
MATE ScreenRuler is a lightweight on-screen ruler written with GTK3.
It helps designers, developers, and QA engineers measure pixel distances
precisely while working across multiple monitors or desktop environments.

The application is designed to behave like a native MATE utility but works
well on any modern GTK-based desktop. It follows the keyboard/mouse UX
conventions of the classic KRuler while adding quality-of-life
improvements such as center-origin measurements, high-contrast overlays,
and a global menu for desktops that support it.

%prep
%setup
sed -i "s|^Categories=.*|Categories=Graphics;RasterGraphics;2DGraphics;GTK;|" data/org.mate.screenruler.desktop.in

%build
%meson
%meson_build

%install
%meson_install

%find_lang %name

%check
%meson_test

%files -f %{name}.lang
%doc LICENSE README.md
%_bindir/mate-screenruler
%_desktopdir/org.mate.screenruler.desktop
%_datadir/glib-2.0/schemas/org.mate.screenruler.gschema.xml
%_datadir/mate-screenruler/ui/ui/prefs.ui
%_datadir/metainfo/org.mate.screenruler.appdata.xml

%changelog
* Sat Nov 14 2026 Nikolay Strelkov <snk@altlinux.org> 1.0.0-alt1
- Initial build for Sisyphus
