# vim: set ft=spec: -*- rpm-spec -*-
# $Id: quakeforge,v 1.22 2006/03/08 15:19:45 raorn Exp $

%def_disable static
%def_disable debug

# Brain damaged lib/plugin system...
%set_verify_elf_method unresolved=relaxed

%define nqver 1.09
%define qwver 2.40

Name: quakeforge
Version: 0.5.5
Release: alt11.1
Summary: QuakeForge 3D game engine
Group: Games/Arcade
License: GPL
URL: http://quakeforge.net/

Packager: Afanasov Dmitry <ender@altlinux.org>

Source: %name-git.tar

Source1: %name.conf
Source2: pakQF.pak

# cpp is unusable with ccache-bte :-(
BuildConflicts: ccache-bte < 1.9-alt3.2

# Automatically added by buildreq on Mon Apr 14 2008
BuildRequires: flex gcc-c++ libSDL-devel libSM-devel libX11-devel libGL-devel libXext-devel libXi-devel libXxf86dga-devel libXxf86vm-devel libalsa-devel libcurl-devel libflac-devel libncurses-devel libpng-devel libvorbis-devel
BuildRequires: libsamplerate-devel
BuildRequires: libwildmidi-devel

%{?_enable_static:BuildPreReq: glibc-devel-static}

%description
QuakeForge is a source port of Quake and QuakeWorld, the successors to id
Software's very popular DOOM series. Its primary development goal is to
remain compatible with the original games released by id Software while
adding portability and optional extensions to enhance gameplay.

%package doc
Summary: QuakeForge 3D game engine - documentation
Group: Games/Arcade
Requires: %name = %version-%release

%description doc
QuakeForge is a source port of Quake and QuakeWorld, the successors to id
Software's very popular DOOM series. Its primary development goal is to
remain compatible with the original games released by id Software while
adding portability and optional extensions to enhance gameplay.

%package libs
Summary: QuakeForge 3D game engine - common libraries
Group: System/Libraries
Requires: %name = %version-%release
Obsoletes: %name-common

%description libs
QuakeForge is a source port of Quake and QuakeWorld, the successors to id
Software's very popular DOOM series. Its primary development goal is to
remain compatible with the original games released by id Software while
adding portability and optional extensions to enhance gameplay.

%package servers
Summary: QuakeForge 3D game engine - servers
Group: Games/Arcade
Requires: %name = %version-%release
Requires: %name-libs = %version-%release
Provides: quakeforge-server = %version-%release
Provides: quake-server = %nqver
Provides: quakeworld-server = %qwver

%description servers
QuakeForge is a source port of Quake and QuakeWorld, the successors to id
Software's very popular DOOM series. Its primary development goal is to
remain compatible with the original games released by id Software while
adding portability and optional extensions to enhance gameplay.

%package glx
Summary: QuakeForge 3D game engine - glx client
Group: Games/Arcade
Requires: %name = %version-%release
Requires: %name-libs = %version-%release
Requires: %name-libs-gl = %version-%release
Provides: %name-client = %version-%release
Provides: %name-gl-client = %version-%release
Provides: quake-client = %nqver
Provides: quakeworld-client = %qwver

%description glx
QuakeForge is a source port of Quake and QuakeWorld, the successors to id
Software's very popular DOOM series. Its primary development goal is to
remain compatible with the original games released by id Software while
adding portability and optional extensions to enhance gameplay.

%package cd-sdl
Summary: QuakeForge 3D game engine - SDL CD plugin
Group: Games/Arcade
Requires: %name = %version-%release
Requires: %name-client

%description cd-sdl
QuakeForge is a source port of Quake and QuakeWorld, the successors to id
Software's very popular DOOM series. Its primary development goal is to
remain compatible with the original games released by id Software while
adding portability and optional extensions to enhance gameplay.

%package sdl
Summary: QuakeForge 3D game engine - SDL client
Group: Games/Arcade
Requires: %name = %version-%release
Requires: %name-libs = %version-%release
Requires: %name-libs-sw = %version-%release
Provides: %name-client = %version-%release
Provides: %name-sw-client = %version-%release
Provides: quake-client = %nqver
Provides: quakeworld-client = %qwver

%description sdl
QuakeForge is a source port of Quake and QuakeWorld, the successors to id
Software's very popular DOOM series. Its primary development goal is to
remain compatible with the original games released by id Software while
adding portability and optional extensions to enhance gameplay.

%package sdl32
Summary: QuakeForge 3D game engine - SDL client
Group: Games/Arcade
Requires: %name = %version-%release
Requires: %name-libs-sw = %version-%release
Provides: %name-client = %version-%release
Provides: %name-sw-client = %version-%release
Provides: quake-client = %nqver
Provides: quakeworld-client = %qwver

%description sdl32
QuakeForge is a source port of Quake and QuakeWorld, the successors to id
Software's very popular DOOM series. Its primary development goal is to
remain compatible with the original games released by id Software while
adding portability and optional extensions to enhance gameplay.

%package sgl
Summary: QuakeForge 3D game engine - SDL-GL client
Group: Games/Arcade
Requires: %name = %version-%release
Requires: %name-libs = %version-%release
Requires: %name-libs-gl = %version-%release
Provides: %name-client = %version-%release
Provides: %name-gl-client = %version-%release
Provides: quake-client = %nqver
Provides: quakeworld-client = %qwver

%description sgl
QuakeForge is a source port of Quake and QuakeWorld, the successors to id
Software's very popular DOOM series. Its primary development goal is to
remain compatible with the original games released by id Software while
adding portability and optional extensions to enhance gameplay.

%package x11
Summary: QuakeForge 3D game engine - X11 client
Group: Games/Arcade
Requires: %name = %version-%release
Requires: %name-libs = %version-%release
Requires: %name-libs-sw = %version-%release
Provides: %name-client = %version-%release
Provides: %name-sw-client = %version-%release
Provides: quake-client = %nqver
Provides: quakeworld-client = %qwver

%description x11
QuakeForge is a source port of Quake and QuakeWorld, the successors to id
Software's very popular DOOM series. Its primary development goal is to
remain compatible with the original games released by id Software while
adding portability and optional extensions to enhance gameplay.

%package snd-alsa
Summary: ALSA sound plugin for QuakeForge
Group: Games/Arcade
Requires: %name = %version-%release
Requires: %name-client

%description snd-alsa
QuakeForge is a source port of Quake and QuakeWorld, the successors to id
Software's very popular DOOM series. Its primary development goal is to
remain compatible with the original games released by id Software while
adding portability and optional extensions to enhance gameplay.

The ALSA plugin for QuakeForge provides digital audio output for QuakeForge
targets that contain clients.

%package snd-oss
Summary: OSS sound plugin for QuakeForge
Group: Games/Arcade
Requires: %name = %version-%release
Requires: %name-client

%description snd-oss
QuakeForge is a source port of Quake and QuakeWorld, the successors to id
Software's very popular DOOM series. Its primary development goal is to
remain compatible with the original games released by id Software while
adding portability and optional extensions to enhance gameplay.

The OSS plugin for QuakeForge provides digital audio output (using OSS/Linux,
OSS/Free, or kernel sound) for QuakeForge targets that contain clients.

NOTE: This plugin does not work on all systems, since it uses memory-mapped
I/O for the output device. If you have trouble, try the quakeforge-alsa
package.

%package snd-sdl
Summary: SDL sound plugin for QuakeForge
Group: Games/Arcade
Requires: %name = %version-%release
Requires: %name-client

%description snd-sdl
QuakeForge is a source port of Quake and QuakeWorld, the successors to id
Software's very popular DOOM series. Its primary development goal is to
remain compatible with the original games released by id Software while
adding portability and optional extensions to enhance gameplay.

The SDL plugin for QuakeForge provides digital audio output for QuakeForge
targets that contain clients.

%package snd-disk
Summary: Diskwriter sound plugin for QuakeForge
Group: Games/Arcade
Requires: %name = %version-%release
Requires: %name-client

%description snd-disk
QuakeForge is a source port of Quake and QuakeWorld, the successors to id
Software's very popular DOOM series. Its primary development goal is to
remain compatible with the original games released by id Software while
adding portability and optional extensions to enhance gameplay.

The Diskwriter plugin for QuakeForge provides digital audio output for
QuakeForge targets that contain clients.

%package libs-gl
Summary: QuakeForge 3D game engine - OpenGL renderer libraries
Group: Games/Arcade
Requires: %name = %version-%release
Requires: %name-libs = %version-%release
Requires: %name-gl-client

%description libs-gl
QuakeForge is a source port of Quake and QuakeWorld, the successors to id
Software's very popular DOOM series. Its primary development goal is to
remain compatible with the original games released by id Software while
adding portability and optional extensions to enhance gameplay.

%package libs-sw
Summary: QuakeForge 3D game engine - Software renderer libraries
Group: Games/Arcade
Requires: %name = %version-%release
Requires: %name-libs = %version-%release
Requires: %name-sw-client

%description libs-sw
QuakeForge is a source port of Quake and QuakeWorld, the successors to id
Software's very popular DOOM series. Its primary development goal is to
remain compatible with the original games released by id Software while
adding portability and optional extensions to enhance gameplay.

%package cd-linux
Summary: QuakeForge 3D game engine - linux CD plugin
Group: Games/Arcade
Requires: %name = %version-%release
Requires: %name-client

%description cd-linux
QuakeForge is a source port of Quake and QuakeWorld, the successors to id
Software's very popular DOOM series. Its primary development goal is to
remain compatible with the original games released by id Software while
adding portability and optional extensions to enhance gameplay.

%package devel
Summary: QuakeForge 3D game engine - headers and development libraries
Group: Development/C
Requires: %name = %version-%release

%description devel
QuakeForge is a source port of Quake and QuakeWorld, the successors to id
Software's very popular DOOM series. Its primary development goal is to
remain compatible with the original games released by id Software while
adding portability and optional extensions to enhance gameplay.

%if_enabled static
%package devel-static
Summary: QuakeForge 3D game engine - static libraries
Group: Development/C
Requires: %name-devel = %version-%release

%description devel-static
QuakeForge is a source port of Quake and QuakeWorld, the successors to id
Software's very popular DOOM series. Its primary development goal is to
remain compatible with the original games released by id Software while
adding portability and optional extensions to enhance gameplay.
%endif

%package -n qfcc
Summary: QuakeForge QuakeC/Ruamoko compiler
Group: Development/Other
Requires: %name-libs = %version-%release
Requires: cpp

%description -n qfcc
QuakeForge is a source port of Quake and QuakeWorld, the successors to id
Software's very popular DOOM series. Its primary development goal is to
remain compatible with the original games released by id Software while
adding portability and optional extensions to enhance gameplay.

qfcc is QuakeForge's extended qcc compiler. It is mostly compatable with id
Software's qcc, but due to extentions and subtle semantics changes, the
language it compiles is call Ruamoko.

%package -n pak
Summary: QuakeForge pakfile managing tool
Group: Archiving/Other
Requires: %name-libs = %version-%release

%description -n pak
QuakeForge is a source port of Quake and QuakeWorld, the successors to id
Software's very popular DOOM series. Its primary development goal is to
remain compatible with the original games released by id Software while
adding portability and optional extensions to enhance gameplay.

pak is a simple tar-like tool for managing pak files.
wad is a simple tar-like tool for managing wad files.

%package utils
Summary: Miscellaneous QuakeForge utilites
Group: File tools
Requires: %name-libs = %version-%release

%description utils
This package contains several tools for use with QuakeForge:

 * qfwavinfo, a tool to assist in converting "looped" WAV files to Ogg
   Vorbis.

%package maptools
Summary: Quake mapping tools from the QuakeForge Project
Group: File tools
Requires: %name-libs = %version-%release

%description maptools
This package contains QuakeForge's versions of the tools Id Software used
to create maps for the Quake engine. Included are:

 * bsp2img, a program for converting Quake I BSP's to a bitmap (map!) of the
   level
 * qfbsp, a program for compiling a map file into a BSP tree.
 * qflight, a program for generating lightmaps from the static lights in a
   BSP file.
 * qfmodelgen, a program for generating a .mdl file from a base triangle file
   (.tri), a texture containing front and back skins (.lbm), and a series of
   frame triangle files (.tri).
 * qfvis, a program for generating the Possibly-Visible Set information from
   a BSP and a portal information file (generated by qfbsp).

%prep
%setup -q -n %name

%build
./bootstrap
# Targets selection

%{?!_enable_static:export lt_cv_prog_cc_static_works=no}
%configure \
  --with-global-cfg=%_sysconfdir/%name.conf \
  --with-user-cfg=~/.%{name}rc \
  --with-sharepath=%_gamesdatadir/%name \
  --with-userpath=~/.%name \
  --with-plugin-path=%_libdir/%name \
  --enable-shared \
  %{subst_enable static} \
  %{subst_enable debug} \
  --disable-jack \
  --with-clients="glx,sdl,sdl32,sgl,x11" \
  --with-tools="bsp2img,carne,pak,qfbsp,qfcc,qflight,qfmodelgen,qfvis,wad,wav"
#                 3dfx,fbdev,glx,mgl,sdl,sdl32,sgl,svga,wgl,x11
#               bsp2img,carne,gsc,pak,qfbsp,qfcc,qflight,qfmodelgen,qfvis,qwaq,wad,wav

%make_build

%install
%make_install DESTDIR=%buildroot install

mkdir -p %buildroot{%_sysconfdir,%_gamesdatadir/%name/QF}
install -m644 %SOURCE1 %buildroot%_sysconfdir
install -m644 %SOURCE2 %buildroot%_gamesdatadir/%name/QF

# Collect some garbage...
#  Clean plugins
find %buildroot%_libdir/%name \( -name '*.a' -o -name '*.la' \) -print0 | \
	xargs -r0 rm -rvf --

%files
%doc COPYING INSTALL NEWS TODO
%config(noreplace) %_sysconfdir/%name.conf
%dir %_gamesdatadir/%name
%dir %_gamesdatadir/%name/QF
%_gamesdatadir/%name/QF/menu.dat*
%_gamesdatadir/%name/QF/menu.plist*
%_gamesdatadir/%name/QF/*.pak
%_gamesdatadir/%name/QF/menu.sym.*

%files doc
%doc doc/*

%files libs
%_libdir/libQFcd.so.*
%_libdir/libQFsound.so.*
%_libdir/libQFconsole.so.*
%_libdir/libQFgamecode.so.*
%_libdir/libQFgib.so.*
%_libdir/libQFimage.so.*
%_libdir/libQFjs.so.*
%_libdir/libQFmodels.so.*
%_libdir/libQFruamoko.so.*
%_libdir/libQFutil.so.*
%dir %_libdir/%name
%_libdir/%name/cd_file.so
%_libdir/%name/console_client.so
%_libdir/%name/snd_render_default.so

%files libs-gl
%_libdir/libQFmodels_gl.so.*
%_libdir/libQFrenderer_gl.so.*

%files libs-sw
%_libdir/libQFmodels_sw.so.*
%_libdir/libQFrenderer_sw32.so.*

%files servers
%_bindir/qw-server
%_bindir/nq-server
%_bindir/qw-master
%_bindir/hw-master
%_bindir/qtv
%_libdir/%name/console_server.so

%files cd-linux
%_libdir/%name/cd_linux.so

%files cd-sdl
%_libdir/%name/cd_sdl.so

%files glx
%_bindir/qw-client-glx
%_bindir/nq-glx

%files x11
%_bindir/qw-client-x11
%_bindir/nq-x11

%files sdl
%_bindir/qw-client-sdl
%_bindir/nq-sdl

%files sdl32
%_bindir/qw-client-sdl32
%_bindir/nq-sdl32

%files sgl
%_bindir/qw-client-sgl
%_bindir/nq-sgl

%files snd-alsa
%_libdir/%name/snd_output_alsa*.so

%files snd-oss
%_libdir/%name/snd_output_oss.so

%files snd-sdl
%_libdir/%name/snd_output_sdl.so

%files snd-disk
%_libdir/%name/snd_output_disk.so

%files devel
%_libdir/libQFcd.so
%_libdir/libQFsound.so
%_libdir/libQFconsole.so
%_libdir/libQFgamecode.so
%_libdir/libQFgib.so
%_libdir/libQFimage.so
%_libdir/libQFjs.so
%_libdir/libQFmodels.so
%_libdir/libQFmodels_gl.so
%_libdir/libQFrenderer_gl.so
%_libdir/libQFmodels_sw.so
%_libdir/libQFrenderer_sw32.so
%_libdir/libQFruamoko.so
%_libdir/libQFutil.so
%dir %_includedir/QF
%dir %_includedir/QF/GL
%dir %_includedir/QF/plugin
%_includedir/QF/GL/*.h
%_includedir/QF/plugin/*.h
%_includedir/QF/*.h
%_pkgconfigdir/quakeforge.pc

%if_enabled static
%files devel-static
%_libdir/libQFcd.a
%_libdir/libQFsound.a
%_libdir/libQFconsole.a
%_libdir/libQFgamecode.a
%_libdir/libQFgib.a
%_libdir/libQFimage.a
%_libdir/libQFjs.a
%_libdir/libQFmodels.a
%_libdir/libQFmodels_gl.a
%_libdir/libQFrenderer_gl.a
%_libdir/libQFmodels_sw.a
%_libdir/libQFrenderer_sw32.a
%_libdir/libQFruamoko.a
%_libdir/libQFutil.a
%endif

%files -n qfcc
%_bindir/qfcc
%_bindir/qfpreqcc
%_bindir/qfprogs
%_man1dir/qfcc.1*
%_libdir/qfcc
%_pkgconfigdir/qfcc.pc

%files -n pak
%_bindir/pak
%_bindir/wad
%_man1dir/pak.1*
%_man1dir/wad.1*

%files utils
%_bindir/qfwavinfo
%_bindir/qfpc
%_bindir/zpak
%_man1dir/zpak.*

%files maptools
%_bindir/bsp2img
%_bindir/qfbsp
%_bindir/qflight
%_bindir/qfmodelgen
%_bindir/qfvis
%_man1dir/qflight.1*
%_man1dir/qfvis.1*

%changelog
* Sat Oct 22 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.5.5-alt11.1
- Rebuild with Python-2.7

* Wed Jan 26 2011 Afanasov Dmitry <ender@altlinux.org> 0.5.5-alt11
- git commit c0b8d0fe (upstream switches to git)

* Tue Dec 02 2008 Valery Inozemtsev <shrek@altlinux.ru> 0.5.5-alt10.1
- NMU:
  * updated build dependencies

* Mon Apr 14 2008 Sir Raorn <raorn@altlinux.ru> 0.5.5-alt10
- SVN revision 11761
- Disabled fbdev target and xmms plugin

* Thu Aug 23 2007 Sir Raorn <raorn@altlinux.ru> 0.5.5-alt9
- SVN revision 11720
 + Added pkgconfig files
 + Fixed console plugin linking

* Wed May 30 2007 Sir Raorn <raorn@altlinux.ru> 0.5.5-alt8
- SVN revision 11706

* Sat Jan 06 2007 Sir Raorn <raorn@altlinux.ru> 0.5.5-alt7
- SVN revision 11344

* Mon Sep 11 2006 Sir Raorn <raorn@altlinux.ru> 0.5.5-alt6
- SVN revision 11274

* Tue Jun 20 2006 Sir Raorn <raorn@altlinux.ru> 0.5.5-alt5
- SVN snapshot 20060524

* Wed Mar 08 2006 Sir Raorn <raorn@altlinux.ru> 0.5.5-alt4.1
- VERIFY_ELF_UNRESOLVED set to "relaxed" :-(

* Fri Mar 03 2006 Sir Raorn <raorn@altlinux.ru> 0.5.5-alt4
- SVN snapshot 20060118
- Removed patches (merged upstream):
 + alt-missionpack-gamedir
- spec cleanup, disabled conditional builds
- BuildRequires updated for Xorg7

* Sat Feb 12 2005 Sir Raorn <raorn@altlinux.ru> 0.5.5-alt3
- CVS snapshot 20050210
- Fixed -game issue with -hipnotic/-rogue/-abyss

* Sat Jan 29 2005 Sir Raorn <raorn@altlinux.ru> 0.5.5-alt2
- CVS snapshot 20050126

* Tue May 04 2004 Sir Raorn <raorn@altlinux.ru> 0.5.5-alt1
- [0.5.5]
- Added qtv to -servers package

* Tue Apr 20 2004 Sir Raorn <raorn@altlinux.ru> 0.5.4-alt9
- CVS snapshot 20040416

* Sun Feb 15 2004 Sir Raorn <raorn@altlinux.ru> 0.5.4-alt8
- CVS snapshot 20040214
- Removed qfdefs (upstream)
- Added qfpreqcc to qfcc package
- Added wad tool to pak package

* Sun Dec 21 2003 Sir Raorn <raorn@altlinux.ru> 0.5.4-alt7
- CVS snapshot 20031219
- devel-static and *.la fixes

* Mon Nov 10 2003 Sir Raorn <raorn@altlinux.ru> 0.5.4-alt6
- CVS snapshot 20031103

* Sun Sep 07 2003 Sir Raorn <raorn@altlinux.ru> 0.5.4-alt5
- CVS snapshot 20030907
- BuildRequires updated

* Sat Jul 19 2003 Sir Raorn <raorn@altlinux.ru> 0.5.4-alt4
- [0.5.4]

* Thu May 01 2003 Sir Raorn <raorn@altlinux.ru> 0.5.2-alt3
- CVS snapshot 20030501
- New maptools: bsp2img and qfmodelgen
- Removed versions from requires to virtual packages (confuses apt)

* Wed Oct 16 2002 Stanislav Ievlev <inger@altlinux.ru> 0.5.2-alt2
- rebuild without svgalib (I had to turn off both svga and 3dfx targets)

* Thu Oct 10 2002 Sir Raorn <raorn@altlinux.ru> 0.5.2-alt1
- [0.5.2]
- qfbsp, qflight and qfvis are moved to -maptools subpackage
- qfwavinfo included in -utils subpackage
- Updated build dependencies

* Sun Sep 22 2002 Sir Raorn <raorn@altlinux.ru> 0.5.1-alt0.12.20020922
- CVS snapshot 20020922
- More BSP utils

* Sat Sep 14 2002 Sir Raorn <raorn@altlinux.ru> 0.5.1-alt0.11.20020913
- CVS snapshot 20020913
- Added BSP utils to -utils subpackage

* Sun Aug 25 2002 Sir Raorn <raorn@altlinux.ru> 0.5.1-alt0.10.20020824
- Disabling optimization with gcc 3.2 was Bad Idea(tm)

* Sun Aug 25 2002 Sir Raorn <raorn@altlinux.ru> 0.5.1-alt0.9.20020824
- Rebuild with --disable-optimize

* Sun Aug 25 2002 Sir Raorn <raorn@altlinux.ru> 0.5.1-alt0.8.20020824
- CVS snapshot 20020824
- Select gcc version to build with

* Sun Aug 18 2002 Sir Raorn <raorn@altlinux.ru> 0.5.1-alt0.7.20020818
- CVS snapshot 20020818
- sgl target is back
- qfdefs is back (now in -utils subpackage)
- New -utils subpackage
- Added some %%dir's in filelist (plugins and includes)
- Set attributes r-s--x--x on suid-root binaries

* Sun Aug 04 2002 Sir Raorn <raorn@altlinux.ru> 0.5.1-alt0.6.20020802
- Updated interpackage requires
- Back to compat-gcc (with 3.1.1 weapon model disappears)

* Sat Aug 03 2002 Sir Raorn <raorn@altlinux.ru> 0.5.1-alt0.5.20020802
- CVS snapshot 20020802
- Updated autotools requires
- sgl target temporary disabled (broken in CVS)
- qfdefs temporary disabled (broken in CVS)
- Dances around configure

* Sat Jun 29 2002 Sir Raorn <raorn@altlinux.ru> 0.5.1-alt0.4.20020628
- CVS snapshot 20020628
- qfpreqcc dropped
- Spec cleanup, added some comments about clent selection
- BuildPreReq updated (buildreqs really SUCKS)

* Sat Jun 08 2002 Sir Raorn <raorn@altlinux.ru> 0.5.1-alt0.3.20020607
- CVS snapshot 20020607
- Addes qfprogs utility and pak manpage to filelist

* Thu May 02 2002 Sir Raorn <raorn@altlinux.ru> 0.5.1-alt0.2.20020501
- CVS snapshot 20020501
- s/BuildRequires/BuildPreReq/g

* Sat Apr 13 2002 Sir Raorn <raorn@altlinux.ru> 0.5.1-alt0.2.20020412
- CVS snapshot 20020412
- Release changed

* Sun Mar 31 2002 Sir Raorn <raorn@altlinux.ru> 0.5.1-alt0.pre.20020329.1
- CVS snapshot 20020329
- pak package

* Sun Feb 24 2002 Sir Raorn <raorn@altlinux.ru> 0.5.1-alt0.pre.20020222.2
- Provides {quake,quakeworld}-{client,server}

* Sat Feb 23 2002 Sir Raorn <raorn@altlinux.ru> 0.5.1-alt0.pre.20020222.1
- CVS snapshot 20020222
- 3dfx subpackage
- more %%if's for packages
- BuildRequires
- spec cleanup

* Thu Feb 21 2002 Sir Raorn <raorn@altlinux.ru> 0.5.1-alt0.pre.20020221.1
- CVS snapshot 20020221
- qfdefs and qfpreqcc
- doc subpackage
- common -> libs
- devel-static subpackage

* Sat Feb 16 2002 Sir Raorn <raorn@altlinux.ru> 0.5.1-alt0.pre.20020208.2
- Spec cleanup

