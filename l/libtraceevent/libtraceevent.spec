# SPDX-License-Identifier: GPL-2.0-only
%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1
%set_verify_elf_method strict

Name: libtraceevent
Version: 1.5.2
Release: alt1
Summary: Library to parse raw trace event formats
License: GPL-2.0-only and LGPL-2.1-only
Group: System/Libraries
Url: https://git.kernel.org/pub/scm/libs/libtrace/libtraceevent.git/
Vcs: git://git.kernel.org/pub/scm/libs/libtrace/libtraceevent.git

Source: %name-%version.tar

Conflicts: trace-cmd-libs < 2.9.6-alt1
BuildRequires: asciidoc
BuildRequires: xmlto

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
%make_build CFLAGS="%optflags" prefix=%_prefix libdir=%_libdir V=1 all doc

%install
%makeinstall_std prefix=%_prefix libdir=%_libdir htmldir=%_defaultdocdir/%name doc-install V=1
rm %buildroot%_libdir/libtraceevent.a
# html documentation is duplicating man pages.
rm -rf %buildroot%_defaultdocdir/%name

%files
%doc LICENSES/*
%_libdir/libtraceevent.so.*
%_libdir/traceevent

%files devel
%_includedir/traceevent
%_libdir/libtraceevent.so
%_libdir/pkgconfig/libtraceevent.pc
%_man3dir/*.3.*

%changelog
* Thu Mar 24 2022 Vitaly Chikunov <vt@altlinux.org> 1.5.2-alt1
- Updated to libtraceevent-1.5.2 (2022-03-09).

* Sat Jan 22 2022 Vitaly Chikunov <vt@altlinux.org> 1.5.0-alt1
- Imported libtraceevent-1.5.0-2-gad8bff2 (2022-01-10).
