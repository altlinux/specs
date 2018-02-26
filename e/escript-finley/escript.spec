%define mpiimpl openmpi
%define mpidir %_libdir/%mpiimpl

Name: escript-finley
Version: 3.2.1
Release: alt3
Summary: Fast Finite Elements for Partial Differential Equations
License: OSLv3.0
Group: Sciences/Mathematics
Url: https://launchpad.net/escript-finley/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar
Source1: localhost_options.py

BuildPreReq: python-devel scons gcc-c++ boost-devel %mpiimpl-devel
BuildPreReq: libnetcdf-mpi-devel libnumpy-devel libparmetis-devel
BuildPreReq: boost-python-devel libpapi-devel libsuitesparse-devel
BuildPreReq: libsilo-devel libhdf5-mpi-devel gmsh
BuildPreReq: doxygen texlive-latex-recommended ghostscript-utils

Requires: lib%name = %version-%release

%description
Escript is a python-based programming tool for mathematical modelling
based on non-linear, time-dependent partial differential equations. It
has been designed to give modelers an easy-to-use environment for
develop and run complex and coupled models without accessing the
underlying data structures directly. This approach leads to highly
portable codes allowing the user to run a simulation on desktop
computers as well as highly parallel supercomputer with no changes to
the program. Escript is suitable for rapid prototyping (e.g for a
student project or thesis) as well as for large software projects. It
has successfully being used in a broad spectrum of applications
including Earth mantel convection, earthquakes, porous media flow,
reactive transport, plate subduction, and tsunamis.

%package -n lib%name
Summary: Shared libraries of Escript
Group: System/Libraries

%description -n lib%name
Escript is a python-based programming tool for mathematical modelling
based on non-linear, time-dependent partial differential equations. It
has been designed to give modelers an easy-to-use environment for
develop and run complex and coupled models without accessing the
underlying data structures directly. This approach leads to highly
portable codes allowing the user to run a simulation on desktop
computers as well as highly parallel supercomputer with no changes to
the program. Escript is suitable for rapid prototyping (e.g for a
student project or thesis) as well as for large software projects. It
has successfully being used in a broad spectrum of applications
including Earth mantel convection, earthquakes, porous media flow,
reactive transport, plate subduction, and tsunamis.

This package contains shared libraries of Escript.

%package devel
Summary: Development files of Escript
Group: Development/C++
BuildArch: noarch
Requires: lib%name = %version-%release
Requires: python-module-esys = %version-%release

%description devel
Escript is a python-based programming tool for mathematical modelling
based on non-linear, time-dependent partial differential equations. It
has been designed to give modelers an easy-to-use environment for
develop and run complex and coupled models without accessing the
underlying data structures directly. This approach leads to highly
portable codes allowing the user to run a simulation on desktop
computers as well as highly parallel supercomputer with no changes to
the program. Escript is suitable for rapid prototyping (e.g for a
student project or thesis) as well as for large software projects. It
has successfully being used in a broad spectrum of applications
including Earth mantel convection, earthquakes, porous media flow,
reactive transport, plate subduction, and tsunamis.

This package contains development files of Escript.

%package -n python-module-esys
Summary: Python module of Escript
Group: Development/Python
Requires: lib%name = %version-%release

%description -n python-module-esys
Escript is a python-based programming tool for mathematical modelling
based on non-linear, time-dependent partial differential equations. It
has been designed to give modelers an easy-to-use environment for
develop and run complex and coupled models without accessing the
underlying data structures directly. This approach leads to highly
portable codes allowing the user to run a simulation on desktop
computers as well as highly parallel supercomputer with no changes to
the program. Escript is suitable for rapid prototyping (e.g for a
student project or thesis) as well as for large software projects. It
has successfully being used in a broad spectrum of applications
including Earth mantel convection, earthquakes, porous media flow,
reactive transport, plate subduction, and tsunamis.

This package contains python module of Escript.

%package docs
Summary: Documentation for Escript
Group: Documentation
BuildArch: noarch

%description docs
Escript is a python-based programming tool for mathematical modelling
based on non-linear, time-dependent partial differential equations. It
has been designed to give modelers an easy-to-use environment for
develop and run complex and coupled models without accessing the
underlying data structures directly. This approach leads to highly
portable codes allowing the user to run a simulation on desktop
computers as well as highly parallel supercomputer with no changes to
the program. Escript is suitable for rapid prototyping (e.g for a
student project or thesis) as well as for large software projects. It
has successfully being used in a broad spectrum of applications
including Earth mantel convection, earthquakes, porous media flow,
reactive transport, plate subduction, and tsunamis.

This package contains documentation for Escript.

%prep
%setup
install -p -m644 %SOURCE1 scons

%ifarch x86_64
LIB_SUFF=64
%endif
sed -i "s|@LIB_SUFF@|$LIB_SUFF|" SConstruct scons/shake34_options.py \
	scons/shake75_options.py scons/guineapig_options.py \
	scons/badger_options.py scons/localhost_options.py
sed -i "s|@PYVER@|%_python_version|" SConstruct
sed -i "s|@BUILDROOT@|%buildroot|" SConstruct scons/localhost_options.py

%install
source %mpidir/bin/mpivars.sh
export OMPI_LDFLAGS="-Wl,--as-needed,-R,%mpidir/lib -L%mpidir/lib"

scons
install -m755 %buildroot%_libexecdir/pythonMPI* %buildroot%_bindir

mkdir -p release/doc/doxygen
scons api_doxygen
scons user_pdf
scons cookbook_pdf

chmod +x %buildroot%_bindir/*
%ifarch x86_64
mv %buildroot%_libexecdir/*.so %buildroot%_libdir/
%endif

install -d %buildroot%_docdir/%name
mv %buildroot/usr/release/doc/user/* \
	%buildroot/usr/release/doc/cookbook/* \
	release/doc/doxygen/* \
	%buildroot%_docdir/%name/
install -d %buildroot%_man1dir
install -p -m644 doc/manpage/man1/* %buildroot%_man1dir

%files
%doc CREDITS.txt README_LICENSE
%_bindir/*
%_man1dir/*

%files -n lib%name
%_libdir/*.so

%files devel
%_includedir/*

%files -n python-module-esys
%python_sitelibdir/*

%files docs
%doc %_docdir/%name
%doc doc/examples

%changelog
* Fri Jun 29 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.2.1-alt3
- Rebuilt with OpenMPI 1.6

* Wed Apr 04 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.2.1-alt2
- Rebuilt with Boost 1.49.0

* Wed Dec 21 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.2.1-alt1
- Initial build for Sisyphus

