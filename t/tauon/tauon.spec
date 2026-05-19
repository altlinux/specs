%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1

%def_with check

Name: tauon
Version: 10.0.0
Release: alt1

Summary: Play your music with style
License: GPL-3.0-or-later
Group: Sound
URL: https://github.com/Taiko2k/Tauon

BuildRequires(pre): rpm-build-python3

BuildRequires: python3-devel
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-wheel
BuildRequires: pkgconfig(flac)
BuildRequires: pkgconfig(libmpg123)
BuildRequires: pkgconfig(vorbis)
BuildRequires: pkgconfig(opusfile)
BuildRequires: pkgconfig(samplerate)
BuildRequires: pkgconfig(libopenmpt)
BuildRequires: pkgconfig(wavpack)
BuildRequires: pkgconfig(libgme)
BuildRequires: pkgconfig(libpipewire-0.3)

%if_with check
BuildRequires: python3(PIL)
BuildRequires: python3(pychromecast)
BuildRequires: python3-module-pygobject3
BuildRequires: python3(OpenGL)
BuildRequires: python3-module-pysdl3
BuildRequires: python3(send2trash)
BuildRequires: python3-module-beautifulsoup4
BuildRequires: python3-module-dbus
BuildRequires: python3(musicbrainzngs)
BuildRequires: python3(mutagen)
BuildRequires: python3(natsort)
BuildRequires: opencc
BuildRequires: python3(setproctitle)
BuildRequires: python3(unidecode)
BuildRequires: python3(h11)
%endif

Requires: typelib(AyatanaAppIndicator3)
Requires: typelib(Gdk)
Requires: typelib(Gtk)
Requires: typelib(Notify)
Requires: typelib(Pango)
Requires: typelib(PangoCairo)
Requires: typelib(Rsvg)

Requires: flac
Requires: mpg123
Requires: opencc
Requires: ffmpeg
Requires: wavpack
Requires: libSDL3_image

Requires: python3(pychromecast)
Requires: python3-module-pygobject3
Requires: python3(OpenGL)
Requires: python3(OpenGL_accelerate)
Requires: python3-module-pysdl3
Requires: python3(natsort)
Requires: python3(setproctitle)

%add_python3_req_skip AppKit objc

Source: %name-%version.tar
Source1: submodules-%name-%version.tar

%description
Tauon is a modern, comfortable and streamlined music player for the
playback of your music collection.

Packed with features while maintaining simplicity. Use drag and drop
for easy file importing and playlist management. Groups albums by folder
and allows you to manage your music with built-in functions such as file
and folder renaming, cover art downloading and file deleting.

Features:

* Playback local audio files including MP3, FLAC and OGG
* Import Spotify tracks and manage Spotify playlists
* Add network tracks from Jellyfin, Airsonic and Plex servers
* Gapless playback
* Automatic CUE sheet detection
* Lookup artists on Rate Your Music and Bandcamp
* Support for last.fm and Listenbrainz
* Import downloaded music archives in one click
* Large album art and gallery layouts
* Support for lyrics including synced lrc files and guitar chords
* Multiple preset colour themes

%prep
%setup -a1

%if_with check
sed -i "s/dbus-python/#dbus-python/" requirements.txt
sed -i "s/^colored_traceback/#colored_traceback/" requirements.txt
sed -i "s/^pypresence/#pypresence/" requirements.txt
sed -i "s/^pylast/#pylast/" requirements.txt
sed -i "s/^tidalapi/#tidalapi/" requirements.txt
# ↓ FIXME - need packaging ↓
sed -i "s/^PlexAPI/#PlexAPI/" requirements.txt
sed -i "s/^jxlpy/#jxlpy/" requirements.txt
sed -i "s/^opencc/#opencc/" requirements.txt
sed -i "s/^tekore/#tekore/" requirements.txt
%endif

%build
%pyproject_build

%install
%pyproject_install

mkdir -p %buildroot%_datadir/locale/
cp -arv %buildroot%python3_sitelibdir/tauon/locale/* %buildroot%_datadir/locale/

install -Dm644 extra/tauonmb.desktop -t %buildroot%_datadir/applications
install -Dm644 extra/tauonmb-symbolic.svg -t %buildroot%_datadir/icons/hicolor/symbolic/apps
install -Dm644 extra/tauonmb.svg -t %buildroot%_iconsdir/hicolor/scalable/apps
install -Dm755 extra/tauonmb.sh %buildroot%_bindir/tauonmb.sh
install -Dm755 extra/tauonmb.sh %buildroot%_bindir/tauon

%find_lang %name

%check
#%%tox_create_default_config
%tox_check_pyproject

%files -f %{name}.lang
%doc README.md
%_bindir/tauon
%_bindir/tauonmb
%_bindir/tauonmb.sh
%_desktopdir/tauonmb.desktop
%_iconsdir/hicolor/scalable/apps/tauonmb.svg
%_iconsdir/hicolor/symbolic/apps/tauonmb-symbolic.svg
%python3_sitelibdir/%name/
%python3_sitelibdir/phazor.cpython*.so
%python3_sitelibdir/phazor-pw.cpython*.so
%python3_sitelibdir/%{pyproject_distinfo tauon_music_box}

%changelog
* Tue May 19 2026 Nikolay Strelkov <snk@altlinux.org> 10.0.0-alt1
- New version 10.0.0.

* Thu Apr 09 2026 Nikolay Strelkov <snk@altlinux.org> 9.1.3-alt1
- New version 9.1.3.

* Fri Mar 20 2026 Nikolay Strelkov <snk@altlinux.org> 9.1.2-alt1
- New version 9.1.2.

* Sun Mar 15 2026 Nikolay Strelkov <snk@altlinux.org> 9.1.1-alt1
- New version 9.1.1.

* Wed Mar 04 2026 Nikolay Strelkov <snk@altlinux.org> 9.1.0-alt1
- New version 9.1.0.

* Wed Feb 25 2026 Nikolay Strelkov <snk@altlinux.org> 9.0.0-alt1
- Initial build for Sisyphus
