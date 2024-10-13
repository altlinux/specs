%def_disable snapshot

%define _name Curtail
%define ver_major 1.11
%define xdg_name com.github.huluti.%_name

%def_enable check

Name: curtail
Version: %ver_major.1
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

%define adwaita_ver 1.6

Requires: typelib(Adw) = 1
Requires: yelp
Requires: jpegoptim
Requires: pngquant
Requires: /usr/bin/cwebp
Requires: /usr/bin/scour
Requires: oxipng

BuildRequires(pre): rpm-macros-meson rpm-build-python3 rpm-build-gir
BuildRequires: meson yelp-tools
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
%_datadir/glib-2.0/schemas/%xdg_name.gschema.xml
%_iconsdir/hicolor/*/apps/%{xdg_name}*.svg
%_datadir/metainfo/%xdg_name.appdata.xml
%doc README*

%changelog
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


