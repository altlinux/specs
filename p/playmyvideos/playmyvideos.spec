%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1

%define appname com.github.artemanufrij.playmyvideos

Name: playmyvideos
Version: 1.1.2
Release: alt1

Summary: video player for watching local video files
License: GPL-3.0-or-later
Group: Video
Url: https://github.com/artemanufrij/playmyvideos

Source: %name-%version.tar

Patch: %name-%version-%release.patch

BuildRequires(pre): rpm-macros-meson
BuildRequires(pre): rpm-macros-cmake
BuildRequires(pre): rpm-build-vala

BuildRequires: meson
BuildRequires: cmake
BuildRequires: vala-tools
BuildRequires: pkgconfig(gtk+-3.0)
BuildRequires: pkgconfig(granite)
BuildRequires: pkgconfig(sqlite3)
BuildRequires: pkgconfig(clutter-gtk-1.0)
BuildRequires: pkgconfig(clutter-gst-3.0)
BuildRequires: vapi(granite)

Provides: cinema = %version
Obsoletes: cinema < %version

Requires: elementary-icon-theme

%description
A very fast video player designed extra for large local libraries
which also supports downloading of box covers.

Features:

* Season playlist
* Subtiles support
* 'TheMovieDB.org' integration for fetching covers

%prep
%setup
sed -i "s|data/icons/64/|%_iconsdir/hicolor/64x64/apps/|" README.md

%patch -p1

%build
%meson
%meson_build

%install
%meson_install

%find_lang %appname

%check
%meson_test

%files -f %{appname}.lang
%doc debian/copyright README.md screenshots
%_bindir/%appname
%_desktopdir/%{appname}.desktop
%_datadir/glib-2.0/schemas/%{appname}.gschema.xml
%_iconsdir/hicolor/*/apps/%{appname}.svg
%_datadir/metainfo/%{appname}.appdata.xml

%changelog
* Tue Dec 23 2025 Nikolay Strelkov <snk@altlinux.org> 1.1.2-alt1
- Initial build for Sisyphus
