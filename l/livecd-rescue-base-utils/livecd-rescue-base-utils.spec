Name: livecd-rescue-base-utils
Version: 1.0
Release: alt2

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
Requires: jfsprogs
Requires: mtools
Requires: ntfs-3g
Requires: reiser4progs
Requires: reiserfsprogs
Requires: xfsprogs

# Applications/Networking
Requires: cifs-utils
Requires: curl
Requires: davfs2
Requires: rsync
Requires: nfs-utils
Requires: ntpdate
Requires: wget

# Console mouse
Requires: gpm

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

%ifarch x86_64
# UEFI Secure Boot
Requires: pesign
Requires: mokutil
%endif

%description
%summary.

%files

%changelog
* Thu Feb 06 2025 Anton Midyukov <antohami@altlinux.org> 1.0-alt2
- Add dependencies on pesign, mokutil (x86_64 only)

* Wed Feb 05 2025 Anton Midyukov <antohami@altlinux.org> 1.0-alt1
- initial build
