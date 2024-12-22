%define APP_ID io.github.halfmexican.Mingle
%def_enable check

Name: mingle
Version: 0.16.1
Release: alt1

Summary: Combine emojis with Google's Emoji Kitchen
License: GPL-3.0-or-later
Group: Graphical desktop/GNOME

Url: https://github.com/halfmexican/mingle
Vcs: https://github.com/halfmexican/mingle
Source: %name-%version.tar

BuildRequires(pre): rpm-macros-meson
BuildRequires: meson >= 0.62.0
BuildRequires: vala
BuildRequires: blueprint-compiler
BuildRequires: pkgconfig(gtk4)
BuildRequires: pkgconfig(libadwaita-1)
BuildRequires: pkgconfig(json-glib-1.0)
BuildRequires: pkgconfig(gee-0.8)
%if_enabled check
BuildRequires: desktop-file-utils
BuildRequires: appstream
BuildRequires: libgio
%endif

%description
Combine emojis with Emoji Kitchen, and send them to friends.

%prep
%setup

%build
%meson
%meson_build

%install
%meson_install
%find_lang --with-gnome %name

%check
%__meson_test

%files -f %name.lang
%_bindir/%name
%_desktopdir/%APP_ID.desktop
%_datadir/glib-2.0/schemas/%APP_ID.gschema.xml
%_iconsdir/hicolor/scalable/actions/*.svg
%_iconsdir/hicolor/*/apps/%{APP_ID}*.svg
%_datadir/metainfo/%APP_ID.metainfo.xml

%changelog
* Tue Dec 17 2024 Oleg Shchavelev <oleg@altlinux.org> 0.16.1-alt1
- New version 0.16.1
- Update build dependencies for check
- Add unpackaged metainfo file

* Mon Nov 18 2024 Oleg Shchavelev <oleg@altlinux.org> 0.15-alt1
- Initial build
