%def_enable snapshot
%define _name apostrophe
%define ver_major 2.6
%define rdn_name org.gnome.gitlab.somas.Apostrophe

Name: %_name
Version: %ver_major.3
Release: alt1

Summary: GTK-based distraction free Markdown editor
License: GPL-3.0-or-later
Group: Editors
Url: https://gitlab.gnome.org/World/apostrophe

%if_disabled snapshot
Source: %url/-/archive/v%version/%_name-%version.tar.gz
%else
Vcs: https://gitlab.gnome.org/World/apostrophe.git
Source: %_name-%version.tar
%endif

BuildArch: noarch

%define gtk_api_ver 3.0
%define gtk_ver 3.24
%define handy_ver 1.0.0
%define webkit_api_ver 4.0

Requires: pandoc
Requires: typelib(Gtk) = %gtk_api_ver
Requires: typelib(WebKit2) = %webkit_api_ver

BuildRequires(pre): rpm-macros-meson rpm-build-python3 rpm-build-gir
BuildRequires: meson sassc /usr/bin/appstream-util desktop-file-utils
BuildRequires: gobject-introspection-devel
BuildRequires: gir(Gtk) = 3.0
BuildRequires: gir(Handy) = 1

%description
Apostrophe is a GTK+ based distraction free Markdown editor, mainly
developed by Wolf Vollprecht and Manuel Genoves. It uses pandoc as
back-end for parsing Markdown and offers a very clean and sleek user
interface.

%prep
%setup -n %_name-%version

%build
%meson
%meson_build

%install
%meson_install
%find_lang %_name

%files -f %_name.lang
%_bindir/%_name
%python3_sitelibdir_noarch/%_name/
%_desktopdir/%rdn_name.desktop
%_datadir/%_name/
%_datadir/glib-2.0/schemas/%rdn_name.gschema.xml
%_iconsdir/hicolor/*/apps/%{rdn_name}*.svg
%_datadir/metainfo/%rdn_name.metainfo.xml
%doc README* NEWS


%changelog
* Sat Apr 30 2022 Yuri N. Sedunov <aris@altlinux.org> 2.6.3-alt1
- 2.6.3

* Thu Mar 31 2022 Yuri N. Sedunov <aris@altlinux.org> 2.6.2-alt1
- 2.6.2

* Sun Mar 20 2022 Yuri N. Sedunov <aris@altlinux.org> 2.6.1-alt1
- updated to v2.6.1-1-gc06e1d7

* Fri Jan 14 2022 Yuri N. Sedunov <aris@altlinux.org> 2.5-alt1
- first build for Sisyphus (v2.5-31-ga7459de)


