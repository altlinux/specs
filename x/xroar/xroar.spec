Name: xroar
Version: 1.3
Release: alt1
Summary: Dragon and Tandy CoCo Emulator
License: GPL-3.0+
Group: Emulators
Url: https://www.6809.org.uk/xroar/
Packager: Artyom Bystrov <arbars@altlinux.org>

Source: https://www.6809.org.uk/xroar/dl/%name-%version.tar.gz
BuildRequires: ImageMagick-tools
BuildRequires: pkg-config
BuildRequires: libalsa-devel
BuildRequires: libgtk+2-devel
BuildRequires: libgtkglext-devel
BuildRequires: libpulseaudio-devel
BuildRequires: libSDL2-devel
BuildRequires: libsndfile-devel
BuildRequires: zlib-devel
BuildRequires: texinfo

%description
A Dragon 32, Dragon 64 and Tandy CoCo emulator for Unix, Linux, GP32, MacOS X
and Windows32. It uses standard cassette images (".cas" files) and virtual
diskettes (".dsk" or ".vdk" files) but has its own snapshot format at the
moment (no ".pak" file support).
.
Firmware ROM images are required to usefully run this emulator.
If you have difficulty extracting these from your real Dragon,
CoCo or MC-10, dumps may be available from the Dragon Archive (http://archive.worldofdragon.org/index.php?title=Main_Page)
or the Color Computer Archive (https://colorcomputerarchive.com).

%prep
%setup

%build
%configure --without-oss
%make_build

# Build docs
make html
make pdf

%install
mkdir -p %buildroot%_bindir
install -m 755 src/%name %buildroot%_bindir

# default rom directory
mkdir -p %buildroot%_datadir/%name/roms

# Generate desktop file
mkdir -p %buildroot%_desktopdir
cat >%buildroot%_desktopdir/%name.desktop <<EOF
[Desktop Entry]
Name=XRoar
GenericName=Dragon 32/64 Emulator
Comment=Emulates the Dragon 32/64 and Tandy CoCo
Exec=%name
Icon=%name
Terminal=false
Type=Application
Categories=Games;Emulator;
EOF

# install menu icons
for N in 16 32 48 64 128;
do
convert src/windows32/xroar-256x256.ico -scale ${N}x${N} $N.png;
install -D -m 0644 $N.png %buildroot%_iconsdir/hicolor/${N}x${N}/apps/%name.png
done


%files
%_bindir/%name
%_datadir/%name
%_iconsdir/hicolor/*/apps/%name.png
%_desktopdir/%name.desktop
%doc COPYING.GPL COPYING.LGPL
%doc ChangeLog README README.SDS
%doc doc/%name.html doc/%name-screens.png doc/%name-timebandit-af.png
%doc doc/%name.pdf

%changelog
* Wed Jan 18 2023 Artyom Bystrov <arbars@altlinux.org> 1.3-alt1
- update to version 1.3

* Wed Jan 18 2023 Artyom Bystrov <arbars@altlinux.org> 1.2-alt1
- initial build for ALT Sisyphus

* Sun Nov 27 2022 Carsten Ziepke <kieltux@gmail.com>
- Update to 1.2
  * Fixed comma, lowercase 'm', lowercase 'Ã¸' glyphs for GIME
  * Fix SDL-only builds
  * 6809: flesh out some illegal instruction behaviours
  * 6309: flesh out some undocumented behaviour
  * Fleshed out T1-compatibility in CoCo 3 GIME
- Changes in 1.1
  * New GDB monitor commands
  * New configure options to only build specific machine archs
  * Support 1M or 2M in CoCo 3
  * Support K7 cassette image files (read-only)
  * Support UTF-8 block characters in -type for MC-10
  * Type ASCII BASIC from file on MC-10
  * Matra & Hachette Alice support (keyboard layout,
    built-in profile)
  * New meta-options -machine-opt and -cart-opt
  * New ide-addr=address cart-opt
  * New abstract block device handling
  * IDE support adjusted to use abstracted block devices
  * MOOH/NX32 support adjusted to use abstracted block devices
  * 6801/6803: fix some illegal instruction timings
  * Fixed uppercase 'G', lowercase 'j' and 'w' glyphs for 6847T1
* Sun Mar  6 2022 Carsten Ziepke <kieltux@gmail.com>
- Update to 1.0.9
  * Close file after serialisation
- Changes in 1.0.8
  * Fix WASM audio for non-Firefox
  * Fix crash reading zero-length CAS file
  * Fix joystick reads for Pacdude Monster Maze
- Changes in 1.0.7
  * Fix Windows 11 video (set SDL hint to use different renderer)
- Changes in 1.0.6
  * Fix SDL audio thread interactions
  * Try multiple SDL video renderers in order
  * Fix composite phase setting
- Changes in 1.0.5
  * Open IDE images in binary mode under Windows
- Changes in 1.0.4
  * GIME IO range fixes
  * Enable GDB for CoCo 3
  * Fix HD6309 TFM when W=0
- Changes in 1.0.3
  * 6801/6803: many more illegal instructions
  * Fix EXTMEM signalling for writes to RAM
  * MC10: Constrain video to internal 4K RAM
  * Default -ao-fragments changed for new SDL audio
  * MPI: return to selected slot on reset
- Fix info-files-without-install-info-postin/postun check
* Sat Dec  4 2021 Carsten Ziepke <kieltux@gmail.com>
- Update to 1.0.2
  * Fix single-bit sound feedback into PIA.
  * Revert SDL audio to callbacks, helps with Windows
  * Fix MC10 INT/EXT wiring
  * 6801/6803: implement more illegal instructions
  * 6803: Lower bits of address to data bus for floating reads
  * MC10: Only set lower 6 bits on keyboard read
- Update to 1.0.1
  * Fix cart disable logic when loading other media
  * MC6801/6803: TST resets CC.C, unlike MC6809.
  * Revert colourburst for NTSC colour modes with CSS+GM0
- Update to 1.0.0
  * Initial CoCo 3 support.
  * Fix MPI FIRQ handling
  * New option -tv-input configures type of video used by machine.
  * New option -kbd-bind for user mapping of (untranslated) keys.
  * Fix duplicate-IDAM issue when reformatting disks
  * Initial MC-10 support (including MC6803 emulation).
  * Fix occasional spurious NMI in RSDOS
  * New snapshot format to support CoCo 3, MC-10.
  * New specific load options: -load-fdX, -load-hdX, -load-sd,
  - load-tape
  * IDE, NX32, MOOH now all require user to specify an image.
  * Games Master Cartridge no longer marked autostart by default.
  * Tape play/pause function (mainly for MC-10 which has
    no motor remote).
  * Snapshot saves only RAM contents into .ram files
  * List physical joysticks on -joy-axis help or -joy-button help.
  * Control+M toggles menubar where appropriate.
- Update to 0.3.7
  * Add Control+Shift+D to flush disk images
  * Support leading "~/" in filenames, not just path elements
  * New option -tape-hysteresis (with new default of 1%% tape input
    hysteresis)
  * New option -tape-rewrite-gap-ms _ms_ sets gap length during
    rewrite
  * New option -tape-rewrite-leader _bytes_ sets leader length
    during rewrite
  * Document previously added option -tape-pan
  * Detect pulse widths for CUE data when using -tape-rewrite
  * RACE Computer Expansion Cage support (-cart mpi-race)
  * Removed -fast-sound option (and related menu options)
- Update to 0.36.2
  * Fix -lp-file option [Pere Serrat]
  * Change default CoCo disk interleave to 5
- Update to 0.36.1
  * Support CAS padding without fast loading enabled
  * Don't escape option arguments if they expect a filename [".mad."]
  * Fix setting 6309 registers from GDB
  * Fix GDB listen on machine reconfigure (eg snapshot load)
  * Fix joystick axis & button option parsing
- Update to 0.36
  * Fix SAM S output in map type 1
  * Work around Windows audio failure when 5.1 is available
  * Cleaner PulseAudio output
  * Try harder to find working SDL2 audio format
  * Avoid buggy 'wasapi' SDL audio backend under Windows
  * HD6309: Clear MD register on reset
  * Relicensed to GPLv3+
  * WebAssembly target support
  * MC6809: LEA instructions work in page 1
  * Recognise .dgn and .cco as potential binary files
  * Migrated Mac OS X UI to SDL2
  * Updates for IDE and IDE cartridge
  * SAM VDG counter switching behaviour updates
  * Reload cartridge ROMs on each reset to aid test cycle
  * Try first listed UI module if user-specified one not found
  * New configuration parsing with quotes and escape sequences
  * In Windows, search Documents/XRoar/ (for config file) and
    Documents/XRoar/roms/ (for ROM images).
- Update to 0.35
  * New EXTMEM/SLENB support allows cartridges to inhibit normal
    device select
  * New NX32 RAM cartridge
  * Fix buffer overrun in MC6847 code
  * New option -ao-gain specifies volume in dBFS
  * New CAS CUE support
  * New -C option allocates debug console in Windows
    (must be first option)
  * Fix use of AltGr key in translated mode on Windows (SDL2)
  * New MOOH RAM + SD card cartridge
  * Support JVC/DSK files with non-standard sectors per track
  * Integrate tracing into CPU code
  * MC6809: Assume certain page2 illegal ops are same as page0
  * WD279x: implement multiple-sector type 2 ops
  * New SN76489 sound chip support
  * New Games Master Cartridge support (-cart gmc)
  * Use SDL2 audio queueing interface where -ao-fragments > 1
  * Optional --disable-simulated-ntsc configure option for speed
  * HD6309: Fix interrupt handling during TFM instruction
- Update license, xroar is relicensed to GPL-3.0+ (0.36)
- Fix package group
- Update BuildRequires to use pkgconfig
- Add icns-utils to extract Mac OS X icons (higher resolutions)
- Build documentation
- Run spec-cleaner
* Thu Sep 29 2016 kieltux@gmail.com
- Update to 0.34.3
- Spec file updated (inspired from the the fedora package done by
  Andrea Musuruane <musuruan@gmail.com>)
* Fri Mar  7 2008 uli@suse.de
- reenable GL (test system was broken)
* Wed Mar  5 2008 uli@suse.de
- update -> 0.20
- disabled GL (segfault)
- use GTK2
