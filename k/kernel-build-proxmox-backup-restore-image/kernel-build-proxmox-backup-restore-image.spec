%define _unpackaged_files_terminate_build 1
%define imagedir /usr/libexec/proxmox-backup/file-restore
%define cachedir /var/cache/proxmox-backup

%ifdef _priority_distbranch
%define altbranch %_priority_distbranch
%else
%define altbranch %(rpm --eval %%_priority_distbranch)
%endif
%if "%altbranch" == "%nil"
%define altbranch sisyphus
%endif

%define flavour 6.18
# select kernel flavour based on branch
%if "%altbranch" == "p10"
# Force un-def kernel flavour
%define flavour un-def
%else if "%altbranch" == "p11" || "%altbranch" == "c10f2"
%define flavour 6.12
%endif

Name: kernel-build-proxmox-backup-restore-image
Version: 4.2.0.1
Release: alt2

Summary: Kernel/initramfs images for Proxmox Backup single file restore
License: GPL-2.0-or-later
Group: Development/Other

ExclusiveArch: x86_64 aarch64 loongarch64

BuildPreReq: rpm-build-initrd-pbs
BuildPreReq: proxmox-backup-restore-daemon = %version
BuildPreReq: kernel-image-%flavour
BuildPreReq: kernel-modules-zfs-%flavour


%description
%summary.

%package -n proxmox-backup-restore-image
Summary: %summary
Group: Development/Other
Obsoletes: pve-backup-restore-image

%description -n proxmox-backup-restore-image
%summary.

%install
install -p -D -m 0644 %imagedir/bzImage %buildroot%imagedir/bzImage
install -p -D -m 0644 %imagedir/initramfs.img %buildroot%cachedir/file-restore-initramfs.img

%files -n proxmox-backup-restore-image
%imagedir/bzImage
%cachedir/file-restore-initramfs.img

%changelog
* Tue Jun 23 2026 Anton Farygin <rider@altlinux.org> 4.2.0.1-alt2
- Renamed source package to kernel-build-proxmox-backup-restore-image;
  binary package proxmox-backup-restore-image is now a subpackage.
- Select kernel flavour by distribution branch: un-def for p10,
  6.12 for p11 and c10f2, 6.18 otherwise.
- Added explicit kernel-image and kernel-modules-zfs build dependencies.

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

