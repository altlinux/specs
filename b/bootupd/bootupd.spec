%define _unpackaged_files_terminate_build 1
%define service_name bootloader-update

Name: bootupd
Version: 0.2.25a
Release: alt1

Summary: Bootloader updater
License: Apache-2.0 AND BSD-3-Clause AND MIT AND (Apache-2.0 OR BSL-1.0) AND (Apache-2.0 OR MIT) AND (Apache-2.0 OR Apache-2.0 OR MIT) AND (Unlicense OR MIT)
Group: System/Base
Url: https://github.com/coreos/bootupd
Vcs: https://github.com/coreos/bootupd.git

Source: %name-%version.tar
Source1: vendor.tar
Patch: %name-%version-alt.patch

BuildRequires: rpm-build-rust rpm-build-systemd
BuildRequires: /proc
BuildRequires: rust-cargo
BuildRequires: pkgconfig(openssl)

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
* Wed Mar 26 2025 Vladimir Vaskov <rirusha@altlinux.org> 0.2.25a-alt1
- Initial build.
