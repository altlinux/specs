%define ver_major 3.15
%define _name org.gnome.MultiWriter

Name: gnome-multi-writer
Version: %ver_major.2
Release: alt1

Summary: Write an ISO file to multiple USB devices at once
Group: Archiving/Backup
License: GPLv2+
Url: https://wiki.gnome.org/Apps/MultiWriter

Source: http://people.freedesktop.org/~hughsient/releases/%name-%version.tar.xz

Requires: gnome-icon-theme-extras

%define gtk_ver 3.12.0
%define gusb_ver 0.2.4

BuildRequires: intltool docbook-utils yelp-tools
BuildRequires: libgtk+3-devel >= %gtk_ver
BuildRequires: libgusb-devel >= %gusb_ver
BuildRequires: libudisks2-devel libcanberra-gtk3-devel
BuildRequires: gobject-introspection-devel

%description
GNOME MultiWriter can be used to write an ISO file to multiple
USB devices simultaneously.

%prep
%setup

%build
%configure
%make_build

%install
%makeinstall_std

%find_lang %name

%files -f %name.lang
%_bindir/%name
%_desktopdir/%_name.desktop
%_datadir/glib-2.0/schemas/%_name.gschema.xml
%_iconsdir/hicolor/*/apps/*
%_man1dir/%name.1.*
%_datadir/appdata/%_name.appdata.xml
%doc README.md AUTHORS NEWS

%changelog
* Mon Jan 12 2015 Yuri N. Sedunov <aris@altlinux.org> 3.15.2-alt1
- first build for Sisyphus

