Name: debugedit
Version: 0.1
Release: alt1

Summary: A collection of debuginfo utilities
License: GPLv3+
Group: Development/Debug
URL: https://sourceware.org/debugedit/
# git://git.altlinux.org/gears/d/debugedit.git
Source: %name-%version-%release.tar

BuildRequires: libelf-devel, libdw-devel

%description
The debugedit project provides programs and scripts for creating
debuginfo and source file distributions, collect build-ids and rewrite
source paths in DWARF data for debugging, tracing and profiling.

%prep
%setup -n %name-%version-%release

%build
%autoreconf
%configure --disable-silent-rules
%make_build

%install
%makeinstall_std
rm %buildroot%_bindir/find-debuginfo.sh

%set_verify_elf_method strict
%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1

%check
%make_build -k check VERBOSE=1

%files
%_bindir/debugedit
%_bindir/sepdebugcrcfix
%doc README scripts/find-debuginfo.sh

%changelog
* Wed Apr 14 2021 Dmitry V. Levin <ldv@altlinux.org> 0.1-alt1
- Initial revision.
