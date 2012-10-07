%define ver_major 3.6

Name: gnome-search-tool
Version: %ver_major.0
Release: alt1

Summary: The GNOME Search Tool
Group: Graphical desktop/GNOME
License: GPLv2+
Url: http://www.gnome.org

Source: %gnome_ftp/%name/%ver_major/%name-%version.tar.xz

%define glib_ver 2.30.0
%define gtk_ver 3.0.0

BuildPreReq: libgio-devel >= %glib_ver libgtk+3-devel >= %gtk_ver
BuildRequires: libSM-devel intltool yelp-tools itstool rpm-build-gnome

%description
Search Tool - search for files on your system using simple and advanced
search options.

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
%_bindir/gnome-search-tool
%_desktopdir/gnome-search-tool.desktop
%dir %_datadir/pixmaps/gsearchtool
%_datadir/pixmaps/gsearchtool/*
%_man1dir/gnome-search-tool.1.*
%_datadir/GConf/gsettings/gnome-search-tool.convert
%config %_datadir/glib-2.0/schemas/org.gnome.gnome-search-tool.gschema.xml
%doc NEWS

%changelog
* Wed Sep 26 2012 Yuri N. Sedunov <aris@altlinux.org> 3.6.0-alt1
- 3.6.0

* Tue Mar 27 2012 Yuri N. Sedunov <aris@altlinux.org> 3.4.0-alt1
- 3.4.0

* Sat Mar 10 2012 Yuri N. Sedunov <aris@altlinux.org> 3.3.1-alt1
- 3.3.1

