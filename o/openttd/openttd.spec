Name: openttd
Version: 1.0.4
Release: alt1

Summary: An open source clone of the Microprose game "Transport Tycoon Deluxe".
License: GPL
Group: Games/Strategy
URL: http://www.openttd.com/
Requires: TiMidity++
Requires: fonts-ttf-dejavu Xdialog
Requires: %name-data = %version-%release
Packager: Anton Farygin <rider@altlinux.com>

Source: %name-%version-%release.tar

Patch0: %name-%version-%release.patch

BuildRequires: libSDL-devel libpng-devel libfreetype-devel fontconfig-devel gcc-c++ liblzo2-devel


%description
An open source clone of the Microprose game "Transport Tycoon Deluxe".

You need following files from TTD Win version:
  - sample.cat
  - trg1r.grf
  - trgcr.grf
  - trghr.grf
  - trgir.grf
  - trgtr.grf

To play music tracks you need files from gm directory

%package data
Buildarch: noarch
Summary: Data files for %name
Requires: %name
Group: Games/Strategy
Requires: %name-3rd-party

%description data
Data files for %name

%prep
%setup -q -n %name-%version-%release
%patch0 -p1

%build
./configure \
    --prefix-dir=%_prefix \
    --with-sdl \
    --with-png \
    --with-freetype \
    --with-fontconfig \
    --without-libtimidity \
    --revision=%version
    
%make_build WITH_SDL=1 UNIX=1 RELEASE=%version INSTALL=1 WITH_NETWORK=1 \
    USE_HOMEDIR=1 VERBOSE=1 PERSONAL_DIR=.%name \
    PREFIX=%_prefix DATA_DIR=share/games/%name \
	
%install
%__mkdir_p %buildroot%_prefix/games
%__mkdir_p %buildroot%_datadir/games/%name/gm
%__mkdir_p %buildroot%_datadir/games/%name/lang
%__mkdir_p %buildroot%_man6dir

%__install -m755 -s bin/%name %buildroot%_prefix/games/%name
%__install -m755 %name-installer %buildroot%_prefix/games/%name-installer
%__cp -a bin/data %buildroot%_datadir/games/%name
%__cp -a bin/lang/*.lng %buildroot%_datadir/games/%name/lang
%__chmod -x %buildroot%_datadir/games/%name/data/*

#menu

%__install -dm 755 %buildroot%_datadir/applications
%__install -m644 media/%name.desktop %buildroot%_datadir/applications/%name.desktop
%__subst "s,Exec=openttd,Exec=openttd-installer," %buildroot%_datadir/applications/%name.desktop

# icons
%__install -pD -m644 media/%name.16.png %buildroot%_miconsdir/%name.png
%__install -pD -m644 media/%name.32.png %buildroot%_niconsdir/%name.png
%__install -pD -m644 media/%name.48.png %buildroot%_liconsdir/%name.png
%__install -pD -m644 docs/%name.6 %buildroot%_man6dir/


%files
%_prefix/games/%name
%_prefix/games/%name-installer

%files data
%doc docs/* bin/scripts readme.txt known-bugs.txt changelog.txt COPYING
%_datadir/games/%name
%_datadir/applications/%name.desktop
%_niconsdir/%name.png
%_miconsdir/%name.png
%_liconsdir/%name.png
%_man6dir/*

%changelog
* Sun Sep 19 2010 Anton Farygin <rider@altlinux.ru> 1.0.4-alt1
- new version

* Tue Aug 31 2010 Anton Farygin <rider@altlinux.ru> 1.0.3-alt1
- new version (fixed CVE-2010-2534)

* Tue Jun 29 2010 Anton Farygin <rider@altlinux.ru> 1.0.2-alt1
- new version

* Thu Jun 17 2010 Anton Farygin <rider@altlinux.ru> 1.0.1-alt1
- new version

* Wed Jan 27 2010 Anton Farygin <rider@altlinux.ru> 0.7.5-alt1
- new version (CVE-2009-4007 fixed)

* Fri Oct 09 2009 Anton Farygin <rider@altlinux.ru> 0.7.3-alt1
- new version

* Wed Sep 02 2009 Anton Farygin <rider@altlinux.ru> 0.7.2-alt2
- use niconsdir instead of iconsdir
- fixed desktop file

* Tue Sep 01 2009 Anton Farygin <rider@altlinux.ru> 0.7.2-alt1
- new version

* Tue Jun 30 2009 Anton Farygin <rider@altlinux.ru> 0.7.1-alt1
- new version

* Sat Apr 11 2009 Anton Farygin <rider@altlinux.ru> 0.7.0-alt2
- 0.7.0

* Thu Mar 26 2009 Anton Farygin <rider@altlinux.ru> 0.7.0-alt1.r15828
- 0.7.0-rc2

* Mon Mar 16 2009 Anton Farygin <rider@altlinux.ru> 0.7.0-alt1.r15737
- 0.7.0-rc1

* Fri Mar 13 2009 Anton Farygin <rider@altlinux.ru> 0.7.0-alt1.r15697
- updated snapshot (fixed some crash issues)

* Thu Mar 12 2009 Anton Farygin <rider@altlinux.ru> 0.7.0-alt1.r15676
- new snapshot (0.7.0-beta2)

* Tue Mar 03 2009 Anton Farygin <rider@altlinux.ru> 0.7.0-alt1.r15601
- new snapshot
- default fonts changed and warning about DejaVu removed

* Sat Feb 28 2009 Anton Farygin <rider@altlinux.ru> 0.7.0-alt1.r15592
- new snapshot

* Thu Feb 26 2009 Anton Farygin <rider@altlinux.ru> 0.7.0-alt1.r15587
- new snapshot (0.7.0-beta1)
- use official revision number (0.7.0-beta1) for playing over network

* Wed Feb 25 2009 Anton Farygin <rider@altlinux.ru> 0.6.3-alt3.r15578
- new snapshot
- squirrel included to maintree

* Fri Feb 20 2009 Anton Farygin <rider@altlinux.ru> 0.6.3-alt2.r15529
- new snapshot

* Mon Feb 16 2009 Anton Farygin <rider@altlinux.ru> 0.6.3-alt2.r15495
- fixed revision in game
- noarch content moved to %name-data subpackage

* Sat Feb 14 2009 Anton Farygin <rider@altlinux.ru> 0.6.3-alt1.svn15476
- new snapshot from svn
- added russian towns

* Fri Feb 13 2009 Anton Farygin <rider@altlinux.ru> 0.6.3-alt1.svn15465
- new snapshot from svn
- Xdialog added to requires

* Wed Feb 11 2009 Anton Farygin <rider@altlinux.ru> 0.6.3-alt1.svn15447
- new snapshot from svn
- added data downloader and installer
- menu file changed to desktop file

* Tue Feb 03 2009 Anton Farygin <rider@altlinux.ru> 0.6.3-alt1
- new version (from svn 15322)
- post-scripts removed 

* Fri Jun 06 2008 Andrew Kornilov <hiddenman@altlinux.ru> 0.6.1-alt1
- New release

* Wed Apr 02 2008 Andrew Kornilov <hiddenman@altlinux.ru> 0.6.0-alt1
- New release
- Fonts patch updated (and enabled AA)

* Wed Oct 03 2007 Andrew Kornilov <hiddenman@altlinux.ru> 0.5.3-alt1
- New release
- Fonts patch was reworked (fontconfig support seems to be fixed, so 
  hardcoded font paths were removed; uses font names now)
- Spec updates (to conform openttd's fs hier)

* Wed Apr 25 2007 Andrew Kornilov <hiddenman@altlinux.ru> 0.5.1-alt2
- New release

* Fri Mar 23 2007 Andrew Kornilov <hiddenman@altlinux.ru> 0.5.1-alt1.RC2
- Bugfix RC2
- Spec cleanups

* Thu Mar 01 2007 Andrew Kornilov <hiddenman@altlinux.ru> 0.5.0-alt2
- Release

* Sun Feb 04 2007 Andrew Kornilov <hiddenman@altlinux.ru> 0.5.0-alt1.svn8588
- New version from SVN
- Updated buildreqs
- Spec cleanups
- Correct man placement
- New patch (use correct, but hardcoded fonts)
- Added missed docs

* Fri Oct 06 2006 Damir Shayhutdinov <damir@altlinux.ru> 0.4.8-alt1
- 0.4.8
- Updated buildreqs.

* Thu Jan 27 2005 Kachalov Anton <mouse@altlinux.ru> 0.3.6-alt1
- 0.3.6
  + some scenarios in docs/scenario
  + scripts example in docs/scripts

* Tue Dec 28 2004 Kachalov Anton <mouse@altlinux.ru> 0.3.5-alt1
- 0.3.5

* Wed Jun 09 2004 Kachalov Anton <mouse@altlinux.ru> 0.3.2.1-alt1
- first build for Sisyphus
