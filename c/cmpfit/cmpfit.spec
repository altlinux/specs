Name: cmpfit
Version: 1.2
Release: alt1
Summary: A MINPACK-1 Least Squares Fitting Library in C
License: BSD
Group: Sciences/Mathematics
Url: http://cow.physics.wisc.edu/~craigm/idl/cmpfit.html
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: rpm-macros-make

%description
MPFIT uses the Levenberg-Marquardt technique to solve the least-squares
problem. In its typical use, MPFIT will be used to fit a user-supplied
function (the "model") to user-supplied data points (the "data") by
adjusting a set of parameters. MPFIT is based upon MINPACK-1 (LMDIF.F)
by More' and collaborators.

%package -n lib%name
Summary: Shared library of MPFIT (a MINPACK-1 Least Squares Fitting Library in C)
Group: System/Libraries

%description -n lib%name
MPFIT uses the Levenberg-Marquardt technique to solve the least-squares
problem. In its typical use, MPFIT will be used to fit a user-supplied
function (the "model") to user-supplied data points (the "data") by
adjusting a set of parameters. MPFIT is based upon MINPACK-1 (LMDIF.F)
by More' and collaborators.

This package contains shared library of MPFIT.

%package -n lib%name-devel
Summary: Development files of MPFIT (a MINPACK-1 Least Squares Fitting Library in C)
Group: Development/C
Requires: lib%name = %version-%release

%description -n lib%name-devel
MPFIT uses the Levenberg-Marquardt technique to solve the least-squares
problem. In its typical use, MPFIT will be used to fit a user-supplied
function (the "model") to user-supplied data points (the "data") by
adjusting a set of parameters. MPFIT is based upon MINPACK-1 (LMDIF.F)
by More' and collaborators.

This package contains development files of MPFIT.

%package test
Summary: Test for MPFIT (a MINPACK-1 Least Squares Fitting Library in C)
Group: Sciences/Mathematics
Requires: lib%name = %version-%release

%description test
MPFIT uses the Levenberg-Marquardt technique to solve the least-squares
problem. In its typical use, MPFIT will be used to fit a user-supplied
function (the "model") to user-supplied data points (the "data") by
adjusting a set of parameters. MPFIT is based upon MINPACK-1 (LMDIF.F)
by More' and collaborators.

This package contains test for MPFIT.

%prep
%setup

%build
%add_optflags %optflags_shared
%make_build_ext

%install
%makeinstall_std LIB=%_lib

%check
export LD_LIBRARY_PATH=$PWD
./testmpfit

%files -n lib%name
%doc DISCLAIMER README
%_libdir/*.so.*

%files -n lib%name-devel
%_includedir/*
%_libdir/*.so

%files test
%_bindir/*

%changelog
* Tue Sep 04 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.2-alt1
- Initial build for Sisyphus

