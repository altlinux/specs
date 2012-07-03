Name: gcompris
Version: 11.12.01
Release: alt1
Summary: Educational suite for kids 3-10 years old
Summary(ru_RU.UTF8): Набор образовательных игр для детей от 3-х до 10 лет
License: GPLv3
Group: Games/Educational
URL: http://www.gcompris.net
Source: ftp://gcompris.sourceforge.net/%name-%version.tar
Source2: %name.desktop
Source3: %name-edit.desktop
Source4: %name-16x16.png
Source5: %name-32x32.png
Source6: %name-48x48.png
Source10: voices-%version.tar
Patch: %name-%version-%release.patch


Packager: Slava Dubrovskiy <dubrsl@altlinux.ru>

Obsoletes: %name-devel %name-gst-plugin

#BuildPreReq: /proc
# Automatically added by buildreq on Thu Jan 07 2010
BuildRequires: chess gnome-common gstreamer-devel intltool libgnet-devel libgnomecanvas-devel librsvg-devel libsqlite3-devel python-module-pycairo-devel python-module-pygtk-devel python-module-pysqlite2 python-modules-encodings tetex-core

Requires: chess sqlite3
# needed for sound support
Requires: gst-plugins-base >= 0.10.14-alt3 gst-plugins-base-audio-filters gst-plugins-vorbis gst-plugins-ogg gst-plugins-alsa
# needed for python support
#Requires: python%__python_version(gnomecanvas) python%__python_version(pygtk) python%__python_version(cairo) python%__python_version(gnome) python%__python_version(pysqlite2)

Provides: python%__python_version(_gcompris) python%__python_version(_gcompris_anim) python%__python_version(_gcompris_bonus)
Provides: python%__python_version(_gcompris_score) python%__python_version(_gcompris_skin) python%__python_version(_gcompris_sound)
Provides: python%__python_version(_gcompris_timer) python%__python_version(_gcompris_utils) python%__python_version(_gcompris_admin)
BuildRequires: desktop-file-utils

%description
GCompris - is an educationnal game for children starting at 3.
More than 50 different activities are proposed:
* Click on the animals => learn the mouse/click usage
* Type the falling letters => learn the keyboard usage
* Falling Dices
* Falling words
* Basic algebra
* Time learning with an analog clock
* Puzzle game with famous paintings
* Drive Plane to catch clouds in increasing number
* Balance the scales
* And much more ...

The Game is included in the Main desktop menu in 'Games'.
You should install it only if you have children using this computer.

%description -l ru_RU.UTF8
GCompris - набор образовательных игр и программ для детей от 3-х лет
Предоставляется более 50 различных обучающих игр:
* Выбери животное => обучение исрользованию мыши
* Падающие буквы => обучение использованию клавиатуры
* Падающие кости
* Падающие слова
* Основы счёта
* Обучение (стрелочным) часам
* Головоломка с известными картинами
* На летящем самолёте ловить облака с возрастающими цифрами
* И многое другое ...

Устанавливать есть смысл только если есть дети, использующие компьютер
К играм есть обширное голосовое сопровождение в пакете %name-voices-ru

%package voices-en
Summary: All voices in English for GCompris
Group: Games/Educational
BuildArch: noarch
Requires: %name = %version-%release
%description voices-en
All voices in English for GCompris

%package voices-ru
Summary: All voices in Russian for GCompris
Group: Games/Educational
BuildArch: noarch
Requires: %name = %version-%release
%description voices-ru
All voices in Russian for GCompris

%package voices-da
Summary: All voices in Danish for GCompris
Group: Games/Educational
BuildArch: noarch
Requires: %name = %version-%release
%description voices-da
All voices in Danish for GCompris

%package voices-de
Summary: All voices in German for GCompris
Group: Games/Educational
BuildArch: noarch
Requires: %name = %version-%release
%description voices-de
All voices in German for GCompris

%package voices-es
Summary: All voices in Spanish for GCompris
Group: Games/Educational
BuildArch: noarch
Requires: %name = %version-%release
%description voices-es
All voices in Spanish for GCompris

%package voices-fr
Summary: All voices in French for GCompris
Group: Games/Educational
BuildArch: noarch
Requires: %name = %version-%release
%description voices-fr
All voices in Spanish for GCompris

%package voices-it
Summary: All voices in Italian for GCompris
Group: Games/Educational
BuildArch: noarch
Requires: %name = %version-%release
%description voices-it
All voices in Italian for GCompris

%package voices-pt
Summary: All voices in Portuguese for GCompris
Group: Games/Educational
BuildArch: noarch
Requires: %name = %version-%release
%description voices-pt
All voices in Portuguese for GCompris

%package voices-sv
Summary: All voices in Swedish for GCompris
Group: Games/Educational
BuildArch: noarch
Requires: %name = %version-%release
%description voices-sv
All voices in Swedish for GCompris

%package voices-eu
Summary: All voices in Basque for GCompris
Group: Games/Educational
BuildArch: noarch
Requires: %name = %version-%release
%description voices-eu
All voices in Basque for GCompris

%package voices-hu
Summary: All voices in Hungarian for GCompris
Group: Games/Educational
BuildArch: noarch
Requires: %name = %version-%release
%description voices-hu
All voices in Hungarian for GCompris

%package voices-fi
Summary: All voices in Finish for GCompris
Group: Games/Educational
BuildArch: noarch
Requires: %name = %version-%release
%description voices-fi
All voices in Finish for GCompris

%package voices-nl
Summary: All voices in Dutch for GCompris
Group: Games/Educational
BuildArch: noarch
Requires: %name = %version-%release
%description voices-nl
All voices in Dutch for GCompris

%package voices-cs
Summary: All voices in Czech for GCompris
Group: Games/Educational
BuildArch: noarch
Requires: %name = %version-%release
%description voices-cs
All voices in Czech for GCompris

%package voices-mr
Summary: All voices in Indian Marathi for GCompris
Group: Games/Educational
BuildArch: noarch
Requires: %name = %version-%release
%description voices-mr
All voices in Indian Marathi for GCompris

%package voices-pt_BR
Summary: All voices in Brasilian for GCompris
Group: Games/Educational
BuildArch: noarch
Requires: %name = %version-%release
%description voices-pt_BR
All voices in Brasilian for GCompris

%package voices-tr
Summary: All voices in Turk for GCompris
Group: Games/Educational
BuildArch: noarch
Requires: %name = %version-%release
%description voices-tr
All voices in Turk for GCompris

%package voices-so
Summary: All voices in Somali for GCompris
Group: Games/Educational
BuildArch: noarch
Requires: %name = %version-%release
%description voices-so
All voices in Somali for GCompris

%package voices-ar
Summary: All voices in Arabic for GCompris
Group: Games/Educational
BuildArch: noarch
Requires: %name = %version-%release
%description voices-ar
All voices in Arabic for GCompris

%package voices-hi
Summary: All voices in Indian Hindi for GCompris
Group: Games/Educational
BuildArch: noarch
Requires: %name = %version-%release
%description voices-hi
All voices in Indian Hindi for GCompris

%package voices-id
Summary: All voices in Indonesian for GCompris
Group: Games/Educational
BuildArch: noarch
Requires: %name = %version-%release
%description voices-id
All voices in Indonesian for GCompris

%package voices-nb
Summary: All voices in Norwegian Bokmal for GCompris
Group: Games/Educational
BuildArch: noarch
Requires: %name = %version-%release
%description voices-nb
All voices in Norwegian Bokmal for GCompris

%package voices-sr
Summary: All voices in Serbian for GCompris
Group: Games/Educational
BuildArch: noarch
Requires: %name = %version-%release
%description voices-sr
All voices in Serbian for GCompris

%package voices-el
Summary: All voices in Greek for GCompris
Group: Games/Educational
BuildArch: noarch
Requires: %name = %version-%release
%description voices-el
All voices in Greek for GCompris

%package voices-br
Summary: All voices in Breton for GCompris
Group: Games/Educational
BuildArch: noarch
Requires: %name = %version-%release
%description voices-br
All voices in Breton for GCompris

%package voices-bg
Summary: All voices in Bulgarian for GCompris
Group: Games/Educational
BuildArch: noarch
Requires: %name = %version-%release
%description voices-bg
All voices in Bulgarian for GCompris

%package voices-ur
Summary: All voices in Urdu for GCompris
Group: Games/Educational
BuildArch: noarch
Requires: %name = %version-%release
%description voices-ur
All voices in Urdu for GCompris

%package voices-he
Summary: All voices in Hebrew for GCompris
Group: Games/Educational
BuildArch: noarch
Requires: %name = %version-%release
%description voices-he
All voices in Hebrew for GCompris

%package voices-pa
Summary: All voices in Punjabi for GCompris
Group: Games/Educational
BuildArch: noarch
Requires: %name = %version-%release
%description voices-pa
All voices in Punjabi for GCompris

%package voices-eo
Summary: All voices in Esperanto for GCompris
Group: Games/Educational
BuildArch: noarch
Requires: %name = %version-%release
%description voices-eo
All voices in Esperanto for GCompris

%package voices-zh_CN
Summary: All voices in Chinese o for GCompris
Group: Games/Educational
BuildArch: noarch
Requires: %name = %version-%release
%description voices-zh_CN
All voices in Chinese for GCompris

%package voices-ast
Summary: All voices in Asturian for GCompris
Group: Games/Educational
BuildArch: noarch
Requires: %name = %version-%release
%description voices-ast
All voices in Asturian for GCompris

%package voices-sl
Summary: All voices in Slovenian for GCompris
Group: Games/Educational
BuildArch: noarch
Requires: %name = %version-%release
%description voices-sl
All voices in Slovenian for GCompris

%package voices-af
Summary: All voices in Afrikaans for GCompris
Group: Games/Educational
BuildArch: noarch
Requires: %name = %version-%release
%description voices-af
All voices in Afrikaans for GCompris

%prep
%setup -q
%patch -p1

#Fix build on x86_64
sed -i "s|br_cv_valid_prefixes=no|br_cv_valid_prefixes=yes|g" acinclude.m4

%build
#autoreconf
./autogen.sh

sed -i "s|LIBADD =|LIBADD = -lgnomecanvas-2 \$(GCOMPRIS_LIBS) \$(XML_LIBS)|g"  src/boards/Makefile.in
sed -i "s|LIBADD =|LIBADD = -lgnomecanvas-2 \$(GCOMPRIS_LIBS) \$(XML_LIBS)|g"  src/boards/Makefile.in

#add_optflags -UGTK_DISABLE_DEPRECATED -UGDK_DISABLE_DEPRECATED
%configure
#	--enable-binreloc

make

%install
make DESTDIR=%buildroot install

mkdir -p %buildroot%_datadir/gcompris/boards/voices
tar -xf %SOURCE10 -C %buildroot%_datadir/gcompris/boards/voices

mkdir -p %buildroot%_miconsdir
mkdir -p %buildroot%_liconsdir
mkdir -p %buildroot%_niconsdir

install -p -m 644 docs/C/*.info %buildroot%_infodir
install -p -m 644 %SOURCE2 %buildroot%_datadir/applications
install -p -m 644 %SOURCE3 %buildroot%_datadir/applications
install -p -m 644 %SOURCE4 %buildroot%_miconsdir/%name.png
install -p -m 644 %SOURCE5 %buildroot%_niconsdir/%name.png
install -p -m 644 %SOURCE6 %buildroot%_liconsdir/%name.png

%find_lang --with-gnome %name
desktop-file-install --dir %buildroot%_desktopdir \
	--remove-category=Utility \
	--add-category=Game \
	--add-category=KidsGame \
	%buildroot%_desktopdir/gcompris-edit.desktop

%files -f %name.lang
%doc AUTHORS COPYING ChangeLog NEWS README

# bin
%_bindir/*

# lib
%_libdir/%name

# menu
##%_menudir/*
%_datadir/applications/*

# data 
%_datadir/%name

#icons
%_datadir/pixmaps/*
%_miconsdir/*
%_liconsdir/*
%_niconsdir/*
##%dir %_datadir/assetml
##%_datadir/assetml/gcompris_flags.assetml

# help
%_infodir/*
%_man6dir/*

# exclude sounds
%exclude %_datadir/gcompris/boards/voices/ar
%exclude %_datadir/gcompris/boards/voices/br
%exclude %_datadir/gcompris/boards/voices/cs
%exclude %_datadir/gcompris/boards/voices/da
%exclude %_datadir/gcompris/boards/voices/de
%exclude %_datadir/gcompris/boards/voices/el
%exclude %_datadir/gcompris/boards/voices/en
%exclude %_datadir/gcompris/boards/voices/es
%exclude %_datadir/gcompris/boards/voices/eu
%exclude %_datadir/gcompris/boards/voices/fi
%exclude %_datadir/gcompris/boards/voices/fr
%exclude %_datadir/gcompris/boards/voices/hi
%exclude %_datadir/gcompris/boards/voices/hu
%exclude %_datadir/gcompris/boards/voices/id
%exclude %_datadir/gcompris/boards/voices/it
%exclude %_datadir/gcompris/boards/voices/mr
%exclude %_datadir/gcompris/boards/voices/nb
%exclude %_datadir/gcompris/boards/voices/nl
%exclude %_datadir/gcompris/boards/voices/pt
%exclude %_datadir/gcompris/boards/voices/pt_BR
%exclude %_datadir/gcompris/boards/voices/ru
%exclude %_datadir/gcompris/boards/voices/so
%exclude %_datadir/gcompris/boards/voices/sr
%exclude %_datadir/gcompris/boards/voices/sv
%exclude %_datadir/gcompris/boards/voices/tr
%exclude %_datadir/gcompris/boards/voices/bg
%exclude %_datadir/gcompris/boards/voices/ur
%exclude %_datadir/gcompris/boards/voices/nn
%exclude %_datadir/gcompris/boards/voices/he
%exclude %_datadir/gcompris/boards/voices/pa
%exclude %_datadir/gcompris/boards/voices/eo
%exclude %_datadir/gcompris/boards/voices/zh_CN
%exclude %_datadir/gcompris/boards/voices/ast
%exclude %_datadir/gcompris/boards/voices/sl
%exclude %_datadir/gcompris/boards/voices/af

%files voices-en
%_datadir/gcompris/boards/voices/en

%files voices-ru
%_datadir/gcompris/boards/voices/ru

%files voices-da
%_datadir/gcompris/boards/voices/da

%files voices-de
%_datadir/gcompris/boards/voices/de

%files voices-es
%_datadir/gcompris/boards/voices/es

%files voices-fr
%_datadir/gcompris/boards/voices/fr

%files voices-it
%_datadir/gcompris/boards/voices/it

%files voices-pt
%_datadir/gcompris/boards/voices/pt

%files voices-sv
%_datadir/gcompris/boards/voices/sv

%files voices-eu
%_datadir/gcompris/boards/voices/eu

%files voices-hu
%_datadir/gcompris/boards/voices/hu

%files voices-fi
%_datadir/gcompris/boards/voices/fi

%files voices-nl
%_datadir/gcompris/boards/voices/nl

%files voices-cs
%_datadir/gcompris/boards/voices/cs

%files voices-mr
%_datadir/gcompris/boards/voices/mr

%files voices-pt_BR
%_datadir/gcompris/boards/voices/pt_BR

%files voices-tr
%_datadir/gcompris/boards/voices/tr

%files voices-so
%_datadir/gcompris/boards/voices/so

%files voices-ar
%_datadir/gcompris/boards/voices/ar

%files voices-hi
%_datadir/gcompris/boards/voices/hi

%files voices-id
%_datadir/gcompris/boards/voices/id

%files voices-nb
%_datadir/gcompris/boards/voices/nb
%_datadir/gcompris/boards/voices/nn

%files voices-sr
%_datadir/gcompris/boards/voices/sr

%files voices-el
%_datadir/gcompris/boards/voices/el

%files voices-br
%_datadir/gcompris/boards/voices/br

%files voices-bg
%_datadir/gcompris/boards/voices/bg

%files voices-ur
%_datadir/gcompris/boards/voices/ur

%files voices-he
%_datadir/gcompris/boards/voices/he

%files voices-pa
%_datadir/gcompris/boards/voices/pa

%files voices-eo
%_datadir/gcompris/boards/voices/eo

%files voices-zh_CN
%_datadir/gcompris/boards/voices/zh_CN

%files voices-ast
%_datadir/gcompris/boards/voices/ast

%files voices-sl
%_datadir/gcompris/boards/voices/sl

%files voices-af
%_datadir/gcompris/boards/voices/af

%changelog
* Mon Jan 09 2012 Slava Dubrovskiy <dubrsl@altlinux.org> 11.12.01-alt1
- Update to 11.12.01 (Bugfix release)

* Thu Dec 22 2011 Slava Dubrovskiy <dubrsl@altlinux.org> 11.12-alt1
- Update to 11.12

* Fri Oct 28 2011 Slava Dubrovskiy <dubrsl@altlinux.org> 11.09-alt1
- Update to 11.09

* Tue May 24 2011 Repocop Q. A. Robot <repocop@altlinux.org> 9.6-alt1.qa1
- NMU (by repocop). See http://www.altlinux.org/Tools/Repocop
- applied repocop fixes:
  * freedesktop-desktop-file-proposed-patch for gcompris
  * postclean-03-private-rpm-macros for the spec file

* Thu Mar 03 2011 Slava Dubrovskiy <dubrsl@altlinux.org> 9.6-alt1
- Update to 9.6
- Add package voices-af (Voice pack for Afrikaans)
- Remove package voices-nn (it's link to nb)

* Mon Dec 06 2010 Slava Dubrovskiy <dubrsl@altlinux.org> 9.4-alt1
- Update to 9.4
- Add package voices-sl (Voice pack for Slovenian)

* Mon Nov 22 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 9.3-alt1.1
- Fixed build

* Fri May 14 2010 Slava Dubrovskiy <dubrsl@altlinux.org> 9.3-alt1
- Update to 9.3
- Add package voices-ast (Voice pack for Asturian by Xandru Armesto Fernandez xandru@softastur.org)

* Tue Feb 16 2010 Slava Dubrovskiy <dubrsl@altlinux.org> 9.2-alt1
- Update to 9.2
- Add patch for diff between alt and upstream branch

* Mon Feb 01 2010 Slava Dubrovskiy <dubrsl@altlinux.org> 9.1-alt2
- Russian translation updates (thanks cas@)

* Mon Jan 25 2010 Slava Dubrovskiy <dubrsl@altlinux.org> 9.1-alt1
- Update to 9.1
- Remove ru.po (in upstream)
- Add package voices-zh_CN (Voice pack for Chinese by Feng Jie)
- Fix bug (ALT #22717)

* Thu Jan 07 2010 Slava Dubrovskiy <dubrsl@altlinux.org> 9.0-alt1
- Update to 9.0
- Switch to git
- Add package voices-eo (voices in Esperanto)
- Translation updates
  + ru.po: updated Russian translation

* Tue Nov 17 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 8.4.13-alt1.1
- Rebuilt with python 2.6

* Tue Oct 20 2009 Slava Dubrovskiy <dubrsl@altlinux.org> 8.4.13-alt1
- Update to 8.4.13

* Wed Aug 26 2009 Slava Dubrovskiy <dubrsl@altlinux.org> 8.4.12-alt2
- Remove gnucap from Requires

* Thu May 07 2009 Slava Dubrovskiy <dubrsl@altlinux.org> 8.4.12-alt1
- Update to 8.4.12
- Delete patch gcompris-8.4.8-alt-fix_sound_memory.patch (in upstream)

* Fri Mar 06 2009 Slava Dubrovskiy <dubrsl@altlinux.org> 8.4.8-alt1
- Update to 8.4.8
- Delete SOURCE7 default-uk.xml (in upstream)
- Add package voices-pa (voices in Punjabi)
- Add Requires: librsvg
- Add patch for fix some sounds in memory game

* Thu Dec 18 2008 Slava Dubrovskiy <dubrsl@altlinux.org> 8.4.7-alt4
- Fix error in spec

* Wed Dec 17 2008 Slava Dubrovskiy <dubrsl@altlinux.org> 8.4.7-alt3
- Remove /usr/lib/menu/gcompris
- Remove depricated update-menus and post_ldconfig

* Fri Oct 17 2008 Slava Dubrovskiy <dubrsl@altlinux.org> 8.4.7-alt2
- Add SOURCE7 default-uk.xml

* Thu Oct 16 2008 Slava Dubrovskiy <dubrsl@altlinux.org> 8.4.7-alt1
- Update to 8.4.7
- Change BuildArch to noarch for voices-* packages

* Fri Aug 15 2008 Slava Dubrovskiy <dubrsl@altlinux.ru> 8.4.6-alt1
- Update to 8.4.6
- Add package voices-he (voices in Hebrew)
- Fixed same bugs
- Fix for repocop tests

* Tue Jun 24 2008 Slava Dubrovskiy <dubrsl@altlinux.org> 8.4.5-alt2
- Fix build on x86_64

* Fri May 16 2008 Slava Dubrovskiy <dubrsl@altlinux.ru> 8.4.5-alt1
- Update to 8.4.5
- Fixed same bugs
- Added mexican geography map by Little_Bear (jorge.diaz on gmail.com)
- Add package voices-nn (voices in Norwegian Nynorsk)

* Fri Feb 15 2008 Slava Dubrovskiy <dubrsl@altlinux.org> 8.4.4-alt1
- Update to 8.4.4
- Add package voices-bg (voices in Bulgarian)
- Add package voices-ur (voices in Urdu)
- Fixed many potential crash of GCompris in the key_press activity callback.
- Ed Montgomery created the canada region map for the geography country activity.
- Now use the voice set from trunk. The sounds are smaller.
- Fixed missing translation in python activity like chat and administration
- Fixed a crash that happens when you click on the image just once it is fully erased

* Wed Feb 06 2008 Slava Dubrovskiy <dubrsl@altlinux.org> 8.4.2-alt5
- Substitute python2.4 with python%__python_version in specfile (thanks bga@)

* Wed Jan 23 2008 Slava Dubrovskiy <dubrsl@altlinux.org> 8.4.2-alt4
- Add Requires: gst-plugins-base >= 0.10.14-alt3
- Add Obsoletes: %name-gst-plugin

* Wed Jan 09 2008 Slava Dubrovskiy <dubrsl@altlinux.org> 8.4.2-alt3
- Remove virtual package %name-gst-plugins
- Add Requires: gst-plugins-base gst-plugins-base-audio-filters gst-plugins-vorbis gst-plugins-ogg gst-plugins-alsa
- Remove autoconf-alt.patch (no need with autoconf_2.60)

* Tue Nov 27 2007 Slava Dubrovskiy <dubrsl@altlinux.org> 8.4.2-alt2
- Update ru.po: (thanks sibskull at gmail.com)
- Update {%name}*.desktop

* Tue Oct 30 2007 Slava Dubrovskiy <dubrsl@altlinux.org> 8.4.2-alt1
- Update to 8.4.2
- Add virtual package %name-gst-plugin
- src/boards/erase.c: (canvas_event): Fixed a crash that happens when
  you click on the image just once it is fully erased (commit 3106)
- src/boards/enumerate.c: (enumerate_create_item): fixed a reference to a
  freed pixmap. It could crash or display broken image in the buttons (commit 3089).
- src/boards/python/redraw.py: fixed a runtime warning
  'DeprecationWarning: integer argument expected, got float' (commit 3079)
- src/gcompris/gcompris.c: (main): fixed again the hack to force
  gnomecanvas symbols not to be stripped. (commit 3078)
- Translation updates:
  + ar.po: Updated Arabic Translation by Djihed Afifi.
  + el.po: Updated Greek translation by Yannis Kaskamanidis 
  + ne.po: Updated Nepali Translation by Pawan Chitrakar

* Fri Oct 26 2007 Slava Dubrovskiy <dubrsl@altlinux.org> 8.4.1-alt1
- Update to 8.4.1
- Add intltoolize --force (thanks ktirf@)
- Add package voices-br (voices in Breton)
- Add Requires: gnucap gst-plugins-base gst-plugins-base-audio-filters gst-plugins-vorbis gst-plugins-ogg gst-plugins-alsa

* Wed Sep 26 2007 Slava Dubrovskiy <dubrsl@altlinux.org> 8.4-alt3
- Update russian translation (by black@)
- Add new SOURCE2 for desktop file (It is translated)

* Thu Sep 20 2007 Slava Dubrovskiy <dubrsl@altlinux.org> 8.4-alt2
- Fix unmet dependencies: add Provides: python2.4(DTW) (#12891)

* Tue Sep 18 2007 Slava Dubrovskiy <dubrsl@altlinux.org> 8.4-alt1
- Update to 8.4
- Update patch %name-%version-autoconf-alt.patch
- Add package voices-sr (voices in Serbian)
- Add package voices-el (voices in Greek)
- Fixed "-l list" option to load the menu list from the base.
  option was not working when boards are compiled statically.
- Now we don't crash if we cannot find a single image at startup.
- Fixed a major bug, target activity is broken, the target never reach it's goal.
- Moved the lock file checking downstairs in the startup
  sequence to avoid for exemple 'gcompris -v' to being locked.
- missingletter: GCompris was asserting when you click on the target image
- Now all voices are in a separated svn module.
  The voices must now be put under boards/voices/<locale> instead of
  boards/sounds/<locale>
- Chronos activity: removed hardcoded translations
- doubleentry: fixed call to audio voices.
- algorithm: Fixed the skip of a level after the call to the help.
- shapegame:
  + Fixed bad reference to hand image to catch small icon
  + fixed, it was missing a X offset coming from
    the box of shapes on the left. It was mostly visible in the doubleentry activity where
    it was not easy to spot the target.
  + use the larger button for the tooltip (country name too large)
  + Translated The Text In Tooltip Were Invalid.
  + Removed text shadow as it isn't always cute depending on the fonts.
- memory: space sound 2 was twice in the list. If they were
  both selected in the game, the children was proposed the same sound
  in 4 spot making the game bugged.
- login: fixed a little bug, in text entry mode
  it was not displayed again if you open/close the help.
- New voices:
  + Added Serbian sounds by Mihailo and Slobodan Simic.
  + New Serbian voices
- Switched GCompris to GPL V3 and Later.
- Translated The Text In shapegame Tooltips Were Invalid
  (i.e, in the geography activity).
- GCompris was asserting when you clicked on the target image in
  missingletter activity.
- sdl_mixer replaced by gstreamer.
- Fixed falling words for arabic
- Internal static gnomecanvas and libart
- The click on letter activity was only proposing the first 4 letters
  of the alphabet, whatever the level.
- Fixed running on machines which
  have / use prefix/lib64 instead of prefix/lib
- Fixed concerns releated to the fullscreen mode
- Fixed the gnuchess search path to accept gnome-gnuchess
- Major fix, GCompris was crashing if you clicked during bonus display

* Mon Apr 30 2007 Slava Dubrovskiy <dubrsl@altlinux.org> 8.3.1-alt1
- Update to 8.3.1
- Add patch %name-%version-autoconf-alt.patch
- Add intltool in BuildPreReq
- Add Obsoletes: %name-devel
- Add package voices-ar (voices in Arabic)
- Add package voices-hi (voices in Indian Hindi)
- Add package voices-id (voices in Indonesian)
- Add package voices-nb (voices in Norwegian)
- New click and draw and draw number activities by Olivier Ponchaut.
- New word processor activity (Bruno)
- Shapes type activities have been reworked by Miguel.
- By Miguel DE IZARRA, added a 2 player mode in connect4.
- Imported sounds from Tuxpaint. Many activities have now many audio effects taken from Tuxpaint.
- New activity by Miguel which replaces the scale activity by a dedicated one (instead of being shape game based).
- Created a new activity, a mini local chat based on multicast. It does not require a server. It does not work on Internet.
- Submarine: reworked this activity to include a goal (a gate on the right and a treasure to catch to open the gate)
- Added a minimal module in the admin to display the log. The module allow to filter by user, sort all columns and reset the log.
- Splitted geography and geography_country
- New top level icons set and bonus from Mathieu Ignacio.
- searace: does instant rotation now. improved the parameters to make it more realistic. Now a straight line won't win all time.
- Fixed skin selection
- Added support for no double instance run. Now by default GCompris won't run again if started less than 30 seconds after a previous one. This can be disable with -nolockcheck

* Mon Dec 11 2006 Slava Dubrovskiy <dubrsl@altlinux.ru> 8.2.2-alt0
- Bug Fix Release 8.2.2
- Add %%autoreconf
- Add package voices-so (voices in Somali)
- Fixed 2 annoying bug in anim/draw:
- It s now easy to move text by using its anchor The DEL key works now. 
  (I just found that the space key doesn't :/)
  + Fixed electricity to work on any gnucap release
  + shape type activity now uses gettext for tittles (missing translation fix)

* Thu Nov 23 2006 Slava Dubrovskiy <dubrsl@altlinux.ru> 8.2.1-alt0
- Bug Fix Release 8.2.1
- Major:
  + Quit of the gnumch or searace activity no more crash GCompris
  + GCompris can save the configuration file,
    even with users having non ascii login name 
- Minor:
  + New interrupt audio mode to have a more reactive experience
    in audio activity. Audio memory and then melody activities
    are now much more pleasant to play (Yves fix on a Markus request).
- Translation updates
  + ar.po: updated arabic translation by Nabil Ben Khalifa
  + mr.po: Updated Marathi by removing fuzzy, per the author request
  + pt_BR.po: Updated by Frederico Goncalves Guimaraes

* Mon Nov 06 2006 Slava Dubrovskiy <dubrsl@altlinux.ru> 8.2-alt0
- Update to 8.2

* Fri Oct 20 2006 Slava Dubrovskiy <dubrsl@altlinux.ru> 8.1-alt1
- fix for build in x86_64 architecture

* Tue Oct 17 2006 Slava Dubrovskiy <dubrsl@altlinux.ru> 8.1-alt0
- Update to 8.1
- Add package voices-cs (voices in Czech)
- Add package voices-mr (voices in Indian Marathi)
- Add package voices-pt_BR (voices in Brasilian)
- Add package voices-tr (voices in Turk)
- Fix #9781

* Wed Apr 12 2006 Slava Dubrovskiy <dubrsl@altlinux.ru> 7.4-alt0
- Update to 7.4
  + Remove alt-makefile.patch (in upstream)
- New menu system by Yves.
- New magic hat activity by Marc Brun
- Awele by Frederic Mazzarol, and reworked by Yves.
- Added memory like activity but based on mathematics 2+2 card matches the 4 card.
- Added command line switch to disable exit and config button. This is usefull to run GCompris on a kiosk.
- Added voices for Dutch by Ivar Snaaijer (Ivar at Snaaijer nl)
- 2 new background scenery images by Herve CHANAL
- 2 New animals by Anne and Erwan for the erase activity.
- fix [ 1451703 ] Learning Clock without refresh in time window
- Changed the internal help to use a GTK textview with a scrollbar.
- Now erase has 10 sublevels to let small children play longer at the same level
- Now sudoku has a new level 5x5 with numbers.

* Tue Mar 28 2006 Slava Dubrovskiy <dubrsl@altlinux.ru> 7.4.0BETA2-alt0
- Update to 7.4.0BETA2
- Add package voices-nl (voices in Dutch)
- Update patch for src/gcompris/Makefile.in

* Sun Mar 19 2006 Slava Dubrovskiy <dubrsl@altlinux.ru> 7.3.2-alt1
- Added patch for src/gcompris/Makefile.in (fix --as-needed)
- Replace make_build to __make for SMP-compatible build

* Thu Mar 02 2006 Slava Dubrovskiy <dubrsl@altlinux.ru> 7.3.2-alt0
- Update to 7.3.2
  + Remove fix in src/gcompris/soundutil.c from dapper.patch (in upstream)
- Add package voices-fi (voices in Finish)
- Remove %buildroot%_menudir/%name files

* Mon Feb 20 2006 Slava Dubrovskiy <dubrsl@altlinux.ru> 7.3-alt0
- Update to 7.3
  + New activity, drive the crane and copy the model by Marc BRUN
  + New activity electricity by Bruno. It is based on the gnucap engine
  + New menu organization by Yves Combe
  + Better graphism by Franck Doucet
- Add fix in src/gcompris/soundutil.c from dapper.patch

* Thu Nov 24 2005 Slava Dubrovskiy <dubrsl@altlinux.ru> 7.2-alt0
- Update to 7.2
- Remove Requires for gnome-libs (#8564)
- Add package voices-hu (voices in Hungarian)

* Wed Nov 02 2005 Slava Dubrovskiy <dubrsl@altlinux.ru> 7.1PRE1-alt1
- Update to 7.1PRE1
- Add new SOURCE1 for ru.po (It is completely translated)
- Add package voices-eu (voices in Basque)

* Thu Oct 13 2005 Slava Dubrovskiy <dubrsl@altlinux.ru> 7.0.3-alt1
- Update to 7.0.3

* Mon Oct 10 2005 Slava Dubrovskiy <dubrsl@altlinux.ru> 7.0.2-alt1
- Update to 7.0.2
  + Add BuildRequires: python-module-PyXML, python-module-pygnome-devel >= 2.9.0 python-module-pysqlite2 libpng3-devel
  + Add Requires: python-module-pysqlite2
  + Remove all path & add %__subst "s|import gnome.canvas|import gnomecanvas|g" src/boards/python.c

* Tue May 17 2005 Slava Dubrovskiy <dubrsl@altlinux.ru> 6.5.3-alt1
- Are allocated in packages of a voice for Danish, German, Spanish, French, Italian, Portuguese, Swedish languages
- Fix bug in menu file
- Added postun_ldconfig & post_ldconfig
- Some spec cleanup
- Added Russian summary

* Tue May 10 2005 Slava Dubrovskiy <dubrsl@altlinux.ru> 6.5.3-alt0
- Final build for Sisyphus

* Mon May 9 2005 Guest007 <guest007@gmail.com>
- initial build 4 Sisyphus
- dedicated for Victory Day
