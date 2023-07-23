# SPDX-License-Identifier: GPL-2.0-only
%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1
%set_verify_elf_method strict

Name: xnvme
Version: 0.7.0
Release: alt1
Summary: xNVMe: cross-platform libraries and tools for NVMe devices
License: BSD-3-Clause
Group: System/Kernel and hardware
Url: https://xnvme.io/
Vcs: https://github.com/OpenMPDK/xNVMe
ExcludeArch: armh %ix86

Source: %name-%version.tar
BuildRequires(pre): rpm-macros-meson
BuildRequires: meson
BuildRequires: libaio-devel
BuildRequires: liburing-devel

%description
%summary.

%package -n libxnvme
Summary: Library for %name
Group: System/Libraries

%description -n libxnvme
%summary.

%package -n libxnvme-devel
Summary: Development files for %name
Group: Development/C
Requires: libxnvme = %EVR

%description -n libxnvme-devel
%summary.

%prep
%setup

%build
%define optflags_lto %nil
%meson \
	-Ddefault_library=shared \
	-Dwith-spdk=false \
	-Dwith-libvfn=false
%meson_build -v

%install
%meson_install
rm %buildroot%_libdir/libxnvme.a

%files
%_bindir/*
%_man1dir/*.1*

%files -n libxnvme
%_libdir/libxnvme.so

%files -n libxnvme-devel
%_includedir/libxnvme*
%_pkgconfigdir/xnvme.pc


%changelog
* Sat Jul 22 2023 Vitaly Chikunov <vt@altlinux.org> 0.7.0-alt1
- First import v0.7.0 (2023-06-20).
