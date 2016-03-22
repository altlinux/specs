Name: live-install
Version: 20160322
Release: alt1
Summary: Copy running system to fixed disk
Group: System/Configuration/Other
License: GPL
BuildArch: noarch

Requires: mdadm cfdisk sfdisk btrfs-progs e2fsprogs rsync grub2-pc syslinux-extlinux

Source: %name-%version.tar.gz

%description
%summary

%prep
%setup -q
%build
%install
install -pD -m 755 %name %buildroot/%_sbindir/%name
install -pD -m 644 dev.cpio.bz2 %buildroot/%_datadir/%name/dev.cpio.bz2
mkdir -p %buildroot/%_datadir/%name/scripts.d

%files
%_sbindir/*
%_datadir/%name
%dir %_datadir/%name/scripts.d

%changelog
* Tue Mar 22 2016 Eugene Prokopiev <enp@altlinux.ru> 20160322-alt1
- audit=0 in kernel cmdline

* Sat Aug 29 2015 Eugene Prokopiev <enp@altlinux.ru> 20150829-alt1
- major improvements:
  + select root device by partition label and autodetect boot devices
  + use only umounted root device (even multi-device btrfs)
  + use grub2 for btrfs and extlinux for ext3/4 (even on md-raid)

* Wed Mar 04 2015 Eugene Prokopiev <enp@altlinux.ru> 20150304-alt1
- do not touch etc/mtab

* Tue Mar 03 2015 Eugene Prokopiev <enp@altlinux.ru> 20140303-alt1
- etc/mtab as symlink and no chkconfig

* Mon Sep 30 2013 Eugene Prokopiev <enp@altlinux.ru> 20130930-alt1
- fix removing live packages again

* Wed Jun 19 2013 Eugene Prokopiev <enp@altlinux.ru> 20130619-alt1
- add option to rename default user

* Mon May 13 2013 Eugene Prokopiev <enp@altlinux.ru> 20130513-alt1
- major improvements implemented by prividen@:
  + use existing mountpoint for system installation
  + install loader on all disks in mdraid array
  + grub2 support

* Mon Apr 15 2013 Eugene Prokopiev <enp@altlinux.ru> 20130415-alt1
- add run directory
- g/lilo/extlinux/g
- cleanup

* Mon Nov 21 2011 Eugene Prokopiev <enp@altlinux.ru> 20111121-alt1
- fix removing obsoleted remount_rw package

* Wed Aug 03 2011 Eugene Prokopiev <enp@altlinux.ru> 20110803-alt2
- fix removing live packages again

* Wed Aug 03 2011 Eugene Prokopiev <enp@altlinux.ru> 20110803-alt1
- fix removing live packages

* Wed Jul 27 2011 Eugene Prokopiev <enp@altlinux.ru> 20110727-alt1
- fix lib64 and installkernel issues

* Tue May 17 2011 Eugene Prokopiev <enp@altlinux.ru> 20110517-alt1
- use installkernel, create empty /cgroup and /selinux

* Thu Apr 07 2011 Eugene Prokopiev <enp@altlinux.ru> 20110407-alt1
- copy existing /home instead of creating it

* Wed Apr 06 2011 Eugene Prokopiev <enp@altlinux.ru> 20110406-alt1
- remove all live packages after install

* Tue Mar 29 2011 Eugene Prokopiev <enp@altlinux.ru> 20110329-alt1
- sync with fakeinstall feature from m-p-l
- add scripts.d

* Sun Feb 06 2011 Michael Pozhidaev <msp@altlinux.ru> 20110206-alt1
- Package was renamed from homeros--install to live-install

* Sun Jan 30 2011 Michael Pozhidaev <msp@altlinux.ru> 20110130-alt1
- Removed altlinux user from installed system
- Enabled sshd and acpid services in installed system

* Fri Jan 28 2011 Michael Pozhidaev <msp@altlinux.ru> 20110128-alt1
- General script update

* Wed Jan 26 2011 Michael Pozhidaev <msp@altlinux.ru> 20110126-alt1
- Initial package

