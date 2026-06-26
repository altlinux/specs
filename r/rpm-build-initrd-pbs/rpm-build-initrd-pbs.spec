%define imagedir /usr/libexec/proxmox-backup/file-restore
Name: rpm-build-initrd-pbs
Version: 0.2
Release: alt1

Summary: RPM helper filetrigger for building PBS initrd image
License: GPL
Group: Development/Other
Source: %name-%version.tar

ExclusiveArch: x86_64 aarch64 loongarch64

Requires: make-initrd
Requires: make-initrd-pbs
Requires: /proc

%description
RPM helper filetrigger for building PBS initrd image,
required for file-restore feature

%prep
%setup

%install
install -p -D -m 0644 proxmox-backup-restore-image.mk %buildroot%imagedir/proxmox-backup-restore-image.mk
install -p -D -m 0755 rpm-build-initrd-pbs.filetrigger %buildroot/usr/lib/rpm/rpm-build-initrd-pbs.filetrigger

%files
%dir %imagedir
%config(noreplace) %imagedir/proxmox-backup-restore-image.mk
%_libexecdir/rpm/rpm-build-initrd-pbs.filetrigger

%changelog
* Tue Jun 23 2026 Anton Farygin <rider@altlinux.org> 0.2-alt1
- moved initrd build from %%post to rpm filetrigger

* Tue Feb 03 2026 Sergey Konev <darisishe@altlinux.org> 0.1-alt4
- Update kernel dependencies for branches (FTBS fix)

* Sat Sep 27 2025 Ivan A. Melnikov <iv@altlinux.org> 0.1-alt3
- NMU: build on loongarch64

* Tue Mar 25 2025 Andrey Cherepanov <cas@altlinux.org> 0.1-alt2
- Added support for c10f2 branch.

* Tue Mar 18 2025 Sergey Konev <darisishe@altlinux.org> 0.1-alt1
- Initial build
