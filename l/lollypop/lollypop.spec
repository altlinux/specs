%def_enable snapshot
%define _libexecdir %_prefix/libexec

%define ver_major 1.4
%define xdg_name org.gnome.Lollypop

%def_enable check

Name: lollypop
Version: %ver_major.40
Release: alt1

Summary: Lollypop music player
License: GPL-3.0
Group: Sound
Url: https://wiki.gnome.org/Apps/Lollypop

%if_disabled snapshot
Source: https://gitlab.gnome.org/World/lollypop/-/archive/v%version/%name-%version.tar.gz
%else
Vcs: https://gitlab.gnome.org/World/lollypop.git
Source: %name-%version.tar
%endif

%define gtk_ver 3.22
%define gi_ver 1.35

Requires: typelib(Gtk) = 3.0 typelib(Handy) = 1 typelib(Soup) = 3.0
Requires: python3(textblob)
Requires: gst-plugins-base1.0
Requires: gst-plugins-good1.0
Requires: yt-dlp
Requires: yelp

%add_python3_req_skip gi.repository.Gio

BuildArch: noarch

BuildRequires(pre): rpm-macros-meson rpm-build-python3 rpm-build-gir
BuildRequires: meson yelp-tools
BuildRequires: pkgconfig(gtk+-3.0) >= %gtk_ver
BuildRequires: pkgconfig(gobject-introspection-1.0) >= %gi_ver
BuildRequires: pkgconfig(libsoup-3.0)
BuildRequires: pkgconfig(pygobject-3.0)
%{?_enable_check:BuildRequires: typelib(Gtk) = 3.0
BuildRequires: python3(PIL) python3(textblob) python3(cairo)
BuildRequires: /usr/bin/appstream-util desktop-file-utils
BuildRequires: /usr/bin/appstreamcli /usr/bin/glib-compile-schemas}

%description
Lollypop is a new GNOME music playing application.

%prep
%setup

%build
%meson
%meson_build

%install
%meson_install
%find_lang --with-gnome --output=%name.lang %name

%check
%__meson_test

%files -f %name.lang
%_bindir/%name
%_libexecdir/%name-sp
%python3_sitelibdir/%name/
%_datadir/%name/
%_desktopdir/%xdg_name.desktop
%_datadir/glib-2.0/schemas/%xdg_name.gschema.xml
%_iconsdir/hicolor/*/*/%{xdg_name}*.*
%_datadir/metainfo/%xdg_name.appdata.xml
%_datadir/gnome-shell/search-providers/%xdg_name.SearchProvider.ini
%_datadir/dbus-1/services/%xdg_name.SearchProvider.service
%_man1dir/%name.1*
%doc README*

%changelog
* Fri Jun 14 2024 Yuri N. Sedunov <aris@altlinux.org> 1.4.40-alt1
- 1.4.40

* Mon Apr 15 2024 Yuri N. Sedunov <aris@altlinux.org> 1.4.39-alt1
- 1.4.39

* Wed Apr 03 2024 Yuri N. Sedunov <aris@altlinux.org> 1.4.38-alt1
- 1.4.38

* Fri Jun 30 2023 Yuri N. Sedunov <aris@altlinux.org> 1.4.37-alt1
- first build for Sisyphus (1.4.36-22-gb2583bd38) (ALT #46720)


