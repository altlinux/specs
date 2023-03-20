%def_disable snapshot
%define xdg_name org.gnome.Evince

%define _libexecdir %_prefix/libexec
%define ver_major 44
%define beta %nil
%define api_ver_major 3
%define api_ver %api_ver_major.0
%define so_ver 4

%def_enable xps
%def_enable ps
%def_enable t1lib
%def_enable dbus
%def_enable introspection
%def_enable multimedia
%def_disable nautilus
%def_enable gtk_doc
%def_disable debug

Name: evince
Version: %ver_major.0
Release: alt1%beta

Summary: A document viewer
Group: Office
License: GPL-2.0-or-later
Url: http://www.gnome.org/projects/evince/

%if_disabled snapshot
Source: ftp://ftp.gnome.org/pub/gnome/sources/%name/%ver_major/%name-%version%beta.tar.xz
%else
Source: %name-%version.tar
%endif

Requires: lib%name = %EVR
Requires: %name-data = %EVR
Requires: gnome-icon-theme gnome-icon-theme-symbolic icon-theme-adwaita
Requires: gvfs-backend-recent-files
Requires: dconf
%{?_enable_multimedia:Requires: gst-plugins-base1.0 gst-libav}

%define poppler_ver 22.02.0
%define libarchive_ver 3.6.0
%define gtk_ver 3.22
%define handy_ver 1.5.0
%define spectre_ver 0.2.0

BuildRequires(pre): rpm-macros-meson
BuildRequires: meson libpoppler-glib-devel >= %poppler_ver
BuildRequires: libgtk+3-devel >= %gtk_ver
BuildRequires: gcc-c++ gnome-common libappstream-glib-devel yelp-tools
BuildRequires: icon-theme-adwaita libdjvu-devel libgnome-keyring-devel
BuildRequires: libspectre-devel >= %spectre_ver libtiff-devel
BuildRequires: libxml2-devel libkpathsea-devel libgail3-devel gsettings-desktop-schemas-devel
BuildRequires: zlib-devel libsecret-devel libarchive-devel >= %libarchive_ver libgspell-devel
BuildRequires: libsynctex-devel
BuildRequires: libgnome-desktop3-devel
BuildRequires: pkgconfig(libhandy-1) >= %handy_ver
%{?_enable_xps:BuildRequires: libgxps-devel}
%{?_enable_t1lib:BuildRequires: t1lib-devel}
%{?_enable_dbus:BuildRequires: libdbus-devel}
%{?_enable_multimedia:BuildRequires: gst-plugins1.0-devel}
%{?_enable_nautilus:BuildRequires: libnautilus-devel}
%{?_enable_introspection:
BuildRequires(pre): rpm-build-gir
BuildRequires: gobject-introspection-devel libgtk+3-gir-devel}
%{?_enable_gtk_doc:BuildRequires: gi-docgen}
BuildRequires: libXi-devel
BuildRequires: pkgconfig(systemd)

%description
Evince is a document viewer capable of displaying multiple and single page
document formats like PDF and Postscript

%package data
Summary: Arch independent files for Evince
Group: Office
BuildArch: noarch

%description data
This package provides noarch data needed for Evince to work.

%package dvi
Summary: Evince backend for dvi files
Group: Office
Requires: %name = %EVR

%description dvi
A backend to let evince display dvi files

%package -n lib%name
Summary: Library for the %name project
Group: System/Libraries

%description -n lib%name
Library for %name project

%package -n lib%name-gir
Summary: GObject introspection data for the Evince library
Group: System/Libraries
Requires: lib%name = %EVR

%description -n lib%name-gir
GObject introspection data for the Evince library

%package -n lib%name-devel
Summary: Development files for the %name
Group: Development/C
Requires: lib%name = %EVR

%description -n lib%name-devel
Header files for %name library

%package -n lib%name-gir-devel
Summary: GObject introspection devel data for the Evince library
Group: Development/Other
BuildArch: noarch
Requires: lib%name-gir = %EVR
Requires: lib%name-devel = %EVR

%description -n lib%name-gir-devel
GObject introspection devel data for the Evince library

%package -n lib%name-devel-doc
Summary: Development documentation for Evince
Group: Development/GNOME and GTK+
BuildArch: noarch
Conflicts: lib%name-devel < %version

%description -n lib%name-devel-doc
This package contains documentation necessary to develop applications
using Evince library.


%prep
%setup -n %name-%version%beta

%build
%meson \
    -Dpdf=enabled \
    -Dtiff=enabled \
    -Ddjvu=enabled \
    -Ddvi=enabled \
    %{?_disable_t1lib:-Dt1lib=disabled} \
    -Dcomics=enabled \
    %{?_disable_gtk_doc:-Dgtk_doc=false} \
    %{?_disable_dbus:-Ddbus=false} \
    %{?_disable_xps:-Dxps=disabled} \
    %{?_enable_ps:-Dps=enabled} \
    %{?_disable_introspection:-Dintrospection=false} \
    %{?_enable_multimedia:-Dmultimedia=enabled} \
    %{?_enbable_nautilus:-Dnautilus=true}
%nil
%meson_build

%install
%meson_install
%find_lang %name --with-gnome

%files
%_bindir/evince*
%{?_enable_dbus:
%_libexecdir/evince*
%_prefix/lib/systemd/user/%xdg_name.service}
%{?_enable_nautilus:%_libdir/nautilus/extensions-3.0/libevince-properties-page.so}
%dir %_libdir/evince
%dir %_libdir/evince/%so_ver
%dir %_libdir/evince/%so_ver/backends
%_libdir/evince/%so_ver/backends/libcomicsdocument.so
%_libdir/evince/%so_ver/backends/libdjvudocument.so
%_libdir/evince/%so_ver/backends/libpdfdocument.so
%{?_enable_ps:%_libdir/evince/%so_ver/backends/libpsdocument.so}
%_libdir/evince/%so_ver/backends/libtiffdocument.so
%{?_enable_xps:%_libdir/evince/%so_ver/backends/libxpsdocument.so}
%_libdir/evince/%so_ver/backends/*.evince-backend
%exclude %_libdir/evince/%so_ver/backends/dvidocument.evince-backend
%doc AUTHORS NEWS* README.md

%files data -f %name.lang
%{?_enable_dbus:%_datadir/dbus-1/services/org.gnome.evince.Daemon.service}
%_datadir/%name/
%_desktopdir/%xdg_name.desktop
%_desktopdir/%xdg_name-previewer.desktop
%_datadir/metainfo/%name-comicsdocument.metainfo.xml
%_datadir/metainfo/%name-djvudocument.metainfo.xml
%_datadir/metainfo/%name-pdfdocument.metainfo.xml
%{?_enable_ps:%_datadir/metainfo/%name-psdocument.metainfo.xml}
%_datadir/metainfo/%name-tiffdocument.metainfo.xml
%_datadir/metainfo/%name-xpsdocument.metainfo.xml
%_datadir/metainfo/%xdg_name.appdata.xml
%_datadir/GConf/gsettings/evince.convert
%_datadir/glib-2.0/schemas/org.gnome.Evince.gschema.xml
%_datadir/thumbnailers/evince.thumbnailer
%_iconsdir/hicolor/*/apps/*
%_man1dir/*.1*

%files -n lib%name
%_libdir/libevdocument%{api_ver_major}.so.%{so_ver}*
%_libdir/libevview%{api_ver_major}.so.*

%files dvi
%_libdir/evince/%so_ver/backends/dvidocument.evince-backend
%_libdir/evince/%so_ver/backends/libdvidocument.so
%_datadir/metainfo/%name-dvidocument.metainfo.xml

%files -n lib%name-devel
%_includedir/evince
%_libdir/libevdocument%{api_ver_major}.so
%_libdir/libevview%{api_ver_major}.so
%_pkgconfigdir/*.pc

%if_enabled gtk_doc
%files -n lib%name-devel-doc
%_datadir/doc/libevdocument
%_datadir/doc/libevview
%endif

%if_enabled introspection
%files -n lib%name-gir
%_libdir/girepository-1.0/EvinceDocument-%api_ver.typelib
%_libdir/girepository-1.0/EvinceView-%api_ver.typelib

%files -n lib%name-gir-devel
%_datadir/gir-1.0/EvinceDocument-%api_ver.gir
%_datadir/gir-1.0/EvinceView-%api_ver.gir
%endif


%changelog
* Sat Mar 18 2023 Yuri N. Sedunov <aris@altlinux.org> 44.0-alt1
- 44.0

* Fri Oct 28 2022 Yuri N. Sedunov <aris@altlinux.org> 43.1-alt1
- 43.1

* Wed Sep 21 2022 Yuri N. Sedunov <aris@altlinux.org> 43.0-alt1
- 43.0
- disabled Nautilus plugin

* Mon May 23 2022 Yuri N. Sedunov <aris@altlinux.org> 42.3-alt1
- 42.3

* Sun Apr 17 2022 Yuri N. Sedunov <aris@altlinux.org> 42.2-alt1
- 42.2

* Sat Mar 19 2022 Yuri N. Sedunov <aris@altlinux.org> 42.1-alt1
- 42.1

* Mon Mar 14 2022 Yuri N. Sedunov <aris@altlinux.org> 41.4-alt1
- 41.4

* Thu Dec 16 2021 Yuri N. Sedunov <aris@altlinux.org> 41.3-alt1.1
- fixed meson options

* Sun Nov 21 2021 Yuri N. Sedunov <aris@altlinux.org> 41.3-alt1
- 41.3

* Sat Oct 09 2021 Yuri N. Sedunov <aris@altlinux.org> 41.2-alt1
- 41.2

* Sat Oct 09 2021 Yuri N. Sedunov <aris@altlinux.org> 40.4-alt2
- 40.4-7-g5fc3dc28 (updated translations)

* Thu Jul 15 2021 Yuri N. Sedunov <aris@altlinux.org> 40.4-alt1
- 40.4
- new -data and libevince-devel-doc subpackages

* Tue Jul 13 2021 Yuri N. Sedunov <aris@altlinux.org> 40.3-alt1
- 40.3

* Wed Jun 09 2021 Yuri N. Sedunov <aris@altlinux.org> 40.2-alt1
- 40.2

* Fri Mar 26 2021 Yuri N. Sedunov <aris@altlinux.org> 40.1-alt1
- 40.1

* Sun Feb 14 2021 Yuri N. Sedunov <aris@altlinux.org> 3.38.2-alt1
- 3.38.2

* Mon Jan 25 2021 Yuri N. Sedunov <aris@altlinux.org> 3.38.1-alt1
- 3.38.1

* Sun Sep 13 2020 Yuri N. Sedunov <aris@altlinux.org> 3.38.0-alt1
- 3.38.0

* Sat Jul 04 2020 Yuri N. Sedunov <aris@altlinux.org> 3.36.7-alt1
- 3.36.7

* Fri Jun 19 2020 Yuri N. Sedunov <aris@altlinux.org> 3.36.6-alt1
- 3.36.6

* Thu Jun 11 2020 Yuri N. Sedunov <aris@altlinux.org> 3.36.5-alt1
- 3.36.5

* Wed Jun 10 2020 Yuri N. Sedunov <aris@altlinux.org> 3.36.4-alt1
- 3.36.4

* Sun May 31 2020 Yuri N. Sedunov <aris@altlinux.org> 3.36.3-alt1
- 3.36.3

* Sat May 30 2020 Yuri N. Sedunov <aris@altlinux.org> 3.36.2-alt1
- 3.36.2 (ported to Meson build system)

* Fri May 29 2020 Yuri N. Sedunov <aris@altlinux.org> 3.36.1-alt1
- 3.36.1

* Tue Mar 24 2020 Yuri N. Sedunov <aris@altlinux.org> 3.36.0-alt2
- made nautilus extension optional

* Sat Mar 07 2020 Yuri N. Sedunov <aris@altlinux.org> 3.36.0-alt1
- 3.36.0

* Tue Nov 26 2019 Yuri N. Sedunov <aris@altlinux.org> 3.34.2-alt1
- 3.34.2

* Mon Oct 07 2019 Yuri N. Sedunov <aris@altlinux.org> 3.34.1-alt1
- 3.34.1

* Sun Sep 29 2019 Yuri N. Sedunov <aris@altlinux.org> 3.34.0-alt1
- 3.34.0

* Sun Sep 29 2019 Yuri N. Sedunov <aris@altlinux.org> 3.32.1-alt1
- 3.32.1

* Wed Sep 11 2019 Yuri N. Sedunov <aris@altlinux.org> 3.32.0-alt3
- rebuilt against libgnome-desktop-3.so.18

* Thu May 16 2019 Yuri N. Sedunov <aris@altlinux.org> 3.32.0-alt2
- updated to 3.32.0-22-g0fecf871

* Thu Mar 14 2019 Yuri N. Sedunov <aris@altlinux.org> 3.32.0-alt1
- 3.32.0

* Tue Oct 23 2018 Yuri N. Sedunov <aris@altlinux.org> 3.30.2-alt1
- 3.30.2

* Sun Sep 30 2018 Yuri N. Sedunov <aris@altlinux.org> 3.30.1-alt1
- 3.30.1

* Tue Sep 04 2018 Yuri N. Sedunov <aris@altlinux.org> 3.30.0-alt1
- 3.30.0

* Sun Sep 02 2018 Yuri N. Sedunov <aris@altlinux.org> 3.28.3-alt1
- 3.28.3

* Tue Apr 10 2018 Yuri N. Sedunov <aris@altlinux.org> 3.28.2-alt1
- 3.28.2

* Mon Mar 12 2018 Yuri N. Sedunov <aris@altlinux.org> 3.28.0-alt1
- 3.28.0

* Sat Feb 10 2018 Igor Vlasenko <viy@altlinux.ru> 3.26.0-alt1.1
- NMU: rebuild with texlive 2016

* Tue Sep 12 2017 Yuri N. Sedunov <aris@altlinux.org> 3.26.0-alt1
- 3.26.0

* Thu Jul 27 2017 Yuri N. Sedunov <aris@altlinux.org> 3.24.1-alt1
- 3.24.1

* Fri Jul 14 2017 Yuri N. Sedunov <aris@altlinux.org> 3.24.0-alt2
- updated to 3.24.0-12-g717df38 (fixed BGO ##691448, 779614,
  784630 (CVE-2017-1000083))

* Mon Mar 20 2017 Yuri N. Sedunov <aris@altlinux.org> 3.24.0-alt1
- 3.24.0

* Wed Oct 12 2016 Yuri N. Sedunov <aris@altlinux.org> 3.22.1-alt1
- 3.22.1

* Tue Sep 20 2016 Yuri N. Sedunov <aris@altlinux.org> 3.22.0-alt1
- 3.22.0

* Thu Jun 23 2016 Yuri N. Sedunov <aris@altlinux.org> 3.20.1-alt1
- 3.20.1

* Mon Mar 21 2016 Yuri N. Sedunov <aris@altlinux.org> 3.20.0-alt1
- 3.20.0

* Wed Nov 11 2015 Yuri N. Sedunov <aris@altlinux.org> 3.18.2-alt1
- 3.18.2

* Wed Oct 21 2015 Yuri N. Sedunov <aris@altlinux.org> 3.18.1-alt1
- 3.18.1

* Mon Sep 21 2015 Yuri N. Sedunov <aris@altlinux.org> 3.18.0-alt1
- 3.18.0

* Wed May 27 2015 Yuri N. Sedunov <aris@altlinux.org> 3.16.1-alt1
- 3.16.1

* Sat Mar 28 2015 Yuri N. Sedunov <aris@altlinux.org> 3.16.0-alt1
- 3.16.0

* Sun Mar 08 2015 Yuri N. Sedunov <aris@altlinux.org> 3.14.2-alt1
- 3.14.2

* Tue Oct 14 2014 Yuri N. Sedunov <aris@altlinux.org> 3.14.1-alt1
- 3.14.1

* Tue Sep 23 2014 Yuri N. Sedunov <aris@altlinux.org> 3.14.0-alt1
- 3.14.0

* Thu Aug 21 2014 Yuri N. Sedunov <aris@altlinux.org> 3.12.2-alt1
- 3.12.2

* Mon Apr 14 2014 Yuri N. Sedunov <aris@altlinux.org> 3.12.1-alt1
- 3.12.1

* Tue Mar 25 2014 Yuri N. Sedunov <aris@altlinux.org> 3.12.0-alt1
- 3.12.0

* Wed Mar 19 2014 Yuri N. Sedunov <aris@altlinux.org> 3.11.92-alt1
- 3.11.92

* Sat Nov 16 2013 Yuri N. Sedunov <aris@altlinux.org> 3.10.3-alt1
- 3.10.3

* Mon Nov 11 2013 Yuri N. Sedunov <aris@altlinux.org> 3.10.2-alt1
- 3.10.2

* Tue Sep 24 2013 Yuri N. Sedunov <aris@altlinux.org> 3.10.0-alt1
- 3.10.0

* Tue Jul 09 2013 Yuri N. Sedunov <aris@altlinux.org> 3.8.3-alt1
- 3.8.3

* Thu Jul 04 2013 Yuri N. Sedunov <aris@altlinux.org> 3.8.2-alt2.1
- added dependendence for icons to work without gnome-shell installed

* Mon Jul 01 2013 Yuri N. Sedunov <aris@altlinux.org> 3.8.2-alt2
- updated to 3059e01 (in particular fixed CVE-2013-3718)
- added gnome-icon-theme-symbolic, dconf to rqs

* Wed May 15 2013 Yuri N. Sedunov <aris@altlinux.org> 3.8.2-alt1
- 3.8.2

* Mon Apr 15 2013 Yuri N. Sedunov <aris@altlinux.org> 3.8.0-alt2
- rebuilt to drop libarchive.so.2 dependence

* Tue Mar 26 2013 Yuri N. Sedunov <aris@altlinux.org> 3.8.0-alt1
- 3.8.0

* Mon Oct 15 2012 Yuri N. Sedunov <aris@altlinux.org> 3.6.1-alt1
- 3.6.1

* Tue Sep 25 2012 Yuri N. Sedunov <aris@altlinux.org> 3.6.0-alt1
- 3.6.0

* Mon Mar 26 2012 Yuri N. Sedunov <aris@altlinux.org> 3.4.0-alt1
- 3.4.0

* Mon Mar 19 2012 Yuri N. Sedunov <aris@altlinux.org> 3.3.92-alt1
- 3.3.92

* Sun Nov 20 2011 Yuri N. Sedunov <aris@altlinux.org> 3.2.1-alt2
- enabled support for XPS documents via libgxps

* Mon Oct 17 2011 Yuri N. Sedunov <aris@altlinux.org> 3.2.1-alt1
- 3.2.1
- introspection enabled

* Sun Oct 16 2011 Yuri N. Sedunov <aris@altlinux.org> 3.2.0-alt1
- 3.2.0

* Sun May 29 2011 Alexey Shabalin <shaba@altlinux.ru> 3.0.2-alt1
- 3.0.2

* Mon Apr 11 2011 Yuri N. Sedunov <aris@altlinux.org> 3.0.0-alt1
- 3.0.0

* Thu Mar 31 2011 Yuri N. Sedunov <aris@altlinux.org> 2.91.93-alt1
- 2.91.93

* Thu Feb 10 2011 Yuri N. Sedunov <aris@altlinux.org> 2.91.6-alt1
- 2.91.6

* Wed Oct 13 2010 Valery Inozemtsev <shrek@altlinux.ru> 2.32.0-alt2
- fixed install gconf schemas

* Thu Oct 07 2010 Valery Inozemtsev <shrek@altlinux.ru> 2.32.0-alt1
- 2.32.0

* Thu Aug 05 2010 Valery Inozemtsev <shrek@altlinux.ru> 2.30.3-alt2
- rebuild with libpoppler-glib.so.5

* Sun Jun 27 2010 Valery Inozemtsev <shrek@altlinux.ru> 2.30.3-alt1
- 2.30.3

* Tue Jun 22 2010 Valery Inozemtsev <shrek@altlinux.ru> 2.30.2-alt1
- 2.30.2

* Thu Apr 29 2010 Valery Inozemtsev <shrek@altlinux.ru> 2.30.1-alt2
- make sure dot_dir exists before creating last_settings file (closes: #23402)

* Mon Apr 26 2010 Valery Inozemtsev <shrek@altlinux.ru> 2.30.1-alt1
- 2.30.1

* Thu Apr 01 2010 Valery Inozemtsev <shrek@altlinux.ru> 2.30.0-alt2
- rebuild

* Tue Mar 30 2010 Valery Inozemtsev <shrek@altlinux.ru> 2.30.0-alt1
- 2.30.0

* Thu Mar 11 2010 Valery Inozemtsev <shrek@altlinux.ru> 2.29.92-alt1
- 2.29.92

* Tue Jan 05 2010 Valery Inozemtsev <shrek@altlinux.ru> 2.29.4-alt1
- 2.29.4

* Thu Dec 17 2009 Valery Inozemtsev <shrek@altlinux.ru> 2.28.2-alt1
- 2.28.2

* Fri Dec 11 2009 Valery Inozemtsev <shrek@altlinux.ru> 2.28.1-alt2
- rebuild with libkpathsea (closes: #22444)

* Tue Oct 20 2009 Valery Inozemtsev <shrek@altlinux.ru> 2.28.1-alt1
- 2.28.1

* Tue Sep 22 2009 Valery Inozemtsev <shrek@altlinux.ru> 2.28.0-alt1
- 2.28.0

* Mon Sep 14 2009 Valery Inozemtsev <shrek@altlinux.ru> 2.27.90-alt2
- updated translations

* Wed Aug 19 2009 Valery Inozemtsev <shrek@altlinux.ru> 2.27.90-alt1
- 2.27.90

* Thu Jun 25 2009 Valery Inozemtsev <shrek@altlinux.ru> 2.27.3-alt1
- 2.27.3

* Wed May 20 2009 Valery Inozemtsev <shrek@altlinux.ru> 2.26.2-alt1
- 2.26.2

* Wed Apr 22 2009 Valery Inozemtsev <shrek@altlinux.ru> 2.26.1-alt1
- 2.26.1

* Fri Mar 13 2009 Evgeny Sinelnikov <sin@altlinux.ru> 2.25.92-alt1
- new version 2.25.92
- rebuild with new libdjvulibre

* Mon Mar 02 2009 Vitaly Lipatov <lav@altlinux.ru> 2.25.91-alt1
- new version 2.25.91
- split libevince and libevince-devel

* Wed Jan 07 2009 Vitaly Lipatov <lav@altlinux.ru> 2.25.4-alt1
- new version 2.25.4 (with rpmrb script)

* Mon Jan 05 2009 Vitaly Lipatov <lav@altlinux.ru> 2.25.2-alt3
- really pack dvi backend module into evince-dvi, not djvu (fix bug #18444)

* Thu Dec 18 2008 Vitaly Lipatov <lav@altlinux.ru> 2.25.2-alt2
- review spec and merge with some Yury Sedunov's changes from his NMU
- build with libspectre
- split dvi support in evince-dvi subpackage
- remove devel stuffs as unneeded

* Tue Dec 16 2008 Vitaly Lipatov <lav@altlinux.ru> 2.25.2-alt1
- new version 2.25.2 (with rpmrb script)
- disable dvi support (due big tetex-core requires)
- pack missed libdirs
- drop obsoleted post/postun macros

* Mon Nov 24 2008 Yuri N. Sedunov <aris@altlinux.org> 2.24.2-alt1
- 2.24.2
- removed obsolete %%post* scripts

* Tue Oct 21 2008 Yuri N. Sedunov <aris@altlinux.org> 2.24.1-alt1
- 2.24.1

* Wed Oct 01 2008 Yuri N. Sedunov <aris@altlinux.org> 2.24.0-alt1
- 2.24.0
- ps support via libspectre
- devel subpackage
- doc-devel subpackage(noarch)

* Sun Jun 15 2008 Vitaly Lipatov <lav@altlinux.ru> 2.22.2-alt1
- new version 2.22.2 (with rpmrb script)

* Thu May 01 2008 Vitaly Lipatov <lav@altlinux.ru> 2.22.1.1-alt2
- rebuild with libpoppler 0.8

* Thu Apr 10 2008 Vitaly Lipatov <lav@altlinux.ru> 2.22.1.1-alt1
- new version 2.22.1.1 (with rpmrb script)

* Thu Dec 27 2007 Vitaly Lipatov <lav@altlinux.ru> 2.21.1-alt1
- new version 2.21.1 (with rpmrb script)

* Tue Nov 27 2007 Vitaly Lipatov <lav@altlinux.ru> 2.20.2-alt1
- new version 2.20.2 (with rpmrb script)
- fix gconf2_ macros using (fix bug #13419)

* Wed Nov 14 2007 Vitaly Lipatov <lav@altlinux.ru> 2.20.1-alt4
- add GConf requires (fix bug #13419)

* Sat Nov 10 2007 Vitaly Lipatov <lav@altlinux.ru> 2.20.1-alt3
- add Provides: bindir/name
- remove NoDisplay from desktop file (fix bug #13369)
- return dvi support
- update buildreqs

* Mon Nov 05 2007 Vitaly Lipatov <lav@altlinux.ru> 2.20.1-alt2
- enable nautilus extension
- add gconf files

* Sun Oct 28 2007 Vitaly Lipatov <lav@altlinux.ru> 2.20.1-alt1
- new version 2.20.1 (with rpmrb script)
- update buildreq

* Wed Sep 26 2007 Vitaly Lipatov <lav@altlinux.ru> 2.20.0-alt1
- new version 2.20.0 (with rpmrb script)

* Wed Sep 05 2007 Vitaly Lipatov <lav@altlinux.ru> 2.19.92-alt1
- new version 2.19.92 (with rpmrb script)
- build with libpoppler 0.6

* Tue Jul 31 2007 Vitaly Lipatov <lav@altlinux.ru> 0.9.3-alt1
- new version 0.9.3 (with rpmrb script)

* Fri Jul 20 2007 Vitaly Lipatov <lav@altlinux.ru> 0.9.2-alt2
- reverted changes for build with libpoppler 0.5.4

* Thu Jul 12 2007 Vitaly Lipatov <lav@altlinux.ru> 0.9.2-alt1
- new version 0.9.2 (with rpmrb script)
- add ghostscript build requires
- still wait for libpoppler >= 0.5.9

* Wed Jun 20 2007 Vitaly Lipatov <lav@altlinux.ru> 0.9.1-alt1
- new version 0.9.1 (with rpmrb script)

* Sat Jun 09 2007 Vitaly Lipatov <lav@altlinux.ru> 0.9.0-alt1
- new version 0.9.0 (with rpmrb script)
- update buildreqs, fix comics build

* Sun Apr 29 2007 Vitaly Lipatov <lav@altlinux.ru> 0.8.1-alt1
- new version 0.8.1 (with rpmrb script)

* Wed Mar 14 2007 Vitaly Lipatov <lav@altlinux.ru> 0.8.0-alt1
- new version 0.8.0 (with rpmrb script)
- bzip ChangeLog (fix bug #11077), thanks icesik@

* Fri Feb 16 2007 Vitaly Lipatov <lav@altlinux.ru> 0.7.2-alt1
- new version 0.7.2 (with rpmrb script)

* Tue Dec 26 2006 Vitaly Lipatov <lav@altlinux.ru> 0.7.0-alt0.1
- new version 0.7.0 (with rpmrb script)

* Fri Oct 13 2006 Vitaly Lipatov <lav@altlinux.ru> 0.6.1-alt0.1
- new version 0.6.1 (with rpmrb script)

* Sun Sep 10 2006 Vitaly Lipatov <lav@altlinux.ru> 0.6.0-alt0.1
- new version (0.6.0), add icons
- remove debian menu, update buildreqs

* Thu Jul 20 2006 Vitaly Lipatov <lav@altlinux.ru> 0.5.4-alt0.1
- new version 0.5.4 (with rpmrb script)

* Sun May 21 2006 Vitaly Lipatov <lav@altlinux.ru> 0.5.2-alt0.1
- enable comics support
- fix build with new libpoppler

* Mon Mar 27 2006 Vitaly Lipatov <lav@altlinux.ru> 0.5.2-alt0.1
- new version (0.5.2)
- update buildreq, use make_build

* Mon Feb 13 2006 Vitaly Lipatov <lav@altlinux.ru> 0.4.0-alt1
- new version

* Sat Sep 10 2005 Vitaly Lipatov <lav@altlinux.ru> 0.4.0-alt0.1
- new version, build with libpoppler 0.4.2, djvu, t1lib
- build with new gnome-doc-utils

* Sun Jul 31 2005 Vitaly Lipatov <lav@altlinux.ru> 0.3.2-alt0.1
- first build for ALT Linux Sisyphus
