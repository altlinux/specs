# spec file for package opie (Version 2.4)
#
# Copyright (c) 2010 SUSE LINUX Products GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/

Name: opie
#!BuildIgnore: opie
BuildRequires: bison libpam-devel
Url: http://www.inner.net/opie
Version: 2.4
Release: alt1
License: GPLv2+
Group: System/Base
Provides: pam_opie
%define name_pam         pam_opie
%define version_pam	 0.21
Packager: Mykola Grechukh <gns@altlinux.ru>

Source: %name-%version.tar.bz2
Source1: %name_pam-%version_pam.tar.bz2
Source2: baselibs.conf
Patch: %name-%version.diff
Patch1: %name_pam-%version_pam.diff
Patch2: %name-%version.newseed.diff
Patch3: uint4_def.patch
Patch4: %name-2.4-bison.patch
Patch5: %name-2.4-nonvoid.patch
Patch6: %name-2.4-decl.diff
Patch7: %name-2.4-nul-overflow.patch
Patch8: %name-2.4-cxx.patch
Patch9: %name-2.4-undef.patch
Patch10: %name-2.4-noroot.patch
Patch11: %name-%{version}_array-subscript.patch
Patch12: %name_pam-%{version_pam}_array-subscript.patch
Patch13: %name-2.4-getline.patch
Patch14: %name-2.4-fclose.patch
Summary: Support for One-Time Passwords

%description
OPIE stands for One-time Passwords In Everything. One-time passwords
can be used to foil password sniffers because they cannot be reused by
the attacker.

This package provides a PAM module and several utility programs that
let you use one-time passwords for authentication.

%package devel
Summary: development headers for opie
Group: Development/C

%description devel
OPIE stands for One-time Passwords In Everything. One-time passwords
can be used to foil password sniffers because they cannot be reused by
the attacker.

This package provides include files required to link applications with opie

%prep
%setup -n %name-%version -a 1
%patch0 -p1
%patch2 -p1
%patch3
%patch4
%patch5
%patch6 -p1
%patch7 -p1
%patch8 -p1
%patch9
perl -pi -e 's/(?<!DESTDIR\))\$\(KEY_FILE\)/\$\(DESTDIR\)\$\(KEY_FILE\)/g' Makefile.in
perl -pi -e 's/(?<!DESTDIR\))\$\(LOCK_DIR\)/\$\(DESTDIR\)\$\(LOCK_DIR\)/g' Makefile.in
perl -pi -e 's/(?<!DESTDIR\))\$\(LOCALBIN\)/\$\(DESTDIR\)\$\(LOCALBIN\)/g' Makefile.in
perl -pi -e 's/(?<!DESTDIR\))\$\(LOCALMAN\)/\$\(DESTDIR\)\$\(LOCALMAN\)/g' Makefile.in
%patch10 -p1
%patch11
cd %name_pam
%patch1 -p0
%patch12
cd ..
%patch13
%patch14

%build
# build opie
export CFLAGS="$RPM_OPT_FLAGS -fno-strict-aliasing"
%configure --enable-insecure-override
%make_build
# build pam_opie
cd %name_pam
%make_build

%install
# install opie
mkdir -p %buildroot/etc
mkdir -p %buildroot%_man1dir/
#
make CHOWN=/bin/echo DESTDIR=%buildroot install
install -m 644 -D opie.h %buildroot%_includedir/opie.h
install -m 644 -D libopie/libopie.a %buildroot%_libdir/libopie.a
mv %name_pam/README ./README.PAM
# install pam_opie
cd %name_pam
make FAKEROOT=%buildroot \
     SECUREDIR=/%_lib/security install

%files
%dir %_sysconfdir/opielocks
%config(noreplace) %_sysconfdir/opiekeys
%_bindir/*
/%_lib/security/pam_opie.so
#_libdir/libopie.a
%doc BUG-REPORT COPYRIGHT.NRL INSTALL License.TIN README README.PAM
%doc %_mandir/man*/*
%files devel
/%_includedir/opie.h

%changelog
* Fri May 27 2011 Mykola Grechukh <gns@altlinux.ru> 2.4-alt1
- initial build for ALT Linux Sisyphus

* Sun Oct 31 2010 jengelh@medozas.de
- Use %%_smp_mflags
* Mon Dec 14 2009 jengelh@medozas.de
- add baselibs.conf as a source
- enable parallel building
* Sat Oct  3 2009 meissner@suse.de
- fclose permsfile handle bnc#535928
* Wed Jun 24 2009 sbrabec@suse.cz
- Supplement pam-32bit/pam-64bit in baselibs.conf (bnc#354164).
* Tue Jun  2 2009 meissner@suse.de
- rename getline() to telnetgetline() to fix glibc 2.10 build failure.
* Thu Apr 10 2008 ro@suse.de
- added baselibs.conf file to build xxbit packages
  for multilib support
* Thu Mar 29 2007 meissner@suse.de
- buildrequirs bison
* Thu Mar 15 2007 pgajdos@suse.cz
- fixed: 'warning: array subscript is above array bounds' (#252562)
- opie-2.4_array-subscript.patch
- pam_opie-0.21_array-subscript.patch
* Fri Feb  9 2007 meissner@suse.de
- build as nonroot.
* Wed Jan 17 2007 aj@suse.de
- Fix undefined operation.
* Fri Mar 17 2006 okir@suse.de
- Make opie.h C++ safe (#158305)
* Fri Feb 17 2006 okir@suse.de
- Fixed a one byte buffer overflow (#151736)
* Wed Jan 25 2006 mls@suse.de
- converted neededforbuild to BuildRequires
* Thu Jul  7 2005 mmj@suse.de
- add missing declarations
* Thu Feb 24 2005 okir@suse.de
- removed permissions file; it's in %_sysconfdir/permissions anyway (#66318)
- Fixed a single NUL byte overflow
* Mon Jan 24 2005 meissner@suse.de
- 0 -> NULL in execl call.
* Sat Jan 15 2005 schwab@suse.de
- Use <owner>:<group> in permissions file.
* Tue May 18 2004 ro@suse.de
- added -fno-strict-aliasing
- added return value to non-void function (main)
* Mon Dec  2 2002 stark@suse.de
- use RPM_OPT_FLAGS
- link pam_opie against libopie from opie instead of own (older)
  version
* Sat Nov 30 2002 stark@suse.de
- include errno.h for new glibc
* Wed Nov 13 2002 ro@suse.de
- try fix for current bison
* Tue Jul  2 2002 choeger@suse.de
- build with -fPIC on all platforms
- define UINT4 with uint32_t to correctly work on all platforms
  (not just alpha)
* Fri Jun 21 2002 uli@suse.de
- build with -fPIC on x86-64 to be able to link it to shared libs
* Tue Jun 18 2002 choeger@suse.de
- also install libopie.a to use opie with cyrus-sasl2
* Mon Apr  8 2002 stark@suse.de
- moved binaries to /usr/bin
- fixed 'make install' for lib64
* Wed Feb 13 2002 stark@suse.de
- fixed bug in filelist :-(
* Wed Feb 13 2002 stark@suse.de
- minor spec cleanup
* Sun Oct 28 2001 bjacke@suse.de
- make opiekeys (noreplace)
- add file in permissions.d
- use buildroot and do other RPM cleanups
- add missing manpages
* Wed Aug  1 2001 sm@suse.de
- fixed opiepasswd: seed was broken after changing passhprases
* Mon Apr  9 2001 schwab@suse.de
- Fix missing -fPIC.
* Mon Apr  9 2001 ro@suse.de
- don't use macro for version
* Thu Apr  5 2001 us@suse.de
- added patch from krahmer@suse.de
- added opie.h to %_includedir
- added missing binary opiegen
* Wed Mar 28 2001 ro@suse.de
- fixed group entry to: Utilities/Security
* Wed Mar 28 2001 us@suse.de
- changed file permissions of %_sysconfdir/opiekeys to 600
- changed file permissions of /bin/opiepasswd to 4755
- in specfile: added configure flag --enable-insecure-override
* Tue Mar 27 2001 us@suse.de
- new version of opie 2.4
- added pam-module pam_opie 0.21
