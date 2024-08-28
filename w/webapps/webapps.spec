%define _name webapps
%define ver_major 0.5
%define rdn_name net.codelogistics.%_name

# online screenshots
%def_disable check

Name: %_name
Version: %ver_major.4
Release: alt1

Summary: Install websites as apps
License: GPL-3.0-or-later
Group: Networking/WWW
Url: https://codeberg.org/eyekay/webapps

BuildArch: noarch

Vcs: https://codeberg.org/eyekay/webapps.git

Source: %name-%version.tar

%add_python3_path %_datadir/%_name

Requires: typelib(Adw) = 1
Requires: typelib(WebKit) = 6.0
Requires: typelib(Xdp) = 1.0
Requires: dconf

BuildRequires(pre): rpm-macros-meson rpm-build-python3 rpm-build-gir
BuildRequires: meson pkgconfig(gio-2.0) /usr/bin/glib-compile-resources
BuildRequires: gtk4-update-icon-cache
%{?_enable_check:BuildRequires: /usr/bin/desktop-file-validate /usr/bin/appstream-util
BuildRequires: /usr/bin/glib-compile-schemas}

%description
Web Apps installs websites as desktop apps, so that they appear in their
own windows separate from any browsers installed.

This is similar to the "Install as App" feature found in popular web
browsers. It uses an internal browser isolated from the system browser,
which can optionally be used in incognito mode. Links to websites other
than the one installed open in a new browser window.

%prep
%setup

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
%_datadir/icons/hicolor/*/apps/*
%_datadir/glib-2.0/schemas/%rdn_name.gschema.xml
%_datadir/appdata/%rdn_name.appdata.xml
%doc README.*

%changelog
* Wed Aug 28 2024 Yuri N. Sedunov <aris@altlinux.org> 0.5.4-alt1
- updated to 0.5.4-10-gef1f870

* Thu Jul 11 2024 Yuri N. Sedunov <aris@altlinux.org> 0.5.2-alt1
- first build for Sisyphus
