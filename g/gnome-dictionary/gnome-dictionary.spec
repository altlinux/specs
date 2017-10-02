%define ver_major 3.26
%define xdg_name org.gnome.Dictionary
%define api_ver 1.0

Name: gnome-dictionary
Version: %ver_major.1
Release: alt1

Summary: Gnome client for MIT dictionary server
Group: Graphical desktop/GNOME
License: LGPLv2.1
Url: https://wiki.gnome.org/Apps/Dictionary

Source: %gnome_ftp/%name/%ver_major/%name-%version.tar.xz

Obsoletes: libgdict < %version

%define glib_ver 2.42.0
%define gtk_ver 3.22.7

BuildPreReq: meson rpm-build-gnome yelp-tools
BuildRequires: libappstream-glib-devel desktop-file-utils
BuildRequires: libgio-devel >= %glib_ver libgtk+3-devel >= %gtk_ver
# for man
BuildRequires: xsltproc docbook-dtds docbook-style-xsl

%description
GNOME Dictionary - look up an online dictionary for definitions and
correct spelling of words.

%prep
%setup

%build
%meson -Denable-ipv6=true
%meson_build

%install
%meson_install

%find_lang --with-gnome %name

%files -f %name.lang
%_bindir/%name
%_desktopdir/%xdg_name.desktop
%_datadir/dbus-1/services/%xdg_name.service
%_datadir/glib-2.0/schemas/org.gnome.dictionary.gschema.xml
%_datadir/gdict-%api_ver/
%_datadir/appdata/%xdg_name.appdata.xml
%_man1dir/%name.*
%doc NEWS README*

%changelog
* Sun Oct 01 2017 Yuri N. Sedunov <aris@altlinux.org> 3.26.1-alt1
- 3.26.1

* Tue Sep 12 2017 Yuri N. Sedunov <aris@altlinux.org> 3.26.0-alt1
- 3.26.0

* Mon Mar 20 2017 Yuri N. Sedunov <aris@altlinux.org> 3.24.0-alt1
- 3.24.0

* Tue Mar 22 2016 Yuri N. Sedunov <aris@altlinux.org> 3.20.0-alt1
- 3.20.0

* Tue Jan 19 2016 Yuri N. Sedunov <aris@altlinux.org> 3.18.1-alt1
- 3.18.1

* Mon Sep 21 2015 Yuri N. Sedunov <aris@altlinux.org> 3.18.0-alt1
- 3.18.0

* Mon May 11 2015 Yuri N. Sedunov <aris@altlinux.org> 3.16.2-alt1
- 3.16.2

* Mon Apr 13 2015 Yuri N. Sedunov <aris@altlinux.org> 3.16.1-alt1
- 3.16.1

* Wed Mar 25 2015 Yuri N. Sedunov <aris@altlinux.org> 3.16.0-alt1
- 3.16.0

* Mon Nov 10 2014 Yuri N. Sedunov <aris@altlinux.org> 3.14.2-alt1
- 3.14.2

* Sun Oct 12 2014 Yuri N. Sedunov <aris@altlinux.org> 3.14.1-alt1
- 3.14.1

* Tue Sep 23 2014 Yuri N. Sedunov <aris@altlinux.org> 3.14.0-alt1
- 3.14.0

* Wed Oct 09 2013 Yuri N. Sedunov <aris@altlinux.org> 3.10.0-alt1
- 3.10.0

* Sun Jul 21 2013 Yuri N. Sedunov <aris@altlinux.org> 3.8.0-alt1
- 3.8.0

* Wed Sep 26 2012 Yuri N. Sedunov <aris@altlinux.org> 3.6.0-alt1
- 3.6.0

* Mon Mar 26 2012 Yuri N. Sedunov <aris@altlinux.org> 3.4.0-alt1
- 3.4.0

* Fri Mar 09 2012 Yuri N. Sedunov <aris@altlinux.org> 3.3.2-alt1
- 3.3.2 snapshot


