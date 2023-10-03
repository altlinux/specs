Name: furnace
Version: 0.6pre17
Release: alt1
Summary: Chiptune tracker supporting many console soundchips
License: GPL-3.0
Group: Sound
Url: https://github.com/tildearrow/furnace
Packager: Artyom Bystrov <arbars@altlinux.org>

Source: %name-%version.tar.gz
BuildRequires: gcc gcc-c++
BuildRequires: cmake
BuildRequires: libalsa-devel
BuildRequires: libfmt-devel
BuildRequires: libjack-devel
BuildRequires: libsndfile-devel
BuildRequires: zlib-devel
BuildRequires: pkgconfig(sdl2)
BuildRequires: ImageMagick-tools

%description
Furnace is a chiptune tracker compatible with DefleMask. Features:

- supports the following systems:
  - Sega Genesis
  - Sega Master System
  - Game Boy
  - PC Engine
  - NES
  - Commodore 64
  - Yamaha YM2151 (plus PCM)
  - Neo Geo
  - AY-3-8910 (ZX Spectrum, Atari ST, etc.)
  - Microchip AY8930
  - Philips SAA1099
  - Amiga
  - TIA (Atari 2600/7800)
- multiple sound chips in a single song!
- clean-room design (guesswork and ABX tests only, no decompilation involved)
- bug/quirk implementation for increased playback accuracy
- VGM and audio file export
- accurate emulation cores whether possible (Nuked, MAME, SameBoy,
Mednafen PCE, puNES, reSID, Stella, SAASound and ymfm)
- additional features on top:
  - FM macros!
  - negative octaves
  - arbitrary pitch samples
  - sample loop points
  - SSG envelopes in Neo Geo
  - full duty/cutoff range in C64
  - ability to change tempo mid-song with `Cxxx` effect
  (`xxx` between `000` and `3ff`)
- open-source under GPLv2 or later.

%package doc
Group: Documentation
Summary: Documentation files for furnace

%description doc
These are the documentation files for the furnace chiptune synth.

%prep
%setup

%build
%cmake -DSYSTEM_FMT=ON -DSYSTEM_LIBSNDFILE=ON -DSYSTEM_ZLIB=ON -DSYSTEM_SDL2=ON
%cmake_build

%install
%cmake_install

# install menu icons
for N in 16 32 48 64 128;
do
convert res/logo.png -scale ${N}x${N} $N.png;
install -D -m 0644 $N.png %buildroot%_iconsdir/hicolor/${N}x${N}/apps/%name.png
done

mkdir %buildroot%_datadir/metainfo/
install -D -m 0644 ./res/furnace.appdata.xml %buildroot%_datadir/metainfo/

%files
%doc README.md CONTRIBUTING.md
%doc LICENSE
%_bindir/%name
%_datadir/%name
%_iconsdir/hicolor/*/apps/*
%_datadir/metainfo/*
%_desktopdir/%name.desktop

%files doc
%_docdir/%name

%changelog
* Tue Oct 3 2023 Artyom Bystrov <arbars@altlinux.org> 0.6pre17-alt1
- New version

* Mon Sep 25 2023 Artyom Bystrov <arbars@altlinux.org> 0.6pre16-alt1
- New version

* Tue Aug 29 2023 Artyom Bystrov <arbars@altlinux.org> 0.6pre9-alt1
- New version

* Tue Jun 06 2023 Artyom Bystrov <arbars@altlinux.org> 0.6pre5-alt1
- New version

* Sun Jun 04 2023 Artyom Bystrov <arbars@altlinux.org> 0.5.8-alt1
- initial build for ALT Sisyphus

* Tue Mar  8 2022 Fabio Pesari <fpesari@tuxfamily.org>
- First upload, v0.5.8
