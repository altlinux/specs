Name: mkbootflash
Version: 0.19
Release: alt5

Summary: Make bootable USB storage
License: GPL
Group: System/Configuration/Other
Url: http://www.altlinux.org/Bootflash/mkbootflash

Source: %name.tar

BuildArch: noarch
Requires: rsync syslinux sfdisk

Packager: Anton V. Boyarshinov <boyarsh@altlinux.ru>

%description
Make bootable USB storage for network installation, rescue or live from installation DVD

%prep
%setup -c

%install
mkdir -p %buildroot/usr/sbin
install -pD -m0755 mkbootflash/mkbootflash %buildroot%_sbindir/mkbootflash

%files
%_sbindir/mkbootflash

%changelog
* Tue Jan 25 2011 Lenar Shakirov <snejok@altlinux.ru> 0.19-alt5
- remove ldlinux.sys from $mpoint: mcopy ask for overwrite

* Tue Jan 25 2011 Lenar Shakirov <snejok@altlinux.ru> 0.19-alt4
- handling of $workdir removed

* Mon Jan 24 2011 Lenar Shakirov <snejok@altlinux.ru> 0.19-alt3
- Url added to spec

* Mon Jan 24 2011 Lenar Shakirov <snejok@altlinux.ru> 0.19-alt2
- unnecessary requires removed

* Mon Jan 24 2011 Lenar Shakirov <snejok@altlinux.ru> 0.19-alt1
- make script shell compatible
- fix small errors and typo
- .gear-rules -> .gear/rules
- spec cleaned: thanks to rpmcs!

* Thu Dec 16 2010 Anton Farygin <rider@altlinux.ru> 0.18-alt1
- increased ramdisk size to 128000Kb

* Thu Nov 12 2009 Anton V. Boyarshinov <boyarsh@altlinux.ru> 0.17-alt1
- fixed block device detection (closes #21707)

* Tue Sep 29 2009 Anton V. Boyarshinov <boyarsh@altlinux.ru> 0.16-alt1
- ALTLinux/base copying added (closes 21714)

* Thu Sep 03 2009 Anton V. Boyarshinov <boyarsh@altlinux.ru> 0.15-alt1
- enlarged ramdisk size

* Tue Jun 30 2009 Anton V. Boyarshinov <boyarsh@altlinux.ru> 0.14-alt1
- added CDROM umounting (closes #20606)

* Wed Jun 03 2009 Anton V. Boyarshinov <boyarsh@altlinux.ru> 0.13-alt1
- changed RPMS.base to RPMS.main according to 5.0 filestructure

* Sat Nov 01 2008 Anton V. Boyarshinov <boyarsh@altlinux.ru> 0.12-alt2.M41.1
- port to M41

* Sat Nov 01 2008 Anton V. Boyarshinov <boyarsh@altlinux.ru> 0.12-alt3
- fixed syslinux.cfg generation for rescue

* Wed Oct 08 2008 Anton V. Boyarshinov <boyarsh@altlinux.ru> 0.12-alt2
- fixed syslinux.cfg generation for rescue and live

* Thu Sep 25 2008 Anton V. Boyarshinov <boyarsh@altlinux.ru> 0.12-alt0.M41.1
- port to M41

* Thu Sep 25 2008 Anton V. Boyarshinov <boyarsh@altlinux.ru> 0.12-alt1
- fixed syslinux run

* Tue Sep 16 2008 Anton V. Boyarshinov <boyarsh@altlinux.ru> 0.11-alt2
- fixed bug in mount_options using

* Mon Sep 15 2008 Anton V. Boyarshinov <boyarsh@altlinux.ru> 0.11-alt1
- make it usable in 4.1 Desktop environment

* Wed Aug 20 2008 Anton V. Boyarshinov <boyarsh@altlinux.ru> 0.10-alt1
- copyng ALTLinux/RPMS.base for install

* Mon Dec 24 2007 Anton V. Boyarshinov <boyarsh@altlinux.ru> 0.9-alt1
- copyng MBR, making partition active

* Thu Sep 27 2007 Anton V. Boyarshinov <boyarsh@altlinux.ru> 0.8-alt1
- fixed bugs appears in 4.0 Desktop envireoment

* Fri Aug 10 2007 Anton V. Boyarshinov <boyarsh@altlinux.ru> 0.7-alt1
- writable etc/bin/usr/var
- gfxboot & bootsplash support added

* Thu Aug 09 2007 Anton V. Boyarshinov <boyarsh@altlinux.ru> 0.6-alt1
- added not overwriting existing hoem image

* Wed Aug 08 2007 Anton V. Boyarshinov <boyarsh@altlinux.ru> 0.5-alt1
- added making initrd from squashfs image

* Tue Aug 07 2007 Anton V. Boyarshinov <boyarsh@altlinux.ru> 0.4-alt1
- added parameter to set kernel release

* Mon Aug 06 2007 Anton V. Boyarshinov <boyarsh@altlinux.ru> 0.3-alt1
- added support for nonpartitioned flash

* Mon Aug 06 2007 Anton V. Boyarshinov <boyarsh@altlinux.ru> 0.2-alt1
- added requires on mtools
- added some errors handling

* Fri Aug 03 2007 Anton V. Boyarshinov <boyarsh@altlinux.ru> 0.1-alt1
- first build

