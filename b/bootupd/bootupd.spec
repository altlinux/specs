%define _unpackaged_files_terminate_build 1
%define service_name bootloader-update

Name: bootupd
Version: 0.2.32
Release: alt3

Summary: Bootloader updater
License: Apache-2.0 AND BSD-3-Clause AND MIT AND (Apache-2.0 OR BSL-1.0) AND (Apache-2.0 OR MIT) AND (Apache-2.0 WITH LLVM-exception OR Apache-2.0 OR MIT) AND (Unlicense OR MIT)
Group: System/Base
URL: https://github.com/coreos/bootupd
VCS: https://github.com/coreos/bootupd.git

Source: %name-%version.tar
Source1: vendor.tar
Patch: %name-%version-%release.patch

BuildRequires: rpm-build-rust
BuildRequires: rpm-build-systemd
BuildRequires: rust-cargo
BuildRequires: pkgconfig(openssl)
BuildRequires: /proc

%description
Today many Linux systems handle updates for bootloader data in an
inconsistent and ad-hoc way. For example, on Fedora and Debian, a
package manager update will update UEFI binaries in /boot/efi, but
not the BIOS MBR data.

Transactional/"image" update systems like OSTree and dual-partition
systems like the Container Linux update system are more consistent:
they normally cover kernel/userspace but not anything related to bootloaders.

The reason for this is straightforward: performing bootloader updates in
an "A/B" fashion requires completely separate nontrivial logic from managing
the kernel and root filesystem. Today OSTree e.g. makes the choice that it
does not update /boot/efi (and also doesn't update the BIOS MBR).

%prep
%setup -a1
%autopatch -p1

%build
%make_compile

%install
%makeinstall_std
%make_install install-grub-static DESTDIR=%buildroot
%make_install install-systemd-unit DESTDIR=%buildroot

%files
%_bindir/bootupctl
%_libexecdir/%name
%_unitdir/%service_name.service
%_prefix/libexec/%name
%doc README.md

%changelog
* Wed Jun 17 2026 Vladimir Romanov <rirusha@altlinux.org> 0.2.32-alt3
- Add refreshing GRUB configs and modules on update, not just install.

* Sat Mar 14 2026 Vladimir Romanov <rirusha@altlinux.org> 0.2.32-alt2
- Added adaptation to the behavior of grub 2.14+.

* Thu Feb 26 2026 Vladimir Romanov <rirusha@altlinux.org> 0.2.32-alt1
- New version: 0.2.32.

* Wed Mar 26 2025 Vladimir Vaskov <rirusha@altlinux.org> 0.2.25a-alt1
- Initial build.
