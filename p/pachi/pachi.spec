# Unpackaged files in buildroot should terminate build
%define _unpackaged_files_terminate_build 1

Name: pachi
Version: 1.0
Release: alt3.qa2

Summary: Cool 2D game like Manic Miner, Jet set Willy and more from the 80s
License: GPLv2
Group: Games/Arcade
Url: http://dragontech.sourceforge.net/
Packager: Slava Semushin <php-coder@altlinux.ru>

BuildRequires: gcc-c++ libSDL-devel libSDL_mixer-devel ImageMagick
Requires: %name-data = %version

# http://prdownloads.sf.net/dragontech/pachi_source.tgz
Source: Pachi.tar.bz2
Patch0: Pachi-makefile-alt.patch
Patch1: pachi-alt-src-off-by-one_fix.patch
Patch2: pachi-alt-warnigs-fix.patch

%description
Pachi el marciano is a cool 2D platforms game inspired in games like
Manic Miner, Jet set Willy and more from the 80s.

%package data
Summary: Data files for Pachi game
Group: Games/Arcade
BuildArch: noarch
Requires: %name = %version

%description data
Architecture-independent data files for Pachi game.

%prep
%setup -n Pachi
%patch0
%patch1
%patch2

%build
%configure --bindir=%_gamesbindir --datadir=%_gamesdatadir
%make_build --silent --no-print-directory CXXFLAGS="%optflags -Werror"

%install
%make_install --silent --no-print-directory DESTDIR=%buildroot install

# menu
mkdir -p %buildroot%_desktopdir
cat > %buildroot%_desktopdir/%{name}.desktop <<EOF
[Desktop Entry]
Version=1.0
Type=Application
Name=Pachi
GenericName=
Comment=%{summary}
Icon=%{name}
Exec=%_gamesbindir/%name
#Exec=%name
Terminal=false
Categories=Game;ArcadeGame;
EOF

# icons
convert Tgfx/icon.bmp -resize 16x16 Tgfx/%name-16.png
convert Tgfx/icon.bmp -resize 32x32 Tgfx/%name-32.png
convert Tgfx/icon.bmp -resize 48x48 Tgfx/%name-48.png

install -pD -m644 Tgfx/%name-16.png %buildroot%_miconsdir/%name.png
install -pD -m644 Tgfx/%name-32.png %buildroot%_niconsdir/%name.png
install -pD -m644 Tgfx/%name-48.png %buildroot%_liconsdir/%name.png

%files
%doc AUTHORS ChangeLog
%attr(2711,root,games) %_gamesbindir/%name
%_desktopdir/%{name}.desktop
%_niconsdir/%name.png
%_miconsdir/%name.png
%_liconsdir/%name.png
%_localstatedir/games/%name
%config(noreplace) %attr(664,games,games) %_localstatedir/games/%name/data/scores.dat

%files data
%_gamesdatadir/%name

%changelog
* Wed Apr 06 2011 Igor Vlasenko <viy@altlinux.ru> 1.0-alt3.qa2
- NMU: converted debian menu to freedesktop

* Thu Feb 04 2010 Repocop Q. A. Robot <repocop@altlinux.org> 1.0-alt3.qa1
- NMU (by repocop): the following fixes applied:
  * pixmap-in-deprecated-location for pachi
  * postclean-05-filetriggers for spec file

* Sat Nov 29 2008 Slava Semushin <php-coder@altlinux.ru> 1.0-alt3
- Fixed Requires in pachi-data subpackage

* Sun Nov 23 2008 Slava Semushin <php-coder@altlinux.ru> 1.0-alt2
- Removed obsolete %%update_menus/%%clean_menus calls (noted by repocop)
- Moved data files to separated pachi-data subpackage (noted by repocop)
- Fixed off-by-one error in print_text() function
- Fixed all warnings and build with -Werror flag
- Enable _unpackaged_files_terminate_build

* Sat Jul 26 2008 Slava Semushin <php-coder@altlinux.ru> 1.0-alt1
- New maintainer
- Updated to 1.0 (no code change, just version increase)
- Changed Group tag to "Games/Arcade" (Closes: #15383)
- Corrected Url tag
- More proper Licence tag
- Spec cleanup

* Tue Jan 18 2005 ALT QA Team Robot <qa-robot@altlinux.org> 0.1-alt1.1
- Rebuilt with libstdc++.so.6.

* Thu Jul 01 2004 Kachalov Anton <mouse@altlinux.ru> 0.1-alt1
- first build for Sisyphus

