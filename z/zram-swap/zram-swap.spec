Name: zram-swap 
Version: 0.2
Release: alt4

Summary: Init and set up swap device in /dev/zram0
License: GPL
Group: System/Configuration/Hardware
BuildArch: noarch

Source: %name.init
Source1: %name.sysconfig


%description
Init and set up swap device in /dev/zram0. Needs kernel module zram.ko
with sysfs interface in 2.6.33 and above

%install
install -D -m755 %SOURCE0 %buildroot%_initdir/%name
install -D -m644 %SOURCE1 %buildroot/etc/sysconfig/%name


%files
%_initdir/%name
/etc/sysconfig/%name

%changelog
* Sun Mar 11 2012 Anton V. Boyarshinov <boyarsh@altlinux.ru> 0.2-alt4
- typos in spec and initscript fixed (thanks to snejok@)

* Mon Nov 28 2011 Anton V. Boyarshinov <boyarsh@altlinux.ru> 0.2-alt3
- typo in zram-swap.sysinit fixed

* Fri May 20 2011 Anton V. Boyarshinov <boyarsh@altlinux.ru> 0.2-alt2
- typo fixed

* Thu May 19 2011 Anton V. Boyarshinov <boyarsh@altlinux.ru> 0.2-alt1
- delay if no device added

* Wed Sep 15 2010 Anton V. Boyarshinov <boyarsh@altlinux.ru> 0.1-alt1
- initial build

