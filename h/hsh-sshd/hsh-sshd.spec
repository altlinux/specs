Name: hsh-sshd
Version: 1.0
Release: alt1

Summary: A helper to run sshd (dropbear) within a hasher chroot
License: GPLv2+
Group: System/Servers

Source: %name-%version.tar

BuildRequires(pre): rpm-macros-meson
BuildRequires: meson
Requires: hasher

%description
%summary.

%package hasher
Summary: internal (in hasher) part of hsh-sshd
Group: Other
Requires: dropbear

%description hasher
%summary.

This package is only intended to be installed inside a hasher chroot.

%prep
%setup

%build
%meson
%meson_build -v

%install
%meson_install

%define _unpackaged_files_terminate_build 1
%set_verify_elf_method strict

%files
%doc README.md
%_bindir/hsh-sshd

%files hasher
%_bindir/hsh-dropbear-wrapper

%changelog
* Wed Mar 25 2026 Gleb F-Malinovskiy <glebfm@altlinux.org> 1.0-alt1
- Initial build.
