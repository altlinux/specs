Name: lphdisk
Version: 0.9.1
Release: alt6

Summary: Utility for formatting Phoenix NoteBIOS hibernation partitions under Linux
License: Artistic License
Group: System/Base

Url: http://www.procyon.com/~pda/lphdisk
Source: %url/%name-%version.tar.gz
Patch0: lphdisk-0.9.1-alt-lrmi.patch
Patch1: lphdisk-0.9.1-debian-syscall-llseek.diff
Packager: Michael Shigorin <mike@altlinux.ru>

ExclusiveArch: %ix86

%description
lphdisk is a Linux reimplementation of the PHDISK.EXE (DOS) utility provided
with most Phoenix NoteBIOS-equipped laptop models.  It will properly format a
NoteBIOS hibernation partition (type A0) to make it usable by the BIOS for
suspending to disk, avoiding the need to use buggy and outdated DOS utilities
to perform this configuration step.

%prep
%setup -q
%patch0 -p1 -b .lrmi
%patch1 -p1 -b .llseek

%build
%make

%install
install -pD -m755 %name %buildroot%_sbindir/%name
install -pD -m644 %name.8 %buildroot%_man8dir/%name.8

%files
%doc ChangeLog CREDITS NEWS README TODO
%_sbindir/*
%_man8dir/*

%changelog
* Sat Sep 27 2008 Michael Shigorin <mike@altlinux.org> 0.9.1-alt6
- build fix: backported lrmi patch by led to included one
  (forward porting the code to current libvbe is a bit beyond me)
- removed gentoo patch superseded by debian's one

* Sat Mar 22 2008 Michael Shigorin <mike@altlinux.org> 0.9.1-alt5
- applied Debian patch to fix FTBFS with current kernel headers
  and also resolve large filesystem related issue (from 0.9.1-3);
  thanks Kirill Shutemov (kas@) for a hint
- removed Gentoo gcc33 patch (superceded)

* Tue Jun 20 2006 Michael Shigorin <mike@altlinux.org> 0.9.1-alt4
- added ExclusiveArch since APM BIOS with suspend-to-disk 
  seems to not exist on x86_64 notebooks (corrections welcome)

* Mon Mar 20 2006 Michael Shigorin <mike@altlinux.org> 0.9.1-alt3
- added gcc33 patch from 0.9.1-0 package by Dag Wieers <dag/wieers.com>

* Mon May 30 2005 Michael Shigorin <mike@altlinux.ru> 0.9.1-alt2
- rebuilt for Sisyphus
- spec cleanup

* Fri Jul 09 2004 Michael Shigorin <mike@altlinux.ru> 0.9.1-alt1
- built for ALT Linux

* Tue Feb 12 2002 Alex Stewart <alex@foogod.com>
- Updated to version 0.9.1

* Thu Aug 23 2001 Patrick D. Ashmore <pda@procyon.com>
- Updated version information in spec file (0.4as1 to 0.9)

* Sun Jul 15 2001 Alex Stewart <alex@foogod.com>
- Initial RPM packaging of lphdisk 0.4as1
