Name: hyperrogue
Version: 112d
Release: alt1
Source: v%version.tar.gz
Url: http://www.roguetemple.com/z/hyper.php
License: GPLv2
Group: Games/Adventure
Summary: Roguelike in non-euclidian world
Epoch: 1

BuildPreReq: rpm-macros-fonts

Requires: fonts-ttf-dejavu

# Automatically added by buildreq on Tue Oct 15 2013
# optimized out: fontconfig libSDL-devel libstdc++-devel
BuildRequires: ImageMagick-tools gcc-c++ libSDL_gfx-devel libSDL_mixer-devel libSDL_ttf-devel libpng-devel
Requires: %name-music = %version

%description
You are a lone outsider in a strange, non-Euclidean world. You can move
with the numpad, vi keys (hjklyubn), or mouse. You can also skip turns
by pressing ".".

As a Rogue, your goal is to collect as many treasures as possible.
However, collecting treasures attracts dangerous monsters (on the other
hand, killing the monsters allows more treasures to be generated).

You can kill most monsters by moving into them. Similarly, if the
monster was next to you at the end of your turn, it would kill you. The
game protects you from getting yourself killed accidentally by ignoring
moves which lead to instant death (similar to the check rule from
Chess).

Ultimately, you will probably run into a situation where monsters
surround you. That means that your adventure is over, and you will have
to teleport back to the Euclidean world to survive by pressing Escape
(quit).

%package music
Buildarch: noarch
Summary: Music for %summary
Group: Games/Adventure
License: CC BY-SA 3.0

%description music
Music for %name

%prep
%setup
sed -i 's@"DejaVuSans-Bold.ttf"@"%_ttffontsdir/dejavu/DejaVuSans-Bold.ttf"@g' graph.cpp

%define sizes 16 24 32 48 64 96
for s in %sizes; do
	convert hr-icon.ico $s.png
done
cat > %name.desktop <<@@@
[Desktop Entry]
Type=Application
Name=Hyper Rogue
GenericName=Roguelike game
Comment=Roguelike in non-Euclidian space
Icon=ImageMagick
Exec=%name
Terminal=false
Categories=Game;RolePlaying;
Comment[ru]=Roguelike-ÉÇÒÁ × ÎÅÅ×ËÌÉÄÏ×ÏÍ ÐÒÏÓÔÒÁÎÓÔ×Å
@@@

%build
%autoreconf
%configure
%make_build LDFLAGS=-lm CXXFLAGS="-O0 -g"

%install
%makeinstall
for s in %sizes; do
	install -D $s.png %buildroot%_iconsdir/hicolor/${s}x${s}/apps/%name.png
done
install -D %name.desktop %buildroot%_desktopdir/%name.desktop

%files
%doc %_defaultdocdir/%name
%_bindir/%name
%_iconsdir/hicolor/*/apps/%name.png
%_desktopdir/%name.desktop

%files music
%_datadir/%name

%changelog
* Mon Nov 04 2019 Fr. Br. George <george@altlinux.ru> 1:112d-alt1
- Autobuild version bump to 112d

* Mon May 29 2017 Fr. Br. George <george@altlinux.ru> 1:9.4g-alt1
- Autobuild version bump to 9.4g

* Mon Jan 23 2017 Fr. Br. George <george@altlinux.ru> 83j-alt2
- Package game music

* Wed Jan 18 2017 Fr. Br. George <george@altlinux.ru> 83j-alt1
- Autobuild version bump to 83j

* Tue Jul 14 2015 Fr. Br. George <george@altlinux.ru> 66-alt1
- Autobuild version bump to 66

* Sun Apr 19 2015 Fr. Br. George <george@altlinux.ru> 55-alt1
- Autobuild version bump to 55
- Switch font to DejaVuSansBold

* Thu Dec 11 2014 Fr. Br. George <george@altlinux.ru> 44-alt2
- Rebuild with new SDL

* Wed Apr 09 2014 Fr. Br. George <george@altlinux.ru> 44-alt1
- Autobuild version bump to 44

* Tue Feb 18 2014 Fr. Br. George <george@altlinux.ru> 43-alt1
- Autobuild version bump to 43

* Wed Jan 15 2014 Fr. Br. George <george@altlinux.ru> 42-alt1
- Autobuild version bump to 42

* Tue Oct 15 2013 Fr. Br. George <george@altlinux.ru> 40t-alt1
- Autobuild version bump to 40t
- Fix build requirements

* Thu Aug 22 2013 Fr. Br. George <george@altlinux.ru> 38-alt1
- Autobuild version bump to 38

* Thu Jul 11 2013 Fr. Br. George <george@altlinux.ru> 37-alt1
- Initial build for ALT

