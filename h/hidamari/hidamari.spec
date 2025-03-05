%define _name io.github.jeffshee.Hidamari

Name: hidamari
Version: 3.6
Release: alt1

Summary:  Video wallpaper for Linux. Written in Python.
License: GPL-3.0
Group: Other

Url: https://github.com/jeffshee/hidamari
Vcs: https://github.com/jeffshee/hidamari

BuildArch: noarch

Source0: %name-%version.tar
Source1: shared-modules.tar

%add_python3_path %_datadir/%name/

Requires: vlc ffprobe ffmpeg

BuildRequires(pre): rpm-macros-meson rpm-build-python3
BuildRequires: meson cmake
BuildRequires: pkgconfig(gio-2.0)
BuildRequires: pkgconfig(gtk4) >= 4.6
BuildRequires: pkgconfig(libadwaita-1) >= 1.2 typelib(Adw) = 1
BuildRequires: /usr/bin/appstreamcli /usr/bin/appstream-util desktop-file-utils 
BuildRequires: /usr/bin/glib-compile-schemas gtk4-update-icon-cache gtk-update-icon-cache

%description
%summary

%prep
%setup -a1

subst "s|AppIndicator3|AyatanaAppIndicator3|" src/menu.py

%build
%meson
%meson_build

%install
%meson_install

%files
%_bindir/%name
%_datadir/appdata/%_name.appdata.xml
%_datadir/applications/%_name.desktop
%_datadir/glib-2.0/schemas/%_name.gschema.xml
%_datadir/%name/*
%_iconsdir/hicolor/*/apps/*.svg
%doc *.md COPYING

%changelog
* Wed Mar 05 2025 Aleksandr Shamaraev <shad@altlinux.org> 3.6-alt1
- Initial build for ALT Linux.