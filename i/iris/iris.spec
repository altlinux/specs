%define _unpackaged_files_terminate_build 1
%define app_id space.x1z53.iris

Name: iris
Version: 0.2.4.1
Release: alt1

Summary: GTK client for Yummy Anime
License: GPL-3.0-only
Group: Video

URL: https://altlinux.space/alt-gnome/iris
VCS: https://altlinux.space/alt-gnome/iris
Source0: %name-%version.tar

BuildRequires(pre): rpm-macros-meson
BuildRequires: meson
BuildRequires: blueprint-compiler
BuildRequires: pkgconfig(gtk4)
BuildRequires: pkgconfig(libadwaita-1)
BuildRequires: pkgconfig(json-glib-1.0)
BuildRequires: pkgconfig(libapi-base-7)
BuildRequires: pkgconfig(webkitgtk-6.0)
BuildRequires: pkgconfig(libcase-0)
BuildRequires: gobject-introspection-devel
BuildRequires: gir(Adw) = 1
BuildRequires: typelib(Case) = 0

Requires: libwebp-pixbuf-loader

Provides: yummy-anime-gtk = %EVR
Obsoletes: yummy-anime-gtk < %EVR

%description
%summary.

%prep
%setup

%build
%meson
%meson_build

%install
%meson_install
%find_lang %name

%check
%meson_test

%files -f %name.lang
%_bindir/%name
%_desktopdir/%app_id.desktop
%_iconsdir/hicolor/*/apps/%{app_id}*.svg
%_datadir/metainfo/%app_id.metainfo.xml
%_datadir/glib-2.0/schemas/%app_id.gschema.xml

%changelog
* Tue Jun 09 2026 David Sultaniiazov <x1z53@altlinux.org> 0.2.4.1-alt1
- Update to 0.2.4.1:
  + fixed memory leaks
  + added Dialogs section
  + fixed Viewing order links
  + moved from libcassette to libcase

* Thu May 21 2026 David Sultaniiazov <x1z53@altlinux.org> 0.2.4-alt2
- Fix spec `files` section.

* Tue May 19 2026 David Sultaniiazov <x1z53@altlinux.org> 0.2.4-alt1
- Update to 0.2.4:
  + fixed memory leaks
  + implemented image caching
  + added additional mirrors that change automatically.
  + added display switching between grid and list
  + added score display and the ability to rate titles
  + added a download spinner and a placeholder for images
  + changed the display of the poster to display as a list
  + added an authorization dialog for actions that require it.
  + added the "Recommendations" and "Schedule" sections on the main page
  + changed default window size to 800x600
  + fixed incorrect behavior of elements in comments

* Sun Mar 29 2026 David Sultaniiazov <x1z53@altlinux.org> 0.2.3-alt1
- Update to 0.2.3:
  + add delete button for own comment
  + add reply and edit functions for comments
  + add rating score and user list for Catalog cards
  + add share and parse buttons to copy and parse links on anime

* Sun Mar 22 2026 David Sultaniiazov <x1z53@altlinux.org> 0.2.2-alt1
- Update to 0.2.2:
  + add environment variables for WebKit stability
  + fix online status only for logged users
  + add formating tags parsing for comments
  + add "Leave comment" section

* Mon Mar 16 2026 David Sultaniiazov <x1z53@altlinux.org> 0.2.1-alt1
- Update to 0.2.1.
- Change URL and VCS.

* Tue Mar 10 2026 David Sultaniiazov <x1z53@altlinux.org> 0.2.0-alt1
- Update to 0.2.0.
- Application rebranding: yummy-anime-gtk -> iris.

* Fri Feb 27 2026 David Sultaniiazov <x1z53@altlinux.org> 0.1.4-alt1
- Update to 0.1.4.

* Sat Feb 21 2026 David Sultaniiazov <x1z53@altlinux.org> 0.1.3-alt1
- Update to 0.1.3.

* Sat Jan 31 2026 David Sultaniiazov <x1z53@altlinux.org> 0.1.2.2-alt1
- Update to 0.1.2.2.

* Thu Jan 29 2026 David Sultaniiazov <x1z53@altlinux.org> 0.1.2.1-alt1
- Initial build.
