Name: kiki
Version: 1.0.2
Release: alt1.qa4.1

Group: Games/Puzzles
Summary: 3D logical game
Summary(ru_RU.UTF-8): Логическая 3D игра
License: Public Domain
Url: http://kiki.sf.net
Icon: kiki.32.png
Packager: Ilya Mashkin <oddity@altlinux.ru>
Source0: %name-%version.tar
Source1: %name.16.png
Source2: %name.32.png
Source3: %name.48.png
Source4: %name-manual.tar.bz2
Patch01: %name-%version-alt.patch

# due to .desktop
Requires: /usr/bin/sound_wrapper

# Automatically added by buildreq on Mon Nov 17 2008
BuildRequires: gcc-c++ libGL-devel libSDL-devel libSDL_image-devel libSDL_mixer-devel libfreeglut-devel python-devel vorbis-tools

%description
    once upon a time,
    there were some
    tiny little robots
    living in the nano world.

    they lived a happy artificial life
    busily collecting resources
    for the maker
    who made more and more
    tiny little robots.

    but one day,
    a parasitic capacity
    destroyed the maker's
    master control program.

    since then he is
    malfunctioning
    and only producing
    lazy stupid little robots
    which shoot each other
    and destroy the nano world.

    your task is to help kiki,
    the only sane bot left over,
    to repair the maker.

Kiki is 3D logical game.  To solve the game, you have to complete
several levels. Every level has it's own task.
Pressing ESC will display a menu with a 'help' item which explains
what you have to do in order to fulfill this task.
Once you managed to fulfill the task, the exit gate will be activated.
If kiki moves through the activated exit gate, it will be 'beamed' to
the next level.

%description -l ru_RU.UTF-8
Кики это логическая 3D игра. Для её прохождения требуется завершить
каждый из предлагаемых уровней. Каждый уровень имеет задание, которое
можно узнать нажав ESC и выбрав ПОМОЩЬ во время игры. Как только
задание выполнено, будут активированы врата. Пройдя через них, Кики
переходит на следующий уровень.

Кики представляет собой небольшого робота, перемещающегося в замкнутом
пространстве. Робот может прыгать, стрелять, двигать блоки,
передвигаться по полу, стенам и потолку (если таковые можно выделить).

%add_python_compile_exclude /usr/share/games/kiki/py
%add_python_req_skip _kiki

%prep
%setup -q
%patch01 -p1
sed -i -e 's,^PYTHON_VERSION=.*$,PYTHON_VERSION=%__python_version,g' linux/Makefile

%build
pushd kodilib/linux
%make_build
popd
pushd linux
%make_build
popd

oggenc sound/*.wav


%install
mkdir -p %buildroot/%_gamesbindir
mkdir -p %buildroot/%_gamesdatadir
mkdir -p %buildroot/%_gamesdatadir/%name
cp -r py sound %buildroot/%_gamesdatadir/%name
rm -f %buildroot/%_gamesdatadir/%name/sound/*.wav
rm -f %buildroot/%_gamesdatadir/%name/*.pyo
rm -f %buildroot/%_gamesdatadir/%name/*.pyc
cp linux/kiki %buildroot/%_gamesbindir/kiki.bin

cat > %buildroot/%_gamesbindir/%name <<EOF
#!/bin/sh
export KIKI_HOME=%_gamesdatadir/%name
%_gamesbindir/kiki.bin
EOF
chmod a=rx %buildroot/%_gamesbindir/%name

mkdir -p %buildroot%_desktopdir
cat > %buildroot%_desktopdir/%{name}.desktop <<EOF
[Desktop Entry]
Version=1.0
Type=Application
Name=Kiki
Comment=3D logical game
Comment[ru]=�~[оги�~Gеская 3D игра
Icon=%{name}
#Exec=%_gamesbindir/%name
Exec=sound_wrapper %_gamesbindir/%name
Terminal=false
Categories=Game;LogicGame;
EOF

mkdir -p %buildroot/{%_miconsdir,%_liconsdir,%_niconsdir}
install -m 644 %SOURCE1 %buildroot/%_miconsdir/%name.png
install -m 644 %SOURCE2 %buildroot/%_niconsdir/%name.png
install -m 644 %SOURCE3 %buildroot/%_liconsdir/%name.png

tar -jxvf %SOURCE4

%files
%_gamesbindir/%name
%_gamesbindir/%name.bin
%_desktopdir/%{name}.desktop
%_gamesdatadir/%name
%_miconsdir/%name.png
%_niconsdir/%name.png
%_liconsdir/%name.png
%doc Readme.txt Thanks.txt manual

%changelog
* Sat Oct 22 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.0.2-alt1.qa4.1
- Rebuild with Python-2.7

* Tue Apr 12 2011 Igor Vlasenko <viy@altlinux.ru> 1.0.2-alt1.qa4
- NMU: .desktop files should use /usr/bin/sound_wrapper

* Fri Apr 08 2011 Igor Vlasenko <viy@altlinux.ru> 1.0.2-alt1.qa3
NMU: polished desktop file

* Fri Jan 15 2010 Repocop Q. A. Robot <repocop@altlinux.org> 1.0.2-alt1.1.qa1
- NMU (by repocop): the following fixes applied:
  * pixmap-in-deprecated-location for kiki
  * postclean-05-filetriggers for spec file

* Thu Nov 12 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.2-alt1.1
- Rebuilt with python 2.6

* Mon Nov 17 2008 Anton Farygin <rider@altlinux.ru> 1.0.2-alt1
- new version
    - patches added from debian
    - localization ported from 0.9.0

* Thu Sep 25 2008 Ilya Mashkin <oddity@altlinux.ru> 0.9.0-alt12.2
- rebuild

* Fri Feb 01 2008 Grigory Batalov <bga@altlinux.ru> 0.9.0-alt12.1
- Rebuilt with python-2.5.

* Tue Jan 22 2008 Grigory Batalov <bga@altlinux.ru> 0.9.0-alt12
- Remove python version from BuildRequires.
- Set current python version in kiki/linux/Makefile.

* Mon May 15 2006 Gleb Stiblo <ulfR@altlinux.ru> 0.9.0-alt11
- kiki-gcc4.1.patch

* Wed Mar 16 2005 Gleb Stiblo <ulfR@altlinux.ru> 0.9.0-alt10
- fixed bug for utf-8
- python 2.4 in build depends

* Tue Dec 21 2004 Gleb Stiblo <ulfR@altlinux.ru> 0.9.0-alt9
- Games to Amusement changed in menu

* Mon Jul 12 2004 Gleb Stiblo <ulfR@altlinux.ru> 0.9.0-alt8
- fixed menu

* Mon May 24 2004 Gleb Stiblo <ulfR@altlinux.ru> 0.9.0-alt7
- recompile due to new python building scheme

* Thu May 20 2004 Gleb Stiblo <ulfR@altlinux.ru> 0.9.0-alt6
- python23-devel changed to python-devel

* Mon May 03 2004 Gleb Stiblo <ulfr@altlinux.ru> 0.9.0-alt5
- glibc 2.3 build

* Wed Mar 31 2004 Gleb Stiblo <ulfr@altlinux.ru> 0.9.0-alt4
- nl_langinfo used now for choosing charset

* Tue Mar 09 2004 Gleb Stiblo <ulfr@altlinux.ru> 0.9.0-alt3
- typo in russian description fixed

* Thu Mar 04 2004 Gleb Stiblo <ulfr@altlinux.ru> 0.9.0-alt2
- russian and byelorussian translation. Only help in english now.
- getwd changed to getcwd

* Tue Feb 17 2004 Gleb Stiblo <ulfr@altlinux.ru> 0.9.0-alt1
- ALT adaptations.

