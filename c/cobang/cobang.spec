%define __name CoBang
%define _name cobang
%define ver_major 2.5
%define rdn_name vn.hoabinh.quan.%__name

%def_enable check

Name: %_name
Version: %ver_major.0
Release: alt1

Summary: A native QR Code and barcode scanner application for Linux desktop
License: GPL-3.0-or-later
Group: Graphics
Url: https://github.com/hongquan/CoBang

Vcs: https://github.com/hongquan/CoBang.git

BuildArch: noarch

Source: %__name-%version.tar

%add_python3_path %_datadir/%_name

%define adw_ver 1.8

Requires: python3-module-pygobject3
Requires: dconf
Requires: typelib(Adw) = 1
Requires: libadwaita-gir >= %adw_ver
Requires: typelib(XdpGtk4) = 1.0
Requires: typelib(GstApp) = 1.0
Requires: gst-plugin-gtk4

BuildRequires(pre): rpm-macros-meson rpm-build-python3 rpm-build-gir
BuildRequires: meson blueprint-compiler
BuildRequires: /usr/bin/glib-compile-resources /usr/bin/gtk4-update-icon-cache
%{?_enable_check:BuildRequires: /usr/bin/desktop-file-validate /usr/bin/appstreamcli /usr/bin/glib-compile-schemas}

%description
CoBang can scan barcode, QR code from webcam or static image, local or
remote.

%prep
%setup -n %__name-%version

%build
%meson
%meson_build

%install
%meson_install
%find_lang %name

%check
%__meson_test

%files -f %name.lang
%_bindir/%name
%_datadir/%name/
%_desktopdir/%rdn_name.desktop
%_datadir/icons/hicolor/*/apps/*
%_datadir/glib-2.0/schemas/%rdn_name.gschema.xml
%_datadir/metainfo/%rdn_name.metainfo.xml
%_datadir/dbus-1/services/%rdn_name.service
%doc README.*

%changelog
* Thu Mar 12 2026 Yuri N. Sedunov <aris@altlinux.org> 2.5.0-alt1
- 2.5.0

* Sun Mar 08 2026 Yuri N. Sedunov <aris@altlinux.org> 2.4.0-alt1
- 2.4.0

* Tue Dec 30 2025 Yuri N. Sedunov <aris@altlinux.org> 2.3.1-alt1
- first build for Sisyphus (v2.3.1-5-g4b435d1)
