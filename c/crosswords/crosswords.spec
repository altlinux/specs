%define _unpackaged_files_terminate_build 1
%define app_id org.gnome.Crosswords
%def_enable check

Name: crosswords
Version: 0.3.15
Release: alt1

Summary: Solve crossword puzzles
License: GPL-3.0-or-later
Group: Games/Puzzles

Url: https://gitlab.gnome.org/jrb/crosswords
Vcs: https://gitlab.gnome.org/jrb/crosswords
Source: %name-%version.tar
Patch0: %name-%version-alt.patch

BuildRequires(pre): rpm-macros-meson
BuildRequires: rpm-build-python3
BuildRequires: meson
BuildRequires: pkgconfig(iso-codes)
BuildRequires: pkgconfig(gio-2.0)
BuildRequires: pkgconfig(json-glib-1.0)
BuildRequires: pkgconfig(gtk4)
BuildRequires: pkgconfig(librsvg-2.0)
BuildRequires: pkgconfig(libadwaita-1)
BuildRequires: pkgconfig(libipuz-0.5)
%if_enabled check
BuildRequires: appstream
BuildRequires: desktop-file-utils
%endif

Requires: %name-puzzle-sets-cats-and-dogs
Requires: %name-puzzle-sets-uri
Requires: ipuz-convertor

%description
A simple and fun game of crosswords. Load your crossword files, or play one of
the included games. Features include:

- Support for shaped and colored crosswords
- Loading .ipuz, .jpuz, .xd, and .puz files
- Hint support, such as showing mistakes and suggesting words
- Dark mode
- Locally installed crosswords as well as support for 3rd party downloaders

%package -n crossword-editor
Summary: Crossword puzzle editor for GNOME Crosswords
Group: Editors

Requires: %name

%description -n crossword-editor
Standalone-tool to create crossword puzzles based on GNOME Crosswords. It can
be used to create simple puzzles with grids and clues. It has a pattern solver
and grid autofill dialog for filling in hard-to-finish corners, and will make
suggestions of words when creating the grid.

%package puzzle-sets-cats-and-dogs
Summary: Cats and dogs puzzle set for GNOME Crosswords
Group: Games/Puzzles

Requires: %name

%description puzzle-sets-cats-and-dogs
%summary.

%package puzzle-sets-uri
Summary: Puzzle sets loader for GNOME Crosswords
Group: Games/Puzzles

Requires: %name

%description puzzle-sets-uri
%summary.

%package thumbnailer
Summary: GNOME Crosswords Thumbnailer
Group: Graphics

Requires: %name

%description thumbnailer
%summary.

%package doc
Summary: Documentation files for GNOME Crosswords
Group: Documentation

Requires: %name

%description doc
%summary.

%package -n ipuz-convertor
Summary: Converts puz files to ipuz files
Group: Games/Puzzles

Requires: %name

%description -n ipuz-convertor
ipuz-converter is a script to convert puzzle files from puz to ipuz.

%prep
%setup
%patch -p 1

%build
%meson -Ddevelopment=false
%meson_build

%install
%meson_install
%find_lang --with-gnome %name

%check
%meson_test

%files -f %name.lang
%_bindir/%name
%_desktopdir/%app_id.desktop
%_datadir/%name/word-lists/player.gresource
%_iconsdir/hicolor/*/apps/%{app_id}*.svg
%_datadir/dbus-1/services/%app_id.service
%_datadir/glib-2.0/schemas/%app_id.gschema.xml
%_datadir/metainfo/%app_id.metainfo.xml
%_datadir/mime/packages/%app_id.xml
%_datadir/%name/puzzle-sets/*
%exclude %_datadir/%name/puzzle-sets/uri*
%exclude %_datadir/%name/puzzle-sets/cats-and-dogs*
%exclude %_iconsdir/hicolor/*/apps/%{app_id}.Editor*.svg

%files -n crossword-editor
%_bindir/crossword-editor
%_desktopdir/%app_id.Editor.desktop
%_datadir/dbus-1/services/%app_id.Editor.service
%_datadir/glib-2.0/schemas/%app_id.Editor.gschema.xml
%_iconsdir/hicolor/*/apps/%app_id.Editor*.svg
%_datadir/metainfo/%app_id.Editor.metainfo.xml
%_datadir/%name/word-lists/broda.gresource
%_datadir/%name/word-lists/wordnik.gresource

%files thumbnailer
%_bindir/%name-thumbnailer
%_datadir/thumbnailers/%name.thumbnailer

%files puzzle-sets-uri
%_datadir/%name/puzzle-sets/uri*

%files puzzle-sets-cats-and-dogs
%_datadir/%name/puzzle-sets/cats-and-dogs*

%files -n ipuz-convertor
%_datadir/%name/ipuz-convertor
%_libexecdir/ipuz-convertor

%files doc
%doc docs

%changelog
* Wed Jun 04 2025 David Sultaniiazov <x1z53@altlinux.org> 0.3.15-alt1
- Initial build
