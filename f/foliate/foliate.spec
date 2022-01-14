%def_enable snapshot

%define ver_major 2.6
%define rdn_name com.github.johnfactotum.Foliate

Name: foliate
Version: %ver_major.4
Release: alt1

Summary: A simple and modern GTK eBook reader
License: GPL-3.0
Group: Office
Url: https://github.com/johnfactotum/foliate

%if_disabled snapshot
Source: %url/archive/%version/%name-%version.tar.gz
%else
Vcs: https://github.com/johnfactotum/foliate.git
Source: %name-%version.tar
%endif

%define handy_api_ver 1
%define webkit_api_ver 4.0
%define tracker_api_ver 3.0
%define gjs_ver 1.52
%define iso_codes_ver 3.57

Requires: libgjs >= %gjs_ver dconf iso-codes >= %iso_codes_ver
#Recommends: espeak, espeak-ng or festival

# find ./ -name "*.js" |/usr/lib/rpm/gir-js.req |sort|uniq|sed -e 's/^/Requires: /'
Requires: typelib(Gdk)
Requires: typelib(GdkPixbuf)
Requires: typelib(Gio)
Requires: typelib(GLib)
Requires: typelib(GObject)
Requires: typelib(Gspell)
Requires: typelib(Gtk) = 3.0
Requires: typelib(Handy) = %handy_api_ver
Requires: typelib(Pango)
Requires: typelib(Soup)
Requires: typelib(Tracker) = %tracker_api_ver
Requires: typelib(WebKit2) = %webkit_api_ver

%add_python3_path %_datadir/%rdn_name

BuildRequires(pre): meson rpm-build-gir rpm-build-python3
BuildRequires: desktop-file-utils libappstream-glib-devel
BuildRequires: libgjs-devel iso-codes-devel >= %iso_codes_ver

%description
Foliate is a simple and modern GTK eBook reader with following features:
- View EPUB, Kindle, FictionBook, Comic book and plain text files
- Two-page view and scrolled view
- Customize font and line-spacing
- Light, sepia, dark, and invert mode
- Reading progress slider with chapter marks
- Bookmarks and annotations
- Find in book
- Quick dictionary lookup

%prep
%setup
# switch python shebangs to python3
sed -i 's|\(#\!/usr/bin/env python\)$|\13|
	s|\(/usr/bin/python\)$|\13|' src/assets/KindleUnpack/*.py

%build
%meson
%meson_build

%install
%meson_install
%find_lang --with-gnome --output=%name.lang %name %rdn_name

%files -f %name.lang
%_bindir/%rdn_name
%_desktopdir/%rdn_name.desktop
%_datadir/%rdn_name/
%_iconsdir/hicolor/symbolic/apps/%rdn_name-symbolic.svg
%_iconsdir/hicolor/scalable/apps/%rdn_name.svg
%_datadir/glib-2.0/schemas/%rdn_name.gschema.xml
%_datadir/metainfo/%rdn_name.metainfo.xml
%doc README*


%changelog
* Fri Jan 14 2022 Yuri N. Sedunov <aris@altlinux.org> 2.6.4-alt1
- updated to 2.6.4-1-ged40d8b

* Sun Apr 11 2021 Yuri N. Sedunov <aris@altlinux.org> 2.6.3-alt1
- 2.6.3

* Thu Mar 25 2021 Yuri N. Sedunov <aris@altlinux.org> 2.6.2-alt1
- 2.6.2

* Wed Mar 24 2021 Yuri N. Sedunov <aris@altlinux.org> 2.6.1-alt1
- 2.6.1

* Wed Oct 28 2020 Yuri N. Sedunov <aris@altlinux.org> 2.5.0-alt1
- 2.5.0

* Tue Jul 07 2020 Yuri N. Sedunov <aris@altlinux.org> 2.4.2-alt1
- 2.4.2

* Mon Jul 06 2020 Yuri N. Sedunov <aris@altlinux.org> 2.4.1-alt1
- 2.4.1

* Thu Jul 02 2020 Yuri N. Sedunov <aris@altlinux.org> 2.4.0-alt1
- 2.4.0

* Fri Jun 19 2020 Yuri N. Sedunov <aris@altlinux.org> 2.3.0-alt1
- updated to 2.3.0-2-g5c4bc78

* Sun Jun 07 2020 Yuri N. Sedunov <aris@altlinux.org> 2.2.1-alt1
- 2.2.1

* Sat May 30 2020 Yuri N. Sedunov <aris@altlinux.org> 2.2.0-alt1
- updated to 2.2.0-3-g9ac9c23

* Thu Apr 09 2020 Yuri N. Sedunov <aris@altlinux.org> 2.1.1-alt1
- 2.1.1

* Sun Apr 05 2020 Yuri N. Sedunov <aris@altlinux.org> 2.0.0-alt1
- updated to 2.0.0-2-g351bbd8

* Sun Mar 22 2020 Yuri N. Sedunov <aris@altlinux.org> 1.5.3-alt2
- swithed KindleUnpack to use Python3

* Thu Jul 25 2019 Yuri N. Sedunov <aris@altlinux.org> 1.5.3-alt1
- 1.5.3

* Fri Jul 19 2019 Yuri N. Sedunov <aris@altlinux.org> 1.5.2-alt1
- 1.5.2

* Thu Jul 18 2019 Yuri N. Sedunov <aris@altlinux.org> 1.5.1-alt1
- 1.5.1

* Mon Jul 15 2019 Yuri N. Sedunov <aris@altlinux.org> 1.5.0-alt1
- 1.5.0

* Mon Jul 08 2019 Yuri N. Sedunov <aris@altlinux.org> 1.4.0-alt1
- 1.4.0

* Sun Jun 30 2019 Yuri N. Sedunov <aris@altlinux.org> 1.3.1-alt1
- 1.3.1

* Tue Jun 18 2019 Yuri N. Sedunov <aris@altlinux.org> 1.3.0-alt1
- updated to 1.3.0-3-g3e30e73

* Fri Jun 07 2019 Yuri N. Sedunov <aris@altlinux.org> 1.2.1-alt1
- 1.2.1

* Thu Jun 06 2019 Yuri N. Sedunov <aris@altlinux.org> 1.2.0-alt1
- 1.2.0

* Tue Jun 04 2019 Yuri N. Sedunov <aris@altlinux.org> 1.1.1-alt1
- 1.1.1

* Mon Jun 03 2019 Yuri N. Sedunov <aris@altlinux.org> 1.1.0-alt1
- 1.1.0

* Sun Jun 02 2019 Yuri N. Sedunov <aris@altlinux.org> 1.0.1-alt1
- first build for Sisyphus



