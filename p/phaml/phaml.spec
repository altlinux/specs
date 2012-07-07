%define mpiimpl openmpi
%define mpidir %_libdir/%mpiimpl
%define pdir %_libdir/petsc-real

%define somver 0
%define sover %somver.0

Name: phaml
Version: 1.10.0
Release: alt3
Summary: The Parallel Hierarchical Adaptive MultiLevel Project
License: Public domain
Group: Sciences/Mathematics
Url: http://math.nist.gov/phaml/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: gcc-fortran %mpiimpl-devel libgotoblas-devel
BuildPreReq: liblapack-devel libslepc-real-devel libparpack-mpi-devel
BuildPreReq: libexodusii-devel libGLUT-devel libf90gl-devel
BuildPreReq: libXaw-devel libXmu-devel libXi-devel libXext-devel

%description
PHAML stands for Parallel Hierarchical Adaptive MultiLevel.  It solves
linear elliptic partial differential equations of the form
(CXX*Ux)x - (CXY*Uy)x + (CYY*Uy)y + CX*Ux + CY*Uy + C*U = F on 2D
domains with Dirichlet, Natural (often Neumann), mixed or periodic
boundary conditions, and eigenvalue problems where F is lambda*U and the
boundary conditions are homogeneous.  It uses linear or high order
finite elements over triangles, adaptive refinement (possibly
hp-adaptive), multigrid and message passing parallelism.

%package -n lib%name
Summary: Shared libraries of PHAML
Group: System/Libraries

%description -n lib%name
PHAML stands for Parallel Hierarchical Adaptive MultiLevel.  It solves
linear elliptic partial differential equations of the form
(CXX*Ux)x - (CXY*Uy)x + (CYY*Uy)y + CX*Ux + CY*Uy + C*U = F on 2D
domains with Dirichlet, Natural (often Neumann), mixed or periodic
boundary conditions, and eigenvalue problems where F is lambda*U and the
boundary conditions are homogeneous.  It uses linear or high order
finite elements over triangles, adaptive refinement (possibly
hp-adaptive), multigrid and message passing parallelism.

This package contains shared libraries of PHAML.

%package -n lib%name-devel
Summary: Development files of PHAML
Group: Development/Other
Requires: lib%name = %version-%release

%description -n lib%name-devel
PHAML stands for Parallel Hierarchical Adaptive MultiLevel.  It solves
linear elliptic partial differential equations of the form
(CXX*Ux)x - (CXY*Uy)x + (CYY*Uy)y + CX*Ux + CY*Uy + C*U = F on 2D
domains with Dirichlet, Natural (often Neumann), mixed or periodic
boundary conditions, and eigenvalue problems where F is lambda*U and the
boundary conditions are homogeneous.  It uses linear or high order
finite elements over triangles, adaptive refinement (possibly
hp-adaptive), multigrid and message passing parallelism.

This package contains development files of PHAML.

%package examples
Summary: Examples for PHAML
Group: Development/Documentation
BuildArch: noarch

%description examples
PHAML stands for Parallel Hierarchical Adaptive MultiLevel.  It solves
linear elliptic partial differential equations of the form
(CXX*Ux)x - (CXY*Uy)x + (CYY*Uy)y + CX*Ux + CY*Uy + C*U = F on 2D
domains with Dirichlet, Natural (often Neumann), mixed or periodic
boundary conditions, and eigenvalue problems where F is lambda*U and the
boundary conditions are homogeneous.  It uses linear or high order
finite elements over triangles, adaptive refinement (possibly
hp-adaptive), multigrid and message passing parallelism.

This package contains examples for PHAML.

%package doc
Summary: Documentation for PHAML
Group: Development/Documentation
BuildArch: noarch

%description doc
PHAML stands for Parallel Hierarchical Adaptive MultiLevel.  It solves
linear elliptic partial differential equations of the form
(CXX*Ux)x - (CXY*Uy)x + (CYY*Uy)y + CX*Ux + CY*Uy + C*U = F on 2D
domains with Dirichlet, Natural (often Neumann), mixed or periodic
boundary conditions, and eigenvalue problems where F is lambda*U and the
boundary conditions are homogeneous.  It uses linear or high order
finite elements over triangles, adaptive refinement (possibly
hp-adaptive), multigrid and message passing parallelism.

This package contains documentation for PHAML.

%prep
%setup

%build
source %_bindir/petsc-real.sh
export OMPI_LDFLAGS="-Wl,--as-needed,-R,%mpidir/lib:%pdir/lib -L%mpidir/lib -L%pdir/lib"

./mkmkfile.sh
mkdir -p lib modules
%make_build

%install
source %mpidir/bin/mpivars.sh
export OMPI_LDFLAGS="-Wl,--as-needed,-R,%mpidir/lib:%pdir/lib -L%mpidir/lib -L%pdir/lib"

install -d %buildroot%_includedir/%name
install -d %buildroot%_libdir

install -m644 modules/* %buildroot%_includedir/%name

pushd src
TOPDIR=$PWD
ar x lib%name.a
popd
pushd %buildroot%_libdir
mpif90 -shared $TOPDIR/*.o \
	-o lib%name.so.%sover -Wl,-soname,lib%name.so.%somver \
	-lpetsc -lslepc -lHYPRE -lzoltan -lf90glut -lf90GLU -lf90GL \
	-lglut -lGLU -lGL -llapack -lgoto2
	ln -s lib%name.so.%sover lib%name.so.%somver
	ln -s lib%name.so.%somver lib%name.so
popd

install -d %buildroot%_libexecdir/%name
cp -fR examples %buildroot%_libexecdir/%name/

%files -n lib%name
%doc README doc/AUXILLARY doc/HINTS doc/KNOWN_PROBLEMS doc/LICENSE
%_libdir/*.so.*

%files -n lib%name-devel
%_includedir/*
%_libdir/*.so

%files doc
%doc doc/*.pdf

%files examples
%_libexecdir/%name

%changelog
* Sat Jul 07 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.10.0-alt3
- Rebuilt with OpenMPI 1.6

* Wed Jun 13 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.10.0-alt2
- Rebuilt with gcc 4.6

* Tue Dec 20 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.10.0-alt1
- Initial build for Sisyphus

