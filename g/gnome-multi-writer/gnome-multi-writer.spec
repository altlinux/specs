%define ver_major 3.15
%define _name org.gnome.MultiWriter

Name: gnome-multi-writer
Version: %ver_major.90
Release: alt1

Summary: Write an ISO file to multiple USB devices at once
Group: Archiving/Backup
License: GPLv2+
Url: https://wiki.gnome.org/Apps/MultiWriter

Source: ftp://ftp.gnome.org/pub/gnome/sources/%name/%ver_major/%name-%version.tar.xz
#Source: %name-%version.tar

Requires: gnome-icon-theme-extras

%define gtk_ver 3.12.0
%define gusb_ver 0.2.4

BuildRequires: intltool docbook-utils yelp-tools
BuildRequires: libgtk+3-devel >= %gtk_ver
BuildRequires: libgusb-devel >= %gusb_ver
BuildRequires: libudisks2-devel libgudev-devel libcanberra-gtk3-devel
BuildRequires: gobject-introspection-devel

%description
GNOME MultiWriter can be used to write an ISO file to multiple
USB devices simultaneously.

%prep
%setup

%build
%autoreconf
%configure
%make_build

%install
%makeinstall_std

%find_lang %name

%files -f %name.lang
%_bindir/%name
%_bindir/%name-probe
%_desktopdir/%_name.desktop
%_datadir/glib-2.0/schemas/%_name.gschema.xml
%_datadir/polkit-1/actions/%_name.policy
%_iconsdir/hicolor/*/apps/*
%_man1dir/%name.1.*
%_datadir/appdata/%_name.appdata.xml
%doc README.md AUTHORS NEWS

%changelog
* Fri Feb 13 2015 Yuri N. Sedunov <aris@altlinux.org> 3.15.90-alt1
- 3.15.90

* Mon Jan 19 2015 Yuri N. Sedunov <aris@altlinux.org> 3.15.4-alt1
- 3.15.4 release

* Mon Jan 12 2015 Yuri N. Sedunov <aris@altlinux.org> 3.15.3-alt0.1
- 3.15.3 snapshot

* Mon Jan 12 2015 Yuri N. Sedunov <aris@altlinux.org> 3.15.2-alt1
- first build for Sisyphus

