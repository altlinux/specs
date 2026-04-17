%define _unpackaged_files_terminate_build 1
%define app_id ru.basealt.WeatherAdw

Name: alt-weather-adw
Version: 1.0.9
Release: alt2

# Missing alt-identify-client on i586
ExcludeArch: i586

Summary: Weather forecast
License: GPL-3.0-or-later
Group: Graphical desktop/GNOME

Url: https://altlinux.space/Basealt/Alt-Weather-Adwaita
Vcs: https://altlinux.space/Basealt/Alt-Weather-Adwaita
Source: %name-%version.tar

Requires: alt-identify-client

BuildRequires(pre): rpm-macros-meson rpm-build-vala
BuildRequires: meson
BuildRequires: vala
BuildRequires: blueprint-compiler
BuildRequires: pkgconfig(json-glib-1.0)
BuildRequires: pkgconfig(libadwaita-1)
BuildRequires: pkgconfig(gee-0.8)

%description
Detailed and convenient weather forecast for your OS Alt.
View detailed weather information for your location or any other location
for the next 24 hours or 10 days.
Features of Weather for OS Alt:
* Hourly weather forecast for 24 hours;
* Weather summary for the next 10 days;
* Ability to choose a weather source between Yandex Weather and Gismeteo;
* Detailed weather information including: humidity, pressure, wind speed,
water temperature, magnetic activity, UV index, and sunrise and sunset times;
* Automatic detection of your location;
* GTK4/Libadwaita interface adapted for desktop, tablet, and mobile devices.

Works only on ALT Workstation.

Note: the application is intended to be used with the default package set of
ALT Workstation. Removing system packages included in the base installation may
affect correct operation of the application.

%prep
%setup

%build
%meson
%meson_build

%install
%meson_install
%find_lang --with-gnome alt-weather

%files -f alt-weather.lang
%_bindir/alt-weather
%_desktopdir/%app_id.desktop
%_datadir/metainfo/%app_id.metainfo.xml
%_iconsdir/hicolor/*/apps/%{app_id}*.svg
%_datadir/glib-2.0/schemas/%app_id.gschema.xml
%_datadir/dbus-1/services/%app_id.service
%doc README.md

%changelog
* Fri Apr 17 2026 Alexander Davydzik <paladindev@altlinux.org> 1.0.9-alt2
- updated description

* Mon Dec 15 2025 Alexander Davydzik <paladindev@altlinux.org> 1.0.9-alt1
- initial build
