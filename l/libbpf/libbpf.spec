# SPDX-License-Identifier: GPL-2.0-only
%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1
%set_verify_elf_method strict

Name: libbpf
Version: 1.4.5
Release: alt1
Summary: Stand-alone build of libbpf from the Linux kernel
Group: System/Libraries
License: BSD-2-Clause or LGPL-2.1
Url: https://github.com/libbpf/libbpf

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
%ifarch x86_64
%add_optflags -fanalyzer -Werror
%endif
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
* Fri Jul 12 2024 Vitaly Chikunov <vt@altlinux.org> 1.4.5-alt1
- Update to v1.4.5 (2024-07-11).

* Tue Jun 04 2024 Vitaly Chikunov <vt@altlinux.org> 1.4.3-alt1
- Update to v1.4.3 (2024-06-03).

* Sun May 12 2024 Vitaly Chikunov <vt@altlinux.org> 1.4.2-alt1
- Update to v1.4.2 (2024-05-10).

* Mon May 06 2024 Vitaly Chikunov <vt@altlinux.org> 1.4.1-alt1
- Update to v1.4.1 (2024-05-01).

* Fri Apr 12 2024 Vitaly Chikunov <vt@altlinux.org> 1.4.0-alt1
- Update to v1.4.0 (2024-03-25).

* Fri Jan 05 2024 Vitaly Chikunov <vt@altlinux.org> 1.3.0-alt1
- Update to v1.3.0 (2023-11-22).

* Wed Jul 12 2023 Alexey Gladkov <legion@altlinux.ru> 1.2.2-alt1
- Update to v1.2.2.

* Mon May 29 2023 Alexey Gladkov <legion@altlinux.ru> 1.2.0-alt1
- Update to v1.2.0.

* Wed Feb 15 2023 Vitaly Chikunov <vt@altlinux.org> 0.8.1-alt2
- (Fixes: CVE-2022-3534, CVE-2022-3606).

* Wed Jul 27 2022 Vitaly Chikunov <vt@altlinux.org> 0.8.1-alt1
- Update to v0.8.1 (2022-07-14).

* Sat May 28 2022 Vitaly Chikunov <vt@altlinux.org> 0.8.0-alt1
- Updated to v0.8.0 (2022-05-16).

* Wed Jan 12 2022 Vitaly Chikunov <vt@altlinux.org> 0.6.1-alt1
- Updated to v0.6.1 (2021-12-10).

* Fri Sep 10 2021 Vitaly Chikunov <vt@altlinux.org> 0.5.0-alt1
- Update to v0.5.0 (2021-09-07).

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
