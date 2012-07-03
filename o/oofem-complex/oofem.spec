%define mpiimpl openmpi
%define mpidir %_libexecdir/%mpiimpl

%define scalar_type complex
%define ldir %_libexecdir/petsc-%scalar_type

%define somver 0
%define sover %somver.2.2
%define oname oofem
Name: oofem-%scalar_type
Version: 2.2
Release: alt3.svn20111202
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
BuildPreReq: libparmetis-devel libhdf5-mpi-devel libSM-devel
BuildPreReq: libneXtaw-devel libXext-devel doxygen graphviz latex2html
%if "%scalar_type" == "real"
BuildPreReq: libimlxx-devel
%endif
BuildPreReq: libtrilinos10-devel chrpath

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
BuildArch: noarch
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
BuildArch: noarch
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
sed -i 's|@SOMVER@|%somver|g' */src/Makefile.in base/main_makefile.in
sed -i 's|@SOVER@|%sover|g' */src/Makefile.in base/main_makefile.in
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
export OMPI_LDFLAGS="-Wl,--as-needed,-Rpath=%mpidir/lib:%ldir/lib -L%mpidir/lib -L%ldir/lib"

export PETSC_INCLUDE=$PETSC_DIR/include
export SLEPC_LIB="-lslepc"
%if "%scalar_type" == "complex"
COMPLEX_FLAGS="-fno-strict-aliasing"
%endif
FLAGS="-I$PETSC_INCLUDE -I%_includedir/boost -I%mpidir/include/metis"
FLAGS="$FLAGS -I$PWD/targets/default/include -DBOOST_PYTHON"
%add_optflags %optflags_shared $FLAGS $COMPLEX_FLAGS
TOP=$PWD

mkdir -p targets/default/include
cp -f base/oofemdef.h.in targets/default/include/

# function for build main package

function buildIt() {
	%configure $3 $4 \
		--with-CKITDIR=$PWD/Ckit \
		--with-ELIXIRDIR=$PWD/Elixir \
		--with-MPIDIR=%mpidir \
		--with-x \
%if "%scalar_type" == "real"
		--enable-iml \
		--with-IMLDIR=%_includedir \
%endif
		--enable-petsc \
		--enable-slepc \
		--with-PETSCDIR=$PETSC_DIR \
		--enable-parmetis \
		--with-PARMETISDIR=%prefix \
		--enable-dss \
		--enable-sm \
		--enable-tm \
		--enable-fm \
		OOFEM_TARGET=$1 \
		CPPFLAGS="-I$TOP/Ckit/include -I$TOP/Elixir/include -I../default/include -g" \
		LIBS="-L$TOP/Ckit/src -L$TOP/Elixir/src"
	if [ "$NO_BUILD" = "" ]; then
		pushd targets/default
		export LIBNAME=lib$2
		if [ "$1" = "default" ]; then
			%make_build SOVER=%sover SOMVER=%somver
		else
			%make_build SOVER=%sover SOMVER=%somver OOFEM_TARGET=$1
		fi 
		rm -f $(find ./ -name '*.o')
		if [ "$1" != "default" ]; then
			cp -f include/* ../$1/include/
		fi
		popd
	fi
}

# prepare

mkdir -p targets/default/include
mkdir -p targets/oofem-release/include
mkdir -p targets/poofem-release/include
mkdir objs
sed -i "s|(PWD)|$PWD|g" configure.in
%autoreconf

NO_BUILD=1
buildIt default poofem --enable-poofem
NO_BUILD=

# create necessary objects

function buildCommon() {
	mpicxx -g %optflags %optflags_shared -I../src/oofemlib \
		-I../src/oofemlib/xfem -I%ldir/include -I../src/sm \
		-I../src/tm -I../src/fm -I../Elixir/include \
		-I../Ckit/include -I../targets/default/include \
		-I../src/oofemlib/iga -I../src/tm/cemhyd \
		-I../src/tm/cemhyd/tinyxml \
		-D__SM_MODULE -D__TM_MODULE -D__FM_MODULE \
		-D__USE_MPI -D__PETSC_MODULE $1 -c *.C
}

pushd objs
cp ../src/main/* ./
cp -f %SOURCE3 ./
rm -f maindebug.C
mkdir tmp

# parallel
buildCommon -D__PARALLEL_MODE
for i in $(ls *.o); do
	mv $i tmp/poofem-$i
done
# sequential
buildCommon
for i in $(ls *.o); do
	mv $i tmp/oofem-$i
done
# graphical
buildCommon -D__OOFEG
for i in $(ls *.o); do
	mv $i tmp/oofeg-$i
done

mv tmp/* ./
rmdir tmp
mv oofeg-oofeg.o oofeg.o

popd

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
%make_build
popd

# main build

buildIt poofem-release poofem --enable-poofem
buildIt oofem-release oofem
buildIt default oofeg --enable-oofeg --enable-oofeg-devel-interface

# need relink libesi & libelixir

pushd Elixir/src
rm -f libesi.*
%make_build OOFEG_LIB="-L../../targets/default -loofeg"
rm -f libelixir.*
%make_build OOFEG_LIB="-L../../targets/default -loofeg" ESI_LIB=-lesi
popd

%install

install -d %buildroot%ldir/bin
install -d %buildroot%_libdir
install -d %buildroot%ldir/lib
install -d %buildroot%ldir/include/Ckit
install -d %buildroot%ldir/include/Elixir

install -m755 targets/default/bin/* %buildroot%ldir/bin
cp -P Ckit/src/*.so* Elixir/src/*.so* \
	%buildroot%ldir/lib
cp -P targets/default/*.so* %buildroot%ldir/lib/
chmod -x %buildroot%ldir/lib/*
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

%files
%doc ChangeLog gpl.txt README
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
