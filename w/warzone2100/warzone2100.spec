%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1
%set_verify_elf_method strict

Name: warzone2100
Version: 4.4.2
Release: alt2
Summary: Warzone 2100 Resurrection Project (RTS 3D game)
License: GPLv2+ and CC-BY-SA-3.0
Group: Games/Strategy
Url: https://wz2100.net

# https://github.com/Warzone2100/warzone2100.git
Source: %name-%version.tar

#Source1: http://www.deviantart.com/download/92153956/Warzone_2100_Tango_Icon_by_Unit66.zip
Source1: Warzone_2100_Tango_Icon_by_Unit66.tar

# Upstream now generates cache via cmake. 
# Use following command on clean full upstream copy of repository while master branch is updated and current release tag is checked out:
# cmake -DOUTPUT_TYPE=sh -DOUTPUT_FILE=autorevision.cache -P build_tools/autorevision.cmake
# ATTENTION: this must be done on pristine full clone of upstream repository, which must include all upstream tags
# and NO downstream tags.
# It counts tags, and resulting information may be used as identificator in multiplayer games to check if client
# has compatible version.
# Thus, generated file must be identical to one included in upstream source tarball, maybe with an exception of VCS_BASENAME and VCS_BRANCH values.
# Failing to follow doing so won't lead to build failure, but may lead to inability to play multiplayer mode with other builds of game.
Source2: autorevision-%version.cache

# submodules
Source3: %name-%version-3rdparty-date.tar
Source4: %name-%version-3rdparty-discord-rpc.tar
Source5: %name-%version-3rdparty-EmbeddedJSONSignature.tar
Source6: %name-%version-3rdparty-launchinfo.tar
Source7: %name-%version-3rdparty-readerwriterqueue.tar
Source8: %name-%version-3rdparty-SQLiteCpp.tar
Source9: %name-%version-3rdparty-SQLiteCpp-googletest.tar
Source10: %name-%version-data-base-texpages.tar
Source11: %name-%version-data-music.tar
Source12: %name-%version-data-fonts.tar
Source13: %name-%version-3rdparty-quickjs-wz.tar
Source14: %name-%version-3rdparty-basis_universal.tar
Source15: %name-%version-data-terrain_overrides-classic.tar
Source16: %name-%version-3rdparty-re2.tar

Source1000: %name.watch
# https://github.com/Warzone2100/data-terrain-high/releases/download/v1/high.wz
Source1001: high.wz

Patch1: %name-alt-unbundle-libs.patch
Patch2: %name-alt-dont-install-portable-marker.patch
Patch3: 0001-Fix-build-on-GCC13.patch
Patch4: %name-alt-bundle-prebuilt.patch

BuildRequires: /proc
BuildRequires: qt5-base-devel qt5-3d-devel qt5-script-devel qt5-x11extras-devel openssl-devel
BuildRequires: elfutils fontconfig-devel libGL-devel libGLU-devel libX11-devel libXrandr-devel libXrender-devel libfreetype-devel libogg-devel libpng-devel libstdc++-devel pkg-config texlive-latex-base xorg-randrproto-devel xorg-renderproto-devel xorg-xproto-devel zlib-devel
BuildRequires: asciidoc-a2x flex gcc-c++ libSDL2-devel libfribidi-devel libglew-devel libopenal-devel libphysfs-devel libtheora-devel libvorbis-devel unzip xorg-cf-files zip
BuildRequires: libglm-devel
BuildRequires: python2-base
BuildRequires: cmake
BuildRequires: libminiupnpc-devel
BuildRequires: libutfcpp-devel
BuildRequires: libutf8proc-devel
BuildRequires: libsodium-devel
BuildRequires: libcurl-devel
BuildRequires: libsqlite3-devel
BuildRequires: libfmt-devel
BuildRequires: asciidoctor
BuildRequires: libharfbuzz-devel
BuildRequires: libopus-devel
BuildRequires: libopusfile-devel

# 'zip -T' called in build process needs unzip to work...

Requires: %name-gamedata = %EVR

%description
Warzone 2100 is a real-time strategy game. Although comparable to Earth 2150
in many significant respects, it does contain aspects that are unique. These
include various radar technologies and a greater focus on artillery and
counter-battery technologies.

%package gamedata
Summary: Game data for warzone2100
Group: Games/Strategy
# We split game data to separate package to make it noarch and thus save
# bandwidth and space on distribution media.
BuildArch: noarch

%description gamedata
Game data for warzone2100.

%prep
%setup -a1 -a3 -a4 -a5 -a6 -a7 -a8 -a9 -a10 -a11 -a12 -a13 -a14 -a15 -a16
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1

install -m644 %SOURCE2 build_tools/autorevision.cache
install -m644 %SOURCE1001 data/terrain_overrides/high.wz

%build
%add_optflags -D_FILE_OFFSET_BITS=64

%cmake \
	-DWZ_DISTRIBUTOR="ALT Linux" \
	-DWZ_FINDSDL2_NOCONFIG:BOOL=OFF \
	-DWZ_ENABLE_WARNINGS_AS_ERRORS:BOOL=OFF \
	-DWZ_FORCE_MINIMAL_OPUSFILE:BOOL=OFF \
	%nil

%cmake_build

%install
%cmakeinstall_std
install -d %buildroot%_pixmapsdir
install -m644 icons/warzone2100.png %buildroot%_pixmapsdir
install -pD -m644 warzone2100_48x48.png %buildroot%_liconsdir/warzone2100.png
install -pD -m644 warzone2100_32x32.png %buildroot%_niconsdir/warzone2100.png
install -pD -m644 warzone2100_16x16.png %buildroot%_miconsdir/warzone2100.png

rm -rf %buildroot%_datadir/fonts
rm -rf %buildroot%_datadir/doc
rm -rf %buildroot%_iconsdir/net.wz2100.warzone2100.png

%find_lang warzone2100

%files -f warzone2100.lang
%doc COPYING* README.md
%_bindir/*
%_miconsdir/*
%_niconsdir/*
%_liconsdir/*
%_pixmapsdir/*
%_desktopdir/*
%_man6dir/*
%_datadir/metainfo/*

%files gamedata
%_datadir/warzone2100

%changelog
* Tue May 07 2024 Elizaveta Morozova <morozovaes@altlinux.org> 4.4.2-alt2
- Built with bundled re2.

* Mon Dec 04 2023 Elizaveta Morozova <morozovaes@altlinux.org> 4.4.2-alt1
- Updated version.

* Mon Jul  3 2023 Artyom Bystrov <arbars@altlinux.org> 4.2.6-alt2
- Fix build on GCC13

* Fri Mar 04 2022 Aleksei Nikiforov <darktemplar@altlinux.org> 4.2.6-alt1
- Updated to upstream version 4.2.6.

* Fri Jan 14 2022 Aleksei Nikiforov <darktemplar@altlinux.org> 4.2.4-alt1
- Updated to upstream version 4.2.4.

* Wed Dec 15 2021 Aleksei Nikiforov <darktemplar@altlinux.org> 4.2.3-alt1
- Updated to upstream version 4.2.3.

* Tue Aug 17 2021 Aleksei Nikiforov <darktemplar@altlinux.org> 4.1.3-alt1
- Updated to upstream version 4.1.3.

* Wed Jul 28 2021 Aleksei Nikiforov <darktemplar@altlinux.org> 4.1.1-alt1
- Updated to upstream version 4.1.1.

* Wed Jun 02 2021 Aleksei Nikiforov <darktemplar@altlinux.org> 4.0.1-alt1
- Updated to upstream version 4.0.1.
- Disabled -Werror build flag.

* Wed Apr 07 2021 Aleksei Nikiforov <darktemplar@altlinux.org> 4.0.0-alt1
- Updated to upstream version 4.0.0.

* Wed Jul 29 2020 Aleksei Nikiforov <darktemplar@altlinux.org> 3.4.1-alt1
- Updated to upstream version 3.4.1.

* Mon Jul 20 2020 Michael Shigorin <mike@altlinux.org> 3.3.0-alt1.1
- E2K: upgrade lcc ftbfs workarounds from 1.23 to 1.24

* Thu Apr 02 2020 Aleksei Nikiforov <darktemplar@altlinux.org> 3.3.0-alt1
- Updated to upstream version 3.3.0.

* Fri May 10 2019 Michael Shigorin <mike@altlinux.org> 3.2.3-alt2
- E2K: avoid UTF-8 BOM

* Wed Aug 29 2018 Grigory Ustinov <grenka@altlinux.org> 3.2.3-alt1.1
- NMU: Rebuild with new openssl 1.1.0.

* Fri Aug 25 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 3.2.3-alt1
- Updated to upstream version 3.2.3.

* Wed Jan 30 2013 Denis Smirnov <mithraen@altlinux.ru> 3.1.0-alt1
- 3.1.0
- build from git

* Sun Nov 27 2011 Victor Forsiuk <force@altlinux.org> 2.3.9-alt1
- 2.3.9

* Sun Jun 19 2011 Victor Forsiuk <force@altlinux.org> 2.3.8-alt1
- 2.3.8

* Sat Mar 26 2011 Victor Forsiuk <force@altlinux.org> 2.3.7-alt2
- Build with new libphysfs.

* Thu Jan 27 2011 Victor Forsiuk <force@altlinux.org> 2.3.7-alt1
- 2.3.7

* Tue Nov 30 2010 Victor Forsiuk <force@altlinux.org> 2.3.6-alt1
- 2.3.6

* Mon Sep 27 2010 Victor Forsiuk <force@altlinux.org> 2.3.5-alt1
- 2.3.5

* Fri Aug 13 2010 Victor Forsiuk <force@altlinux.org> 2.3.4-alt1
- 2.3.4

* Wed Aug 04 2010 Victor Forsiuk <force@altlinux.org> 2.3.3-alt1
- 2.3.3

* Tue Jun 15 2010 Victor Forsiuk <force@altlinux.org> 2.3.1-alt1
- 2.3.1

* Tue May 25 2010 Victor Forsiuk <force@altlinux.org> 2.3.0-alt1
- 2.3.0

* Sat Nov 14 2009 Victor Forsyuk <force@altlinux.org> 2.2.4-alt1
- 2.2.4

* Thu Sep 03 2009 Victor Forsyuk <force@altlinux.org> 2.2.2-alt1
- 2.2.2

* Mon Jul 06 2009 Victor Forsyuk <force@altlinux.org> 2.2.1-alt1
- 2.2.1

* Mon Dec 22 2008 Victor Forsyuk <force@altlinux.org> 2.1.0-alt1
- 2.1.0
- Split (huge!) game data to noarch package.

* Tue Jan 22 2008 Victor Forsyuk <force@altlinux.org> 2.0.10-alt1
- 2.0.10

* Mon Jul 09 2007 Victor Forsyuk <force@altlinux.org> 2.0.7-alt1
- 2.0.7

* Thu Apr 05 2007 Victor Forsyuk <force@altlinux.org> 2.0.6-alt1
- 2.0.6

* Tue Mar 27 2007 Victor Forsyuk <force@altlinux.org> 2.0.5-alt2
- Fix to build for 64 bit.

* Fri Dec 29 2006 Victor Forsyuk <force@altlinux.org> 2.0.5-alt1
- 2.0.5
- New URL.
- Refresh buildrequires.
- More informative summary and description.

* Wed Nov 16 2005 Anton Farygin <rider@altlinux.ru> 2.0.2.3-alt1
- new version

* Fri Sep 02 2005 Anton Farygin <rider@altlinux.ru> 0.2.2-alt1
- first build for Sisyphus
