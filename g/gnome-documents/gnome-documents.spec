%define ver_major 0.4
%define api_ver 1.0
%define _libexecdir %_prefix/libexec

Name: gnome-documents
Version: %ver_major.2
Release: alt1

Summary: A document manager application for GNOME
Group: Office
License: GPLv2+
Url: https://live.gnome.org/Design/Apps/Documents

Source: ftp://ftp.gnome.org/pub/gnome/sources/%name/%ver_major/%name-%version.tar.xz
#Patch: %name-0.3.92-alt-gir.patch

%define glib_ver 2.31.6
%define gtk_ver 3.3.6
%define evince_ver 3.3.0
%define tracker_ver 0.13.1
%define goa_ver 3.2.0
%define gdata_ver 0.11

BuildRequires: intltool
BuildRequires: libgio-devel >= %glib_ver libgtk+3-devel >= %gtk_ver
BuildRequires: libclutter-gtk3-devel libgnome-desktop3-devel libgdata-devel >= %gdata_ver
BuildRequires: liboauth-devel libgnome-online-accounts-devel >= %goa_ver
BuildRequires: tracker-devel >= %tracker_ver libevince-devel >= %evince_ver
BuildRequires: libgtk+3-gir-devel libgjs-devel libevince-gir-devel libgdata-gir-devel libgnome-online-accounts-gir-devel

%description
gnome-documents is a document manager application for GNOME,
aiming to be a simple and elegant replacement for using Files to show
the Documents directory.

%package devel
Summary: Development files for %name
Group: Development/C
Requires: %name = %version-%release

%description devel
The %name-devel package contains libraries and header files for
developing applications that use %name.

%package gir
Summary: GObject introspection data for %name
Group: System/Libraries
Requires: %name = %version-%release

%description gir
GObject introspection data for the %name library.

%package gir-devel
Summary: GObject introspection devel data for %name
Group: Development/Other
BuildArch: noarch
Requires: %name-gir = %version-%release

%description gir-devel
GObject introspection devel data for the %name library.

%define pkglibdir %_libdir/%name
%define pkgdatadir %_datadir/%name

%prep
%setup
#%%patch -p1

%build
%autoreconf
%configure --disable-static
%make_build

%install
make DESTDIR=%buildroot install
%find_lang %name

mkdir -p %buildroot{%_typelibdir,%_girdir}
ln -s ../%name/girepository-1.0/Gd-%api_ver.typelib %buildroot%_typelibdir/Gd-%api_ver.typelib
ln -s ../%name/gir-1.0/Gd-%api_ver.gir %buildroot%_girdir/Gd-%api_ver.gir

%files -f %name.lang
%_bindir/%name
%dir %pkglibdir
%pkglibdir/*.so
%exclude %pkglibdir/*.la
%_libexecdir/gd-tracker-gdata-miner
%_libexecdir/gnome-documents-search-provider
%pkgdatadir/
%exclude %pkgdatadir/gir-1.0
%_datadir/dbus-1/services/org.gnome.Documents.GDataMiner.service
%_datadir/dbus-1/services/org.gnome.Documents.SearchProvider.service
%_datadir/glib-2.0/schemas/org.gnome.Documents.enums.xml
%_datadir/glib-2.0/schemas/org.gnome.documents.gschema.xml
%_datadir/gnome-shell/search-providers/gnome-documents-search-provider.ini
%_datadir/applications/%name.desktop
%_iconsdir/hicolor/*/apps/%name.png
%doc README AUTHORS NEWS TODO

#%files gir
%dir %pkglibdir/girepository-1.0
%pkglibdir/girepository-1.0/Gd-%api_ver.typelib
%_typelibdir/Gd-%api_ver.typelib

#%files gir-devel
%exclude %pkgdatadir/gir-1.0
%exclude %pkgdatadir/gir-1.0/Gd-%api_ver.gir
%exclude %_girdir/Gd-%api_ver.gir

%changelog
* Tue May 15 2012 Yuri N. Sedunov <aris@altlinux.org> 0.4.2-alt1
- 0.4.2

* Tue Apr 17 2012 Yuri N. Sedunov <aris@altlinux.org> 0.4.1-alt1
- 0.4.1

* Mon Mar 26 2012 Yuri N. Sedunov <aris@altlinux.org> 0.4.0.1-alt1
- 0.4.0.1

* Mon Nov 07 2011 Yuri N. Sedunov <aris@altlinux.org> 0.2.1-alt1
- first build for Sisyphus

