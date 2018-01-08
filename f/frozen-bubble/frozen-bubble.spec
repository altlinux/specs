Name: frozen-bubble
Version: 2.2.0
Release: alt4

Summary: Frozen Bubble arcade game
License: GPL
Group: Games/Arcade

Url: http://www.frozen-bubble.org/
Source: %name-%version.tar
Patch: %name-%version-%release.patch

Requires: %name-data = %version

# Automatically added by buildreq on Sun Oct 16 2011 (-bi)
BuildRequires: libSDL_mixer-devel libSDL_pango-devel perl-Locale-gettext perl-Math-Complex perl-SDL_Perl perl-devel

Summary(ru_RU.UTF-8): игра Frozen Bubble

%description
Colorful 3D rendered penguin animations, 100 levels of 1p game,
hours and hours of 2p game, nights and nights of 2p/3p/4p/5p game
over LAN or Internet, a level-editor, 3 professional quality
digital soundtracks, 15 stereo sound effects, 8 unique graphical
transition effects, 8 unique logo eye-candies.

%description -l ru_RU.UTF-8
Цветные мультяшные пингвины, 100 уровней однопользовательской игры,
многие часы игры вдвоём, долгие ночи двух-пятипользовательской игры
по локальной сети или через интернет, редактор уровней, три дорожки
звукового сопровождения профессионального качества, 15 стереоэффектов,
8 уникальных эффектов графического перехода и 8 просто красивостей.

%prep
%setup
%patch -p1

%build
cd c_stuff
%perl_vendor_build MAKEFILE=Makefile

%install
mkdir -p %buildroot{%_bindir,%_man6dir,%_datadir/%name,%_desktopdir}
install -pm755 %name %name-editor %buildroot%_bindir
install -pm644 doc/%name.6 doc/%name-editor.6 %buildroot%_man6dir
cp -a data gfx snd %buildroot%_datadir/%name

cat <<EOF >%buildroot%_desktopdir/%name.desktop
[Desktop Entry]
Type=Application
Encoding=UTF-8
Name=Frozen Bubble
TryExec=frozen-bubble
Exec=frozen-bubble
Categories=Application;Game;ArcadeGame
Icon=/usr/share/icons/hicolor/48x48/apps/frozen-bubble.png
Comment=Frozen Bubble Arcade Game
Comment[ru]=Игра Frozen Bubble
EOF

install -pDm644 icons/%name-icon-16x16.png %buildroot%_miconsdir/%name.png
install -pDm644 icons/%name-icon-32x32.png %buildroot%_niconsdir/%name.png
install -pDm644 icons/%name-icon-48x48.png %buildroot%_liconsdir/%name.png

cd c_stuff
%perl_vendor_install

%files
%doc README AUTHORS TIPS NEWS
%_bindir/%name
%_bindir/%name-editor
%_man6dir/%name.6*
%_man6dir/%name-editor.6*
%_desktopdir/%name.desktop
%_niconsdir/*.png
%_miconsdir/*.png
%_liconsdir/*.png
%perl_vendor_archlib/*.pm
%perl_vendor_autolib/fb_c_stuff

%package data
Summary: Frozen Bubble arcade game
Group: Games/Arcade
Conflicts: %name < %version
BuildArch: noarch

%description data
Colorful 3D rendered penguin animations, 100 levels of 1p game,
hours and hours of 2p game, nights and nights of 2p/3p/4p/5p game
over LAN or Internet, a level-editor, 3 professional quality
digital soundtracks, 15 stereo sound effects, 8 unique graphical
transition effects, 8 unique logo eye-candies.

%files data
%dir %_datadir/%name
%_datadir/%name/data
%_datadir/%name/gfx
%_datadir/%name/snd

# TODO:
# - package server
# - package locales

%changelog
* Mon Jan 08 2018 Michael Shigorin <mike@altlinux.org> 2.2.0-alt4
- E2K: added openbsd clang patch
- added Russian descriptions (closes: #33776)
- minor spec cleanup

* Fri Dec 15 2017 Igor Vlasenko <viy@altlinux.ru> 2.2.0-alt3.2.1.1
- rebuild with new perl 5.26.1

* Fri Feb 03 2017 Igor Vlasenko <viy@altlinux.ru> 2.2.0-alt3.2.1
- rebuild with new perl 5.24.1

* Tue Jun 14 2016 Igor Vlasenko <viy@altlinux.ru> 2.2.0-alt3.2
- preparing for perl-SDL rename

* Wed Nov 25 2015 Igor Vlasenko <viy@altlinux.ru> 2.2.0-alt3.1.1
- rebuild with new perl 5.22.0

* Tue Dec 09 2014 Igor Vlasenko <viy@altlinux.ru> 2.2.0-alt3.1
- rebuild with new perl 5.20.1

* Fri Aug 30 2013 Vladimir Lettiev <crux@altlinux.ru> 2.2.0-alt3
- built for perl 5.18

* Tue Sep 04 2012 Vladimir Lettiev <crux@altlinux.ru> 2.2.0-alt2
- rebuilt for perl-5.16

* Sun Oct 16 2011 Alexey Tourbin <at@altlinux.ru> 2.2.0-alt1.2
- rebuilt for perl-5.14

* Sun Nov 07 2010 Vladimir Lettiev <crux@altlinux.ru> 2.2.0-alt1.1
- rebuilt with perl 5.12

* Fri Feb 19 2010 Alexey Tourbin <at@altlinux.ru> 2.2.0-alt1
- 2.1.0 -> 2.2.0
- split %name-data noarch package

* Wed Feb 03 2010 Repocop Q. A. Robot <repocop@altlinux.org> 2.1.0-alt2.qa1
- NMU (by repocop): the following fixes applied:
  * update_menus for frozen-bubble
  * pixmap-in-deprecated-location for frozen-bubble
  * postclean-05-filetriggers for spec file

* Thu Dec 14 2006 Pavlov Konstantin <thresh@altlinux.ru> 2.1.0-alt2
- Fixed .desktop file.

* Tue Nov 28 2006 Pavlov Konstantin <thresh@altlinux.ru> 2.1.0-alt1
- 2.1.0 release.

* Sat Nov 18 2006 Pavlov Konstantin <thresh@altlinux.ru> 2.0.0-alt3
- Fixed @LIBDIR@ in fb_stuff.pm.

* Thu Nov 09 2006 Pavlov Konstantin <thresh@altlinux.ru> 2.0.0-alt2
- Packager changed.
- Cleaned up spec file a bit.
- Added freedesktop menu.

* Mon Oct 30 2006 Pavlov Konstantin <thresh@altlinux.ru> 2.0.0-alt1
- 2.0.0 release.
- Removed patch for SDL_Perl-2.x.
- Changed Source URL.
- Altered BuildRequires.
- New Description.

* Fri Feb 04 2005 Alexey Tourbin <at@altlinux.ru> 1.0.0-alt5
- ported to SDL_Perl-2.x API
- abandoned Makefile, reworked specfile

* Fri May 07 2004 Alexey Voinov <voins@altlinux.ru> 1.0.0-alt4
- removed gimp-perl from buildreqs
- little spec cleaun up
- man pages included

* Tue Oct 14 2003 Alexey Tourbin <at@altlinux.ru> 1.0.0-alt3
- unnecessary files removed along with dependencies (#3159)

* Tue Sep 30 2003 Alexey Tourbin <at@altlinux.ru> 1.0.0-alt2
- fixed build (Makefile workarounds)
- specfile cleanup

* Mon Feb 24 2003 Rider <rider@altlinux.ru> 1.0.0-alt1
- 1.0.0

* Thu Jan 09 2003 Konstantin Volckov <goldhead@altlinux.ru> 0.9.3-alt4
- Fixed menu file

* Thu Oct 31 2002 Konstantin Volckov <goldhead@altlinux.ru> 0.9.3-alt3
- Rebuilt with new perl
- Fixed icons permissions

* Thu Oct 24 2002 Konstantin Volckov <goldhead@altlinux.ru> 0.9.3-alt2
- Rebuilt in new environment

* Fri Jun 07 2002 Konstantin Volckov <goldhead@altlinux.ru> 0.9.3-alt1
- 0.9.3
- Remove internal libSDL_mixer
- Remove fixed packager

* Tue Mar 05 2002 Alexander Bokovoy <ab@altlinux.ru> 0.9.2-alt1
- Initial build for ALT Linux

* Thu Feb  7 2002 Guillaume Cottenceau <gc@mandrakesoft.com> 0.9.2-1mdk
- new version

* Wed Feb  6 2002 Guillaume Cottenceau <gc@mandrakesoft.com> 0.9.1-1mdk
- first mdk rpm

