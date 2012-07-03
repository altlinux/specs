Name: syskeeper
Summary: %name
Version: 0.8
Release: alt1
License: GPL
Group: System/Base
BuildArch: noarch
Url: http://sisyphus.ru/ru/srpm/Sisyphus/syskeeper
Packager: Denis Smirnov <mithraen@altlinux.ru>
Requires(pre): etckeeper
Requires: %name-base = %version-%release
Source: %name-%version.tar

%package -n kernelbootlog
Summary: Automaticaly backup some system info when booting
Group: System/Base
BuildArch: noarch

%description -n kernelbootlog
Automaticaly backup some system info when booting

%package base
Summary: Base files for syskeeper
Group: System/Base
Requires: crontabs

%description base
Base files for syskeeper

%package base-git
Summary: git support for syskeeper
Group: System/Base
Requires: %name-base = %version-%release
Requires: perl-Git

%description base-git
git support for syskeeper

%package disks
Summary: Autobackup storage information
Group: System/Base
Requires: %name = %version-%release
Requires: %name-base = %version-%release

%description disks
Autobackup storage information
- fstab
- blkid
- disks partitioning
- LVM information


%package disks-git
Summary: Autobackup storage information
Group: System/Base
Requires: %name-disks = %version-%release

%description disks-git
Autobackup storage information
- fstab
- blkid
- disks partitioning
- LVM information


%package hn
Summary: Autobackup system info (use it for HN)
Group: System/Base
Requires: %name-ve = %version-%release
Requires: %name-disks-git = %version-%release
Requires: %name-system-git = %version-%release
Requires: kernelbootlog

%description hn
Autobackup system info (use it for HN)

%package rpm
Summary: Autobackup installed packages list
Group: System/Base
Requires: %name-base = %version-%release

%description rpm
Autobackup installed packages list

%package rpm-git
Summary: Autobackup installed packages list
Group: System/Base
Requires: %name-rpm = %version-%release

%description rpm-git
Autobackup installed packages list

%package system
Summary: Autobackup system information
Group: System/Base
Requires: %name = %version-%release
Requires: %name-base = %version-%release

%description system
Autobackup system information
- CPU
- DMI


%package system-git
Summary: Autobackup system information
Group: System/Base
Requires: %name-disks = %version-%release

%description system-git
Autobackup system information
- CPU
- DMI


%package ve
Summary: Autobackup system info (use it for VE)
Group: System/Base
Requires: %name = %version-%release
Requires: %name-rpm-git = %version-%release

%description ve
Autobackup system info (use it for VE)


%description
%name


%prep
%setup -c

%install
%makeinstall_std
mkdir -p %buildroot%_initdir/
install -p kernelbootlog %buildroot%_initdir/kernelbootlog
mkdir -p %buildroot/var/log/kernelbootlog

%preun -n kernelbootlog
%preun_service kernelbootlog

%post -n kernelbootlog
%post_service kernelbootlog

%files
%_sysconfdir/apt/apt.conf.d/syskeeper.conf
%_sbindir/syskeeper
%_sysconfdir/firsttime.d/%name

%files -n kernelbootlog
%_initdir/kernelbootlog
/var/log/kernelbootlog

%files base
%dir %_datadir/syskeeper
%_datadir/syskeeper/functions
%_sysconfdir/cron.daily/syskeeper
%dir %attr(0750,root,wheel) /var/lib/syskeeper

%files base-git
%_datadir/syskeeper/functions-git

%files disks
%_datadir/syskeeper/backup_disk

%files disks-git
%_datadir/syskeeper/backup_disk_git

%files hn

%files rpm
%_datadir/syskeeper/backup_rpm
%_datadir/syskeeper/optimize_package_list

%files rpm-git
%_datadir/syskeeper/backup_rpm_git

%files system
%_datadir/syskeeper/backup_system

%files system-git
%_datadir/syskeeper/backup_system_git

%files ve

%changelog
* Tue Jul 03 2012 Denis Smirnov <mithraen@altlinux.ru> 0.8-alt1
- update backup_disk

* Thu Feb 09 2012 Denis Smirnov <mithraen@altlinux.ru> 0.7-alt1
- ignore zram devices

* Sat May 15 2010 Denis Smirnov <mithraen@altlinux.ru> 0.6-alt1
- work _fast_ when used from apt
- add cpu and dmi info backup

* Tue Nov 03 2009 Denis Smirnov <mithraen@altlinux.ru> 0.5-alt2
- fix requires

* Sat Oct 31 2009 Denis Smirnov <mithraen@altlinux.ru> 0.5-alt1
- don't try backup partition tables on md* devices (ALT#20982)

* Sun Oct 11 2009 Denis Smirnov <mithraen@altlinux.ru> 0.4-alt1
- fix syskeeper main script

* Tue Oct 06 2009 Denis Smirnov <mithraen@altlinux.ru> 0.3-alt3
- fix typo

* Tue Oct 06 2009 Denis Smirnov <mithraen@altlinux.ru> 0.3-alt2
- fix kernelbootlog packaging

* Tue Oct 06 2009 Denis Smirnov <mithraen@altlinux.ru> 0.3-alt1
- import kernelbootlog

* Sun Oct 04 2009 Denis Smirnov <mithraen@altlinux.ru> 0.0.14-alt4
- fix typo

* Sun Oct 04 2009 Denis Smirnov <mithraen@altlinux.ru> 0.0.14-alt3
- code cleanup
- separate syskeeper-rpm package
- separate git support for syskeeper

* Mon Sep 28 2009 Denis Smirnov <mithraen@altlinux.ru> 0.0.13-alt3
- spec refactoring

* Mon Sep 28 2009 Denis Smirnov <mithraen@altlinux.ru> 0.0.13-alt2
- add Url tag

* Thu Sep 24 2009 Denis Smirnov <mithraen@altlinux.ru> 0.0.13-alt1
- fix HP Smart Array Controller compatibiltiy

* Thu Apr 23 2009 Denis Smirnov <mithraen@altlinux.ru> 0.0.12-alt1
- initialize syskeeper in firsttime.d, instead of post section

* Thu Apr 23 2009 Denis Smirnov <mithraen@altlinux.ru> 0.0.11-alt1
- use sfdisk for partitioning backup

* Thu Apr 23 2009 Denis Smirnov <mithraen@altlinux.ru> 0.0.10-alt1
- create etckeeper repo in postin silently

* Sun Dec 14 2008 Denis Smirnov <mithraen@altlinux.ru> 0.0.9-alt1
- fix typo in backup_disk

* Sat Dec 13 2008 Denis Smirnov <mithraen@altlinux.ru> 0.0.8-alt1
- ignore loop devices when backup data from disk storages

* Tue Nov 11 2008 Denis Smirnov <mithraen@altlinux.ru> 0.0.7-alt1
- fix git >= 1.6.0 compatibility

* Sun Aug 31 2008 Denis Smirnov <mithraen@altlinux.ru> 0.0.6-alt1
- suppress error output from LVM utilites
- not try to create git repo if it already exists
- set LANG to 'POSIX' (for correct lvm utils output)

* Sun Aug 24 2008 Denis Smirnov <mithraen@altlinux.ru> 0.0.5-alt1
- set return code to 0
- create directory for disk partitioning backup from backup_disk module
- add requires to kernelbootlog for syskeeper-hn

* Sat Aug 23 2008 Denis Smirnov <mithraen@altlinux.ru> 0.0.4-alt1
- split to subpackages (disk partitioning backup not needed in VEs)

* Sat Aug 23 2008 Denis Smirnov <mithraen@altlinux.ru> 0.0.3-alt1
- init etckeeper after install

* Sat Aug 23 2008 Denis Smirnov <mithraen@altlinux.ru> 0.0.2-alt1
- copy optimize_package_list from rpm-utils (syskeeper must not requires
  rpm-build)

* Sat Aug 23 2008 Denis Smirnov <mithraen@altlinux.ru> 0.0.1-alt1
- first build

