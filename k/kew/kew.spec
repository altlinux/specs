Name: kew
Version: 3.0.1
Release: alt1

Summary: A terminal music player
License: GPL-2.0
Group: Sound
Url: https://github.com/ravachol/kew

Source: %name-%version.tar

BuildRequires: gcc-c++
BuildRequires: pkgconfig(chafa)
BuildRequires: pkgconfig(faad2)
BuildRequires: pkgconfig(fftw3f)
BuildRequires: pkgconfig(gio-2.0)
BuildRequires: pkgconfig(glib-2.0)
BuildRequires: pkgconfig(libnotify)
BuildRequires: pkgconfig(ogg)
BuildRequires: pkgconfig(opus)
BuildRequires: pkgconfig(opusfile)
BuildRequires: pkgconfig(taglib)
BuildRequires: pkgconfig(vorbis)

%description
Listen to music in the terminal.

Features:
* Search a music library with partial titles.
* Creates a playlist based on a matched directory.
* Control the player with previous, next and pause.
* Edit the playlist by adding and removing songs.
* Supports gapless playback between files of the same format and type.
* Supports MP3, FLAC, MPEG-4 (AAC, M4A), OPUS, OGG and WAV audio.
* Supports desktop events through MPRIS.
* Private, no data is collected by kew.

%prep
%setup

%build
OPTFLAGS='%optflags' \
%make_build

%install
%make_install DESTDIR=%buildroot PREFIX=%_prefix MAN_DIR=%_mandir install

%files
%_bindir/kew
%_man1dir/kew.1*

%changelog
* Tue Dec 03 2024 Sergey Bolshakov <sbolshakov@altlinux.org> 3.0.1-alt1
- 3.0.1 released
