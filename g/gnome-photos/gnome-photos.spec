%define _unpackaged_files_terminate_build 1
%define xdg_name org.gnome.Photos
%define ver_major 3.22
%define _libexecdir %_prefix/libexec
%define gegl_api_ver 0.3

Name: gnome-photos
Version: %ver_major.2
Release: alt1

Summary: Photos - access, organize and share your photos on GNOME
License: %gpl2plus
Group: Graphics
Url: https://wiki.gnome.org/Apps/Photos

Source: %gnome_ftp/%name/%ver_major/%name-%version.tar.xz

%define glib_ver 2.44
%define gtk_ver 3.20.0
%define tracker_ver 0.18
%define gdata_ver 0.15.2
%define gegl_ver 0.3.5
%define grilo_ver 0.3
%define png_ver 1.5

Requires: grilo-plugins >= %grilo_ver

BuildPreReq: rpm-build-gnome rpm-build-licenses
# From configure.ac
BuildRequires: gnome-common intltool yelp-tools desktop-file-utils
BuildPreReq: libgio-devel >= %glib_ver
BuildPreReq: libgtk+3-devel >= %gtk_ver
BuildPreReq: tracker-devel >= %tracker_ver
BuildPreReq: libgdata-devel >= %gdata_ver
BuildPreReq: libgegl%gegl_api_ver-devel >= %gegl_ver
BuildPreReq: libgrilo-devel >= %grilo_ver
BuildPreReq: libpng-devel >= %png_ver
BuildRequires: libgexiv2-devel libexempi-devel liblcms2-devel librsvg-devel
BuildRequires: libjpeg-devel libgfbgraph-devel
BuildRequires: libgnome-desktop3-devel libgnome-online-accounts-devel zlib-devel
BuildRequires: gobject-introspection-devel libgtk+3-gir-devel

%description
Photos, like Documents, Music and Videos, is one of the core GNOME
applications meant for find and reminding the user about her content.
The internal architecture Photos is based on Documents -- the document
manager application for GNOME, because they share similar UI/UX
patterns and objectives.

%prep
%setup
# downgrade required libpng
subst 's|libpng16|libpng15|' configure.ac

%build
%autoreconf
%configure \
    --disable-schemas-compile

%make_build

%install
%makeinstall_std
rm -rf %buildroot/%_datadir/doc/%name
%find_lang --with-gnome %name

%files -f %name.lang
%_bindir/%name
%_desktopdir/%xdg_name.desktop
%_iconsdir/hicolor/*/apps/%xdg_name.*
%_iconsdir/hicolor/scalable/apps/%xdg_name-symbolic.svg
%_datadir/appdata/%xdg_name.appdata.xml
%_datadir/gnome-shell/search-providers/%xdg_name.search-provider.ini
%_datadir/dbus-1/services/%xdg_name.service
%config %_datadir/glib-2.0/schemas/org.gnome.photos.gschema.xml
%doc ARTISTS AUTHORS NEWS README

%changelog
* Sat Nov 05 2016 Yuri N. Sedunov <aris@altlinux.org> 3.22.2-alt1
- 3.22.2

* Thu Oct 06 2016 Yuri N. Sedunov <aris@altlinux.org> 3.22.1-alt1
- 3.22.1

* Sat Sep 17 2016 Yuri N. Sedunov <aris@altlinux.org> 3.22.0-alt1
- 3.22.0

* Tue Aug 09 2016 Yuri N. Sedunov <aris@altlinux.org> 3.20.3-alt1
- 3.20.3

* Tue Jun 21 2016 Yuri N. Sedunov <aris@altlinux.org> 3.20.2-alt1
- 3.20.2

* Wed Apr 13 2016 Yuri N. Sedunov <aris@altlinux.org> 3.20.1-alt1
- 3.20.1

* Mon Mar 21 2016 Yuri N. Sedunov <aris@altlinux.org> 3.20.0-alt1
- 3.20.0

* Tue Mar 15 2016 Yuri N. Sedunov <aris@altlinux.org> 3.18.3-alt1
- 3.18.3 (CVE-2013-7447)

* Sun Nov 08 2015 Yuri N. Sedunov <aris@altlinux.org> 3.18.2-alt1
- 3.18.2

* Mon Oct 12 2015 Yuri N. Sedunov <aris@altlinux.org> 3.18.1-alt1
- 3.18.1

* Tue Sep 22 2015 Yuri N. Sedunov <aris@altlinux.org> 3.18.0-alt1
- 3.18.0

* Mon Sep 07 2015 Yuri N. Sedunov <aris@altlinux.org> 3.16.2-alt3
- rebuilt against libgrilo-0.2.so.10

* Sun Aug 09 2015 Yuri N. Sedunov <aris@altlinux.org> 3.16.2-alt2
- rebuilt against libgdata.so.22

* Wed May 13 2015 Yuri N. Sedunov <aris@altlinux.org> 3.16.2-alt1
- 3.16.2

* Wed Mar 25 2015 Yuri N. Sedunov <aris@altlinux.org> 3.16.0-alt1
- 3.16.0

* Mon Nov 10 2014 Yuri N. Sedunov <aris@altlinux.org> 3.14.2-alt1
- 3.14.2

* Wed Sep 24 2014 Yuri N. Sedunov <aris@altlinux.org> 3.14.0-alt1
- 3.14.0

* Tue Apr 15 2014 Yuri N. Sedunov <aris@altlinux.org> 3.12.1-alt1
- 3.12.1

* Mon Mar 24 2014 Yuri N. Sedunov <aris@altlinux.org> 3.12.0-alt1
- 3.12.0

* Mon Mar 17 2014 Yuri N. Sedunov <aris@altlinux.org> 3.11.92-alt1
- 3.11.92

* Wed Nov 13 2013 Yuri N. Sedunov <aris@altlinux.org> 3.10.2-alt1
- 3.10.2

* Mon Oct 14 2013 Yuri N. Sedunov <aris@altlinux.org> 3.10.1-alt1
- 3.10.1

* Mon Sep 23 2013 Yuri N. Sedunov <aris@altlinux.org> 3.10.0-alt1
- 3.10.0

* Tue May 14 2013 Yuri N. Sedunov <aris@altlinux.org> 3.8.2-alt1
- 3.8.2

* Mon Apr 15 2013 Yuri N. Sedunov <aris@altlinux.org> 3.8.0-alt1
- 3.8.0

* Sun Mar 24 2013 Yuri N. Sedunov <aris@altlinux.org> 3.7.3-alt1
- first build for people/gnome

