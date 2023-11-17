# SPDX-License-Identifier: GPL-2.0-only
%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1
%set_verify_elf_method strict

%define sover 2
Name: minisat
Version: 2.2.1
Release: alt1
Summary: A minimalistic and high-performance SAT solver
License: MIT
Group: Sciences/Mathematics
Url: http://minisat.se/
Vcs: https://github.com/niklasso/minisat
# Forks are messed up, tagging 2.2.1 (2017) and releases/2.2.1 (2018),
# mostly maintaining CMakeLists.txt, accepting-and-then reverting correct
# downstream parches (to CMakeLists.txt).
#   Vcs: https://github.com/stp/minisat
#   Vcs: https://github.com/msoos/minisat
# 3rd party How-To: https://dwheeler.com/essays/minisat-user-guide.html
Requires: libminisat%sover = %EVR

Source: %name-%version.tar
BuildRequires: gcc-c++
BuildRequires: zlib-devel

%description
MiniSat is a minimalistic, open-source SAT solver, developed to help
researchers and developers alike to get started on SAT.

%package -n libminisat%sover
Summary: Shared library for minisat
Group: System/Libraries

%description -n libminisat%sover
%summary.

%package -n libminisat-devel
Summary: Development headers for %name
Group: Development/C
Requires: libminisat%sover = %EVR

%description -n libminisat-devel
%summary.

%package -n libminisat-devel-static
Summary: Static library for %name
Group: Development/C
Requires: libminisat-devel = %EVR

%description -n libminisat-devel-static
%summary.

This is what CBMC requires to compile.

%prep
%setup

%build
%{?optflags_lto:%global optflags_lto %optflags_lto -ffat-lto-objects}
%add_optflags %(getconf LFS_CFLAGS)
# Build extended solver with simplification capabilities (simp), not a core one.
# No parallel make.
%make lsh sh lr CXXFLAGS="%optflags" prefix=%_prefix libdir=%_libdir VERB=

%install
%makeinstall VERB=
install -Dpm644 minisat.1 -t %buildroot%_man1dir

%check
# Input in a simplified DIMACS CNF format.
cat <<-EOF > test.in
	c Here is a comment.
	p cnf 5 3
	1 -5 4 0
	-1 5 3 4 0
	-3 -4 0
EOF
export LD_LIBRARY_PATH=%buildroot%_libdir
( set +e
  %buildroot%_bindir/minisat test.in test.out
  test $? -eq 10 )
cat test.out
grep -x 'SAT' test.out
grep -x -e '-1 -2 -3 -4 -5 0' test.out
# Our result: -1 -2 -3 -4 -5 0
# Fedora/Debian: -1 -2 -3 -4 -5 0
# User Guide: 1 2 -3 4 5 0

%files
%_bindir/minisat*
%_man1dir/minisat.1*

%files -n libminisat%sover
%define _customdocdir %_docdir/%name
%doc LICENSE README doc/ReleaseNotes-2.2.0.txt minisat-user-guide.md
%_libdir/libminisat.so.%sover
%_libdir/libminisat.so.%sover.*

%files -n libminisat-devel
%_includedir/minisat
%_libdir/libminisat.so

%files -n libminisat-devel-static
%_libdir/libminisat.a

%changelog
* Wed Nov 15 2023 Vitaly Chikunov <vt@altlinux.org> 2.2.1-alt1
- Revive the package (for cbmc).
- Upstream is abandoned sine 2013-09-25, community released what had not been
  released as 2.2.1 (2018-03-07), then maintaining mostly CMake build system.

* Thu Dec 05 2013 Michael Pozhidaev <msp@altlinux.ru> 2.2.0-alt5
- Fixed building bug with missed m4 directory

* Fri Mar 01 2013 Michael Pozhidaev <msp@altlinux.ru> 2.2.0-alt4
- Proper collisions support
- Assumptions support is removed

* Sat Jan 19 2013 Michael Pozhidaev <msp@altlinux.ru> 2.2.0-alt3
- Conflicts analyzing is added

* Sat Dec 22 2012 Michael Pozhidaev <msp@altlinux.ru> 2.2.0-alt2
- Variable value assumption support added

* Sun Oct 28 2012 Michael Pozhidaev <msp@altlinux.ru> 2.2.0-alt1
- Initial package
