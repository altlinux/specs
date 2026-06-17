# Unpackaged files in buildroot should terminate build
%define _unpackaged_files_terminate_build 1
%def_with check

# Scotch links against either scotcherr or scotcherrexit,
# symbols are left undefined; the end user is to choose
%set_verify_elf_method unresolved=relaxed

%define mpiimpl openmpi
%define mpidir %_libdir/%mpiimpl

%define sover 7.0

Name: scotch
Version: 7.0.12
Release: alt1

Summary: Package and libraries for sequential and parallel graph partitioning
License: CECILL-C
Group: Sciences/Mathematics

URL: http://www.labri.fr/perso/pelegrin/scotch
VCS: https://gitlab.inria.fr/scotch/scotch

# Source-url: %vcs/-/archive/v%version/%name-v%version.tar.gz
Source: %name-%version.tar

Patch: disable-scotchmetisv3.patch

BuildRequires(pre): rpm-macros-cmake
BuildRequires: gcc-fortran libgfortran-devel bison flex cmake
BuildRequires: zlib-devel bzlib-devel liblzma-devel
BuildRequires: glibc-devel %mpiimpl-devel
%if_with check
BuildRequires: ctest
%endif

%description
Scotch is a software package and libraries for sequential and parallel graph
partitioning, static mapping, and sparse matrix block ordering, and sequential
mesh and hypergraph partitioning.

%package -n libscotch%sover
Summary: Shared libraries of Scotch
Group: System/Libraries

%description -n libscotch%sover
Scotch is a software package and libraries for sequential and parallel graph
partitioning, static mapping, and sparse matrix block ordering, and sequential
mesh and hypergraph partitioning.

This package contains shared libraries of Scotch.

%package -n libesmumps%sover
Summary: MUMPS interface component for Scotch
Group: System/Libraries
Requires: libscotch%sover = %EVR

%description -n libesmumps%sover
Scotch is a software package and libraries for sequential and parallel graph
partitioning, static mapping, and sparse matrix block ordering, and sequential
mesh and hypergraph partitioning.

This package contains MUMPS interface component for Scotch.

%package -n libscotchmetis%sover
Summary: MeTiS compatibility library for Scotch
Group: System/Libraries
Requires: libscotch%sover = %EVR

%description -n libscotchmetis%sover
Scotch is a software package and libraries for sequential and parallel graph
partitioning, static mapping, and sparse matrix block ordering, and sequential
mesh and hypergraph partitioning.

This package contains MeTiS compatibility library for Scotch.

%package -n libptscotch%sover
Summary: Shared libraries of PT-Scotch
Group: System/Libraries
Requires: libscotch%sover = %EVR

%description -n libptscotch%sover
Scotch is a software package and libraries for sequential and parallel graph
partitioning, static mapping, and sparse matrix block ordering, and sequential
mesh and hypergraph partitioning.

This package contains shared libraries of PT-Scotch, the parallelized version
of Scotch.

%package -n libptesmumps%sover
Summary: MUMPS interface component for PT-Scotch
Group: System/Libraries
Requires: libptscotch%sover = %EVR

%description -n libptesmumps%sover
Scotch is a software package and libraries for sequential and parallel graph
partitioning, static mapping, and sparse matrix block ordering, and sequential
mesh and hypergraph partitioning.

This package contains MUMPS interface component for PT-Scotch, the parallelized
version of Scotch.

%package -n libptscotchparmetis%sover
Summary: ParMeTiS compatibility library for PT-Scotch
Group: System/Libraries
Requires: libptscotch%sover = %EVR

%description -n libptscotchparmetis%sover
Scotch is a software package and libraries for sequential and parallel graph
partitioning, static mapping, and sparse matrix block ordering, and sequential
mesh and hypergraph partitioning.

This package contains ParMeTiS compatibility library for PT-Scotch,
the parallelized version of Scotch.

%package -n lib%name-devel
Summary: Development files of Scotch
Group: Development/Other
Provides: %name-devel = %EVR
Requires: libscotch%sover = %EVR
Requires: libesmumps%sover = %EVR
Requires: libscotchmetis%sover = %EVR
Requires: libptscotch%sover = %EVR
Requires: libptesmumps%sover = %EVR
Requires: libptscotchparmetis%sover = %EVR

%description -n lib%name-devel
Scotch is a software package and libraries for sequential and parallel graph
partitioning, static mapping, and sparse matrix block ordering, and sequential
mesh and hypergraph partitioning.

This package contains development files of Scotch.

%package -n lib%name-devel-doc
Summary: Development documentation and example source code for Scotch
Group: Development/Other
BuildArch: noarch
Provides: %name-doc = %EVR

%description -n lib%name-devel-doc
Scotch is a software package and libraries for sequential and parallel graph
partitioning, static mapping, and sparse matrix block ordering, and sequential
mesh and hypergraph partitioning.

This package contains development documentation and example source code
for Scotch.

%package data
Summary: GRF and TGT files for Scotch
Group: Development/Other
BuildArch: noarch

%description data
Scotch is a software package and libraries for sequential and parallel graph
partitioning, static mapping, and sparse matrix block ordering, and sequential
mesh and hypergraph partitioning.

This package contains GRF and TGT files for Scotch.

%prep
%setup
%autopatch -p1

iconv -f windows-1252 -t utf-8 doc/CeCILL-C_V1-en.txt -o CeCILL-C_V1-en.txt

%build
mpi-selector --set %mpiimpl
source %mpidir/bin/mpivars.sh
%cmake \
	-DBUILD_SHARED_LIBS=ON \
	-DCMAKE_INSTALL_INCLUDEDIR=%_includedir/%name
%cmake_build

%install
source %mpidir/bin/mpivars.sh
%cmake_install

install -pD -m644 -t %buildroot%_datadir/%name/grf grf/*
install -pD -m644 -t %buildroot%_datadir/%name/tgt tgt/*

# fix binary file names
pushd %buildroot%_bindir
rename "" scotch_ *
popd

# fix man file names
pushd %buildroot%_man1dir
rename "" scotch_ *
sed -i 's|^.so man1/|.so man1/scotch_|' scotch_*
popd

install -pD -m644 -t %buildroot%_docdir/%name doc/*.pdf doc/scotch_example.f

%check
%if_with check
# Force intranode communication
export OMPI_MCA_plm_rsh_agent=false OMPI_MCA_btl=^tcp
%ctest
%endif

%files
%doc LICENSE_en.txt CeCILL-C_V1-en.txt
%_bindir/scotch_*
%_man1dir/scotch_*

%files -n libscotch%sover
%_libdir/libscotch.so.%sover
%_libdir/libscotch.so.%version
%_libdir/libscotcherr.so.%sover
%_libdir/libscotcherr.so.%version
%_libdir/libscotcherrexit.so.%sover
%_libdir/libscotcherrexit.so.%version

%files -n libesmumps%sover
%_libdir/libesmumps.so.%sover
%_libdir/libesmumps.so.%version

%files -n libscotchmetis%sover
%_libdir/libscotchmetisv5.so.%sover
%_libdir/libscotchmetisv5.so.%version

%files -n libptscotch%sover
%_libdir/libptscotch.so.%sover
%_libdir/libptscotch.so.%version
%_libdir/libptscotcherr.so.%sover
%_libdir/libptscotcherr.so.%version
%_libdir/libptscotcherrexit.so.%sover
%_libdir/libptscotcherrexit.so.%version

%files -n libptesmumps%sover
%_libdir/libptesmumps.so.%sover
%_libdir/libptesmumps.so.%version

%files -n libptscotchparmetis%sover
%_libdir/libptscotchparmetisv3.so.%sover
%_libdir/libptscotchparmetisv3.so.%version

%files -n lib%name-devel
%_libdir/*.so
%_includedir/%name/
%_cmakedir/%name/

%files -n lib%name-devel-doc
%_docdir/%name

%files data
%dir %_datadir/%name
%_datadir/%name/grf
%_datadir/%name/tgt

%changelog
* Wed Jun 17 2026 Valery Zabrovsky <brow@altlinux.org> 7.0.12-alt1
- New version 7.0.12.

* Tue May 12 2026 Valery Zabrovsky <brow@altlinux.org> 7.0.11-alt1
- New version 7.0.11 (Closes: 43103).
- Split libscotch into packages with optional libraries.
- Transfer to CMake build system.
- Add check section.
- Add new aliases for devel and doc packages for future rename.

* Mon Jun 23 2025 Anton Midyukov <antohami@altlinux.org> 5.1.12b-alt7.svn20110910
- NMU: add prefix 'scotch_' to name of binaries (Closes: 54343)

* Mon Jan 13 2025 Andrew A. Vasilyev <andy@altlinux.org> 5.1.12b-alt6.svn20110910
- Fix FTBFS with gcc14.

* Mon Sep 30 2024 Michael Shigorin <mike@altlinux.org> 5.1.12b-alt5.svn20110910
- Fixed 64-bit builds for non-x86.
- Minor spec cleanup.

* Thu Sep 17 2020 Grigory Ustinov <grenka@altlinux.org> 5.1.12b-alt4.svn20110910
- Fixed FTBFS.

* Fri Jun 22 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 5.1.12b-alt3.svn20110910
- Rebuilt with OpenMPI 1.6

* Sun May 20 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 5.1.12b-alt2.svn20110910
- Fixed build (thnx glebfm@)

* Sun Dec 18 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 5.1.12b-alt1.svn20110910
- Version 5.1.12b

* Wed Dec 14 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 5.1.10-alt2.svn20101209
- Fixed RPATH

* Fri May 13 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 5.1.10-alt1.svn20101209
- New snapshot
- Disabled devel-static package

* Fri Mar 18 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 5.1.10-alt1.svn20101007.2
- Added -g into compiler flags

* Thu Feb 10 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 5.1.10-alt1.svn20101007.1
- Rebuilt for debuginfo

* Mon Oct 25 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 5.1.10-alt1.svn20101007
- Version 5.1.10

* Wed Oct 13 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 5.1.6-alt1.svn20090513.1
- Fixed linking of libraries

* Mon Jul 12 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 5.1.6-alt1.svn20090513
- New snapshot

* Mon Sep 14 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 5.1.6-alt1
- Version 5.1.6

* Fri Aug 28 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 5.1.4-alt5.svn20090828
- New snapshot
- Fixed manpages
- Added shared libraries

* Tue Aug 25 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 5.1.4-alt4.2
- Removed scotch-metis libraries from pkg-config file

* Mon Aug 24 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 5.1.4-alt4.1
- Fixed pkg-config file for esmumps

* Sun Aug 23 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 5.1.4-alt4
- Added pkg-config file
- Fixed:
    + breaking strict-aliasing rules
    + format not a string literal and no format arguments

* Sun Jun 14 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 5.1.4-alt3
- Rebuild with PIC

* Wed May 13 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 5.1.4-alt2
- Rebuild with gcc 4.4 and OpenMPI
- Disable static build for executables
- Fix for x86_64

* Fri Apr 24 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 5.1.4-alt1
- Initial build for Sisyphus

