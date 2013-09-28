%define ver_major 3.10

Name: gnome-photos
Version: %ver_major.0
Release: alt1

Summary: Photos - access, organize and share your photos on GNOME
License: %gpl2plus
Group: Graphics
Url: https://live.gnome.org/GnomePhotos

Source: %gnome_ftp/%name/%ver_major/%name-%version.tar.xz

BuildPreReq: rpm-build-gnome rpm-build-licenses

# From configure.ac
BuildRequires: gnome-common intltool yelp-tools desktop-file-utils
BuildPreReq: libgio-devel >= 2.36.0
BuildPreReq: libgtk+3-devel >= 3.9.4
BuildPreReq: libexif-devel >= 0.6.14
BuildRequires: libbabl-devel libgegl-devel libexempi-devel
BuildRequires: liblcms2-devel librsvg-devel
BuildRequires: libgnome-desktop3-devel libgnome-online-accounts-devel tracker-devel
BuildRequires: libgrilo-devel zlib-devel
BuildRequires: gobject-introspection-devel libgtk+3-gir-devel

%description
Photos, like Documents, Music and Videos, is one of the core GNOME
applications meant for find and reminding the user about her content.
The internal architecture Photos is based on Documents -- the document
manager application for GNOME, because they share similar UI/UX
patterns and objectives.


%prep
%setup

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
%_datadir/%name
%_iconsdir/hicolor/*/apps/%name.*
%config %_datadir/glib-2.0/schemas/org.gnome.photos.gschema.xml
%_datadir/appdata/%name.appdata.xml

%doc ARTISTS AUTHORS NEWS README

%changelog
* Mon Sep 23 2013 Yuri N. Sedunov <aris@altlinux.org> 3.10.0-alt1
- 3.10.0

* Tue May 14 2013 Yuri N. Sedunov <aris@altlinux.org> 3.8.2-alt1
- 3.8.2

* Mon Apr 15 2013 Yuri N. Sedunov <aris@altlinux.org> 3.8.0-alt1
- 3.8.0

* Sun Mar 24 2013 Yuri N. Sedunov <aris@altlinux.org> 3.7.3-alt1
- first build for people/gnome

