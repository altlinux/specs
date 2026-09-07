%define _unpackaged_files_terminate_build 1

%def_with check

Name: meteo
Version: 1.0.0
Release: alt1

Summary: A forecast application using OpenWeatherMap API
License: GPL-3.0
Group: Graphical desktop/Other
Url: https://gitlab.com/bitseater/meteo

Source: %name-%version.tar

BuildRequires(pre): rpm-macros-meson
BuildRequires(pre): rpm-build-vala
BuildRequires: meson
BuildRequires: vala
BuildRequires: cmake
BuildRequires: pkgconfig(gee-0.8)
BuildRequires: pkgconfig(gtk4)
BuildRequires: pkgconfig(json-glib-1.0)
BuildRequires: pkgconfig(webkitgtk-6.0)
BuildRequires: pkgconfig(libadwaita-1)

%description
Know the forecast of the next hours & days.

Developed with Vala & Gtk, using OpenWeatherMap API.

Features:

- Current weather, with information about temperature, pressure, wind
  speed and direction, sunrise & sunset.
- Forecast for next 18 hours.
- Forecast for next five days.
- Choose your units (metric, imperial or british).
- Choose your city, with maps help.
- Awesome maps with weather info.
- System tray indicator.

%prep
%setup
sed -i "s|/data/screens|/screens|g" README.md
sed -i 's|^Categories=.*|Categories=Science;Maps;|' data/com.gitlab.bitseater.meteo.desktop.in

%build
%meson
%meson_build

%install
%meson_install

%find_lang %name --all-name

%check
%meson_test

%files -f %{name}.lang
%doc AUTHORS CHANGELOG CONTRIBUTING.md COPYING CREDITS.md README.md data/screens
%_bindir/*
%_desktopdir/*.desktop
%_man1dir/*
%_datadir/glib-2.0/schemas/*.xml
%_iconsdir/hicolor/*/*/*
%_datadir/metainfo/*%{name}.metainfo.xml

%changelog
* Mon Sep 07 2026 Nikolay Strelkov <snk@altlinux.org> 1.0.0-alt1
- New version 1.0.0.

* Fri Jun 27 2025 Nikolay Strelkov <snk@altlinux.org> 0.9.9.3-alt2
- Applied repocop fix for freedesktop-desktop

* Sun Jun 22 2025 Nikolay Strelkov <snk@altlinux.org> 0.9.9.3-alt1
Initial build for Sisyphus with support of Ayatana Indicator
