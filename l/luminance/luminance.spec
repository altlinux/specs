%def_enable snapshot

%define _name Luminance
%define ver_major 1.5
%define rdn_name com.sidevesh.%_name
%define uuid luminance-extension@sidevesh

Name: luminance
Version: %ver_major.0
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

BuildRequires(pre): rpm-macros-meson rpm-build-gir
BuildRequires: meson
BuildRequires: pkgconfig(libadwaita-1)
BuildRequires: pkgconfig(ddcutil)
BuildRequires: pkgconfig(udev)

%description
Luminance is a simple GTK application to control brightness of displays
including external displays supporting DDC/CI.

%package -n gnome-shell-extension-%name
Summary: %_name Extension for GNOME Shell
Group: Graphical desktop/GNOME
BuildArch: noarch
Requires: gnome-shell >= 49
Requires: %name = %EVR

%description -n gnome-shell-extension-%name
Companion GNOME Shell extension for %_name app.

%prep
%setup

%build
%meson \
    -Dbuildtype=release
%nil
%meson_build

%install
%meson_install
mkdir -p %buildroot%_datadir/gnome-shell/extensions
cp -a gnome-extension/%uuid %buildroot%_datadir/gnome-shell/extensions/

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

%files -n gnome-shell-extension-%name
%_datadir/gnome-shell/extensions/%uuid/

%changelog
* Sun Jun 21 2026 Yuri N. Sedunov <aris@altlinux.org> 1.5.0-alt1
- 1.5.0-2-g8041300
- new gnome-shell-extension-luminance subpackage

* Mon Feb 16 2026 Yuri N. Sedunov <aris@altlinux.org> 1.4.6-alt1
- 1.4.6

* Sat Feb 07 2026 Yuri N. Sedunov <aris@altlinux.org> 1.4.2-alt1
- 1.4.2

* Mon Oct 27 2025 Yuri N. Sedunov <aris@altlinux.org> 1.2.0-alt1
- updated to 1.2.0-1-g48380b5

* Tue Jul 02 2024 Yuri N. Sedunov <aris@altlinux.org> 1.1.0-alt1
- first build for Sisyphus



