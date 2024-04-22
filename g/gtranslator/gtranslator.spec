%def_disable snapshot

%define ver_major 46
%define beta %nil
%define api_ver 3.0
%define xdg_name org.gnome.Gtranslator

%def_disable gtk_doc

Name: gtranslator
Version: %ver_major.1
Release: alt1%beta

Summary: A GNOME po file editor with many bells and whistles.
License: GPLv3
Group: Development/Tools
Url: https://wiki.gnome.org/Apps/Gtranslator

%if_disabled snapshot
Source: ftp://ftp.gnome.org/pub/gnome/sources/%name/%ver_major/%name-%version.tar.xz
%else
Source: %name-%version.tar
%endif

Requires: libgda6-sqlite gettext-tools

%define gtk_ver 4.12.0
%define adw_ver 1.5
%define spell_ver 0.2.0
%define gtksourceview_api_ver 5
%define gtksourceview_ver 5.10.0
%define xml_ver 2.4.12

BuildRequires(pre): rpm-macros-meson rpm-build-gir
BuildRequires: meson yelp-tools gtk-doc
BuildRequires: libgtk4-devel >= %gtk_ver
BuildRequires: pkgconfig(libadwaita-1) >= %adw_ver
BuildRequires: libgda6-devel libgtksourceview%gtksourceview_api_ver-devel >= %gtksourceview_ver
BuildRequires: libsoup3.0-devel gsettings-desktop-schemas-devel iso-codes-devel
BuildRequires: libspelling-devel >= %spell_ver libxml2-devel >= %xml_ver
BuildRequires: libjson-glib-devel

%description
gtranslator is a quite comfortable gettext po/po.gz/(g)mo files editor
for the GNOME 3.x platform with many features. It's evolving quite fast
and many useful functions are already implemented; gtranslator aims to
be a very complete editing environment for translation issues within the
GNU gettext/GNOME desktop world.

%package devel
Summary: %name header files
Group: Development/C
BuildArch: noarch
Requires: %name = %EVR

%description devel
This package provides header files needed for build %name plugins.

%package devel-doc
Summary: %name development documentation
Group: Development/C
BuildArch: noarch
Conflicts: %name < %version

%description devel-doc
This package contains documentation needed to develop %name plugins.

%set_typelibdir %_libdir/%name/girepository-1.0

%prep
%setup

%build
%meson -Dbuildtype=release \
%{?_enable_gtk_doc:-Dgtk_doc=true}
%nil
%meson_build

%install
%meson_install
%find_lang --with-gnome %name

%files -f %name.lang
%_bindir/%name
%_datadir/%name/
%_datadir/gtksourceview-%gtksourceview_api_ver/language-specs/%name.lang
%_datadir/glib-2.0/schemas/*.xml
%_desktopdir/%xdg_name.desktop
%_iconsdir/hicolor/*/apps/%{xdg_name}*.svg
%_man1dir/%name.1*
%_datadir/metainfo/%xdg_name.appdata.xml
%doc AUTHORS NEWS README* THANKS

%files devel
%_includedir/gtr-marshal.h

%{?_enable_gtk_doc:%files devel-doc
%_datadir/gtk-doc/html/%name/}

%changelog
* Mon Apr 22 2024 Yuri N. Sedunov <aris@altlinux.org> 46.1-alt1%beta
- 46.1

* Thu Mar 21 2024 Yuri N. Sedunov <aris@altlinux.org> 46.0-alt1
- 46.0

* Wed Oct 25 2023 Yuri N. Sedunov <aris@altlinux.org> 45.3-alt1
- 45.3

* Mon Oct 02 2023 Yuri N. Sedunov <aris@altlinux.org> 45.2-alt1
- 45.2

* Thu Sep 21 2023 Yuri N. Sedunov <aris@altlinux.org> 45.1-alt1
- 45.1 (ported to GTK4/Libadwaita/libspelling)

* Mon Apr 11 2022 Yuri N. Sedunov <aris@altlinux.org> 42.0-alt1
- 42.0

* Sun Mar 27 2022 Yuri N. Sedunov <aris@altlinux.org> 41.0-alt2
- updated to 41.0-6-gab775966 (updated translations)
- fixed build with meson >= 0.61

* Tue Mar 01 2022 Yuri N. Sedunov <aris@altlinux.org> 41.0-alt1
- 41.0

* Thu Dec 16 2021 Yuri N. Sedunov <aris@altlinux.org> 40.0-alt2
- updated to 40.0-12-g1becbcdf
- fixed meson options

* Fri Apr 09 2021 Yuri N. Sedunov <aris@altlinux.org> 40.0-alt1
- 40.0

* Fri Sep 18 2020 Yuri N. Sedunov <aris@altlinux.org> 3.38.0-alt1
- 3.38.0

* Sat Mar 14 2020 Yuri N. Sedunov <aris@altlinux.org> 3.36.0-alt1
- 3.36.0

* Tue Sep 10 2019 Yuri N. Sedunov <aris@altlinux.org> 3.34.0-alt1
- 3.34.0

* Sun Apr 21 2019 Yuri N. Sedunov <aris@altlinux.org> 3.32.1-alt1
- 3.32.1

* Mon Mar 11 2019 Yuri N. Sedunov <aris@altlinux.org> 3.32.0-alt1
- 3.32.0

* Fri Nov 23 2018 Yuri N. Sedunov <aris@altlinux.org> 3.30.1-alt1
- 3.30.1

* Sat Nov 03 2018 Yuri N. Sedunov <aris@altlinux.org> 3.30.0-alt1
- 3.30.0

* Sun Dec 30 2012 Yuri N. Sedunov <aris@altlinux.org> 2.91.6-alt4
- 2.91.6

* Mon Dec 03 2012 Yuri N. Sedunov <aris@altlinux.org> 2.91.5-alt3
- rebuild against libgda5

* Sat Dec 01 2012 Yuri N. Sedunov <aris@altlinux.org> 2.91.5-alt2
- updated to 398ebe3e8

* Tue Oct 02 2012 Yuri N. Sedunov <aris@altlinux.org> 2.91.5-alt1.2
- rebuilt against libgdl-3.so.5

* Tue Jun 12 2012 Yuri N. Sedunov <aris@altlinux.org> 2.91.5-alt1.1
- used %%set_typelibdir macros

* Thu Jun 07 2012 Yuri N. Sedunov <aris@altlinux.org> 2.91.5-alt1
- 2.91.5

* Sat Oct 09 2010 Valery Inozemtsev <shrek@altlinux.ru> 1.9.12-alt1
- 1.9.12

* Fri May 14 2010 Valery Inozemtsev <shrek@altlinux.ru> 1.9.11-alt1
- 1.9.11

* Wed Apr 21 2010 Valery Inozemtsev <shrek@altlinux.ru> 1.9.10-alt1
- 1.9.10

* Sun Feb 21 2010 Valery Inozemtsev <shrek@altlinux.ru> 1.9.9-alt1
- 1.9.9

* Thu Feb 11 2010 Valery Inozemtsev <shrek@altlinux.ru> 1.9.8-alt1
- 1.9.8

* Mon Feb 01 2010 Valery Inozemtsev <shrek@altlinux.ru> 1.9.7-alt1
- 1.9.7

* Wed Dec 23 2009 Valery Inozemtsev <shrek@altlinux.ru> 1.9.6-alt2
- rebuild with libgdl 2.28.2

* Tue Aug 25 2009 Valery Inozemtsev <shrek@altlinux.ru> 1.9.6-alt1
- 1.9.6

* Fri Jul 10 2009 Valery Inozemtsev <shrek@altlinux.ru> 1.9.5-alt3
- updated translation

* Tue Jun 09 2009 Valery Inozemtsev <shrek@altlinux.ru> 1.9.5-alt2
- updated build dependencies

* Wed Jun 03 2009 Valery Inozemtsev <shrek@altlinux.ru> 1.9.5-alt1
- initial relese

