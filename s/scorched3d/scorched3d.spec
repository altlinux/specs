%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1
%set_verify_elf_method strict

%set_automake_version 1.11

%define lang_path 	./data/lang
%define data_path 	./data
%define ru_tips 	%lang_path/tips_RU.txt
%define ru_tutor 	%lang_path/tutorial_RU.xml
%define ru_lang_res 	%lang_path/lang_RU.resource

Name:    scorched3d
Version: 44
Release: alt2
License: GPL
Group:   Games/Arcade
Summary: A 3D version of the classic DOS game Scorched Earth
Summary(ru_RU.UTF8): 3D версия классической DOS игрушки - Scorched Earth.
URL: http://www.scorched3d.co.uk

Source: %name-%version.tar
Source1: %name.desktop
Source2: %name-16.png
Source3: %name-32.png
Source4: %name-48.png

Patch1: configure.ac.patch
Patch2: %name-%version-fedora-help.patch
Patch3: %name-%version-fedora-system-lua.patch
Patch4: %name-%version-fedora-syslibs.patch
Patch5: %name-%version-fedora-returntype.patch
Patch6: %name-%version-alt-thumbsdb.patch
Patch7: %name-%version-alt-wxGTK-compat.patch

BuildRequires: gcc-c++ libGL-devel libSDL-devel libSDL_net-devel
BuildRequires: libexpat-devel libfftw3-devel libjpeg-devel
BuildRequires: libopenal-devel libpango-devel libpng-devel
BuildRequires: libvorbis-devel libwxGTK3.0-devel libogg-devel
BuildRequires: libalut-devel hd2u findutils
BuildRequires: liblua-devel libGLEW-devel

Requires: %name-data = %EVR

%description
Scorched 3D is a game based loosely on the classic DOS game Scorched
Earth "The Mother Of All Games".

%description -l ru_RU.UTF-8
Scorched 3D — компьютерная игра, римейк пошаговой артиллерийской стратегии Scorched Earth.
Игра полностью переработана на трёхмерную графику. В отличии от оригинальной Scorched Earth,
которая является shareware-игрой, Scorched 3D является полностью бесплатной и распостраняется на
условиях лицензии GNU. Играть можно против компьютерного соперника или по сети. Присутствует также
коллективная игра, за одним компьютером могут играть до 24 игрока. (c) wiki

%package data
Summary: Data files for Scorched 3D
Group: Games/Arcade
BuildArch: noarch

%description data
Scorched 3D is a game based loosely on the classic DOS game Scorched
Earth "The Mother Of All Games".

This package contains data files for Scorched 3D.

%prep
%setup -n scorched
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p0
%patch6 -p3
%patch7 -p3

# ensure we use the system versions of these
rm -f src/common/common/snprintf.c
rm -f src/common/lua/l*.{cpp,h}
rm -f src/common/lua/print.cpp

%build
%add_optflags -D_FILE_OFFSET_BITS=64

/bin/touch {INSTALL,AUTHORS,COPYING,ChangeLog,NEWS}
export OPENAL_CONFIG=%_bindir/openal-config
export FREEALUT_CONFIG=%_bindir/freealut-config

#repocop Thumbs.db
find \( -name 'Thumbs.db' -o -name 'Thumbs.db.gz' \) -print -delete

echo RU > %lang_path/language.ini
dos2unix %ru_tips
dos2unix %ru_tutor
dos2unix %ru_lang_res

%autoreconf
%configure \
	--bindir=%_gamesbindir \
	--datadir=%_gamesdatadir/%name \
	--libdir=%_libdir \
	--with-wx=%prefix \
	--with-wx-config=%_bindir/wx-config \
	--with-vorbis=%prefix \
	--with-fftw=%prefix \
	--with-sdl=%prefix \
	--with-gl=%prefix

%make_build

%install
%makeinstall_std
%make_install DESTDIR="%buildroot/" install
install -pD -m644 %SOURCE1 %buildroot%_desktopdir/%name.desktop
install -pD -m644 %SOURCE2 %buildroot%_miconsdir/%name.png
install -pD -m644 %SOURCE3 %buildroot%_niconsdir/%name.png
install -pD -m644 %SOURCE4 %buildroot%_liconsdir/%name.png

%files
%_gamesbindir/scorched3d*
%_miconsdir/%name.png
%_niconsdir/%name.png
%_liconsdir/%name.png
%_desktopdir/%name.desktop
%doc AUTHORS README documentation/*

%files data
%_gamesdatadir/*

%changelog
* Mon Oct 04 2021 Aleksei Nikiforov <darktemplar@altlinux.org> 44-alt2
- Rebuilt with new wxGTK.

* Wed Sep 20 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 44-alt1
- Updated to upstream version 44.

* Thu Nov 28 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 43.3d-alt2.2
- Fixed build

* Mon Oct 08 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 43.3d-alt2.1
- Rebuilt with libpng15

* Tue Jun 26 2012 Evgeny V Shishkov <shev@altlinux.org> 43.3d-alt2
- Fix linking

* Wed Mar 21 2012 Evgeny V Shishkov <shev@altlinux.org> 43.3d-alt1
- 43.3d

* Wed Dec 08 2010 Evgeny V. Shishkov <shev@altlinux.org> 43.2a-alt1
- 43.2a

* Tue Nov 30 2010 Evgeny V. Shishkov <shev@altlinux.org> 43.2-alt1
- 43.2

* Wed May 05 2010 Evgeny V. Shishkov <shev@altlinux.org> 43.1c-alt1
- 43.1c

* Mon Apr 26 2010 Evgeny V. Shishkov <shev@altlinux.org> 43.1b-alt1
- new version
- Russian language

* Sun Mar 21 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 43-alt02.svn20100317.1
- Exctacted data files into separate package


* Sat Mar 20 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 43-alt02.svn20100317
- Version 43, beta 2, snapshot from upstream svn

* Tue Mar 09 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 42.1-alt1.1
- Rebuilt with wxGTK 2.8

* Tue Mar 03 2009 Evgeny V. Shishkov <shev@altlinux.org> 42.1-alt1
- version 42.1
- removed scorched3d-42-gcc43.patch

* Wed Feb 25 2009 Evgeny V. Shishkov <shev@altlinux.org> 42-alt1
- version 42
- add scorched3d-42-gcc43.patch
- updated build requires
- updated .spec file

* Tue Jan 29 2008 Eugene V. Horohorin <genix@altlinux.ru> 41.3-alt1
- 41.3

* Mon Jan 14 2008 Eugene V. Horohorin <genix@altlinux.ru> 41.2-alt1
- 41.2

* Mon Nov 12 2007 Eugene V. Horohorin <genix@altlinux.ru> 41.1-alt1
- 41.1

* Tue Oct 16 2007 Eugene V. Horohorin <genix@altlinux.ru> 41-alt1
- 41
- removed unused patches
- updated build requires

* Thu Mar 22 2007 Eugene V. Horohorin <genix@altlinux.ru> 40.1d-alt1
- 40.1d
- fix/rebuild with freealut

* Fri Dec 22 2006 Eugene V. Horohorin <genix@altlinux.ru> 40.1-alt2
- rebuild with wxGTK2u

* Sun Oct 29 2006 Eugene V. Horohorin <genix@altlinux.ru> 40.1-alt1
- 40.1

* Mon Aug 21 2006 Eugene V. Horohorin <genix@altlinux.ru> 40-alt1
- 40

* Thu Dec 15 2005 LAKostis <lakostis at altlinux.ru> 39.1-alt0.cvs20050929
- NMU.
- rebuild with wxGTK2.
- CVS snapshot 20050929 from Debian.
- x86_64 build fixes.

* Tue Oct 18 2005 Eugene V. Horohorin <genix@altlinux.ru> 39-alt2
- scorched3d-aspect.patch added
- zlib static removed #8246

* Sat Aug 13 2005 Eugene V. Horohorin <genix@altlinux.ru> 39-alt1
- new version

* Fri Apr 01 2005 Eugene V. Horohorin <genix@altlinux.ru> 38.1-alt1
- new version

* Tue Dec 28 2004 Eugene V. Horohorin <genix@altlinux.ru> 38-alt1
- new version

* Tue Oct 26 2004 Eugene V. Horohorin <genix@altlinux.ru> 37-alt2
- menu file group fix

* Sat Sep 25 2004 Eugene V. Horohorin <genix@altlinux.ru> 37-alt1
- First build.

