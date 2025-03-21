%define _unpackaged_files_terminate_build 1
%define imagedir /usr/libexec/proxmox-backup/file-restore
%define cachedir /var/cache/proxmox-backup

Name: proxmox-backup-restore-image
Version: 3.3.3.1
Release: alt1

Summary: Kernel/initramfs images for Proxmox Backup single file restore
License: GPL-2.0-or-later
Group: Development/Other

ExclusiveArch: x86_64 aarch64

Obsoletes: pve-backup-restore-image

BuildPreReq: rpm-build-initrd-pbs
BuildPreReq: proxmox-backup-restore-daemon = %version

%description
%summary.

%install
install -p -D -m 0644 %imagedir/bzImage %buildroot%imagedir/bzImage
install -p -D -m 0644 %imagedir/initramfs.img %buildroot%cachedir/file-restore-initramfs.img

%files
%imagedir/bzImage
%cachedir/file-restore-initramfs.img

%changelog
* Wed Mar 19 2025 Sergey Konev <darisishe@altlinux.org> 3.3.3.1-alt1
- Initial build

