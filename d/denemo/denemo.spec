%def_disable jack
%def_enable fluidsynth
%def_enable doc

Name: denemo
Version: 0.8.12
Release: alt1.1

Summary: WYSIWYG musical score editor, and frontend for Lilypond
Summary(ru_RU.KOI8-R): Нотный редактор с поддержкой Lilypond
Group: Sound
License: GPL
Url: http://www.%name.org/

Packager: Ildar Mulyukov <ildar@altlinux.ru>

Source: %name.tar
Source1: %name.conf
Patch0: %name-0.8.12-alt-glib2-2.32.0.patch

Requires: TiMidity++ lilypond
# csound

# Automatically added by buildreq on Sat Jan 30 2010 (-bi)
BuildRequires: /usr/bin/convert cvs flex guile18-devel libaubio-devel libfftw3-devel libgtksourceview-devel libportaudio2-devel libsamplerate-devel libxml2-devel xz

#gtk-doc

%if_enabled jack
BuildRequires: jackit-devel
Requires: jackd
%endif
%if_enabled fluidsynth
BuildRequires: libfluidsynth-devel
%endif
%if_enabled lash
BuildRequires: liblash-devel
%endif

%description
Denemo is a music notation program for Linux and Windows that lets you rapidly
enter notation for typesetting via the LilyPond music engraver. Music can be
typed in at the PC-Keyboard, or played into a microphone plugged into your
computer's soundcard.

Denemo itself does not engrave the music - it uses LilyPond which generates
beautiful sheet music to the highest publishing standards. Denemo just displays
the music so you can enter and edit the music efficiently.

%description -l ru_RU.KOI8-R
Denemo - графический WYSIWYG редактор партитур, поддерживает ввод с
клавиатуры компьютера и midi-клавиатуры, или даже с микрофона, подключённого
к звуковой карте компьютера. Для вывода нотных записей на печать использует
Lilypond.

%prep
%setup -q -n %name
%patch0 -p0

%build
%autoreconf
%configure \
	%{subst_enable jack} \
	%{subst_enable fluidsynth} \
	%{subst_enable doc} \

%make_build

%install
%make_install DESTDIR=%buildroot install
install -m644 %SOURCE1 %buildroot%_sysconfdir/%name

find %buildroot -name 'Makefile*' -exec rm -f {} \;
mv %buildroot%_datadir/fonts/{truetype,ttf}
mkdir -p %buildroot%_iconsdir/hicolor/{48x48,32x32,16x16}/apps/
convert %buildroot%_pixmapsdir/%name.png -resize 48x48 %buildroot%_liconsdir/%name.png
convert %buildroot%_pixmapsdir/%name.png -resize 32x32 %buildroot%_niconsdir/%name.png
convert %buildroot%_pixmapsdir/%name.png -resize 16x16 %buildroot%_miconsdir/%name.png
xz ChangeLog
%find_lang %name

%post
fc-cache %_datadir/fonts/ttf/%name ||:

%files -f %name.lang
%_sysconfdir/%name
%_bindir/*
%_desktopdir/%name.desktop
%_datadir/%name
%_datadir/fonts/ttf/%name
%_pixmapsdir/%name.png
%_iconsdir/hicolor/*/apps/%name.png
%doc AUTHORS ChangeLog* LICENSE_OFL.txt NEWS README*

%changelog
* Wed Apr 04 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.8.12-alt1.1
- Fixed build with new glib2

* Fri Jan 29 2010 Ildar Mulyukov <ildar@altlinux.ru> 0.8.12-alt1
- new version
- add config file

* Tue Apr 07 2009 Ildar Mulyukov <ildar@altlinux.ru> 0.8.2_230_g06967f1-alt1
- new version
- patches are no more needed

* Thu Nov 06 2008 Ildar Mulyukov <ildar@altlinux.ru> 0.8-alt1
- back from orphaned
- lots of changes since last build 4.5 years ago!

* Thu Apr 15 2004 Yuri N. Sedunov <aris@altlinux.ru> 0.7.2-alt0.5a
- 0.7.2a

* Mon Apr 07 2003 Yuri N. Sedunov <aris@altlinux.ru> 0.7.1-alt1
- go to gtk2.

* Mon Oct 14 2002 Yuri N. Sedunov <aris@altlinux.ru> 0.6.0-alt2
- Rebuild with gcc-3.2.

* Tue Jul 02 2002 Yuri N. Sedunov <aris@altlinux.ru> 0.6.0-alt1
- 0.6.0

* Wed Feb 20 2002 Yuri N. Sedunov <aris@altlinux.ru> 0.5.9-alt1
- new version

* Mon Jan 28 2002 Yuri N. Sedunov <aris@altlinux.ru> 0.5.8-alt2
- cleanups

* Sun Dec 30 2001 Yuri N. Sedunov <aris@altlinux.ru> 0.5.8-alt1
- Updated to 0.5.8

* Thu Nov 16 2001 Yuri N. Sedunov <aris@altlinux.ru> 0.5.7-alt2
- Spec cleanup.

* Fri Nov 16 2001 Yuri N. Sedunov <aris@altlinux.ru> 0.5.7-alt1
- First build for Sisyphus
