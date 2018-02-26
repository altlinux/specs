%define ver_major 2.30

Name: swfdec-gnome
Version: %ver_major.1
Release: alt1
Summary: Programs to integrate Flash into the GNOME desktop

Group: Graphical desktop/GNOME
License: GPLv3
Url: http://swfdec.freedesktop.org/
Source: ftp://ftp.gnome.org/pub/gnome/sources/%name/%ver_major/%name-%version.tar.bz2

Requires(post,preun): GConf

BuildPreReq: GConf libGConf-devel
BuildPreReq: intltool >= 0.35.0
BuildPreReq: libgtk+2-devel >= 2.12.0
BuildPreReq: libswfdec-devel >= 0.8.0
BuildPreReq: desktop-file-utils

%description
This package contains programs to integrate Flash functionality into the GNOME
desktop. It's main application is swfdec-player, a stand-alone viewer for
Flash files. It also contains swfdec-thumbnailer, a program that provides
screenshots for files to display in the Nautilus file manager

%prep
%setup -q

%build
%configure \
    --disable-schemas-install

%make_build

%install
%make DESTDIR=%buildroot install

%find_lang --with-gnome %name

%post
%gconf2_install swfdec-thumbnailer

%preun
if [ "$1" -eq 0 ]; then
%gconf2_uninstall swfdec-thumbnailer
fi

%files -f %name.lang
%_bindir/swfdec-player
%_bindir/swfdec-thumbnailer
%_datadir/applications/*
%_datadir/%name/
%_datadir/icons/hicolor/*/apps/%name.png
%_datadir/icons/hicolor/scalable/apps/%name.svg
%_sysconfdir/gconf/schemas/swfdec-thumbnailer.schemas
%_man1dir/*
%doc AUTHORS ChangeLog NEWS README

%changelog
* Tue Oct 19 2010 Yuri N. Sedunov <aris@altlinux.org> 2.30.1-alt1
- 2.30.1

* Tue Mar 30 2010 Yuri N. Sedunov <aris@altlinux.org> 2.30.0-alt1
- 2.30.0

* Tue Sep 22 2009 Yuri N. Sedunov <aris@altlinux.org> 2.28.0-alt1
- 2.28.0

* Mon Apr 13 2009 Yuri N. Sedunov <aris@altlinux.org> 2.26.0-alt1
- 2.26.0

* Fri Oct 03 2008 Yuri N. Sedunov <aris@altlinux.org> 2.24.0-alt1
- first build for Sisyphus
