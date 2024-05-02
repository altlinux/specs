%def_enable snapshot
%define _name apostrophe
%define ver_major 3.0
%define rdn_name org.gnome.gitlab.somas.Apostrophe
%define reveal_ver 5.1.0

Name: %_name
Version: %ver_major
Release: alt1

Summary: GTK-based distraction free Markdown editor
License: GPL-3.0-or-later
Group: Editors
Url: https://apps.gnome.org/Apostrophe

Vcs: https://gitlab.gnome.org/World/apostrophe.git

%if_disabled snapshot
Source: https://gitlab.gnome.org/World/apostrophe/-/archive/v%version/%_name-%version.tar.gz
%else
Source: %_name-%version.tar
%endif
Source1: https://github.com/hakimel/reveal.js/archive/%reveal_ver/reveal.js-%reveal_ver.tar.gz
Patch1: apostrophe-3.0-alt-embed-reveal.patch

BuildArch: noarch

%define gtk_api_ver 4.0
%define gtk_ver 4.0.0
%define adw_ver 1.4
%define gtksource_api_ver 5
%define webkit_api_ver 6.0

Requires: pandoc dconf
Requires: typelib(Gtk) = %gtk_api_ver
Requires: typelib(WebKit) = %webkit_api_ver
%add_typelib_req_skiplist typelib(WebKit2)
Requires: typelib(GtkSource) = %gtksource_api_ver
Requires: typelib(Spelling) = 1
# optional
#Requires: /usr/bin/pdftex

BuildRequires(pre): rpm-macros-meson rpm-build-python3 rpm-build-gir
BuildRequires: meson
BuildRequires: gobject-introspection-devel
BuildRequires: gir(Gtk) = %gtk_api_ver
BuildRequires: gir(Adw) = 1
#BuildRequires: reveal.js >= %reveal_ver
%{?_enable_check: /usr/bin/appstreamcli desktop-file-utils /usr/bin/glib-compile-schemas}

%description
Apostrophe is a GTK4 based distraction free Markdown editor, mainly
developed by Wolf Vollprecht and Manuel Genoves. It uses pandoc as
back-end for parsing Markdown and offers a very clean and sleek user
interface.

%prep
%setup -n %_name-%version -a1
%patch1 -b .reveal
mkdir -p %name/libs/reveal.js
cp -r reveal.js-%reveal_ver/* %name/libs/reveal.js

%build
%meson
%meson_build

%install
%meson_install

mkdir -p %buildroot/%_datadir/%name/libs/reveal.js
cp -r reveal.js-%reveal_ver/* %buildroot/%_datadir/%name/libs/reveal.js

%find_lang %_name

%check
%__meson_test

%files -f %_name.lang
%_bindir/%_name
%python3_sitelibdir_noarch/%_name/
%_desktopdir/%rdn_name.desktop
%_datadir/%_name/
%_datadir/glib-2.0/schemas/%rdn_name.gschema.xml
%_iconsdir/hicolor/*/apps/%{rdn_name}*.svg
%_datadir/metainfo/%rdn_name.metainfo.xml
%doc README* NEWS*


%changelog
* Thu May 02 2024 Yuri N. Sedunov <aris@altlinux.org> 3.0-alt1
- 3.0

* Sat Apr 30 2022 Yuri N. Sedunov <aris@altlinux.org> 2.6.3-alt1
- 2.6.3

* Thu Mar 31 2022 Yuri N. Sedunov <aris@altlinux.org> 2.6.2-alt1
- 2.6.2

* Sun Mar 20 2022 Yuri N. Sedunov <aris@altlinux.org> 2.6.1-alt1
- updated to v2.6.1-1-gc06e1d7

* Fri Jan 14 2022 Yuri N. Sedunov <aris@altlinux.org> 2.5-alt1
- first build for Sisyphus (v2.5-31-ga7459de)


