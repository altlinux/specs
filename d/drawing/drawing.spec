%def_disable snapshot
%define _name drawing
%define ver_major 1.0
%define rdn_name com.github.maoschanz.drawing

Name: %_name
Version: %ver_major.2
Release: alt1

Summary: A simple raster image editor for the GNOME desktop
License: GPL-3.0-or-later
Group: Graphics
Url: https://github.com/maoschanz/drawing

%if_disabled snapshot
Source: https://github.com/maoschanz/%_name/archive/%version/%_name-%version.tar.gz
%else
Vcs: https://github.com/maoschanz/drawing.git
Source: %_name-%version.tar
%endif

BuildArch: noarch

Requires: typelib(Gtk) = 3.0
%add_python3_path %_datadir/%_name

BuildRequires(pre): rpm-macros-meson rpm-build-python3 rpm-build-gir
BuildRequires: meson yelp-tools /usr/bin/appstream-util desktop-file-utils

%description
Drawing is a simple image editor, similar to Microsoft Paint, is aiming at the
GNOME desktop. PNG, JPEG and BMP files are supported.

%prep
%setup -n %_name-%version

%build
%meson
%meson_build

%install
%meson_install
%find_lang --with-gnome %_name

%files -f %_name.lang
%_bindir/%_name
%_desktopdir/%rdn_name.desktop
%_datadir/%_name/
%_datadir/glib-2.0/schemas/%rdn_name.gschema.xml
%_iconsdir/hicolor/*/apps/%{rdn_name}*.*
%_datadir/metainfo/%rdn_name.*.xml
%doc README*


%changelog
* Sat Feb 25 2023 Yuri N. Sedunov <aris@altlinux.org> 1.0.2-alt1
- 1.0.2

* Sun Apr 10 2022 Yuri N. Sedunov <aris@altlinux.org> 1.0.1-alt1
- 1.0.1

* Sun Mar 27 2022 Yuri N. Sedunov <aris@altlinux.org> 1.0.0-alt1
- 1.0.0

* Thu Jan 27 2022 Yuri N. Sedunov <aris@altlinux.org> 0.8.5-alt1
- first build for Sisyphus


