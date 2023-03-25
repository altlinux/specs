%def_enable snapshot

%define _name openweather
%define ver_major 120
%define beta %nil
%define uuid %_name-extension@jenslody.de
%define xdg_name org.gnome.shell.extensions.%_name
%define gettext_domain gnome-shell-extension-%_name

%def_enable check

Name: gnome-shell-extension-%_name
Version: %ver_major
Release: alt0.5

Summary: Weather extension for the GNOME Shell
Group: Graphical desktop/GNOME
License: GPL-3.0
Url: https://gitlab.com/skrewball/openweather

BuildArch: noarch

%if_disabled snapshot
Source: %url/archive/v%version%beta/%_name-%version%beta.tar.gz
%else
Vcs: https://gitlab.com/skrewball/openweather.git
Source: %name-%version%beta.tar
%endif
#https://gitlab.com/skrewball/openweather/-/issues/74
Patch: %name-120-up-shell-44.patch

Requires: gnome-shell >= 44
Requires: typelib(Gtk) = 4.0

BuildRequires: /usr/bin/glib-compile-schemas

%description
OpenWeather (gnome-shell-extension-openweather) is a simple extension
for displaying weather conditions and forecasts for any location on Earth
in the GNOME Shell. It provides support for multiple locations with
editable names using coordinates to store the locations, a beautiful
layout, and more.

Weather data is fetched from OpenWeatherMap (https://openweathermap.org)
including 3 hour forecasts for up to 5 days.

%prep
%setup -n %name-%version%beta
%patch -p1

%build
%make VERSION=%version

%install
%makeinstall_std
%find_lang %gettext_domain


%files -f %gettext_domain.lang
%_datadir/gnome-shell/extensions/%uuid/
%_datadir/glib-2.0/schemas/%xdg_name.gschema.xml
%doc AUTHORS README.md

%changelog
* Sat Mar 25 2023 Yuri N. Sedunov <aris@altlinux.org> 120-alt0.5
- first build for Sisyphus

