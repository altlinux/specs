%ifnarch %ix86
%def_without asm
%else
%set_verify_elf_method textrel=relaxed
%endif

# default build options
%{!?_without_asm:%define asm_buildopt USE_X86_ASM=yes}
%{!?_without_alsa:%define alsa_buildopt USE_ALSA=yes}
%{!?_without_midi:%define midi_buildopt USE_MIDI=yes}
%{!?_without_timidity:%define timidity_buildopt USE_CODEC_TIMIDITY=yes}
%{!?_without_wavmusic:%define wavmusic_buildopt USE_CODEC_WAVE=yes}
%{!?_with_mpg123:%define mp3_libraryopt MP3LIB=mad}
%{!?_without_mp3:%define mp3_buildopt USE_CODEC_MP3=yes}
%{!?_without_ogg:%define ogg_buildopt USE_CODEC_VORBIS=yes}
%{!?_with_flac:%define flac_buildopt USE_CODEC_FLAC=no}
%{!?_with_opus:%define opus_buildopt USE_CODEC_OPUS=no}
%{!?_with_mikmod:%define mikmod_buildopt USE_CODEC_MIKMOD=no}
%{!?_with_umx:%define umx_buildopt USE_CODEC_UMX=no}
# build option overrides
%{?_without_asm:%define asm_buildopt USE_X86_ASM=no}
%{?_without_alsa:%define alsa_buildopt USE_ALSA=no}
%{?_without_midi:%define midi_buildopt USE_MIDI=no}
%{?_without_timidity:%define timidity_buildopt USE_CODEC_TIMIDITY=no}
%{?_without_wavmusic:%define wavmusic_buildopt USE_CODEC_WAVE=no}
%{?_with_mpg123:%define mp3_libraryopt MP3LIB=mpg123}
%{?_without_mp3:%define mp3_buildopt USE_CODEC_MP3=no}
%{?_without_ogg:%define ogg_buildopt USE_CODEC_VORBIS=no}
%{?_with_flac:%define flac_buildopt USE_CODEC_FLAC=yes}
%{?_with_opus:%define opus_buildopt USE_CODEC_OPUS=yes}
%{?_with_mikmod:%define mikmod_buildopt USE_CODEC_MIKMOD=yes}
%{?_with_umx:%define umx_buildopt USE_CODEC_UMX=yes}
# all build options passed to makefile
%define engine_buildopt	%asm_buildopt %alsa_buildopt %midi_buildopt %timidity_buildopt %wavmusic_buildopt %mp3_buildopt %mp3_libraryopt %ogg_buildopt %opus_buildopt %flac_buildopt %mikmod_buildopt %umx_buildopt

%define mk_build %make_build %engine_buildopt

%define desktop_vendor	uhexen2
%define gamecode_ver	1.29b
%define gamedir %_libdir/%name

Name: hexen2
License: GPLv2
Group: Games/Arcade
Version: 1.5.9
Release: alt3
Summary: Hexen II: Hammer of Thyrion
Url: http://uhexen2.sourceforge.net/
Source: http://download.sourceforge.net/uhexen2/hexen2source-%version.tgz
#Source1:	http://download.sourceforge.net/uhexen2/gamedata-src-%gamecode_ver.tgz
Source1: http://download.sourceforge.net/uhexen2/hexen2source-gamecode-%version.tgz
Source2: http://download.sourceforge.net/uhexen2/hexenworld-pakfiles-0.15.tgz
Patch:	hexen-MAX_OSPATH.patch

%{!?_without_asm:BuildRequires:  nasm >= 0.98}

# Automatically added by buildreq on Wed Apr 21 2021
# optimized out: fontconfig glibc-kernheaders-generic glibc-kernheaders-x86 libImageMagick6-common libglvnd-devel libgpg-error libogg-devel python2-base sh4
BuildRequires: ImageMagick-tools libSDL-devel libalsa-devel libmad-devel libvorbis-devel

%description
Hexen II is a class based shooter game by Raven Software from 1997.
Hammer of Thyrion is a port of the GPL'ed source code released by
Raven. This package contains binaries that will run both the original
game and the Portal of Praevus mission pack, a dedicated server and a
launcher application which provides a GTK gui for launching different
versions of the game.

%package -n hexenworld
Group: Games/Arcade
Summary: HexenWorld Client and Server
Requires: hexen2 >= 1.4.3

%description -n hexenworld
Hexen II is a class based shooter game by Raven Software from 1997.
Hammer of Thyrion is a port of the GPL'ed source code released by
Raven. HexenWorld is an extension of Hexen II with enhancements for
internet play. This package contains the files which are required to
run a HexenWorld server or client, and a master server application.

%prep
%setup -q -n hexen2source-%version -a1 -a2
sed -i 's@hexen2dir=.*@hexen2dir=%gamedir@' scripts/hexen2-run.sh

%build

# Build the main game binaries
%mk_build -C engine/hexen2 h2
%make -s -C engine/hexen2 localclean
%mk_build -C engine/hexen2 glh2
%make -s -C engine/hexen2 localclean
# Build the dedicated server
%make_build -C engine/hexen2/server
# HexenWorld binaries
%make_build -C engine/hexenworld/server
%mk_build -C engine/hexenworld/client hw
%make -s -C engine/hexenworld/client localclean
%mk_build -C engine/hexenworld/client glhw
# HexenWorld master server
%make_build -C hw_utils/hwmaster

# Build h2patch
%make_build -C h2patch

# Build the hcode compiler
%make_build -C utils/hcc
# Build the game-code
utils/hcc/hcc -src gamecode-%gamecode_ver/hc/h2 -os
utils/hcc/hcc -src gamecode-%gamecode_ver/hc/h2 -os -name progs2.src
utils/hcc/hcc -src gamecode-%gamecode_ver/hc/portals -os -oi -on
utils/hcc/hcc -src gamecode-%gamecode_ver/hc/hw -os -oi -on
#utils/bin/hcc -src gamecode-%gamecode_ver/hc/siege -os -oi -on

# Install menu entry
cat > %name.desktop << EOF
[Desktop Entry]
Name=Hexen 2
Comment=Hexen II
Exec=hexen2
Icon=hexen2
Terminal=false
Type=Application
Categories=Game;ActionGame;
EOF
# Done building

convert engine/resource/hexen2n.png -resize 48x48 48.png
convert engine/resource/hexen2n.png -resize 16x16 16.png

%install
install -D -m755 engine/hexen2/glhexen2 %buildroot/%gamedir/glhexen2
install -D -m755 engine/hexen2/hexen2 %buildroot/%gamedir/hexen2
install -D -m755 engine/hexen2/server/h2ded %buildroot/%gamedir/h2ded
install -D -m755 engine/hexenworld/client/hwcl %buildroot/%gamedir/hwcl
install -D -m755 engine/hexenworld/client/glhwcl %buildroot/%gamedir/glhwcl
install -D -m755 engine/hexenworld/server/hwsv %buildroot/%gamedir/hwsv
install -D -m755 hw_utils/hwmaster/hwmaster %buildroot/%gamedir/hwmaster
install -D -m755 h2patch/h2patch %buildroot/%gamedir/h2patch

# Install the run script and make symlinks to it
install -D -m755 scripts/hexen2-run.sh %buildroot/%_bindir/hexen2-run.sh
ln -s hexen2-run.sh %buildroot/%_bindir/glhexen2
ln -s hexen2-run.sh %buildroot/%_bindir/hexen2
ln -s hexen2-run.sh %buildroot/%_bindir/h2ded
ln -s hexen2-run.sh %buildroot/%_bindir/glhwcl
ln -s hexen2-run.sh %buildroot/%_bindir/hwcl
ln -s hexen2-run.sh %buildroot/%_bindir/hwsv

# Install the cd-rip scripts
install -m755 scripts/cdrip_* %buildroot/%gamedir/

# Install the gamedata
install -D -m644 gamecode-%gamecode_ver/hc/h2/progs.dat %buildroot/%gamedir/data1/progs.dat
install -D -m644 gamecode-%gamecode_ver/hc/h2/progs2.dat %buildroot/%gamedir/data1/progs2.dat
install -D -m644 gamecode-%gamecode_ver/res/h2/hexen.rc %buildroot/%gamedir/data1/hexen.rc
install -D -m644 gamecode-%gamecode_ver/res/h2/strings.txt %buildroot/%gamedir/data1/strings.txt
install -D -m644 gamecode-%gamecode_ver/res/h2/default.cfg %buildroot/%gamedir/data1/default.cfg
install -D -m644 gamecode-%gamecode_ver/hc/portals/progs.dat %buildroot/%gamedir/portals/progs.dat
install -D -m644 gamecode-%gamecode_ver/res/portals/hexen.rc %buildroot/%gamedir/portals/hexen.rc
install -D -m644 gamecode-%gamecode_ver/res/portals/strings.txt %buildroot/%gamedir/portals/strings.txt
install -D -m644 gamecode-%gamecode_ver/res/portals/infolist.txt %buildroot/%gamedir/portals/infolist.txt
install -D -m644 gamecode-%gamecode_ver/res/portals/maplist.txt %buildroot/%gamedir/portals/maplist.txt
install -D -m644 gamecode-%gamecode_ver/res/portals/puzzles.txt %buildroot/%gamedir/portals/puzzles.txt
install -D -m644 gamecode-%gamecode_ver/res/portals/default.cfg %buildroot/%gamedir/portals/default.cfg
install -D -m644 gamecode-%gamecode_ver/hc/hw/hwprogs.dat %buildroot/%gamedir/hw/hwprogs.dat
install -D -m644 gamecode-%gamecode_ver/res/hw/mapcycle.cfg %buildroot/%gamedir/hw/mapcycle.cfg
install -D -m644 gamecode-%gamecode_ver/res/hw/server.cfg %buildroot/%gamedir/hw/server.cfg
install -D -m644 gamecode-%gamecode_ver/res/hw/strings.txt %buildroot/%gamedir/hw/strings.txt
install -D -m644 gamecode-%gamecode_ver/res/hw/default.cfg %buildroot/%gamedir/hw/default.cfg
install -D -m644 hw/pak4.pak %buildroot/%gamedir/hw/pak4.pak

# Install ent fixes handling map quirks
install -D -m644 gamecode-%gamecode_ver/mapfixes/data1/maps/README.txt %buildroot/%gamedir/data1/maps/README.txt
install -D -m644 gamecode-%gamecode_ver/mapfixes/data1/maps/cath.ent %buildroot/%gamedir/data1/maps/cath.ent
install -D -m644 gamecode-%gamecode_ver/mapfixes/data1/maps/cath.txt %buildroot/%gamedir/data1/maps/cath.txt
install -D -m644 gamecode-%gamecode_ver/mapfixes/data1/maps/demo2.ent %buildroot/%gamedir/data1/maps/demo2.ent
install -D -m644 gamecode-%gamecode_ver/mapfixes/data1/maps/demo2.txt %buildroot/%gamedir/data1/maps/demo2.txt
install -D -m644 gamecode-%gamecode_ver/mapfixes/data1/maps/egypt4.ent %buildroot/%gamedir/data1/maps/egypt4.ent
install -D -m644 gamecode-%gamecode_ver/mapfixes/data1/maps/egypt4.txt %buildroot/%gamedir/data1/maps/egypt4.txt
install -D -m644 gamecode-%gamecode_ver/mapfixes/data1/maps/egypt5.ent %buildroot/%gamedir/data1/maps/egypt5.ent
install -D -m644 gamecode-%gamecode_ver/mapfixes/data1/maps/egypt5.txt %buildroot/%gamedir/data1/maps/egypt5.txt
install -D -m644 gamecode-%gamecode_ver/mapfixes/data1/maps/romeric5.ent %buildroot/%gamedir/data1/maps/romeric5.ent
install -D -m644 gamecode-%gamecode_ver/mapfixes/data1/maps/romeric5.txt %buildroot/%gamedir/data1/maps/romeric5.txt
install -D -m644 gamecode-%gamecode_ver/mapfixes/data1/maps/tower.ent %buildroot/%gamedir/data1/maps/tower.ent
install -D -m644 gamecode-%gamecode_ver/mapfixes/data1/maps/tower.txt %buildroot/%gamedir/data1/maps/tower.txt
install -D -m644 gamecode-%gamecode_ver/mapfixes/portals/maps/README.txt %buildroot/%gamedir/portals/maps/README.txt
install -D -m644 gamecode-%gamecode_ver/mapfixes/portals/maps/tibet2.ent %buildroot/%gamedir/portals/maps/tibet2.ent
install -D -m644 gamecode-%gamecode_ver/mapfixes/portals/maps/tibet2.txt %buildroot/%gamedir/portals/maps/tibet2.txt
install -D -m644 gamecode-%gamecode_ver/mapfixes/portals/maps/tibet9.ent %buildroot/%gamedir/portals/maps/tibet9.ent
install -D -m644 gamecode-%gamecode_ver/mapfixes/portals/maps/tibet9.txt %buildroot/%gamedir/portals/maps/tibet9.txt

# Install the pak deltas
install -D -m644 gamecode-%gamecode_ver/patch111/patchdat/data1/data1pk0.xd3 %buildroot/%gamedir/patchdat/data1/data1pk0.xd3
install -D -m644 gamecode-%gamecode_ver/patch111/patchdat/data1/data1pk1.xd3 %buildroot/%gamedir/patchdat/data1/data1pk1.xd3
install -D -m644 gamecode-%gamecode_ver/patch111/patchdat.txt %buildroot/%gamedir/patchdat.txt

install -D -m644 engine/resource/hexen2.png %buildroot/%gamedir/hexen2.png

# Install the menu icon
install -D engine/resource/%name.png %buildroot%_niconsdir/%name.png
install -D 48.png %buildroot%_liconsdir/%name.png
install -D 16.png %buildroot%_miconsdir/%name.png

install -D -m 0644 %name.desktop  %buildroot%_desktopdir/%name.desktop

%files
%doc docs/*
%_bindir/*
%exclude %_bindir/*hw*
%gamedir/*
%exclude %gamedir/*hw* 
%_desktopdir/%name.desktop
%_iconsdir/hicolor/*/apps/*

%files -n hexenworld
%doc docs/*hw*
%_bindir/*hw*
%gamedir/*hw* 

%changelog
* Wed Apr 21 2021 Fr. Br. George <george@altlinux.ru> 1.5.9-alt3
- Submajor version update
- Brute force ix86 build

* Thu May 24 2012 Fr. Br. George <george@altlinux.ru> 1.4.3-alt3
- DSO list completion

* Mon Mar 14 2011 Fr. Br. George <george@altlinux.ru> 1.4.3-alt2
- Buildreq regenerated

* Mon Jun 07 2010 Fr. Br. George <george@altlinux.ru> 1.4.3-alt1
- Initial build from original src.rpm

* Fri Apr 04 2008 O.Sezer <sezero@users.sourceforge.net> 1.4.3-1
- 1.4.3-final.

* Tue Mar 25 2008 O.Sezer <sezero@users.sourceforge.net> 1.4.3-0.2.rc2
- 1.4.3-rc2.

* Thu Feb 07 2008 O.Sezer <sezero@users.sourceforge.net> 1.4.3-0.1.rc1
- 1.4.3-rc1.

* Wed Feb 05 2008 O.Sezer <sezero@users.sourceforge.net>
- incremented the gamecode version number to 1.19a

* Wed Oct 03 2007 O.Sezer <sezero@users.sourceforge.net> 1.4.2-1
- 1.4.2-final.

* Wed Sep 26 2007 O.Sezer <sezero@users.sourceforge.net> 1.4.2-0.6.rc3
- 1.4.2-rc3.

* Mon Aug 22 2007 O.Sezer <sezero@users.sourceforge.net>
- removed the .gtk1 suffix from launcher gtk-1.2 builds

* Sun Jul 22 2007 O.Sezer <sezero@users.sourceforge.net> 1.4.2-0.5.rc2
- 1.4.2-rc2.

* Fri Jun 15 2007 O.Sezer <sezero@users.sourceforge.net>
- The software renderer clients can now be compiled on non-intel.

* Sun May 20 2007 O.Sezer <sezero@users.sourceforge.net> 1.4.2-0.4.rc1
- 1.4.2-rc1.

* Tue Apr 10 2007 O.Sezer <sezero@users.sourceforge.net>
- xdelta now builds without autotools.

* Tue Apr 03 2007 O.Sezer <sezero@users.sourceforge.net> 1.4.2-0.3.pre3
- 1.4.2-pre3 prerelease.

* Tue Mar 20 2007 O.Sezer <sezero@users.sourceforge.net>
- xdelta version is 1.1.4: rename the binary properly.

* Tue Mar 20 2007 O.Sezer <sezero@users.sourceforge.net> 1.4.2-0
- 1.4.2-pre2 prerelease.

* Sun Mar 18 2007 O.Sezer <sezero@users.sourceforge.net>
- gamecode version changed to 1.17.

* Mon Feb 13 2007 O.Sezer <sezero@users.sourceforge.net> 1.4.2-0
- 1.4.2-pre1 prerelease.

* Mon Feb 05 2007 O.Sezer <sezero@users.sourceforge.net>
- xdelta is now included in the source tarball.

* Fri Dec 01 2006 O.Sezer <sezero@users.sourceforge.net> 1.4.1-2
- Version 1.4.1-rev1 :
  - Updated to gamedata-1.16a
  - Updated to xdelta-1.1.3b
  - Updated the URLs

* Wed Oct 18 2006 O.Sezer <sezero@users.sourceforge.net> 1.4.1-1
- Merged the hexen2 and mission pack packages.
- Added build option --without midi.
- Added build option --without alsa.
- Added build option --without asm.
- Disabled x86 assembly on non-intel cpus.
- Do not build or package the software renderer versions when not
  using x86 assembly until we fix them properly.
- Version 1.4.1-final.

* Wed Aug 14 2006 O.Sezer <sezero@users.sourceforge.net> 1.4.1-0
- Added the dedicated server to the packaged binaries.
  1.4.1-pre8. Preparing for a future 1.4.1 release.

* Tue Apr 18 2006 O.Sezer <sezero@users.sourceforge.net> 1.4.0-7
- More packaging tidy-ups for 1.4.0-final

* Sun Apr 16 2006 O.Sezer <sezero@users.sourceforge.net> 1.4.0-6
- Back to xdelta: removed loki_patch. All of its fancy bloat can
  be done in a shell script, which is more customizable.

* Mon Apr 04 2006 O.Sezer <sezero@users.sourceforge.net> 1.4.0-5
- Since 1.4.0-rc2 no mission pack specific binaries are needed.

* Mon Mar 26 2006 O.Sezer <sezero@users.sourceforge.net> 1.4.0-4
- Moved hexenworld related documentation to the hexenworld package
  lib3dfxgamma is no longer needed. not packaging it.

* Thu Mar 02 2006 O.Sezer <sezero@users.sourceforge.net> 1.4.0-3
- Added Features to the packaged documentation

* Wed Mar 01 2006 O.Sezer <sezero@users.sourceforge.net> 1.4.0-2
- Updated after the utilities reorganization

* Sun Feb 12 2006 O.Sezer <sezero@users.sourceforge.net> 1.4.0-1
- Updated for 1.4.0

* Thu Aug 29 2005 O.Sezer <sezero@users.sourceforge.net> 1.3.0-2
- Patch: We need to remove OS checks from the update_h2 script

* Thu Aug 21 2005 O.Sezer <sezero@users.sourceforge.net> 1.3.0-1
- First sketchy spec file for RedHat and Fedora Core

