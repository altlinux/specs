%define _unpackaged_files_terminate_build 1
%define ver_major 3.20
%define xdg_name org.gnome.Screenshot

Name: gnome-screenshot
Version: %ver_major.1
Release: alt1

Summary: The GNOME Screenshot Tool
Group: Graphical desktop/GNOME
License: GPLv2+
Url: https://git.gnome.org/browse/gnome-screenshot

Source: %gnome_ftp/%name/%ver_major/%name-%version.tar.xz

%define glib_ver 2.36

BuildPreReq: libgio-devel >= %glib_ver
BuildRequires: libgtk+3-devel libcanberra-gtk3-devel libX11-devel libXext-devel
BuildRequires: rpm-build-gnome intltool libappstream-glib-devel

%description
GNOME Screenshot Tool makes screenshots from desktop.

%prep
%setup

%build
%configure
%make_build

%install
%makeinstall_std

%find_lang %name

%files -f %name.lang
%_bindir/%name
%_datadir/applications/%xdg_name.desktop
%_datadir/dbus-1/services/%xdg_name.service
%_datadir/GConf/gsettings/%name.convert
%_datadir/glib-2.0/schemas/org.gnome.%name.gschema.xml
%_datadir/appdata/%xdg_name.appdata.xml
%_man1dir/%name.1.*
%doc NEWS

%changelog
* Wed Jun 22 2016 Yuri N. Sedunov <aris@altlinux.org> 3.20.1-alt1
- 3.20.1

* Sat Jun 18 2016 Yuri N. Sedunov <aris@altlinux.org> 3.20.0-alt1
- 3.20.0

* Wed Sep 23 2015 Yuri N. Sedunov <aris@altlinux.org> 3.18.0-alt1
- 3.18.0

* Wed May 13 2015 Yuri N. Sedunov <aris@altlinux.org> 3.16.2-alt1
- 3.16.2

* Wed Mar 25 2015 Yuri N. Sedunov <aris@altlinux.org> 3.16.0-alt1
- 3.16.0

* Tue Sep 23 2014 Yuri N. Sedunov <aris@altlinux.org> 3.14.0-alt1
- 3.14.0

* Tue Mar 25 2014 Yuri N. Sedunov <aris@altlinux.org> 3.12.0-alt1
- 3.12.0

* Tue Nov 19 2013 Yuri N. Sedunov <aris@altlinux.org> 3.10.1-alt1
- 3.10.1

* Tue Sep 24 2013 Yuri N. Sedunov <aris@altlinux.org> 3.10.0-alt1
- 3.10.0

* Wed Jul 10 2013 Yuri N. Sedunov <aris@altlinux.org> 3.8.3-alt1
- 3.8.3

* Tue May 14 2013 Yuri N. Sedunov <aris@altlinux.org> 3.8.2-alt1
- 3.8.2

* Tue Apr 16 2013 Yuri N. Sedunov <aris@altlinux.org> 3.8.1-alt1
- 3.8.1

* Mon Mar 25 2013 Yuri N. Sedunov <aris@altlinux.org> 3.8.0-alt1
- 3.8.0

* Tue Nov 13 2012 Yuri N. Sedunov <aris@altlinux.org> 3.6.1-alt1
- 3.6.1

* Mon Sep 24 2012 Yuri N. Sedunov <aris@altlinux.org> 3.6.0-alt1
- 3.6.0

* Tue Apr 17 2012 Yuri N. Sedunov <aris@altlinux.org> 3.4.1-alt1
- 3.4.1

* Tue Mar 27 2012 Yuri N. Sedunov <aris@altlinux.org> 3.4.0-alt1
- 3.4.0

* Mon Mar 19 2012 Yuri N. Sedunov <aris@altlinux.org> 3.3.92-alt1
- 3.3.92

* Mon Feb 06 2012 Yuri N. Sedunov <aris@altlinux.org> 3.3.2-alt1
- first build for Sisyphus

