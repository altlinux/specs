Name: debugedit
Version: 5.3
Release: alt1

Summary: A collection of debuginfo utilities
License: GPLv3+
Group: Development/Debug
URL: https://sourceware.org/debugedit/
Vcs: https://sourceware.org/git/debugedit.git
Source: %name-%version-%release.tar

BuildRequires: help2man, libelf-devel, libdw-devel
BuildRequires: libxxhash-devel
%{?!_without_check:%{?!_disable_check:
BuildRequires: gcc-c++
}}

%description
The debugedit project provides programs and scripts for creating
debuginfo and source file distributions, collect build-ids and rewrite
source paths in DWARF data for debugging, tracing and profiling.

%prep
%setup -n %name-%version-%release
# We do not use find-debuginfo and tests fail.
sed -i '/find-debuginfo.at/d' tests/testsuite.at
# It's a find-debuginfo helper.
sed -i '/debugedit-classify-ar.at/d' tests/testsuite.at
# Make tools required for find-debuginfo (such as dwz and gdb) optional.
sed -i '/find-debuginfo/s/AC_MSG_ERROR/AC_MSG_WARN/' configure.ac
# Avoid configure error messages due to missing related tools.
sed -i '/./{H;$!d};x;/GDB_VERSION_STRING/d' configure.ac

%build
%autoreconf
%configure --disable-silent-rules
%make_build

%install
%makeinstall_std
rm %buildroot%_bindir/find-debuginfo
rm %buildroot%_man1dir/find-debuginfo.1
rm %buildroot%_bindir/debugedit-classify-ar
rm %buildroot%_man1dir/debugedit-classify-ar.1

%set_verify_elf_method strict
%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1

%check
%make_build -k check VERBOSE=1 || {
	cat tests/testsuite.log
	exit 1
}

%files
%_bindir/debugedit
%_bindir/sepdebugcrcfix
%_man1dir/debugedit.1*
%_man1dir/sepdebugcrcfix.1*
%doc README find-debuginfo find-debuginfo.1

%changelog
* Sat Mar 14 2026 Vitaly Chikunov <vt@altlinux.org> 5.3-alt1
- Update to debugedit-5.3 (2026-03-10).

* Fri Jun 27 2025 Vitaly Chikunov <vt@altlinux.org> 5.1-alt1.g468ff08
- Update to debugedit-5.1-11-g468ff08 (2025-06-27) (ALT#54930).

* Fri May 03 2024 Dmitry V. Levin <ldv@altlinux.org> 5.0.0.27.6dd2-alt1
- 5.0-19-g5bade25 -> 5.0-27-g6dd28bb (closes: #50067).

* Fri Apr 21 2023 Dmitry V. Levin <ldv@altlinux.org> 5.0.0.19.5bad-alt1
- 5.0-2-gae27211 -> 5.0-19-g5bade25 (closes: #45958).

* Mon Aug 02 2021 Dmitry V. Levin <ldv@altlinux.org> 5.0.0.2.ae27-alt1
- 0.3-7-ge04296d -> 5.0-2-gae27211.

* Mon Jul 05 2021 Dmitry V. Levin <ldv@altlinux.org> 0.3.0.7.e042-alt1
- 0.2 -> 0.3-7-ge04296d.

* Wed May 05 2021 Dmitry V. Levin <ldv@altlinux.org> 0.2-alt1
- 0.1 -> 0.2.

* Wed Apr 14 2021 Dmitry V. Levin <ldv@altlinux.org> 0.1-alt1
- Initial revision.
