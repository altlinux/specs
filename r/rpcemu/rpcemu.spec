Name: rpcemu
Version: 0.9.4
Release: alt1
Summary: Acorn RiscPC Emulator
License: GPL-2.0-only
Group: Emulators
Url: https://www.marutan.net/rpcemu
Packager: Artyom Bystrov <arbars@altlinux.org>

Source: http://www.marutan.net/rpcemu/%version/%name-%version.tar.gz
Patch2: %name-config.patch
BuildRequires: dos2unix
BuildRequires: pkgconfig(Qt5Core)
BuildRequires: pkgconfig(Qt5Gui)
BuildRequires: pkgconfig(Qt5Multimedia)
BuildRequires: pkgconfig(Qt5Widgets)
ExclusiveArch: %ix86 x86_64

%description
Acorn RiscPC emulator. Requires RISC OS ROMs >= 3.70 in
%_datadir/rpcemu/roms. Press Ctrl + End to access the GUI.

%prep
%setup
%patch2 -p1
dos2unix readme.txt

%build
%qmake_qt5 src/qt5
%make_build
%qmake_qt5 src/qt5 "CONFIG+=dynarec"
%make_build

%install
install -d -m 755 %buildroot%_bindir
install -m 755 rpcemu-interpreter %buildroot%_bindir
install -m 755 rpcemu-recompiler %buildroot%_bindir
install -d -m 755 %buildroot%_datadir/rpcemu
cp -a cmos.ram rpc.cfg roms %buildroot%_datadir/rpcemu
chmod -x riscos-progs/HostFS/hostfs*

%files
%doc readme.txt riscos-progs
%_bindir/rpcemu-interpreter
%_bindir/rpcemu-recompiler
%config %_datadir/rpcemu/rpc.cfg
%config %_datadir/rpcemu/cmos.ram
%_datadir/rpcemu/roms
%dir %_datadir/rpcemu

%changelog
* Wed Apr 26 2023 Artyom Bystrov <arbars@altlinux.org> 0.9.4-alt1
- initial build for ALT Sisyphus

* Sat Mar 18 2023 Luigi Baldoni <aloisio@gmx.com>
- Update to version Version 0.9.4
  * ARM
    + Performance gains on x86 and x64 dynamic recompiler.
    + Many of the instructions that were not accelerated on the
    x64 architecture but were on x86 have now been implemented
    on x64 BIC/MUL.
    + Refactoring of Dynamic Recompiler code.
    + Many bugfixes.
    + Accessing CP15 should only be permitted in privileged
    modes.
  * Network Address Translation
    + You can now configure ports to be forwarded between your
    host network and RPCEmu. This allows you to host servers
    under RPCEmu that can be accessed by other machines on
    your network.
    (Note, this still does not enable the use of ShareFS)
  * Floppy Disc
    + Support HFE format floppy disc images. HFE disc images are
    lower-level than ADF discs as they can also store the
    information required for various copy protection systems.
    Contributed by Sarah Walker.
  * VIDC
    + If you are not using VRAM you can now use up to 4MB of RAM
    for video modes.
  * Other
    + Fix the crash on shutdown or reset of RISC OS 5. Based on
    a suggestion from Rob Sprowson.
  * GCC
    + Compiling with GCC 10 no longer needs a workaround for the
    common symbols errors.
  Version 0.9.3:
  * Easy-Start bundles
    + Two ROM/Disc Image sets are now available to make setting
    up RPCEmu as simple as possible. both are configured with
    networking by default.
    ° RISC OS Direct, a version of the RISC OS 5 based
    distribution with many extras, ideal for running recent
    applications
    ° RISC OS 3.71, an older '26-bit' version of RISC OS,
    ideal for running 'classic' applications.
    + Both are pre-setup with a large number of applications,
    tools, and both ship with !Store and PackMan package
    managers for installing more.
  * ARM
    + Correct several issues related to the MSR instruction
    + Correct several instruction decoding issues
    + Generate undefined instruction exceptions in the correct
    places of the instruction set
    + Implement ARMv4 (StrongARM) Load store extensions
    + Make ARMv4 extensions only available when configured as
    ARMv4
  * Floppy Discs
    + We now support loading of DOS and Atari 360KB (.img) disc
    images into the floppy drives.
  * Other fixes
    + Settings files and CMOS ram files are saved as changes are
    made to them, so these settings are retained even if the
    program is closed abnormally.
- Drop rpmcemu-rpmlintrc
* Fri Nov  1 2019 Luigi Baldoni <aloisio@gmx.com>
- Update to version 0.9.2 (see
  http://www.marutan.net/rpcemu/index.php#release_notes
  for changelog)
- Refreshed rpcemu-config.patch
- Use upstream binary names
- Spec cleanup
* Wed Nov 23 2016 aloisio@gmx.com
- Update to 0.8.15 (see
  http://www.marutan.net/rpcemu/index.php#release_notes
  for changelog)
- Dropped rpcemu.dif and rpcemu-rpmlint.patch
- Spec cleanup
* Sun Dec 21 2008 uli@suse.d
- fixed rpmlint complaints for i386 code as well
* Wed Nov 26 2008 uli@suse.d
- update to 20081127svn:
  - Use fixed border and correct window size calculation
  - Added missing resource ids
  - Implement sound under Linux
  - If the rpcemu window becomes too small then the menubar can't be used.
    (Sometimes the emulated system goes wrong somehow and ends up giving
    rubbish to VIDC20.) This patch sets a minimum size for the window so you
    can always see the menubar.
  - rpcemu isn't very friendly if no roms can be found.  This patch makes it
    report the cause of errors better.  It also warns of unsupported command
    line options (that is, any options at all).
  - HostFS now handles spaces in filenames
- fixed rpmlint complaints
* Tue Apr 29 2008 uli@suse.d
- update to 20080430svn
- added sound output
- build both recompiler and interpreter
- changes to default config (sound, memory, blitting)
