Name: kew
Version: 4.1.7
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
%make_build OPTFLAGS='%optflags' PREFIX=%_prefix

%install
%make_install DESTDIR=%buildroot PREFIX=%_prefix MAN_DIR=%_mandir install

%files
%_bindir/kew
%_datadir/kew
%_desktopdir/*.desktop
%_iconsdir/*/*/*/*.png
%_man1dir/kew.1*

%changelog
* Mon Jul 06 2026 Sergey Bolshakov <sbolshakov@altlinux.org> 4.1.7-alt1
- 4.1.7 released

* Thu Apr 30 2026 Sergey Bolshakov <sbolshakov@altlinux.org> 4.0.0-alt1
- 4.0.0 released

* Tue Dec 23 2025 Sergey Bolshakov <sbolshakov@altlinux.org> 3.7.3-alt1
- 3.7.3 released

* Tue Dec 16 2025 Sergey Bolshakov <sbolshakov@altlinux.org> 3.7.2-alt1
- 3.7.2 released

* Fri Dec 12 2025 Sergey Bolshakov <sbolshakov@altlinux.org> 3.7.1-alt1
- 3.7.1 released

* Thu Dec 11 2025 Sergey Bolshakov <sbolshakov@altlinux.org> 3.7.0-alt1
- 3.7.0 released

* Tue Oct 21 2025 Sergey Bolshakov <sbolshakov@altlinux.org> 3.6.4-alt1
- 3.6.4 released

* Mon Oct 20 2025 Sergey Bolshakov <sbolshakov@altlinux.org> 3.6.3-alt1
- 3.6.3 released

* Mon Oct 13 2025 Sergey Bolshakov <sbolshakov@altlinux.org> 3.5.3-alt1
- 3.5.3 released

* Tue Oct 07 2025 Sergey Bolshakov <sbolshakov@altlinux.org> 3.5.2-alt1
- 3.5.2 released

* Fri Aug 29 2025 Sergey Bolshakov <sbolshakov@altlinux.org> 3.4.1-alt1
- 3.4.1 released

* Fri Jul 11 2025 Sergey Bolshakov <sbolshakov@altlinux.org> 3.4.0-alt1
- 3.4.0 released

* Fri May 30 2025 Sergey Bolshakov <sbolshakov@altlinux.org> 3.3.3-alt1
- 3.3.3 released

* Wed May 14 2025 Sergey Bolshakov <sbolshakov@altlinux.org> 3.3.2-alt1
- 3.3.2 released

* Mon May 12 2025 Sergey Bolshakov <sbolshakov@altlinux.org> 3.3.0-alt1
- 3.3.0 released

* Wed Apr 23 2025 Sergey Bolshakov <sbolshakov@altlinux.org> 3.2.0-alt1
- 3.2.0 released

* Mon Mar 24 2025 Sergey Bolshakov <sbolshakov@altlinux.org> 3.1.2-alt1
- 3.1.2 released

* Mon Jan 20 2025 Sergey Bolshakov <sbolshakov@altlinux.org> 3.0.3-alt1
- 3.0.3 released

* Fri Dec 13 2024 Sergey Bolshakov <sbolshakov@altlinux.org> 3.0.2-alt1
- 3.0.2 released

* Tue Dec 03 2024 Sergey Bolshakov <sbolshakov@altlinux.org> 3.0.1-alt1
- 3.0.1 released
