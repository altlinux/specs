%define ver_major 0.6
%define xdg_name org.gnome.Recipes

Name: recipes
Version: %ver_major.0
Release: alt1

Summary: GNOME likes to cook
License: GPLv3+
Group: Office
Url: https://wiki.gnome.org/Apps/Recipes

Source: ftp://ftp.gnome.org/pub/gnome/sources/%name/%ver_major/%name-%version.tar.xz

Requires: %name-data = %EVR

%define gtk_ver 3.20

BuildRequires: autoconf-archive libappstream-glib-devel
BuildRequires: libgtk+3-devel >= %gtk_ver libjson-glib-devel
BuildRequires: libgspell-devel libgnome-autoar-devel vala-tools

%description
Recipes is an easy to use app that will help you to discover what to cook today,
tomorrow, the rest of the week and for your special occasions.

%package data
Summary: Recipes data files
Group: Office
BuildArch: noarch

%description data
Recipes is an easy to use app that will help you to discover what to cook today,
tomorrow, the rest of the week and for your special occasions.

This package contains common noarch files needed for Recipes.


%prep
%setup

%build
%autoreconf
%configure --disable-static
%make_build

%install
%makeinstall_std
rm -f %buildroot%_libdir/%name/*.{a,la}

%find_lang --with-gnome %name

%check
%make check

%files -f %name.lang
%_bindir/%name
%_libdir/%name/
%doc NEWS

%files data
%_datadir/%name/
%_desktopdir/%xdg_name.desktop
%_datadir/dbus-1/services/%xdg_name.service
%_datadir/gnome-shell/search-providers/%xdg_name-search-provider.ini
#%_datadir/glib-2.0/schemas/%xdg_name.gschema.xml
%_iconsdir/hicolor/*x*/apps/*.png
%_iconsdir/hicolor/symbolic/apps/*.svg
%_datadir/appdata/%xdg_name.appdata.xml


%changelog
* Mon Jan 09 2017 Yuri N. Sedunov <aris@altlinux.org> 0.6.0-alt1
- first build for Sisyphus

