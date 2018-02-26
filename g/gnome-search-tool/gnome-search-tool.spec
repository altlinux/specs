%define ver_major 3.4

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

Requires(post,preun): GConf

BuildPreReq: libgio-devel >= %glib_ver libgtk+3-devel >= %gtk_ver
BuildRequires: libSM-devel GConf libGConf-devel
BuildRequires: intltool gnome-doc-utils rpm-build-gnome

%description
Search Tool - search for files on your system using simple and advanced
search options.

%prep
%setup

%build
%configure \
	--disable-schemas-install

%make_build

%install
%makeinstall_std

%find_lang --with-gnome %name

%post
%gconf2_install gnome-search-tool

%preun
if [ $1 = 0 ]; then
%gconf2_uninstall gnome-search-tool
fi

%files -f %name.lang
%_bindir/gnome-search-tool
%_desktopdir/gnome-search-tool.desktop
%dir %_datadir/pixmaps/gsearchtool
%_datadir/pixmaps/gsearchtool/*
%_man1dir/gnome-search-tool.1.*
%config %gconf_schemasdir/gnome-search-tool.schemas
%doc NEWS

%changelog
* Tue Mar 27 2012 Yuri N. Sedunov <aris@altlinux.org> 3.4.0-alt1
- 3.4.0

* Sat Mar 10 2012 Yuri N. Sedunov <aris@altlinux.org> 3.3.1-alt1
- 3.3.1

