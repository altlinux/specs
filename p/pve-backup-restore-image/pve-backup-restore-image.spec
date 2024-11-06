# SPDX-License-Identifier: GPL-2.0-or-later
%define _unpackaged_files_terminate_build 1
%define imagedir /usr/libexec/proxmox-backup/file-restore
%define cachedir /var/cache/proxmox-backup

Name: pve-backup-restore-image
Version: 0.5
Release: alt1

Summary: Kernel/initramfs images for Proxmox Backup single file restore
License: GPL-2.0-or-later
Group: Development/Other
Source: %name-%version.tar

ExclusiveArch: x86_64 aarch64

Requires: make-initrd-pbs >= 1.0.5
Requires: thin-provisioning-tools
Requires: proxmox-backup-file-restore
Requires: /proc

Provides: proxmox-backup-restore-image = %EVR

%description
%summary.

%prep
%setup

%install
install -p -D -m 0644 pve-backup-restore-image.mk %buildroot%imagedir/%name.mk
install -p -D -m 0755 pve-backup-restore-image.sh %buildroot%imagedir/%name.sh
install -p -D -m 0755 pve-backup-restore-image.filetrigger %buildroot%_rpmlibdir/%name.filetrigger

%files
%dir %imagedir
%config(noreplace) %imagedir/%name.mk
%imagedir/%name.sh
%_rpmlibdir/%name.filetrigger
#%%ghost %%imagedir/bzImage
#%%ghost %%imagedir/initramfs.img

%changelog
* Wed Nov 06 2024 Alexey Shabalin <shaba@altlinux.org> 0.5-alt1
- update filetrigger: update initramfs on self update

* Tue Nov 05 2024 Alexey Shabalin <shaba@altlinux.org> 0.4-alt1
- add rpm filetrigger
- move load ntfs module to make-initrd-pbs = 1.0.5
- not requires kernel package

* Fri Oct 13 2023 Andrew A. Vasilyev <andy@altlinux.org> 0.3-alt1
- fix NTFS restore (only for kernels 5.15+)

* Thu Oct 12 2023 Andrew A. Vasilyev <andy@altlinux.org> 0.2-alt1
- add Provides for proxmox-backup-restore-image

* Fri Jul 21 2023 Andrew A. Vasilyev <andy@altlinux.org> 0.1-alt1
- Initial release.

