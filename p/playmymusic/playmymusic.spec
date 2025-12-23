%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1

%define appname com.github.artemanufrij.playmymusic

Name: playmymusic
Version: 2.2.1
Release: alt1

Summary: music player for listening to local music files, online radios and audio CDs
License: GPL-3.0-or-later
Group: Sound
Url: https://github.com/artemanufrij/playmymusic

Source: %name-%version.tar

Patch: %name-%version-%release.patch

BuildRequires(pre): rpm-macros-meson
BuildRequires(pre): rpm-macros-cmake
BuildRequires(pre): rpm-build-vala

BuildRequires: meson
BuildRequires: cmake
BuildRequires: vala-tools
BuildRequires: pkgconfig(gtk+-3.0)
BuildRequires: pkgconfig(json-glib-1.0)
BuildRequires: pkgconfig(granite)
BuildRequires: pkgconfig(sqlite3)
BuildRequires: pkgconfig(gstreamer-pbutils-1.0)
BuildRequires: pkgconfig(taglib_c-0)
BuildRequires: vapi(granite)

Provides: melody = %version
Obsoletes: melody < %version

Requires: elementary-icon-theme

%description
A very fast music player designed extra for large local libraries
which also supports online radios and downloading album covers.

Features:

* Show all Albums from your library
* Group tracks by Artists
* Manage your Playlists
* Listen to online Radio
* Audio CD support
* Manage your MTP device
* ID3-Tag support

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
%_iconsdir/hicolor/symbolic/apps/playlist-queue-symbolic.svg
%_iconsdir/hicolor/symbolic/apps/playlist-symbolic.svg
%_datadir/metainfo/%{appname}.appdata.xml

%changelog
* Tue Dec 23 2025 Nikolay Strelkov <snk@altlinux.org> 2.2.1-alt1
- Initial build for Sisyphus
