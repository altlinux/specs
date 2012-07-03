%ifnarch %ix86
%define _without_asm 1
%endif

%define mk_build %make_build LDFLAGS="-lm -ldl"

%define desktop_vendor	uhexen2
%define gamecode_ver	1.19a
%define gamedir %_libdir/%name

Name: hexen2
License: GPL
Group: Games/Arcade
Version: 1.4.3
Release: alt3
Summary: Hexen II: Hammer of Thyrion
Url: http://uhexen2.sourceforge.net/
Source: http://download.sourceforge.net/uhexen2/hexen2source-%version.tgz
#Source1:	http://download.sourceforge.net/uhexen2/gamedata-src-%gamecode_ver.tgz
Source1: http://download.sourceforge.net/uhexen2/hexen2source-gamecode-%version.tgz
Source2: http://download.sourceforge.net/uhexen2/hexenworld-pakfiles-0.15.tgz
Patch:	hexen-MAX_OSPATH.patch

%{!?_without_asm:BuildRequires:  nasm >= 0.98}

# Automatically added by buildreq on Sun Jun 06 2010
BuildRequires: libGL-devel libSDL_mixer-devel libalsa-devel libgtk+2-devel zlib-devel

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
%if %{?_without_asm:1}0
sed -i 's/USE_X86_ASM=yes/USE_X86_ASM=no/' hexen2/Makefile hexenworld/Client/Makefile
%endif
#if %{?_without_alsa:1}0
#ed -i 's/USE_ALSA=yes/USE_ALSA=no/' hexen2/Makefile hexenworld/Client/Makefile
#endif
#if %{?_without_midi:1}0
#ed -i 's/USE_MIDI=yes/USE_MIDI=no/' hexen2/Makefile hexenworld/Client/Makefile
#endif

%patch -p1

%build

# Build the main game binaries
%mk_build -C hexen2 h2
%make -s -C hexen2 clean
%mk_build -C hexen2 glh2
%make -s -C hexen2 clean
# Build the dedicated server
%make_build -C hexen2 -f Makefile.sv
# HexenWorld binaries
%make_build -C hexenworld/Server
%mk_build -C hexenworld/Client hw
%make -s -C hexenworld/Client clean
%mk_build -C hexenworld/Client glhw
# HexenWorld master server
%make_build -C hexenworld/Master

# Build xdelta binary and its libraries: do this before
# building the launcher, it uses its object files.
%make_build -C xdelta11 -f Makefile.xd

# Launcher binaries
%make_build -C launcher
# Build the hcode compilers
%make_build -C utils/hcc_old
%make_build -C utils/hcc
# Build the game-code
utils/hcc_old/hcc -src gamecode-%gamecode_ver/hc/h2
utils/hcc_old/hcc -src gamecode-%gamecode_ver/hc/h2 -name progs2.src
utils/bin/hcc -src gamecode-%gamecode_ver/hc/portals -oi -on
utils/bin/hcc -src gamecode-%gamecode_ver/hc/hw -oi -on
#utils/bin/hcc -src gamecode-%gamecode_ver/hc/siege -oi -on

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

%install
install -D -m755 hexen2/h2ded %buildroot/%gamedir/h2ded
install -D -m755 hexen2/glhexen2 %buildroot/%gamedir/glhexen2
install -D -m755 hexen2/hexen2 %buildroot/%gamedir/hexen2
install -D -m755 hexenworld/Client/hwcl %buildroot/%gamedir/hwcl
install -D -m755 hexenworld/Client/glhwcl %buildroot/%gamedir/glhwcl
install -D -m755 hexenworld/Server/hwsv %buildroot/%gamedir/hwsv
install -D -m755 hexenworld/Master/hwmaster %buildroot/%gamedir/hwmaster
install -D -m755 launcher/h2launcher %buildroot/%gamedir/h2launcher
# Make a symlink of the game-launcher
mkdir -p %buildroot/%_bindir
ln -s %gamedir/h2launcher %buildroot/%_bindir/hexen2

# Install the gamedata
mkdir -p %buildroot/%gamedir/data1/
install -D -m644 gamecode-%gamecode_ver/hc/h2/progs.dat %buildroot/%gamedir/data1/progs.dat
install -D -m644 gamecode-%gamecode_ver/hc/h2/progs2.dat %buildroot/%gamedir/data1/progs2.dat
install -D -m644 gamecode-%gamecode_ver/txt/h2/hexen.rc %buildroot/%gamedir/data1/hexen.rc
install -D -m644 gamecode-%gamecode_ver/txt/h2/strings.txt %buildroot/%gamedir/data1/strings.txt
install -D -m644 gamecode-%gamecode_ver/txt/h2/default.cfg %buildroot/%gamedir/data1/default.cfg
mkdir -p %buildroot/%gamedir/portals/
install -D -m644 gamecode-%gamecode_ver/hc/portals/progs.dat %buildroot/%gamedir/portals/progs.dat
install -D -m644 gamecode-%gamecode_ver/txt/portals/hexen.rc %buildroot/%gamedir/portals/hexen.rc
install -D -m644 gamecode-%gamecode_ver/txt/portals/strings.txt %buildroot/%gamedir/portals/strings.txt
install -D -m644 gamecode-%gamecode_ver/txt/portals/infolist.txt %buildroot/%gamedir/portals/infolist.txt
install -D -m644 gamecode-%gamecode_ver/txt/portals/maplist.txt %buildroot/%gamedir/portals/maplist.txt
install -D -m644 gamecode-%gamecode_ver/txt/portals/puzzles.txt %buildroot/%gamedir/portals/puzzles.txt
install -D -m644 gamecode-%gamecode_ver/txt/portals/default.cfg %buildroot/%gamedir/portals/default.cfg
mkdir -p %buildroot/%gamedir/hw/
install -D -m644 gamecode-%gamecode_ver/hc/hw/hwprogs.dat %buildroot/%gamedir/hw/hwprogs.dat
install -D -m644 gamecode-%gamecode_ver/txt/hw/strings.txt %buildroot/%gamedir/hw/strings.txt
install -D -m644 gamecode-%gamecode_ver/txt/hw/default.cfg %buildroot/%gamedir/hw/default.cfg
install -D -m644 hw/pak4.pak %buildroot/%gamedir/hw/pak4.pak

# Install the xdelta updates
mkdir -p %buildroot/%gamedir/patchdata/
mkdir -p %buildroot/%gamedir/patchdata/data1
install -D -m755 gamecode-%gamecode_ver/pak_v111/update_xdelta.sh %buildroot/%gamedir/update_xdelta.sh
install -D -m644 gamecode-%gamecode_ver/pak_v111/patchdata/data1/data1pak0.xd %buildroot/%gamedir/patchdata/data1/data1pak0.xd
install -D -m644 gamecode-%gamecode_ver/pak_v111/patchdata/data1/data1pak1.xd %buildroot/%gamedir/patchdata/data1/data1pak1.xd

# Install the update-patcher binaries
install -D -m755 xdelta11/xdelta %buildroot/%gamedir/xdelta114

# Install the menu icon
mkdir -p %buildroot/%_datadir/pixmaps
install -D -m644 hexen2/icons/h2_32x32x4.png %buildroot/%_datadir/pixmaps/%name.png

install -D -m 0644 %name.desktop  %buildroot%_desktopdir/%name.desktop

%files
%doc docs/*
#exclude %_defaultdocdir/%name-%version/README.hw*
%gamedir/h2ded
%gamedir/hexen2
%gamedir/glhexen2
%gamedir/xdelta114
%gamedir/update_xdelta.sh
%gamedir/patchdata/data1/data1pak0.xd
%gamedir/patchdata/data1/data1pak1.xd
%gamedir/data1/progs.dat
%gamedir/data1/progs2.dat
%gamedir/data1/hexen.rc
%gamedir/data1/strings.txt
%gamedir/data1/default.cfg
%gamedir/portals/progs.dat
%gamedir/portals/hexen.rc
%gamedir/portals/strings.txt
%gamedir/portals/puzzles.txt
%gamedir/portals/infolist.txt
%gamedir/portals/maplist.txt
%gamedir/portals/default.cfg
%_bindir/hexen2
%_datadir/pixmaps/%name.png
%gamedir/h2launcher
%_desktopdir/%name.desktop

%files -n hexenworld
%doc docs/README.hw*
%gamedir/hwsv
%gamedir/hwmaster
%gamedir/hwcl
%gamedir/glhwcl
%gamedir/hw/hwprogs.dat
%gamedir/hw/pak4.pak
%gamedir/hw/strings.txt
%gamedir/hw/default.cfg

%changelog
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

