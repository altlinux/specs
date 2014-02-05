%define ver_major 3.12

Name: gnome-logs
Version: %ver_major.0
Release: alt1

Summary: The GNOME logfile viewer
Group: Graphical desktop/GNOME
License: GPLv3
Url: https://wiki.gnome.org/Apps/Logs

Source: %gnome_ftp/%name/%ver_major/%name-%version.tar.xz

#Obsoletes: gnome-system-log < 3.11
#Provides: gnome-system-log = %version-%release

Requires: gsettings-desktop-schemas

%define glib_ver 2.31.0
%define gtk_ver 3.9.11

BuildPreReq: rpm-build-gnome gnome-common libgio-devel >= %glib_ver libgtk+3-devel >= %gtk_ver
BuildRequires: gsettings-desktop-schemas-devel libsystemd-journal-devel
BuildRequires: intltool docbook-dtds docbook-style-xsl xsltproc appdata-tools
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
%_desktopdir/%name.desktop
%_iconsdir/hicolor/*x*/apps/%name.png
%_man1dir/%name.1.*
%_datadir/appdata/%name.appdata.xml
%doc NEWS README

%changelog
* Tue Mar 25 2014 Yuri N. Sedunov <aris@altlinux.org> 3.12.0-alt1
- 3.12.0

* Tue Feb 04 2014 Yuri N. Sedunov <aris@altlinux.org> 3.11.5-alt1
- first build for Sisyphus

