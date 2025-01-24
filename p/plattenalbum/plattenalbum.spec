%define _unpackaged_files_terminate_build 1
%define rdn_name de.wagnermartin.Plattenalbum

Name: plattenalbum
Version: 2.2.1
Release: alt1
Summary: Connect to your music
License: GPL-3.0
Group: Sound
Url: https://github.com/SoongNoonien/plattenalbum

Source: %name-%version.tar

BuildArch: noarch

BuildRequires(pre): rpm-macros-meson
BuildRequires: meson rpm-build-python3
BuildRequires: python3-module-mpd python3-module-pygobject3
BuildRequires: libgio gtk4-update-icon-cache

%description
A client for the Music Player Daemon (MPD).
Browse your collection while viewing large album covers. Play your music without
managing playlists.

%prep
%setup

%build
%meson
%meson_build

%install
%meson_install

%files
%_bindir/plattenalbum
%_desktopdir/%rdn_name.desktop
%_datadir/%rdn_name/%rdn_name.gresource
%_datadir/glib-2.0/schemas/%rdn_name.gschema.xml
%_iconsdir/hicolor/*/apps/%{rdn_name}*.svg
%_datadir/locale/*/LC_MESSAGES/%rdn_name.mo
%_datadir/metainfo/%rdn_name.metainfo.xml
%doc README* NEWS


%changelog
* Fri Jan 24 2025 Andrey Kovalev <ded@altlinux.org> 2.2.1-alt1
- Initial build for Sisyphus.
