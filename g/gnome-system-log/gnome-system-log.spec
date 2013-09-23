%define ver_major 3.9

Name: gnome-system-log
Version: %ver_major.90
Release: alt1

Summary: The GNOME logfile viewer
Group: Graphical desktop/GNOME
License: GPLv2+
Url: http://www.gnome.org

Source: %gnome_ftp/%name/%ver_major/%name-%version.tar.xz

%define glib_ver 2.31.0
%define gtk_ver 3.9.11

BuildPreReq: libgio-devel >= %glib_ver libgtk+3-devel >= %gtk_ver
BuildRequires: zlib-devel intltool yelp-tools itstool rpm-build-gnome

%description
System Log Viewer - monitor and view system log files.

%prep
%setup

%build
%configure \
	--disable-schemas-compile \
	--enable-zlib

%make_build

%install
%makeinstall_std

%find_lang --with-gnome %name

%files -f %name.lang
%_bindir/%name
%_desktopdir/%name.desktop
%_iconsdir/hicolor/*x*/apps/logview.png
%_iconsdir/HighContrast/*x*/apps/logview.png
%_man1dir/%name.1.*
%config  %_datadir/glib-2.0/schemas/org.gnome.%name.gschema.xml
%_datadir/GConf/gsettings/logview.convert
%doc NEWS

%changelog
* Thu Aug 29 2013 Yuri N. Sedunov <aris@altlinux.org> 3.9.90-alt1
- 3.9.90

* Tue Apr 16 2013 Yuri N. Sedunov <aris@altlinux.org> 3.8.1-alt1
- 3.8.1

* Mon Mar 25 2013 Yuri N. Sedunov <aris@altlinux.org> 3.8.0-alt1
- 3.8.0

* Wed Feb 27 2013 Yuri N. Sedunov <aris@altlinux.org> 3.7.90-alt1
- 3.7.90

* Tue Nov 13 2012 Yuri N. Sedunov <aris@altlinux.org> 3.6.1-alt1
- 3.6.1

* Mon Sep 24 2012 Yuri N. Sedunov <aris@altlinux.org> 3.6.0-alt1
- 3.6.0

* Tue Apr 17 2012 Yuri N. Sedunov <aris@altlinux.org> 3.4.1-alt1
- 3.4.1

* Mon Mar 26 2012 Yuri N. Sedunov <aris@altlinux.org> 3.4.0-alt1
- 3.4.0

* Mon Mar 19 2012 Yuri N. Sedunov <aris@altlinux.org> 3.3.92-alt1
- 3.3.92

