%define xdg_name io.github.zingytomato.netpeek

Name: netpeek
Version: 0.2.3.1
Release: alt1
License: GPL-3.0

Summary: A modern network scanner

Group: Networking/Other

Url: https://github.com/ZingyTomato/NetPeek
Vcs: https://github.com/ZingyTomato/NetPeek.git

Source: %name-%version.tar

BuildArch: noarch
AutoProv: nopython3

BuildRequires(pre): rpm-macros-meson
BuildRequires: meson rpm-build-python3

BuildRequires: pkgconfig(gio-2.0)

BuildRequires: gtk4-update-icon-cache

%add_python3_path %_datadir/%name

%description
A modern libadwaita-based network scanner for GNOME
that helps you discover devices on your local network.

%prep
%setup

%build
%meson
%meson_build

%install
%meson_install
%find_lang %name

%files -f %name.lang
%_bindir/%name
%_datadir/%name
%_desktopdir/%xdg_name.desktop
%_datadir/dbus-1/services/%xdg_name.service
%_datadir/glib-2.0/schemas/%xdg_name.gschema.xml
%_iconsdir/hicolor/*/apps/*.svg
%_datadir/metainfo/%xdg_name.metainfo.xml

%changelog
* Sat Aug 09 2025 Kirill Unitsaev <fiersik@altlinux.org> 0.2.3.1-alt1
- Initial build
