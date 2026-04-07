Name: warzone2100
Version: 4.7.0
Release: alt1

Summary: Warzone 2100 Resurrection Project (RTS 3D game)
License: GPLv2+ and CC-BY-SA-3.0
Group: Games/Strategy
URL: https://wz2100.net
VCS: https://github.com/warzone2100/warzone2100

Source0: %name-%version.tar
Source1: deps-%version.tar
# https://github.com/Warzone2100/data-terrain-high/releases/download/v3/high.wz
Source2: high.wz
# https://github.com/Warzone2100/wz-sequences/releases/download/v3/standard-quality-en-sequences.wz
Source3: sequences.wz

Requires: %name-gamedata = %EVR

%ifdef bootstrap
BuildRequires: wget
%endif
BuildRequires: cmake gcc-c++ glslc zip
BuildRequires: /usr/bin/asciidoctor
BuildRequires: /usr/bin/convert
BuildRequires: pkgconfig(libsodium)
BuildRequires: pkgconfig(sqlite3)
BuildRequires: pkgconfig(protobuf)
BuildRequires: pkgconfig(libzip)
BuildRequires: pkgconfig(physfs)
BuildRequires: pkgconfig(libpng)
BuildRequires: pkgconfig(libjpeg)
BuildRequires: pkgconfig(freetype2)
BuildRequires: pkgconfig(harfbuzz)
BuildRequires: pkgconfig(fribidi)
BuildRequires: pkgconfig(vulkan)
BuildRequires: pkgconfig(miniupnpc)
BuildRequires: pkgconfig(sdl3)
BuildRequires: pkgconfig(openal)
BuildRequires: pkgconfig(vorbis)
BuildRequires: pkgconfig(opus)
BuildRequires: pkgconfig(opusfile)
BuildRequires: pkgconfig(theora)
BuildRequires: pkgconfig(libcurl)
BuildRequires: pkgconfig(gnutls)

%package gamedata
Summary: Game data for warzone2100
Group: Games/Strategy
# We split game data to separate package to make it noarch and thus save
# bandwidth and space on distribution media.
BuildArch: noarch

%description
Warzone 2100 is a real-time strategy game. Although comparable to Earth 2150
in many significant respects, it does contain aspects that are unique. These
include various radar technologies and a greater focus on artillery and
counter-battery technologies.

%description gamedata
Game data for warzone2100.

%prep
%setup -a1
%ifdef bootstrap
wget https://github.com/Warzone2100/data-terrain-high/releases/download/v3/high.wz -O %SOURCE2
wget https://github.com/warzone2100/wz-sequences/releases/download/v3/standard-quality-en-sequences.wz -O %SOURCE3
%endif
install -m644 %SOURCE2 data/terrain_overrides/high.wz

# Upstream now generates cache via cmake.
# Use following command on clean full upstream copy of repository while master branch is updated and current release tag is checked out:
# cmake -DOUTPUT_TYPE=sh -DOUTPUT_FILE=autorevision.cache -P build_tools/autorevision.cmake
# ATTENTION: this must be done on pristine full clone of upstream repository, which must include all upstream tags
# and NO downstream tags.
# It counts tags, and resulting information may be used as identificator in multiplayer games to check if client
# has compatible version.
# Thus, generated file must be identical to one included in upstream source tarball, maybe with an exception of VCS_BASENAME and VCS_BRANCH values.
# Failing to follow doing so won't lead to build failure, but may lead to inability to play multiplayer mode with other builds of game.
touch build_tools/autorevision.cmake

%build
%add_optflags -D_FILE_OFFSET_BITS=64

%cmake \
	-DWZ_DISTRIBUTOR="ALT Linux" \
	-DWZ_FINDSDL2_NOCONFIG:BOOL=OFF \
	-DWZ_ENABLE_WARNINGS_AS_ERRORS:BOOL=OFF \
	-DWZ_FORCE_MINIMAL_OPUSFILE:BOOL=OFF \
	-DWZ_USE_SYSTEM_LIBJPEG_TURBO=ON \
	-DWZ_SKIP_ELF_SEPARATE_DEBUG=ON \
	%nil

%cmake_build

%install
%cmakeinstall_std
install -m644 %SOURCE3 %buildroot%_datadir/warzone2100/sequences.wz

for sz in 16x16 32x32 48x48; do
    d=%buildroot%_iconsdir/hicolor/$sz/apps; mkdir -p $d
    convert icons/warzone2100.large.png -resize $sz $d/warzone2100.png
done
sed -ri '/^Icon=/ s,=.+$,=warzone2100,' %buildroot%_desktopdir/*.desktop
rm %buildroot%_iconsdir/net.wz2100.warzone2100.png

%find_lang --output warzone2100.lang warzone2100 warzone2100_guide

%define _customdocdir %_defaultdocdir/%name

%files -f warzone2100.lang
%_bindir/warzone2100
%_desktopdir/*.desktop
%_datadir/metainfo/*.xml
%_iconsdir/hicolor/*/*/*.png
%_man6dir/warzone2100.6*

%files gamedata
%_datadir/doc/warzone2100
%_datadir/warzone2100

%changelog
* Tue Apr 07 2026 Sergey Bolshakov <sbolshakov@altlinux.org> 4.7.0-alt1
- 4.7.0 released

* Thu Feb 05 2026 Sergey Bolshakov <sbolshakov@altlinux.org> 4.6.3-alt1
- 4.6.3 released

* Fri Jan 16 2026 Sergey Bolshakov <sbolshakov@altlinux.org> 4.6.2-alt1
- 4.6.2 released

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
