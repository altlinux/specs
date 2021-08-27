# SPDX-License-Identifier: GPL-2.0-only
%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1

Name: libbpf
Version: 0.4.0
Release: alt2
Summary: Stand-alone build of libbpf from the Linux kernel
Group: System/Libraries
License: BSD-2-Clause or LGPL-2.1
Url: https://github.com/libbpf/libbpf
Vcs: https://github.com/libbpf/libbpf.git

Source: %name-%version.tar

BuildRequires: libelf-devel
BuildRequires: zlib-devel

%description
Library to access Linux kernel BPF API.

%package devel
Summary: Libbpf library and headers
Group: Development/C
License: LGPLv2 or BSD
Requires: %name = %EVR

%description devel
Library and header files to build with libbpf.

%prep
%setup

%build
cd src
%make_build CFLAGS="%optflags -fPIC" V=1 STATIC_LIBS=

%install
cd src
%makeinstall_std LIBSUBDIR=%_lib STATIC_LIBS=

%files
%_libdir/libbpf.so.*

%files devel
%doc LICENSE* README.md
%_includedir/bpf
%_libdir/libbpf.so
%_pkgconfigdir/libbpf.pc

%changelog
* Fri Aug 27 2021 Vitaly Chikunov <vt@altlinux.org> 0.4.0-alt2
- Fix build with latest gcc/binutils with LTO.
- Do not build libbpf-devel-static package.

* Mon May 31 2021 Vitaly Chikunov <vt@altlinux.org> 0.4.0-alt1
- Update to v0.4.0 (2021-05-22).

* Mon Jan 25 2021 Vitaly Chikunov <vt@altlinux.org> 0.3-alt2
- Re-compile with `-fPIC'.

* Thu Jan 07 2021 Vitaly Chikunov <vt@altlinux.org> 0.3-alt1
- Update to v0.3 (2021-01-02).

* Sat Dec 05 2020 Vitaly Chikunov <vt@altlinux.org> 0.2-alt1
- Update to v0.2 (2020-10-28).

* Mon Oct 05 2020 Vitaly Chikunov <vt@altlinux.org> 0.1.1-alt1
- Update to v0.1.1 (2020-09-24).

* Mon Aug 24 2020 Vitaly Chikunov <vt@altlinux.org> 0.1.0-alt1
- Update v0.1.0 (2020-08-18).

* Wed Jul 01 2020 Vitaly Chikunov <vt@altlinux.org> 0.0.9-alt1
- Update to v0.0.9.

* Mon Apr 27 2020 Vitaly Chikunov <vt@altlinux.org> 0.0.8-alt1
- First import of v0.0.8.
