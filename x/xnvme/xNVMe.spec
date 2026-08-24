# SPDX-License-Identifier: GPL-2.0-only
%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1
%set_verify_elf_method strict
%define soname 0

Name: xnvme
Version: 0.7.5
Release: alt1
Summary: xNVMe: cross-platform libraries and tools for NVMe devices
License: BSD-3-Clause
Group: System/Kernel and hardware
Url: https://xnvme.io/
Vcs: https://github.com/OpenMPDK/xNVMe
ExcludeArch: armh %ix86

Source: %name-%version.tar
Patch1: %name-%version-%release.patch
BuildRequires(pre): rpm-macros-meson
BuildRequires: meson
BuildRequires: bash-completion
BuildRequires: libaio-devel
BuildRequires: liburing-devel

%description
%summary.

%package -n libxnvme%soname
Summary: Library for %name
Group: System/Libraries

%description -n libxnvme%soname
%summary.

%package -n libxnvme-devel
Summary: Development files for %name
Group: Development/C
Requires: libxnvme%soname = %EVR
Conflicts: libxnvme = 0.7.0-alt1

%description -n libxnvme-devel
%summary.

%prep
%setup
%patch1 -p1

%build
%define optflags_lto %nil
%meson \
	-Ddefault_library=shared \
	-Dwith-spdk=disabled \
	-Dwith-libvfn=disabled \
	-Dtests=false \
	-Dexamples=false
%meson_build -v

%install
%meson_install

%files
%_bindir/*
%_man1dir/*.1*
%_datadir/bash-completion/completions/*

%files -n libxnvme%soname
%_libdir/libxnvme.so.%soname
%_libdir/libxnvme.so.%soname.*

%files -n libxnvme-devel
%_libdir/libxnvme.so
%_includedir/libxnvme*
%_pkgconfigdir/xnvme.pc


%changelog
* Sun Aug 23 2026 Anton Farygin <rider@altlinux.org> 0.7.5-alt1
- 0.7.0 -> 0.7.5
- dropped test and example utilities

* Sat Jul 22 2023 Vitaly Chikunov <vt@altlinux.org> 0.7.0-alt1
- First import v0.7.0 (2023-06-20).
