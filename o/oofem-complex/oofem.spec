%define mpiimpl openmpi
%define mpidir %_libdir/%mpiimpl

%define scalar_type complex
%define ldir %_libdir/petsc-%scalar_type

%define somver 0
%define sover %somver.2.2
%define oname oofem
Name: oofem-%scalar_type
Version: 2.4.0
Release: alt1.git20140703.1
Summary: Object Oriented Finite Element Code
License: %gpl2plus
Group: Sciences/Mathematics
Url: http://www.oofem.org/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# http://www.oofem.org/svn/trunk
Source: %oname-%version.tar.gz
#Source1: http://www.oofem.org/download/ckit.tar.gz
#Source2: http://www.oofem.org/download/elixir.tar.gz
Source3: main.C

Requires: lib%name = %version-%release

BuildRequires(pre): rpm-build-licenses
BuildPreReq: python-devel boost-python-devel libparpack-mpi-devel
BuildPreReq: %mpiimpl-devel gcc-c++ libslepc-%scalar_type-devel
BuildPreReq: libX11-devel libXt-devel libICE-devel libXaw-devel libXmu-devel
BuildPreReq: libparmetis-devel libhdf5-mpi-devel libSM-devel libdakota-devel
BuildPreReq: libneXtaw-devel libXext-devel doxygen graphviz latex2html
%if "%scalar_type" == "real"
BuildPreReq: libimlxx-devel
%endif
BuildPreReq: libtrilinos10-devel chrpath cmake
BuildPreReq: libtinyxml2-devel liblapack-devel
BuildPreReq: libvtk-devel vtk-examples vtk-python
BuildPreReq: boost-python-devel

%description
OOFEM is free finite element code with object oriented architecture for
solving mechanical, transport and fluid mechanics problems that operates on
various platforms.

The aim of this project is to develop efficient and robust tool for FEM
computations as well as to provide modular and extensible environment for
future development.

%package -n lib%name
Summary: Shared libraries of Object Oriented Finite Element Code
Group: System/Libraries
Requires: libpetsc-%scalar_type

%description -n lib%name
OOFEM is free finite element code with object oriented architecture for
solving mechanical, transport and fluid mechanics problems that operates on
various platforms.

The aim of this project is to develop efficient and robust tool for FEM
computations as well as to provide modular and extensible environment for
future development.

This package contains shared libraries of OOFEM.

%package -n lib%name-devel
Summary: Shared libraries of Object Oriented Finite Element Code
Group: Development/C++
Requires: lib%name = %version-%release
Requires: libpetsc-%scalar_type-devel

%description -n lib%name-devel
OOFEM is free finite element code with object oriented architecture for
solving mechanical, transport and fluid mechanics problems that operates on
various platforms.

The aim of this project is to develop efficient and robust tool for FEM
computations as well as to provide modular and extensible environment for
future development.

This package contains development files of OOFEM.

%package -n %oname-doc
Summary: User's and developer's documentation for OOFEM
Group: Documentation
BuildArch: noarch

%description -n %oname-doc
OOFEM is free finite element code with object oriented architecture for
solving mechanical, transport and fluid mechanics problems that operates on
various platforms.

The aim of this project is to develop efficient and robust tool for FEM
computations as well as to provide modular and extensible environment for
future development.

This package contains user's and developer's documentation for OOFEM.

%package -n %oname-tests
Summary: Tests for OOFEM
Group: Sciences/Mathematics
BuildArch: noarch

%description -n %oname-tests
OOFEM is free finite element code with object oriented architecture for
solving mechanical, transport and fluid mechanics problems that operates on
various platforms.

The aim of this project is to develop efficient and robust tool for FEM
computations as well as to provide modular and extensible environment for
future development.

This package contains tests for OOFEM.

%package -n libckit-%scalar_type
Summary: Shared library of C Programmer's Toolbox
Group: System/Libraries
Provides: libckit = %version-%release

%description -n libckit-%scalar_type
This is a C-language toolkit (Ckit), which consists of a number of
useful packages. These are made into a single support library. The
core of the Ckit is a list processing package (formerly C-toolkit) by
Robert A Zimmermann. It helped to build programs faster and more
comfortably.

%package -n libckit-%scalar_type-devel
Summary: Development files of C Programmer's Toolbox
Group: Development/C
Provides: libckit-devel = %version-%release
Requires: libckit-%scalar_type = %version-%release

%description -n libckit-%scalar_type-devel
This is a C-language toolkit (Ckit), which consists of a number of
useful packages. These are made into a single support library. The
core of the Ckit is a list processing package (formerly C-toolkit) by
Robert A Zimmermann. It helped to build programs faster and more
comfortably.

This package contains development files of C Programmer's Toolbox.

%package -n libckit-devel-doc
Summary: Documentation for C Programmer's Toolbox
Group: Development/Documentation
BuildArch: noarch

%description -n libckit-devel-doc
This is a C-language toolkit (Ckit), which consists of a number of
useful packages. These are made into a single support library. The
core of the Ckit is a list processing package (formerly C-toolkit) by
Robert A Zimmermann. It helped to build programs faster and more
comfortably.

This package contains development documentation for C Programmer's
Toolbox.

%package -n libelixir-%scalar_type
Summary: Extension LIbrary of X-based Interactive gRaphics
Group: System/Libraries
Provides: libelixir = %version-%release
Requires: libckit-%scalar_type = %version-%release

%description -n libelixir-%scalar_type
ELIXIR is a set of utilities enabling the programmer to interactively
display and manipulate three-dimensional graphic entities within
multiple windows on a monitor screen.

%package -n libelixir-%scalar_type-devel
Summary: Development files of Extension LIbrary of X-based Interactive gRaphics
Group: Development/C
Provides: libelixir-devel = %version-%release
Requires: libelixir-%scalar_type = %version-%release
Requires: libckit-%scalar_type-devel = %version-%release

%description -n libelixir-%scalar_type-devel
ELIXIR is a set of utilities enabling the programmer to interactively
display and manipulate three-dimensional graphic entities within
multiple windows on a monitor screen.

This package contains development files of ELIXIR.

%package -n libelixir-devel-doc
Summary: Documentation for Extension LIbrary of X-based Interactive gRaphics
Group: Development/Documentation
BuildArch: noarch

%description -n libelixir-devel-doc
ELIXIR is a set of utilities enabling the programmer to interactively
display and manipulate three-dimensional graphic entities within
multiple windows on a monitor screen.

This package contains development documentation for ELIXIR.

%prep
%setup
sed -i 's|@SOMVER@|%somver|g' */src/Makefile.in
sed -i 's|@SOVER@|%sover|g' */src/Makefile.in
%if "%scalar_type" == "real"
pushd doc
tar -cf ../docs.tar $(find ./ -name '*.pdf')
popd
%endif
pushd src
tar -cf ../incs.tar $(find ./ -name '*.h')
popd

%build
mpi-selector --set %mpiimpl
source /usr/bin/petsc-%scalar_type.sh
export OMPI_LDFLAGS="-Wl,--as-needed,-rpath,%mpidir/lib:%ldir/lib -L%mpidir/lib -L%ldir/lib"
export MPIDIR=%mpidir

#export PETSC_INCLUDE=$PETSC_DIR/include
#export SLEPC_LIB="-lslepc"
%if "%scalar_type" == "complex"
COMPLEX_FLAGS="-fno-strict-aliasing"
%endif
FLAGS="-I$PETSC_INCLUDE -I%_includedir/boost -I%mpidir/include/metis"
FLAGS="$FLAGS -I$PWD/targets/default/include -I$PWD/src/oofemlib"
FLAGS="$FLAGS -I%_includedir/python%_python_version -DBOOST_PYTHON"
%add_optflags %optflags_shared $FLAGS $COMPLEX_FLAGS -fpermissive
TOP=$PWD

# build necessary libraries

pushd Ckit/src
%autoreconf
%configure
%make_build
popd

pushd Elixir/src
%autoreconf
%configure \
	--with-x \
	CPPFLAGS="-I$TOP/Ckit/include" \
	LIBS="-L$TOP/Ckit/src"
%make
popd

cmake \
%if %_lib == lib64
	-DLIB_SUFFIX=64 \
%endif
	-DCMAKE_INSTALL_PREFIX:PATH=%ldir \
	-DCMAKE_C_FLAGS:STRING="%optflags" \
	-DCMAKE_CXX_FLAGS:STRING="%optflags" \
	-DCMAKE_Fortran_FLAGS:STRING="%optflags" \
	-DCMAKE_STRIP:FILEPATH="/bin/echo" \
	-DSCALAR_TYPE:STRING=%scalar_type \
	-DSOMVER:STRING=%somver \
	-DSOVER:STRING=%sover \
	-DBLAS_LIBRARIES:STRING="openblas" \
	-DLAPACK_LIBRARIES:STRING="lapack" \
	-DCKIT_DIR:PATH="$PWD/Ckit" \
	-DELIXIR_DIR:PATH="$PWD/Elixir" \
	-DMETIS_DIR:PATH="%prefix" \
	-DMPI_DIR:PATH="%mpidir" \
	-DMY_PETSC_DIR:PATH="$PETSC_DIR" \
	-DPARMETIS_DIR:PATH="%prefix" \
	-DSLEPC_DIR:PATH="$PETSC_DIR" \
	-DSPOOLES_DIR:PATH="%_libdir/spooles" \
	-DTINYXML2_DIR:PATH="%prefix" \
	-DVTK_DIR:PATH="%prefix" \
	-DUSE_CEMHYD:BOOL=ON \
	-DUSE_DSS:BOOL=ON \
	-DUSE_LAPACK:BOOL=ON \
	-DUSE_OOFEG:BOOL=ON \
	-DUSE_PARALLEL:BOOL=ON \
	-DUSE_METIS:BOOL=ON \
	-DUSE_PARMETIS:BOOL=ON \
	-DUSE_PETSC:BOOL=ON \
	-DUSE_PYTHON:BOOL=ON \
	-DUSE_PYTHON_BINDINGS:BOOL=ON \
	-DUSE_SLEPC:BOOL=ON \
	-DUSE_SPOOLES:BOOL=OFF \
	-DUSE_TRIANGLE:BOOL=OFF \
	-DUSE_TINYXML:BOOL=ON \
	-DUSE_VTK:BOOL=ON \
%if "%scalar_type" == "real"
	-DUSE_IML:BOOL=ON \
%endif
	.

%make_build VERBOSE=1

# need relink libesi & libelixir

pushd Elixir/src
rm -f libesi.*
%make_build OOFEG_LIB="-L$TOP -loofem $TOP/CMakeFiles/oofem.dir/src/main/main.C.o"
rm -f libelixir.*
%make_build OOFEG_LIB="-L$TOP -loofem $TOP/CMakeFiles/oofem.dir/src/main/main.C.o" \
	ESI_LIB=-lesi
popd

%install
source /usr/bin/petsc-%scalar_type.sh
export OMPI_LDFLAGS="-Wl,--as-needed,-rpath,%mpidir/lib:%ldir/lib -L%mpidir/lib -L%ldir/lib"
export MPIDIR=%mpidir

%makeinstall_std

install -d %buildroot%ldir/bin
install -d %buildroot%_libdir
install -d %buildroot%ldir/lib
install -d %buildroot%ldir/include/Ckit
install -d %buildroot%ldir/include/Elixir

#install -m755 targets/default/bin/* %buildroot%ldir/bin
cp -P Ckit/src/*.so* Elixir/src/*.so* \
	%buildroot%ldir/lib/
#cp -P targets/default/*.so* %buildroot%ldir/lib/
cp -fP liboofem.so* %buildroot%ldir/lib/
cp -fP oofe? %buildroot%ldir/bin/
#chmod -x %buildroot%ldir/lib/*
install -p -m644 Ckit/include/*.h %buildroot%ldir/include/Ckit
install -p -m644 Elixir/include/*.h %buildroot%ldir/include/Elixir
pushd %buildroot%ldir/include
tar -xf $OLDPWD/incs.tar
popd

# tests & docs

%if "%scalar_type" == "real"
install -d %buildroot%_datadir/%oname
cp -fR tests %buildroot%_datadir/%oname/

install -d %buildroot%_docdir/%oname
install -d %buildroot%_docdir/Ckit
install -d %buildroot%_docdir/Elixir
install -p -m644 Ckit/docs/* %buildroot%_docdir/Ckit
install -p -m644 Elixir/doc/* %buildroot%_docdir/Elixir
pushd %buildroot%_docdir/%oname
tar -xf $OLDPWD/docs.tar
popd
%endif

cp Ckit/README README.Ckit
cp Elixir/README README.Elixir

# fix rpath

for i in %buildroot%ldir/lib/*.so %buildroot%ldir/bin/*
do
	chrpath -r %ldir/lib:%mpidir/lib $i
done

#cp Ckit/README README.Ckit
#cp Elixir/README README.Elixir

%files
%doc ChangeLog README
%ldir/bin/*

%files -n lib%name
%ldir/lib/*.so.*
%exclude %ldir/lib/libckit.so.*
%exclude %ldir/lib/libelixir.so.*
%exclude %ldir/lib/libesi.so.*

%files -n lib%name-devel
%ldir/lib/*.so
%exclude %ldir/lib/libckit.so
%exclude %ldir/lib/libelixir.so
%exclude %ldir/lib/libesi.so
%ldir/include/*
%exclude %ldir/include/Ckit
%exclude %ldir/include/Elixir

%files -n libckit-%scalar_type
%doc Ckit/README
%ldir/lib/libckit.so.*

%files -n libckit-%scalar_type-devel
%ldir/lib/libckit.so
%ldir/include/Ckit

%files -n libelixir-%scalar_type
%doc Elixir/README
%ldir/lib/libelixir.so.*
%ldir/lib/libesi.so.*

%files -n libelixir-%scalar_type-devel
%ldir/lib/libelixir.so
%ldir/lib/libesi.so
%ldir/include/Elixir

%if "%scalar_type" == "real"
%files -n %oname-doc
%_docdir/%oname

%files -n %oname-tests
%dir %_datadir/%oname
%_datadir/%oname/tests

%files -n libckit-devel-doc
%_docdir/Ckit

%files -n libelixir-devel-doc
%_docdir/Elixir
%endif

%changelog
* Sat Jan 03 2015 Ivan A. Melnikov <iv@altlinux.org> 2.4.0-alt1.git20140703.1
- rebuild with boost 1.57.0

* Mon Jul 07 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.4.0-alt1.git20140703
- New snapshot

* Fri Jun 06 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.4.0-alt1.git20140529
- Version 2.4.0

* Thu Jul 11 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.2-alt7.svn20121029
- Rebuilt with new PETSc

* Tue May 07 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.2-alt6.svn20121029
- Fixed build

* Wed Feb 06 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.2-alt5.svn20121029
- New snapshot

* Wed Sep 19 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.2-alt5.svn20120918
- New snapshot

* Mon Aug 13 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.2-alt5.svn20111202
- Rebuilt with PETSc 3.3

* Sat Jul 07 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.2-alt4.svn20111202
- Rebuilt with OpenMPI 1.6

* Mon May 21 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.2-alt3.svn20111202
- Fixed build

* Fri Dec 16 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.2-alt2.svn20111202
- Fixed RPATH

* Fri Dec 09 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.2-alt1.svn20111202
- Version 2.2

* Mon Sep 19 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.0-alt1.svn20110511.1
- Rebuilt with parmetis 4.0

* Fri May 13 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.0-alt1.svn20110511
- New snapshot

* Sat Mar 12 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.0-alt1.svn20101117.2
- Rebuilt for debuginfo

* Thu Mar 10 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.0-alt1.svn20101117.1
- Fixed build

* Sat Nov 20 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.0-alt1.svn20101117
- New snapshot

* Tue Nov 02 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.0-alt1.svn20100727.3
- Rebuilt for soname set-versions

* Fri Oct 15 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.0-alt1.svn20100727.2
- Fixed linking

* Tue Aug 10 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.0-alt1.svn20100727.1
- Set libckit-%scalar_type-devel and libelixir-%scalar_type-devel as
  noarch

* Mon Aug 09 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.0-alt1.svn20100727
- New snapshot
- Rebuilt with PETSc 3.1

* Fri Jul 02 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.0-alt1.svn20100623.2
- Set Elixir and Ckit as scalar type dependent

* Thu Jul 01 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.0-alt1.svn20100623.1
- Set lib%name-devel as noarch package

* Thu Jul 01 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.0-alt1.svn20100623
- New snapshot

* Thu Dec 17 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.0-alt1.svn20091001.1
- Rebuilt with Trilinos v10

* Sun Oct 11 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.0-alt1.svn20091001
- Initial build for Sisyphus
