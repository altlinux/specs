%define ver_major 3.18
%define _libexecdir %_prefix/libexec

Name: bijiben
Version: %ver_major.2
Release: alt2

Summary: Note editor for GNOME
License: LGPLv3+
Group: Graphical desktop/GNOME
Url: https://wiki.gnome.org/Apps/Bijiben

Source: ftp://ftp.gnome.org/pub/gnome/sources/%name/%ver_major/%name-%version.tar.xz

%define glib_ver 2.28
%define gtk_ver 3.11.4
%define tracker_ver 0.17
%define eds_ver 3.13.90

BuildPreReq: libgtk+3-devel >= %gtk_ver
BuildPreReq: libgio-devel >= %glib_ver
BuildPreReq: tracker-devel >= %tracker_ver
BuildRequires: libxml2-devel libclutter-gtk3-devel libwebkitgtk3-devel
BuildRequires: libgnome-online-accounts-devel libzeitgeist2.0-devel libuuid-devel
BuildRequires: evolution-data-server-devel >= %eds_ver libical-devel libicu-devel
BuildRequires: rpm-build-xdg gnome-common intltool yelp-tools libappstream-glib-devel

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
%make_build V=1

%install
%makeinstall_std

%find_lang --with-gnome %name

%files -f %name.lang
%_bindir/*
%_libexecdir/%name-shell-search-provider
%_datadir/applications/*
%_datadir/%name
%_iconsdir/hicolor/*x*/*/%name.png
%_iconsdir/hicolor/scalable/*/%name-symbolic.svg
%_datadir/gnome-shell/search-providers/%name-search-provider.ini
%_datadir/dbus-1/services/org.gnome.Bijiben.SearchProvider.service
%_xdgmimedir/packages/bijiben.xml
%config %_datadir/glib-2.0/schemas/org.gnome.%name.gschema.xml
%_datadir/appdata/%name.appdata.xml
%doc README AUTHORS NEWS

%changelog
* Fri Jan 22 2016 Yuri N. Sedunov <aris@altlinux.org> 3.18.2-alt2
- rebuilt against libical.so.2

* Mon Nov 09 2015 Yuri N. Sedunov <aris@altlinux.org> 3.18.2-alt1
- 3.18.2

* Mon Oct 12 2015 Yuri N. Sedunov <aris@altlinux.org> 3.18.1-alt1
- 3.18.1

* Sun Sep 20 2015 Yuri N. Sedunov <aris@altlinux.org> 3.18.0-alt1
- 3.18.0

* Tue May 12 2015 Yuri N. Sedunov <aris@altlinux.org> 3.16.2-alt1
- 3.16.2

* Mon Apr 13 2015 Yuri N. Sedunov <aris@altlinux.org> 3.16.1-alt1
- 3.16.1

* Sat Mar 28 2015 Yuri N. Sedunov <aris@altlinux.org> 3.16.0-alt1
- 3.16.0

* Mon Mar 02 2015 Yuri N. Sedunov <aris@altlinux.org> 3.15.91-alt1
- 3.15.91

* Tue Nov 11 2014 Yuri N. Sedunov <aris@altlinux.org> 3.14.2-alt1
- 3.14.2

* Tue Oct 14 2014 Yuri N. Sedunov <aris@altlinux.org> 3.14.1-alt1
- 3.14.1

* Tue Sep 23 2014 Yuri N. Sedunov <aris@altlinux.org> 3.14.0-alt1
- 3.14.0

* Tue May 13 2014 Yuri N. Sedunov <aris@altlinux.org> 3.12.2-alt1
- 3.12.2

* Tue Mar 25 2014 Yuri N. Sedunov <aris@altlinux.org> 3.12.0-alt1
- 3.12.0

* Tue Nov 12 2013 Yuri N. Sedunov <aris@altlinux.org> 3.10.2-alt1
- 3.10.2

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

