%define _unpackaged_files_terminate_build 1

Name: hasher-proot
Version: 0.1.0
Release: alt1

Summary: Hasher backend using PRoot
License: GPL-3.0-or-later
Group: Development/Other

BuildArch: noarch

Source: %name-%version.tar

Requires: hasher
Requires: proot >= 5.5.0
Requires: fakeroot

BuildRequires: python3
BuildRequires: hasher

%description
Run Hasher through PRoot without privileged chroot helpers.
Private adapted Hasher scripts leave the system Hasher unchanged.
Only the default Hasher subconfiguration is supported.

%prep
%setup

%install
%makeinstall_std

%files
%_bindir/hasher-proot
%_prefix/libexec/hasher-proot
%_datadir/hasher-proot
%doc README.md

%changelog
* Tue Nov 03 2026 Vladimir Romanov <rirusha@altlinux.org> 0.1.0-alt1
- Initial build.
