Name: lightyears
Version: 1.4
Release: alt1
License: GPL
Summary: A steampunk-themed strategy game where you have to manage a steam supply network
Source: %name-%version.tar.bz2
Group: Games/Puzzles
Url: http://www.jwhitham.org/20kly
BuildArch: noarch

BuildPreReq: rpm-build-fonts

BuildRequires: ImageMagick-tools fonts-ttf-vera

%description
20,000 Light Years Into Space is a steampunk-themed strategy game where
you have to manage a steam supply network. It is written in Python and
runs on Windows and Linux. It was first released in 2006, and won second
prize in the Pyweek game programming competition. It is free software,
licensed under the GNU GPL version 2. It is now being distributed with
the Debian and Ubuntu operating systems, and you can download it here
too. There is a story for the game. Light Years includes an interactive
tutorial; you can also read the instructions and a bit of history about
Light Years.

%prep
%setup

%build
for n in 72 64 48 32 ; do
  convert data/city1.png -trim -resize ${n}x$n -background transparent -gravity Center -extent ${n}x$n! $n.png; done

cat > %name.desktop <<@@@
[Desktop Entry]
Comment=%summary
Name=20,000 Light Years Into Space
GenericName=Simple strategy game
Type=Application
Exec=%name
Icon=%name
Terminal=false
Categories=Game;StrategyGame;
@@@

%install
mkdir -p %buildroot%_gamesdatadir
cp -rp . %buildroot%_gamesdatadir/%name
rm %buildroot%_gamesdatadir/%name/data/Vera.ttf
ln -s %_ttffontsdir/TrueType-vera/Vera.ttf %buildroot%_gamesdatadir/%name/data/Vera.ttf
install -D %name %buildroot%_gamesbindir/%name
install -D %name.desktop %buildroot%_desktopdir/%name.desktop
for n in 72 64 48 32; do install -D $n.png %buildroot%_iconsdir/hicolor/${n}x$n/apps/%name.png; done

%files
%doc README.txt manual
%_gamesdatadir/%name
%_gamesbindir/%name
%_desktopdir/*
%_iconsdir/hicolor/*/apps/*

%changelog

* Sun Nov 14 2011 Fr. Br. George <george@altlinux.ru> 1.4-alt1
- Autobuild version bump to 1.4
- Remove patch (fixed by upstream)

* Sat Oct 22 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.3a-alt3.1
- Rebuild with Python-2.7

* Thu Jun 30 2011 Fr. Br. George <george@altlinux.ru> 1.3a-alt3
- System font used instead of shipped one
- IFARCH removed for noarch compatibility

* Tue Feb 22 2011 Fr. Br. George <george@altlinux.ru> 1.3a-alt2
- Accurate arch handling

* Thu Dec 03 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.3a-alt1.qa1.1
- Rebuilt with python 2.6

* Sat Nov 14 2009 Repocop Q. A. Robot <repocop@altlinux.org> 1.3a-alt1.qa1
- NMU (by repocop): the following fixes applied:
  * backup-file-in-package for lightyears
  * postclean-05-filetriggers for spec file

* Mon Jun 29 2009 Fr. Br. George <george@altlinux.ru> 1.3a-alt1
- Initial build from scratch

