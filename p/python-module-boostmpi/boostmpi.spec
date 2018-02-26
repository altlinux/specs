%define mpiimpl openmpi
%define mpidir %_libdir/%mpiimpl

%define oname boostmpi
Name: python-module-%oname
Version: 1.39
Release: alt5.git20091015
Summary: Boost MPI Python wrappers
License: Boost Software License V1
Group: Development/Python
Url: http://mathema.tician.de/software/boostmpi
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# http://git.tiker.net/trees/boostmpi.git
Source: %oname-%version.tar

BuildPreReq: %mpiimpl-devel boost-python-devel boost-mpi-devel
BuildPreReq: graphviz python-module-sphinx-devel

%description
boostmpi is a high-quality Python wrapper around the Message Passing
Interface (MPI). MPI is a standardized interface to libraries such as
OpenMPI and MPICH that provide high-performance inter-process
communication for distributed-memory computing.

boostmpi uses the Boost.MPI library, which gives MPI a very usable C++
interface. This C++ interface is then made accessible to Python via the
Boost.Python library.

%package devel
Summary: Development files of boostmpi
Group: Development/Python
BuildArch: noarch
Requires: %name = %version-%release

%description devel
boostmpi is a high-quality Python wrapper around the Message Passing
Interface (MPI). MPI is a standardized interface to libraries such as
OpenMPI and MPICH that provide high-performance inter-process
communication for distributed-memory computing.

boostmpi uses the Boost.MPI library, which gives MPI a very usable C++
interface. This C++ interface is then made accessible to Python via the
Boost.Python library.

This package contains development files of boostmpi.

%package devel-doc
Summary: Documentation for boostmpi
Group: Development/Documentation
BuildArch: noarch

%description devel-doc
boostmpi is a high-quality Python wrapper around the Message Passing
Interface (MPI). MPI is a standardized interface to libraries such as
OpenMPI and MPICH that provide high-performance inter-process
communication for distributed-memory computing.

boostmpi uses the Boost.MPI library, which gives MPI a very usable C++
interface. This C++ interface is then made accessible to Python via the
Boost.Python library.

This package contains development documentation for boostmpi.

%prep
%setup

%prepare_sphinx doc

%build
source %mpidir/bin/mpivars.sh
export OMPI_LDFLAGS="-Wl,--as-needed,-rpath,%mpidir/lib -L%mpidir/lib"

export LDFLAGS="$OMPI_LDFLAGS"
%python_build_debug

export PYTHONPATH=$PWD
%make -C doc html

%install
source %mpidir/bin/mpivars.sh
export OMPI_LDFLAGS="-Wl,--as-needed,-rpath,%mpidir/lib -L%mpidir/lib"

%python_install

%files
%python_sitelibdir/*

%files devel
%_includedir/*

%files devel-doc
%doc doc/build/html/*

%changelog
* Mon Jun 25 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.39-alt5.git20091015
- Rebuilt with OpenMPI 1.6

* Wed Apr 04 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.39-alt4.git20091015
- Rebuilt with Boost 1.49.0

* Wed Dec 14 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.39-alt3.git20091015
- Fixed RPATH

* Sat Dec 03 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.39-alt2.git20091015
- Rebuilt with Boost 1.48.0

* Mon Oct 24 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.39-alt1.git20091015.3.1
- Rebuild with Python-2.7

* Mon Jul 25 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.39-alt1.git20091015.3
- Rebuilt with Boost 1.47.0

* Tue Apr 05 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.39-alt1.git20091015.2
- Rebuilt with python-module-sphinx-devel

* Thu Mar 24 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.39-alt1.git20091015.1
- Rebuilt for debuginfo

* Mon Jan 03 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.39-alt1.git20091015
- Initial build for Sisyphus

