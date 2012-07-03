Name: spt-profiles-junior-school
Version: 0.4
Release: alt7

Summary: spt profiles for building junior
Group: Development/Other
License: GPL

Source: %name-%version-%release.tar.bz2
BuildArch: noarch

AutoReq: yes, noshell

%description
This package contains spt profiles for building junior.

%prep
%setup

%install
mkdir -p %buildroot/etc/spt/profiles/junior-school
for d in base cd cdx dvd4; do
	cp -a "$d" %buildroot/etc/spt/profiles/junior-school
done

%files
%config(noreplace) /etc/spt/profiles/*

%changelog
* Fri Apr 25 2008 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.4-alt7
- all qt sql drivers added to package lists (#14538)

* Fri Apr 11 2008 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.4-alt6
- prepared for use with udev-aware installer's 1st stage
- package lists rearranged again

* Mon Feb  4 2008 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.4-alt5
- renamed profile to junior-school

* Mon Dec 24 2007 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.4-alt4
- RC4 released

* Mon Dec 17 2007 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.4-alt3
- RC3 released

* Fri Dec 14 2007 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.4-alt2
- RC2 released

* Fri Dec 14 2007 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.4-alt1
- RC1 released

* Mon Dec  3 2007 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.3-alt2
- beta2 released

* Mon Nov 12 2007 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.3-alt1
- first beta release

* Wed Sep 12 2007 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.2-alt2
- cleaned up

* Tue Jul 31 2007 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.2-alt1
- used for junior

* Thu Jul 26 2007 Anton V. Boyarshinov <boyarsh@altlinux.ru> 0.2-alt1
- noload=ahci, documentation 

* Thu Jul 19 2007 Anton V. Boyarshinov <boyarsh@altlinux.ru> 0.1-alt10
- progressbar in installation enabled
- clock not in UTC

* Thu Jul 12 2007 Anton V. Boyarshinov <boyarsh@altlinux.ru> 0.1-alt9
- many changes :( 

* Wed Jun 06 2007 Anton V. Boyarshinov <boyarsh@altlinux.ru> 0.1-alt8
- packages changes, livecd video setup changed 

* Tue May 29 2007 Anton V. Boyarshinov <boyarsh@altlinux.ru> 0.1-alt7
- added bootsplash animation
- russian by default in gfxboot

* Thu May 24 2007 Anton V. Boyarshinov <boyarsh@altlinux.ru> 0.1-alt6
- fixed livecd profile
- added intel firmware

* Mon May 21 2007 Anton V. Boyarshinov <boyarsh@altlinux.ru> 0.1-alt5
- bootsplash added 

* Wed May 16 2007 Anton V. Boyarshinov <boyarsh@altlinux.ru> 0.1-alt4
- added hooks into livecd
- packages changes

* Mon May 07 2007 Anton V. Boyarshinov <boyarsh@altlinux.ru> 0.1-alt3
- added LiveCD profile
- added consolehelper

* Fri May 04 2007 Anton V. Boyarshinov <boyarsh@altlinux.ru> 0.1-alt2
- build fixed 

* Thu May 03 2007 Anton V. Boyarshinov <boyarsh@altlinux.ru> 0.1-alt1
- Initial version 
