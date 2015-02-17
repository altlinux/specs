%define _unpackaged_files_terminate_build 1
%define ver_major 3.14
%define _name org.gnome.font-viewer

Name: gnome-font-viewer
Version: %ver_major.1
Release: alt1

Summary: The GNOME Font Viewer
Group: Graphical desktop/GNOME
License: GPLv2+
Url: http://www.gnome.org

Source: %gnome_ftp/%name/%ver_major/%name-%version.tar.xz

%define glib_ver 2.38.0
%define gtk_ver 3.12.0

BuildPreReq: libgio-devel >= %glib_ver libgtk+3-devel >= %gtk_ver
BuildRequires: libfreetype-devel libharfbuzz-devel libgnome-desktop3-devel
BuildRequires: intltool rpm-build-gnome

%description
GNOME Font Viewer is a simple application to preview fonts.

%prep
%setup

%build
%configure \
	--disable-schemas-compile

%make_build

%install
%makeinstall_std

%find_lang --with-gnome %name

%files -f %name.lang
%_bindir/%name
%_bindir/gnome-thumbnail-font
%_datadir/applications/%_name.desktop
%_datadir/thumbnailers/%name.thumbnailer
%_datadir/dbus-1/services/%_name.service
%_datadir/appdata/%_name.appdata.xml
%doc NEWS

%changelog
* Wed Feb 18 2015 Yuri N. Sedunov <aris@altlinux.org> 3.14.1-alt1
- 3.14.1

* Tue Sep 23 2014 Yuri N. Sedunov <aris@altlinux.org> 3.14.0-alt1
- 3.14.0

* Wed Mar 26 2014 Yuri N. Sedunov <aris@altlinux.org> 3.12.0-alt1
- 3.12.0

* Tue Sep 24 2013 Yuri N. Sedunov <aris@altlinux.org> 3.10.0-alt1
- 3.10.0

* Mon Mar 25 2013 Yuri N. Sedunov <aris@altlinux.org> 3.8.0-alt1
- 3.8.0

* Thu Dec 06 2012 Yuri N. Sedunov <aris@altlinux.org> 3.6.2-alt1
- 3.6.2

* Tue Nov 13 2012 Yuri N. Sedunov <aris@altlinux.org> 3.6.1-alt1
- 3.6.1

* Mon Sep 24 2012 Yuri N. Sedunov <aris@altlinux.org> 3.6.0-alt1
- 3.6.0

* Mon Mar 26 2012 Yuri N. Sedunov <aris@altlinux.org> 3.4.0-alt1
- 3.4.0

* Mon Mar 19 2012 Yuri N. Sedunov <aris@altlinux.org> 3.3.92-alt1
- 3.3.92

