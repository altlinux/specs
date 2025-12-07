%define _unpackaged_files_terminate_build 1

Name: grimripper
Version: 3.0.2
Release: alt1

Summary: Graphical audio CD ripper and encoder
License: GPL-2.0-or-later
Group: Sound
Url: https://gitlab.gnome.org/Salamandar/GrimRipper

Source: %name-%version.tar

# sync with version 3.0.2-5 from Debian unstable
Patch: %name-%version-%release.patch

BuildRequires(pre): rpm-macros-meson
BuildRequires(pre): rpm-macros-cmake

BuildRequires: meson
BuildRequires: cmake
BuildRequires: pkgconfig(gtk+-3.0)
BuildRequires: pkgconfig(libcddb)

Requires: cdparanoia
Requires: /usr/bin/flac
Requires: /usr/bin/lame
Requires: /usr/bin/mac
Requires: /usr/bin/oggenc
Requires: /usr/bin/opusenc
Requires: /usr/bin/wavpack

%description
GrimRipper can be used to save tracks from Audio CDs. Main features:

* Supports WAV, MP3, Ogg Vorbis, FLAC, and Wavpack audio files
* Uses CDDB to name and tag each track
* Can encode to multiple formats in one session
* Creates M3U playlists
* Allows for each track to be by a different artist
* Does not require a specific desktop environment (just Gtk3)

%prep
%setup
%patch -p1
sed -i "s/Categories=.*/Categories=AudioVideo;Audio;Recorder;Music;/" data/org.gnome.gitlab.grimripper.desktop

%build
%meson
%meson_build

%install
%meson_install

%find_lang %name --all-name

%check
%meson_test

%files -f %{name}.lang
%doc AUTHORS ChangeLog COPYING Readme.md TODO
%_bindir/grimripper
%_desktopdir/org.gnome.gitlab.grimripper.desktop
%_iconsdir/hicolor/scalable/apps/org.gnome.gitlab.grimripper.svg
%_datadir/metainfo/org.gnome.gitlab.grimripper.metainfo.xml

%changelog
* Sun Dec 07 2025 Nikolay Strelkov <snk@altlinux.org> 3.0.2-alt1
- Initial build for Sisyphus
