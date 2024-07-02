%def_enable snapshot
%define _libexecdir %_prefix/libexec

%define rdn_name com.github.FontManager.FontManager
%define rdn_name1 com.github.FontManager.FontViewer

%def_with nautilus
%define nautilus_extdir %_libdir/nautilus/extensions-4

Name: font-manager
Version: 0.9.0
Release: alt1

Summary: A font management application for the GNOME desktop
License: GPL-3.0-or-later
Group: Graphical desktop/GNOME
Url: http://fontmanager.github.io/

%if_disabled snapshot
Source: https://github.com/FontManager/%name/archive/%version/%name-%version.tar.gz
%else
Vcs: https://github.com/FontManager/font-manager.git
Source: %name-%version.tar
%endif

Requires: file-roller

%define vala_ver 0.42
%define pango_ver 1.4
%define adw_ver 1.5

BuildRequires(pre): meson rpm-build-gir
BuildRequires: vala-tools >= %vala_ver
BuildRequires: libpango-devel >= %pango_ver
BuildRequires: pkgconfig(libadwaita-1) >= %adw_ver
BuildRequires: libjson-glib-devel
BuildRequires: libsqlite3-devel libxml2-devel
BuildRequires: yelp-tools desktop-file-utils /usr/bin/appstream-util
BuildRequires: gobject-introspection-devel libjson-glib-gir-devel gir(Adw) = 1
BuildRequires: pkgconfig(webkitgtk-6.0)
%if_with nautilus
BuildRequires: libnautilus-devel
%endif

%description
Font Manager is an application that allows users to easily manage fonts
on their system.

Font Manager is not intended to be a professional-grade font management
solution, but rather a simple application suitable for the needs of most
desktop users, and even graphics designers who may need to manage just a
few thousand font files.

Although designed with the GNOME desktop environment in mind, it should
work well with most major desktop environments such as XFCE,
Enlightenment, and even KDE.

%prep
%setup

%build
%meson \
	-Dreproducible=true \
	%{?_with_nautilus:-Dnautilus=true}
%meson_build

%install
%meson_install
%find_lang --with-gnome %name

%files -f %name.lang
%_bindir/%name
%dir %_libexecdir/%name
%_libexecdir/%name/font-viewer
%_libdir/%name/
%_desktopdir/%rdn_name.desktop
%_desktopdir/%rdn_name1.desktop
%_datadir/dbus-1/services/%rdn_name.service
%_datadir/dbus-1/services/%rdn_name1.service
%_datadir/glib-2.0/schemas/%rdn_name.gschema.xml
%_datadir/glib-2.0/schemas/%rdn_name1.gschema.xml
%_iconsdir/hicolor/*/apps/*.svg
%_datadir/gnome-shell/search-providers/%rdn_name.SearchProvider.ini
%_man1dir/%name.1.*
%_datadir/metainfo/%rdn_name.metainfo.xml
%_datadir/metainfo/%rdn_name1.metainfo.xml
%{?_with_nautilus:%nautilus_extdir/*.so}
%doc README* CHANGELOG


%changelog
* Tue Jul 02 2024 Yuri N. Sedunov <aris@altlinux.org> 0.9.0-alt1
- 0.9.0-1-g77df195c (ported to GTK4/Libadwaita)

* Thu May 23 2024 Yuri N. Sedunov <aris@altlinux.org> 0.8.9-alt1
- 0.8.9

* Sun May 19 2024 Yuri N. Sedunov <aris@altlinux.org> 0.8.8-alt3
- updated to 0.8.8-68-g4c15fe6c
- enabled nautilus support again

* Wed Sep 21 2022 Yuri N. Sedunov <aris@altlinux.org> 0.8.8-alt2
- disabled Nautilus support

* Mon Feb 28 2022 Yuri N. Sedunov <aris@altlinux.org> 0.8.8-alt1
- 0.8.8

* Sat Jan 15 2022 Yuri N. Sedunov <aris@altlinux.org> 0.8.7-alt2
- updated to 0.8.7-41-g85dd400

* Tue Jul 27 2021 Yuri N. Sedunov <aris@altlinux.org> 0.8.7-alt1
- 0.8.7

* Sun Apr 11 2021 Yuri N. Sedunov <aris@altlinux.org> 0.8.6-alt1
- 0.8.6

* Fri Apr 09 2021 Yuri N. Sedunov <aris@altlinux.org> 0.8.5-alt1
- 0.8.5-1-5-g4d6f3fd

* Mon Feb 01 2021 Yuri N. Sedunov <aris@altlinux.org> 0.8.4-alt1
- 0.8.4

* Sat Dec 05 2020 Yuri N. Sedunov <aris@altlinux.org> 0.8.3-alt1
- 0.8.3

* Thu Nov 26 2020 Yuri N. Sedunov <aris@altlinux.org> 0.8.0-alt1
- 0.8.0

* Mon Sep 21 2020 Yuri N. Sedunov <aris@altlinux.org> 0.7.9-alt1
- 0.7.9

* Fri Jul 10 2020 Yuri N. Sedunov <aris@altlinux.org> 0.7.8-alt1
- updated to 0.7.8-1-ge750377

* Fri Dec 20 2019 Yuri N. Sedunov <aris@altlinux.org> 0.7.7-alt1
- updated to 0.7.7-2-g456d80b

* Sat Apr 27 2019 Yuri N. Sedunov <aris@altlinux.org> 0.7.5-alt2
- fixed build (ALT #36689)

* Sun Apr 21 2019 Yuri N. Sedunov <aris@altlinux.org> 0.7.5-alt1
- 0.7.5 (ported to Meson build system)
- built nautilus extension with python3 (nautilus-python-1.2.2-alt2)

* Tue Mar 19 2019 Yuri N. Sedunov <aris@altlinux.org> 0.7.4.3-alt1
- updated to 0.7.4.3-13-g96b3261

* Thu Jan 31 2019 Yuri N. Sedunov <aris@altlinux.org> 0.7.4.2-alt1
- 0.7.4.2

* Sat Sep 08 2018 Yuri N. Sedunov <aris@altlinux.org> 0.7.3.1-alt1
- 0.7.3.1

* Tue Apr 25 2017 Yuri N. Sedunov <aris@altlinux.org> 0.7.3-alt2
- updated to 0.7.3-11-gb4ee339

* Fri Oct 28 2016 Yuri N. Sedunov <aris@altlinux.org> 0.7.3-alt1
- 0.7.3

* Fri May 29 2015 Yuri N. Sedunov <aris@altlinux.org> 0.7.2-alt1
- 0.7.2 release (rev 425)

* Tue Apr 28 2015 Yuri N. Sedunov <aris@altlinux.org> 0.7.2-alt0.1
- 0.7.2, rev 422

* Sat Nov 29 2014 Yuri N. Sedunov <aris@altlinux.org> 0.7.1-alt1
- 0.7.1

* Sat Mar 17 2012 Yuri N. Sedunov <aris@altlinux.org> 0.5.7-alt2
- fixed build

* Fri Jan 06 2012 Yuri N. Sedunov <aris@altlinux.org> 0.5.7-alt1
- 0.5.7

* Tue Oct 25 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.5.5-alt1.1
- Rebuild with Python-2.7

* Wed Jun 30 2010 Yuri N. Sedunov <aris@altlinux.org> 0.5.5-alt1
- 0.5.5

* Wed Jun 09 2010 Yuri N. Sedunov <aris@altlinux.org> 0.5.4-alt1
- 0.5.4

* Wed May 05 2010 Yuri N. Sedunov <aris@altlinux.org> 0.5.2-alt1
- 0.5.2

* Wed Mar 10 2010 Yuri N. Sedunov <aris@altlinux.org> 0.4.4-alt1
- first build for Sisyphus

