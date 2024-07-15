
%define _unpackaged_files_terminate_build 1

Name: box64
Version: 0.3.0
Release: alt2

Summary: Linux Userspace x86_64 Emulator with a twist

License: MIT
Group: Emulators
Url: https://github.com/ptitSeb/box64.git

Packager: Dmitry Terekhin <jqt4@altlinux.org>

ExclusiveArch: aarch64 loongarch64 riscv64

Source: %name-%version.tar
Source2: alt-box64-x64lib.tar
Patch:  %name-%version-%release.patch

BuildRequires(pre): rpm-macros-cmake
BuildRequires: cmake
BuildRequires: gcc
BuildRequires: python3

%description
Box64 lets you run x86_64 Linux programs (such as games)
on non-x86_64 Linux systems.

%ifarch aarch64
%define target ARM64
%endif
%ifarch loongarch64
%define target LARCH64
%endif
%ifarch riscv64
%define target RV64
%endif

# hey brp, please don't touch x86_64 libs
%define sysroot %_libexecdir/x86_64-linux-gnu
%add_verify_elf_skiplist %sysroot/*
%add_findreq_skiplist %sysroot/*
%add_findprov_skiplist %sysroot/*
%add_debuginfo_skiplist %sysroot/*

%prep
%setup
%autopatch -p1

%build
%cmake \
    -D%target:BOOL=ON \
    -DNOGIT:BOOL=ON \
    -DNO_LIB_INSTALL:BOOL=ON \
    %nil
%cmake_build

%install
%cmake_install

install -Dm644 %buildroot/etc/binfmt.d/box64.conf %buildroot%_binfmtdir/box64.conf
rm -rvf %buildroot/etc/binfmt.d

mkdir -p %buildroot%sysroot
tar -xvf %SOURCE2 -C %buildroot%sysroot --strip-components=1

%files
%doc README.md docs/*
%_bindir/box64
%_sysconfdir/box64.box64rc
%_binfmtdir/box64.conf
%sysroot

%changelog
* Fri Jul 12 2024 Ivan A. Melnikov <iv@altlinux.org> 0.3.0-alt2
- fix undefined symbol in box64 on riscv64
- bundle libraries from ALT archives in place of binaries
  provided by upstream

* Thu Jul 11 2024 Ivan A. Melnikov <iv@altlinux.org> 0.3.0-alt1
- 0.3.0

* Wed May 22 2024 Ivan A. Melnikov <iv@altlinux.org> 0.2.8-alt1.1
- disable loongarch64 extensions in dynarec
  (segfault workaround).

* Wed May 22 2024 Ivan A. Melnikov <iv@altlinux.org> 0.2.8-alt1
- 0.2.8

* Mon Dec 18 2023 Ivan A. Melnikov <iv@altlinux.org> 0.2.6-alt1.1
- Fix build on loongarch64.

* Sun Dec 17 2023 Ivan A. Melnikov <iv@altlinux.org> 0.2.6-alt1
- 0.2.6
- simplify spec
- loongarch64 support

* Mon Aug 21 2023 Ivan A. Melnikov <iv@altlinux.org> 0.2.4-alt1
- 0.2.4

* Tue Feb 07 2023 Dmitry Terekhin <jqt4@altlinux.org> 0.2.0-alt1
- Initial build
