%def_disable snapshot

%define __name SimpleWeather
%define git_name %__name
%define _name simple-weather
%define ver_major 50
%define beta %nil
%define uuid %_name@romanlefler.com
%define xdg_name org.gnome.shell.extensions.%_name
%define gettext_domain %uuid

%def_enable check

%def_disable bootstrap

Name: gnome-shell-extension-%_name
Version: %ver_major.1.0
Release: alt1

Summary: Weather extension for the GNOME Shell
Group: Graphical desktop/GNOME
License: GPL-3.0-or-later
Url: https://github.com/romanlefler/SimpleWeather

Vcs: https://github.com/romanlefler/SimpleWeather.git

Obsoletes: gnome-shell-extension-openweather < 140

BuildArch: noarch

%if_disabled snapshot
Source: %url/archive/v%version%beta/%git_name-%version%beta.tar.gz
%else
Source: %git_name-%version%beta.tar
%endif
Source1: %git_name-%version-npm.tar
# fix install in Makefile
Patch1: %__name-49.2.0-alt-makefile.patch

Requires: gnome-shell >= 48
Requires: typelib(Adw) = 1
Requires: geoclue2 typelib(Geoclue)

BuildRequires: npm /usr/bin/tsc
BuildRequires: /usr/bin/glib-compile-schemas

%description
A highly configurable GNOME shell extension for viewing the weather.

%prep
%setup -n %git_name-%version%beta %{?_disable_bootstrap:-a1}
%patch1 -b .alt
%{?_enable_bootstrap:
npm install && npm audit fix --force &&
tar -cf %git_name-%version-npm.tar node_modules && \
mv %git_name-%version-npm.tar %_sourcedir/}

%build
%make VERSION=%version

%install
%makeinstall_std INSTALLTYPE=system
%find_lang %gettext_domain

%files -f %gettext_domain.lang
%_datadir/gnome-shell/extensions/%uuid/
%_datadir/glib-2.0/schemas/%xdg_name.gschema.xml
%doc AUTHORS README.md CHANGELOG*

%changelog
* Thu Jul 02 2026 Yuri N. Sedunov <aris@altlinux.org> 50.1.0-alt1
- 50.1.0

* Sun Apr 12 2026 Yuri N. Sedunov <aris@altlinux.org> 50.0.0-alt1
- 50.0.0

* Sat Jan 24 2026 Yuri N. Sedunov <aris@altlinux.org> 49.2.0-alt1
- 49.2.0

* Mon Dec 15 2025 Yuri N. Sedunov <aris@altlinux.org> 49.1.1-alt1
- 49.1.1

* Fri Dec 05 2025 Yuri N. Sedunov <aris@altlinux.org> 49.1.0-alt1
- 49.1.0

* Wed Oct 08 2025 Yuri N. Sedunov <aris@altlinux.org> 49.0.0-alt1
- first build for Sisyphus

