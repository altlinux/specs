%define oname petiga
%define scalar_type complex
%define ldir %_libdir/petsc-%scalar_type

%define sover 0

Name: %oname-%scalar_type
Version: 0.1
Release: alt1.hg20140708
Summary: PetIGA: A framework for high performance Isogeometric Analysis (%scalar_type scalars)
License: BSD
Group: Sciences/Mathematics
Url: https://petiga-igakit.readthedocs.org/en/latest/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# hg clone https://bitbucket.org/dalcinl/PetIGA
Source: %name-%version.tar

BuildPreReq: libpetsc-%scalar_type-devel python-module-sphinx-devel
BuildPreReq: cmake

%description
This software framework implements a NURBS-based Galerkin finite element
method (FEM), popularly known as isogeometric analysis (IGA). It is
heavily based on PETSc, the Portable, Extensible Toolkit for Scientific
Computation. PETSc is a collection of algorithms and data structures for
the solution of scientific problems, particularly those modeled by
partial differential equations (PDEs). PETSc is written to be applicable
to a range of problem sizes, including large-scale simulations where
high performance parallel is a must. PetIGA can be thought of as an
extension of PETSc, which adds the NURBS discretization capability and
the integration of forms. The PetIGA framework is intended for
researchers in the numeric solution of PDEs who have applications which
require extensive computational resources.

%package -n lib%name
Summary: PetIGA: A framework for high performance Isogeometric Analysis (%scalar_type scalars)
Group: System/Libraries

%description -n lib%name
This software framework implements a NURBS-based Galerkin finite element
method (FEM), popularly known as isogeometric analysis (IGA). It is
heavily based on PETSc, the Portable, Extensible Toolkit for Scientific
Computation. PETSc is a collection of algorithms and data structures for
the solution of scientific problems, particularly those modeled by
partial differential equations (PDEs). PETSc is written to be applicable
to a range of problem sizes, including large-scale simulations where
high performance parallel is a must. PetIGA can be thought of as an
extension of PETSc, which adds the NURBS discretization capability and
the integration of forms. The PetIGA framework is intended for
researchers in the numeric solution of PDEs who have applications which
require extensive computational resources.

%package -n lib%name-devel
Summary: Development files of PetIGA (%scalar_type scalars)
Group: Development/Other
Requires: lib%name = %EVR
Requires: libpetsc-%scalar_type-devel

%description -n lib%name-devel
This software framework implements a NURBS-based Galerkin finite element
method (FEM), popularly known as isogeometric analysis (IGA). It is
heavily based on PETSc, the Portable, Extensible Toolkit for Scientific
Computation. PETSc is a collection of algorithms and data structures for
the solution of scientific problems, particularly those modeled by
partial differential equations (PDEs). PETSc is written to be applicable
to a range of problem sizes, including large-scale simulations where
high performance parallel is a must. PetIGA can be thought of as an
extension of PETSc, which adds the NURBS discretization capability and
the integration of forms. The PetIGA framework is intended for
researchers in the numeric solution of PDEs who have applications which
require extensive computational resources.

This package contains development files of PetIGA.

%package -n %oname-docs
Summary: Documentation for PetIGA
Group: Development/Documentation
BuildArch: noarch

%description -n %oname-docs
This software framework implements a NURBS-based Galerkin finite element
method (FEM), popularly known as isogeometric analysis (IGA). It is
heavily based on PETSc, the Portable, Extensible Toolkit for Scientific
Computation. PETSc is a collection of algorithms and data structures for
the solution of scientific problems, particularly those modeled by
partial differential equations (PDEs). PETSc is written to be applicable
to a range of problem sizes, including large-scale simulations where
high performance parallel is a must. PetIGA can be thought of as an
extension of PETSc, which adds the NURBS discretization capability and
the integration of forms. The PetIGA framework is intended for
researchers in the numeric solution of PDEs who have applications which
require extensive computational resources.

This package contains development documentation for PetIGA.

%prep
%setup

%prepare_sphinx docs
ln -s ../objects.inv docs/manual/

%build
source %_bindir/petsc-%scalar_type.sh
export PETIGA_DIR=$PWD

mkdir BUILD
pushd BUILD

cmake \
%if %_lib == lib64
	-DLIB_SUFFIX=64 \
%endif
	-DCMAKE_INSTALL_PREFIX:PATH=$PETSC_DIR \
	-DCMAKE_C_FLAGS:STRING="%optflags" \
	-DCMAKE_CXX_FLAGS:STRING="%optflags" \
	-DCMAKE_Fortran_FLAGS:STRING="%optflags" \
	-DCMAKE_STRIP:FILEPATH="/bin/echo" \
	-DSOVER:STRING=%sover \
	..
%make_build VERBOSE=1

popd

%if "%scalar_type" == "real"
%make -C docs/manual html
%endif

%install
source %_bindir/petsc-%scalar_type.sh
export PETIGA_DIR=$PWD

%makeinstall_std -C BUILD

sed -i '1a\PETIGA_DIR=${PETSC_DIR}' \
	%buildroot%ldir/conf/petigavariables

%files -n lib%name
%doc *.rst
%ldir/lib/*.so.*

%files -n lib%name-devel
%ldir/include/*
%ldir/conf/*
%ldir/lib/*.so

%if "%scalar_type" == "real"
%files -n %oname-docs
%doc docs/manual/_build/html/*
%endif

%changelog
* Thu Jul 10 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1-alt1.hg20140708
- Initial build for Sisyphus

