%define _unpackaged_files_terminate_build 1

%define mpiimpl openmpi
%define mpidir %_libdir/%mpiimpl

%global soname_version 5.3

Name: mumps
Version: 5.3.5
Release: alt3

Summary: MUltifrontal Massively Parallel sparse direct Solver
License: ALT-Public-Domain
Group: Sciences/Mathematics

Url: http://mumps.enseeiht.fr/

# http://mumps.enseeiht.fr/MUMPS_%{version}.tar.gz
Source: MUMPS_%version.tar

# Custom Makefile changed for Fedora and built from Make.inc/Makefile.gfortran.PAR in the source.
Source1: MUMPS-Makefile.par.inc

# Custom Makefile changed for Fedora and built from Make.inc/Makefile.gfortran.SEQ in the source.
Source2: MUMPS-Makefile.seq.inc

# These patches create static and shared versions of pord, sequential and mumps libraries
# They are changed for Fedora and  derive from patches for Debian on 
# http://bazaar.launchpad.net/~ubuntu-branches/ubuntu/raring/mumps/raring/files/head:/debian/patches/
Patch0: MUMPS-examples-mpilibs.patch
Patch1: MUMPS-shared-pord.patch
Patch2: MUMPS-shared.patch
Patch3: MUMPS-shared-seq.patch

Patch100: MUMPS-alt-build.patch

BuildRequires: %mpiimpl-devel libopenblas-devel
BuildRequires: libscotch-devel libparmetis-devel
BuildRequires: libscalapack-devel
BuildRequires: libmetis-devel
BuildRequires: libgomp-devel

%description
MUMPS solves a sparse system of linear equations A x = b
using Gaussian elimination. Please read the README file and
the documentation for a complete list of functionalities.
Documentation and publications related to
MUMPS can also be found at http://mumps.enseeiht.fr/
or at http://graal.ens-lyon.fr/MUMPS

%package -n lib%name-headers
Summary: Headers for MUMPS
Group: Development/Other
BuildArch: noarch

%description -n lib%name-headers
MUMPS solves a sparse system of linear equations A x = b
using Gaussian elimination.

This package contains headers for MUMPS.

%package -n lib%name
Summary: Shared libraries of MUMPS
Group: System/Libraries

%description -n lib%name
MUMPS solves a sparse system of linear equations A x = b
using Gaussian elimination.

This package contains shared libraries of MUMPS.

%package -n lib%name-devel
Summary: Development files of MUMPS
Group: Development/Other
Requires: lib%name-headers = %EVR
Requires: lib%name = %EVR

%description -n lib%name-devel
MUMPS solves a sparse system of linear equations A x = b
using Gaussian elimination.

This package contains development files of MUMPS.

%package -n lib%name-seq
Summary: Shared libraries of MUMPS (sequential version)
Group: System/Libraries

%description -n lib%name-seq
MUMPS solves a sparse system of linear equations A x = b
using Gaussian elimination.

This package contains shared libraries of MUMPS (sequential version).

%package -n lib%name-seq-devel
Summary: Development files of MUMPS (sequential version)
Group: Development/Other
Requires: lib%name-headers = %EVR
Requires: lib%name = %EVR
Conflicts: lib%name-devel < %EVR
Obsoletes: lib%name-devel < %EVR

%description -n lib%name-seq-devel
MUMPS solves a sparse system of linear equations A x = b
using Gaussian elimination.

This package contains development files of MUMPS (sequential version).

%package -n lib%name-examples
Summary: Examples for MUMPS
Group: Development/Other

%description -n lib%name-examples
MUMPS solves a sparse system of linear equations A x = b
using Gaussian elimination.

This package contains examples for MUMPS.

%package -n lib%name-seq-examples
Summary: Examples for MUMPS (sequential version)
Group: Development/Other

%description -n lib%name-seq-examples
MUMPS solves a sparse system of linear equations A x = b
using Gaussian elimination.

This package contains examples for MUMPS (sequential version).

%prep
%setup
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch100 -p2

mv examples/README examples/README-examples

%ifarch %e2k
# openmp troubles as of lcc 1.26.16
sed -i '/^!\$/d' src/{{s,d,z,c}sol_{distrhs,c},zsol_{lr,fwd_aux},csol_lr}.F
%endif

pushd ..
cp -r %name-%version %name-%version-seq
popd

pushd ../%name-%version-seq
%patch3 -p2
popd

%build
%ifarch %e2k
%define build_fflags %optflags
%else
# Workaround for GCC-10
# https://gcc.gnu.org/gcc-10/porting_to.html
%define build_fflags %optflags -fallow-argument-mismatch
%endif

%define mpif77_cflags %(env PKG_CONFIG_PATH=%mpidir/lib/pkgconfig pkg-config --cflags ompi-f77)
%define mpif77_libs %(env PKG_CONFIG_PATH=%mpidir/lib/pkgconfig pkg-config --libs ompi-f77)
%define mpifort_cflags %(env PKG_CONFIG_PATH=%mpidir/lib/pkgconfig pkg-config --cflags ompi-fort)
%define mpifort_libs %(env PKG_CONFIG_PATH=%mpidir/lib/pkgconfig pkg-config --libs ompi-fort)
%define mpic_libs %(env PKG_CONFIG_PATH=%mpidir/lib/pkgconfig pkg-config --libs ompi)

mpi-selector --yes --set %mpiimpl
source %mpidir/bin/mpivars.sh
export OMPI_LDFLAGS="-Wl,--as-needed,-rpath,%mpidir/lib -L%mpidir/lib"
export MPIDIR=%mpidir

cp -f %{SOURCE1} Makefile.inc

# -DBLR_MT needs OpenMP
sed -e "s| -DBLR_MT||g" -i Makefile.inc

# Set build flags macro
sed -e "s|@@FFLAGS@@|%{build_fflags} -Dscotch -Dmetis -Dptscotch -DWITHOUT_PTHREAD -DINTSIZE32|g" -i Makefile.inc
sed -e "s|@@CFLAGS@@|%optflags -Dscotch -Dmetis -Dptscotch -DWITHOUT_PTHREAD -DINTSIZE32|g" -i Makefile.inc
sed -e "s|@@LDFLAGS@@|${OMPI_LDFLAGS}|g" -i Makefile.inc
sed -e "s|@@MPICLIB@@|-lmpi|g" -i Makefile.inc
sed -e "s|@@MPIFORTRANLIB@@|${OMPI_LDFLAGS} %{mpif77_libs}|g" -i Makefile.inc

MUMPS_MPI=openmpi
MUMPS_INCDIR=-I%mpidir/include
LMETISDIR=%{_libdir}
IMETIS="-I%mpidir/include/metis"
LMETIS="-L%{_libdir} -lmetis"
SCOTCHDIR=%mpidir/lib
ISCOTCH=-I%_includedir
LSCOTCH=" -L%mpidir/lib -lesmumps -lscotch -lscotcherr -lptscotch -lptscotcherr"
IPORD=" -I$PWD/PORD/include/"
LPORD=" -L$PWD/PORD/lib -lpord"

export MPIBLACSLIBS=""
export MPI_COMPILER_NAME=openmpi
export LD_LIBRARY_PATH="%mpidir/lib:%_libdir"
export LDFLAGS="${OMPI_LDFLAGS}"

export LIBBLAS="-L%_libdir -lopenblas"
export INCBLAS=-I%_includedir/openblas

%make_build all \
	SONAME_VERSION=%{soname_version} \
	CC=%mpidir/bin/mpicc \
	FC=%mpidir/bin/mpif77 \
	FL=%mpidir/bin/mpif77 \
	MUMPS_MPI="$MUMPS_MPI" \
	MUMPS_INCDIR="$MUMPS_INCDIR $INCBLAS" \
	MUMPS_LIBF77="${LIBBLAS} -L%mpidir -Wl,-rpath -Wl,%mpidir %{mpic_libs} $MPIFORTRANSLIB -lscalapack -llapack $MPIBLACSLIBS" \
	LMETISDIR="$LMETISDIR" LMETIS="$LMETIS" \
	IMETIS="$IMETIS" \
	SCOTCHDIR=$SCOTCHDIR \
	ISCOTCH=$ISCOTCH \
	LSCOTCH="$LSCOTCH" \
	IPORD="$IPORD" \
	LPORD="$LPORD" \
	OPTL="${OMPI_LDFLAGS}" \
	%nil

mkdir -p %name-%version-%mpiimpl/lib
mkdir -p %name-%version-%mpiimpl/examples
mkdir -p %name-%version-%mpiimpl/modules

cp -pr lib/* %name-%version-%mpiimpl/lib
cp -pr examples/* %name-%version-%mpiimpl/examples
cp -a include %name-%version-%mpiimpl/
cp -pr src/*.mod %name-%version-%mpiimpl/modules

pushd ../%name-%version-seq
cp -f %{SOURCE2} Makefile.inc

# Set build flags macro
sed -e "s|@@CFLAGS@@|%optflags -fopenmp -Dscotch -Dmetis -DWITHOUT_PTHREAD -DINTSIZE32|g" -i Makefile.inc
sed -e "s|@@FFLAGS@@|%{build_fflags} -fopenmp -Dscotch -Dmetis -DWITHOUT_PTHREAD -DINTSIZE32|g" -i Makefile.inc
sed -e "s|@@LDFLAGS@@|-fopenmp -lgomp -lrt|g" -i Makefile.inc

IPORD=" -I$PWD/PORD/include/"
LPORD=" -L$PWD/PORD/lib -lpord_seq"
IMETIS="-I%_includedir/metis"

export LIBBLAS="-L%_libdir -lopenblas"
export INCBLAS=-I%_includedir/openblas
export LDFLAGS="-fopenmp -lgomp -lrt"

%make_build all \
	SONAME_VERSION=%{soname_version} \
	CC=gcc \
	FC=gfortran \
	FL=gfortran \
	MUMPS_LIBF77="${LIBBLAS} -llapack" \
	LIBBLAS="${LIBBLAS}" \
	LIBOTHERS=" " \
	LIBSEQ="-L../libseq -lmpiseq" \
	INCSEQ="-I../libseq $INCBLAS" \
	LMETISDIR=%_libdir \
	IMETIS="$IMETIS" \
	LMETIS="-L%_libdir -lmetis" \
	SCOTCHDIR=%_prefix \
	ISCOTCH="-I%_includedir" \
	LSCOTCH=" -L%_libdir -lesmumps -lscotch -lscotcherr -lscotchmetis" \
	IPORD="$IPORD" \
	LPORD="$LPORD" \
	OPTL="-fopenmp -lrt" \
	%nil

make -C examples

mkdir -p %name-%version-seq/lib
mkdir -p %name-%version-seq/examples
mkdir -p %name-%version-seq/modules

cp -pr lib/* %name-%version-seq/lib
cp -pr examples/* %name-%version-seq/examples
cp -a include %name-%version-seq/
cp -pr src/*.mod %name-%version-seq/modules
popd

%install
mkdir -p %buildroot%_libdir
mkdir -p %buildroot%_libdir/%name-%version-%mpiimpl-examples
mkdir -p %buildroot%_libdir/%name-%version-seq-examples
mkdir -p %buildroot%_includedir/%name

### install common files
install -cpm 644 %name-%version-%mpiimpl/include/*.h %buildroot%_includedir/%name/
install -cpm 644 PORD/include/* %buildroot%_includedir/%name/
install -cpm 644 %name-%version-%mpiimpl/modules/* %buildroot%_includedir/%name/

### install mpi version
source %mpidir/bin/mpivars.sh
export OMPI_LDFLAGS="-Wl,--as-needed,-rpath,%mpidir/lib -L%mpidir/lib"

# Install libraries.
install -cpm 755 %name-%version-%mpiimpl/lib/lib*-*.so %buildroot%_libdir/

# Install development files.
cp -a %name-%version-%mpiimpl/lib/lib*.so %buildroot%_libdir/

install -cpm 755 %name-%version-%mpiimpl/examples/?simpletest %buildroot%_libdir/%name-%version-%mpiimpl-examples/
install -cpm 755 %name-%version-%mpiimpl/examples/input_* %buildroot%_libdir/%name-%version-%mpiimpl-examples/
install -cpm 755 %name-%version-%mpiimpl/examples/README-* %buildroot%_libdir/%name-%version-%mpiimpl-examples/

### install seq version
pushd ../%name-%version-seq

# Install libraries.
install -cpm 755 %name-%version-seq/lib/lib*-*.so %buildroot%_libdir/

# Install development files.
cp -a %name-%version-seq/lib/lib*.so %buildroot%_libdir/

install -cpm 755 %name-%version-seq/examples/?simpletest %buildroot%_libdir/%name-%version-seq-examples/
install -cpm 755 %name-%version-seq/examples/input_* %buildroot%_libdir/%name-%version-seq-examples/
install -cpm 755 %name-%version-seq/examples/README-* %buildroot%_libdir/%name-%version-seq-examples/

popd

%check
# Running test programs
pushd ../%name-%version-seq/examples
LD_LIBRARY_PATH=$PWD:../lib:$LD_LIBRARY_PATH \
 ./ssimpletest < input_simpletest_real
LD_LIBRARY_PATH=$PWD:../lib:$LD_LIBRARY_PATH \
 ./dsimpletest < input_simpletest_real
LD_LIBRARY_PATH=$PWD:../lib:$LD_LIBRARY_PATH \
 ./csimpletest < input_simpletest_cmplx
LD_LIBRARY_PATH=$PWD:../lib:$LD_LIBRARY_PATH \
 ./zsimpletest < input_simpletest_cmplx
LD_LIBRARY_PATH=$PWD:../lib:$LD_LIBRARY_PATH \
 ./c_example
popd

%files -n lib%name-headers
%_includedir/*

%files -n lib%name
%doc LICENSE
%doc ChangeLog CREDITS README
%_libdir/*-%{soname_version}.so
%exclude %_libdir/*_seq-%{soname_version}.so
%exclude %_libdir/libmpiseq-%{soname_version}.so

%files -n lib%name-devel
%_libdir/*.so
%exclude %_libdir/*-%{soname_version}.so
%exclude %_libdir/*_seq.so
%exclude %_libdir/libmpiseq.so

%files -n lib%name-seq
%doc LICENSE
%doc ChangeLog CREDITS README
%_libdir/*_seq-%{soname_version}.so
%_libdir/libmpiseq-%{soname_version}.so

%files -n lib%name-seq-devel
%_libdir/*_seq.so
%_libdir/libmpiseq.so

%files -n lib%name-examples
%_libdir/%name-%version-%mpiimpl-examples

%files -n lib%name-seq-examples
%_libdir/%name-%version-seq-examples

%changelog
* Mon Apr 17 2023 Michael Shigorin <mike@altlinux.org> 5.3.5-alt3
- E2K: ftbfs workarounds (ICE; ilyakurdyukov@)
- enable parallel build (ilyakurdyukov@)

* Fri Jul 23 2021 Michael Shigorin <mike@altlinux.org> 5.3.5-alt2
- E2K: avoid lcc-unsupported option
  (it's not gcc10 to work around in the first place...)

* Wed Apr 21 2021 Aleksei Nikiforov <darktemplar@altlinux.org> 5.3.5-alt1
- Updated to upstream version 5.3.5 by adapting spec and patches from Fedora.

* Fri Sep 18 2020 Aleksei Nikiforov <darktemplar@altlinux.org> 4.10.0-alt11
- Updated conflicts and obsoletes.

* Fri Jul 05 2019 Sergey V Turchin <zerg@altlinux.org> 4.10.0-alt10
- build without arpack

* Thu Dec 27 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 4.10.0-alt9
- Updated interpackage dependencies and build architectures.

* Mon Nov 20 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 4.10.0-alt8
- Fixed build.

* Tue Jul 23 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.10.0-alt7
- Fixed build

* Sun Aug 12 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.10.0-alt6
- Built with OpenBLAS instead of GotoBLAS2

* Sun Jun 24 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.10.0-alt5
- Rebuilt with OpenMPI 1.6

* Mon May 21 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.10.0-alt4
- Fixed build

* Wed Dec 14 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.10.0-alt3
- Fixed RPATH

* Tue Sep 13 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.10.0-alt2
- Rebuilt with parmetis 4.0

* Fri Sep 09 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.10.0-alt1
- Version 4.10.0

* Fri Apr 08 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.9.2-alt7
- Rebuilt with GotoBLAS2 1.13-alt3

* Thu Apr 07 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.9.2-alt6
- Built with GotoBLAS instead of ATLAS

* Sat Feb 26 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.9.2-alt5
- Rebuilt with parmetis 3.1.1-alt10

* Thu Feb 10 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.9.2-alt4
- Rebuilt for debuginfo

* Wed Oct 13 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.9.2-alt3
- Fixed overlinking of libraries

* Tue Jul 06 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.9.2-alt2
- Rebuilt with reformed ParMetis

* Thu Jun 17 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.9.2-alt1
- Version 4.9.2

* Sat Aug 29 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.8.4-alt3
- Added shared libraries

* Sun Jun 14 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.8.4-alt2
- Rebuild with PIC

* Wed May 27 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.8.4-alt1
- Initial build for Sisyphus

