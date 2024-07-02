%define _name Luminance
%define ver_major 1.1
%define rdn_name com.sidevesh.%_name

Name: luminance
Version: %ver_major.0
Release: alt1

Summary: A simple GTK application to control brightness of displays
License: GPL-3.0-or-later
Group: System/Configuration/Hardware
Url: https://github.com/sidevesh/Luminance

Vcs: https://github.com/sidevesh/Luminance.git

Source: %name-%version.tar

Requires: dconf

BuildRequires: pkgconfig(libadwaita-1)
BuildRequires: pkgconfig(ddcutil)

%description
Luminance is a simple GTK application to control brightness of displays including
external displays supporting DDC/CI.

%prep
%setup

%build
gcc $RPM_OPT_FLAGS $(pkg-config --cflags gtk4 libadwaita-1) \
-o build/app src/main.c $(pkg-config --libs gtk4 libadwaita-1) -l ddcutil

%install
install -pD -m755 build/app %buildroot%_bindir/%rdn_name
install -pD -m644 install_files/%rdn_name.desktop %buildroot%_desktopdir/%rdn_name.desktop
install -pD -m644 install_files/44-backlight-permissions.rules %buildroot%_udevrulesdir/44-backlight-permissions.rules
install -pD -m644 install_files/%rdn_name.gschema.xml %buildroot%_datadir/glib-2.0/schemas/%rdn_name.gschema.xml
install -pD -m644 icons/hicolor/scalable/apps/%rdn_name.svg %buildroot%_iconsdir/hicolor/scalable/apps/%rdn_name.svg
install -pD -m644 icons/hicolor/symbolic/apps/%rdn_name-symbolic.svg %buildroot%_iconsdir/hicolor/symbolic/apps/%rdn_name-symbolic.svg

%find_lang %name

%files -f %name.lang
%_bindir/%rdn_name
%_udevrulesdir/44-backlight-permissions.rules
%_desktopdir/%rdn_name.desktop
%_datadir/icons/hicolor/*/apps/*
%_datadir/glib-2.0/schemas/%rdn_name.gschema.xml
#%_datadir/metainfo/%rdn_name.metainfo.xml
%doc README*

%changelog
* Tue Jul 02 2024 Yuri N. Sedunov <aris@altlinux.org> 1.1.0-alt1
- first build for Sisyphus



