%define xdg_name io.github.Foldex.AdwSteamGtk

Name: adwaita-steam-gtk
Version: 0.6.11
Release: alt1
License: GPL-3.0

Summary: A simple Gtk wrapper for Adwaita-for-Steam

Group: Games/Other

Url: https://github.com/Foldex/AdwSteamGtk

Source: %name-%version.tar

BuildArch: noarch
AutoProv: nopython3

BuildRequires(pre): rpm-macros-meson

BuildRequires: meson rpm-build-python3

BuildRequires: pkgconfig(gio-2.0)
BuildRequires: blueprint-compiler

%add_python3_path %_datadir/%name

%description
%summary.

%prep
%setup
subst "s|python install.py|python3 install.py|" src/install.py

%build
%meson
%meson_build

%install
%meson_install
%find_lang %name
rm -rf %buildroot%_datadir/locale/zh_Hans

%files -f %name.lang
%_bindir/%name
%_datadir/%name
%_datadir/glib-2.0/schemas/%xdg_name.gschema.xml
%_datadir/appdata/%xdg_name.appdata.xml
%_desktopdir/%xdg_name.desktop
%_iconsdir/hicolor/*/apps/*.svg

%changelog
* Sat Oct 19 2024 Kirill Unitsaev <fiersik@altlinux.org> 0.6.11-alt1
- Initial build
