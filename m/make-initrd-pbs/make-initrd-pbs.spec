%define parent make-initrd
%define child pbs

Name: %parent-%child
Version: 1.0.5
Release: alt1

Summary: This feature is needed to create a file recovery image used by Proxmox backup client
License: GPL-3.0
Group: System/Base
ExclusiveArch: x86_64 aarch64

Source: %name-%version.tar

BuildRequires: proxmox-backup-file-restore
Requires: zfs-utils lvm2
Requires: make-initrd >= 2.2.6
Requires: make-initrd-lvm make-initrd-mdadm make-initrd-luks
Requires: make-initrd-iscsi make-initrd-multipath make-initrd-devmapper

%description
%summary.

%prep
%setup

%install
mkdir -p %buildroot%_datadir/%parent/features
cp -r pbs %buildroot%_datadir/%parent/features

%files
%_datadir/%parent/features/pbs

%changelog
* Tue Nov 05 2024 Alexey Shabalin <shaba@altlinux.org> 1.0.5-alt1
- add lvchange and zfs to PBS_PROGS
- use MODULES_TRY_ADD instead of MODULES_PRELOAD
- add more modules load
- disable preload modules defined in qemu and modules-virtio FEATURES

* Fri May 03 2024 Ivan Pepelyaev <fl0pp5@altlinux.org> 1.0.4-alt1
- v1.0.3 -> v1.0.4

* Fri Oct 13 2023 Ivan Pepelyaev <fl0pp5@altlinux.org> 1.0.3-alt2
- remove ntfs-3g package

* Fri Oct 13 2023 Ivan Pepelyaev <fl0pp5@altlinux.org> 1.0.3-alt1
- v1.0.2 -> v1.0.3

* Thu Oct 12 2023 Ivan Pepelyaev <fl0pp5@altlinux.org> 1.0.2-alt1
- v1.0.1 -> v1.0.2

* Wed Jul 26 2023 Ivan Pepelyaev <fl0pp5@altlinux.org> 1.0.1-alt1
- v1.0.0 -> v1.0.1

* Fri Jul 21 2023 Ivan Pepelyaev <fl0pp5@altlinux.org> 1.0.0-alt1
- Initial build for ALT
