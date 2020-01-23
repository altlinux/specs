Name: freedink
Version: 109.6
Release: alt1
Summary: Adventure and role-playing game
Group: Games/Adventure
#BuildRequires: fontconfig-devel libffi-devel gcc-c++
License: GPLv3+
Url: http://www.freedink.org/
Source: %name-%version.tar.gz

Requires: freedink-engine = %version-%release  freedink-dfarc freedink-data

# Automatically added by buildreq on Thu Jan 23 2020
# optimized out: fontconfig glib2-devel glibc-kernheaders-generic glibc-kernheaders-x86 gnu-config libSDL2-devel libfreetype-devel libstdc++-devel pkg-config python2-base sh4
BuildRequires: fontconfig-devel gcc-c++ help2man libSDL2_gfx-devel libSDL2_image-devel libSDL2_mixer-devel libSDL2_ttf-devel libglm-devel

%description
Dink Smallwood is an adventure/role-playing game, similar to Zelda,
made by RTsoft. Besides twisted humour, it includes the actual game
editor, allowing players to create hundreds of new adventures called
Dink Modules or D-Mods for short.

GNU FreeDink is a new and portable version of the game engine, which
runs the original game as well as its D-Mods, with close
compatibility, under multiple platforms.

This package is a metapackage to install the game, its data and a
front-end to manage game options and D-Mods.

%package engine
Summary: Adventure and role-playing game (engine)
Group: Games/Adventure
Requires: freedink-data

%description engine
Dink Smallwood is an adventure/role-playing game, similar to Zelda,
made by RTsoft. Besides twisted humour, it includes the actual game
editor, allowing players to create hundreds of new adventures called
Dink Modules or D-Mods for short.

GNU FreeDink is a new and portable version of the game engine, which
runs the original game as well as its D-Mods, with close
compatibility, under multiple platforms.

This package contains the game engine alone.

%prep
%setup
sed -i 's@SDL_SetHint(SDL_HINT_ANDROID_SEPARATE_MOUSE_AND_TOUCH, "0");@@' src/input.cpp
# RPM/BUILD/freedink-109.6/src/input.cpp:  SDL_SetHint(SDL_HINT_ANDROID_SEPARATE_MOUSE_AND_TOUCH, "0");

%build
# Using '--disable-embedded-resources' because 'rpmbuild' will remove
# them anyway (so it can make the -debuginfo package -- too bad :/)
%configure --disable-embedded-resources --disable-tests
%make

%install
%makeinstall
%find_lang %name
%find_lang %name-gnulib
# %files only support one '-f' argument (see below)
cat %name-gnulib.lang >> %name.lang

%files
%files engine -f %name.lang
%doc AUTHORS COPYING NEWS README THANKS TROUBLESHOOTING ChangeLog
%_bindir/*
%_datadir/applications/*
%_datadir/%name/
%_datadir/pixmaps/*
%_mandir/man6/*
%_iconsdir/hicolor/scalable/apps/freedink.svg
%_datadir/metainfo/freedink.appdata.xml

%changelog
* Thu Jan 23 2020 Fr. Br. George <george@altlinux.ru> 109.6-alt1
- Autobuild version bump to 109.6
- Switch to SDL2

* Thu Dec 11 2014 Fr. Br. George <george@altlinux.ru> 108.4-alt2
- Rebuild with new SDL

* Thu Oct 23 2014 Fr. Br. George <george@altlinux.ru> 108.4-alt1
- Autobuild version bump to 108.4
- Fix buildreq

* Mon Jun 09 2014 Fr. Br. George <george@altlinux.ru> 108.2-alt1
- Autobuild version bump to 108.2

* Mon Dec 17 2012 Fr. Br. George <george@altlinux.ru> 1.08.20121209-alt1
- Autobuild version bump to 1.08.20121209

* Mon May 24 2010 Fr. Br. George <george@altlinux.ru> 1.08.20100420-alt1
- Version up

* Thu Sep 24 2009 Fr. Br. George <george@altlinux.ru> 1.08.20090918-alt1
- Initial build from FC

* Fri Sep 18 2009 Sylvain Beucler <beuc@beuc.net> - 1.08.20090918-1
- New upstream release

* Wed Sep 16 2009 Sylvain Beucler <beuc@beuc.net> - 1.08.20090916-1
- New upstream release
- Can optionaly bundle default font, to avoid liberation-fonts
  vs. liberation-sans-fonts issues when building snapshot RPMs

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.08.20090120-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.08.20090120-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Wed Feb 04 2009 Sylvain Beucler <beuc@beuc.net> - 1.08.20090120-2
- Apply Fedora font rename: liberation-fonts -> liberation-sans-fonts

* Tue Jan 20 2009 Sylvain Beucler <beuc@beuc.net> - 1.08.20090120-1
- New upstream release (fix engine freeze in some DinkC scripts)

* Fri Jan 09 2009 Sylvain Beucler <beuc@beuc.net> - 1.08.20090109-2
- Bump version to fix build tag issue

* Fri Jan 09 2009 Sylvain Beucler <beuc@beuc.net> - 1.08.20090109-1
- New upstream release
- Declare .mo translation catalogs

* Sun Oct 05 2008 Sylvain Beucler <beuc@beuc.net> - 1.08.20080920-4
- Use liberation-fonts in all distro versions

* Wed Sep 24 2008 Sylvain Beucler <beuc@beuc.net> - 1.08.20080920-3
- Don't use 'update-desktop-database' for simple desktop files
- Fix unescaped macros in comments
- Use spaces around '=' in version-specific dependency

* Wed Sep 24 2008 Sylvain Beucler <beuc@beuc.net> - 1.08.20080920-2
- Fix variable s/fedora_version/fedora/
- Meta-package depends on same version of freedink-engine
- Use "install -p" to preserve timestamps
- Validate installed .desktop files

* Sat Sep 20 2008 Sylvain Beucler <beuc@beuc.net> - 1.08.20080920-1
- New upstream release

* Thu Aug 28 2008 Sylvain Beucler <beuc@beuc.net> - 1.08.20080828-1
- Initial package
