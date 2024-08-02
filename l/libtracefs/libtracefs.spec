# SPDX-License-Identifier: GPL-2.0-only
%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1
%set_verify_elf_method strict

Name: libtracefs
Version: 1.8.1
Release: alt1
Summary: Library to access kernel tracefs
License: LGPL-2.1-only
Group: System/Libraries
Url: https://git.kernel.org/pub/scm/libs/libtrace/libtracefs.git

Source: %name-%version.tar

Conflicts: trace-cmd-libs < 2.9.6-alt1
BuildRequires: asciidoc
BuildRequires: libtraceevent-devel
BuildRequires: xmlto
%{?!_without_check:%{?!_disable_check:
BuildRequires: CUnit-devel
}}

%description
%summary.

%package tools
Summary: %summary (sqlhist)
Group: Development/Tools
Requires: %name = %EVR

%description tools
%summary.

As sqlhist is just example code from a man page, it is guaranteed to contain
lots of bugs. For one thing, not all error paths are covered properly.

%package devel
Summary: %summary (Headers)
Group: Development/C
Requires: %name = %EVR

%description devel
%summary.

%package doc
Summary: %summary (Documentation)
Group: Development/Documentation

%description doc
%summary.

%prep
%setup
sed -i 's/,-rpath=\$\$ORIGIN//' scripts/utils.mk

%build
%define optflags_lto %nil
%add_optflags %(getconf LFS_CFLAGS)
export CFLAGS="%optflags"
%make_build prefix=%_prefix libdir=%_libdir all doc sqlhist V=1

%install
%makeinstall_std prefix=%_prefix libdir=%_libdir install_doc V=1
rm %buildroot%_libdir/libtracefs.a
install -Dp bin/sqlhist %buildroot/%_bindir/sqlhist

%check
%make_build test V=1
utest/trace-utest

%files
%doc LICENSES/LGPL-2.1 LICENSES/GPL-2.0
%_libdir/libtracefs.so.*

%files tools
%_bindir/sqlhist
%_man1dir/sqlhist.1*

%files devel
%doc README
%_includedir/tracefs
%_libdir/libtracefs.so
%_pkgconfigdir/libtracefs.pc
%_man3dir/*.3*

%files doc
%_defaultdocdir/%name-doc

%changelog
* Fri Aug 02 2024 Vitaly Chikunov <vt@altlinux.org> 1.8.1-alt1
- Update to libtracefs-1.8.1 (2024-07-24).

* Sat Jan 13 2024 Vitaly Chikunov <vt@altlinux.org> 1.8.0-alt1
- Update to libtracefs-1.8.0 (2024-01-09).

* Mon Jun 26 2023 Vitaly Chikunov <vt@altlinux.org> 1.7.0-alt1
- Update to libtracefs-1.7.0 (2023-06-07).

* Mon May 08 2023 Vitaly Chikunov <vt@altlinux.org> 1.6.4-alt1
- Update to libtracefs-1.6.4 (2023-01-09).

* Sat Aug 27 2022 Vitaly Chikunov <vt@altlinux.org> 1.4.2-alt1
- Updated to libtracefs-1.4.2 (2022-07-14).

* Wed Mar 23 2022 Vitaly Chikunov <vt@altlinux.org> 1.3.1-alt1
- Updated to libtracefs-1.3.1 (2022-03-10).

* Sat Jan 22 2022 Vitaly Chikunov <vt@altlinux.org> 1.2.5-alt1
- Imported libtracefs-1.2.5 (2021-08-03).
