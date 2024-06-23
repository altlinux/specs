%define _unpackaged_files_terminate_build 1

Name: grub-btrfs
Version: 4.13
Release: alt3

Summary: Include btrfs snapshots at boot options. (Grub menu)
License: GPLv3
Group: System/Kernel and hardware
URL: https://github.com/Antynea/grub-btrfs
BuildArch: noarch

Source: %name-%version.tar
Patch1: grub-btrfs-4.13-alt-disable-root-check.patch

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
%makeinstall_std

rm -v %buildroot/%_datadir/licenses/%name/LICENSE

%files
%config(noreplace) %_sysconfdir/default/%name/config
%doc LICENSE
%_sysconfdir/grub.d/41_snapshots-btrfs
%_unitdir/%{name}d.service
%_docdir/%name/README.md
%_docdir/%name/initramfs-overlayfs.md
%_bindir/%{name}d
%_man8dir/%name.8.xz
%_man8dir/%{name}d.8.xz

%changelog
* Sun Jun 23 2024 Anton Kurachenko <srebrov@altlinux.org> 4.13-alt3
- Fix FTBFS.

* Sun Jul 09 2023 Anton Kurachenko <srebrov@altlinux.org> 4.13-alt2
- Renaming a patch file according to naming conventions.
- Cosmetic changes in the spec file.

* Tue Jul 04 2023 Anton Kurachenko <srebrov@altlinux.org> 4.13-alt1
- Update to version 4.13.

* Mon Aug 08 2022 Oleg Solovyov <mcpain@altlinux.org> 4.11-alt1
- Initial build for Sisyphus.
