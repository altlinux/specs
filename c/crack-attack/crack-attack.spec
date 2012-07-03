# Unpackaged files in buildroot should terminate build
%define _unpackaged_files_terminate_build 1

Name: crack-attack
Version: 1.1.14
Release: alt9

Summary: Crack Attack! is a fast paced 3D puzzle game
Summary(ru_RU.UTF-8): Crack Attack! - быстрая 3D игра-головоломка

License: GPLv2
Group: Games/Arcade
Url: http://www.nongnu.org/crack-attack/

Source: http://savannah.nongnu.org/download/crack-attack/%name-%version.tar.bz2

# Tarballs based on files pulled from SuSe package:
# http://ftp.chg.ru/pub/opensuse/distribution/10.3/repo/oss/suse/noarch/crack-attack-sounds-1.1.14-58.noarch.rpm
Source1: crack-attack-sounds.tar.gz
Source2: crack-attack-music.tar.gz

Patch: %name-alt-warnings-Wall_fix.patch
Patch1: %name-upstream-start_game_fix.patch
Patch2: %name-alt-upstream-alt_f4_exit_fix.patch
Patch3: %name-upstream-src-glutDestroyWindow_call_fix.patch
Patch4: %name-alt-src-gcc43_fix.patch


# Automatically added by buildreq on Tue Apr 12 2011
# optimized out: fontconfig fontconfig-devel glib2-devel libGL-devel libGLU-devel libICE-devel libSDL-devel libSM-devel libX11-devel libatk-devel libcairo-devel libfreetype-devel libgdk-pixbuf libgdk-pixbuf-devel libgio-devel libpango-devel libstdc++-devel pkg-config xorg-xproto-devel
BuildRequires: gcc-c++ libSDL_mixer-devel libXi-devel libXmu-devel libfreeglut-devel libgtk+2-devel

%description
Crack Attack! is a fast-paced puzzle game inspired by the classic
Super NES title Tetris Attack!

%description -l ru_RU.UTF-8
Crack Attack! - это быстрая игра-головоломка, вдохновленная классической
игрой от Super NES под названием Tetris Attack!

%prep
%setup
%patch -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1

# fixed warnings from autoconf
sed -i '4a\
AC_CANONICAL_HOST\
AC_CANONICAL_TARGET

;14,16d' configure.ac

%autoreconf

%build
%configure --bindir=%_gamesbindir \
			--datadir=%_gamesdatadir \
			--enable-sound
%make_build --silent --no-print-directory CXXFLAGS="%optflags"

%install
%make_install --silent --no-print-directory DESTDIR=%buildroot install

mkdir -p %buildroot%_pixmapsdir
ln -s %_gamesdatadir/%name/%name.xpm %buildroot%_pixmapsdir

install -pD -m 644 %buildroot%_gamesdatadir/%name/%name.desktop %buildroot%_desktopdir/%name.desktop
rm %buildroot%_gamesdatadir/%name/%name.desktop

mkdir -p %buildroot%_gamesdatadir/%name/{sounds,music}
tar xf %SOURCE1 -C %buildroot%_gamesdatadir/%name/sounds/
tar xf %SOURCE2 -C %buildroot%_gamesdatadir/%name/music/

# Fix Categories key (replace deprecated "Application" and "Games" values)
sed -i '/^Categories/s/Application;Games/Game;ArcadeGame/' %buildroot%_desktopdir/%name.desktop

# Fix Icon key (remove extension)
sed -i '/^Icon/s/\.xpm$//' %buildroot%_desktopdir/%name.desktop

# Remove deprecated Encoding key
sed -i '/^Encoding=/d' %buildroot%_desktopdir/%name.desktop

%files
%doc AUTHORS ChangeLog COPYRIGHT
%doc doc/index.html doc/dl_ii_linux.html doc/logo_big.jpg
%doc doc/tn_* doc/screen_explanation.jpg
%_gamesbindir/%name
%_gamesdatadir/%name/
%_desktopdir/%name.desktop
%_man6dir/%name.6.*
%_pixmapsdir/%name.xpm

%changelog
* Tue Apr 12 2011 Fr. Br. George <george@altlinux.ru> 1.1.14-alt9
- BuildRequires recalculated

* Tue Nov 18 2008 Slava Semushin <php-coder@altlinux.ru> 1.1.14-alt8
- Fixed build with gcc4.3
- Removed obsolete %%update_menus/%%clean_menus calls (noted by repocop)
- Build without -Werror flag

* Fri Oct 17 2008 Slava Semushin <php-coder@altlinux.ru> 1.1.14-alt7
- Fixed desktop file (noted by repocop)

* Sat Apr 19 2008 Slava Semushin <php-coder@altlinux.ru> 1.1.14-alt6
- Added and enable sound (idea from NetBSD pkgsrc, files from SuSe package)
- Spec improvements:
  + Corrected License tag
  + Replace %%__autoreconf macros to %%autoreconf
  + Added references to Debian bugzilla to last entry in %%changelog

* Sun Oct 21 2007 Slava Semushin <php-coder@altlinux.ru> 1.1.14-alt5
- Backported patches from upstream:
  + Fix for game start with freeglut 2.4.0
    (savannah bug #16073)
  + Fix for error during exit from 'crack-attack --solo'
    (savannah bug #15821)
  + Correctly exit from game when Alt+F4 pressed or 'x' button clicked
    (savannah bug #13163 and #17839, deb #371146)
- Move symlink to icon from /usr/share/icons to /usr/share/pixmaps
- More proper Categories in desktop file
- Corrected BuildPreReq tag

* Fri May 18 2007 Slava Semushin <php-coder@altlinux.ru> 1.1.14-alt4
- Imported into git and built with gear
- Spec cleanup:
  + Changed my name in Packager tag
  + Formatted and corrected %%description
  + Use builtin %%patch instead of external command
  + s/%%setup -q/%%setup/
  + Removed useless --with-x option for configure script
- Enable _unpackaged_files_terminate_build

* Tue Feb 07 2006 php-coder <php-coder@altlinux.ru> 1.1.14-alt3
- Updated BuildRequires for Xorg7
- Fixed Categories in desktop file
- Using %%_desktopdir and %%__autoreconf macroses
- Fixed orthographical errors in %%changelog (spotted by mike@)
- Give CXXFLAGS variable to make instead of using %%add_optflags
- Renamed patch to Wall_fix
- More strict names in %%files section
- Dont use macros for patch, sed, mkdir -p, ln -s, install and rm
  commands
- Removed Summary and %%description in koi8-r and utf8 charsets

* Sat Dec 24 2005 php-coder <php-coder@altlinux.ru> 1.1.14-alt2
- Added patch which fixes all warnings from compiler
- Using -Werror flag for compiler by default
- Running make with --no-print-directory and --silent options to make
  terminal output clean
- Removed COPYING file from package
- Removed menu file because already exist .desktop file
- Updated BuildRequires

* Mon Jul 25 2005 php-coder <php-coder@altlinux.ru> 1.1.14-alt1
- First build for Sisyphus

