%def_enable    jack
%def_enable    fluidsynth
%def_enable    lash
%def_enable    guile_2_2
%def_enable    doc

Name:          denemo
Version:       2.6.0
Release:       alt1
Summary:       WYSIWYG musical score editor, and frontend for Lilypond
Summary(ru_RU.UTF-8): Нотный редактор с поддержкой Lilypond
Group:         Sound
License:       GPLv3+
Url:           http://www.denemo.org/
Vcs:           https://github.com/denemo/denemo.git

Source:        %name-%version.tar
Source1:       %name.conf
BuildRequires: xmllint
BuildRequires: convert
BuildRequires: gtk-doc
BuildRequires: intltool
BuildRequires: flex
BuildRequires: glib2-devel
BuildRequires: libxml2-devel
BuildRequires: librsvg-devel
BuildRequires: libsndfile-devel
BuildRequires: libaubio-devel
BuildRequires: libgtk+3-devel
BuildRequires: libgtksourceview3-devel
BuildRequires: libevince-devel
BuildRequires: librubberband-devel
BuildRequires: libportaudio2-devel
BuildRequires: libfftw3-devel
BuildRequires: libportmidi-devel
%{?!_disable_jack:BuildRequires: jackit-devel}
%{?!_disable_fluidsynth:BuildRequires: libfluidsynth-devel}
%{?!_disable_lash:BuildRequires: liblash-devel}
%{?!_disable_guile_2_2:BuildRequires: guile guile-devel}
Requires:      lilypond
Requires:      TiMidity++
%{?!_disable_jack:BuildRequires: jackd}

%add_optflags -L/%_lib -lm

%description
Denemo is a music notation program for Linux and Windows that lets you rapidly
enter notation for typesetting via the LilyPond music engraver. Music can be
typed in at the PC-Keyboard, or played into a microphone plugged into your
computer's soundcard.

Denemo itself does not engrave the music - it uses LilyPond which generates
beautiful sheet music to the highest publishing standards. Denemo just displays
the music so you can enter and edit the music efficiently.

%description   -l ru_RU.UTF-8
Denemo - графический WYSIWYG редактор партитур, поддерживает ввод с
клавиатуры компьютера и midi-клавиатуры, или даже с микрофона, подключённого
к звуковой карте компьютера. Для вывода нотных записей на печать использует
Lilypond.

Denemo использует библиотеки GTK+, которые являются частью рабочего стола GNOME.

В дополнение к редактированию нот, Denemo предоставляет возможность
воспроизвести мелодию - посредством MIDI или в режиме Csound. В режиме Csound
Denemo создает на лету оркестровый файл на языке Csound и позволяет программе
Csound воспроизвести ее. Об этих и других продвинутых функциях Denemo написано
в руководстве. Вкратце можно сказать, что Denemo - это активный проект и
многообещающая программа.


%prep
%setup

%build
%autoreconf
%configure \
	%{subst_enable guile_2_2} \
	%{subst_enable jack} \
	%{subst_enable fluidsynth} \
	%{subst_enable doc} \

%make_build

%install
%make_install DESTDIR=%buildroot install
mkdir -p %buildroot%_sysconfdir/%name
install -m644 %SOURCE1 %buildroot%_sysconfdir/%name

find %buildroot -name 'Makefile*' -exec rm -f {} \;
mv %buildroot%_datadir/fonts/{truetype,ttf}
mkdir -p %buildroot%_iconsdir/hicolor/{48x48,32x32,16x16}/apps/ \
         %buildroot%_pixmapsdir/ \
         %buildroot%_desktopdir \
         %buildroot%_datadir/appdata
convert pixmaps/%{name}128x128.png -resize 48x48 %buildroot%_liconsdir/%name.png
convert pixmaps/%{name}128x128.png -resize 32x32 %buildroot%_niconsdir/%name.png
convert pixmaps/%{name}128x128.png -resize 16x16 %buildroot%_miconsdir/%name.png
install -m644 pixmaps/%name.png %buildroot%_pixmapsdir/%name.png
install -m644 pixmaps/org.denemo.Denemo.desktop %buildroot%_desktopdir/%name.desktop
xmllint org.denemo.Denemo.appdata.xml.in > %buildroot%_datadir/appdata/%name.appdata.xml
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
%_datadir/appdata/%name.appdata.xml
%_pixmapsdir/%name.png
%_iconsdir/hicolor/*/apps/%name.png
%doc AUTHORS ChangeLog* LICENSE_OFL.txt NEWS README*

%changelog
* Mon May 20 2024 Pavel Skrylev <majioa@altlinux.org> 2.6.0-alt1
- ^ 2.4.0 -> 2.6.0
- ! fixed compilation without explicitly defined math (-lm) library

* Mon Mar 01 2021 Sergey Bolshakov <sbolshakov@altlinux.ru> 2.5.0-alt1
- 2.5.0 released

* Thu Feb 04 2021 Sergey Bolshakov <sbolshakov@altlinux.ru> 2.4.5-alt1
- 2.4.5 released

* Fri Dec 11 2020 Pavel Skrylev <majioa@altlinux.org> 2.4.0-alt1
- ^ 2.3.0 -> 2.4.0

* Wed Jan 22 2020 Pavel Skrylev <majioa@altlinux.org> 2.3.0-alt1
- updated (^) 0.8.12 -> 2.3.0

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
