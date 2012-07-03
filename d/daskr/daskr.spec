%define sover 0
Name: daskr
Version: 2011.06.08
Release: alt1
Summary: Differential-algebraic system solver with rootfinding
License: BSD
Group: Sciences/Mathematics
Url: http://www.netlib.org/ode/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# http://www.netlib.org/ode/daskr.tgz
Source: %name-%version.tar

BuildPreReq: gcc-fortran

%description
DASKR is a solver for systems of differential-algebraic equations
(DAEs). It includes options for both direct and iterative (Krylov)
methods for the solution of the linear systems arising at each
(implicit) time step.  DASKR is a variant of the DASPK package. In
addition to all the capabilities of DASPK, DASKR includes the ability to
find the roots of a given set of functions while integrating the DAE
system.

%package -n lib%name
Summary: Shared libraries of DASKR
Group: System/Libraries

%description -n lib%name
DASKR is a solver for systems of differential-algebraic equations
(DAEs). It includes options for both direct and iterative (Krylov)
methods for the solution of the linear systems arising at each
(implicit) time step.  DASKR is a variant of the DASPK package. In
addition to all the capabilities of DASPK, DASKR includes the ability to
find the roots of a given set of functions while integrating the DAE
system.

This package contains shared library of DASKR.

%package -n lib%name-devel
Summary: Development files of DASKR
Group: Development/Other
Requires: lib%name = %version-%release

%description -n lib%name-devel
DASKR is a solver for systems of differential-algebraic equations
(DAEs). It includes options for both direct and iterative (Krylov)
methods for the solution of the linear systems arising at each
(implicit) time step.  DASKR is a variant of the DASPK package. In
addition to all the capabilities of DASPK, DASKR includes the ability to
find the roots of a given set of functions while integrating the DAE
system.

This package contains development files of DASKR.

%package examples
Summary: Examples for DASKR
Group: Development/Documentation
BuildArch: noarch

%description examples
DASKR is a solver for systems of differential-algebraic equations
(DAEs). It includes options for both direct and iterative (Krylov)
methods for the solution of the linear systems arising at each
(implicit) time step.  DASKR is a variant of the DASPK package. In
addition to all the capabilities of DASPK, DASKR includes the ability to
find the roots of a given set of functions while integrating the DAE
system.

This package contains examples for DASKR.

%prep
%setup

%build
g77 -c %optflags %optflags_shared preconds/*.f solver/*.f

g77 -shared d*.o -o lib%name.so.%sover \
	-Wl,-soname,lib%name.so.%sover

g77 -shared s*.o -o libs%name.so.%sover \
	-Wl,-soname,libs%name.so.%sover

%install
install -d %buildroot%_libdir
install -m644 *.so.* %buildroot%_libdir
ln -s lib%name.so.%sover %buildroot%_libdir/lib%name.so
ln -s libs%name.so.%sover %buildroot%_libdir/libs%name.so

%files -n lib%name
%doc README
%_libdir/*.so.*

%files -n lib%name-devel
%_libdir/*.so

%files examples
%doc examples/*

%changelog
* Thu Dec 01 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2011.06.08-alt1
- Version 2011.06.08

* Tue Apr 12 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2007.10.03-alt1
- Initial build for Sisyphus

