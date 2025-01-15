%define APP_ID io.github.amit9838.mousam
%def_enable check

Name: mousam
Version: 1.4.0
Release: alt1

Summary: Weather at a glance
License: GPL-3.0-or-later
Group: Graphical desktop/GNOME

Url: https://amit9838.github.io/mousam/
Vcs: https://github.com/amit9838/mousam
Source: %name-%version.tar

%add_python3_path %_datadir/%name

AutoProv: nopython3

BuildRequires(pre): rpm-macros-meson
BuildRequires(pre): rpm-macros-python3
BuildRequires: rpm-build-python3
BuildRequires: meson
BuildRequires: gtk4-update-icon-cache
BuildRequires: pkgconfig(gio-2.0)
%if_enabled check
# Report running all tests. Validate appstream file FAIL
BuildRequires: desktop-file-utils
BuildRequires: libgio
%endif

BuildArch: noarch

%description
Current Weather conditions and forcasts.

Features:
* Displays real-time temperature, humidity, wind speed, UV index,
  pressure and more
* Utilizes graphical representations, such as temperature , precipitation graphs
  and wind-speed with direction to provide an hourly forecast
  for the next 24 hours
* Also provides tomorrow and 7-day forcasts
* See conditions in metric or imperial systems

%prep
%setup

%build
%meson
%meson_build

%install
%meson_install
%find_lang --with-gnome %name

%check
%meson_test

%files -f %name.lang
%_bindir/%name
%_datadir/appdata/%APP_ID.appdata.xml
%_datadir/applications/%APP_ID.desktop
%_datadir/glib-2.0/schemas/%APP_ID.gschema.xml
%_iconsdir/hicolor/*/apps/%{APP_ID}*.svg
%_iconsdir/hicolor/scalable/mousam_icons/*.svg
%_datadir/%name

%changelog
* Fri Nov 15 2024 Oleg Shchavelev <oleg@altlinux.org> 1.4.0-alt1
- Initial build
