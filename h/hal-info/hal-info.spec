%define _fdidir %_datadir/hal/fdi

Summary: Device information files for HAL
Name: hal-info
Version: 20091130
Release: alt1
License: AFL/GPL
Group: System/Libraries
URL: http://www.freedesktop.org/Software/hal
Packager: Valery Inozemtsev <shrek@altlinux.ru>

Conflicts: hal < 0.5.12

Source: %name-%version.tar
Patch: %name-%version-%release.patch

BuildArch: noarch
BuildRequires: libhal-devel >= 0.5.11

%description 
The hal-info package contains various device information files for the hal package.

%prep
%setup -q
%patch -p1

echo %version > VERSION

%build
%autoreconf
%configure \
	--disable-killswitch-thinkpad-bluetooth \
	--disable-killswitch-iwl-wlan

%install
%make DESTDIR=%buildroot install

%files
%dir %_datadir/hal
%dir %_fdidir
%dir %_fdidir/information
%dir %_fdidir/preprobe
%dir %_fdidir/information/10freedesktop
%dir %_fdidir/information/20thirdparty
%dir %_fdidir/preprobe/10osvendor
%_fdidir/information/*/*.fdi
%_fdidir/preprobe/10osvendor/*.fdi

%changelog
* Tue Dec 01 2009 Valery Inozemtsev <shrek@altlinux.ru> 20091130-alt1
- 20091130

* Mon Jul 20 2009 Valery Inozemtsev <shrek@altlinux.ru> 20090716-alt1
- 20090716

* Tue Apr 14 2009 Valery Inozemtsev <shrek@altlinux.ru> 20090414-alt1
- 20090414

* Mon Mar 30 2009 Valery Inozemtsev <shrek@altlinux.ru> 20090330-alt1
- 20090330

* Mon Mar 09 2009 Valery Inozemtsev <shrek@altlinux.ru> 20090309-alt1
- 20090309

* Wed Feb 04 2009 Valery Inozemtsev <shrek@altlinux.ru> 20090202-alt0.M50.1
- build for branch 5.0

* Wed Feb 04 2009 Valery Inozemtsev <shrek@altlinux.ru> 20090202-alt1
- 20090202

* Thu Jan 15 2009 Valery Inozemtsev <shrek@altlinux.ru> 20081219-alt4
- droped EeePC killswitch
- added EeePC keymap

* Tue Dec 30 2008 Valery Inozemtsev <shrek@altlinux.ru> 20081219-alt3
- corrected EeePC check

* Tue Dec 30 2008 Valery Inozemtsev <shrek@altlinux.ru> 20081219-alt2
- added EeePC killswitch

* Fri Dec 19 2008 Valery Inozemtsev <shrek@altlinux.ru> 20081219-alt1
- 20081219

* Thu Nov 27 2008 Valery Inozemtsev <shrek@altlinux.ru> 20081022-alt6
- disable killswitch iwl wlan

* Thu Nov 27 2008 Valery Inozemtsev <shrek@altlinux.ru> 20081022-alt5
- build for hal-0.5.12

* Tue Nov 25 2008 Valery Inozemtsev <shrek@altlinux.ru> 20081022-alt3.M41.1
- build for branch 4.1

* Mon Nov 24 2008 Valery Inozemtsev <shrek@altlinux.ru> 20081022-alt4
- packaged fdi/information/20thirdparty

* Mon Nov 24 2008 Valery Inozemtsev <shrek@altlinux.ru> 20081022-alt2.M41.1
- build for branch 4.1

* Mon Nov 24 2008 Valery Inozemtsev <shrek@altlinux.ru> 20081022-alt3
- added lost fdi/information/20thirdparty/10-modem.fdi

* Fri Nov 21 2008 Valery Inozemtsev <shrek@altlinux.ru> 20081022-alt1.M41.1
- build for branch 4.1

* Wed Nov 19 2008 Valery Inozemtsev <shrek@altlinux.ru> 20081022-alt2
- ipw-rfkill: added iwlagn driver

* Wed Oct 22 2008 Valery Inozemtsev <shrek@altlinux.ru> 20081022-alt1
- 20081022

* Mon Oct 13 2008 Valery Inozemtsev <shrek@altlinux.ru> 20081013-alt1
- 20081013

* Tue Oct 07 2008 Valery Inozemtsev <shrek@altlinux.ru> 20080508-alt3
- added EeePC CardReader (close #17464)

* Tue Sep 09 2008 Valery Inozemtsev <shrek@altlinux.ru> 20080508-alt2
- add SonyEricsson W800/K790/P1i, Motorola V3r, Nokia 3109c/6300/E50/E61/N81, Samsung SGH-E900 as GSM modem

* Thu May 08 2008 Valery Inozemtsev <shrek@altlinux.ru> 20080508-alt1
- 20080508

* Mon Mar 31 2008 Valery Inozemtsev <shrek@altlinux.ru> 20080317-alt1
- 20080317

* Sat Mar 15 2008 Valery Inozemtsev <shrek@altlinux.ru> 20080313-alt1
- 20080313

* Mon Mar 10 2008 Valery Inozemtsev <shrek@altlinux.ru> 20080310-alt1
- 20080310

* Sat Feb 16 2008 Valery Inozemtsev <shrek@altlinux.ru> 20080215-alt1
- 20080215

* Mon Dec 17 2007 Valery Inozemtsev <shrek@altlinux.ru> 20071212-alt0.M40.1
- build for branch 4.0

* Thu Dec 13 2007 Valery Inozemtsev <shrek@altlinux.ru> 20071212-alt1
- 20071212

* Thu Nov 22 2007 Valery Inozemtsev <shrek@altlinux.ru> 20071030-alt1.M40.1
- build for branch 4.0

* Mon Nov 19 2007 Valery Inozemtsev <shrek@altlinux.ru> 20071030-alt2
- split K750i, W810i, K610i, W300i mobile phone information

* Wed Oct 30 2007 Valery Inozemtsev <shrek@altlinux.ru> 20071030-alt1
- 20071030

* Fri Oct 12 2007 Valery Inozemtsev <shrek@altlinux.ru> 20071011-alt1
- 20071011

* Sun Sep 30 2007 Valery Inozemtsev <shrek@altlinux.ru> 20070925-alt1
- 20070925

* Mon Sep 03 2007 Valery Inozemtsev <shrek@altlinux.ru> 20070831-alt1
- 20070831

* Mon Jul 30 2007 Valery Inozemtsev <shrek@altlinux.ru> 20070725-alt1
- 20070725
