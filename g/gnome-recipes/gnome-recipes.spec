%define ver_major 2.0
%define xdg_name org.gnome.Recipes

Name: gnome-recipes
Version: %ver_major.2
Release: alt2

Summary: GNOME likes to cook
License: GPLv3+
Group: Office
Url: https://wiki.gnome.org/Apps/Recipes

Source: ftp://ftp.gnome.org/pub/gnome/sources/%name/%ver_major/%name-%version.tar.xz

Obsoletes: recipes < 0.14
Provides: recipes = %EVR

Requires: %name-data = %EVR

%define gtk_ver 3.20

BuildRequires: meson git-core libappstream-glib-devel rpm-build-xdg yelp-tools
BuildRequires: libgtk+3-devel >= %gtk_ver libjson-glib-devel
BuildRequires: libgspell-devel libgnome-autoar-devel libsoup-devel
BuildRequires: libcanberra-gtk3-devel
BuildRequires: libgnome-online-accounts-devel librest-devel
BuildRequires: vala-tools gobject-introspection-devel

%description
Recipes is an easy to use app that will help you to discover what to cook today,
tomorrow, the rest of the week and for your special occasions.

%package data
Summary: Recipes data files
Group: Office
BuildArch: noarch
Obsoletes: recipes-data < 0.14
Provides: recipes-data = %EVR

%description data
Recipes is an easy to use app that will help you to discover what to cook today,
tomorrow, the rest of the week and for your special occasions.

This package contains common noarch files needed for Recipes.


%prep
%setup

%build
%meson
%meson_build

%install
%meson_install
%find_lang %name
%find_lang --with-gnome --output=%name.lang %name %name-data %xdg_name

%check
%meson_test

%files
%_bindir/%name
%doc README.md

%files data -f %name.lang
%_datadir/%name/
%_desktopdir/%xdg_name.desktop
%_datadir/dbus-1/services/%xdg_name.service
%_datadir/gnome-shell/search-providers/%xdg_name-search-provider.ini
%_datadir/glib-2.0/schemas/%xdg_name.gschema.xml
%_iconsdir/hicolor/*x*/apps/*.png
%_iconsdir/hicolor/symbolic/apps/*.svg
%_xdgmimedir/packages/org.gnome.Recipes-mime.xml
%_datadir/appdata/%xdg_name.appdata.xml


%changelog
* Tue Mar 13 2018 Yuri N. Sedunov <aris@altlinux.org> 2.0.2-alt2
- rebuilt against libgspell-1.so.2

* Sun Nov 12 2017 Yuri N. Sedunov <aris@altlinux.org> 2.0.2-alt1
- 2.0.2

* Mon Oct 30 2017 Yuri N. Sedunov <aris@altlinux.org> 2.0.0-alt1
- 2.0.0

* Thu Jul 27 2017 Yuri N. Sedunov <aris@altlinux.org> 1.6.2-alt1
- 1.6.2

* Thu Jun 22 2017 Yuri N. Sedunov <aris@altlinux.org> 1.4.6-alt1
- 1.4.6

* Sun May 07 2017 Yuri N. Sedunov <aris@altlinux.org> 1.0.6-alt1
- 1.0.6

* Sun Apr 02 2017 Yuri N. Sedunov <aris@altlinux.org> 1.0.4-alt1
- 1.0.4

* Sat Apr 01 2017 Yuri N. Sedunov <aris@altlinux.org> 1.0.2-alt1
- 1.0.2

* Sat Mar 18 2017 Yuri N. Sedunov <aris@altlinux.org> 1.0.0-alt1
- 1.0.0

* Mon Mar 13 2017 Yuri N. Sedunov <aris@altlinux.org> 0.22.0-alt1
- 0.22.0

* Sat Mar 04 2017 Yuri N. Sedunov <aris@altlinux.org> 0.20.0-alt1
- 0.20.0

* Thu Mar 02 2017 Yuri N. Sedunov <aris@altlinux.org> 0.18.0-alt1
- 0.18.0

* Sun Feb 26 2017 Yuri N. Sedunov <aris@altlinux.org> 0.16.0-alt1
- 0.16.0

* Mon Feb 20 2017 Yuri N. Sedunov <aris@altlinux.org> 0.14.2-alt1
- 0.14.2

* Wed Feb 08 2017 Yuri N. Sedunov <aris@altlinux.org> 0.10.0-alt1
- 0.10.0

* Thu Jan 19 2017 Yuri N. Sedunov <aris@altlinux.org> 0.8.0-alt1
- 0.8.0

* Mon Jan 09 2017 Yuri N. Sedunov <aris@altlinux.org> 0.6.0-alt1
- first build for Sisyphus

