%define _unpackaged_files_terminate_build 1
%define app_id org.altlinux.Weather

Name: alt-weather
Version: 1.0.6
Release: alt1

# Missing alt-identify-client on i586
ExcludeArch: i586

Summary: Weather forecast
License: GPL-3.0-or-later
Group: Graphical desktop/GNOME

Url: https://altlinux.space/ALTLinux/ALTWeather
Vcs: https://altlinux.space/ALTLinux/ALTWeather
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
%_desktopdir/%app_id.desktop
%_datadir/metainfo/%app_id.metainfo.xml
%_iconsdir/hicolor/*/apps/%{app_id}*.svg
%_datadir/glib-2.0/schemas/%app_id.gschema.xml
%_datadir/dbus-1/services/%app_id.service
%doc README.md

%changelog
* Mon Dec 01 2025 Alexander Davydzik <paladindev@altlinux.org> 1.0.6-alt1
- show previous forecast data if failed to reload data

* Thu Nov 27 2025 Alexander Davydzik <paladindev@altlinux.org> 1.0.5-alt1
- fixed translations

* Thu Nov 27 2025 Alexander Davydzik <paladindev@altlinux.org> 1.0.4-alt1
- better location search
- disabled location detection for gismeteo
- updating weather on unit change

* Wed Nov 26 2025 Alexander Davydzik <paladindev@altlinux.org> 1.0.3-alt1
- added license file

* Wed Nov 26 2025 Alexander Davydzik <paladindev@altlinux.org> 1.0.2-alt1
- used a more accurate method to determine geolocation

* Tue Nov 25 2025 Alexander Davydzik <paladindev@altlinux.org> 1.0.1-alt1
- fixed location detection

* Thu Nov 20 2025 Alexander Davydzik <paladindev@altlinux.org> 1.0.0-alt2
- drop i586

* Thu Nov 20 2025 Alexander Davydzik <paladindev@altlinux.org> 1.0.0-alt1
- initial build
