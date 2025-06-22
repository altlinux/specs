%define _unpackaged_files_terminate_build 1

Name: meteo
Version: 0.9.9.3
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
BuildRequires: pkgconfig(gtk+-3.0)
BuildRequires: pkgconfig(json-glib-1.0)
BuildRequires: pkgconfig(webkit2gtk-4.0)
BuildRequires: pkgconfig(ayatana-appindicator3-0.1)
BuildRequires: libayatana-appindicator3-vala

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

%build
%meson
%meson_build

%install
%meson_install

%find_lang %name --all-name

%files -f %{name}.lang
%doc AUTHORS CHANGELOG CONTRIBUTING.md COPYING CREDITS.md README.md data/screens
%_bindir/*
%_desktopdir/*.desktop
%_man1dir/*
%_datadir/glib-2.0/schemas/*.xml
%_iconsdir/hicolor/*/*/*
%_datadir/metainfo/*%{name}.appdata.xml

%changelog
* Sun Jun 22 2025 Nikolay Strelkov <snk@altlinux.org> 0.9.9.3-alt1
Initial build for Sisyphus with support of Ayatana Indicator
