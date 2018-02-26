Name: memtest86
Version: 4.0a
Release: alt2

Summary: Memory test for x86 architecture
License: GPL
Group: System/Kernel and hardware

Url: http://www.memtest86.com
Source0: %url/%name-%version.tar.gz
Source2: memtest86-3.0-README.rover
Source3: memtest86-3.0-rover-tested_cpus.tar.gz
Patch0: memtest86-3.0-rover-centrino+c3+amd.patch
Patch1: memtest86-3.2-rover-fixcrash.patch
Packager: Michael Shigorin <mike@altlinux.org>

ExclusiveArch: %ix86 x86_64
BuildRequires: dev86
Requires(post,preun): bootloader-utils >= 0.3

Summary(ru_RU.KOI8-R): Тест памяти для x86-архитектуры
Summary(uk_UA.KOI8-U): Тест пам'ят╕ для x86-арх╕тектури

%description
Memtest86 is thorough, standalone memory test for x86 systems.

Memtest86 is a standalone program and can be loaded from either a disk
partition via lilo or a floppy disk. Memtest86 uses "moving inversions"
algorithm that is proven to be effective in finding memory errors.
The BIOS based memory test is just a quick check that will often miss
many of the failures that are detected by Memtest86.

%description -l ru_RU.KOI8-R
Memtest86 -- тщательный и самостоятельный тест памяти для x86-систем.
Он может быть загружен или с жесткого диска при помощи LILO/GRUB,
или с дискеты.

Тест использует алгоритм "движущихся инверсий", доказавший свою
эффективность при обнаружении сбоев памяти. Не обращайте внимания
на "тест" BIOS -- он практически ничего не значит, так как
пропустит много ошибок из тех, которые обнаружит memtest86.

Также может использоваться для создания загрузочной тест-дискеты.

%description -l uk_UA.KOI8-U
Memtest86 -- ретельний та самост╕йний тест пам'ят╕ для x86-систем.
В╕н може бути завантажений як з жорсткого диску за допомогою LILO/GRUB,
так ╕ з дискети.

Тест використову╓ алгоритм "рухаючихся ╕нверс╕й", який дов╕в свою
ефективн╕сть при визначенн╕ негаразд╕в ╕з пам'яттю. Не звертайте уваги
на "тест" BIOS -- в╕н практично н╕чого не означа╓, тому що пройде повз
багатьох збо╖в з тих, що знаходить memtest86.

Також може використовуватися для створення завантажувально╖
тест-дискети.

%prep
%setup
%patch1 -p1

%build
make	# intentionally without optimizations

%install
install -m644 -pD memtest.bin %buildroot/boot/memtest-%version.bin

%post
/sbin/installkernel --memtest %version

%preun
/sbin/installkernel --memtest --remove %version

%files
/boot/memtest-%version.bin
%doc README*

%changelog
* Fri Sep 23 2011 Alexey Tourbin <at@altlinux.ru> 4.0a-alt2
- removed set_strip_method macro

* Fri Sep 23 2011 Michael Shigorin <mike@altlinux.org> 4.0a-alt1
- 4.0a:
  + Multi-CPU Support!
    Multi-threaded for parallel testing of memory with up to 16 CPUs
  + Works with up to 64Gb of memory
  + Supports 32 and 64 bit CPUs
  + Supports all memory types (DDR, DDR2, DDR3)
  + Corrections in bugfix A:
    - Fix for erroneous errors in tests 7 and 8 errors when
      the number of cores is not a power of 2 (6 and 12 cores).
    - Fixed cache detection for newer Intel CPUs
- dropped patch2 (merged upstream)

* Tue Feb 10 2009 Michael Shigorin <mike@altlinux.org> 3.5-alt2
- ah, so -m32 should work by now

* Mon Feb 09 2009 Michael Shigorin <mike@altlinux.org> 3.5-alt1
- 3.5:
  + limited SMP support
  + support for detection of additional chipsets
    (from Memtest86+ v2.11)
  + better CPU detection including reporting of L3 cache
  + reworked information display
  + abbreviated iterations for first pass
  + enhancements to memory sizing
  + bugfixes
- updated makefile patch

* Sat Jun 21 2008 Michael Shigorin <mike@altlinux.org> 3.4-alt1
- 3.4:
  + added error summary display
  + added upport for additional chipsets (from memtest86+ v1.70)
  + additions/corrections for CPU detection
  + added support for memory module information reporting
  + bugfixes
- fix build with SSP-enabled gcc4.1 again (this time a patch)
- buildreq

* Wed Jun 27 2007 Michael Shigorin <mike@altlinux.org> 3.3-alt1
- 3.3

* Sat Oct 14 2006 Michael Shigorin <mike@altlinux.org> 3.2-alt3
- fix build with SSP-enabled gcc4.1 (thanks damir@ and wrar@)

* Fri Mar 03 2006 Michael Shigorin <mike@altlinux.org> 3.2-alt2
- re-added fix for crash with unknown CPU cache
  (courtesy of Andrey Liakhovets again)

* Wed Feb 22 2006 Michael Shigorin <mike@altlinux.org> 3.2-alt1
- 3.2
- built with current gcc
- disabled rover modifications; many thanks to Andrey Liakhovets
  for doing them but seems I'm not in position to check whether
  any of them are merged upstream (seems we've sent the patches)
  or that the result of forward-porting would really work;
  so if you need them, please get 3.0-alt6+ from ALC2.3/ALM2.4
  -- or have a look at memtest86+ package.
- removed redundant installmemtest86 (which was a symlink 
  since last build), added installkernel parameter instead
- spec cleanup

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
