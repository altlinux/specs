Name: freedink
Version: 1.08.20100420
Release: alt1
Summary: Adventure and role-playing game
Group: Games/Adventure
#BuildRequires: fontconfig-devel libffi-devel gcc-c++
License: GPLv3+
Url: http://www.freedink.org/
Source: ftp://ftp.gnu.org/gnu/freedink/freedink-%version.tar.gz
Packager: Fr. Br. George <george@altlinux.ru>

Requires: freedink-engine = %version-%release  freedink-dfarc freedink-data

# Automatically added by buildreq on Wed Sep 23 2009
BuildRequires: fontconfig-devel help2man libSDL-devel libSDL_gfx-devel libSDL_image-devel libSDL_mixer-devel libSDL_ttf-devel

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
%setup -q

%build
# Using '--disable-embedded-resources' because 'rpmbuild' will remove
# them anyway (so it can make the -debuginfo package -- too bad :/)
%configure --disable-embedded-resources
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

%changelog
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

* Wed Feb  4 2009 Sylvain Beucler <beuc@beuc.net> - 1.08.20090120-2
- Apply Fedora font rename: liberation-fonts -> liberation-sans-fonts

* Tue Jan 20 2009 Sylvain Beucler <beuc@beuc.net> - 1.08.20090120-1
- New upstream release (fix engine freeze in some DinkC scripts)

* Wed Jan  9 2009 Sylvain Beucler <beuc@beuc.net> - 1.08.20090109-2
- Bump version to fix build tag issue

* Wed Jan  9 2009 Sylvain Beucler <beuc@beuc.net> - 1.08.20090109-1
- New upstream release
- Declare .mo translation catalogs

* Sun Oct  5 2008 Sylvain Beucler <beuc@beuc.net> - 1.08.20080920-4
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
