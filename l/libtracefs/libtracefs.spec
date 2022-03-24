# SPDX-License-Identifier: GPL-2.0-only
%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1
%set_verify_elf_method strict

Name: libtracefs
Version: 1.3.1
Release: alt1
Summary: Library to access kernel tracefs
License: LGPL-2.1-only
Group: System/Libraries
Url: https://git.kernel.org/pub/scm/libs/libtrace/libtracefs.git

Source: %name-%version.tar

Conflicts: trace-cmd-libs < 2.9.6-alt1
BuildRequires: libtraceevent-devel

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
export CFLAGS="%optflags"
%make_build prefix=%_prefix libdir=%_libdir V=1

%install
%makeinstall_std prefix=%_prefix libdir=%_libdir V=1
rm %buildroot%_libdir/libtracefs.a

%files
%doc LICENSES/LGPL-2.1
%_libdir/libtracefs.so.*

%files devel
%_includedir/tracefs
%_libdir/libtracefs.so
%_libdir/pkgconfig/libtracefs.pc

%changelog
* Wed Mar 23 2022 Vitaly Chikunov <vt@altlinux.org> 1.3.1-alt1
- Updated to libtracefs-1.3.1 (2022-03-10).

* Sat Jan 22 2022 Vitaly Chikunov <vt@altlinux.org> 1.2.5-alt1
- Imported libtracefs-1.2.5 (2021-08-03).
