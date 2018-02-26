Name: apmd
Version: 3.2.2
Release: alt5
Epoch: 1
%define subver 3

#  Devel-static is omitted by default,
#  but may be overridden using 'rpmbuid --with static ...'
%def_without static

Summary: Advanced Power Management (APM) BIOS utilities for laptops
License: GPL
Group: System/Servers

Url: ftp://ftp.debian.org/debian/pool/main/a/%name
Source0: %url/%{name}_%version.orig.tar.gz
Source1: apmd.init
Source2: apmd_proxy
Source3: apmd.conf
Source4: apmd.README.ALT
Patch1: %url/%{name}_%version-%subver.diff.gz
Patch2: %name-3.2.1-alt-makefile.patch
Patch3: %name-3.2.1-alt-doc.patch
Patch4: %name-3.2.1-alt-fixes.patch
Patch5: apmd-3.2.2-pld-libtool.patch
Packager: Michael Shigorin <mike@altlinux.org>

# Automatically added by buildreq on Wed May 13 2009
BuildRequires: libXaw-devel libXext-devel

Requires: libapm = %version-%release
PreReq: powermgmt-base
Requires(post): %post_service
Requires(preun): %preun_service

ExclusiveArch: %ix86

Summary(ru_RU.KOI8-R): Утилиты управления системой питания (APM BIOS)

%package -n xapm
Summary: The X11 utility that displays APM BIOS information
Summary(ru_RU.KOI8-R): Графическая утилита для показа информации BIOS об APM
Group: System/XFree86
Requires: %name = %version-%release
Provides: %name-x11 = %version-%release
Obsoletes: %name-x11

%package -n libapm
Summary: The shared library for interacting with the kernel APM driver
Summary(ru_RU.KOI8-R): Библиотека для взаимодействия с APM-драйвером ядра
Group: System/Libraries

%package -n libapm-devel
Summary: The development library and header files for APM
Summary(ru_RU.KOI8-R): Средства разработки для доступа к APM
Group: Development/C
Requires: libapm = %version-%release
Provides: apmd-devel = %version-%release
Obsoletes: apmd-devel

%if_with static
%package -n libapm-devel-static
Summary: The development library for linking APM access functions statically
Summary(ru_RU.KOI8-R): Статическая библиотека для работы с APM
Group: Development/C
Requires: libapm-devel = %version-%release
%endif

%description
On laptop computers, the Advanced Power Management (APM) support provides
access to battery status information and may help you to conserve
battery power, depending on your laptop and the APM implementation.
The apmd program also lets you run arbitrary programs when APM events
happen (for example, you can eject PCMCIA devices when you suspend,
or change hard drive timeouts when you connect the battery).

This package contains apmd(8), a daemon for logging and acting on APM
events; and apm(1), a client that prints the information in /proc/apm
in a readable format.

%description -l ru_RU.KOI8-R
На портативных компьютерах функции расширенного управления питанием
(Advanced Power Management, APM) служат для доступа к информации
о состоянии батареи и управления режимом энергопотребления.

Данный пакет содержит apmd(8), демон для протоколирования и реакции
на исходящие от APM события, а также консольную утилиту apm(1)
для распечатки информации из /proc/apm в читабельном виде.

Примерами реакции на APM-события могут служить отключение PCMCIA-устройств
при переходе в спящий режим или увеличение таймаута бездействия диска
при подключении дополнительной батареи.

%description -n xapm
On laptop computers, the Advanced Power Management (APM) support provides
access to battery status information and may help you to conserve battery
power, depending on your laptop and the APM implementation.

This package contains xapm(1), an X11 utility that displays APM BIOS
information.

%description -n xapm -l ru_RU.KOI8-R
На портативных компьютерах функции расширенного управления питанием
(Advanced Power Management, APM) служат для доступа к информации
о состоянии батареи и управления режимом энергопотребления.

Данный пакет содержит xapm, утилиту для показа состояния APM
в графическом режиме.

%description -n libapm
On laptop computers, the Advanced Power Management (APM) support provides
access to battery status information and may help you to conserve battery
power, depending on your laptop and the APM implementation.

This package contains a shared library that provides support for
interacting with the APM driver in the kernel.

%description -n libapm -l ru_RU.KOI8-R
На портативных компьютерах функции расширенного управления питанием
(Advanced Power Management, APM) служат для доступа к информации
о состоянии батареи и управления режимом энергопотребления.

Данный пакет содержит динамическую разделяемую библиотеку,
через которую программы осуществляют взаимодействие с драйвером APM,
расположенным в ядре.

%description -n libapm-devel
On laptop computers, the Advanced Power Management (APM) support provides
access to battery status information and may help you to conserve battery
power, depending on your laptop and the APM implementation.

This package contains a library and header files needed to write programs
that interact with the APM driver in the kernel.

%description -n libapm-devel -l ru_RU.KOI8-R
На портативных компьютерах функции расширенного управления питанием
(Advanced Power Management, APM) служат для доступа к информации
о состоянии батареи и управления режимом энергопотребления.

Данный пакет содержит заголовочные файлы и подсказки, необходимые
для разработки и сборки программ, использующих библиотеку доступа
к функциям драйвера APM.

%if_with static

%description -n libapm-devel-static
On laptop computers, the Advanced Power Management (APM) support provides
access to battery status information and may help you to conserve battery
power, depending on your laptop and the APM implementation.

This package contains a library needed to static linking programs
that interact with the APM driver in the kernel.

%description -n libapm-devel-static -l ru_RU.KOI8-R
На портативных компьютерах функции расширенного управления питанием
(Advanced Power Management, APM) служат для доступа к информации
о состоянии батареи и управления режимом энергопотребления.

Данный пакет содержит библиотеку для статической компоновки программ,
использующих APM.

%endif

%prep
%setup -q -n %name-%version.orig
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
install -p -m644 %SOURCE4 README.ALT

%build
#make_build
make

%install
mkdir -p %buildroot%_mandir/man{1,8}
%make_install install DESTDIR=%buildroot
install -p -m644 {apm,apmsleep,xapm}.1 %buildroot%_man1dir/
install -p -m644 apmd.8 %buildroot%_man8dir/
install -pD -m755 %SOURCE1 %buildroot%_initdir/%name
install -pD -m755 %SOURCE2 %buildroot%_sysconfdir/apm/apmd_proxy
install -pD -m644 %SOURCE3 %buildroot%_sysconfdir/sysconfig/%name

%post
%post_service apmd

%preun
%preun_service apmd

%files
%_sbindir/*
%_bindir/*
%exclude %_bindir/xapm
%_mandir/man?/*
%exclude %_man1dir/xapm.*
%config %_initdir/%name
%config %_sysconfdir/apm/apmd_proxy
%config(noreplace) %_sysconfdir/sysconfig/%name
%doc AUTHORS ChangeLog LSM *README*

%files -n xapm
%_bindir/xapm
%_man1dir/xapm.*

%files -n libapm
%_libdir/*.so.*

%files -n libapm-devel
%_libdir/*.so
%_includedir/*

%if_with static
%files -n libapm-devel-static
%_libdir/libapm.a
%else
%exclude %_libdir/libapm.a
%endif

%changelog
* Wed May 13 2009 Michael Shigorin <mike@altlinux.org> 1:3.2.2-alt5
- applied three-year-and-two-days old PLD patch
  to fix build with newer libtool
- minor spec cleanup
- buildreq

* Sun Nov 09 2008 Michael Shigorin <mike@altlinux.org> 1:3.2.2-alt4
- rebuilt against current libXaw-devel

* Tue May 27 2008 Michael Shigorin <mike@altlinux.org> 1:3.2.2-alt3
- fixed build (buildreq)
- spec macro abuse cleanup
- added myself as a Packager:

* Mon Oct 10 2005 Ilya Evseev <evseev@altlinux.ru> 1:3.2.2-alt2
- Fixed bug in URL macro

* Tue Mar  8 2005 Ilya Evseev <evseev@altlinux.ru> 1:3.2.2-alt1
- Updated to 3.2.2-3.
- Specfile: added russian summaries/descriptions
- Build static library (optionally)

* Mon Apr 19 2004 Dmitry V. Levin <ldv@altlinux.org> 1:3.2.1-alt1
- Updated to 3.2.1.
- Reviewed patches:
  + all old patches appear to be obsolete and therefore removed;
  + applied generic patch from Debian apmd package (3.2.1-4);
  + applied patch required for proper build;
  + fixed potential descriptor leak problems.
- Repackaged:
  + old: apmd + apmd-x11 + apmd-devel;
  + new: libapm + libapm-devel + apmd + xapm.
- Rewritten startup script.
- Removed all apm scripts, use new powermgmt infrastructure.

* Mon Feb 03 2003 Rider <rider@altlinux.ru> 1:3.0.2-alt5
- fix init script for start apmd after syslog

* Fri Dec 13 2002 Rider <rider@altlinux.ru> 1:3.0.2-alt4
- removed bad pustun trigger
- BuildReq added

* Mon Dec 09 2002 Rider <rider@altlinux.ru> 1:3.0.2-alt3
- fixed bug #0001669

* Tue Dec 03 2002 Rider <rider@altlinux.ru> 1:3.0.2-alt2
- move xapm to %name-x11 package

* Mon Nov 18 2002 Rider <rider@altlinux.ru> 1:3.0.2-alt1
- new version
- patches from RedHat

* Wed Sep 12 2001 Dmitry V. Levin <ldv@altlinux.ru> 3.0final-ipl19mdk
- Corrected startup script to attempt modprobe apm.

* Mon Mar 19 2001 Dmitry V. Levin <ldv@altlinux.ru> 3.0final-ipl18mdk
- Fixed Requires.

* Thu Feb 22 2001 Dmitry V. Levin <ldv@fandra.org> 3.0final-ipl17mdk
- Fixed error reporting.
- Reenabled default startup runlevels.

* Sat Feb 17 2001 Dmitry V. Levin <ldv@fandra.org> 3.0final-ipl16mdk
- Merged some RH patches.
- Fixed apmd-scripts.

* Sun Jan 21 2001 Dmitry V. Levin <ldv@fandra.org> 3.0final-ipl15mdk
- RE adaptions.

* Tue Nov 28 2000 Chmouel Boudjnah <chmouel@mandrakesoft.com> 3.0final-15mdk
- Make apmd-devel requires apmd.
- Make %%config files as (noreplace).
- script_version 1.4.0.

* Mon Nov 27 2000 Chmouel Boudjnah <chmouel@mandrakesoft.com> 3.0final-14mdk
- No need to build xapm.

* Thu Nov  2 2000 Chmouel Boudjnah <chmouel@mandrakesoft.com> 3.0final-13mdk
- Set clock --hctosys after suspend (#742).

* Tue Oct  3 2000 Chmouel Boudjnah <chmouel@mandrakesoft.com> 3.0final-12mdk
- Fix spelling error.
- Add NETWORK_RESTART option for some laptop.

* Tue Oct  3 2000 Chmouel Boudjnah <chmouel@mandrakesoft.com> 3.0final-11mdk
- remove silly temporary files (thks Alexander).

* Mon Oct  2 2000 Chmouel Boudjnah <chmouel@mandrakesoft.com> 3.0final-10mdk
- Upgrade to bero 1.4.9 scripts.

* Mon Oct  2 2000 Chmouel Boudjnah <chmouel@mandrakesoft.com> 3.0final-9mdk
- Integrated suggetions of (Michael Reinsch <mr@uue.org>) :
		- Fix shell syntax in LOCk_X
		- use RESTORESOUNDPROGS only when lsof is here.
		- use service sound to restore the sound and remove the SOUNDMODULES stuff.

* Tue Sep 26 2000 Chmouel Boudjnah <chmouel@mandrakesoft.com> 3.0final-8mdk
- Merge with rh scripts.

* Wed Jul 19 2000 Chmouel Boudjnah <chmouel@mandrakesoft.com> 3.0final-7mdk
- Don't resumie anancron job if we are low in power.
- Resume sound if the commercial oss drivers are loaded.
- BM.
- Macros.

* Sun Jun  4 2000 Chmouel Boudjnah <chmouel@mandrakesoft.com> 3.0final-6mdk
- Upgrade apm_script from rh.
- Add SUSPEND_USB option to apm_script.

* Tue Apr 25 2000 Chmouel Boudjnah <chmouel@mandrakesoft.com> 3.0final-5mdk
- Remove bogus require from -devel.

* Fri Apr  7 2000 Chmouel Boudjnah <chmouel@mandrakesoft.com> 3.0final-4mdk
- Fix apmd-devel groups.

* Wed Mar 29 2000 Chmouel Boudjnah <chmouel@mandrakesoft.com> 3.0final-3mdk
- bzip2 man pages (again afther johnb).

* Sun Mar 19 2000 John Buswell <johnb@mandrakesoft.com> 3.0final-2mdk
- Added PPC support

* Mon Mar 13 2000 Chmouel Boudjnah <chmouel@mandrakesoft.com> 3.0final-1mdk
- Adjust groups.
- Upgrade to debian 3.0final.
- Upgrade 1.2.1 redhat script.
- Clean up specs.

* Mon Dec 20 1999 Frederic Lepied <flepied@mandrakesoft.com> 3.0beta9-6mdk

- added graphic switch patch.

* Fri Nov 12 1999 Chmouel Boudjnah <chmouel@mandrakesoft.com>
- Merge with the rh package :
  - Put in new apm scripts to handle PCMCIA suspend/resume, and give the
  possibility to refresh displays and reload sound modules for some
  broken chipsets.

* Mon Oct 25 1999 Chmouel Boudjnah <chmouel@mandrakesoft.com>
- Add a provides to fix ghost bug with rpm :-\.

* Mon Oct 18 1999 Chmouel Boudjnah <chmouel@mandrakesoft.com>
- 3.0beta9.
- Split package with -devel.

* Wed Jun 23 1999 Bernhard RosenkrДnzer <bero@mandrakesoft.com>
- 3.0beta8

* Tue Jun 22 1999 Chmouel Boudjnah <chmouel@mandrakesoft.com>

- Merging with RedHat change :
	- add check for /proc/apm (not on SMP) (#3403)
	- shell script tweak (#3176).

* Fri May  7 1999 Bill Nottingham <notting@redhat.com>
- set -u flag for utc

* Sat Apr 17 1999 Matt Wilson <msw@redhat.com>
- prereqs chkconfig

* Fri Apr 16 1999 Cristian Gafton <gafton@redhat.com>
- exlusive arch i3786, as sparcs and alphas have no apm support...

* Wed Apr 14 1999 <ewt@redhat.com>
- removed X bits; gnome has a much better X interface for apm anyway

* Sun Mar 21 1999 Cristian Gafton <gafton@redhat.com>
- auto rebuild in the new build environment (release 4)

* Fri Mar 19 1999 Preston Brown <pbrown@redhat.com>
- quoted APMD_OPTIONS variable in the init script

* Tue Mar 09 1999 Preston Brown <pbrown@redhat.com>
- whoops, making /etc/rc.d/init.d/apmd a directory was a bad idea. fixed.

* Mon Mar 08 1999 Preston Brown <pbrown@redhat.com>
- now owned by Avery Pennarun <apenwarr@debian.org>, upgraded to his latest.

* Wed Feb 24 1999 Preston Brown <pbrown@redhat.com>
- Injected new description and group.

* Fri Nov 06 1998 Preston Brown <pbrown@redhat.com>
- updated to latest patchlevel from web page.

* Wed Apr 22 1998 Michael K. Johnson <johnsonm@redhat.com>
- enhanced init script

* Thu Apr 1 1998 Erik Troan <ewt@redhat.com>
- moved init script into a separate source file
- added restart and status options to initscript
- made it use a build root
- don't start apm when the package is installed
- don't stop apm when the package is removed

* Mon Dec  8 1997 Jan "Yenya" Kasprzak <kas@fi.muni.cz>
- Compiled on RH5.0 against libc6.
- Renamed /etc/rc.d/init.d/apmd.init to /etc/rc.d/init.d/apmd
- Make /etc/rc.d/init.d/apmd to be chkconfig-compliant.

* Thu Oct  2 1997 Jan "Yenya" Kasprzak <kas@fi.muni.cz>
- Fixed buggy /etc/sysconfig/apmd file generation in the spec file.
- Added a patch for apm.c's option handling.
- Both fixes were submitted by Richard D. McRobers <rdm@csn.net>
