# SPDX-License-Identifier: GPL-2.0-only
%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1
%set_verify_elf_method strict

Name: libtraceevent
Version: 1.8.3
Release: alt1
Summary: Library to parse raw trace event formats
License: GPL-2.0-only and LGPL-2.1-only
Group: System/Libraries
Url: https://git.kernel.org/pub/scm/libs/libtrace/libtraceevent.git/
Vcs: git://git.kernel.org/pub/scm/libs/libtrace/libtraceevent.git

Source: %name-%version.tar

Conflicts: trace-cmd-libs < 2.9.6-alt1
BuildRequires: asciidoc
BuildRequires: source-highlight
BuildRequires: xmlto
%{?!_without_check:%{?!_disable_check:
BuildRequires: CUnit-devel
}}

%description
%summary.

%package devel
Summary: %summary
Group: Development/C
Requires: %name = %EVR

%description devel
%summary.

%prep
%setup
sed -i 's/,-rpath=\$\$ORIGIN//' scripts/utils.mk

%build
%define optflags_lto %nil
%add_optflags %(getconf LFS_CFLAGS)
# Parallel build causing races on e2k.
%make CFLAGS="%optflags" prefix=%_prefix libdir=%_libdir V=1 all doc

%install
%makeinstall_std prefix=%_prefix libdir=%_libdir htmldir=%_defaultdocdir/%name doc-install V=1
rm %buildroot%_libdir/libtraceevent.a
# html documentation is duplicating man pages.
rm -rf %buildroot%_defaultdocdir/%name

%check
%make test V=1
utest/trace-utest

%files
%doc LICENSES/*
%_libdir/libtraceevent.so.*
%_libdir/traceevent

%files devel
%doc samples/*.c
%_includedir/traceevent
%_libdir/libtraceevent.so
%_libdir/pkgconfig/libtraceevent.pc
%_man3dir/*.3.*

%changelog
* Fri Aug 02 2024 Vitaly Chikunov <vt@altlinux.org> 1.8.3-alt1
- Update to libtraceevent-1.8.3 (2024-07-24).

* Tue Jan 09 2024 Vitaly Chikunov <vt@altlinux.org> 1.8.2-alt1
- Update to libtraceevent-1.8.2 (2024-01-08).

* Sun Dec 31 2023 Vitaly Chikunov <vt@altlinux.org> 1.8.1-alt1
- Update to libtraceevent-1.8.1 (2023-12-28).

* Mon Dec 25 2023 Vitaly Chikunov <vt@altlinux.org> 1.8.0-alt1
- Update to libtraceevent-1.8.0 (2023-12-24).

* Mon Jun 26 2023 Vitaly Chikunov <vt@altlinux.org> 1.7.3-alt1
- Update to libtraceevent-1.7.3 (2023-06-07).

* Thu May 11 2023 Vitaly Chikunov <vt@altlinux.org> 1.7.2-alt2
- spec: Disable parallel build.
- spec: Fix source-highlight warning when building doc.

* Mon May 08 2023 Vitaly Chikunov <vt@altlinux.org> 1.7.2-alt1
- Update to libtraceevent-1.7.2 (2023-03-27).

* Sat Aug 27 2022 Vitaly Chikunov <vt@altlinux.org> 1.6.2-alt1
- Updated to libtraceevent-1.6.2 (2022-07-14).

* Sat Mar 26 2022 Vitaly Chikunov <vt@altlinux.org> 1.5.3-alt1
- Updated to libtraceevent-1.5.3 (2022-03-24).

* Thu Mar 24 2022 Vitaly Chikunov <vt@altlinux.org> 1.5.2-alt1
- Updated to libtraceevent-1.5.2 (2022-03-09).

* Sat Jan 22 2022 Vitaly Chikunov <vt@altlinux.org> 1.5.0-alt1
- Imported libtraceevent-1.5.0-2-gad8bff2 (2022-01-10).
