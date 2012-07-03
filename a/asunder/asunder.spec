Name: asunder
Version: 2.2
Release: alt1

Summary: Audio CD ripper and encoder for Linux
License: %gpl2only
Group: Sound
Url: http://littlesvr.ca/%name/index.php

Source: http://littlesvr.ca/%name/releases/%name-%version.tar.bz2
Patch1: %name-1.5-fix-desktop-file-categories.patch
Packager: Alexey Rusakov <ktirf@altlinux.org>

Requires: cdparanoia

BuildPreReq: rpm-build-licenses >= 0.7 intltool

BuildPreReq: libgtk+2-devel >= 2.4.0
BuildPreReq: glib2-devel >= 2.4.0
BuildPreReq: libcddb-devel >= 0.9.5

%description
Asunder is a graphical Audio CD ripper and encoder for Linux. You can use
it to save tracks from an Audio CD as WAV, MP3, OGG, FLAC, and/or Wavpack.
Features:
    * Supports WAV, MP3, Ogg Vorbis, FLAC, and Wavpack audio files
    * Uses CDDB to name and tag each track
    * Creates M3U playlists
    * Can encode to multiple formats in one session
    * Simultaneous rip and encode
    * Allows for each track to be by a different artist
    * Does not require a specific desktop environment

%prep
%setup -q
%patch1

%build
%configure
%make

%install
%make_install install DESTDIR=%buildroot

# Copy the icon to the standard location
mkdir -p %buildroot%_liconsdir
cp %buildroot%_pixmapsdir/%name.png %buildroot%_liconsdir/

%find_lang %name

%files -f %name.lang
%_bindir/%name
%_desktopdir/%name.desktop
%_pixmapsdir/%name.png
%_liconsdir/%name.png

%changelog
* Tue May 29 2012 Yuri N. Sedunov <aris@altlinux.org> 2.2-alt1
- 2.2

* Fri Aug 19 2011 Yuri N. Sedunov <aris@altlinux.org> 2.1-alt1
- updated to 2.1

* Mon Aug 31 2009 Alexey Rusakov <ktirf@altlinux.org> 1.6.2-alt2
- Replaced excess categories in the .desktop file, with the one that fits
  the application better.

* Sat Dec 06 2008 Alexey Rusakov <ktirf@altlinux.org> 1.6.2-alt1
- New version (1.6.2).
- Removed update_menus call, since it is no more needed.
- Added Packager tag.
- Updated the patch for .desktop file (more categories added).

* Sun Apr 27 2008 Alexey Rusakov <ktirf@altlinux.org> 1.5-alt2
- Fixes after repocop reports:
  - Mention additional categories in the .desktop file.
  - Copy the icon to the standard location.

* Sun Apr 27 2008 Alexey Rusakov <ktirf@altlinux.org> 1.5-alt1
- new version (1.5)

* Mon Feb 04 2008 Alexey Rusakov <ktirf@altlinux.org> 1.0.2-alt1
- New version (1.0.2).

* Sat Oct 13 2007 Alexey Rusakov <ktirf@altlinux.org> 0.9-alt2
- added runtime dependency on cdparanoia (ALT Bug #13112).
- added menus update in post/postun (ALT Bug #13113).

* Thu Oct 11 2007 Alexey Rusakov <ktirf@altlinux.org> 0.9-alt1
- new version (0.9)
- fixed the package group.

* Sat Sep 01 2007 Alexey Rusakov <ktirf@altlinux.org> 0.8.1-alt1
- Initial Sisyphus package
