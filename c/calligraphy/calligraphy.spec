%define xdg_name dev.geopjr.Calligraphy

Name: calligraphy
Version: 1.1.0
Release: alt1
License: GPL-3.0

Summary: Turn text into ASCII banners

Group: Graphical desktop/GNOME

Url: https://gitlab.gnome.org/GeopJr/Calligraphy
Vcs: https://gitlab.gnome.org/GeopJr/Calligraphy.git

Source: %name-%version.tar

BuildArch: noarch
AutoProv: nopython3

BuildRequires(pre): rpm-macros-meson

BuildRequires: meson rpm-build-python3
BuildRequires: gtk-update-icon-cache

BuildRequires: pkgconfig(gio-2.0)

%add_python3_path %_datadir/%xdg_name

%description
%summary.

%prep
%setup

%build
%meson
%meson_build

%install
%meson_install
%find_lang %name
rm -rf %buildroot%_datadir/locale/zh_Hans

%files -f %name.lang
%_bindir/%name
%_datadir/%xdg_name
%_datadir/glib-2.0/schemas/%xdg_name.gschema.xml
%_datadir/metainfo/%xdg_name.metainfo.xml
%_desktopdir/%xdg_name.desktop
%_iconsdir/hicolor/*/apps/*.svg

%changelog
* Sun Feb 16 2025 Kirill Unitsaev <fiersik@altlinux.org> 1.1.0-alt1
- Initial build
