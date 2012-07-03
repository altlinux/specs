Name: gnormalize
Version: 0.63
Release: alt1.qa1

Summary: An audio converter, a ripper, an encoder, a tag editor and a cd player
summary(ru_RU.KOI8-R): Преобразователь, считыватель, кодировщик звука, а также редактор тэгов и проигрыватель компакт-дисков

License: GPL
Group: Sound
Url: http://gnormalize.sourceforge.net/

Packager: Vitaly Lipatov <lav@altlinux.ru>

Source: http://prdownloads.sf.net/%name/%name-%version.tar.bz2

BuildArchitectures: noarch

Requires: perl-CDDB_get perl-MP3-Info perl-Audio-CD
Requires: cdparanoia normalize cdda2wav

# Automatically added by buildreq on Wed Jul 16 2008 (-bi)
BuildRequires: perl-Encode perl-Gtk2 perl-Unicode-Normalize

%description
gnormalize is a front end to normalize, a ripper, an encoder and
an audio converter. It uses gtk2-perl.

gnormalize decodes the MP3/MP4/MPC/OGG/APE/FLAC file to WAV,
then normalizes the WAV to a targeted volume level and re-encodes it.
gnormalize can also rip, encode, convert audio format between MP3, MP4,
MPC, OGG, APE and FLAC, play audio cd, change the encoding and tag
properties of final normalized files.

%prep
%setup -q
%__subst "s|Gtk2 -init;|Gtk2; INIT {Gtk2->init;}|" ./gnormalize

%build
%install
mkdir -p %buildroot%_bindir
mkdir -p %buildroot%_datadir/gnormalize/animations
mkdir -p %buildroot{%_niconsdir,%_liconsdir,%_miconsdir}

install -m 755 gnormalize     %buildroot%_bindir/gnormalize

install -m 644 README            %buildroot%_datadir/gnormalize
install -m 644 animations/*.gif  %buildroot%_datadir/gnormalize/animations

# icons
install -m 644 icons/%name-48.png %buildroot%_liconsdir/%name.png
install -m 644 icons/%name-32.png %buildroot%_niconsdir/%name.png
install -m 644 icons/%name-16.png %buildroot%_miconsdir/%name.png

mkdir -p %buildroot%_desktopdir
cat > %buildroot%_desktopdir/%name.desktop << EOF
[Desktop Entry]
Name=Gnormalize
Comment=A ripper, an encoder and an audio converter
Exec=%_bindir/%name
Icon=%name
Terminal=false
Type=Application
Categories=AudioVideo;Audio;AudioVideoEditing;
EOF

%files
%doc README
%_bindir/%name
%_desktopdir/*
%_niconsdir/%name.png
%_liconsdir/%name.png
%_miconsdir/%name.png
%_datadir/%name/

%changelog
* Tue Nov 24 2009 Repocop Q. A. Robot <repocop@altlinux.org> 0.63-alt1.qa1
- NMU (by repocop): the following fixes applied:
  * update_menus for gnormalize
  * postclean-05-filetriggers for spec file

* Wed Jul 16 2008 Vitaly Lipatov <lav@altlinux.ru> 0.63-alt1
- new version 0.63 (with rpmrb script)
- update buildreqs

* Sat Apr 12 2008 Vitaly Lipatov <lav@altlinux.ru> 0.53-alt1
- new version 0.53 (with rpmrb script)

* Thu Dec 28 2006 Vitaly Lipatov <lav@altlinux.ru> 0.52-alt0.2
- use noarch build, cleanup spec
- add requires to perl-Audio-CD
- remove mppenc/mppdec ugly precompiled binaries from package

* Mon Dec 25 2006 Vitaly Lipatov <lav@altlinux.ru> 0.52-alt0.1
- new version 0.52 (with rpmrb script)
- replace debian menu with desktop file
- add requires to perl-MP3-Info

* Wed Sep 20 2006 Vitaly Lipatov <lav@altlinux.ru> 0.50-alt0.1
- new version 0.50 (with rpmrb script)

* Sun Apr 02 2006 Vitaly Lipatov <lav@altlinux.ru> 0.49-alt0.1
- new version 0.49, update buildreqs
- fix icons dir using

* Mon Nov 14 2005 Vitaly Lipatov <lav@altlinux.ru> 0.47-alt1
- new version

* Mon Oct 24 2005 Vitaly Lipatov <lav@altlinux.ru> 0.45-alt1
- new version
- fix arch (bug #8272)

* Sat Sep 17 2005 Vitaly Lipatov <lav@altlinux.ru> 0.40-alt1.1
- fix menu

* Thu Sep 15 2005 Vitaly Lipatov <lav@altlinux.ru> 0.40-alt1
- fix URL, fix dir packing
- fix autoreq, add used program to requires
- improve spec

* Tue Sep 13 2005 Vitaly Lipatov <lav@altlinux.ru> 0.40-alt0.1
- first build for ALT Linux Sisyphus
