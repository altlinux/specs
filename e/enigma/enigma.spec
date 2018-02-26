Name: enigma
Version: 1.01
Release: alt5
Summary: Find and uncover all pairs of identical Oxyd stones in each landscape
License: GPL
Group: Games/Arcade

Packager: Ilya Mashkin <oddity@altlinux.ru>
Url: http://www.nongnu.org/enigma/
Source0: %name-%version.tar.bz2
Patch1:         enigma-gcc-4.3-ftbfs.patch
Patch2:         enigma-gcc-4.4-ftbfs.patch
Patch3:         enigma-consts.patch

# Automatically added by buildreq on Fri Jan 05 2007
BuildRequires: esound gcc-c++ libpng-devel libSDL-devel libSDL_image-devel libSDL_mixer-devel libSDL_ttf-devel libX11-devel tetex-core xerces-c-devel

BuildRequires: libSDL-devel >= 1.2
BuildRequires: libSDL_mixer-devel >= 1.2.5
BuildRequires: libSDL_image-devel >= 1.2.0

Requires: libSDL >= 1.2
Requires: libSDL_mixer >= 1.2.4
Requires: libSDL_image >= 1.2.0
Requires: libSDL_ttf >= 2.0.6

%description
Enigma is a tribute to and a re-implementation of one of the most
original and intriguing computer games of the 1990's: Oxyd.  Your
objective is easily explained: find and uncover all pairs of identical
Oxyd stones in each landscape.  Sounds simple?  It would be, if it
weren't for hidden traps, vast mazes, insurmountable obstacles and
innumerable puzzles blocking your direct way to the Oxyd stones...

%prep
%setup
%patch1
%patch2 -p1
%patch3 -p1

%build

%configure --enable-optimize
%make_build

%install
%makeinstall pngdir=$RPM_BUILD_ROOT%_docdir/%name-%version/images \
             htmldir=$RPM_BUILD_ROOT%_docdir/%name-%version \
             docdir=$RPM_BUILD_ROOT%_docdir/%name-%version \
             indexdir=$RPM_BUILD_ROOT%_docdir/%name-%version \
             refdir=$RPM_BUILD_ROOT%_docdir/%name-%version/reference

%__rm -f $RPM_BUILD_ROOT%_docdir/%name-%version/COPYING
%__ln_s /usr/share/license/GPL-2 $RPM_BUILD_ROOT%_docdir/%name-%version/COPYING

%__rm -rf $RPM_BUILD_ROOT%_includedir
%__rm -rf $RPM_BUILD_ROOT%_libdir

%find_lang %{name}


%files -f %name.lang
%_docdir/*
%_bindir/*
%_datadir/pixmaps/*
%_datadir/%name
%_datadir/applications/*
%_man6dir/*
%_iconsdir/hicolor/*/*/*

%changelog
* Tue Aug 17 2010 Ilya Mashkin <oddity@altlinux.ru> 1.01-alt5
- update requires

* Tue Jul 14 2009 Ilya Mashkin <oddity@altlinux.ru> 1.01-alt4
- fix build with gcc4.4

* Fri Nov 13 2008 Ilya Mashkin <oddity@altlinux.ru> 1.01-alt3
- fix build with gcc4.3

* Mon Oct 06 2008 Ilya Mashkin <oddity@altlinux.ru> 1.01-alt2.1
- rebuild

* Sat Feb  2 2008 Alexander Borovsky <partizan@altlinux.ru> 1.01-alt2
- Menu entry fixed

* Sun Nov 25 2007 Alexander Borovsky <partizan@altlinux.ru> 1.01-alt1
- New version
- Fixed build

* Thu Jan 04 2007 Alexander Borovsky <partizan@altlinux.ru> 1.0-alt1
- New version

* Fri Sep 15 2006 Alexander Borovsky <partizan@altlinux.ru> 0.92-alt2
- Fixed build with GCC4

* Sat Jun 18 2005 Alexander Borovsky <partizan@altlinux.ru> 0.92-alt1
- New version

* Tue Jan 18 2005 ALT QA Team Robot <qa-robot@altlinux.org> 0.90-alt1.1
- Rebuilt with libstdc++.so.6.

* Tue Nov 16 2004 Alexander Borovsky <partizan@altlinux.ru> 0.90-alt1
- New version (0.90-beta)

* Tue Jul 13 2004 Alexander Borovsky <partizan@altlinux.ru> 0.81-alt2
- Fixed menu file (#4772)

* Thu Jun 17 2004 Alexander Borovsky <partizan@altlinux.ru> 0.81-alt1
- First build for Sisyphus
