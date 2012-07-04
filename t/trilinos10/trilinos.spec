%def_with dakota
%def_without petsc
%define mpiimpl openmpi
%define mpidir %_libdir/%mpiimpl

%define longdesc The Trilinos Project is an effort to develop and implement \
robust algorithms and enabling technologies using modern object-oriented \
software design, while still leveraging the value of established libraries \
such as PETSc, Metis/ParMetis, SuperLU, Aztec, the BLAS and LAPACK. It \
emphasizes abstract interfaces for maximum flexibility of component \
interchanging, and provides a full-featured set of concrete classes that \
implement all abstract interfaces.

%define somver 10
%define sover %somver.10.0
%define scalar_type real
%define ldir %_libdir/petsc-%scalar_type

%define oname trilinos
Name: %oname%somver
Version: 10.10.0
Release: alt4
Summary: Solution of large-scale, complex multi-physics problems
License: LGPL
Group: Sciences/Mathematics
Url: http://trilinos.sandia.gov/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: http://trilinos.sandia.gov/download/files/%oname-%version-Source.tar.gz
Source1: CMakeCache.txt
Source2: %oname.pc
Source3: http://people.sc.fsu.edu/~jburkardt/cpp_src/sandia_rules/sandia_rules.H
Source4: http://people.sc.fsu.edu/~jburkardt/cpp_src/sandia_sgmg/sandia_sgmg.H
Source5: http://people.sc.fsu.edu/~jburkardt/cpp_src/sandia_sgmga/sandia_sgmga.H
Source6: http://people.sc.fsu.edu/~jburkardt/cpp_src/sandia_rules/sandia_rules.C
Source7: http://people.sc.fsu.edu/~jburkardt/cpp_src/sandia_sgmg/sandia_sgmg.C
Source8: http://people.sc.fsu.edu/~jburkardt/cpp_src/sandia_sgmga/sandia_sgmga.C

Requires: lib%name = %version-%release

BuildRequires(pre): rpm-build-python
BuildPreReq: gcc-fortran libgfortran-devel gcc-c++ libnumpy-devel
BuildPreReq: liblapack-devel doxygen getfemxx binutils-devel
BuildPreReq: openmpi-devel expat libexpat-devel swig graphviz
BuildPreReq: libgmp_cxx-devel libgmp-devel libxml2-devel
BuildPreReq: boost-devel libsuperlu-devel libarprec-devel libqd-devel
BuildPreReq: liby12m-devel libsuitesparse-devel libhdf5-mpi-devel
BuildPreReq: libmtl4-devel libsundials-devel python-devel
BuildPreReq: libscotch-devel libcheck-devel libblacs-devel
BuildPreReq: libsuperlu_dist-devel libscalapack-devel libmumps-devel
BuildPreReq: libparmetis0-devel libparpack-mpi-devel libarpack-devel
BuildPreReq: libadolc-devel libtvmet-devel libchaco-devel libfiatxx-devel
BuildPreReq: dblatex liboski-%scalar_type-devel
BuildPreReq: liboski-%scalar_type-devel python-module-docutils
BuildPreReq: libblitz-devel libtaucs-devel cmake ctest zlib-devel
BuildPreReq: libhypre-devel libgomp-devel python-module-pysparse
BuildPreReq: ghostscript-utils chrpath python-module-pyMPI
BuildPreReq: libtbb-devel libqt4-devel boost-program_options-devel
BuildPreReq: chaco libnetcdf-mpi-devel libexodusii-devel libnewmat-devel
BuildPreReq: libsparskit-devel boost-signals-devel tinyxml-devel Xdmf-devel
BuildPreReq: python-module-mpi4py-devel
%if_with dakota
BuildPreReq: libdakota-devel
%endif
%if_with petsc
BuildPreReq: libpetsc-%scalar_type-devel petsc-%scalar_type-sources
%endif

%description
%longdesc

%package headers
Summary: Headers for development packages of Trilinos
Group: Development/C++
#BuildArch: noarch
AutoReq: yes, nocpp
Provides: %oname-headers = %version-%release
Conflicts: %oname-headers < %version-%release

%description headers
%longdesc

This package contains headers for development packages of Trilinos.

%package -n lib%name
Summary: Shared libraries of Trilinos
Group: System/Libraries
Requires: libamesos%somver = %version-%release
Requires: libaztecoo%somver = %version-%release
Requires: libepetra%somver = %version-%release
Requires: libifpack%somver = %version-%release
Requires: libml%somver = %version-%release
Requires: libnox%somver = %version-%release
Requires: librtop%somver = %version-%release
Requires: libteuchos%somver = %version-%release
Requires: libthyra%somver = %version-%release
Requires: libepetraext%somver = %version-%release
Requires: libgaleri%somver = %version-%release
Requires: libzoltan%somver = %version-%release
Requires: libfei%somver = %version-%release
Requires: libisorropia%somver = %version-%release

%description -n lib%name
%longdesc

This package contains shared libraries of Trilinos.

%package -n lib%name-devel
Summary: Development files of Trilinos
Group: Development/C++
Requires: lib%name = %version-%release
Requires: %name = %version-%release
Requires: %name-headers = %version-%release
Requires: libsundance%somver-devel = %version-%release
Requires: libamesos%somver-devel = %version-%release
Requires: libanasazi%somver-devel = %version-%release
Requires: libaztecoo%somver-devel = %version-%release
Requires: libepetra%somver-devel = %version-%release
Requires: libepetraext%somver-devel = %version-%release
Requires: libgaleri%somver-devel = %version-%release
Requires: libifpack%somver-devel = %version-%release
Requires: libml%somver-devel = %version-%release
Requires: libmoocho%somver-devel = %version-%release
Requires: libnox%somver-devel = %version-%release
Requires: libpytrilinos%somver-devel = %version-%release
Requires: libstratimikos%somver-devel = %version-%release
Requires: libteuchos%somver-devel = %version-%release
Provides: lib%oname-devel = %version-%release
Conflicts: lib%oname-devel < %version-%release

%description -n lib%name-devel
%longdesc

This package contains development files of Trilinos.

%package -n libintrepid%somver
Summary: Interoperable tools for compatible discretizations of PDEs
Group: System/Libraries
Requires: libteuchos%somver = %version-%release

%description -n libintrepid%somver
%longdesc

Intrepid is a library of interoperable tools for compatible
discretizations of Partial Differential Equations (PDEs). Included with
the Trilinos 10.0 release is the "expert version" of Intrepid. This
version is intended primarily for application developers who want to
reuse large parts of their existing code frameworks such as I/O, data
structures, assembly routines, etc. while gaining access to advanced
discretization capabilities provided by Intrepid.

%package -n libintrepid%somver-devel
Summary: Development files of Intrepid
Group: Development/C++
Requires: %name-headers = %version-%release
Requires: libintrepid%somver = %version-%release
Provides: libintrepid-devel = %version-%release

%description -n libintrepid%somver-devel
%longdesc

Intrepid is a library of interoperable tools for compatible
discretizations of Partial Differential Equations (PDEs). Included with
the Trilinos 10.0 release is the "expert version" of Intrepid. This
version is intended primarily for application developers who want to
reuse large parts of their existing code frameworks such as I/O, data
structures, assembly routines, etc. while gaining access to advanced
discretization capabilities provided by Intrepid.

This package contains development files of Intrepid.

%package -n libshards%somver
Summary: Common tools for numerical and topological data used to solve PDEs
Group: System/Libraries

%description -n libshards%somver
%longdesc

Shards is a suite of common tools for numerical and topological data
that facilitate interoperability between typical software modules used
to solve Partial Differential Equations (PDEs) by finite element, finite
volume and finite difference methods. Shards provides two categories of
tools: templated multi-dimensional array implementation and templated
cell topologies.

%package -n libshards%somver-devel
Summary: Development files of Shards
Group: Development/C++
Requires: %name-headers = %version-%release
Requires: libshards%somver = %version-%release
Provides: libshards-devel = %version-%release

%description -n libshards%somver-devel
%longdesc

Shards is a suite of common tools for numerical and topological data
that facilitate interoperability between typical software modules used
to solve Partial Differential Equations (PDEs) by finite element, finite
volume and finite difference methods. Shards provides two categories of
tools: templated multi-dimensional array implementation and templated
cell topologies.

This package contains development files of Shards.

%package -n libtpetra%somver
Summary: Next-generation, templated version of Petra
Group: System/Libraries
Requires: libteuchos%somver = %version-%release
Requires: libkokkos%somver = %version-%release

%description -n libtpetra%somver
%longdesc

This package contains next-generation, templated version of Petra,
taking advantage of the newer advanced features of C++.

%package -n libtpetra%somver-devel
Summary: Development files of next-generation, templated version of Petra
Group: Development/C++
Requires: %name-headers = %version-%release
Requires: libtpetra%somver = %version-%release
Provides: libtpetra-devel = %version-%release

%description -n libtpetra%somver-devel
%longdesc

This package contains development files of next-generation, templated
version of Petra, taking advantage of the newer advanced features of
C++.

%package -n libisorropia%somver
Summary: Partitioning and load-balancing in the Trilinos framework
Group: System/Libraries
Requires: libepetra%somver = %version-%release
Requires: libzoltan%somver = %version-%release
Requires: libteuchos%somver = %version-%release

%description -n libisorropia%somver
%longdesc

This is a package for partitioning and load-balancing in the Trilinos framework.

%package -n libisorropia%somver-devel
Summary: Development files of partitioning and load-balancing package
Group: Development/C++
Requires: %name-headers = %version-%release
Requires: libisorropia%somver = %version-%release
Provides: libisorropia-devel = %version-%release
Conflicts: libisorropia-devel < %version-%release

%description -n libisorropia%somver-devel
%longdesc

This package contains development files of package for partitioning and
load-balancing in the Trilinos framework.

%package -n libamesos%somver
Summary: Direct solver classes (Trilinos Project)
Group: System/Libraries
Requires: libepetraext%somver = %version-%release
Requires: libepetra%somver = %version-%release
Requires: libteuchos%somver = %version-%release

%description -n libamesos%somver
%longdesc

This package contains direct solver classes. Supports use of a growing list of
third party direct solvers, including DSCPACK, SuperLU, SuperLUDist and UMFPACK.
Compatible with Epetra.

%package -n libamesos%somver-devel
Summary: Development files of direct solver classes (Trilinos Project)
Group: Development/C++
Requires: %name-headers = %version-%release
Requires: libamesos%somver = %version-%release
Provides: libamesos-devel = %version-%release
Conflicts: libamesos-devel < %version-%release

%description -n libamesos%somver-devel
%longdesc

This package contains development files of direct solver classes. Supports use
of a growing list of third party direct solvers, including DSCPACK, SuperLU,
SuperLUDist and UMFPACK. Compatible with Epetra.

%package -n libanasazi%somver
Summary: Framework for large-scale eigenvalue algorithms (Trilinos Project)
Group: System/Libraries
Requires: libepetra%somver = %version-%release
Requires: libteuchos%somver = %version-%release

%description -n libanasazi%somver
%longdesc

This package contains extensible and interoperable framework for large-scale
eigenvalue algorithms. The motivation for this framework is to provide a generic
interface to a collection of algorithms for solving large-scale eigenvalue
problems. Anasazi is interoperable because both the matrix and vectors (defining
the eigenspace) are considered to be opaque objects---only knowledge of the
matrix and vectors via elementary operations is necessary. An implementation of
Anasazi is accomplished via the use of interfaces. Current interfaces available
include Epetra and so any libraries that understand Epetra matrices and vectors
(such as AztecOO) may also be used in conjunction with Anasazi.

%package -n libanasazi%somver-devel
Summary: Development files of framework for large-scale eigenvalue algorithms
Group: Development/C++
Requires: %name-headers = %version-%release
Requires: libanasazi%somver = %version-%release
Provides: libanasazi-devel = %version-%release
Conflicts: libanasazi-devel < %version-%release

%description -n libanasazi%somver-devel
%longdesc

This package contains development files of extensible and interoperable
framework for large-scale eigenvalue algorithms. The motivation for this
framework is to provide a generic interface to a collection of algorithms for
solving large-scale eigenvalue problems. Anasazi is interoperable because both
the matrix and vectors (defining the eigenspace) are considered to be opaque
objects---only knowledge of the matrix and vectors via elementary operations is
necessary. An implementation of Anasazi is accomplished via the use of
interfaces. Current interfaces available include Epetra and so any libraries
that understand Epetra matrices and vectors (such as AztecOO) may also be used
in conjunction with Anasazi.

%package -n libaztecoo%somver
Summary: Preconditioned Krylov solver package (Trilinos Project)
Group: System/Libraries
Requires: libepetra%somver = %version-%release
Requires: libteuchos%somver = %version-%release

%description -n libaztecoo%somver
%longdesc

This package contains preconditioned Krylov solver package. Supercedes Aztec
2.1. Solves linear systems of equations via preconditioned Krylov methods. Uses
Epetra objects, compatible with IFPACK, ML and Aztec.

%package -n libaztecoo%somver-devel
Summary: Development files of preconditioned Krylov solver package
Group: Development/C++
Requires: %name-headers = %version-%release
Requires: libaztecoo%somver = %version-%release
Provides: libaztecoo-devel = %version-%release
Conflicts: libaztecoo-devel < %version-%release

%description -n libaztecoo%somver-devel
%longdesc

This package contains development files of preconditioned Krylov solver
package. Supercedes Aztec 2.1. Solves linear systems of equations via
preconditioned Krylov methods. Uses Epetra objects, compatible with IFPACK, ML
and Aztec.

%package -n libbelos%somver
Summary: Next-generation iterative solvers written using a traits interface
Group: System/Libraries
Requires: libepetra%somver = %version-%release
Requires: libteuchos%somver = %version-%release

%description -n libbelos%somver
%longdesc

This package contains next-generation iterative solvers written using a traits
interface, meaning that it has no explicit dependence on any concrete linear
algebra library. Instead, it can be used with any concrete linear algebra
library that implements the Thyra abstract interfaces and even Epetra directly.

%package -n libbelos%somver-devel
Summary: Development files of next-generation iterative solvers
Group: Development/C++
Requires: %name-headers = %version-%release
Requires: libbelos%somver = %version-%release
Provides: libbelos-devel = %version-%release
Conflicts: libbelos-devel < %version-%release

%description -n libbelos%somver-devel
%longdesc

This package contains development files of next-generation iterative solvers
written using a traits interface, meaning that it has no explicit dependence on
any concrete linear algebra library. Instead, it can be used with any concrete
linear algebra library that implements the Thyra abstract interfaces and even
Epetra directly.

%package -n libmoocho%somver
Summary: Multifunctional Object-Oriented arCHitecture for Optimization
Group: System/Libraries
Requires: librtop%somver = %version-%release
Requires: libteuchos%somver = %version-%release
Requires: libthyra%somver = %version-%release

%description -n libmoocho%somver
%longdesc

This package contains MOOCHO (Multifunctional Object-Oriented arCHitecture for
Optimization) designed to solve large-scale, equality and inequality nonlinearly
constrained, non-convex optimization problems (i.e. nonlinear programs) using
reduced-space successive quadratic programming (SQP) methods.

%package -n libmoocho%somver-devel
Summary: Development files of Object-Oriented arCHitecture for Optimization
Group: Development/C++
Requires: %name-headers = %version-%release
Requires: libmoocho%somver = %version-%release
Provides: libmoocho-devel =  %version-%release
Conflicts: libmoocho-devel < %version-%release

%description -n libmoocho%somver-devel
%longdesc

This package contains development files of MOOCHO (Multifunctional
Object-Oriented arCHitecture for Optimization) designed to solve large-scale,
equality and inequality nonlinearly constrained, non-convex optimization
problems (i.e. nonlinear programs) using reduced-space successive quadratic
programming (SQP) methods.

%package -n libpliris%somver
Summary: Object-oriented interface to a LU solver for parallel dense matrices
Group: System/Libraries
Requires: libepetra%somver = %version-%release

%description -n libpliris%somver
%longdesc

This package contains an object-oriented interface to a LU solver for dense
matrices on parallel platforms.

%package -n libpliris%somver-devel
Summary: Development files of object-oriented interface to a LU solver
Group: Development/C++
Requires: %name-headers = %version-%release
Requires: libpliris%somver = %version-%release
Provides: libpliris-devel = %version-%release
Conflicts: libpliris-devel < %version-%release

%description -n libpliris%somver-devel
%longdesc

This package contains development files of an object-oriented interface to a LU
solver for dense matrices on parallel platforms.

%package -n libepetra%somver
Summary: Wrappers for select BLAS and LAPACK routines (Trilinos Project)
Group: System/Libraries
Requires: libteuchos%somver = %version-%release

%description -n libepetra%somver
%longdesc

This package contains core linear algebra package. Facilitates construction and
manipulation of distributed and serial graphs, sparse and dense matrices,
vectors and multivectors.

%package -n libepetra%somver-devel
Summary: Development files of wrappers for select BLAS and LAPACK routines
Group: Development/C++
Requires: %name-headers = %version-%release
Requires: libepetra%somver = %version-%release
Provides: libepetra-devel = %version-%release
Conflicts: libepetra-devel < %version-%release

%description -n libepetra%somver-devel
%longdesc

This package contains development files of core linear algebra package.
Facilitates construction and manipulation of distributed and serial graphs,
sparse and dense matrices, vectors and multivectors.

%package -n libepetraext%somver
Summary: Extensions to the core linear algebra package, Epetra
Group: System/Libraries
Requires: lib%name = %version-%release
Requires: libepetra%somver = %version-%release
Requires: libteuchos%somver = %version-%release
Requires: libzoltan%somver = %version-%release

%description -n libepetraext%somver
%longdesc

This package contains Matrix/Vector read/write utilities, extensions to the
core linear algebra package, Epetra.

%package -n libepetraext%somver-devel
Summary: Development files of extensions to the core linear algebra package
Group: Development/C++
Requires: %name-headers = %version-%release
Requires: libepetraext%somver = %version-%release
Provides: libepetraext-devel = %version-%release
Conflicts: libepetraext-devel < %version-%release

%description -n libepetraext%somver-devel
%longdesc

This package contains development files of Matrix/Vector read/write utilities,
extensions to the core linear algebra package, Epetra.

%package -n libphdmesh%somver
Summary: Parallel Heterogeneous Dynamic unstructured Mesh data structure library
Group: System/Libraries

%description -n libphdmesh%somver
%longdesc

This package contains the Parallel Heterogeneous Dynamic unstructured Mesh
(phdMesh) data structure library, intended to be component used within a
finite element or finite volume library or code. The phdMesh data structure
supports arbitrary unstructured mesh connectivity, application-defined groupings
of mesh entities, and application-defined computational field data. The included
parallel-performance test application performs dynamic load balancing and
parallel geometric proximity searching on the contrived "gears" test problem.

%package -n libphdmesh%somver-devel
Summary: Development files of Dynamic unstructured Mesh data structure library
Group: Development/C++
Requires: %name-headers = %version-%release
Requires: libphdmesh%somver = %version-%release
Provides: libphdmesh-devel = %version-%release
Conflicts: libphdmesh-devel < %version-%release

%description -n libphdmesh%somver-devel
%longdesc

This package contains development files of the Parallel Heterogeneous Dynamic
unstructured Mesh (phdMesh) data structure library, intended to be component
used within a finite element or finite volume library or code. The phdMesh data
structure supports arbitrary unstructured mesh connectivity, application-defined
groupings of mesh entities, and application-defined computational field data.
The included parallel-performance test application performs dynamic load
balancing and parallel geometric proximity searching on the contrived "gears"
test problem.

%package -n libsundance%somver
Summary: Rapid development of high-performance parallel finite-element solutions
Group: System/Libraries
Requires: libteuchos%somver = %version-%release
Requires: libthyra%somver = %version-%release
Requires: librtop%somver = %version-%release
Requires: libnox%somver = %version-%release
Requires: libml%somver = %version-%release
Requires: libifpack%somver = %version-%release
Requires: libamesos%somver = %version-%release
Requires: libaztecoo%somver = %version-%release
Requires: libepetra%somver = %version-%release

%description -n libsundance%somver
%longdesc

This package contains Sundance, a system for rapid development of
high-performance parallel finite-element solutions of partial differential
equations. It is built on top of an engine for in-place Frechet differentiation
of symbolic objects, thereby enabling differentiable simulations for use in
optimization, uncertainty quantification, and adaptive error control.

%package -n libsundance%somver-devel
Summary: Development files of rapid development of finite-element solutions
Group: Development/C++
Requires: %name-headers = %version-%release
Requires: libsundance%somver = %version-%release
Provides: libsundance-devel = %version-%release
Conflicts: libsundance-devel < %version-%release

%description -n libsundance%somver-devel
%longdesc

This package contains development files of Sundance, a system for rapid
development of high-performance parallel finite-element solutions of partial
differential equations. It is built on top of an engine for in-place Frechet
differentiation of symbolic objects, thereby enabling differentiable simulations
for use in optimization, uncertainty quantification, and adaptive error control.

%package -n python-module-PySundance
Summary: Python interface to Sundance
Group: Development/Python
%setup_python_module PySundance
%py_provides PySundance

%description -n python-module-PySundance
%longdesc

This package contains Python interface to Sundance, a system for rapid
development of high-performance parallel finite-element solutions of partial
differential equations. It is built on top of an engine for in-place Frechet
differentiation of symbolic objects, thereby enabling differentiable simulations
for use in optimization, uncertainty quantification, and adaptive error control.

%package -n python-module-PySundance-examples
Summary: Examples for Python interface to Sundance
Group: Development/Python
#BuildArch: noarch

%description -n python-module-PySundance-examples
%longdesc

This package contains examples for PySundance, a system for rapid
development of high-performance parallel finite-element solutions of partial
differential equations. It is built on top of an engine for in-place Frechet
differentiation of symbolic objects, thereby enabling differentiable simulations
for use in optimization, uncertainty quantification, and adaptive error control.

%package -n libml%somver
Summary: Multilevel, distributed memory algebraic preconditioners
Group: System/Libraries
Requires: libifpack%somver = %version-%release
Requires: libamesos%somver = %version-%release
Requires: libgaleri%somver = %version-%release
Requires: libaztecoo%somver = %version-%release
Requires: libepetraext%somver = %version-%release
Requires: libzoltan%somver = %version-%release
Requires: libepetra%somver = %version-%release
Requires: libteuchos%somver = %version-%release

%description -n libml%somver
%longdesc

This package contains ML - multilevel, distributed memory algebraic
preconditioners. It provides multi-level, multigrid-like preconditioners for
distributed linear systems. Compatible with AztecOO.

%package -n libml%somver-devel
Summary: Development files of distributed memory algebraic preconditioners
Group: Development/C++
Conflicts: libopencv-devel < 1.2.1
Requires: %name-headers = %version-%release
Requires: libml%somver = %version-%release
Provides: libml-devel = %version-%release
Conflicts: libml-devel < %version-%release

%description -n libml%somver-devel
%longdesc

This package contains development files of ML - multilevel, distributed memory
algebraic preconditioners. It provides multi-level, multigrid-like
preconditioners for distributed linear systems. Compatible with AztecOO.

%package -n libfei%somver
Summary: Finite Element Interface to linear solvers (Trilinos Project)
Group: System/Libraries
Requires: libteuchos%somver = %version-%release
Requires: libml%somver = %version-%release
Requires: libamesos%somver = %version-%release
Requires: libaztecoo%somver = %version-%release
Requires: libepetra%somver = %version-%release

%description -n libfei%somver
%longdesc

This package contains Finite Element Interface to linear solvers (FEI). FEI is a
library for assembling sparse linear systems arising from finite element
applications, and other applications which use unstructured mesh data.

%package -n libfei%somver-devel
Summary: Development files of finite Element Interface to linear solvers
Group: Development/C++
Requires: %name-headers = %version-%release
Requires: libfei%somver = %version-%release
Provides: libfei-devel = %version-%release
Conflicts: libfei-devel < %version-%release

%description -n libfei%somver-devel
%longdesc

This package contains development files of finite Element Interface to linear
solvers (FEI). FEI is a library for assembling sparse linear systems arising
from finite element applications, and other applications which use unstructured
mesh data.

%package -n libgaleri%somver
Summary: A package for generating linear systems (Trilinos Project)
Group: System/Libraries
Requires: libepetra%somver = %version-%release
Requires: libteuchos%somver = %version-%release

%description -n libgaleri%somver
%longdesc

This package contains Galeri, a package for generating linear systems.

%package -n libgaleri%somver-devel
Summary: Development files of a package for generating linear systems
Group: Development/C++
Requires: %name-headers = %version-%release
Requires: libgaleri%somver = %version-%release
Provides: libgaleri-devel = %version-%release
Conflicts: libgaleri-devel < %version-%release

%description -n libgaleri%somver-devel
%longdesc

This package contains development files of Galeri, a package for generating
linear systems.

%package -n libifpack%somver
Summary: Distributed algebraic preconditioner package (Trilinos Project)
Group: System/Libraries
Requires: libamesos%somver = %version-%release
Requires: libaztecoo%somver = %version-%release
Requires: libepetra%somver = %version-%release
Requires: libteuchos%somver = %version-%release

%description -n libifpack%somver
%longdesc

This package contains IFPACK, distributed algebraic preconditioner package. It
includes incomplete factorizations and relaxation-based preconditioners in
domain decomposition framework. Compatible with AztecOO.

%package -n libifpack%somver-devel
Summary: Development files of Distributed algebraic preconditioner package
Group: Development/C++
Requires: %name-headers = %version-%release
Requires: libifpack%somver = %version-%release
Provides: libifpack-devel = %version-%release
Conflicts: libifpack-devel < %version-%release

%description -n libifpack%somver-devel
%longdesc

This package contains development files of IFPACK, distributed algebraic
preconditioner package. It includes incomplete factorizations and
relaxation-based preconditioners in domain decomposition framework. Compatible
with AztecOO.

%package -n libkokkos%somver
Summary: Core kernel package of Trilinos Project
Group: System/Libraries
Requires: lib%name = %version-%release
Requires: libteuchos%somver = %version-%release

%description -n libkokkos%somver
%longdesc

This package contains Core kernel package of Trilinos Project, a collection of
the handful of sparse and dense kernels that determine the much of the
performance for preconditioned Krylov methods.  In particular, it contains
function class for sparse matrix vector multiplication and triangular solves,
and also for dense kernels that are not part of the standard BLAS.

%package -n libkokkos%somver-devel
Summary: Development Files of core kernel package of Trilinos Project
Group: Development/C++
Requires: %name-headers = %version-%release
Requires: libkokkos%somver = %version-%release
Provides: libkokkos-devel = %version-%release
Conflicts: libkokkos-devel < %version-%release

%description -n libkokkos%somver-devel
%longdesc

This package contains development files of Core kernel package of Trilinos
Project, a collection of the handful of sparse and dense kernels that
determine the much of the performance for preconditioned Krylov methods.  In
particular, it contains function class for sparse matrix vector multiplication
and triangular solves, and also for dense kernels that are not part of the
standard BLAS.

%package -n libkomplex%somver
Summary: Complex linear solver package (Trilinos Project)
Group: System/Libraries
Requires: libaztecoo%somver = %version-%release
Requires: libteuchos%somver = %version-%release
Requires: libepetra%somver = %version-%release

%description -n libkomplex%somver
%longdesc

This package contains complex linear solver package. Solves complex-valued
linear systems via equivalent real formulations.

%package -n libkomplex%somver-devel
Summary: Development files of complex linear solver package (Trilinos Project)
Group: Development/C++
Requires: %name-headers = %version-%release
Requires: libkomplex%somver = %version-%release
Provides: libkomplex-devel = %version-%release
Conflicts: libkomplex-devel < %version-%release

%description -n libkomplex%somver-devel
%longdesc

This package contains development files of complex linear solver package. Solves
complex-valued linear systems via equivalent real formulations.

%package -n libloca%somver
Summary: Performing bifurcation analysis of large-scale applications
Group: System/Libraries
Requires: libnox%somver = %version-%release
Requires: libepetraext%somver = %version-%release
Requires: libepetra%somver = %version-%release
Requires: libteuchos%somver = %version-%release
Requires: libthyra%somver = %version-%release

%description -n libloca%somver
%longdesc

This package contains software library for performing bifurcation analysis of
large-scale applications. When implemented with an application code, LOCA
enables the tracking of solution branches as a function of system parameters and
the direct tracking of bifurcation points. LOCA is designed to drive application
codes that use Newton's method to locate steady-state solutions to nonlinear
problems.

%package -n libloca%somver-devel
Summary: Development files of bifurcation analysis of large-scale applications
Group: Development/C++
Requires: %name-headers = %version-%release
Requires: libloca%somver = %version-%release
Provides: libloca-devel = %version-%release
Conflicts: libloca-devel < %version-%release

%description -n libloca%somver-devel
%longdesc

This package contains development files of software library for performing
bifurcation analysis of large-scale applications. When implemented with an
application code, LOCA enables the tracking of solution branches as a function
of system parameters and the direct tracking of bifurcation points. LOCA is
designed to drive application codes that use Newton's method to locate
steady-state solutions to nonlinear problems.

%package -n libmeros%somver
Summary: Segregated preconditioning package (Trilinos Project)
Group: System/Libraries
Requires: libthyra%somver = %version-%release
Requires: librtop%somver = %version-%release
Requires: libteuchos%somver = %version-%release

%description -n libmeros%somver
%longdesc

This package contains segregated preconditioning package. Provides scalable
block preconditioning for problems that coupled simultaneous solution variables
such as Navier-Strokes problems.

%package -n libmeros%somver-devel
Summary: Development files of segregated preconditioning package
Group: Development/C++
Requires: %name-headers = %version-%release
Requires: libmeros%somver = %version-%release
Provides: libmeros-devel = %version-%release
Conflicts: libmeros-devel < %version-%release

%description -n libmeros%somver-devel
%longdesc

This package contains development files of segregated preconditioning package.
Provides scalable block preconditioning for problems that coupled simultaneous
solution variables such as Navier-Strokes problems.

%package -n libmoertel%somver
Summary: Mortar methods for nonconforming situations (Trilinos Project)
Group: System/Libraries
Requires: libml%somver = %version-%release
Requires: libamesos%somver = %version-%release
Requires: libaztecoo%somver = %version-%release
Requires: libepetraext%somver = %version-%release
Requires: libepetra%somver = %version-%release
Requires: libteuchos%somver = %version-%release

%description -n libmoertel%somver
%longdesc

This package contains Mortar methods that can be used in a large class of
nonconforming situations such as the surface coupling of different physical
models, discretization schemes or non-matching triangulations along interior
interfaces of a domain.

%package -n libmoertel%somver-devel
Summary: Development files of mortar methods for nonconforming situations
Group: Development/C++
Requires: %name-headers = %version-%release
Requires: libmoertel%somver = %version-%release
Provides: libmoertel-devel = %version-%release
Conflicts: libmoertel-devel < %version-%release

%description -n libmoertel%somver-devel
%longdesc

This package contains development files of Mortar methods that can be used in a
large class of nonconforming situations such as the surface coupling of
different physical models, discretization schemes or non-matching triangulations
along interior interfaces of a domain.

%package -n libthyra%somver
Summary: Abstract linear solver package (Trilinos Project)
Group: System/Libraries
Requires: libepetraext%somver = %version-%release
Requires: libepetra%somver = %version-%release
Requires: libteuchos%somver = %version-%release
Requires: librtop%somver = %version-%release

%description -n libthyra%somver
%longdesc

This package contains abstract linear solver package, that replaces the
now-deprecated TSF family.

%package -n libthyra%somver-devel
Summary: Development files of abstract linear solver package
Group: Development/C++
Requires: %name-headers = %version-%release
Requires: libthyra%somver = %version-%release
Provides: libthyra-devel = %version-%release
Conflicts: libthyra-devel < %version-%release

%description -n libthyra%somver-devel
%longdesc

This package contains development files of abstract linear solver package, that
replaces the now-deprecated TSF family.

%package -n libnox%somver
Summary: Nonlinear solver package (Trilinos Project)
Group: System/Libraries
Requires: libstratimikos%somver = %version-%release
Requires: libml%somver = %version-%release
Requires: libifpack%somver = %version-%release
Requires: libamesos%somver = %version-%release
Requires: libaztecoo%somver = %version-%release
Requires: libthyra%somver = %version-%release
Requires: libepetraext%somver = %version-%release
Requires: libepetra%somver = %version-%release
Requires: libteuchos%somver = %version-%release

%description -n libnox%somver
%longdesc

This package contains nonlinear solver package. Abstract and concrete classes
for construction and solution of nonlinear problems.

%package -n libnox%somver-devel
Summary: Development files of nonlinear solver package (Trilinos Project)
Group: Development/C++
Requires: %name-headers = %version-%release
Requires: libnox%somver = %version-%release
Provides: libnox-devel = %version-%release
Conflicts: libnox-devel < %version-%release

%description -n libnox%somver-devel
%longdesc

This package contains development files of nonlinear solver package. Abstract
and concrete classes for construction and solution of nonlinear problems.

%package -n libpamgen%somver
Summary: PAMGEN creates hexahedral or quadrilateral finite element meshes
Group: System/Libraries

%description -n libpamgen%somver
%longdesc

This package contains PAMGEN, that creates hexahedral or quadrilateral (in 2D)
finite element meshes of simple shapes (cubes and cylinders) in parallel. When
linked to an application as a library, it allows each process of a parallel
simulation to generate its finite element domain representation at execution
time.

%package -n libpamgen%somver-devel
Summary: Development files of PAMGEN
Group: Development/C++
Requires: %name-headers = %version-%release
Requires: libpamgen%somver = %version-%release
Provides: libpamgen-devel = %version-%release
Conflicts: libpamgen-devel < %version-%release

%description -n libpamgen%somver-devel
%longdesc

This package contains development files of PAMGEN, that creates hexahedral or
quadrilateral (in 2D) finite element meshes of simple shapes (cubes and
cylinders) in parallel. When linked to an application as a library, it allows
each process of a parallel simulation to generate its finite element domain
representation at execution time.

%package -n libphalanx%somver
Summary: A local field evaluation kernel (Trilinos Project)
Group: System/Libraries
Requires: libteuchos%somver = %version-%release

%description -n libphalanx%somver
%longdesc

This package contains a local field evaluation kernel specifically designed for
general partial differential equation solvers.

%package -n libphalanx%somver-devel
Summary: Development files of a local field evaluation kernel (Trilinos Project)
Group: Development/C++
Requires: %name-headers = %version-%release
Requires: libphalanx%somver = %version-%release
Provides: libphalanx-devel = %version-%release
Conflicts: libphalanx-devel < %version-%release

%description -n libphalanx%somver-devel
%longdesc

This package contains development files of a local field evaluation kernel
specifically designed for general partial differential equation solvers.

%package -n librtop%somver
Summary: Reduction/transformation operators (Trilinos Project)
Group: System/Libraries
Requires: libteuchos%somver = %version-%release

%description -n librtop%somver
%longdesc

This package contains RTOp (reduction/transformation operators), that provides
the basic mechanism for implementing vector operations in a flexible and
efficient manner.

%package -n librtop%somver-devel
Summary: Development Files of reduction/transformation operators
Group: Development/C++
Requires: %name-headers = %version-%release
Requires: librtop%somver = %version-%release
Provides: librtop-devel = %version-%release
Conflicts: librtop-devel < %version-%release

%description -n librtop%somver-devel
%longdesc

This package contains development files of RTOp (reduction/transformation
operators), that provides the basic mechanism for implementing vector operations
in a flexible and efficient manner.

%package -n librythmos%somver
Summary: A transient integrator for ordinary differential equations
Group: System/Libraries
Requires: libthyra%somver = %version-%release
Requires: libteuchos%somver = %version-%release

%description -n librythmos%somver
%longdesc

This package contains a transient integrator for ordinary differential equations
and differential-algebraic equations with support for explicit, implicit,
one-step and multi-step algorithms. The fundamental design of Rythmos is aimed
at supporting operator-split algorithms, multi-physics applications, block
linear algebra, and adjoint integration.

%package -n librythmos%somver-devel
Summary: Development files of integrator for ordinary differential equations
Group: Development/C++
Requires: %name-headers = %version-%release
Requires: librythmos%somver = %version-%release
Provides: librythmos-devel = %version-%release
Conflicts: librythmos-devel < %version-%release

%description -n librythmos%somver-devel
%longdesc

This package contains development files of a transient integrator for ordinary
differential equations and differential-algebraic equations with support for
explicit, implicit, one-step and multi-step algorithms. The fundamental design
of Rythmos is aimed at supporting operator-split algorithms, multi-physics
applications, block linear algebra, and adjoint integration.

%package -n libsacado%somver
Summary: Automatic differentiation of C++ programs (Trilinos Project)
Group: System/Libraries
Requires: libteuchos%somver = %version-%release
Requires: libepetra%somver = %version-%release
Requires: libepetraext%somver = %version-%release

%description -n libsacado%somver
%longdesc

This package contains Sacado, a package for automatic differentiation of C++
programs. It provides simple yet fast and efficient classes for forward, revers
and Taylor polynomial mode automatic differentiation using C++ template and
operator overloading. The resulting derivatives can be leverage in numerous ways
including nonlinear solves with NOX continuation and bifurcation analysis with
LOCA optimization with MOOCHO, and time integration with Rythmos.

%package -n libsacado%somver-devel
Summary: Development files of automatic differentiation of C++ programs
Group: Development/C++
Requires: %name-headers = %version-%release
Requires: libsacado%somver = %version-%release
Provides: libsacado-devel = %version-%release
Conflicts: libsacado-devel < %version-%release

%description -n libsacado%somver-devel
%longdesc

This package contains development files of Sacado, a package for automatic
differentiation of C++ programs. It provides simple yet fast and efficient
classes for forward, revers and Taylor polynomial mode automatic differentiation
using C++ template and operator overloading. The resulting derivatives can be
leverage in numerous ways including nonlinear solves with NOX continuation and
bifurcation analysis with LOCA optimization with MOOCHO, and time integration
with Rythmos.

%package -n libstratimikos%somver
Summary: Unified set of Thyra-based wrappers (Trilinos Project)
Group: System/Libraries
Requires: libamesos%somver = %version-%release
Requires: libthyra%somver = %version-%release
Requires: libepetra%somver = %version-%release
Requires: libteuchos%somver = %version-%release
Requires: libaztecoo%somver = %version-%release
Requires: libepetraext%somver = %version-%release
Requires: libifpack%somver = %version-%release
Requires: libml%somver = %version-%release

Requires: librtop%somver = %version-%release
Requires: lib%name = %version-%release
Requires: libzoltan%somver = %version-%release
Requires: libgaleri%somver = %version-%release
Requires: libfei%somver = %version-%release

%description -n libstratimikos%somver
%longdesc

This package contains Stratimikos, unified set of Thyra-based wrappers to linear
solver and preconditioner capabilities in Trilinos. The name Stratimikos was
created from the Greek words "stratigiki" and "grammikos" which which mean
"strategy" and "linear in English. The word "stratimikos" itself has not real
meaning itself. The Stratimikos package is also a place where unified testing of
linear solvers and preconditioners can be performed.

%package -n libstratimikos%somver-devel
Summary: Development files of unified set of Thyra-based wrappers
Group: Development/C++
Requires: %name-headers = %version-%release
Requires: libstratimikos%somver = %version-%release
Provides: libstratimikos-devel = %version-%release
Conflicts: libstratimikos-devel < %version-%release

%description -n libstratimikos%somver-devel
%longdesc

This package contains development files of Stratimikos, unified set of
Thyra-based wrappers to linear solver and preconditioner capabilities in
Trilinos. The name Stratimikos was created from the Greek words "stratigiki" and
"grammikos" which which mean "strategy" and "linear in English. The word
"stratimikos" itself has not real meaning itself. The Stratimikos package is
also a place where unified testing of linear solvers and preconditioners can be
performed.

%package -n libteuchos%somver
Summary: Common tools package (Trilinos Project)
Group: System/Libraries

%description -n libteuchos%somver
%longdesc

This package provides wrappers for select BLAS and LAPACK routines.

%package -n libteuchos%somver-devel
Summary: Development files of common tools package (Trilinos Project)
Group: Development/C++
Requires: %name-headers = %version-%release
Requires: libteuchos%somver = %version-%release
Provides: libteuchos-devel = %version-%release
Conflicts: libteuchos-devel < %version-%release

%description -n libteuchos%somver-devel
%longdesc

This package contains development files of  wrappers for select BLAS and LAPACK
routines.

%package -n libzoltan%somver
Summary: A toolkit of parallel services for simulations (Trilinos Project)
Group: System/Libraries

%description -n libzoltan%somver
%longdesc

This package contains a toolkit of parallel services for dynamic, unstructured,
and/or adaptive simulations. Zoltan provides parallel dynamic load balancing and
related services for a wide variety of applications, including finite element
methods, matrix operations, particle methods, and crash simulations. Zoltan also
provides parallel graph coloring, matrix ordering, unstructured communication
tools, and distributed data directories.

%package -n libzoltan%somver-devel
Summary: Development files of a toolkit of parallel services for simulations
Group: Development/C++
Requires: %name-headers = %version-%release
Requires: libzoltan%somver = %version-%release
Provides: libzoltan-devel = %version-%release
Conflicts: libzoltan-devel < %version-%release

%description -n libzoltan%somver-devel
%longdesc

This package contains development files of a toolkit of parallel services for
dynamic, unstructured, and/or adaptive simulations. Zoltan provides parallel
dynamic load balancing and related services for a wide variety of applications,
including finite element methods, matrix operations, particle methods, and crash
simulations. Zoltan also provides parallel graph coloring, matrix ordering,
unstructured communication tools, and distributed data directories.

%package examples
Summary: Examples for Trilinos Project
Group: Development/Documentation
#BuildArch: noarch
Provides: %oname-examples = %version-%release
Requires: lib%name >= %version

%description examples
%longdesc

This package contains development documentation for Trilinos Project.

%package -n lib%name-devel-doc
Summary: Documentation for Trilinos Project
Group: Development/Documentation
#BuildArch: noarch
Provides: lib%oname-devel-doc = %version-%release
Conflicts: lib%oname-devel-doc < %version-%release
Obsoletes: lib%oname-devel-doc < %version-%release
Obsoletes: libnox-devel-doc
Obsoletes: libamesos-devel-doc
Obsoletes: libanasazi-devel-doc
Obsoletes: libml-devel-doc
Obsoletes: libifpack-devel-doc
Obsoletes: libkokkos-devel-doc
Obsoletes: libkomplex-devel-doc
Obsoletes: libmeros-devel-doc
Obsoletes: libmoertel-devel-doc
Obsoletes: libphalanx-devel-doc
Obsoletes: libpliris-devel-doc
Obsoletes: libteuchos-devel-doc

%description -n lib%name-devel-doc
%longdesc

This package contains development documentation for Trilinos Project.

%package -n libpytrilinos%somver
Summary: Shared library of PyTrilinos
Group: System/Libraries
Requires: libepetraext%somver = %version-%release
Requires: libepetra%somver = %version-%release
Requires: libteuchos%somver = %version-%release

%description -n libpytrilinos%somver
%longdesc

This package contains shared library of PyTrilinos.

%package -n libpytrilinos%somver-devel
Summary: Development files of PyTrilinos
Group: Development/C++
Requires: %name-headers = %version-%release
Requires: libpytrilinos%somver = %version-%release
Requires: libepetra%somver-devel = %version-%release
Requires: libteuchos%somver-devel = %version-%release
Requires: python-module-PyTrilinos%somver = %version-%release
Provides: libpytrilinos-devel = %version-%release
Conflicts: libpytrilinos-devel < %version-%release

%description -n libpytrilinos%somver-devel
%longdesc

This package contains development files of PyTrilinos.

%package -n python-module-PyTrilinos%somver
Summary: Python Interface to Trilinos
Group: Development/Python
Requires: lib%name = %version-%release
Requires: libpytrilinos%somver = %version-%release
Requires: libamesos%somver = %version-%release
Requires: libaztecoo%somver = %version-%release
Requires: libepetra%somver = %version-%release
Requires: libepetraext%somver = %version-%release
Requires: libgaleri%somver = %version-%release
Requires: libifpack%somver = %version-%release
Requires: libml%somver = %version-%release
Requires: libteuchos%somver = %version-%release
Requires: libzoltan%somver = %version-%release
Requires: libnox%somver = %version-%release
Requires: libhdf5-mpi
%setup_python_module PyTrilinos
%py_requires mpi4py
Provides: python-module-PyTrilinos = %version-%release
Conflicts: python-module-PyTrilinos < %version-%release
Obsoletes: python-module-PyTrilinos < %version-%release

%description -n python-module-PyTrilinos%somver
%longdesc

This package contains Python Interface to Trilinos.

%package -n python-module-PyTrilinos%somver-examples
Summary: Examples and tests for Python Interface to Trilinos
Group: Development/Python
Requires: python-module-PyTrilinos%somver >= %version
Provides: python-module-PyTrilinos-examples = %version-%release

%description -n python-module-PyTrilinos%somver-examples
%longdesc

This package contains examples and tests for Python Interface to
Trilinos.

%package -n python-module-PyTrilinos%somver-doc
Summary: Documentation for Python Interface to Trilinos
Group: Development/Documentation
Provides: python-module-PyTrilinos-doc = %version-%release
Conflicts: python-module-PyTrilinos-doc < %version-%release
Obsoletes: python-module-PyTrilinos-doc < %version-%release

%description -n python-module-PyTrilinos%somver-doc
%longdesc

This package contains documentation for Python Interface to Trilinos.

%package -n libmesquite%somver
Summary: Mesh Quality Improvement Toolkit
Group: System/Libraries
Provides: libmesquite = %version-%release

%description -n libmesquite%somver
%longdesc

MESQUITE is a linkable software library that applies a variety of
node-movement algorithms to improve the quality and/or adapt a given
mesh. Mesquite uses advanced smoothing and optimization to:

  * Untangle meshes,
  * Provide local size control,
  * Improve angles, orthogonality, and skew,
  * Increase minimum edge-lengths for increased time-steps,
  * Improve mesh smoothness,
  * Perform anisotropic smoothing,
  * Improve surface meshes, adapt to surface curvature,
  * Improve hybrid meshes (including pyramids & wedges),
  * Smooth meshes with hanging nodes,
  * Maintain quality of moving and/or deforming meshes,
  * Perform ALE rezoning,
  * Improve mesh quality on and near boundaries,
  * Improve transitions across internal boundaries,
  * Align meshes with vector fields, and
  * R-adapt meshes to solutions using error estimates.

Mesquite improves surface or volume meshes which are structured,
unstructured, hybrid, or non-comformal. A variety of element types are
permitted. Mesquite is designed to be as efficient as possible so that
large meshes can be improved.

%package -n libmesquite%somver-devel
Summary: Development files of Mesh Quality Improvement Toolkit
Group: Development/C++
Requires: %name-headers = %version-%release
Requires: libmesquite%somver = %version-%release
Provides: libmesquite-devel = %version-%release

%description -n libmesquite%somver-devel
%longdesc

MESQUITE is a linkable software library that applies a variety of
node-movement algorithms to improve the quality and/or adapt a given
mesh. Mesquite uses advanced smoothing and optimization.

This package contains development files of MESQUITE.

%package -n liboptika%somver
Summary: Easy access to GUI input methods for trilinos users' programs
Group: System/Libraries
Provides: liboptika = %version-%release

%description -n liboptika%somver
%longdesc

The Optika package give developers the tools they need to quickly obtain
information from their users, while still implementing a robust GUI. The
general work flow of a program utilizing the Optika package goes
something like this:

  1. Determine what inputs are needed from the user
  2. Create a list specifying these inputs
  3. Execute the GUI with the getInput() function to obtain the inputs
specified in step 2
  4. Proceed with the rest of the program with the given user inputs

An alternate work flow is also available. In this work flow, the
developer specifies a custom fucntion along with the inputs. When the
GUI is executed, it stays active for the entire duration of the program.
Everytime the user clicks a button, the custom function is called with
the current input values.

%package -n liboptika%somver-devel
Summary: Development files of Optika package
Group: Development/C++
Requires: %name-headers = %version-%release
Requires: liboptika%somver = %version-%release
Provides: liboptika-devel = %version-%release

%description -n liboptika%somver-devel
%longdesc

The Optika package give developers the tools they need to quickly obtain
information from their users, while still implementing a robust GUI.

This package contains development files of Optika.

%package -n liboptipack%somver
Summary: Collection of simple Thyra-based Optimization ANAs
Group: System/Libraries
Provides: liboptipack = %version-%release

%description -n liboptipack%somver
%longdesc

The package OptiPack contains abstract interfaces and a few concrete
implementation of some simple optimization Abstract Numerical Algorithms
(ANAs) based on Thyra.

%package -n liboptipack%somver-devel
Summary: Development files of OptiPack
Group: Development/C++
Requires: %name-headers = %version-%release
Requires: liboptipack%somver = %version-%release
Requires: libthyra%somver-devel = %version-%release
Requires: libteuchos%somver-devel = %version-%release
Provides: liboptipack-devel = %version-%release

%description -n liboptipack%somver-devel
%longdesc

The package OptiPack contains abstract interfaces and a few concrete
implementation of some simple optimization Abstract Numerical Algorithms
(ANAs) based on Thyra.

This package contains development files of OptiPack.

%package -n libpiro%somver
Summary: Strategy package for embedded analysis capabilitites
Group: System/Libraries
Provides: libpiro = %version-%release

%description -n libpiro%somver
%longdesc

Piro is the top-level, unifying package of the Embedded Nonlinear
Analysis Capability area. The main purpose of the package is to provide
driver classes for the common uses of Trilinos nonlinear analysis tools.
These drivers all can be constructed similarly, with a ModelEvaluator
and a ParameterList, to make it simple to switch between different types
of analysis. They also all inherit from the same base classes
(reponse-only model evaluators) so that the resulting analysis can in
turn driven by non-intrusive analysis routines.

%package -n libpiro%somver-devel
Summary: Development files of Piro, strategy package for embedded analysis capabilitites
Group: Development/C++
Requires: %name-headers = %version-%release
Requires: libpiro%somver = %version-%release
Provides: libpiro-devel = %version-%release

%description -n libpiro%somver-devel
%longdesc

Piro is the top-level, unifying package of the Embedded Nonlinear
Analysis Capability area. The main purpose of the package is to provide
driver classes for the common uses of Trilinos nonlinear analysis tools.
These drivers all can be constructed similarly, with a ModelEvaluator
and a ParameterList, to make it simple to switch between different types
of analysis. They also all inherit from the same base classes
(reponse-only model evaluators) so that the resulting analysis can in
turn driven by non-intrusive analysis routines.

This package contains development files of Piro.

%package -n libstokhos%somver
Summary: Stokhos Discretization Method
Group: System/Libraries
Provides: libstokhos = %version-%release

%description -n libstokhos%somver
%longdesc

Stokhos is a package for intrusive stochastic Galerkin uncertainty
quantification methods. It provides methods for computing well-known
intrusive stochastic Galerkin projections such as Polynomial Chaos and
Generalized Polynomial Chaos, interfaces for forming the resulting
nonlinear systems, and linear solver methods for solving block
stochastic Galerkin linear systems.

%package -n libstokhos%somver-devel
Summary: Stokhos Discretization Method
Group: Development/C++
Requires: %name-headers = %version-%release
Requires: libstokhos%somver = %version-%release
Provides: libstokhos-devel = %version-%release

%description -n libstokhos%somver-devel
%longdesc

Stokhos is a package for intrusive stochastic Galerkin uncertainty
quantification methods. It provides methods for computing well-known
intrusive stochastic Galerkin projections such as Polynomial Chaos and
Generalized Polynomial Chaos, interfaces for forming the resulting
nonlinear systems, and linear solver methods for solving block
stochastic Galerkin linear systems.

This package contains development files of Stokhos.

%package -n libSTK%somver
Summary: The Sierra Toolkit Mesh
Group: System/Libraries
Provides: libSTK = %version-%release

%description -n libSTK%somver
%longdesc

The Sierra Toolkit Mesh product provides a unstructured mesh in-memory,
parallel-distributed database. Mesh capabilities include a mesh topology
data structure, mesh subsetting, coefficient data, mesh field data,
support for changing the mesh topology, and support for parallel
operations on the mesh.

%package -n libSTK%somver-devel
Summary: Development files of the Sierra Toolkit Mesh
Group: Development/C++
Requires: %name-headers = %version-%release
Requires: libSTK%somver = %version-%release
Provides: libSTK-devel = %version-%release

%description -n libSTK%somver-devel
%longdesc

The Sierra Toolkit Mesh product provides a unstructured mesh in-memory,
parallel-distributed database. Mesh capabilities include a mesh topology
data structure, mesh subsetting, coefficient data, mesh field data,
support for changing the mesh topology, and support for parallel
operations on the mesh.

This package contains development files of STK.

%package -n libctrilinos%somver
Summary: C interface to Trilinos
Group: System/Libraries
Provides: libctrilinos = %version-%release

%description -n libctrilinos%somver
%longdesc

C interface to Trilinos.

%package -n libctrilinos%somver-devel
Summary: Development files of C interface to Trilinos
Group: Development/C
Requires: %name-headers = %version-%release
Requires: libctrilinos%somver = %version-%release
Requires: libifpack%somver-devel = %version-%release
Requires: libamesos%somver-devel = %version-%release
Requires: libgaleri%somver-devel = %version-%release
Requires: libaztecoo%somver-devel = %version-%release
Requires: libepetra%somver-devel = %version-%release
Requires: libteuchos%somver-devel = %version-%release
Provides: libctrilinos-devel = %version-%release

%description -n libctrilinos%somver-devel
%longdesc

C interface to Trilinos.

This package contains development files of CTrilinos.

%package -n libteko%somver
Summary: For block and physics-based preconditioners
Group: System/Libraries
Provides: libteko = %version-%release

%description -n libteko%somver
%longdesc

Teko is a library for implementation of blocked and segregated
preconditioners in the context of iterative solvers for linear
systems. This includes a high level interface for manipulating
block operators and creating inverse operators using solver
and preconditioning capabilities in Trilinos.  In addition,
utilities are provided that decompose large Epetra_CrsMatrix
objects into physically meaningful sub blocks.

%package -n libteko%somver-devel
Summary: Development files of Teko
Group: Development/C
Requires: %name-headers = %version-%release
Requires: libteko%somver = %version-%release
Requires: libstratimikos%somver-devel = %version-%release
Requires: libisorropia%somver-devel = %version-%release
Requires: libthyra%somver-devel = %version-%release
Requires: libepetraext%somver-devel = %version-%release
Requires: libepetra%somver-devel = %version-%release
Requires: libteuchos%somver-devel = %version-%release
Provides: libteko-devel = %version-%release

%description -n libteko%somver-devel
%longdesc

Teko is a library for implementation of blocked and segregated
preconditioners in the context of iterative solvers for linear
systems. This includes a high level interface for manipulating
block operators and creating inverse operators using solver
and preconditioning capabilities in Trilinos.  In addition,
utilities are provided that decompose large Epetra_CrsMatrix
objects into physically meaningful sub blocks.

This package contains development files of Teko.

%package -n libglobipack%somver
Summary: Collection of Scalar 1D globalizaton utilities
Group: System/Libraries
Provides: libglobipack = %version-%release

%description -n libglobipack%somver
%longdesc

The package GlobiPack contains abstract interfaces and a few concrete
implementation of 1D globalization algorithms.  These algorithms are
used in various nonlinear equations solver and optimization algorithms.

%package -n libglobipack%somver-devel
Summary: Development files of GlobiPack
Group: Development/C++
Requires: %name-headers = %version-%release
Requires: libglobipack%somver = %version-%release
Provides: libglobipack-devel = %version-%release

%description -n libglobipack%somver-devel
%longdesc

The package GlobiPack contains abstract interfaces and a few concrete
implementation of 1D globalization algorithms.  These algorithms are
used in various nonlinear equations solver and optimization algorithms.

This package contains development files of GlobiPack.

%package -n libtrikota%somver
Summary: Dakota framework underneath Trilinos as if it were another Trilinos package
Group: System/Libraries
Provides: libtrikota = %version-%release

%description -n libtrikota%somver
%longdesc

TriKota is a convenience package that builds the Dakota framework
underneath Trilinos as if it were another Trilinos package. Dakota
contains a wide array of algorithms for optimization and UQ. TriKota
provides adaptors between the Trilinos (ModelEvaluator) interface to the
Dakota interface, and wraps the typical library-mode usage of Dakota in
a convenience class and some simple example problems.

%package -n libtrikota%somver-devel
Summary: Development files of TriKota
Group: Development/C++
Requires: %name-headers = %version-%release
Provides: libtrikota-devel = %version-%release

%description -n libtrikota%somver-devel
%longdesc

TriKota is a convenience package that builds the Dakota framework
underneath Trilinos as if it were another Trilinos package. Dakota
contains a wide array of algorithms for optimization and UQ. TriKota
provides adaptors between the Trilinos (ModelEvaluator) interface to the
Dakota interface, and wraps the typical library-mode usage of Dakota in
a convenience class and some simple example problems.

This package contains development files of TriKota.

%package -n libseacas%somver
Summary: Extra libraries for Trilinos
Group: System/Libraries
Provides: libseacas = %version-%release

%description -n libseacas%somver
%longdesc

SEACAS is a set of additional libraries for Trilinos.

%package -n libseacas%somver-devel
Summary: Development files of SEACAS
Group: Development/C++
Requires: libseacas%somver = %version-%release
Requires: %name-headers = %version-%release
Provides: libseacas-devel = %version-%release

%description -n libseacas%somver-devel
%longdesc

SEACAS is a set of additional libraries for Trilinos.

This package contains development files of SEACAS.

%package -n libseacas%somver-apps
Summary: Libraries for SEACAS applications
Group: System/Libraries
Provides: libseacas-apps = %version-%release
Requires: libseacas%somver = %version-%release

%description -n libseacas%somver-apps
%longdesc

SEACAS is a set of additional libraries for Trilinos.
This package contains libraries for SEACAS applications.

%package -n libseacas%somver-apps-devel
Summary: Development files of SEACAS application libraries
Group: Development/C++
Requires: libseacas%somver = %version-%release
Requires: libseacas%somver-apps = %version-%release
Requires: %name-headers = %version-%release
Provides: libseacas-apps-devel = %version-%release

%description -n libseacas%somver-apps-devel
%longdesc

SEACAS is a set of additional libraries for Trilinos.

This package contains development files for SEACAS applications.

%package -n seacas%somver-apps
Summary: SEACAS applications
Group: Sciences/Mathematics
Provides: seacas-apps = %version-%release
Requires: libseacas%somver-apps = %version-%release

%description -n seacas%somver-apps
%longdesc

SEACAS is a set of additional libraries for Trilinos.

This package contains SEACAS applications.

%prep
%setup
rm -fR packages/seacas/libraries/nemesis

#sed -i 's|@LIBDIR@|%_libdir|g' \
#	cmake/python/data/TrilinosPackageDependencies.xml

sed -i 's|@SOMVER@|%somver|' \
	cmake/tribits/package_arch/TribitsLibraryMacros.cmake
sed -i 's|@SOVER@|%sover|' \
	cmake/tribits/package_arch/TribitsLibraryMacros.cmake

install -m644 %SOURCE1 %SOURCE2 .
sed -i 's|@VERSION@|%version|' %oname.pc

sed -i 's|@MPIDIR@|%mpidir|g' %oname.pc CMakeCache.txt
sed -i 's|@PYVER@|%_python_version|g' %oname.pc CMakeCache.txt \
	packages/PyTrilinos/src/CMakeLists.txt \
	packages/Sundance/python/src/CMakeLists.txt
sed -i 's|@LIBDIR@|%_libdir|g' CMakeCache.txt \
	packages/Sundance/python/src/CMakeLists.txt \
	packages/TriKota/src/CMakeLists.txt

%if_with dakota
sed -i 's|@DAKOTA@|ON|' CMakeCache.txt
%else
sed -i 's|@DAKOTA@|OFF|' CMakeCache.txt
%endif

%ifarch x86_64
LIB64=64
%endif
sed -i "s|@64@|$LIB64|g" CMakeCache.txt

%if_with petsc
sed -i 's|@ENABLE_PETSC@||' CMakeCache.txt
sed -i 's|@PETSC_DIR@|%ldir|g' %oname.pc CMakeCache.txt
%else
sed -i 's|@PETSC_DIR@/lib|%_libdir|g' %oname.pc CMakeCache.txt
sed -i 's|@PETSC_DIR@|%prefix|g' %oname.pc CMakeCache.txt
sed -i 's|@ENABLE_PETSC@|#|' CMakeCache.txt
%endif

sed -i 's|^\(GENERATE_MAN\).*|\1 = YES|' \
	$(find ./ -name 'Doxyfile*')

install -d packages/TriKota/Dakota/install/include
#install -p -m644 %SOURCE3 %SOURCE4 %SOURCE5 \
#	packages/TriKota/Dakota/install/include
install -p -m644 %SOURCE3 %SOURCE4 %SOURCE5 %SOURCE6 %SOURCE7 %SOURCE8 \
	packages/stokhos/src

%build
mpi-selector --set %mpiimpl
source %mpidir/bin/mpivars.sh
export OMPI_LDFLAGS="-Wl,--as-needed,-R,%mpidir/lib -L%mpidir/lib"
%if_with petsc
source %_bindir/petsc-%scalar_type.sh
%endif

mkdir BUILD
cp CMakeCache.txt BUILD/
pushd BUILD
#rm -fR packages/TriKota/Dakota
#ln -s %_includedir/dakota packages/TriKota/Dakota
cmake \
	-DCMAKE_INSTALL_PREFIX=%prefix \
	-DMPI4PY_INCLUDE_DIR:PATH=%python_sitelibdir/mpi4py/include \
	..
%make -j2 VERBOSE=1
#make VERBOSE=1
popd

# docs

%ifnarch x86_64
pushd doc
./build_docs.pl
popd

pushd packages/PyTrilinos/doc
%make_build -C OverviewOfPyTrilinos
%make_build -C PyTrilinos-ACM-TOMS
%make_build -C UsersGuide
popd

pushd packages/Sundance/doc
%make_build
popd
%endif

%install
source %mpidir/bin/mpivars.sh
export OMPI_LDFLAGS="-Wl,--as-needed,-R,%mpidir/lib -L%mpidir/lib"
%if_with petsc
source %_bindir/petsc-%scalar_type.sh
%endif

pushd BUILD

mkdir -p packages/TriKota/Dakota/install/lib
mkdir -p packages/TriKota/Dakota/install/include
%makeinstall_std

install -d %buildroot%_pkgconfigdir
install -m644 ../%oname.pc %buildroot%_pkgconfigdir
#install -p -m644 %SOURCE3 %SOURCE4 %SOURCE5 \
#	%buildroot%_includedir

TOPDIR=$PWD

# PyTrilinos

pushd packages/PyTrilinos
install -d %buildroot%python_sitelibdir/PyTrilinos/example
install -d %buildroot%python_sitelibdir/PyTrilinos/test
cp -fR src/PyTrilinos \
	%buildroot%python_sitelibdir/
install -m644 example/*.py \
	%buildroot%python_sitelibdir/PyTrilinos/example
install -m644 test/*.py \
	%buildroot%python_sitelibdir/PyTrilinos/test
touch %buildroot%python_sitelibdir/PyTrilinos/example/__init__.py
touch %buildroot%python_sitelibdir/PyTrilinos/test/__init__.py

install -d %buildroot%_includedir/PyTrilinos
install -p -m644 src/*.h \
	%buildroot%_includedir/PyTrilinos
popd

%ifnarch x86_64
pushd ../packages/PyTrilinos/doc
install -d %buildroot%_libdir/%name/doc/PyTrilinos
cp -fR DevelopersGuide OverviewOfPyTrilinos/*.ps \
	SciPy05 UsersGuide/*.ps \
	PyTrilinos-ACM-TOMS/*.pdf  PyTrilinos-ACM-TOMS/*test* \
	%buildroot%_libdir/%name/doc/PyTrilinos/
popd
%endif

# PySundance

install -d %buildroot%python_sitelibdir/PySundance
cp -fR ../packages/Sundance/python/utils \
	%buildroot%python_sitelibdir/PySundance/
touch %buildroot%python_sitelibdir/PySundance/utils/__init__.py
touch %buildroot%python_sitelibdir/PySundance/utils/Meshing/__init__.py

install -d %buildroot%_includedir/PySundance
cp ../packages/Sundance/python/src/*.hpp \
	%buildroot%_includedir/PySundance

pushd packages/Sundance/python
install -d %buildroot%python_sitelibdir/PySundance
install -p -m644 src/*.py src/*.so \
	%buildroot%python_sitelibdir/PySundance
rm -f %buildroot%python_sitelibdir/PySundance/setup.py

%ifnarch x86_64
install -d %buildroot%_docdir/PySundance
cp -fR example \
	%buildroot%_docdir/PySundance/
%endif
popd

popd # BUILD

# docs

%ifnarch x86_64
install -d %buildroot%_man3dir
for i in $(find ./ -name man3);
do
	if [ "$(ls $i |wc -l)" != "0" ]; then
		install -m644 $i/* %buildroot%_man3dir
	fi
done

for i in $(find packages -name html |sort); do
	if [ "$(ls $i |wc -l)" != "0" ]; then
		install -d %buildroot%_docdir/%name/$i
		cp -fR $i/* %buildroot%_docdir/%name/$i/
	fi
done
install -p -m644 doc/index.html %buildroot%_docdir/%name/html

pushd packages
for i in $(find ./*.pdf) $(find ./*.ps); do
	dir=$(echo $i |sed 's|\(.*\)\/.*|\1|')
	install -d %buildroot%_docdir/%name/pdf_ps/$dir
	install -p -m644 $i \
		%buildroot%_docdir/%name/pdf_ps/$dir
done

# examples

for i in $(find ./ -name '*xampl*' -type d); do
	install -d %buildroot%_docdir/%name/examples/$i
	cp -fR $i/* %buildroot%_docdir/%name/examples/$i/
done
%endif

# clean buildroot

pushd %buildroot
rm -fR  $(find ./ -name '*.o') \
	$(find ./%_docdir -name '*.so*') \
	$(find ./%_libdir -name '*.pl.in') \
	$(find ./ -name '*.src') \
	$(find ./ -name '*.cmake') \
	$(find ./ -name 'CMake*') \
	$(find ./ -name 'Makefile') \
	./%_libdir/libnemesis.so*
#	./%_libexecdir/libnem_spread_app_lib.so* \
popd
install -m755 $TOPDIR/packages/seacas/applications/aprepro/aprepro \
	$TOPDIR/packages/seacas/applications/epu/epu \
	$TOPDIR/packages/seacas/applications/exodiff/exodiff \
	$TOPDIR/packages/seacas/applications/exotxt/exotxt \
	%buildroot%_bindir

# fix RPATH

for i in $(find %buildroot -name '*.so') \
	 $(find %buildroot -name '*.so.%sover') \
	 $(find %buildroot -name '*.exe') \
	 %buildroot%_bindir/*
do
	if [ "$(file $i|sed 's|.*\(ELF\).*|\1|')" = "ELF" ]; then
		if [ "$i" = "%buildroot%python_sitelibdir/PySundance/_PySundance.so" ]
		then
			ADDDIR=:%python_sitelibdir
		else
			ADDDIR=
		fi
%if_with petsc
		chrpath -r %mpidir/lib:%ldir/lib:%_libdir/oski$ADDDIR $i ||:
%else
		chrpath -r %mpidir/lib:%_libdir/oski$ADDDIR $i || \
			chrpath -r %mpidir/lib$ADDDIR $i ||:
%endif
	fi
done

# fix for x86_64

%ifarch x86_64
mv %buildroot%_libexecdir/*.so* %buildroot%_libdir/
%endif

mv %buildroot%prefix/site-packages/*PerceptMesh* \
	%buildroot%python_sitelibdir/

# fix file conflict with libmesh-doc

%ifnarch x86_64
pushd %buildroot%_man3dir
mv todo.3 trilinos.todo.3
popd
%endif

%files
%doc README RELEASE_NOTES *.txt

%files headers
%_includedir/*

%files -n lib%name
%_libdir/libtriutils.so.*
%_libdir/libtrilinoscouplings.so.*
%_libdir/libtpi.so.*

%files -n lib%name-devel
%_libdir/libtriutils.so
%_libdir/libtrilinoscouplings.so
%_libdir/libtpi.so
%_pkgconfigdir/*

%files -n libisorropia%somver
%_libdir/libisorropia.so.*

%files -n libisorropia%somver-devel
%_libdir/libisorropia.so

%files -n libamesos%somver
%_libdir/libamesos.so.*

%files -n libamesos%somver-devel
%_libdir/libamesos.so

%files -n libanasazi%somver
%_libdir/libanasazi*.so.*
%_libdir/libModeLaplace.so.*

%files -n libanasazi%somver-devel
%_libdir/libanasazi*.so
%_libdir/libModeLaplace.so

%files -n libaztecoo%somver
%_libdir/libaztecoo.so.*

%files -n libaztecoo%somver-devel
%_libdir/libaztecoo.so

%files -n libbelos%somver
%_libdir/libbelos*.so.*

%files -n libbelos%somver-devel
%_libdir/libbelos*.so

%files -n libmoocho%somver
%_libdir/libmoocho*.so.*

%files -n libmoocho%somver-devel
%_libdir/libmoocho*.so

%files -n libpliris%somver
%_libdir/lib?pliris.so.*

%files -n libpliris%somver-devel
%_libdir/lib?pliris.so

%files -n libepetra%somver
%_libdir/libepetra.so.*

%files -n libepetra%somver-devel
%_libdir/libepetra.so

%files -n libepetraext%somver
%_libdir/libepetraext.so.*

%files -n libepetraext%somver-devel
%_libdir/libepetraext.so

#files -n libphdmesh%somver
#_libdir/libphd*.so.*

#files -n libphdmesh%somver-devel
#_libdir/libphd*.so

%files -n libsundance%somver
%_libdir/libsundance*.so.*
%_libdir/libplaya.so.*
%_libdir/libpdeopt.so.*

%files -n libsundance%somver-devel
%_libdir/libsundance*.so
%_libdir/libplaya.so
%_libdir/libpdeopt.so

%files -n libml%somver
%_libdir/libml.so.*

%files -n libml%somver-devel
%_libdir/libml.so

%files -n libfei%somver
%_libdir/libfei*.so.*

%files -n libfei%somver-devel
%_libdir/libfei*.so

%files -n libgaleri%somver
%_libdir/libgaleri.so.*

%files -n libgaleri%somver-devel
%_libdir/libgaleri.so

%files -n libifpack%somver
%_libdir/libifpack*.so.*
#_libdir/libtifpack.so.*

%files -n libifpack%somver-devel
%_libdir/libifpack*.so
#_libdir/libtifpack.so

%files -n libkokkos%somver
%_libdir/libkokkos*.so.*

%files -n libkokkos%somver-devel
%_libdir/libkokkos*.so

%files -n libkomplex%somver
%_libdir/libkomplex.so.*

%files -n libkomplex%somver-devel
%_libdir/libkomplex.so

%files -n libloca%somver
%_libdir/libloca*.so.*

%files -n libloca%somver-devel
%_libdir/libloca*.so

#files -n libmeros%somver
#_libdir/libmeros*.so.*

#files -n libmeros%somver-devel
#_libdir/libmeros*.so

%files -n libmoertel%somver
%_libdir/libmoertel*.so.*

%files -n libmoertel%somver-devel
%_libdir/libmoertel*.so

%files -n libthyra%somver
%_libdir/libthyra*.so.*

%files -n libthyra%somver-devel
%_libdir/libthyra*.so

%files -n libnox%somver
%_libdir/libnox*.so.*

%files -n libnox%somver-devel
%_libdir/libnox*.so

%files -n libpamgen%somver
%_libdir/libpamgen*.so.*

%files -n libpamgen%somver-devel
%_libdir/libpamgen*.so

%files -n libphalanx%somver
%_bindir/phalanx_create_evaluator.py
%_libdir/libphalanx*.so.*

%files -n libphalanx%somver-devel
%_libdir/libphalanx*.so

%files -n librtop%somver
%_libdir/librtop.so.*

%files -n librtop%somver-devel
%_libdir/librtop.so

%files -n librythmos%somver
%_libdir/librythmos*.so.*
%_libdir/libgaasp.so.*

%files -n librythmos%somver-devel
%_libdir/librythmos*.so
%_libdir/libgaasp.so

%files -n libsacado%somver
%_libdir/libsacado.so.*

%files -n libsacado%somver-devel
%_libdir/libsacado.so

%files -n libstratimikos%somver
%_libdir/libstratimikos*.so.*

%files -n libstratimikos%somver-devel
%_libdir/libstratimikos*.so

%files -n libteuchos%somver
%_libdir/libteuchos.so.*

%files -n libteuchos%somver-devel
%_libdir/libteuchos.so

%files -n libzoltan%somver
%_libdir/libzoltan*.so.*

%files -n libzoltan%somver-devel
%_libdir/libzoltan*.so

%ifnarch x86_64
%files -n lib%name-devel-doc
%_docdir/%name/
%exclude %_docdir/%name/examples
%_man3dir/*
%exclude %_man3dir/deprecated.3*
%endif

%files -n libpytrilinos%somver
%_libdir/libpytrilinos.so.*

%files -n libpytrilinos%somver-devel
%_libdir/libpytrilinos.so

%files -n python-module-PyTrilinos%somver
%python_sitelibdir/PyTrilinos*
%exclude %python_sitelibdir/PyTrilinos/example
%exclude %python_sitelibdir/PyTrilinos/test
# antirepocop
%ifarch x86_64
%exclude %python_sitelibdir_noarch/PyTrilinos*
%endif
%python_sitelibdir/*PerceptMesh*

%files -n python-module-PySundance
%python_sitelibdir/PySundance*

%ifnarch x86_64
%files -n python-module-PyTrilinos%somver-examples
%python_sitelibdir/PyTrilinos/example
%python_sitelibdir/PyTrilinos/test

%files -n python-module-PyTrilinos%somver-doc
%dir %_libdir/%name/doc
%_libdir/%name/doc/PyTrilinos

%files examples
%dir %_docdir/%name
%_docdir/%name/examples

%files -n python-module-PySundance-examples
%dir %_docdir/PySundance
%_docdir/PySundance/example
%endif

%files -n libshards%somver
%_libdir/libshards.so.*

%files -n libshards%somver-devel
%_libdir/libshards.so

%files -n libtpetra%somver
%_libdir/libtpetra*.so.*

%files -n libtpetra%somver-devel
%_libdir/libtpetra*.so

%files -n libintrepid%somver
%_libdir/libintrepid*.so.*

%files -n libintrepid%somver-devel
%_libdir/libintrepid*.so

%files -n libmesquite%somver
%_libdir/libmesquite.so.*
#_libdir/libmsq*.so.*

%files -n libmesquite%somver-devel
%_libdir/libmesquite.so
#_libdir/libmsq*.so

%files -n liboptika%somver
%_libdir/liboptika.so.*

%files -n liboptika%somver-devel
%_libdir/liboptika.so

%files -n liboptipack%somver
%_libdir/liboptipack.so.*

%files -n liboptipack%somver-devel
%_libdir/liboptipack.so

%files -n libpiro%somver
%_libdir/libpiro.so.*

%files -n libpiro%somver-devel
%_libdir/libpiro.so

%files -n libSTK%somver
%_libdir/libstk*.so.*

%files -n libSTK%somver-devel
%_libdir/libstk*.so

%files -n libstokhos%somver
%_libdir/libstokhos.so.*

%files -n libstokhos%somver-devel
%_libdir/libstokhos.so

%files -n libctrilinos%somver
%_libdir/libctrilinos.so.*

%files -n libctrilinos%somver-devel
%_libdir/libctrilinos.so

%files -n libteko%somver
%_libdir/libteko.so.*

%files -n libteko%somver-devel
%_libdir/libteko.so

%files -n libglobipack%somver
%_libdir/libglobipack.so.*

%files -n libglobipack%somver-devel
%_libdir/libglobipack.so

%files -n libseacas%somver
%_libdir/libIoex.so.*
%_libdir/libIogn.so.*
%_libdir/libIohb.so.*
%_libdir/libIonit.so.*
%_libdir/libIopg.so.*
%_libdir/libIoss.so.*
%_libdir/libIotr.so.*
%_libdir/libIoxf.so.*
%_libdir/libaprepro_lib.so.*
%_libdir/libexodus*.so.*
%_libdir/libsupes.so.*
%_libdir/libsuplib.so.*
%_libdir/libchaco.so.*
%_libdir/libmapvarlib.so.*

%files -n libseacas%somver-devel
%_libdir/libIoex.so
%_libdir/libIogn.so
%_libdir/libIohb.so
%_libdir/libIonit.so
%_libdir/libIopg.so
%_libdir/libIoss.so
%_libdir/libIotr.so
%_libdir/libIoxf.so
%_libdir/libaprepro_lib.so
%_libdir/libexodus*.so
%_libdir/libsupes.so
%_libdir/libsuplib.so
%_libdir/libchaco.so
%_libdir/libmapvarlib.so

%files -n libseacas%somver-apps
%_libdir/libepu_lib.so.*
%_libdir/*app_lib*.so.*

%files -n libseacas%somver-apps-devel
%_libdir/libepu_lib.so
%_libdir/*app_lib*.so

%files -n seacas%somver-apps
%_bindir/*
%exclude %_bindir/phalanx_create_evaluator.py

%if_with dakota
%files -n libtrikota%somver
%_libdir/libtrikota.so.*

%files -n libtrikota%somver-devel
%_libdir/libtrikota.so
%else
%files -n libtrikota%somver

%files -n libtrikota%somver-devel
%endif

%changelog
* Wed Jul 04 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 10.10.0-alt4
- Rebuilt with Dakota

* Sun Jul 01 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 10.10.0-alt3
- Rebuilt with OpenMPI 1.6 (without Dakota)

* Fri Jun 08 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 10.10.0-alt2
- Fixed build

* Wed Feb 15 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 10.10.0-alt1
- Version 10.10.0

* Fri Jan 27 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 10.8.5-alt1
- Version 10.8.5

* Thu Dec 15 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 10.8.3-alt3
- Fixed build with superlu_dist 3.0

* Thu Dec 08 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 10.8.3-alt2
- Disabled links to libnem_spread_app_lib.so

* Tue Dec 06 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 10.8.3-alt1
- Version 10.8.3

* Sat Dec 03 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 10.8.1-alt3
- Avoid conflict with libchaco-devel

* Thu Dec 01 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 10.8.1-alt2
- Built with Dakota

* Thu Nov 24 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 10.8.1-alt1
- Version 10.8.1 (bootstrap: without Dakota)
- Added SEACAS libraries and applications

* Sat Oct 22 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 10.6.4-alt7.1
- Rebuild with Python-2.7

* Wed Sep 14 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 10.6.4-alt7
- Rebuilt with libparmetis0 instead of libparmetis
- Build with Xdmf and Nemesis

* Wed Sep 07 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 10.6.4-alt6
- Rebuilt with libhdf5-7-mpi

* Mon Jul 25 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 10.6.4-alt5
- Rebuilt with Boost 1.47.0

* Sun Apr 24 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 10.6.4-alt4
- Rebuilt with libnetcdf7

* Fri Apr 22 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 10.6.4-alt3
- Rebuilt with Dakota 5.1

* Sat Apr 09 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 10.6.4-alt2
- Built with GotoBLAS2 instead of ATLAS

* Sun Mar 27 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 10.6.4-alt1
- Version 10.6.4

* Sat Mar 19 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 10.6.1-alt6
- Built with Dakota, ExodusII and Sparskit
- Added TriKota package

* Wed Mar 16 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 10.6.1-alt5
- Rebuilt with Boost 1.46.1

* Thu Mar 03 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 10.6.1-alt4
- Rebuilt for debuginfo

* Fri Feb 25 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 10.6.1-alt3
- Rebuilt with parmetis 3.1.1-alt10

* Wed Nov 24 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 10.6.1-alt2
- Rebuilt for soname set-versions

* Sun Nov 14 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 10.6.1-alt1
- Version 10.6.1

* Wed Oct 13 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 10.2.0-alt4
- Fixed linking

* Wed Jul 07 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 10.2.0-alt3
- Rebuilt with reformed ParMetis

* Thu Jun 17 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 10.2.0-alt2
- Rebuilt with superlu_dist 2.4

* Fri Apr 23 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 10.2.0-alt1 - Version 10.2.0
- Added libraries: libmesquite, liboptika, libpiro, libstokhos, libSTK

* Thu Feb 18 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 10.0.2-alt6
- Fixed file conflicts with libemotion-devel

* Fri Feb 05 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 10.0.2-alt5
- Rebuilt with reformed NumPy

* Tue Jan 12 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 10.0.2-alt4
- Obsoletes old docs packages

* Tue Jan 05 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 10.0.2-alt3
- Rebuilt with new NumPy

* Tue Dec 22 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 10.0.2-alt2
- Rebuilt with TBB and SuperLU 4.0

* Wed Dec 16 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 10.0.2-alt0.M51.1
- Port for branch 5.1

* Sun Dec 06 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 10.0.2-alt1
- Version 10.0.2

* Sun Oct 18 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 9.0.3-alt10
- Cleaned spec (inspired by damir@)
- Moved all headers into one package: %name-headers
- Optimized requirements
- Rebuilt with texlive instead of tetex
- Added python-module-PySundance package

* Sun Sep 27 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 9.0.3-alt9
- Rebuilt with TAUCS

* Tue Sep 22 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 9.0.3-alt8
- Added Makefile.export.zoltan*

* Fri Sep 11 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 9.0.3-alt7
- Changed requirement in pkg-config file: scalapack-full -> scalapack

* Sun Sep 06 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 9.0.3-alt6.1
- Fixed linking PyTrilinos with OpenMPI libraries

* Sat Sep 05 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 9.0.3-alt6
- Rebuilt with shared libraries of requirements instead static

* Tue Aug 25 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 9.0.3-alt5.1
- Fixed export's Makefiles

* Thu Aug 20 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 9.0.3-alt5
- Configured Teuchos with support for expat
- Moved PyTrilinos docs into %%_libdir/%%name
- libnox-devel-doc: added explicit conflict with libqwt-devel
- Fixed PyTrilinos examples: exEpetra and exEpetra_ImportExport
- Added examples for subpackages
- Fixed Sundance's TSFVectorSpace2EpetraMap
- Added pkg-config file

* Tue Aug 18 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 9.0.3-alt4
+ Enabled
  - shared libraries
  - additional interactions of subpackages
  - python interface
	- documentation of subpackages
- Built with additional parallel mathematical packages

* Fri Jun 12 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 9.0.3-alt3
- Rebuild with HDF5 (MPI version) and SUNDIALS

* Tue May 19 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 9.0.3-alt2
- Rename package libml-devel to libml-devel-static

* Sun May 10 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 9.0.3-alt1
- Initial build for Sisyphus
