%define _unpackaged_files_terminate_build 1

%define _user _q3
%define _group _q3
%define _home %_localstatedir/%name

# compatibility with upstream binaries (see Makefile)
%define __arch %(uname -m | sed -e 's/aarch64/arm64/' -e 's/i.86/x86/')

Name: quake3
Version: 1.36
Release: alt9.git3fb9006e

Summary: Libre game engine compatible with Quake 3 Arena
License: GPL-2.0-or-later
Group: Games/Arcade
Url: https://ioquake3.org
VCS: https://github.com/ioquake/ioq3.git

Source: quake3-%version.tar

Source10: quake3.init
Source11: quake3.sysconfig
Source12: quake3-ctf.init
Source13: quake3-ctf.sysconfig

Patch0: quake3-alt-no-pie.patch
Patch1: quake3-alt-riscv64-loongarch64.patch
Patch2: quake3-debian-modules-to-libs.patch
Patch3: quake3-alt-constexpr-c23.patch

Requires: quake3-server = %EVR
Requires: quake3-common = %EVR

BuildRequires: libcurl-devel
BuildRequires: libopenal-devel
BuildRequires: libjpeg-devel
BuildRequires: libopus-devel
BuildRequires: libopusfile-devel
BuildRequires: libSDL2-devel
BuildRequires: libvorbis-devel
BuildRequires: zlib-devel

Obsoletes: quake3-client-up
Provides: quake3-client-up = %EVR

Obsoletes: quake3-client-smp
Provides: quake3-client-smp = %EVR

Obsoletes: quake3-client
Provides: quake3-client = %EVR

%description
Metapackage for libre game engine compatible with Quake 3 Arena.

%description -l ru_RU.UTF-8
Метапакет для свободного игрового движка совместимого с Quake 3 Arena.

%package common
Summary: Common files for libre game engine compatible with Quake 3 Arena
Group: Games/Arcade

%description common
Game engine for video game called in market name as Quake 3 Arena. Originally
developed by ID Software as proprietary software. In 2005 published as free
software and maintained by community. This package contains common files.

%description common -l ru_RU.UTF-8
Игровой движок для видеоигры под рыночным названием Quake 3 Arena. Изначально
разработанный фирмой ID Software как проприетарное ПО. В 2005 опубликован как
свободное ПО и поддерживается сообществом. Этот пакет содержит общие файлы.

%package server
Summary: Dedicated server for libre game engine compatible with Quake 3 Arena
Group: Games/Arcade

Requires: quake3-common = %EVR

%description server
%summary.

%description server -l ru_RU.UTF-8
Выделенный сервер для свободного игрового движка совместимого с Quake 3 Arena.

%prep
%setup
%autopatch -p1

%ifarch %e2k
sed -i "/#define ARCH_STRING \"sh\"/a\\\n#elif defined __e2k__\n#define ARCH_STRING \"e2k\"" \
  code/qcommon/q_platform.h
%endif

# compatibility with previous ALT releases
sed -i 's,ioquake3,quake3,g' misc/setup/ioquake3.desktop

# remove bundled code
pushd code
rm -rf \
  AL \
  autoupdater \
  curl-* \
  jpeg-* \
  libogg-* \
  libs \
  libvorbis-* \
  opus-* \
  opusfile-* \
  SDL2 \
  web \
  zlib \
  #
popd

%build
%define build_options \\\
  BUILD_CLIENT_SMP=1 \\\
  USE_CODEC_VORBIS=1 \\\
  USE_INTERNAL_JPEG=0 \\\
  USE_INTERNAL_OGG=0 \\\
  USE_INTERNAL_OPUS=0 \\\
  USE_INTERNAL_VORBIS=0 \\\
  USE_INTERNAL_ZLIB=0 \\\
  USE_LOCAL_HEADERS=0 \\\
%nil

%make_build release V=1 \
  %build_options \
  #

%install
mkdir -p %buildroot%_bindir/

install -p -D -m644 misc/setup/ioquake3.desktop \
  %buildroot%_datadir/applications/quake3.desktop

cat << __EOF__ > %buildroot%_bindir/quake3
#!/bin/sh

%_libdir/quake3/ioquake3.%__arch +set sv_pure 0 +set vm_cgame 0 +set vm_game 0 +set vm_ui 0 $@
__EOF__

chmod +x %buildroot%_bindir/quake3
ln -sf %_libdir/quake3/ioq3ded.%__arch %buildroot%_bindir/q3ded

install -D -p -m 0644 misc/quake3.png %buildroot%_niconsdir/quake3.png

mkdir -p %buildroot%_libdir/quake3/baseq3/
make copyfiles COPYDIR="%buildroot%_libdir/quake3" V=1 \
  %build_options \
  #

# initscript for dedicated server
install -pDm0644 %SOURCE11 %buildroot%_sysconfdir/sysconfig/quake3
install -pDm0644 %SOURCE13 %buildroot%_sysconfdir/sysconfig/quake3-ctf
install -pDm0755 %SOURCE10 %buildroot%_initdir/quake3
install -pDm0755 %SOURCE12 %buildroot%_initdir/quake3-ctf

install -dm1700 %buildroot%_home/

%pre server
/usr/sbin/groupadd -r -f %_group ||:
/usr/sbin/useradd -g %_group -c 'The quake3 user' \
  -d %_home -s /dev/null -r %_user >/dev/null 2>&1 ||:

%post server
%post_service quake3
%post_service quake3-ctf

%preun server
%preun_service quake3
%preun_service quake3-ctf

%files
%doc ChangeLog opengl2-readme.md
%_bindir/quake3
%_datadir/applications/quake3.desktop
%_libdir/quake3/ioquake3.%__arch
%_libdir/quake3/renderer_opengl1_%__arch.so
%_libdir/quake3/renderer_opengl2_%__arch.so
%_niconsdir/quake3.png

%files common
%dir %_libdir/quake3/
%dir %_libdir/quake3/baseq3/
%_libdir/quake3/baseq3/cgame%__arch.so
%_libdir/quake3/baseq3/qagame%__arch.so
%_libdir/quake3/baseq3/ui%__arch.so
%dir %_libdir/quake3/missionpack/
%_libdir/quake3/missionpack/cgame%__arch.so
%_libdir/quake3/missionpack/qagame%__arch.so
%_libdir/quake3/missionpack/ui%__arch.so

%files server
%_bindir/q3ded
%_initdir/quake3*
%_libdir/quake3/ioq3ded.%__arch
%config(noreplace) %_sysconfdir/sysconfig/*
%dir %attr(1770,root,%_group) %_home

%changelog
* Sat Jul 04 2026 Anton Osipov <radiolamp@altlinux.org> 1.36-alt9.git3fb9006e
- Fix FTBFS with GCC 15 (C23 constexpr keyword conflict).

* Mon Feb 03 2025 Constantin Sunzow <protvin@altlinux.org> 1.36-alt8.git3fb9006e
- Fix FTBFS: new intermediate release from upstream main branch.
- Fix License tag according to SPDX.
- Compliance with Services Policy.

* Fri Dec 01 2023 Ivan A. Melnikov <iv@altlinux.org> 1.36-alt7.svn2349
- Build on %%arm

* Tue Nov 28 2023 Ivan A. Melnikov <iv@altlinux.org> 1.36-alt6.svn2349
- Build on loongarch64 and riscv64

* Mon Jun 21 2021 Ilya Kurdyukov <ilyakurdyukov@altlinux.org> 1.36-alt5.svn2349
- fixed build on Elbrus
- corrected the license

* Fri Apr 23 2021 Slava Aseev <ptrnine@altlinux.org> 1.36-alt4.svn2349
- Fix build on ix86 due to --enable-default-pie
- Disable build on arm

* Sat Sep 28 2019 Gleb F-Malinovskiy <glebfm@altlinux.org> 1.36-alt3.svn2349
- Fixed build on ppc64le and aarch64 architectures.

* Mon Nov 30 2015 Igor Vlasenko <viy@altlinux.ru> 1.36-alt2.svn2349
- NMU: added BR: libspeexdsp-devel

* Thu Jan 17 2013 Igor Zubkov <icesik@altlinux.org> 1.36-alt1.svn2349
- Bump version

* Sun Nov 25 2012 Igor Zubkov <icesik@altlinux.org> 1.34-alt12.svn2349
- Remove quake3-alt-bug14027.patch
- Move %%_libdir/games/quake3/ -> %%_libdir/quake3/
- Build and link with system zlib
- Build and link with system libspeex
- Build with Ogg Vorbis support

* Sun Nov 25 2012 Igor Zubkov <icesik@altlinux.org> 1.34-alt11.svn2349
- svn1114 -> 2349
- Merge quake3-client-up and quake3-client-smp to quake3

* Wed Oct 31 2012 Igor Zubkov <icesik@altlinux.org> 1.34-alt10.svn1114
- convert spec to UTF-8
- buildreq

* Sun Apr 10 2011 Lenar Shakirov <snejok@altlinux.ru> 1.34-alt9.svn1114
- Fixed build: BuildReqs: libmesa-devel -> libGL-devel
- Desktop file fixed and cleaned: thanks to repocop!

* Sun Nov 08 2009 Repocop Q. A. Robot <repocop@altlinux.org> 1.34-alt8.svn1114.qa1
- NMU (by repocop): the following fixes applied:
  * update_menus for quake3-client-smp
  * pixmap-in-deprecated-location for quake3
  * update_menus for quake3-client-up
  * postclean-05-filetriggers for spec file

* Thu Aug 14 2008 Pavlov Konstantin <thresh@altlinux.ru> 1.34-alt8.svn1114
- Fix #16247, thanks vvk@.

* Mon Jan 28 2008 Pavlov Konstantin <thresh@altlinux.ru> 1.34-alt7.svn1114
- Fix #14027.

* Tue Dec 04 2007 Pavlov Konstantin <thresh@altlinux.ru> 1.34-alt6.svn1114
- Merged vvk@'s initscripts for server side.

* Mon Jul 16 2007 Pavlov Konstantin <thresh@altlinux.ru> 1.34-alt5.svn1114
- 1114 revision.
- Fixed launching.

* Tue Apr 10 2007 Pavlov Konstantin <thresh@altlinux.ru> 1.34-alt4.svn1062
- Modified smp-desktop file to be able to launch SMP version.

* Tue Apr 10 2007 Pavlov Konstantin <thresh@altlinux.ru> 1.34-alt3.svn1062
- 1062 revision.

* Thu Feb 22 2007 Pavlov Konstantin <thresh@altlinux.ru> 1.34-alt3.svn1046
- Added requires: client-*, server to quake3 package.

* Sun Feb 18 2007 Pavlov Konstantin <thresh@altlinux.ru> 1.34-alt2.svn1046
- 1046 svn revision.
- Fixed symlinks.

* Mon Jan 29 2007 Pavlov Konstantin <thresh@altlinux.ru> 1.34-alt2.svn1037
- 1037 svn revision.
- Gearified package.
- Added freedesktop menu files.
- Fixed Requires for common package.
- Fixed Provides for -client-smp package.
- Rewrote descriptions and summaries.
- Make common package own directories in %%_libdir/games/.
- Minor spec cleanup.
- Removed xorg-x11-devel from BuildRequires,
  Added libXt-devel and libmesa-devel to BuildRequires instead.
- Added icon.
- Added README.ALT concerning running the program.
- Removed gcc3.4 build-dependancy.
- Fixed URL.
- Rewrote install section using quake3 own Makefile directives.
- Moved binaries to %%_libdir/games/quake3.

* Wed Nov 01 2006 Igor Zubkov <icesik@altlinux.org> 1.34-alt1.svn956
- new version (#10073)
- rename quake3-client to quake3-client-up (#7811)
- add provides quake3-client to quake3-client-up and quake3-client-smp (#7811)
- add docs (#7810)
- use gcc 3.4 for build

* Tue Oct 31 2006 Alexey Shabalin <shaba@altlinux.ru> 1.34-alt0.1svn956
- svn 956
- fix spec for build x86_64
- move clients and server to %_bindir
- fix menu files

* Thu Oct 19 2006 Afanasov Dmitry <ender@atrus.ru> svn916-alt1
- svn rebuild

* Fri Aug 26 2005 Igor Zubkov <icesik@altlinux.ru> 1.32b-alt1
- Initial build for Sisyphus
