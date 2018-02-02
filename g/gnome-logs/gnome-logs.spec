%define _unpackaged_files_terminate_build 1
%define ver_major 3.26
%define _name org.gnome.Logs

Name: gnome-logs
Version: %ver_major.3
Release: alt1

Summary: The GNOME logfile viewer
Group: Graphical desktop/GNOME
License: GPLv3
Url: https://wiki.gnome.org/Apps/Logs

Source: %gnome_ftp/%name/%ver_major/%name-%version.tar.xz

#Obsoletes: gnome-system-log < 3.11
#Provides: gnome-system-log = %version-%release

Requires: gsettings-desktop-schemas

%define glib_ver 2.44
%define gtk_ver 3.22

BuildPreReq: rpm-build-gnome gnome-common libgio-devel >= %glib_ver libgtk+3-devel >= %gtk_ver
BuildRequires: gsettings-desktop-schemas-devel libsystemd-journal-devel
BuildRequires: intltool docbook-dtds docbook-style-xsl xsltproc desktop-file-utils
BuildRequires: appdata-tools libappstream-glib-devel
BuildRequires: yelp-tools

%description
GNOME Logs is a log viewer for the systemd journal.

%prep
%setup

%build
%autoreconf
%configure

%make_build

%install
%makeinstall_std

%find_lang --with-gnome %name

%files -f %name.lang
%_bindir/%name
%_desktopdir/%_name.desktop
%_datadir/dbus-1/services/%_name.service
%_datadir/glib-2.0/schemas/%_name.enums.xml
%_datadir/glib-2.0/schemas/%_name.gschema.xml
%_iconsdir/hicolor/*x*/apps/%name.png
%_iconsdir/hicolor/symbolic/apps/%name-symbolic.svg
%_man1dir/%name.1.*
%_datadir/metainfo/%_name.appdata.xml
%doc NEWS README

%changelog
* Fri Feb 02 2018 Yuri N. Sedunov <aris@altlinux.org> 3.26.3-alt1
- 3.26.3

* Mon Oct 30 2017 Yuri N. Sedunov <aris@altlinux.org> 3.26.2-alt1
- 3.26.2

* Mon Sep 11 2017 Yuri N. Sedunov <aris@altlinux.org> 3.26.0-alt1
- 3.26.0

* Sat Jul 29 2017 Yuri N. Sedunov <aris@altlinux.org> 3.24.2-alt1
- 3.24.2

* Mon Apr 10 2017 Yuri N. Sedunov <aris@altlinux.org> 3.24.1-alt1
- 3.24.1

* Tue Mar 21 2017 Yuri N. Sedunov <aris@altlinux.org> 3.24.0-alt1
- 3.24.0

* Mon Oct 10 2016 Yuri N. Sedunov <aris@altlinux.org> 3.22.1-alt1
- 3.22.1

* Tue Sep 20 2016 Yuri N. Sedunov <aris@altlinux.org> 3.22.0-alt1
- 3.22.0

* Mon Apr 11 2016 Yuri N. Sedunov <aris@altlinux.org> 3.20.1-alt1
- 3.20.1

* Tue Mar 22 2016 Yuri N. Sedunov <aris@altlinux.org> 3.20.0-alt1
- 3.20.0

* Mon Oct 12 2015 Yuri N. Sedunov <aris@altlinux.org> 3.18.1-alt1
- 3.18.1

* Tue Sep 22 2015 Yuri N. Sedunov <aris@altlinux.org> 3.18.0-alt1
- 3.18.0

* Mon May 11 2015 Yuri N. Sedunov <aris@altlinux.org> 3.16.2-alt1
- 3.16.2

* Tue Apr 14 2015 Yuri N. Sedunov <aris@altlinux.org> 3.16.1-alt1
- 3.16.1

* Wed Mar 25 2015 Yuri N. Sedunov <aris@altlinux.org> 3.16.0-alt1
- 3.16.0

* Tue Nov 11 2014 Yuri N. Sedunov <aris@altlinux.org> 3.14.2-alt1
- 3.14.2

* Tue Oct 14 2014 Yuri N. Sedunov <aris@altlinux.org> 3.14.1-alt1
- 3.14.1

* Tue Sep 23 2014 Yuri N. Sedunov <aris@altlinux.org> 3.14.0-alt1
- 3.14.0

* Tue May 13 2014 Yuri N. Sedunov <aris@altlinux.org> 3.12.2-alt1
- 3.12.2

* Mon Apr 14 2014 Yuri N. Sedunov <aris@altlinux.org> 3.12.1-alt1
- 3.12.1

* Tue Mar 25 2014 Yuri N. Sedunov <aris@altlinux.org> 3.12.0-alt1
- 3.12.0

* Tue Feb 04 2014 Yuri N. Sedunov <aris@altlinux.org> 3.11.5-alt1
- first build for Sisyphus

