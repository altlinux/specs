%def_enable snapshot

%define _name Valuta
%define ver_major 1.3
%define rdn_name io.github.idevecore.%_name

# online screenshots
%def_disable check

Name: valuta
Version: %ver_major.1
Release: alt1

Summary: Currency converter for GNOME
License: GPL-3.0-or-later
Group: Graphical desktop/GNOME
Url: https://apps.gnome.org/Valuta

Vcs: https://github.com/ideveCore/valuta.git

%if_disabled snapshot
Source: https://github.com/ideveCore/valuta/releases/download/v%version/%name-%version.tar.gz
%else
Source: %name-%version.tar
%endif

BuildArch: noarch

%add_python3_path %_datadir/%name

%define gst_api_ver 1.0
%define gst_ver 1.18
%define adw_ver 1.0

Requires: typelib(Adw) = 1
Requires: typelib(Soup) = 3.0
#Requires: gstreamer%gst_api_ver >= %gst_ver
#Requires: gst-plugins-base%gst_api_ver
Requires: dconf

BuildRequires(pre): rpm-macros-meson rpm-build-python3 rpm-build-gir
BuildRequires: meson blueprint-compiler
BuildRequires: pkgconfig(libadwaita-1) >= %adw_ver gir(Adw)
BuildRequires: pkgconfig(gstreamer-1.0) >= %gst_ver
BuildRequires: pkgconfig(libsoup-3.0)
BuildRequires: pkgconfig(pygobject-3.0)
%{?_enable_check:BuildRequires: /usr/bin/appstream-util desktop-file-utils}

%description
Valuta is a simple and fast conversion tool, ideal for those who need to
convert between different currencies repeatedly. Use it while traveling,
budgeting, or anytime else you need to quickly convert between two
currencies.

%prep
%setup -n %name-%version

%build
%meson
%meson_build

%install
%meson_install
%find_lang %name

%check
%__meson_test

%files -f %name.lang
%attr(0755,root,root) %_bindir/%name
%_datadir/%name/
%_desktopdir/%rdn_name.desktop
%_datadir/glib-2.0/schemas/%rdn_name.gschema.xml
%_datadir/dbus-1/services/%rdn_name.SearchProvider.service
%_datadir/gnome-shell/search-providers/%rdn_name.SearchProvider.ini
%_iconsdir/hicolor/*/*/*.svg
%_datadir/appdata/%rdn_name.appdata.xml
%doc README*

%changelog
* Sun Jul 14 2024 Yuri N. Sedunov <aris@altlinux.org> 1.3.1-alt1
- first build for Sisyphus (v1.3.1-6-gd9b8de3)


