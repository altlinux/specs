%define _unpackaged_files_terminate_build 1

Summary: Include btrfs snapshots at boot options. (Grub menu) 
Name: grub-btrfs
Version: 4.11
Release: alt1
License: GPLv3
Group: System/Kernel and hardware
URL: https://github.com/Antynea/grub-btrfs
BuildArch: noarch

Source: %name-%version.tar
Patch1: disable-root-check.patch

%description
Improves grub by adding "btrfs snapshots" to the grub menu.

You can boot your system on a "snapshot" from the grub menu.
Supports manual snapshots, snapper, timeshift ...

%prep
%setup
%patch1 -p1

%build
%make_build DESTDIR=%buildroot

%install
%make_install DESTDIR=%buildroot

mv %buildroot/usr/lib/ %buildroot/lib/
rm %buildroot/%_datadir/licenses/grub-btrfs/LICENSE

%files
%config(noreplace) %_sysconfdir/default/%name/config
%doc LICENSE
%_sysconfdir/grub.d/41_snapshots-btrfs
%_unitdir/%name.path
%_unitdir/%name.service
%_docdir/%name/README.md
%_docdir/%name/initramfs-overlayfs.md

%changelog
* Mon Aug 08 2022 Oleg Solovyov <mcpain@altlinux.org> 4.11-alt1
- Initial build for Sisyphus
