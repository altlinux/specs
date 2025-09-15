Name: livecd-rescue-base-utils
Version: 1.1
Release: alt5

Summary: Base utils for Live Rescue
License: GPL-2.0-or-later
Group: System/Base

Url: https://www.altlinux.org/Rescue

# Disk utils
Requires: dc3dd
Requires: dcfldd
Requires: ddrescue
Requires: gpart
Requires: hdparm
Requires: lsblk
Requires: lsmount
Requires: lvm2
Requires: nvme
Requires: mdadm
Requires: photorec
Requires: sleuthkit
Requires: smartmontools
Requires: testdisk
Requires: wipefreespace
Requires: whdd

# Partition management
Requires: cfdisk
Requires: cgdisk
Requires: fdisk
Requires: fixparts
Requires: gdisk
Requires: sfdisk
Requires: parted

# Filesystem maintenance
Requires: btrfs-progs
Requires: dosfstools
Requires: e2fsprogs
Requires: exfatprogs
Requires: f2fs-tools
#Requires: jfsprogs
Requires: mtools
Requires: ntfs-3g
#Requires: xfsprogs

# Applications/Networking
Requires: cifs-utils
Requires: curl
Requires: davfs2
Requires: rsync
Requires: nfs-utils
Requires: ntpdate
Requires: wget

# Console mouse
#Requires: gpm

# File management
Requires: mc
Requires: vim-console
Requires: nano

# Provisioning
Requires: partclone

# Misc
Requires: livecd-rescue-utility
Requires: system-backup
Requires: gostsum
Requires: flashrom
Requires: dialog
Requires: usbutils

%ifarch x86_64
# UEFI Secure Boot
Requires: pesign
Requires: mokutil
%endif

%description
%summary.

%files

%changelog
* Mon Sep 15 2025 Anton Midyukov <antohami@altlinux.org> 1.1-alt5
- Add dependency on nvme.

* Tue Jul 01 2025 Anton Midyukov <antohami@altlinux.org> 1.1-alt4
- Add dependency on wipefreespace again.

* Tue Jul 01 2025 Anton Midyukov <antohami@altlinux.org> 1.1-alt3
- Add dependency on usbutils.

* Tue Jul 01 2025 Anton Midyukov <antohami@altlinux.org> 1.1-alt2
- Add dependency on dialog.

* Fri Jun 06 2025 Anton Midyukov <antohami@altlinux.org> 1.1-alt1
- Remove dependencies on wipefreespace, jfsprogs, reiser4progs,
  reiserfsprogs, xfsprogs, gpm

* Thu Feb 06 2025 Anton Midyukov <antohami@altlinux.org> 1.0-alt2
- Add dependencies on pesign, mokutil (x86_64 only)

* Wed Feb 05 2025 Anton Midyukov <antohami@altlinux.org> 1.0-alt1
- initial build
