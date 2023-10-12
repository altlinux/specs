%define imagedir /usr/libexec/proxmox-backup/file-restore
%define cachedir /var/cache/proxmox-backup

Name: pve-backup-restore-image
Version: 0.2
Release: alt1

Summary: Kernel/initramfs images for Proxmox Backup single file restore
License: GPL-2.0
Group: Development/Other

ExclusiveArch: x86_64 aarch64

Requires(post): make-initrd-pbs
Requires(post): thin-provisioning-tools
Requires(post): kernel
Requires(post): proxmox-backup-file-restore
Requires: /proc

Provides: proxmox-backup-restore-image = %EVR

%description
%summary.

%install
mkdir -p %buildroot%imagedir

cat > %buildroot%imagedir/%name.mk <<END
IMAGEFILE = %imagedir/initramfs.img
FEATURES += pbs
END

cat > %buildroot%imagedir/%name.sh <<EOF
#!/bin/sh

INST_PATH="%imagedir"
CACHE_PATH="%cachedir/file-restore-initramfs.img"

export PATH="/sbin:/bin:/usr/sbin:/usr/bin:/usr/local/bin"

trap "rm -rf -- \$CACHE_PATH.tmp" EXIT

mkdir -p %imagedir
VMLINUZ="\$(readlink -e -- /boot/vmlinuz-*alt*)"
KVER="\${VMLINUZ##*/vmlinuz-}"
echo "VMLINUZ = \$VMLINUZ"
echo "KVER = \$KVER"
rm -f "%imagedir/initramfs.img"
make-initrd --config=%imagedir/%name.mk --kernel=\$KVER

mkdir -p "%cachedir"
cp "\$INST_PATH/initramfs.img" "\$CACHE_PATH.tmp"
mv -f "\$CACHE_PATH.tmp" "\$CACHE_PATH"

cp /boot/vmlinuz-\$KVER %imagedir/bzImage
chmod 0644 %imagedir/{bzImage,initramfs.img}
exit 0
EOF
chmod 0755 %buildroot%imagedir/%name.sh

%post
%imagedir/%name.sh

%files
%dir %imagedir
%config(noreplace) %imagedir/%name.mk
%imagedir/%name.sh
#%%ghost %imagedir/bzImage
#%%ghost %imagedir/initramfs.img

%changelog
* Thu Oct 12 2023 Andrew A. Vasilyev <andy@altlinux.org> 0.2-alt1
- add Provides for proxmox-backup-restore-image

* Fri Jul 21 2023 Andrew A. Vasilyev <andy@altlinux.org> 0.1-alt1
- Initial release.

