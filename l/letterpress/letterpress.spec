%def_enable snapshot
%define _name letterpress
%define ver_major 2.0
%define rdn_name io.gitlab.gregorni.Letterpress

%def_enable check

Name: %_name
Version: %ver_major
Release: alt1

Summary: Create beautiful ASCII art
License: GPL-3.0-or-later
Group: Graphics
Url: https://apps.gnome.org/Letterpress

%if_disabled snapshot
Source: https://gitlab.gnome.org/World/Letterpress/-/archive/%version/%_name-%version.tar.gz
%else
Vcs: https://gitlab.gnome.org/World/Letterpress.git
Source: %_name-%version.tar
%endif

BuildArch: noarch

%define bp_ver 0.10

%add_python3_path %_datadir/%_name

Requires: jp2a
Requires: typelib(Adw) = 1

BuildRequires(pre): rpm-macros-meson rpm-build-python3 rpm-build-gir
BuildRequires: meson blueprint-compiler >= %bp_ver typelib(Adw)
%{?_enable_check:BuildRequires: /usr/bin/appstream-util desktop-file-utils}

%description
Letterpress converts your images into a picture made up of ASCII
characters. You can save the output to a file, copy it, and even change
its resolution! High-res output can still be viewed comfortably by
lowering the zoom factor.

%prep
%setup -n %_name-%version

%build
%meson
%meson_build

%install
%meson_install
%find_lang --with-gnome %_name

%__meson_test

%files -f %_name.lang
%_bindir/%_name
%_desktopdir/%rdn_name.desktop
%_datadir/%_name/
%_datadir/glib-2.0/schemas/%rdn_name.gschema.xml
%_iconsdir/hicolor/*/apps/%{rdn_name}*.*
%_datadir/appdata/%rdn_name.*.xml
%doc README*


%changelog
* Wed Oct 04 2023 Yuri N. Sedunov <aris@altlinux.org> 2.0-alt1
- first preview for Sisyphus (2.0-12-ge6d8a39)


