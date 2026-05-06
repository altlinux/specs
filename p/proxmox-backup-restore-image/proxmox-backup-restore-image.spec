%define _unpackaged_files_terminate_build 1
%define imagedir /usr/libexec/proxmox-backup/file-restore
%define cachedir /var/cache/proxmox-backup

Name: proxmox-backup-restore-image
Version: 4.2.0.1
Release: alt1

Summary: Kernel/initramfs images for Proxmox Backup single file restore
License: GPL-2.0-or-later
Group: Development/Other

ExclusiveArch: x86_64 aarch64 loongarch64

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
* Wed May 06 2026 Sergey Konev <darisishe@altlinux.org> 4.2.0.1-alt1
- 4.2.0-1

* Thu Feb 05 2026 Sergey Konev <darisishe@altlinux.org> 4.0.14.1-alt2
- Rebuild with ntfs-3g as ntfs3 fallback

* Mon Aug 18 2025 Sergey Konev <darisishe@altlinux.org> 4.0.14.1-alt1
- 4.0.14-1

* Thu Jun 12 2025 Ivan A. Melnikov <iv@altlinux.org> 3.3.3.1-alt2
- NMU: build on loongarch64

* Wed Mar 19 2025 Sergey Konev <darisishe@altlinux.org> 3.3.3.1-alt1
- Initial build

