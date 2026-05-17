%define _unpackaged_files_terminate_build 1

Name: unionfs
Version: 3.7
Release: alt1
Summary: union filesystem using FUSE

Group: File tools
License: BSD
Url: https://github.com/rpodgorny/unionfs-fuse

Source: %name-%version.tar

BuildRequires: gcc libattr-devel libfuse3-devel

%description
unionfs filesystem implementation which is way more flexible than the current in-kernel unionfs solution.

%prep
%setup

%build
%make_build

%install
%makeinstall_std PREFIX=%_prefix

%files
%_bindir/*
%_sbindir/mount.unionfs
%_man8dir/*.8*
%doc README.md

%changelog
* Sun May 17 2026 Dmitry Udalov <udalov@altlinux.org> 3.7-alt1
- Update to upstream v3.7.
- Switch from libfuse to libfuse3.
- Package new mount.unionfs helper and unionfsctl control utility.

* Wed May 24 2017 Alexey Gladkov <legion@altlinux.ru> 2.0-alt1.git039ba92
- Initial build for ALT Linux Sisyphus
