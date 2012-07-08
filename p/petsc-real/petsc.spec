%def_without mpi4py
%def_without petsc4py
%def_with netcdf
%def_without tops

%define mpiimpl openmpi
%define mpidir %_libdir/%mpiimpl
%define pastix_sover 0
%define spooles_sover 2

%define oname petsc
%define scalar_type real
%define ldir %_libdir/%oname-%scalar_type
%if "%scalar_type" == "real"
%define alttype complex
%else
%define alttype real
%endif

%define somver 3
%define sover %somver.2.0

%define topsomver 0
%define topsover %topsomver.0.0

Name: %oname-%scalar_type
Version: 3.2_p7
Release: alt3
Summary: Portable, Extensible Toolkit for Scientific Computation (%scalar_type scalars)
License: BSD
Group: Sciences/Mathematics
Url: http://www.mcs.anl.gov/petsc/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# http://ftp.mcs.anl.gov/pub/petsc/release-snapshots/petsc-3.2-p5.tar.gz
Source: %oname-%version.tar.gz
Source1: ftp://ftp.mcs.anl.gov/pub/petsc/externalpackages/Generator.tar.gz
Source3: gen_makefile
Source4: makefile.tmpl
Source5: LICENSE.LLNL

Requires: lib%name-devel = %version-%release
Requires: python-module-%oname-config >= %version-%release
Requires: %oname-common >= %version-%release
Requires: openpdt tau mpe2
# skip 'requires' generation, because import directory calculated at runtime
%add_python_req_skip script

BuildRequires(pre): rpm-build-python
BuildPreReq: chrpath python-module-Pyro4 python-module-Scientific
BuildPreReq: %mpiimpl-devel gcc-fortran libgfortran-devel
BuildPreReq: libstdc++-devel libsz2-devel libarpack-devel
BuildPreReq: liblapack-goto-devel gcc-c++ libscalapack-devel libX11-devel
BuildPreReq: libXt-devel libsowing-devel boost-devel python-module-fiat
BuildPreReq: libparmetis-devel libblacs-devel libspooles-devel
BuildPreReq: libtetgen-devel zlib-devel libblocksolve95-devel
BuildPreReq: libtriangle-devel libsuperlu_dist-devel libsuitesparse-devel
BuildPreReq: libsuperlu-devel liby12m-devel
BuildPreReq: cproto libchaco-devel c2html
BuildPreReq: libtau-devel libmtl4-devel libmpe2-devel boost-python-devel
BuildPreReq: libplapack-devel python-devel gdb libnumpy-devel
BuildPreReq: libtrilinos10-devel python-module-Scientific-devel
%if %scalar_type == real
BuildPreReq: liboski-%scalar_type-devel
%if_with petsc4py
BuildPreReq: python-module-petsc4py-%scalar_type
%endif
BuildPreReq: libscotch-devel libmumps-devel libpastix-devel
BuildPreReq: libamesos10-devel libepetraext10-devel libteuchos10-devel
BuildPreReq: libifpack10-devel libaztecoo10-devel libepetra10-devel
BuildPreReq: libml10-devel libzoltan10-devel
BuildPreReq: ffc libhypre-devel libspai-devel libparms-devel
BuildPreReq: libblopex-devel libhdf5-mpi-devel
BuildPreReq: libexpat-devel
%if_with mpi4py
BuildPreReq: python-module-mpi4py
%endif
%if_with netcdf
BuildPreReq: libnetcdf-mpi-devel
%endif
BuildPreReq: libsundials-devel libsprng1-devel
%endif
%if %scalar_type == complex
BuildPreReq: libfftw3-mpi-devel
%endif
%if_with tops
BuildPreReq: babel ccaffeine cca-spec-classic cca-spec-babel cca-spec-neo
%endif

%description
Portable, Extensible Toolkit for Scientific Computation (PETSc) is a suite of
data structures and routines for the scalable (parallel) solution of scientific
applications modeled by partial differential equations. It employs the MPI
standard for parallelism.

For generating initial makefiles for Your programs use script named
`gen_makefile'. If You want create log file when running Your programs for event
vizualisations, use `-log_mpe [logfile]' as a parameter for Your executables.

%package -n lib%name
Summary: Shared libraries of PETSc (%scalar_type scalars)
Group: System/Libraries
Conflicts: lib%name-devel < %version-%release
Obsoletes: lib%name-devel < %version-%release
Conflicts: libslepc-%scalar_type-devel < 3.0.0_p4-alt2
Obsoletes: libslepc-%scalar_type-devel < 3.0.0_p4-alt2
Requires: libspooles
%if %scalar_type == real
Requires: libpastix
%endif

%description -n lib%name
Portable, Extensible Toolkit for Scientific Computation (PETSc) is a suite of
data structures and routines for the scalable (parallel) solution of scientific
applications modeled by partial differential equations. It employs the MPI
standard for parallelism.

This package contains shared libraries of PETSc (with %scalar_type scalar types).

%package -n lib%name-devel
Summary: Development files of PETSc (%scalar_type scalars)
Group: Development/Other
AutoReq: yes, nopython
Requires: lib%name = %version-%release
Requires: %oname-common >= %version-%release
Requires: %mpiimpl-devel gcc-fortran libgfortran-devel
Requires: libstdc++-devel libsz2-devel libarpack-devel
Requires: liblapack-goto-devel gcc-c++ libscalapack-devel libX11-devel
Requires: libXt-devel libsowing-devel boost-devel python-module-fiat
Requires: libparmetis-devel libblacs-devel libspooles-devel
Requires: libtetgen-devel zlib-devel libblocksolve95-devel
Requires: libtriangle-devel libsuperlu_dist-devel libsuitesparse-devel
Requires: libsuperlu-devel liby12m-devel
Requires: cproto libchaco-devel
Requires: libtau-devel libmtl4-devel libmpe2-devel boost-python-devel
Requires: libplapack-devel python-devel
%if %scalar_type == real
%if_with petsc4py
Requires: python-module-petsc4py-%scalar_type
%endif
Requires: libscotch-devel libmumps-devel libpastix-devel
Requires: libamesos10-devel libepetraext10-devel libteuchos10-devel
Requires: libifpack10-devel libaztecoo10-devel libepetra10-devel
Requires: libml10-devel libzoltan10-devel liboski-%scalar_type-devel
Requires: ffc libhypre-devel libspai-devel libparms-devel
Requires: libblopex-devel libhdf5-mpi-devel python-module-numpy
Requires: libexpat-devel
%if_with mpi4py
Requires: python-module-mpi4py
%endif
%if_with netcdf
Requires: libnetcdf-mpi-devel
%endif
Requires: libsundials-devel libsprng1-devel
%endif
%if %scalar_type == complex
Requires: libfftw3-mpi-devel
%endif
%if_with tops
Requires: babel ccaffeine cca-spec-classic cca-spec-babel cca-spec-neo
%endif


%description -n lib%name-devel
Portable, Extensible Toolkit for Scientific Computation (PETSc) is a suite of
data structures and routines for the scalable (parallel) solution of scientific
applications modeled by partial differential equations. It employs the MPI
standard for parallelism.

This package contains development files of PETSc (with %scalar_type
scalar types).

%package -n lib%name-devel-static
Summary: Static development files of PETSc (%scalar_type scalars)
Group: Development/Other
Requires: lib%name-devel = %version-%release
Requires: libparmetis-devel libsuitesparse-devel
Requires: libspooles-devel libsuperlu_dist-devel libsuperlu-devel
Requires: libchaco-devel libblocksolve95-devel
Requires: libmtl4-devel libparms-devel libopenpdt-devel
Requires: libmpe2-devel libscalasca-devel libplapack-devel
%if %scalar_type == real
Requires: libscotch-devel libmumps-devel libpastix-devel
Requires: libzoltan-devel libspai-devel libblopex-devel
Requires: libhypre-devel
Requires: libscalapack-devel libml10-devel
Requires: libsprng1-devel
%endif
%if %scalar_type == complex
Requires: libfftw3-mpi-devel
%endif

%description -n lib%name-devel-static
Portable, Extensible Toolkit for Scientific Computation (PETSc) is a suite of
data structures and routines for the scalable (parallel) solution of scientific
applications modeled by partial differential equations. It employs the MPI
standard for parallelism.

This package contains static development files of PETSc (with %scalar_type
scalar types).

%package -n python-module-%oname-config
Summary: Configuration system of PETSc (%scalar_type scalars)
Group: Development/Other
Requires: %oname-common = %version-%release
%py_provides petsc_config
AutoReq: yes, nopython

%description -n python-module-%oname-config
Portable, Extensible Toolkit for Scientific Computation (PETSc) is a suite of
data structures and routines for the scalable (parallel) solution of scientific
applications modeled by partial differential equations. It employs the MPI
standard for parallelism.

This package contains configuration system of PETSc (with %scalar_type scalar
types).

%package -n %oname-docs
Summary: Documentation for PETSc
Group: Development/Documentation
BuildArch: noarch

%description -n %oname-docs
Portable, Extensible Toolkit for Scientific Computation (PETSc) is a suite of
data structures and routines for the scalable (parallel) solution of scientific
applications modeled by partial differential equations. It employs the MPI
standard for parallelism.

This package contains development documentation for PETSc.

%package -n %oname-examples
Summary: Examples of PETSc
Group: Development/Tools
Requires: %oname-common = %version-%release
Requires: python-module-%oname-config = %version-%release
# skip 'requires' generation, because import directory calculated at runtime
%add_python_req_skip RDict script
AutoReq: yes, nopython

%description -n %oname-examples
Portable, Extensible Toolkit for Scientific Computation (PETSc) is a suite of
data structures and routines for the scalable (parallel) solution of scientific
applications modeled by partial differential equations. It employs the MPI
standard for parallelism.

This package contains examples of PETSc. If You want build some example, execute
command `gen_makefile NAME'.

%package -n %oname-common
Summary: Common files of PETSc (both for real and complex scalars)
Group: Development/Tools
BuildArch: noarch
Conflicts: libxforms-demos
%add_python_req_skip RDict script

%description -n %oname-common
Portable, Extensible Toolkit for Scientific Computation (PETSc) is a suite of
data structures and routines for the scalable (parallel) solution of scientific
applications modeled by partial differential equations. It employs the MPI
standard for parallelism.

This package contains common files of PETSc.

%package tops
Summary: TOPS components of PETSc (for %scalar_type scalars)
Group: Development/Tools
Requires: %name = %version-%release
Requires: %oname-tops = %version-%release
Requires: lib%name-tops = %version-%release

%description tops
Portable, Extensible Toolkit for Scientific Computation (PETSc) is a suite of
data structures and routines for the scalable (parallel) solution of scientific
applications modeled by partial differential equations. It employs the MPI
standard for parallelism.

This package provides Towards Optimal Petscale Simulations (TOPS) components
of PETSc.

%package -n lib%name-tops
Summary: Shared libraries of TOPS components of PETSc (for %scalar_type scalars)
Group: System/Libraries
Requires: lib%name = %version-%release

%description -n lib%name-tops
Portable, Extensible Toolkit for Scientific Computation (PETSc) is a suite of
data structures and routines for the scalable (parallel) solution of scientific
applications modeled by partial differential equations. It employs the MPI
standard for parallelism.

This package contains shared libraries of Towards Optimal Petscale Simulations
(TOPS) components of PETSc.

%package -n %oname-tops
Summary: Common files of TOPS components of PETSc (for %scalar_type scalars)
Group: Development/Tools

%description -n %oname-tops
Portable, Extensible Toolkit for Scientific Computation (PETSc) is a suite of
data structures and routines for the scalable (parallel) solution of scientific
applications modeled by partial differential equations. It employs the MPI
standard for parallelism.

This package contains common files of Towards Optimal Petscale Simulations
(TOPS) components of PETSc.

%package sources
Summary: Prepared sources of PETSc (for %scalar_type scalars)
Group: Development/Tools
AutoReq: yes, nopython

%description sources
Portable, Extensible Toolkit for Scientific Computation (PETSc) is a suite of
data structures and routines for the scalable (parallel) solution of scientific
applications modeled by partial differential equations. It employs the MPI
standard for parallelism.

This package contains prepared sources of PETSc.

%prep
%setup
tar -xzf %SOURCE1
rm -f Generator/.hgignore
rm -fR Generator/.hg
sed -i -e 's/^\(import\ lex\)/from fract4d \1/' Generator/exprlex.py
sed -i -e 's/^\(import\ yacc\)/from fract4d \1/' Generator/exprparse.py
sed -i 's|2\.5|%_python_version|g' tutorials/python/ex1.c
sed -i 's|/usr/lib/|%_libdir/|g' tutorials/python/ex1.c
sed -i 's|@SCALAR_TYPE@|%scalar_type|g' src/sys/utils/str.c
install %SOURCE5 .

for i in $(find ./ -name makefile) conf/rules; do
	sed -i 's|\-@|-|' $i
	sed -i 's|@\$|$|' $i
done

%install
install -d %buildroot%ldir/lib

mpi-selector --set %mpiimpl
source %_sysconfdir/profile.d/mpi-selector.sh
source %mpidir/bin/mpivars.sh
OMPI_LDFLAGS="-Wl,--as-needed,-rpath,%mpidir/lib -L%mpidir/lib -L%_libdir/oski"
export OMPI_LDFLAGS="$OMPI_LDFLAGS -lmpi_f90 -lmpi_f77"

export PETSC_DIR=$PWD
export PETSC_ARCH=linux-gnu
OPTFLAGS="%optflags %optflags_shared -DPETSC_HAVE_MPE -I$PETSC_DIR/include/sieve"
%if_with netcdf
OPTFLAGS="$OPTFLAGS -DPETSC_HAVE_NETCDF"
%endif
OPTFLAGS="$OPTFLAGS -DTETLIBRARY -I%mpidir/include/netcdf-3"
BLASLAPACK="[libxerbla.a,liblapack.so,libgoto2.so]"
MUMPS="[libcmumps.so,libdmumps.so,libsmumps.so,libzmumps.so,libmumps_common.so"
MUMPS="$MUMPS,libpord.so,libesmumps.so,libptscotch.so,libscotch.so]"
MUMPS="$MUMPS,libscotcherr.so]"
ML="[libml.so,libamesos.so,libepetraext.so,libifpack.so,libaztecoo.so"
ML="$ML,libepetra.so,libteuchos.so,liby12m.so]"
#SUNDIALS="[libsundials_cvode.so,libsundials_nvecserial.so"
SUNDIALS="[libsundials_cvode.so"
SUNDIALS="$SUNDIALS,libsundials_nvecparallel.so]"
%if_with tops
CCAS="-lcca_0_8_6_b_1.4.0-cxx -lsidlstub_cxx"
%endif

./configure \
	--prefix=%prefix \
	--with-shared-libraries \
	--with-scalar-type=%scalar_type \
	--with-alternatives=1 \
	--with-is-color-value-type=char \
	--with-fortran-interfaces=1 \
	--with-debugging=yes \
	--with-debugger=gdb \
	--ignoreCompileOutput=0 \
	--ignoreWarnings=0 \
	--search-dirs=/bin:%_bindir:%mpidir/bin \
	--with-host-cpu=%_arch \
	--with-clanguage=C++ \
	--with-timer=mpi \
	--with-mpi-dir=%mpidir \
	--with-mpi-shared=1 \
	--with-xt=1 \
	--with-sowing=1 \
	--with-sowing-dir=%prefix \
	--with-boost=1 \
	--with-boost-dir=%prefix \
	--with-c2html=1 \
	--with-c2html-dir=%prefix \
	--with-fiat=1 \
	--with-fiat-dir=%python_sitelibdir_noarch \
	--with-scientificpython-include=%python_includedir/Scientific \
	--with-scientificpython-lib=[libpython%_python_version.so] \
	--with-parmetis=1 \
	--with-parmetis-include=%mpidir/include/metis \
	--with-parmetis-lib=[libparmetis.so] \
	--with-blacs=1 \
	--with-blacs-include=%_includedir \
	--with-blacs-lib=[libblacs.so] \
	--with-scalapack=1 \
	--with-scalapack-include=%_includedir \
	--with-scalapack-lib=[libscalapack.so,libblacs.so,libarpack_LINUX.so] \
	--with-triangle=1 \
	--with-triangle-include=%_includedir/triangle \
	--with-triangle-lib=libtriangle.so \
	--with-superlu_dist=1 \
	--with-superlu_dist-include=%_includedir/superlu_dist \
	--with-superlu_dist-lib=libsuperlu_dist_2.4.so \
	--with-superlu=1 \
	--with-superlu-include=%_includedir \
	--with-superlu-lib=[libtmglib.so,libsuperlu_4.0.so] \
	--with-umfpack=1 \
	--with-umfpack-include=%_includedir/suitesparse \
	--with-umfpack-lib=[libumfpack.so,libamd.so] \
	--with-tetgen=1 \
	--with-tetgen-include=%_includedir \
	--with-tetgen-lib=[libtetgen.so] \
	--with-spooles=1 \
	--with-spooles-include=%_libdir/spooles/include \
	--with-spooles-lib=[libspoolesMPI.so,libspooles.so] \
	--with-blas-lapack-lib=$BLASLAPACK \
	--with-chaco=1 \
	--with-chaco-lib=[libchaco2.so] \
	--with-chaco-include=%_includedir \
	--with-generator=$PWD/Generator \
	--with-cproto=1 \
	--with-cproto-dir=%prefix \
	--with-blocksolve95=1 \
	--with-blocksolve95-dir=%prefix \
	--with-blocksolve95-bopt=O \
	--with-blocksolve95-arch=linux \
	--with-plapack=1 \
	--with-plapack-include=%_includedir/plapack \
	--with-plapack-lib=[libPLAPACK.so] \
	--with-mpe=1 \
	--with-mpe-include=%_includedir \
	--with-mpe-lib=[liblmpe.so,libmpe.so] \
%if %scalar_type == real
	--with-oski=1 \
	--with-oski-include=%_includedir/oski \
	--with-oski-lib=[liboski.so,liboski_Tid.so] \
	--with-parms=1 \
	--with-parms-lib=[-lparms] \
	--with-parms-include=%_includedir \
	--with-ml=1 \
	--with-ml-include=%_includedir \
	--with-ml-lib=$ML \
	--with-ffc=1 \
	--with-ffc-dir=%prefix \
	--with-hypre=1 \
	--with-hypre-include=%_includedir/hypre \
	--with-hypre-lib=[libHYPRE.so,libgomp.so] \
	--with-expat=1 \
	--with-expat-lib=[-lexpat] \
	--with-expat-include=%_includedir \
	--with-sundials=1 \
	--with-sundials-include=%_includedir/sundials-double \
	--with-sundials-lib=$SUNDIALS \
	--with-hdf5=1 \
	--with-hdf5-lib=[-lhdf5_fortran,-lhdf5,-lz] \
	--with-hdf5-include=%mpidir/include \
	--with-zoltan=1 \
	--with-zoltan-include=%_includedir \
	--with-zoltan-lib=[libzoltan.so] \
	--with-blopex=1 \
	--with-blopex-include=%_includedir/libblopex \
	--with-blopex-lib=libBLOPEX.so \
	--with-spai=1 \
	--with-spai-include=%_includedir/spai \
	--with-spai-lib=libspai.so \
	--with-numpy=1 \
	--with-numpy-dir=%prefix \
	--with-sprng=1 \
	--with-sprng-include=%_includedir/sprng1 \
	--with-sprng-lib=[libcmrg.so,liblcg64.so,liblcg.so,liblfg.so,libmlfg.so] \
%if_with mpi4py
	--with-mpi4py=1 \
	--with-mpi4py-dir=%prefix \
%endif
%if_with petsc4py
	--with-petsc4py=1 \
	--with-petsc4py-dir=%prefix \
%endif
%if_with netcdf
	--with-netcdf=1 \
	--with-netcdf-lib=[-lnetcdf_c++,-lnetcdf] \
	--with-netcdf-include=%mpidir/include/netcdf-3 \
%endif
%endif
%if %scalar_type == complex
	--with-fftw=1 \
	--with-fftw-include=%_includedir/fftw3-mpi \
	--with-fftw-lib=[libfftw3_mpi.so] \
%endif
%if %scalar_type == real
	--with-mumps=1 \
	--with-mumps-include=%_includedir \
	--with-mumps-lib=$MUMPS \
	--with-scotch=1 \
	--with-scotch-dir=%prefix \
	--with-ptscotch=1 \
	--with-ptscotch-lib=[-lesmumps,-lptscotch,-lptscotcherr] \
	--with-ptscotch-include=%_includedir \
	--with-pastix=1 \
	--with-pastix-include=%_includedir \
	--with-pastix-lib=[libpastix.so,libparmetis.so,libptscotch.so,librt.so] \
%endif
%if_with tops
	--with-babel=1 \
	--with-babel-dir=%prefix \
	--with-ccafe=1 \
	--with-ccafe-dir=%prefix \
%endif
	--CC=mpicc --CXX=mpicxx --FC=mpif90 \
	--COPTFLAGS="$OPTFLAGS" \
	--CXXOPTFLAGS="$OPTFLAGS" \
	--FOPTFLAGS="$OPTFLAGS" \
	--LIBS="-L$PWD -L%_libdir/oski -llmpe -lmpe $CCAS $DUMMY"

%ifarch x86_64
sed -i 's|%_libexecdir|%_libdir|g' conf/petscvariables
%endif

%make all SOMVER=%somver SOVER=%sover
#make alldoc LOC=$PETSC_DIR

export INSTALL_DIR=%buildroot%prefix
%make_install PETSC_DIR=$PWD PETSC_ARCH=linux-gnu \
	INSTALL_DIR=%buildroot%prefix DESTDIR=%buildroot%prefix \
	SOMVER=%somver SOVER=%sover \
	install

install -d %buildroot%_sysconfdir
install -d %buildroot%ldir/examples
install -d %buildroot%_docdir/%oname/include/adic
install -d %buildroot%_docdir/%oname/include/finclude
install -d %buildroot%_docdir/%oname/include/mpiuni
install -d %buildroot%_docdir/%oname/include/private
install -d %buildroot%_docdir/%oname/include/sieve
install -d %buildroot%_datadir/%name
install -d %buildroot%_datadir/%oname
install -d %buildroot%python_sitelibdir/%{oname}_config
install -d %buildroot%ldir/lib
install -d %buildroot%ldir/include
install -d %buildroot%ldir/python

mv %buildroot%_libexecdir/*.so* %buildroot%_libexecdir/*.a \
	%buildroot%ldir/lib/
#ln -s libpetsc.so.%sover %buildroot%ldir/lib/libpetsc.so.%somver
#ln -s libpetsc.so.%somver %buildroot%ldir/lib/libpetsc.so
mv %buildroot%_includedir/* %buildroot%ldir/include/

mv Generator %buildroot%python_sitelibdir/%{oname}_config/
rm -fR config/examples
mv config/* %buildroot%python_sitelibdir/%{oname}_config/
touch %buildroot%python_sitelibdir/%{oname}_config/__init__.py

pushd %buildroot%_bindir
rm -fR matlab win32fe
rm -f mpiexec.gmalloc mpiexec.llrun mpiexec.poe mpiexec.prun
#mv %buildroot%_bindir/hostnames.chiba %buildroot%_sysconfdir/
chmod +x parseargs.py
popd

pushd %buildroot%ldir/include
mv *.html %buildroot%_docdir/%oname/include/
for i in adic finclude mpiuni private sieve; do
	mv $i/*.html %buildroot%_docdir/%oname/include/$i/
done
#cp $PETSC_DIR/src/dm/mesh/sieve/Filter.hh sieve/
sed -i "s|$PETSC_DIR/Generator|%python_sitelibdir/%{oname}_config/Generator|g" \
	$(find -type f)
sed -i "s|$PETSC_DIR/linux-gnu/lib|%ldir/lib|g" $(find -type f)
sed -i "s|$PETSC_DIR/include|%ldir/include|g" $(find -type f)
sed -i "s|$PETSC_DIR|%_datadir/%name|g" $(find -type f)
mv makefile makefile.%oname
popd

pushd %buildroot/%prefix/conf
rm -f uninstall.py *.log
sed -i "s|$PETSC_DIR/Generator|%python_sitelibdir/%{oname}_config/Generator|g" *
sed -i "s|$PETSC_DIR/config|%python_sitelibdir/%{oname}_config|g" *
sed -i "s|$PETSC_DIR/conf|%_datadir/%name/conf|g" *
sed -i "s|$PETSC_DIR/include|%ldir/include|g" *
sed -i "s|%buildroot||g" *
sed -i "s|$PETSC_DIR|%prefix|g" *
sed -i 's|/usr/config|%python_sitelibdir/%{oname}_config|g' *
sed -i 's|/usr/conf|%_datadir/%name/conf|g' *
sed -i 's|linux\-gnu/||g' RDict.db
sed -i "s|/usr/include|%ldir/include|" variables
sed -i "83s|^\(PETSC_LIB_DIR_COMPLEX\).*|\1 = %ldir/lib|g" variables
sed -i "11s|^\(PETSC_LIB_DIR\).*|\1 = %ldir/lib|g" variables
sed -i "s|/usr/include/petscconf.h|%ldir/include/petscconf.h|g" rules
popd

mv %buildroot%prefix/conf %buildroot%_datadir/%name/
ln -s %_datadir/%name/conf %buildroot%ldir
ln -s %ldir/lib %buildroot%_datadir/%name
ln -s %ldir/include %buildroot%_datadir/%name

mkdir doc
cp docs/copyright.html doc/
mv *.html docs tutorials %buildroot%_docdir/%oname/
%if %scalar_type == real
pushd src
rm -fR contrib/semiLagrange
for i in $(find ./ -name examples); do
	install -d %buildroot%ldir/examples/$i
	cp -fR $i/* %buildroot%ldir/examples/$i/
done
popd
%endif

install -p -m755 %SOURCE3 %buildroot%_bindir
install -p -m644 %SOURCE4 %buildroot%_datadir/%oname

cat <<EOF >%buildroot%_bindir/%name.sh
source %mpidir/bin/mpivars.sh
export PETSC_DIR=%ldir
export PETSC_LDIR=%ldir
export PETSC_LIB_DIR=%ldir/lib
export PETSC_SCALAR_TYPE=%scalar_type
export PETSC_CONFIG_DIR=%ldir/python/%{oname}_config
export TAU_MAKEFILE=$(rpm -ql libtau-common|grep Makefile)
export SLEPC_DIR=%ldir
PATH="\`echo \$PATH|sed 's|:%_libexecdir/%oname-%alttype/bin||g'\`"
PATH="\`echo \$PATH|sed 's|:%_libdir/%oname-%alttype/bin||g'\`"
PATH="\`echo \$PATH|sed 's|:%ldir/bin||g'\`"
export PATH="\$PATH:%ldir/bin"
PYPATH="\`echo \$PYTHONPATH|sed 's|:%_libexecdir/%oname-%alttype/python||g'\`"
PYPATH="\`echo \$PYTHONPATH|sed 's|:%_libdir/%oname-%alttype/python||g'\`"
PYPATH="\`echo \$PYPATH|sed 's|:%python_sitelibdir/%oname-%alttype/python||g'\`"
PYPATH="\`echo \$PYPATH|sed 's|:%ldir/python||g'\`"
PYPATH="\`echo \$PYPATH|sed 's|:%python_sitelibdir/%oname-%scalar_type/python||g'\`"
export PYTHONPATH="\$PYPATH:%ldir/python"
EOF
chmod +x %buildroot%_bindir/%name.sh

install -d %buildroot%_pkgconfigdir
cat <<EOF >%buildroot%_pkgconfigdir/%name.pc
prefix=%prefix
exec_prefix=%prefix
libdir=%ldir/lib
includedir=%ldir/include
pyexecdir=%ldir/python

Name: %name
Description: Portable, Extensible Toolkit for Scientific Computation (%scalar_type scalars)
Version: %version
Libs: -L%ldir/lib -lpetsc -Wl,-R%mpidir/lib:%ldir/lib
Cflags: -I%mpidir/include -I%ldir/include
EOF

ln -s %name.sh %buildroot%_bindir/slepc-%scalar_type.sh
ln -s %python_sitelibdir/petsc_config %buildroot%ldir/python

# TOPS

%if_with tops
#mv %buildroot%_libexecdir/tops/*/*.a \
#	%buildroot%_libexecdir/tops/*/*.so.%topsover \
#	%buildroot%ldir/lib/

install -d %buildroot%_datadir/%oname/tops
rm -fR src/tops/server
pushd src/tops/utils
install -p -m755 genSCLCCA* generateClientMakefile.sh \
	%buildroot%_bindir
rm -f genSCLCCA* generateClientMakefile.sh
popd
cp -fR src/tops %buildroot%_datadir/%oname/tops/
%endif

# fix RPATH

pushd %buildroot%ldir/lib
chrpath -r \
	%ldir/lib:%mpidir/lib \
	lib%oname.so.%sover
ln -s lib%oname.so.%sover lib%oname.so.%somver
ln -s lib%oname.so.%somver lib%oname.so
#if_with tops
#for i in topsclient-c topsclient-cxx
#do
#	if [ -f lib$i.so.%topsover ]; then
#		chrpath -r %ldir/lib:%mpidir/lib lib$i.so.%topsover
#		ln -s lib$i.so.%topsover lib$i.so.%topsomver
#		ln -s lib$i.so.%topsomver lib$i.so
#	fi
#done
#endif
popd

rm -f $(find ./ -name '*.o') \
	$(find ./ -name '*.a') \
	$(find ./ -name '*.so*') \
	$(find ./ -name '*.html'|egrep -v copyright)
install -d %buildroot%ldir/sources
cp -fR src include %buildroot%ldir/sources/

#chmod +x %buildroot%_bindir/matio.py

mv %buildroot%_bindir/pythonscripts/* \
	%buildroot%_bindir/pythonscripts ||:
rm -fR %buildroot%_bindir/pythonscripts

sed -i 's|^\(PETSC_FC_INCLUDES.*\)|\1 -I%ldir/include|' \
	%buildroot%_datadir/%name/conf/petscvariables
sed -i 's|^\(PETSC_CC_INCLUDES.*\)|\1 -I%ldir/include|' \
	%buildroot%_datadir/%name/conf/petscvariables

%files

%files -n lib%name
%doc doc/copyright.html
%doc LICENSE.LLNL
%dir %ldir
%dir %ldir/lib
%dir %ldir/python
%ldir/lib/*.so.*
%_bindir/%name.sh
%_bindir/slepc-%scalar_type.sh

%files -n lib%name-devel
%ldir/include
%ldir/lib/*.so
%_datadir/%name
%ldir/conf
%_pkgconfigdir/*

#files -n lib%name-devel-static
#ldir/lib/*.a

%if_with tops
%files tops

%files -n lib%name-tops
%ldir/libtops*.so.*
%endif

%if %scalar_type == real
%files -n %oname-common
#_sysconfdir/hostnames.chiba
%_bindir/*
%exclude %_bindir/%name.sh
%exclude %_bindir/slepc-%scalar_type.sh
%_datadir/%oname
%if_with tops
%exclude %_bindir/TOPS*
%exclude %_datadir/%oname/tops
%dir %_libexecdir/cca
%_libexecdir/cca/*
%endif

%if_with tops
%files -n %oname-tops
%_bindir/TOPS*
%_bindir/genSCLCCA*
%_bindir/generateClientMakefile.sh
%_datadir/%oname/tops
%endif

%files -n %oname-docs
%_docdir/%oname

%files -n python-module-%oname-config
%python_sitelibdir/*
%ldir/python/petsc_config

%files -n %oname-examples
%dir %ldir
%ldir/examples
%exclude %ldir/examples/tops
%endif

%files sources
%ldir/sources

%changelog
* Fri Jul 06 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.2_p7-alt3
- Changed native directory: %%_libexecdir/%name -> %%_libdir/%name

* Tue Jun 26 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.2_p7-alt2
- Rebuilt with OpenMPI 1.6

* Fri Jun 01 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.2_p7-alt1
- Version 3.2-p7

* Sat Mar 31 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.2_p6-alt2
- Rebuilt with OpenPDT instead of pdtoolkit

* Tue Feb 21 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.2_p6-alt1
- Version 3.2-p6

* Sun Dec 04 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.2_p5-alt1
- Version 3.2-p5

* Thu Dec 01 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.1_p8-alt7
- Rebuilt with chaco 2.2-alt7

* Sat Oct 22 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 3.1_p8-alt6.1
- Rebuild with Python-2.7

* Mon Sep 19 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.1_p8-alt6
- Rebuilt with parmetis 4.0

* Thu Sep 08 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.1_p8-alt5
- Rebuilt with libhdf5-7-mpi

* Wed May 04 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.1_p8-alt4
- Rebuilt with pastix 3184
- Built with OSKI library

* Mon Apr 25 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.1_p8-alt3
- Built with NetCDF

* Fri Apr 15 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.1_p8-alt2
- Rebuilt

* Sun Apr 10 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.1_p8-alt1
- Version 3.1-p8

* Sun Apr 10 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.1_p5-alt8
- Built with GotoBLAS2 instead of ATLAS
- Disabled devel-static package

* Wed Mar 23 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.1_p5-alt7
- Rebuilt with shared libftw3-mpi

* Fri Mar 11 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.1_p5-alt6
- Rebuilt with numpy 2.0.0-alt1.svn20100607.7

* Sat Mar 05 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.1_p5-alt5
- Rebuilt for debuginfo

* Sat Feb 19 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.1_p5-alt4
- Fixed build

* Fri Dec 17 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.1_p5-alt3
- Added %ldir/bin into PATH environment variable

* Mon Nov 22 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.1_p5-alt2
- Fixed checking of pARMS

* Sun Nov 14 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.1_p5-alt1
- Version 3.1-p5

* Wed Nov 03 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.1_p4-alt6
- Rebuilt for soname set-versions

* Tue Oct 26 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.1_p4-alt5
- Rebuilt with new pastix

* Fri Oct 15 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.1_p4-alt4
- Fixed overlinking of libraries

* Tue Aug 31 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.1_p4-alt3
- Fixed for checkbashisms

* Wed Aug 11 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.1_p4-alt2
- chmod +x /usr/bin/matio.py

* Mon Aug 09 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.1_p4-alt1
- Version 3.1-p4

* Thu Aug 05 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.1_p3-alt1
- Version 3.1-p3

* Tue Jul 06 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.0.0_p10-alt4
- Rebuilt with reformed ParMetis

* Fri Jun 18 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.0.0_p10-alt3
- Rebuilt with superlu_dist 2.4

* Wed Dec 23 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.0.0_p10-alt2
- Rebuilt with SuperLU 4.0

* Wed Dec 16 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.0.0_p10-alt0.M51.1
- Port for branch 5.1

* Tue Dec 08 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.0.0_p10-alt1
- Version 3.0.0-p10

* Sun Dec 06 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.0.0_p8-alt5
- Rebuilt with Trilinos v10

* Fri Nov 13 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.0.0_p8-alt4
- Rebuilt with python 2.6

* Thu Nov 05 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.0.0_p8-alt3
- Rebuild with trilinos-9.0.3-alt10

* Sun Sep 20 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.0.0_p8-alt2
- Added necessary requirements for devel package

* Thu Sep 10 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.0.0_p8-alt1
- Version 3.0.0_p8

* Tue Sep 08 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.0.0_p7-alt6
- Rebuilt with shared libraries of all requirements
- Enabled build with SPRNG

* Tue Aug 18 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.0.0_p7-alt5
- Rebuild with shared libraries of ScaLAPACK and ML
- Build with petsc4py
- Added package with prepared sources

* Thu Jul 23 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.0.0_p7-alt4
- Rebuild with python 2.6

* Sun Jul 19 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.0.0_p7-alt3.3
- Link with libpetscdummy (for complex scalars)

* Sat Jul 18 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.0.0_p7-alt3.2
- Corrected %_bindir/%name.sh for PYTHONPATH

* Sat Jul 18 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.0.0_p7-alt3.1
- Drop requirement on lib%name-%scalar_type for config module

* Sat Jul 18 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.0.0_p7-alt3
- Integrated startup commands for all client packages in %_bindir/%name.sh
- Moved %_bindir/%name.sh into lib%name package

* Fri Jul 17 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.0.0_p7-alt2
- Redefined PETSC_DIR: /usr/share/petsc-%scalar_type -> /usr/lib/petsc-%scalar_type
- Added necessary libraries requirements for devel package
- Created pkg-config file
- Moved examples into /usr/lib/petsc-%scalar_type

* Tue Jul 14 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.0.0_p7-alt1
- Version 3.0.0_p7

* Sun Jul 12 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.0.0_p6-alt2
- Fixed include directory in $PETSC_DIR/conf files
- Added links to development files into $PETSC_DIR

* Wed Jun 24 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.0.0_p6-alt1
- Initial build for Sisyphus
