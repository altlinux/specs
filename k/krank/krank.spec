Name: krank
Version: 07
Release: alt2.1
License: GPL
Source: %name-%version.tar.bz2
Source1: %name.png
Source2: %name.desktop.in
Summary: Mouse magnet manipulation game with nifty graphics
Group: Games/Other
Buildarch: noarch
Packager: Fr. Br. George <george@altlinux.ru>

# Automatically added by buildreq on Mon Jan 05 2009
BuildRequires: ImageMagick-tools

%description
the snake  follows your mouse or the analog stick of your joypad.
the balls move if you touch them with the snake or another ball.
the links are like balls, but they bond together if they touch each other.
the stones never move and do nothing else.
the magnets, unmovable themselves, attract everything that moves. the number of circles rotating around them indicates how many items may get captured in them.
the anchors never move, but bond together with links. the number of circles rotating around them indicates how many links may bond with them.

the aim of each level is to remove all anchors and magnets.

%prep
%setup
rm -r levels/images/.DS_Store

%build
rm src/*.pyc
sed -i '/KRANKPATH=/s@=.*@=%_gamesdatadir/%name@' %name
sed -i '/^python/i\
export APPDATA="$HOME/.krank"\
mkdir -p "$APPDATA"\
cd $KRANKPATH
' %name
sed -i 's/@Summary@/%summary/g' %SOURCE2
sed -i 's/@Name@/%name/g' %SOURCE2 > %name.desktop
for N in 16 24 32 64 128; do convert %SOURCE1 -resize ${N}x${N} $N.png; done

%install
mkdir -p %buildroot/%_gamesdatadir/%name
for D in fonts html levels sounds src; do cp -a $D %buildroot/%_gamesdatadir/%name/; done
install -D %name %buildroot/%_gamesbindir/%name
install -D %name.desktop %buildroot/%_desktopdir/%name.desktop
install -D 16.png %buildroot%_miconsdir/%name.png
install -D 24.png %buildroot%_niconsdir/%name.png
install -D 32.png %buildroot%_liconsdir/%name.png
install -D 64.png %buildroot%_iconsdir/hicolor/64x64/apps/%name.png
install -D 128.png %buildroot%_iconsdir/hicolor/128x128/apps/%name.png

%files
%doc CHANGELOG.txt Info.plist README
%dir %_gamesdatadir/%name
%_gamesdatadir/%name/*
%_gamesbindir/%name
%_desktopdir/%name.desktop
%_iconsdir/hicolor/*/apps/%name.png

%changelog
* Sat Oct 22 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 07-alt2.1
- Rebuild with Python-2.7


* Tue May 11 2010 Fr. Br. George <george@altlinux.ru> 07-alt2
- Fix repocop warnings

* Thu Dec 03 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 07-alt1.qa1.1
- Rebuilt with python 2.6

* Sat Nov 14 2009 Repocop Q. A. Robot <repocop@altlinux.org> 07-alt1.qa1
- NMU (by repocop): the following fixes applied:
  * macos-ds-store-file-in-package for krank
  * postclean-05-filetriggers for spec file


* Mon Jan 05 2009 Fr. Br. George <george@altlinux.ru> 07-alt1
- Initial build from scratch

