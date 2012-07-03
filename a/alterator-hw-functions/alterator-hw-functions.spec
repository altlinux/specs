%define _altdata_dir %_datadir/alterator

Name: alterator-hw-functions
Version: 0.7
Release: alt6

Packager: Stanislav Ievlev <inger@altlinux.org>

BuildArch: noarch

Source1: %name

Summary: helper functions for alterator to retrieve hardware info
License: GPL
Group: System/Base

%description
helper functions for alterator to retrieve hardware info

%install
install -Dpm644 %SOURCE1 %buildroot%_bindir/%name

%files
%_bindir/*

%changelog
* Tue Oct 04 2011 Lenar Shakirov <snejok@altlinux.ru> 0.7-alt6
- first try ifplugstatus, otherwise ethtool:
  * to detect status of cable (closes: #24030)

* Sat Oct 01 2011 Lenar Shakirov <snejok@altlinux.ru> 0.7-alt5
- use ethtool instead of ifplugstatus to detect status of cable (ALT# 24030)

* Wed Sep 14 2011 Mikhail Efremov <sem@altlinux.org> 0.7-alt4
- sort disk_list by name (by Timur Aitov).

* Sat Nov 13 2010 Mikhail Efremov <sem@altlinux.org> 0.7-alt3
- Use /usr/share/misc/*.ids as well as /usr/share/hwdatabase/*.ids.

* Wed Jun 10 2009 Stanislav Ievlev <inger@altlinux.org> 0.7-alt2
- add netdev_read_ip()

* Thu Jun 04 2009 Vladislav Zavjalov <slazav@altlinux.org> 0.7-alt1
- Treat "!" in sysfs as "/" in device names (closes: #20287)

* Wed May 20 2009 Stanislav Ievlev <inger@altlinux.org> 0.6-alt1
- fix partition_uuid() and partition_blkid()
- add fstab_add() and fstab_del()

* Tue May 19 2009 Vladislav Zavjalov <slazav@altlinux.org> 0.5-alt1
- fix blockdev_get_symlink()

* Wed Apr 22 2009 Vladislav Zavjalov <slazav@altlinux.org> 0.4-alt1
- add new functions:
  + partition_id()
  + partition_uuid()
  + partition_fstype()
  + disk_info()

* Wed Apr 22 2009 Vladislav Zavjalov <slazav@altlinux.org> 0.3-alt1
- rewrite block device related functions
- replace netdev_read_info() by no-HAL version
- add support for old sysfs (2.6.18-24 kernels)

* Tue Apr 21 2009 Stanislav Ievlev <inger@altlinux.org> 0.2-alt4
- fix netdev_is_wireless function

* Mon Apr 13 2009 Stanislav Ievlev <inger@altlinux.org> 0.2-alt3
- made netdev_is_up more silent

* Fri Apr 10 2009 Vladislav Zavjalov <slazav@altlinux.org> 0.2-alt2
- fix blockdev_get_symlink()

* Fri Apr 10 2009 Vladislav Zavjalov <slazav@altlinux.org> 0.2-alt1
- add some functions for working with block devices:
  + blockdev_list()
  + blockdev_is_virtual()
  + blockdev_is_removable()
  + blockdev_read_size()
  + partition_list()
  + human_readable_size()
  + blockdev_get_symlink()
  + blockdev_follow_symlink()

* Thu Apr 09 2009 Stanislav Ievlev <inger@altlinux.org> 0.1-alt1
- Initial build

