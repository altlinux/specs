Name: input-utils
Version: 20110106
Release: alt1

Summary: A Set of Utilities for Input Devices

Group: System/Configuration/Hardware
License: GPL v2 or later
Url: http://linuxconsole.sourceforge.net/input/input.html

Packager: Vitaly Lipatov <lav@altlinux.ru>

Conflicts: dvb-utils <= 0.9.4-alt2
Conflicts: linuxtv-dvb-apps <= 1.1.1-alt1

# Source-url: https://launchpad.net/ubuntu/+archive/primary/+files/input-utils_0.0.%version.orig.tar.gz
Source: %name-%version.tar

%description
Utilities for input devices. It includes joystick testing and
calibration, force feedback testing, and generic event tools.

%prep
%setup

%build
%make_build

%install
%makeinstall_std prefix=%prefix

%files
%_bindir/*
%_man8dir/*

%changelog
* Sun Jul 31 2011 Vitaly Lipatov <lav@altlinux.ru> 20110106-alt1
- new version (20110106) with rpmbs script (ALT bug #25968)

* Sun Oct 21 2007 Vitaly Lipatov <lav@altlinux.ru> 2007.06.22-alt1
- initial build for ALT Linux Sisyphus (fix bug #10133)

* Fri Jun 22 2007 - jdelvare@suse.de
- input-utils-2005.08.02-prototypes.diff: Drop the change to
  fftest.c, which is no longer needed.
- Update to current SVN. This brings a fix to attachinput (286271).
- Rename input-utils-2005.08.02-prototypes.diff to
  input-utils-ffmvforce-on_exit-prototype-fix.diff, polish it for
  upstream submission.
- input-utils-inputattach-update-help-text.diff: Update the
  inputattach help text; submitted upstream.
* Wed Jan 25 2006 - mls@suse.de
- converted neededforbuild to BuildRequires
* Tue Aug 02 2005 - mjancar@suse.cz
- update to current cvs
* Fri May 28 2004 - mcihar@suse.cz
- update to current cvs
- renamed to input-utils and included more programs (see bug #40444)
* Sun Jan 11 2004 - adrian@suse.de
- add %%defattr
* Wed Oct 30 2002 - mcihar@suse.cz
- updated to latest CVS version (excluding things that work only with 2.5.x
  kernels)
- jstest patch to fix cooperation with YaST
* Thu Nov 22 2001 - vinil@suse.cz
- update to cvs version
- temporarily removed twiddler support because of missing
  definitions in linux/serio.h (glibc-devel)
- description fixed
* Mon Nov 13 2000 - ro@suse.de
- don't include linux/module.h if not needed
* Fri Jun 16 2000 - vinil@suse.cz
- modules removed
- binaries are striped
- description fixed
* Tue May 23 2000 - vinil@suse.cz
- buildroot and description fixed
* Tue May 09 2000 - vinil@suse.cz
- update to 1.2.15
- buildroot added
* Fri Jan 21 2000 - ro@suse.de
- update to 1.2.14
* Mon Dec 06 1999 - ro@suse.de
- use RPM_OPT_FLAGS for CFLAGS
* Mon Sep 13 1999 - bs@suse.de
- ran old prepare_spec on spec file to switch to new prepare_spec.
* Mon Nov 16 1998 - ro@suse.de
- compile binaries only
* Thu Dec 11 1997 - ro@suse.de
- moved usr/include/linux/joystick.h to usr/doc/packages/joystick
* Thu Oct 09 1997 - ro@suse.de
- first suse version 0.8.0
  kernel module will be contained in package kernmod
  devices are not remade, since included in package devs
