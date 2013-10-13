%define ver_major 3.10
%define _libexecdir %_prefix/libexec

Name: bijiben
Version: %ver_major.1
Release: alt1

Summary: Note editor for GNOME
License: LGPLv3+
Group: Graphical desktop/GNOME
Url: https://live.gnome.org/Bijiben

Source: ftp://ftp.gnome.org/pub/gnome/sources/%name/%ver_major/%name-%version.tar.xz

%define glib_ver 2.28
%define gtk_ver 3.9.3
%define tracker_ver 0.16

BuildPreReq: libgtk+3-devel >= %gtk_ver
BuildPreReq: libgio-devel >= %glib_ver
BuildPreReq: tracker-devel >= %tracker_ver
BuildRequires: libxml2-devel libclutter-gtk3-devel libwebkitgtk3-devel
BuildRequires: libgnome-online-accounts-devel libzeitgeist2.0-devel
BuildRequires: rpm-build-xdg gnome-common intltool yelp-tools
BuildRequires: libuuid-devel

%description
Bijiben is an attempt to design an intuitive note editor with strong
desktop integration.

%prep
%setup

%build
%configure \
	--disable-static \
	--disable-schemas-compile \
	--disable-update-mimedb
%make_build

%install
%makeinstall_std

%find_lang --with-gnome %name

%files -f %name.lang
%_bindir/*
%_libexecdir/%name-shell-search-provider
%_datadir/applications/*
%_datadir/%name
%_iconsdir/hicolor/*x*/*/%name.png
#%_iconsdir/hicolor/scalable/*/%name.svg
%_iconsdir/HighContrast/scalable/apps/bijiben.svg
%_datadir/gnome-shell/search-providers/%name-search-provider.ini
%_datadir/dbus-1/services/org.gnome.Bijiben.SearchProvider.service
%_xdgmimedir/packages/bijiben.xml
%config %_datadir/glib-2.0/schemas/org.gnome.%name.gschema.xml
%_datadir/appdata/%name.appdata.xml
%doc README AUTHORS NEWS

%changelog
* Mon Oct 14 2013 Yuri N. Sedunov <aris@altlinux.org> 3.10.1-alt1
- 3.10.1

* Mon Sep 23 2013 Yuri N. Sedunov <aris@altlinux.org> 3.10.0-alt1
- 3.10.0

* Mon Aug 19 2013 Yuri N. Sedunov <aris@altlinux.org> 3.8.4-alt1
- 3.8.4

* Sat Jun 22 2013 Yuri N. Sedunov <aris@altlinux.org> 3.8.3-alt1
- 3.8.3

* Sat May 11 2013 Yuri N. Sedunov <aris@altlinux.org> 3.8.2-alt1
- 3.8.2

* Thu Apr 18 2013 Yuri N. Sedunov <aris@altlinux.org> 3.8.1-alt1
- 3.8.1

* Wed Mar 27 2013 Yuri N. Sedunov <aris@altlinux.org> 3.8.0-alt1
- 3.8.0

* Mon Mar 18 2013 Yuri N. Sedunov <aris@altlinux.org> 3.7.92-alt1
- first build for people/gnome

