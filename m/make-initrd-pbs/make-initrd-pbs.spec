%define parent make-initrd
%define child pbs

Name: %parent-%child
Version: 1.0.0
Release: alt1

Summary: This feature is needed to create a file recovery image used by proxmox
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
* Fri Jul 21 2023 Ivan Pepelyaev <fl0pp5@altlinux.org> 1.0.0-alt1
- Initial build for ALT
