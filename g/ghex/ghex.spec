%define ver_major 3.4
%define api_ver 3.0

Name: ghex
Version: %ver_major.1
Release: alt1

Summary: Binary editor for GNOME
Group: Development/Tools
License: GPLv2+
Url: http://live.gnome.org/Ghex

Source: ftp://ftp.gnome.org/pub/gnome/sources/%name/%ver_major/%name-%version.tar.xz

%define glib_ver 2.31.10
%define gtk_ver 3.3.8

BuildRequires: glib2-devel >= %glib_ver libgtk+3-devel >= %gtk_ver
BuildRequires: libgail3-devel gnome-doc-utils intltool librarian

%description
GHex is a hex editor for the GNOME desktop.

GHex can load raw data from binary files and display them for editing in
the traditional hex editor view. The display is split in two columns,
with hexadecimal values in one column and the ASCII representation in
the other. A useful tool for working with raw data.

%package devel
Summary: Development files for GtkHex
Group: Development/C
Requires: %name = %version-%release

%description devel
The %name-devel package contains libraries and header files for
developing applications that use GtkGHex library.

%prep
%setup

%build
%configure --disable-scrollkeeper \
	--disable-schemas-compile

%make_build

%install
make DESTDIR=%buildroot install

%find_lang --with-gnome --output=%name.lang %name %name-%api_ver

%files -f %name.lang
%_bindir/*
%_datadir/applications/%name.desktop
%_datadir/GConf/gsettings/%name.convert
%_datadir/glib-2.0/schemas/org.gnome.GHex.gschema.xml
%_iconsdir/hicolor/*/apps/*
%_libdir/*.so.*
%doc AUTHORS NEWS README

%files devel
%_includedir/*
%_libdir/*.so
%_libdir/pkgconfig/*.pc

%changelog
* Mon May 14 2012 Yuri N. Sedunov <aris@altlinux.org> 3.4.1-alt1
- 3.4.1

* Tue Mar 27 2012 Yuri N. Sedunov <aris@altlinux.org> 3.4.0-alt1
- 3.4.0

* Mon Mar 05 2012 Yuri N. Sedunov <aris@altlinux.org> 3.3.91-alt1
- 3.3.91

* Mon Nov 21 2011 Yuri N. Sedunov <aris@altlinux.org> 3.0.0-alt1
- first build for Sisyphus

