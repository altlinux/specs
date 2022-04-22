%def_disable snapshot
%define ver_major 42
%define beta %nil
%define xdg_name org.gnome.TextEditor

%def_enable gtk_doc
%def_disable check

Name: gnome-text-editor
Version: %ver_major.1
Release: alt1%beta

Summary: A simple Text Editor for GNOME
Group: Editors
License: GPL-3.0
Url: https://gitlab.gnome.org/GNOME/gnome-text-editor

%if_disabled snapshot
Source: https://download.gnome.org/sources/%name/%ver_major/%name-%version%beta.tar.xz
%else
Source: %name-%version.tar
%endif

%define glib_ver 2.69
%define gtk_ver 4.6
%define gtksource_ver 5.3.1
%define enchant_ver 2.2.0

BuildRequires(pre): rpm-macros-meson
BuildRequires: meson libappstream-glib-devel desktop-file-utils yelp-tools
BuildRequires: libgio-devel >= %glib_ver
BuildRequires: libgtk4-devel >= %gtk_ver libpcre-devel
BuildRequires: libgtksourceview5-devel >= %gtksource_ver
BuildRequires: pkgconfig(enchant-2) >= %enchant_ver
BuildRequires: pkgconfig(libadwaita-1)
BuildRequires: libicu-devel

%description
Text Editor is a simple editor for GNOME focused on being a good
general purpose default editor.

%prep
%setup -n %name-%version%beta

%build
%meson
%meson_build

%install
%meson_install
%find_lang %name --with-gnome

%check
%meson_test

%files -f %name.lang
%_bindir/*
%_desktopdir/%xdg_name.desktop
%_datadir/%name/
%_datadir/glib-2.0/schemas/%xdg_name.gschema.xml
%_datadir/dbus-1/services/%xdg_name.service
%_iconsdir/hicolor/*/apps/%{xdg_name}*.svg
%_iconsdir/hicolor/*/actions/*.svg
%_datadir/metainfo/%xdg_name.appdata.xml
%doc README* NEWS

%changelog
* Thu Apr 21 2022 Yuri N. Sedunov <aris@altlinux.org> 42.1-alt1
- 42.1

* Sat Mar 19 2022 Yuri N. Sedunov <aris@altlinux.org> 42.0-alt1
- 42.0

* Wed Oct 06 2021 Yuri N. Sedunov <aris@altlinux.org> 41.1-alt1
- 41.1

* Thu Aug 26 2021 Yuri N. Sedunov <aris@altlinux.org> 41-alt0.2.beta1
- first build for Sisyphus


