%def_enable check

%define _name app.drey.Damask

Name: damask
Version: 0.2.2
Release: alt2.ff908293

Summary:  Automatically set wallpaper images from a variety of sources
License: GPL-3.0-or-later
Group: Graphical desktop/GNOME

Url: https://gitlab.gnome.org/subpop/damask
Vcs: https://gitlab.gnome.org/subpop/damask

Source: %name-%version.tar

BuildRequires(pre): rpm-macros-meson rpm-build-cmake
BuildRequires: meson blueprint-compiler libgee0.8-devel libportal-devel libportal-gtk4-devel
BuildRequires: pkgconfig(json-glib-1.0)
BuildRequires: pkgconfig(gtk4) >= 4.0
BuildRequires: pkgconfig(libadwaita-1) >= 1.2 typelib(Adw) = 1

%{?_enable_check:BuildRequires: /usr/bin/appstreamcli desktop-file-utils /usr/bin/glib-compile-schemas}

%description
Damask is an application that will automatically set wallpaper images by
selecting images from a variety of sources, including local files and folders.
It currently supports setting the wallpaper image from the following sources:
- wallhaven.cc
- Microsoft Bing Wallpaper of the day
- NASA Astronomy Picture of the Day
- Unsplash

%prep
%setup

%build
%meson
%meson_build

%install
%meson_install
%find_lang --with-gnome %name

%check
%meson_test

%files -f %name.lang
%_bindir/%name
%_datadir/applications/%_name.desktop
%_datadir/glib-2.0/schemas/%_name.gschema.xml
%_iconsdir/hicolor/*/apps/%{_name}*.svg
#%_datadir/locale/*/LC_MESSAGES/%name.mo
%_datadir/metainfo/%_name.metainfo.xml
%doc README*

%changelog
* Sat Nov 30 2024 Aleksandr Shamaraev <shad@altlinux.org> 0.2.2-alt2.ff908293
- Fixed app.drey.Damask.desktop by Repocop comment.
- Rename macro %%__meson_test -> %%meson_test

* Thu Nov 21 2024 Aleksandr Shamaraev <shad@altlinux.org> 0.2.2-alt1
- Initial build for Sisyphus.
