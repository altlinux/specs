%define _name org.yorba.california
%define ver_major 0.3
%define api_ver 1.0

Name: california
Version: %ver_major.1
Release: alt1

Summary: GNOME 3 Calendar
License: %lgpl2plus
Group: Office
Url: https://wiki.gnome.org/Apps/California

#Source: %name-%version.tar
Source: %gnome_ftp/%name/%ver_major/%name-%version.tar.xz

BuildPreReq: rpm-build-gnome rpm-build-licenses

# From configure.ac
%define glib_ver 2.38.0
%define gtk_ver 3.12.2
%define gi_ver 1.38.0
%define gee_ver 0.10.5
%define vala_ver 0.24.0
%define eds_ver 3.8.5
%define soup_ver 2.44
%define gdata_ver 0.14.0
%define goa_ver 3.8.5

BuildPreReq: vala-tools >= %vala_ver
BuildPreReq: libgio-devel >= %glib_ver
BuildPreReq: libgtk+3-devel >= %gtk_ver
BuildPreReq: libgee0.8-devel >= %gee_ver
BuildPreReq: evolution-data-server-devel >= %eds_ver evolution-data-server-vala
BuildPreReq: libsoup-devel >= %soup_ver
BuildPreReq: libgdata-devel >= %gdata_ver
BuildPreReq: libgnome-online-accounts-devel >= %goa_ver
BuildPreReq: gobject-introspection-devel >= %gi_ver
BuildRequires: libgnome-online-accounts-gir-devel
BuildRequires: libical-devel gsettings-desktop-schemas-devel
BuildRequires: rpm-build-gnome rpm-build-licenses
BuildRequires: gnome-common intltool yelp-tools xdg-utils

%description
California is a calendar built for GNOME 3. It allows you to view and
manage your online calendars with a simple and modern interface.

%prep
%setup
[ ! -d m4 ] && mkdir m4

%build
%autoreconf
%configure \
    --disable-schemas-compile
%make_build

%install
%makeinstall_std

%find_lang --with-gnome %name

%files -f %name.lang
%_bindir/*
%_desktopdir/*
%_datadir/%name/
%config %_datadir/glib-2.0/schemas/%_name.gschema.xml
%_datadir/appdata/%name.appdata.xml
%doc AUTHORS NEWS README THANKS

%changelog
* Wed Feb 04 2015 Yuri N. Sedunov <aris@altlinux.org> 0.3.1-alt1
- 0.3.1

* Tue Dec 09 2014 Yuri N. Sedunov <aris@altlinux.org> 0.3.0-alt1
- 0.3.0

* Wed Oct 01 2014 Yuri N. Sedunov <aris@altlinux.org> 0.2.0-alt1
- first build for Sisyphus


