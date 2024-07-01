%def_disable snapshot

%define _name openweather
%define git_name gnome-%_name
%define ver_major 138
%define beta %nil
%define uuid %_name-extension@penguin-teal.github.io
%define xdg_name org.gnome.shell.extensions.%{_name}refined
%define gettext_domain gnome-shell-extension-%{_name}refined

%def_enable check

Name: gnome-shell-extension-%_name
Version: %ver_major
Release: alt1

Summary: Weather extension for the GNOME Shell
Group: Graphical desktop/GNOME
License: GPL-3.0-or-later
Url: https://github.com/penguin-teal/gnome-openweather

BuildArch: noarch

%if_disabled snapshot
Source: %url/archive/v%version%beta/%git_name-%version%beta.tar.gz
%else
Vcs: https://github.com/penguin-teal/gnome-openweather.git
Source: %git_name-%version%beta.tar
%endif

Requires: gnome-shell >= 45
Requires: typelib(Adw) = 1
Requires: geoclue2 typelib(Geoclue)

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
%setup -n %git_name-%version%beta

%build
%make VERSION=%version

%install
%makeinstall_std
%find_lang %gettext_domain


%files -f %gettext_domain.lang
%_datadir/gnome-shell/extensions/%uuid/
%_datadir/glib-2.0/schemas/%xdg_name.gschema.xml
%doc AUTHORS README.md CHANGELOG*

%changelog
* Mon Jul 01 2024 Yuri N. Sedunov <aris@altlinux.org> 138-alt1
- 138

* Sat Jun 29 2024 Yuri N. Sedunov <aris@altlinux.org> 137-alt1
- 137

* Wed Jun 12 2024 Yuri N. Sedunov <aris@altlinux.org> 136-alt1
- 136

* Mon May 06 2024 Yuri N. Sedunov <aris@altlinux.org> 135-alt1
- 135

* Sat Apr 20 2024 Yuri N. Sedunov <aris@altlinux.org> 134-alt1
- 134

* Sat Apr 06 2024 Yuri N. Sedunov <aris@altlinux.org> 133-alt1
- 133

* Sun Mar 31 2024 Yuri N. Sedunov <aris@altlinux.org> 132-alt1
- 132 (gnome-46 supported)

* Mon Feb 19 2024 Yuri N. Sedunov <aris@altlinux.org> 129-alt1
- 129

* Fri Feb 02 2024 Yuri N. Sedunov <aris@altlinux.org> 128-alt1
- 128

* Wed Jan 24 2024 Yuri N. Sedunov <aris@altlinux.org> 127-alt1
- 127

* Tue Jan 16 2024 Yuri N. Sedunov <aris@altlinux.org> 126-alt1
- 126 (new upstream)

* Tue Apr 25 2023 Yuri N. Sedunov <aris@altlinux.org> 121-alt1
- 121

* Sat Mar 25 2023 Yuri N. Sedunov <aris@altlinux.org> 120-alt0.5
- first build for Sisyphus

