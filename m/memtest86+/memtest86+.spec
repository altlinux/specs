Name: memtest86+
Version: 6.10
Release: alt1

Summary: Memory test for x86 architecture
License: GPL-2.0-or-later
Group: System/Kernel and hardware

Url: http://www.memtest.org
Source: %url/download/%version/%name-%version.tar.gz
# Source-url: https://github.com/memtest86plus/memtest86plus/archive/refs/tags/v%version.tar.gz

Packager: Michael Shigorin <mike@altlinux.org>

ExclusiveArch: %ix86 x86_64
Requires(post,preun): bootloader-utils >= 0.3

%description
Memtest86 is thorough, standalone memory test for x86 systems. It is
a standalone program and can be loaded from either a disk partition via
lilo or a floppy disk. Memtest86 uses a "moving inversions" algorithm
that is proven to be effective in finding memory errors.  The BIOS based
memory test is just a quick check that will often miss many of the
failures that are detected by Memtest86.

The ELF version should be used for booting from grub,
and avoids the following errors:
"Error 7: Loading below 1MB is not supported"
"Error 13: Invalid or unsupported executable format"
"Error 28: Selected item cannot fit into memory"

%description -l ru_RU.UTF-8
Тщательный и самостоятельный тест памяти для x86-систем, который может
быть загружен или с жесткого диска при помощи LILO/GRUB, или с дискеты.

Тест использует алгоритм "движущихся инверсий", доказавший свою
эффективность при обнаружении сбоев памяти. Не обращайте внимания на
"тест" BIOS: он практически ничего не значит, так как пропустит много
ошибок из тех, которые обнаружит memtest86.

Также может использоваться для создания загрузочной тест-дискеты.

%description -l uk_UA.UTF-8
Ретельний та самостійний тест пам'яті для x86-систем, що може бути
завантажений як з жорсткого диску за допомогою LILO/GRUB, так і з
дискети.

Тест використовує алгоритм "рухаючихся інверсій", який довів свою
ефективність при визначенні негараздів із пам'яттю. Не звертайте уваги
на "тест" BIOS: він практично нічого не означає, тому що пройде повз
багатьох збоїв з тих, що знаходить memtest86.

Також може використовуватися для створення завантажувальної
тест-дискети.

%prep
%setup

%build
%ifarch %ix86
cd build32
%else
cd build64
%endif
%make_build LD=/usr/bin/ld.bfd

%install
%ifarch %ix86
cd build32
%else
cd build64
%endif
install -pDm644 memtest.bin %buildroot/boot/memtest-%version.bin
%ifnarch %ix86
install -pDm644 memtest.efi %buildroot/boot/memtest-%version.efi
%endif
mkdir -p %buildroot%_sbindir
ln -s `relative /sbin/installkernel %_sbindir/installmemtest86+` \
	%buildroot%_sbindir/installmemtest86+

%post
%_sbindir/installmemtest86+ %version

%preun
%_sbindir/installmemtest86+ --remove %version

%files
/boot/memtest-%version.bin
%ifnarch %ix86
/boot/memtest-%version.efi
%endif
%_sbindir/installmemtest86+
%doc README.md

%changelog
* Sat Feb 04 2023 Anton Midyukov <antohami@altlinux.org> 6.10-alt1
- new version (6.10) with rpmgs script

* Tue Oct 25 2022 Anton Midyukov <antohami@altlinux.org> 6.00-alt1
- new version (6.00) with rpmgs script (Closes: 44133)
- cleanup spec
- update license field

* Sat Aug 06 2022 Anton Midyukov <antohami@altlinux.org> 5.31b-alt2
- NMU: fix build with gcc12

* Sun Jan 31 2021 Ilya Mashkin <oddity@altlinux.ru> 5.31b-alt1
- 5.31b

* Mon Jan 09 2017 Michael Shigorin <mike@altlinux.org> 5.01-alt2
- "fixed" FTBFS (by downgrading to gcc4)

* Wed May 28 2014 Michael Shigorin <mike@altlinux.org> 5.01-alt1
- 5.01:
  + added support for:
    - up to 2 TB of RAM on X64 CPUs
    - up to 32 cores SMT (experimental, via F2 at startup)
    - complete detection for memory controllers
    - motherboard manufacturer & model reporting
    - CPU temperature reporting
    - Intel "Sandy Bridge-E", "Ivy Bridge" CPUs
    - Intel "Haswell", "Haswell-ULT" CPUs (preliminary)
    - AMD "Kabini" (K16), "Bulldozer", "Trinity", "Bobcat" CPUs
    - Intel Atom "Pineview", "Cedar Trail" CPUs
    - SPD detection on most AMD Chipsets
  + assorted bugfixes
  + dropped #29048 patch (see also bnc#773569, lp#1071209)
- added fedora patches and description bits
  + initial build would fail to actually run tests for me
- build and package ELF binary too (e.g. for GRUB)

* Sun Jul 14 2013 Nikolay A. Fetisov <naf@altlinux.ru> 4.20-alt3
- Fix false positives on test #7 (Closes: 29048)

* Wed Nov 28 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.20-alt2.1
- Fixed build

* Fri Sep 23 2011 Alexey Tourbin <at@altlinux.ru> 4.20-alt2
- removed set_strip_method macro

* Tue Jan 25 2011 Michael Shigorin <mike@altlinux.org> 4.20-alt1
- 4.20:
  + added support for:
    - failsafe mode (F1 at startup)
    - Intel "Sandy Bridge" CPU
    - AMD "fusion" CPU
    - Coreboot "table forward"
  + corrected some memory brand not detected
  + various bug fixes

* Wed May 05 2010 Michael Shigorin <mike@altlinux.org> 4.10-alt1
- 4.10:
  + added support for:
    - Core i7 Extreme CPU (32nm)
    - Core i5/i3 (32 nm)
    - Pentium Gxxxx (32 mn)
    - Westmere-based Xeon
    - Intel Sandy Bridge (preliminary)
    - AMD 6-cores CPU
    - Intel 3200/3210
  + new installer for USB Key
  + fixed a crash at startup
  + many other bug fixes

* Wed Sep 23 2009 Michael Shigorin <mike@altlinux.org> 4.00-alt1
- 4.00:
  + major architectural changes
  + first pass twice faster (reduced iterations)
  + detect DDR2/3 brands and part numbers on Intel Chipsets
  + CPU detection:
    - corrected for Intel "Lynnfield" and AMD 45nm K10
    - added for Intel "Clarkdale" and "Gulftown", AMD "Magny-Cours"
    - added for CPU w/ 0.5/1.5/3/6/12/16/18/24MB L3
    - solved crash with AMD Geode LX
  + memory detection:
    - added for Intel XMP Memory
    - "clean" DMI for DDR3/FBDIMM2
    - improved for Integrated Memory Controllers
  + complies with SMBIOS 2.6.1 specs
  + fixed compilation issues with gcc 4.2+
  + many others bug fixes
- minor spec cleanup

* Mon Dec 29 2008 Michael Shigorin <mike@altlinux.org> 2.11-alt1
- 2.11:
  + added support for:
    - Intel Core i5 (Lynnfield) CPU
    - Intel P55 Southbridge
    - Intel PM45/GM45/GM47 Mobile chipset
    - Intel GL40/GS45 Mobile chipset
  + fixed:
    - DDR2/DDR3 detection on Intel x35/x45
    - detection on some Core i7 CPU
    - a bug with some AMI BIOS (freeze at startup)
    - various bugs

* Sat Nov 15 2008 Michael Shigorin <mike@altlinux.org> 2.10-alt1
- 2.10:
  + added support for:
    - Intel Core i7 (Nehalem), Atom CPU
    - Intel G41/G43/G45, P43/P45, US15W (Poulsbo) chipsets
    - Intel EP80579 (Tolapai) SoC CPU
    - ICH10 Southbridge (SPD/DMI)
  + added detection for Intel 5000X
  + added workaround for DDR3 DMI detection
  + now fully aware of CPU w/ L3 cache (Core i7 & K10)
  + fixed:
    - Intel 5000Z chipset detection
    - Memory Frequency on AMD K10
    - cache detection on C7/Isaiah CPU
    - Memtest86+ not recognized as Linux Kernel
- built with gcc 4.1 as upstream recommends for this version

* Sat Mar 29 2008 Michael Shigorin <mike@altlinux.org> 2.01-alt1
- 2.01:
  + added support for:
    - 45nm Mobile Core2 w/3Mb L2
    - i945GM/PM/GME, i946PL/GZ, iGM965/iGL960/iPM965/iGME965/iGLE960
  + added detection for:
    SiS 649/656/671/6, i430MX/i430TX
  + added an optional beep mode (pass completed w/o error)
  + pass duration 20%% reduced
  + removed blinking cursor
  + reverted Test #0 to cached
  + fixed:
    - major bug in Memory Address Errors Reporting
    - Intel Mac
    - Intel 3-Series (P35/X38) chipset init
    - a bug with SPD Display and ESB6300
    - a detection bug on P965/G965 C-Stepping
    - incoherency with pass progress indicator
    - Makefile to compile on x86_64
  + bootable Memtest86+ ISO more compatible
- 2.00 enhancements:
  + major architecture changes
  + modulo test now use random pattern for better accuracy
  + new Advanced DMI Errors Reporting Mode
  + added support for:
    - bus ratio changes on Intel Core CPU
    - non-integer bus ratio on latest Intel CPU
    - VIA C7/C7-D/C7-M/Eden on Esther Core
    - AMD K10 (Phenom) CPU w/timings detection
    - Intel Pentium E w/1 MB L2 Cache
    - Intel Core2 45nm (Penryn)
    - FSB1333/FSB1600 Intel CPU
    - Intel 5400A/5400B, Q35/P35/G33/Q33, X38/X48 w/timings detection
  + added preliminary support for:
    + VIA CN Isaiah CPU, Intel Nehalem
    + Intel 5000P/V/Z
  + added SPD Data Display for all Intel Chipsets (more to come)
  + added serial support as a linux boot parameter (Thanks to Michal S.)
  + removed on-the-fly memory timings change (unstable)
  + numerous (really) bug fixes

* Tue Oct 16 2007 Alex V. Myltsev <avm@altlinux.ru> 1.70-alt2
- fix build (thanks to ldv@)
- package FAQ

* Tue Jul 17 2007 Michael Shigorin <mike@altlinux.org> 1.70-alt1
- 1.70 (fixes #12126):
  + new features
    - add new DMI polling feature
    - add support for Core/Core2 Solo/Duo/Quad CPU
    - add support for AMD K8 with DDR2 Memory
    - add support for Intel CPU with 192/384 KB L2 Cache
    - add support for FB-DIMM based memory (DMI)
    - add detection for ALI CyberAladdin-T (M1644)
    - add detection for Turion 64 X2
    - add support for ATi Radeon xPress 3200
    - add support for Intel i975X
    - add support for Intel Q965/P965
    - add support for Intel Q963/Q965
  + bug fixes
    - force detection for AMD K8 with unknown chipsets
- spec macro abuse (and other) cleanup

* Mon Oct 23 2006 Serge Pavlovsky <pal@altlinux.ru> 1.65-alt3
- -fno-stack-protector

* Thu Feb 16 2006 Serge Pavlovsky <pal@altlinux.ru> 1.65-alt2
- added x86_64 to exclusivearch

* Thu Oct 06 2005 Serge Pavlovsky <pal@altlinux.ru> 1.65-alt1
- new version

* Mon Jul 04 2005 Serge Pavlovsky <pal@altlinux.ru> 1.60-alt1
- new version

* Wed Feb 16 2005 Serge Pavlovsky <pal@altlinux.ru> 1.51-alt1
- new version

* Sat Jan 22 2005 Serge Pavlovsky <pal@altlinux.ru> 1.50-alt1
- new version

* Mon Dec 27 2004 Serge Pavlovsky <pal@altlinux.ru> 1.40-alt3
- memtest86+

* Fri Jun 11 2004 Alexey Tourbin <at@altlinux.ru> 3.0-alt8
- use /sbin/installkernel from recent bootloader-utils
  in post/preun scripts; hopefully this should fix #3317

* Wed Nov 26 2003 Michael Shigorin <mike@altlinux.ru> 3.0-alt7
- removed dependency on initscripts;
  thanks Nick Fedchik <nick fedchik org ua> for noticing

* Sat Oct 25 2003 Michael Shigorin <mike@altlinux.ru> 3.0-alt6
- updated patch by Andrey Liakhovets:
  AMD Athlon XP support, general cleanups

* Mon Oct 06 2003 Michael Shigorin <mike@altlinux.ru> 3.0-alt5
- updated patch by AL (now handles VIA C3 too); changed its company prefix
  from "alt" to "rover" as it should reflect the origin more properly
- added README.rover (see also #2648 history) and cpus/ to docs
- minor spec cleanup, TODO update

* Thu Sep 25 2003 Michael Shigorin <mike@altlinux.ru> 3.0-alt4
- added buildrequires to "fix" hasher build
- hopefully fixed #2648;
  thanks to Andrey Liakhovets <lyakhovetz rovercomputers ru>

* Thu Nov 28 2002 Michael Shigorin <mike@altlinux.ru> 3.0-alt3
- major bugfix: rolled back broken gcc3 build attempt, hardwired compat-gcc

* Fri Oct 18 2002 Stanislav Ievlev <inger@altlinux.ru> 3.0-alt2
- rebuild with gcc3

* Wed May 29 2002 Michael Shigorin <mike@altlinux.ru> 3.0-alt1
- new version

* Sat May 04 2002 Michael Shigorin <mike@altlinux.ru> 2.9-alt2
- 2.8-alt3 reverse fix somehow managed to pass by 2.9-alt1, so it just
  didn't update the bootsector.  Fixed; sorry for that :-(

* Sat Apr 13 2002 Michael Shigorin <mike@altlinux.ru> 2.9-alt1
- new version

* Thu Mar 28 2002 Michael Shigorin <mike@altlinux.ru> 2.8-alt3
- fixed post/preun scriptlets (installmemtest86 error handling by rpm)
- undone module search path "fix" in installmemtest86 (apparently broken by me)

* Tue Mar 26 2002 Michael Shigorin <mike@altlinux.ru> 2.8-alt2
- added missing PreReq: bootloader-utils

* Fri Nov 23 2001 Michael Shigorin <mike@altlinux.ru> 2.8-alt1
- alt1: 2.8a from memtest86.com
  spec synced with and install script borrowed from Mandrake Cooker src.rpm
  moved install script from /usr/share/loader/ to /usr/sbin
