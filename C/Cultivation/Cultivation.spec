Name: Cultivation
Version: 8
Release: alt5

Summary: Cultivation is a game about the interactions within a gardening community
License: GPL
Group: Games/Arcade

Url: http://cultivation.sourceforge.net/
Source: Cultivation_8_UnixSource.tar
Patch: Cultivation-8-alt-Makefile.patch
Packager: Fr. Br. George <george@altlinux.ru>

# Automatically added by buildreq on Tue Apr 05 2011
# optimized out: libGL-devel libGLU-devel libX11-devel libstdc++-devel
BuildRequires: gcc-c++ libGLUT-devel

BuildRequires: desktop-file-utils

%description
Cultivation is a game about a community of gardeners growing food
for themselves in a shared space.

Cultivation is quite different from most other games. It is a
social simulation, and the primary form of conflict is over land
and plant resources --- there is no shooting, but there are plenty
of angry looks. It is also an evolution simulation. Within the
world of Cultivation, you can explore a virtually infinite
spectrum of different plant and gardener varieties.

All of the graphics, sounds, melodies,and other content in
Cultivation are 100%% procedurally generated at playtime. In other
words, there are no hand-painted texture maps --- instead, each
object has a uniquely 'grown' appearance. Every time you play,
Cultivation generates fresh visuals, music, and behaviors.

%prep
%setup -n %{name}_%{version}_UnixSource
%patch -p2
%ifarch %e2k
sed -i 's/-O9/-O%_optlevel/g' game2/Makefile.common
%endif

%build
sed -i -e "s|/usr/X11R6/lib|%_lib|g" game2/Makefile.GnuLinux
export CFLAGS="$RPM_OPT_FLAGS -fPIC -DPIC"
# make: *** No rule to make target 'lib/', needed by 'lib/libportaudio.a'. Stop.
pushd minorGems/sound/portaudio
	chmod u+x ./configure
	%configure
	%make
popd
pushd game2
rm -f gameSource/Makefile
cat \
	Makefile.GnuLinux \
	Makefile.common \
	../minorGems/build/Makefile.minorGems \
	gameSource/Makefile.all \
	../minorGems/build/Makefile.minorGems_targets > gameSource/Makefile

pushd gameSource
	%make_build
popd

popd

%install
install -dm 755 %buildroot%_bindir
install -dm 755 %buildroot%_gamesbindir
install -pm 755 game2/gameSource/%name \
	%buildroot%_gamesbindir/%name.bin

install -dm 755 %buildroot%_datadir/%name
install -pm 644 game2/gameSource/font.tga \
	%buildroot%_datadir/%name
install -pm 644 game2/gameSource/features.txt \
	%buildroot%_datadir/%name
install -pm 644 game2/gameSource/language.txt \
	%buildroot%_datadir/%name
install -dm 755 %buildroot%_datadir/%name/languages
install -pm 644 game2/gameSource/languages/*.txt \
	%buildroot%_datadir/%name/languages

# startscript
cat > %name.sh <<EOF
#! /bin/bash
if [ ! -e \$HOME/.%name ]; then
	mkdir -p \$HOME/.%name
	cd \$HOME/.%name
	cp %_datadir/%name/*.txt .
	ln -s %_datadir/%name/*.tga .
	ln -s %_datadir/%name/languages .
fi

cd \$HOME/.%name
%_gamesbindir/%name.bin
EOF
install -pm 755 %name.sh \
	%buildroot%_bindir/%name

# icon
install -dm 755 %buildroot%_datadir/pixmaps
install -pm 644 game2/build/win32/iconSource.png \
	%buildroot%_datadir/pixmaps/%name.png

install -dm 755 %buildroot/%_datadir/applications
cat > %name.desktop << EOF
[Desktop Entry]
Type=Application
Comment=Cultivation is a game about the interactions within a gardening community
Terminal=false
Exec=%name
Icon=%name
Name=%name
Encoding=UTF-8
Categories=Game;ArcadeGame;
EOF
desktop-file-install --dir=%buildroot%_datadir/applications %name.desktop --vendor=""

%files
%doc game2/documentation/*
%_gamesbindir/%name.bin
%_bindir/%name
%dir %_datadir/%name
%_datadir/%name/*
%_datadir/applications/*.desktop
%_datadir/pixmaps/*.png

%changelog
* Sat Nov 09 2019 Michael Shigorin <mike@altlinux.org> 8-alt5
- E2K: fix superfluous optimization level
- avoid tarball compression
- partially enable parallel build
- more reproducible installed file timestamps

* Thu Oct 18 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 8-alt4
- NMU: rebuilt with libGLUT.

* Tue Nov 20 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 8-alt3.1
- Fixed build

* Tue Apr 05 2011 Fr. Br. George <george@altlinux.ru> 8-alt3
- Forbidden requires eliminated

* Tue Dec 02 2008 Valery Inozemtsev <shrek@altlinux.ru> 8-alt2.qa1.1
- NMU:
  * updated build dependencies
  * removed obsolete %%update_menus/%%clean_menus calls

* Thu Apr 10 2008 Igor Vlasenko <viy@altlinux.ru> 8-alt2.qa1
- NMU (by repocop): the following fixes applied:
 * update_menus for Cultivation

* Sun Sep 23 2007 Fr. Br. George <george@altlinux.ru> 8-alt2
- Desktop file fixed

* Sat Sep 22 2007 Fr. Br. George <george@altlinux.ru> 8-alt1
- Initial build for ALT

* Sun Sep 02 2007 Toni Graffy <toni@links2linux.de> - 8-0.pm.2
- fixed desktop file
* Thu Aug 07 2007 Toni Graffy <toni@links2linux.de> - 8-0.pm.1
- initial build 8
