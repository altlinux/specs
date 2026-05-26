%def_disable snapshot

%define _name Curtail
%define ver_major 1.16
%define xdg_name com.github.huluti.%_name

%def_enable check

Name: curtail
Version: %ver_major.2
Release: alt1

Summary: An Image Compressor for GNOME
License: GPL-3.0-or-later
Group: Graphics
Url: https://apps.gnome.org/Curtail

Vcs: https://github.com/Huluti/Curtail.git

%if_disabled snapshot
Source: https://github.com/Huluti/Curtail/archive/%version/%name-%version.tar.gz
%else
Source: %name-%version.tar
%endif

BuildArch: noarch
%add_python3_path %_datadir/%name

%define adwaita_ver 1.8
%define oxipng_ver 10.1.1

Requires: python3-module-pygobject3
Requires: typelib(Adw) = 1
Requires: yelp
Requires: jpegoptim
Requires: pngquant
Requires: /usr/bin/cwebp
Requires: /usr/bin/scour
Requires: oxipng >= %oxipng_ver

BuildRequires(pre): rpm-macros-meson rpm-build-python3 rpm-build-gir
BuildRequires: meson blueprint-compiler yelp-tools
BuildRequires: pkgconfig(libadwaita-1) >= %adwaita_ver
%{?_enable_check:BuildRequires: /usr/bin/appstreamcli desktop-file-utils}

%description
Curtail is a useful image compressor that supports PNG, JPEG, WebP and
SVG file types.

It supports both lossless and lossy compression modes with an option to
whether keep or not metadata of images.

%prep
%setup %{?_disable_snapshot:-n %_name-%version}

%build
%meson
%meson_build

%install
%meson_install
%find_lang --with-gnome %name

%check
%__meson_test -v

%files -f %name.lang
%_bindir/%name
%_datadir/%name/
%_desktopdir/%xdg_name.desktop
%_datadir/dbus-1/services/%xdg_name.service
%_datadir/glib-2.0/schemas/%xdg_name.gschema.xml
%_iconsdir/hicolor/*/apps/%{xdg_name}*.svg
%_datadir/metainfo/%xdg_name.appdata.xml
%doc README* CHANGELOG*

%changelog
* Mon May 25 2026 Yuri N. Sedunov <aris@altlinux.org> 1.16.2-alt1
- 1.16.2

* Sat May 16 2026 Yuri N. Sedunov <aris@altlinux.org> 1.16.1-alt1
- 1.16.1

* Tue May 12 2026 Yuri N. Sedunov <aris@altlinux.org> 1.16.0-alt1
- 1.16.0

* Sun Mar 01 2026 Yuri N. Sedunov <aris@altlinux.org> 1.15.1-alt1
- 1.15.1

* Fri Jan 16 2026 Yuri N. Sedunov <aris@altlinux.org> 1.15.0-alt1
- 1.15.0

* Tue Jan 06 2026 Yuri N. Sedunov <aris@altlinux.org> 1.14.0-alt1
- 1.14.0

* Tue Apr 22 2025 Yuri N. Sedunov <aris@altlinux.org> 1.13.0-alt1
- 1.13.0

* Tue Jan 14 2025 Yuri N. Sedunov <aris@altlinux.org> 1.12.0-alt1
- 1.12.0

* Sun Oct 13 2024 Yuri N. Sedunov <aris@altlinux.org> 1.11.1-alt1
- 1.11.1

* Sat Oct 05 2024 Yuri N. Sedunov <aris@altlinux.org> 1.11.0-alt1
- 1.11.0

* Sat Jun 15 2024 Yuri N. Sedunov <aris@altlinux.org> 1.10.0-alt1
- updated to 1.10.0-2-ge6900c9

* Tue Apr 16 2024 Yuri N. Sedunov <aris@altlinux.org> 1.9.1-alt1
- 1.9.1

* Wed Nov 29 2023 Yuri N. Sedunov <aris@altlinux.org> 1.8.0-alt1
- updated to 1.8.0-6-gc67c19c

* Thu Sep 28 2023 Yuri N. Sedunov <aris@altlinux.org> 1.7.0-alt1
- first build for Sisyphus (1.7.0-28-gafc2978)


