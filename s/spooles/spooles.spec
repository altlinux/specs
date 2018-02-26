%define mpiimpl openmpi
%define mpidir %_libdir/%mpiimpl

%define somver 2
%define sover %somver.2.0
Name: spooles
Version: 2.2
Release: alt11
Summary: SParse Object Oriented Linear Equations Solver
License: Free
Group: Sciences/Mathematics
Url: http://www.netlib.org/linalg/spooles/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name.%version.tar.gz
Source1: http://www.netlib.org/linalg/spooles/AllInOne.ps.gz
Source2: http://www.netlib.org/linalg/spooles/Eigen.ps.gz
Source3: http://www.netlib.org/linalg/spooles/LinSol.ps.gz
Source4: http://www.netlib.org/linalg/spooles/Ordering.ps.gz
Source5: http://www.netlib.org/linalg/spooles/PP99.ps.gz
Source6: http://www.netlib.org/linalg/spooles/ReferenceManual.ps.gz

Requires: %name-common = %version-%release

BuildPreReq: %mpiimpl-devel

%description
SPOOLES is a library for solving sparse real and complex linear systems of
equations, written in the C language using object oriented design. At present,
there is the following functionality:

1. Compute multiple minimum degree, generalized nested dissection and
multisection orderings of matrices with symmetric structure.

2. Factor and solve square linear systems of equations with symmetric structure,
with or without pivoting for stability. The factorization can be symmetric LDLT,
Hermitian LDLH, or nonsymmetric LDU. A direct factorization or a drop tolerance
factorization can be computed. The factors and solve can be done in serial mode,
multithreaded with Solaris or POSIX threads, or with MPI.

3. Factor and solve overdetermined full rank systems of equations using a
multifrontal QR factorization, in serial or using POSIX threads.

4. Solve square linear systems using a variety of Krylov iterative methods. The
preconditioner is a drop tolerance factorization, constructed with or without
pivoting for stability.

%package common
Summary: Common files of SPOOLES
Group: Sciences/Mathematics

%description common
SPOOLES is a library for solving sparse real and complex linear systems of
equations, written in the C language using object oriented design.

This package contains common files of SPOOLES.

%package -n lib%name-devel-doc
Summary: Documentation for SPOOLES
Group: Development/Documentation
BuildArch: noarch

%description  -n lib%name-devel-doc
SPOOLES is a library for solving sparse real and complex linear systems of
equations, written in the C language using object oriented design.

This package contains development documentation for SPOOLES.

%package -n lib%name
Summary: Shared libraries of SPOOLES
Group: System/Libraries

%description  -n lib%name
SPOOLES is a library for solving sparse real and complex linear systems of
equations, written in the C language using object oriented design.

This package contains shared libraries of SPOOLES.

%package -n lib%name-devel
Summary: Devepopment files of SPOOLES
Group: Development/C
Requires: %name-common = %version-%release
Requires: lib%name = %version-%release
Conflicts: lib%name-devel < %version-%release
Obsoletes: lib%name-devel < %version-%release

%description  -n lib%name-devel
SPOOLES is a library for solving sparse real and complex linear systems of
equations, written in the C language using object oriented design.

This package contains development files of SPOOLES.

%package -n lib%name-devel-static
Summary: Static libraries of SPOOLES
Group: Development/C
Requires: lib%name-devel = %version-%release
Conflicts: lib%name-devel < %version-%release

%description  -n lib%name-devel-static
SPOOLES is a library for solving sparse real and complex linear systems of
equations, written in the C language using object oriented design.

This package contains static libraries of SPOOLES.

%prep
%setup

for i in $(egrep -R '%_libexecdir/spooles' spooles/ |awk -F : '{print $1}')
do
	sed -i 's|%_libexecdir/spooles|%_libdir/spooles|g' $i
done

%build
mpi-selector --set %mpiimpl
source %mpidir/bin/mpivars.sh
export OMPI_LDFLAGS="-Wl,--as-needed,-R,%mpidir/lib -L%mpidir/lib"

%make_build MPIDIR=%mpidir lib
pushd MT
%make_build MPIDIR=%mpidir lib
popd
pushd MPI
%make_build MPIDIR=%mpidir lib
popd

%make_build MPIDIR=%mpidir ADDPARAM="-Wl,-R%mpidir/lib"
pushd MT
%make_build MPIDIR=%mpidir ADDPARAM="-Wl,-R%mpidir/lib"
popd
pushd MPI
%make_build MPIDIR=%mpidir ADDPARAM="-Wl,-R%mpidir/lib"
popd

for i in Eigen/srcMPI Eigen/srcMT Eigen/srcST Eigen/drivers IVL/drivers/ \
	Iter/src Iter/drivers LinSol/srcMPI LinSol/srcMT LinSol/srcST
do
	pushd $i
	%make MPIDIR=%mpidir ADDPARAM="-Wl,-R%mpidir/lib"
	popd
done

%install
source %mpidir/bin/mpivars.sh
export OMPI_LDFLAGS="-Wl,--as-needed,-R,%mpidir/lib -L%mpidir/lib"

install -d %buildroot%_libdir/%name/bin
install -d %buildroot%_libdir
install -d %buildroot%_libdir/%name/lib/eigen
install -d %buildroot%_libdir/%name/lib/iter
install -d %buildroot%_libdir/%name/lib/linsol
install -d %buildroot%_libdir/%name/include
install -d %buildroot%_docdir/%name
install -d %buildroot%_datadir/%name

mv DSTree/drivers/cutoff.dvf %buildroot%_datadir/%name/
mv Eigen/drivers/*.inp %buildroot%_datadir/%name/
mv MPI/drivers/*.pg %buildroot%_datadir/%name/
mv MPI/drivers/*.input %buildroot%_datadir/%name/
mv MT/drivers/*.input %buildroot%_datadir/%name/
mv misc/drivers/*.input %buildroot%_datadir/%name/
mv SubMtx/drivers/temp* %buildroot%_datadir/%name/
mv Matrices %buildroot%_datadir/%name/

for i in A2 BPG Chv Coords DSTree DV Drand EGraph ETree FrontMtx GPart \
	Graph I2Ohash ILUMtx IV IVL InpMtx Iter MPI MSMD MT Perm SemiImplMtx SubMtx \
	SymbFac Tree Utilities ZV misc
do
	rm -f $i/drivers/makefile $i/drivers/*.o $i/drivers/*.c
	install -m755 $i/drivers/* %buildroot%_libdir/%name/bin
done

install -m644 *.a MT/src/*.a MPI/src/*.a %buildroot%_libdir/%name/lib
install -m644 *.h %buildroot%_libdir/%name/include
for i in Eigen Iter LinSol MPI Utilities SubMtxManager Pencil Drand \
	PatchAndGoInfo MSMD ILUMtx DenseMtx A2 Lock EGraph I2Ohash Ideq FrontMtx \
	ChvManager Network DV IIheap Graph IVL BKL Tree ZV InpMtx BPG MT SubMtx \
	SolveMap IV Coords GPart SubMtxList SymbFac SemiImplMtx Chv ChvList ETree \
	misc DSTree Perm
do
	install -d %buildroot%_libdir/%name/include/$i
	install -m644 $i/*.h %buildroot%_libdir/%name/include/$i
done

install -p -m644 %SOURCE1 %SOURCE2 %SOURCE3 %SOURCE4 %SOURCE5 %SOURCE6 \
	LinSol/doc/wrappers.ps.gz documentation/PP99/ASHCRAFC.ps.gz \
	%buildroot%_docdir/%name

install -m644 $(find Eigen -name '*.a') %buildroot%_libdir/%name/lib/eigen
install -m644 $(find Iter -name '*.a') %buildroot%_libdir/%name/lib/iter
install -m644 $(find LinSol -name '*.a') \
	%buildroot%_libdir/%name/lib/linsol

for i in %name %{name}MPI %{name}MT; do
	ln -s $i.a %buildroot%_libdir/%name/lib/lib$i.a
done

# shared libraries

pushd %buildroot%_libdir/%name/lib
mkdir tmp
pushd tmp
for i in spooles spoolesMT spoolesMPI; do
	ar x ../lib$i.a
	if [ "$i" == "spoolesMT" ]; then
		PTH=-lpthread
	else
		PTH=
	fi
	mpicc -shared * -L.. $ADDLIB $PTH \
		-Wl,-R%mpidir/lib \
		-Wl,-soname,lib$i.so.%somver -o %buildroot%_libdir/lib$i.so.%sover
	ln -s lib$i.so.%sover %buildroot%_libdir/lib$i.so.%somver
	ln -s lib$i.so.%somver %buildroot%_libdir/lib$i.so
	rm -f *
	ADDLIB="-lspooles"
done
popd
rmdir tmp
popd

%files
%doc %name.%version.html
%_libdir/%name/bin

%files common
%dir %_libdir/%name
%_datadir/%name

%files -n lib%name-devel-doc
%_docdir/%name

%files -n lib%name
%dir %_libdir/%name
%dir %_libdir/%name/lib
%_libdir/*.so.*

%files -n lib%name-devel
%_libdir/%name/include
%_libdir/*.so

%files -n lib%name-devel-static
%_libdir/%name/lib/*.a
%_libdir/%name/lib/eigen
%_libdir/%name/lib/iter
%_libdir/%name/lib/linsol

%changelog
* Fri Jun 22 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.2-alt11
- Rebuilt with OpenMPI 1.6
- Set native directory as %_libdir/%name instead of %_libexecdir/%name

* Wed Dec 14 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.2-alt10
- Fixed RPATH

* Fri Mar 04 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.2-alt9
- Moved shared libraries into %_libdir
- Added -g for compiler flags

* Fri Feb 11 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.2-alt8
- Rebuilt for debuginfo

* Mon Oct 18 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.2-alt7
- Fixed overlinking

* Sat Aug 29 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.2-alt6
- Added shared libraries

* Sat Jun 13 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.2-alt5
- Removed runtime linking with unexistent LANCZOS libraries

* Fri Jun 05 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.2-alt4
- Fix paths to example data in scripts

* Sun May 31 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.2-alt3
- add links libspooles*.a -> spooles*.a

* Wed May 27 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.2-alt2
- Add missing headers

* Mon May 18 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.2-alt0.M50.1
- Port for Branch 5.0

* Sat May 16 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.2-alt1
- Initial build for Sisyphus

