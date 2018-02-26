%define mpiimpl openmpi
%define mpidir %_libdir/%mpiimpl
%define seqdir %_libdir/hdf5-seq
%define seqmpi seq
%define oname cgns
%if "%seqmpi" == "seq"
%define altname %oname-mpi
%define desc sequential
%else
%define altname %oname-seq
%define desc parallel
%endif
%define longdesc The CFD General Notation System (CGNS) provides a general, portable, and \
extensible standard for the storage and retrieval of computational fluid \
dynamics (CFD) analysis data. It consists of a collection of \
conventions, and free and open software implementing those conventions. \
It is self-descriptive, machine-independent, well-documented, and \
administered by an international steering committee. It is also an \
American Institute of Aeronautics and Astronautics (AIAA) Recommended \
Practice.

Name: %oname-%seqmpi
Version: 3.1.3
Release: alt2.svn20111216
Summary: CFD General Notation System (%desc version)

Group: Sciences/Mathematics
License: Free (see license.txt)
URL: http://cgns.sourceforge.net/
# https://cgns.svn.sourceforge.net/svnroot/cgns
Source: %oname-%version.tar
Source1: CMakeCache.txt
Source2: CGNS_docs.tar
Source3: UserGuideCode.tar
Source4: F77_examples.tar
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Provides: %oname = %version-%release
Requires: lib%name = %version-%release
Requires: %oname-data = %version-%release
Conflicts: %altname

BuildPreReq: cmake gcc-c++ gcc-fortran zlib-devel libGL-devel tk-devel
BuildPreReq: libGLU-devel xorg-xproto-devel libXmu-devel libXtst-devel
BuildPreReq: libXcomposite-devel libXcursor-devel libXdamage-devel
BuildPreReq: libXdmcp-devel libXfixes-devel libXft-devel libXi-devel
BuildPreReq: libXpm-devel libXrandr-devel libXrender-devel libXv-devel
BuildPreReq: libXxf86misc-devel libXinerama-devel libXxf86vm-devel
%if "%seqmpi" == "seq"
BuildPreReq: libhdf5-devel
%else
BuildPreReq: libhdf5-mpi-devel libsz2-devel %mpiimpl-devel chrpath
%endif

%description
%longdesc

The system consists of two parts: (1) a standard format for recording
the data, and (2) software that reads, writes, and modifies data in that
format. The format is a conceptual entity established by the
documentation; the software is a physical product supplied to enable
developers to access and produce data recorded in that format.

%package -n lib%name
Summary: Shared libraries of CFD General Notation System (%desc version)
Group: System/Libraries
Provides: lib%oname = %version-%release
%if "%seqmpi" == "seq"
Requires: libhdf5
%else
Requires: libhdf5-mpi
%endif
Conflicts: lib%altname

%description -n lib%name
%longdesc

This package contains shared libraries of CGNS.

%package -n lib%name-devel
Summary: Development files of CFD General Notation System (%desc version)
Group: Development/C++
Requires: lib%name = %version-%release
%if "%seqmpi" == "seq"
Requires: libhdf5-devel
%else
Requires: libhdf5-mpi-devel
%endif
Conflicts: lib%altname-devel

%description -n lib%name-devel
%longdesc

This package contains development files of CGNS.

%package -n %oname-data
Summary: Architecture independent files of CFD General Notation System (%desc version)
Group: Sciences/Mathematics
BuildArch: noarch

%description -n %oname-data
%longdesc

This package contains architecture independent files of CGNS.

%package -n %oname-devel-doc
Summary: Documentation for CFD General Notation System (%desc version)
Group: Development/Documentation
BuildArch: noarch

%description -n %oname-devel-doc
%longdesc

This package contains development documentation for CGNS.

%prep
%setup
install %SOURCE1 .
%if "%seqmpi" == "seq"
sed -i 's|@CXX@|g++|' CMakeCache.txt
sed -i 's|@CC@|gcc|' CMakeCache.txt
sed -i 's|@FC@|f95|' CMakeCache.txt
sed -i 's|@HDF5@|%seqdir|' CMakeCache.txt
sed -i 's|@MPI@|OFF|' CMakeCache.txt
%else
sed -i 's|@CXX@|mpicxx|' CMakeCache.txt
sed -i 's|@CC@|mpicc|' CMakeCache.txt
sed -i 's|@FC@|mpif90|' CMakeCache.txt
sed -i 's|@HDF5@|%mpidir|' CMakeCache.txt
sed -i 's|@MPI@|ON|' CMakeCache.txt
%endif

tar -xf %SOURCE2
tar -xf %SOURCE3
tar -xf %SOURCE4

%build
%if "%seqmpi" == "mpi"
mpi-selector --set %mpiimpl
source %mpidir/bin/mpivars.sh
export OMPI_LDFLAGS="-Wl,--as-needed,-rpath,%mpidir/lib -L%mpidir/lib"
FLAGS="-I%mpidir/include"
%else
FLAGS="-I%seqdir/include"
%endif

FLAGS="%optflags %optflags_shared $FLAGS"
cmake \
%ifarch x86_64
	-DENABLE_64BIT:BOOL=ON \
%endif
	-DCMAKE_C_FLAGS:STRING="$FLAGS" \
	-DCMAKE_CXX_FLAGS:STRING="$FLAGS" \
	-DCMAKE_Fortran_FLAGS:STRING="$FLAGS" \
	.
%make_build

%install
%if "%seqmpi" == "mpi"
source %mpidir/bin/mpivars.sh
export OMPI_LDFLAGS="-Wl,--as-needed,-rpath,%mpidir/lib -L%mpidir/lib"
%endif

%makeinstall_std

%ifarch x86_64
install -d %buildroot%_libdir
mv %buildroot%_libexecdir/* %buildroot%_libdir/
%endif

%if "%seqmpi" == "mpi"
for i in $(find %buildroot%_bindir -type f) \
	$(find %buildroot%_libdir -name '*.so.*')
do
	FTYPE=$(file $i |sed 's|.*\(ELF\).*|\1|')
	if [ "$FTYPE" = "ELF" ]; then
		chrpath -r %mpidir/lib $i
	fi
done
%endif

install -p -m644 src/cgnsKeywords.h %buildroot%_includedir

mv %buildroot%_bindir/cgnstools/* %buildroot%_bindir/
rmdir %buildroot%_bindir/cgnstools

# The package contains a CVS/.svn/.git/.hg/.bzr/_MTN directory of revision control system.
# It was most likely included by accident since CVS/.svn/.hg/... etc. directories 
# usually don't belong in releases. 
# When packaging a CVS/SVN snapshot, export from CVS/SVN rather than use a checkout.
find $RPM_BUILD_ROOT -type d \( -name 'CVS' -o -name '.svn' -o -name '.git' -o -name '.hg' -o -name '.bzr' -o -name '_MTN' \) -print -exec rm -rf {} \; ||:
# the find below is useful in case those CVS/.svn/.git/.hg/.bzr/_MTN directory is added as %%doc
find . -type d \( -name 'CVS' -o -name '.svn' -o -name '.git' -o -name '.hg' -o -name '.bzr' -o -name '_MTN' \) -print -exec rm -rf {} \; ||:

%files
%doc license.txt
%_bindir/*

%files -n lib%name
%_libdir/*.so.*

%files -n lib%name-devel
%_libdir/*.so
%_includedir/*

%if "%seqmpi" == "seq"
%files -n %oname-data
%_datadir/cgnstools

%files -n %oname-devel-doc
#doc doc/html/*
%doc CGNS_docs UserGuideCode F77_examples
%endif

%changelog
* Mon Jun 25 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.1.3-alt2.svn20111216
- Rebuilt

* Fri Dec 16 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.1.3-alt1.svn20111216
- New snapshot

* Wed Sep 07 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.1.3-alt1.svn20110816.1
- Rebuilt with libhdf5-7

* Sat Aug 20 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.1.3-alt1.svn20110816
- New snapshot

* Mon May 09 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.1.3-alt1.svn20110503
- Version 3.1.3
- Disabled devel-static package

* Tue Mar 01 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.0.8-alt1.svn20100525.4
- Rebuilt for debuginfo

* Tue Nov 02 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.0.8-alt1.svn20100525.3
- Rebuilt for soname set-versions

* Wed Oct 13 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.0.8-alt1.svn20100525.2
- Fixed overlinking of libraries

* Mon Jun 21 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.0.8-alt1.svn20100525.1
- Added missing %_includedir/cgnsKeywords.h

* Fri Jun 18 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.0.8-alt1.svn20100525
- Version 3.0.8

* Thu Oct 15 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.0.7-alt1.svn20091009
- Initial build for Sisyphus

