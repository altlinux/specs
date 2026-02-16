# https://github.com/ahshabbir/ddcbc-api required
%def_enable snapshot

%define _name Luminance
%define ver_major 1.4
%define rdn_name com.sidevesh.%_name

Name: luminance
Version: %ver_major.6
Release: alt1

Summary: A simple GTK application to control brightness of displays
License: GPL-3.0-or-later
Group: System/Configuration/Hardware
Url: https://github.com/sidevesh/Luminance

Vcs: https://github.com/sidevesh/Luminance.git

%if_disabled snapshot
Source: https://github.com/sidevesh/Luminance/archive/%version/%name-%version.tar.gz
%else
Source: %name-%version.tar
%endif

Requires: dconf

BuildRequires(pre): rpm-macros-meson
BuildRequires: meson
BuildRequires: pkgconfig(libadwaita-1)
BuildRequires: pkgconfig(ddcutil)
BuildRequires: pkgconfig(udev)

%description
Luminance is a simple GTK application to control brightness of displays
including external displays supporting DDC/CI.

%prep
%setup

%build
%meson \
    -Dbuildtype=release
%nil
%meson_build

%install
%meson_install
%find_lang %name

%check
%__meson_test

%files -f %name.lang
%_bindir/%rdn_name
%_udevrulesdir/44-backlight-permissions.rules
%_desktopdir/%rdn_name.desktop
%_datadir/icons/hicolor/*/apps/*
%_datadir/glib-2.0/schemas/%rdn_name.gschema.xml
%_datadir/dbus-1/services/%rdn_name.service
%_datadir/metainfo/%rdn_name.metainfo.xml
%doc README*

%changelog
* Mon Feb 16 2026 Yuri N. Sedunov <aris@altlinux.org> 1.4.6-alt1
- 1.4.6

* Sat Feb 07 2026 Yuri N. Sedunov <aris@altlinux.org> 1.4.2-alt1
- 1.4.2

* Mon Oct 27 2025 Yuri N. Sedunov <aris@altlinux.org> 1.2.0-alt1
- updated to 1.2.0-1-g48380b5

* Tue Jul 02 2024 Yuri N. Sedunov <aris@altlinux.org> 1.1.0-alt1
- first build for Sisyphus



