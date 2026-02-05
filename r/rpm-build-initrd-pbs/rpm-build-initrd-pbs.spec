%define imagedir /usr/libexec/proxmox-backup/file-restore

%ifdef _priority_distbranch
%define altbranch %_priority_distbranch
%else
%define altbranch %(rpm --eval %%_priority_distbranch)
%endif
%if "%altbranch" == "%nil"
%define altbranch sisyphus
%endif

Name: rpm-build-initrd-pbs
Version: 0.1
Release: alt4

Summary: RPM helper post script for building PBS initrd image
License: GPL
Group: Development/Other
Source: %name-%version.tar

ExclusiveArch: x86_64 aarch64 loongarch64

Requires(pre): make-initrd
Requires(pre): make-initrd-pbs
Requires(pre): /proc

%if "%altbranch" == "p10"
Requires(pre): kernel >= 6.1
# Force un-def kernel flavour (no ZFS for 6.12 in p10)
Conflicts: kernel >= 6.2
%elif "%altbranch" == "p11" || "%altbranch" == "c10f2"
Requires(pre): kernel >= 6.12
# There's no zfs module for 6.14 kernel
Conflicts: kernel >= 6.13
%else
# Sisyphus
Requires(pre): kernel >= 6.18
# Force strict version
Conflicts: kernel >= 6.19
%endif

Requires(pre): zfs-kernel-module


%description
RPM helper post script for building PBS initrd image,
required for file-restore feature

%prep
%setup

%install
install -p -D -m 0644 proxmox-backup-restore-image.mk %buildroot%imagedir/proxmox-backup-restore-image.mk

%post
mkdir -p %imagedir

# Filter out bad kernel flavours in case they were installed (may happen during install-check)
VMLINUZ=$(ls -1 /boot/vmlinuz-*alt* 2>/dev/null | grep -vE "(rocknix|pine|rpi|sunxi|repka|rk|mp|rt|talos)" | head -n 1)
KVER="${VMLINUZ##*/vmlinuz-}"
echo "VMLINUZ = $VMLINUZ"
echo "KVER = $KVER"
rm -f "%imagedir/initramfs.img"

make-initrd --verbose --no-checks \
    --config=%imagedir/proxmox-backup-restore-image.mk --kernel=$KVER
cp /boot/vmlinuz-$KVER %imagedir/bzImage

chmod 0644 %imagedir/{bzImage,initramfs.img}

%files
%config(noreplace) %imagedir/proxmox-backup-restore-image.mk

%changelog
* Tue Feb 03 2026 Sergey Konev <darisishe@altlinux.org> 0.1-alt4
- Update kernel dependencies for branches (FTBS fix)

* Sat Sep 27 2025 Ivan A. Melnikov <iv@altlinux.org> 0.1-alt3
- NMU: build on loongarch64

* Tue Mar 25 2025 Andrey Cherepanov <cas@altlinux.org> 0.1-alt2
- Added support for c10f2 branch.

* Tue Mar 18 2025 Sergey Konev <darisishe@altlinux.org> 0.1-alt1
- Initial build
