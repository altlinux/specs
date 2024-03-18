%define _localname melonDS

Name:             melonds
Summary:          Nintendo DS emulator
Version:          0.9.5
Release:          alt1
Group:            Emulators
License:          GPL-3.0-or-later
URL:              http://melonds.kuribo64.net/
Source0:          https://github.com/Arisotura/melonDS/archive/%{version}.tar.gz#/%{_localname}-%{version}.tar.gz
ExcludeArch: %ix86

BuildRequires:    binutils gcc-c++
BuildRequires:    cmake >= 3.13
BuildRequires:    hicolor-icon-theme
BuildRequires:    libarchive-devel
BuildRequires:    libcurl-devel
BuildRequires:    libpcap-devel
BuildRequires:    libslirp-devel
BuildRequires:    pkgconfig(gtk+-3.0)
BuildRequires:    pkgconfig(Qt5Core)
BuildRequires:    pkgconfig(Qt5Network)
BuildRequires:    pkgconfig(Qt5OpenGL)
BuildRequires:    pkgconfig(Qt5Multimedia)
BuildRequires:    pkgconfig(Qt5Widgets)
BuildRequires:    pkgconfig(sdl2)
BuildRequires:    pkgconfig(epoxy)
BuildRequires:    ninja-build extra-cmake-modules


%description
melonDS is a Nintendo DS emulator.

%prep
%setup -q -n %{_localname}-%{version}

%build
mkdir build
cd build
cmake \
    -DCMAKE_INSTALL_PREFIX=%{_prefix} \
    -G "Ninja" \
    ..

ninja -v

%install
cd build
DESTDIR=%{buildroot} ninja install

%files

%doc README.md LICENSE
%{_bindir}/%{_localname}
%{_datadir}/applications/net.kuribo64.melonDS.desktop
%{_datadir}/icons/hicolor/*/apps/net.kuribo64.melonDS.png

%changelog
* Fri Mar 15 2024 Artyom Bystrov <arbars@altlinux.org> 0.9.5-alt1
- Update to new version

* Fri Mar 15 2024 Artyom Bystrov <arbars@altlinux.org> 0.9.4-alt1
- Imported from srpm

* Tue Mar  8 2022 Markus S <kamikazow@web.de>
- Update to 0.9.4
  * Redesign of the Input dialog (Rayyan)
  * Use DraStic open-source DS BIOS replacement (Swordfish90, asiekierka)
  * Generate non-bootable firmware replacement (Swordfish90, asiekierka, others)
  * Support for syncing DLDI/DSi SD image to a folder (Arisotura)
  * ARM9 PU (code/data abort) support in interpreter mode (Arisotura)
  * Fix ADPCM decoding bug resulting in potential crackling (Arisotura)
  * Block sound DMA from reading the ARM7 BIOS (Arisotura)
  * Smarter SDL initialization (andrigamerita, Nadia, Arisotura)
  * Properly center the main window on macOS (Nadia)
  * Don't try to render if the emulator is inactive (Nadia)
  * Fix potential issues with DSi title importing (Nadia, Epicpkmn11)
  * Custom path support (Arisotura)
  * Fix nifi socket init on BSD and macOS (Nadia)
  * Add support for zero addresses in AR codes 3xxxxxxx to Axxxxxxx (Arisotura)
  * Lower window refresh rate if running too fast (RSDuck)
  * Wifi power-saving support (RSDuck)
  * Allow swap-screen hotkey to swap between displaying only top screen and only bottom screen (ZackWeinstein)
  * Add RAM search dialog (2jun0)
  * Add power management dialog for setting battery parameters (Rayyan)
* Sun Nov  7 2021 Markus S <kamikazow@opensuse.org>
- Update to 0.9.3
  - Changes from 0.9.0:
  * merge in experimental DSi support
  * 2D: delay palette lookup for sprites
  * 2D: some attempts at fixing mosaic
  * CP15: only update PU regions when actually needed
  * 2D: fix sprite Y-flip
  * 3D/GL: fix transparency bugs
  * add warning against hacked firmwares
  * fix libpcap bug (i404788)
  * better file handling code (Nadia)
  * GBA slot and solar sensor support (rzumer)
  * add support for AR cheat codes
  * fix handling of ROMs with encrypted secure area
  * 3D: change clipping to be closer to hardware
  * 3D: implement DISP_1DOT_DEPTH
  * 3D: more accurate viewport transform
  * build fixes (Nadia)
  * add JIT recompiler (RSDuck)
  * new Qt UI
  * SPU: only start channels when they can actually run
  * 2D: allow writes to DISPCNT/masterbright/capture/dispFIFO regardless of POWCNT
  * SPU: don't process channels with len<4
  * 3D/GL: cleaner polygon generation code
  * 3D/GL: add attempt at reducing warping on quads/etc
  * 3D: add missing variables to savestates
  * wifi: avoid potential out-of-bounds writes with invalid RX buffer setups
  * 3D/GL: fix issues with framebuffer handling
  * make MAC randomization optional
  * make software renderer the default
  * add basic DLDI
  - Changes from 0.9.1:
  * add fullscreen hotkey
  * remove hardcoded F11-debug key (oops)
  * fix some gaps in the IO handlers
  * add ability to run unlaunch'd DSi NANDs
  * add preliminary camera support (feeds fixed stripe pattern)
  * fix potential bugs with tight timers (fixes ZXDS)
  * SPU: small optimization to the mixer
  * better framerate limiter
  * fix several JIT issues
  * GPU: lay bases for EVIL PLANS
  * GPU: emulate separate scroll register for 3D layer scrolling
  * some corrections to the ROM savetype list
  * a bunch of misc fixes, as usual
  - Changes from 0.9.2:
  * GX: optimize single-param commands
  * add recent-files menu (abcdjdj)
  * add support for loading files from archives
  * fix JIT bugs
  * fix wifi bugs
  * improve performance of save-memory writeback
  * add hotkey for swapping screens
  * 3D/GL: attempt fixing various bugs
  * fix OpenGL scaling on hiDPI displays
  * rework GPU2D for easier integration of full GL rendering
  * rework NDSCart and GBACart to make it easier to implement new cart types
  * add support for NAND save memory (WarioWare DIY, Jam with the Band)
  * fix bugs in DSi I2C and SD/MMC interfaces
  * new screen modes
  - Changes from 0.9.3:
  * Fill most gaps in ROMList (Arisotura)
  * Fix touchscreen code in non-hybrid layout mode (Arisotura)
  * GBACart: simulate open-bus decay roughly (Arisotura)
  * Frontend: handle tablet and touch events (Generic aka RSDuck)
  * Implement NO$GBA debug registers (BlueTheDuck)
  * Add frame step hotkey (Yukitty, additional fixes by Gal20)
  * Add DSP code (PoroCYon, purringChaos)
  * Save window state (Arisotura)
  * JIT optimisations and fixes (Generic aka RSDuck)
  * Add ROM info dialog (Rayyan)
  * Allow using DSi footer within NAND images (MightyMax)
  * More accurate NWRAM implementation (MightyMax)
  * Only open microphone if necessary (Arisotura)
  * Fix undo load savestate loading (Generic aka RSDuck)
  * Fix pause when inactive (Generic aka RSDuck)
  * Add audio interpolation (Arisotura)
  * Add SOUNDBIAS and optional 10bit audio (Nadia)
  * Patch touchscreen calibration data in DSi mode (Arisotura)
  * Add DSi title manager (Arisotura)
  * Fix threaded rasteriser deadlock when VCount is moved (Generic aka RSDuck)
  * More accurate DMA timings (Arisotura)
  * Add preliminary DSi-mode direct boot (MightyMax, Arisotura)
* Fri Nov 22 2019 Markus S <kamikazow@opensuse.org>
- Install icon and launcher
* Sun Nov 10 2019 Markus S <kamikazow@opensuse.org>
- Initial packaging
