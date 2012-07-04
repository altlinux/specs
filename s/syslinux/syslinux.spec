Name: syslinux
Version: 4.04
Release: alt3
Serial: 2

Summary: Simple kernel loader which boots from a FAT filesystem
License: GPL
Group: System/Kernel and hardware
Url: http://syslinux.zytor.com/

Requires: mtools

Source0: %name-%version.tar.bz2
Source1: isolinux-config
Source2: README.gfxboot
# SuSE
Patch1: syslinux-4.04-cwd.diff
Patch2: syslinux-4.04-iso9660.diff
Patch3: syslinux-4.04-isohybrid-hex-option-parsing.diff
Patch4: syslinux-4.04-mboot_bootif.diff
Patch5: syslinux-4.04-md5pass.diff
Patch6: syslinux-4.04-noinitrd.diff
# ALT
Patch100: syslinux-4.04-alt-ext2fs-header.patch

#BuildPrereq: nasm perl-base
# Automatically added by buildreq on Tue Oct 28 2008 (-bi)
BuildRequires: nasm perl-Crypt-PasswdMD5 perl-Digest-SHA1 libe2fs-devel
#linux-libc-headers

%description
Syslinux is a simple kernel loader. It normally loads the kernel (and an 
optional initrd image) from a FAT filesystem. It can also be used as a
PXE bootloader during network boots.

%package extlinux
Group: System/Kernel and hardware
Summary: The EXTLINUX bootloader, for booting the local system.
Requires: %name = %serial:%version-%release
%description extlinux
The EXTLINUX bootloader, for booting the local system, as well as all
the SYSLINUX/PXELINUX modules in /boot.

%package tftpboot
Group: System/Kernel and hardware
Summary: SYSLINUX modules in /tftpboot, available for network booting
Requires: %name = %serial:%version-%release
%description tftpboot
All the SYSLINUX/PXELINUX modules directly available for network
booting in the /tftpboot directory.

%package devel
Summary: Simple kernel loader which boots from a FAT filesystem, devel path
Group: System/Kernel and hardware
Requires: %name = %serial:%version

%description devel
Read main packages description 

%prep
%setup -q
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1
%patch100 -p1
install -m 0644 %SOURCE2 .

%build
export CFLAGS="%optflags"
%make_build CC="gcc -fno-stack-protector" spotless
%make_build CC="gcc -fno-stack-protector"
#make_build spotless
#make_build


%install
%make \
	INSTALLDIR=%buildroot \
	INSTALLROOT=%buildroot \
	BINDIR=%_bindir \
	SBINDIR=%_bindir \
	DATADIR=%_libexecdir \
	INCDIR=%_includedir \
	MANDIR=%_mandir \
	EXTLINUXDIR=/boot/extlinux \
	install-all
#	TFTPBOOT=/tftpboot \

rm -rf %buildroot/tftpboot
rm -rf %buildroot/%_libexecdir/%name/com32

mkdir -p %_sysconfdir
#ln -s `relative /boot/extlinux/extlinux.conf %_sysconfdir/extlinux.conf` %buildroot/%_sysconfdir/extlinux.conf

for f in ldlinux.sys ldlinux.bss
do
    install -m 0644 core/$f %buildroot/%_libexecdir/%name/
done

install -m 0755 %SOURCE1 %buildroot/%_bindir


%files
%doc NEWS README* doc/* sample/sample.*
%_bindir/*
%exclude %_bindir/extlinux
%dir %_libexecdir/%name/
%_libexecdir/%name/*
%_man1dir/*.1.*

%files extlinux
%_bindir/extlinux
/boot/extlinux

%changelog
* Wed Jul 04 2012 Sergey V Turchin <zerg@altlinux.org> 2:4.04-alt3
- package extlinux separately

* Mon May 14 2012 Sergey V Turchin <zerg@altlinux.org> 2:4.04-alt2
- use external ext2_fs.h from libe2fs

* Mon Apr 23 2012 Sergey V Turchin <zerg@altlinux.org> 2:4.04-alt1
- new version

* Fri Jul 08 2011 Sergey V Turchin <zerg@altlinux.org> 2:3.86-alt6
- package ldlinux.bss (ALT#23543)

* Mon Jul 04 2011 Sergey V Turchin <zerg@altlinux.org> 2:3.86-alt5
- fix boot from local disk

* Wed Jun 15 2011 Michael Shigorin <mike@altlinux.org> 2:3.86-alt4
- backported/extended vesa-related fix from hdt-0.4.1:
  hdt-0.3.6 would drop to CLI if UI was gfxboot/vesa
  (and would erroneously take "automatic=" for "auto")

* Wed May 25 2011 Sergey V Turchin <zerg@altlinux.org> 2:3.86-alt3
- new version
- don't apply gfxboot-media-type.patch

* Tue May 24 2011 Michael Shigorin <mike@altlinux.org> 2:3.82-alt6.1
- added whichsys.c32 (closes: #25663)

* Mon May 31 2010 Sergey V Turchin <zerg@altlinux.org> 2:3.82-alt6
- fix detect media type for gfxboot; thanks boyarsh@alt

* Fri May 28 2010 Sergey V Turchin <zerg@altlinux.org> 2:3.82-alt5
- revert to 3.82

* Thu May 27 2010 Sergey V Turchin <zerg@altlinux.org> 1:3.86-alt2
- fix detect media type for gfxboot; thanks boyarsh@alt

* Thu May 20 2010 Sergey V Turchin <zerg@altlinux.org> 1:3.86-alt1
- see README.gfxboot (ALT#23502)

* Fri Aug 14 2009 Sergey V Turchin <zerg@altlinux.org> 1:3.63-alt4
- revert from 3.82

* Wed Apr 29 2009 Sergey V Turchin <zerg@altlinux.org> 3.63-alt3
- package ldlinux.sys (ALT#18588)
- update gfx patch (allow leave a20 untouched when hold SHIFT at boot)

* Sun Jan 11 2009 Sergey V Turchin <zerg at altlinux dot org> 3.63-alt2
- add mtools to requires

* Tue Oct 28 2008 Sergey V Turchin <zerg at altlinux dot org> 3.63-alt1
- new version

* Tue Aug 14 2007 Sergey V Turchin <zerg at altlinux dot org> 3.36-alt2
- fix %%license, %%url

* Tue Feb 13 2007 Sergey V Turchin <zerg at altlinux dot org> 3.36-alt1
- new version

* Wed Jan 31 2007 Sergey V Turchin <zerg at altlinux dot org> 3.35-alt1
- new version

* Wed Dec 13 2006 Sergey V Turchin <zerg at altlinux dot org> 3.31-alt1
- new version
- update gfx patch from SUSE 

* Tue May 23 2006 Andriy Stepanov <stanv@altlinux.ru> 3.11-alt1
- new version

* Mon Jul 04 2005 Anton D. Kachalov <mouse@altlinux.org> 2.11-alt2
- multilib support

* Sun Dec 05 2004 Anton Farygin <rider@altlinux.ru> 2.11-alt1
- new version, updated gfx patch from SUSE

* Thu Nov 27 2003 Grigory Milev <week@altlinux.ru> 2.06-alt1
- new version released
- added gfx patch from SUSE 

* Mon Aug 18 2003 Grigory Milev <week@altlinux.ru> 2.05-alt1
- new version released

* Fri Nov 29 2002 Grigory Milev <week@altlinux.ru> 2.00-alt1
- new version released

* Wed Oct  2 2002 Grigory Milev <week@altlinux.ru> 1.76-alt1
- new version released

* Wed Oct  2 2002 Grigory Milev <week@altlinux.ru> 1.52-alt1
- ALT Linux adaptation

* Tue Jan 29 2002 Sergey Bolshakov <s.bolshakov@belcaf.com> 1.52-1aw
- AW adaptations

* Sat Feb 10 2001 Matt Wilson <msw@redhat.com>
- 1.52

* Wed Jan 24 2001 Matt Wilson <msw@redhat.com>
- 1.51pre7

* Mon Jan 22 2001 Matt Wilson <msw@redhat.com>
- 1.51pre5

* Fri Jan 19 2001 Matt Wilson <msw@redhat.com>
- 1.51pre3, with e820 detection

* Tue Dec 12 2000 Than Ngo <than@redhat.com>
- rebuilt with fixed fileutils

* Thu Nov 9 2000 Than Ngo <than@redhat.com>
- update to 1.49
- update ftp site
- clean up specfile
- add some useful documents

* Tue Jul 18 2000 Nalin Dahyabhai <nalin@redhat.com>
- add %%defattr (release 4)

* Wed Jul 12 2000 Prospector <bugzilla@redhat.com>
- automatic rebuild

* Thu Jul 06 2000 Trond Eivind Glomsrød <teg@redhat.com>
- use %%{_tmppath}
- change application group (Applications/Internet doesn't seem
  right to me)
- added BuildRequires

* Tue Apr 04 2000 Erik Troan <ewt@redhat.com>
- initial packaging
