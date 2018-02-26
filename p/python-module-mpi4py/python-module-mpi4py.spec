%define mpiimpl openmpi
%define mpidir %_libdir/%mpiimpl
%define oname mpi4py

%def_with python3

Name: python-module-%oname
Version: 1.3
Release: alt2.hg20120510
Summary: MPI bindings for Python
License: Public
Group: Development/Python
Url: http://www.cimec.org.ar/python/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# hg clone https://code.google.com/p/mpi4py/
Source: %oname-%version.tar.gz

BuildRequires(pre): rpm-build-python rpm-macros-make
BuildPreReq: %mpiimpl-devel
BuildPreReq: python-devel python-module-Cython libmpe2-devel
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel python3-module-Cython
%endif
%setup_python_module %oname

%description
This package is constructed on top of the MPI-1
specification and provides an object oriented interface
which closely follows MPI-2 C++ bindings. It supports
point-to-point (sends, receives) and collective
(broadcasts, scatters, gathers) communications of any
*picklable* Python object.

%if_with python3
%package -n python3-module-%oname
Summary: MPI bindings for Python 3
Group: Development/Python3

%description -n python3-module-%oname
This package is constructed on top of the MPI-1
specification and provides an object oriented interface
which closely follows MPI-2 C++ bindings. It supports
point-to-point (sends, receives) and collective
(broadcasts, scatters, gathers) communications of any
*picklable* Python object.

%package -n python3-module-%oname-devel
Summary: Headers of MPI bindings for Python 3
Group: Development/Python3
Requires: python3-module-%oname = %version-%release
Requires: %mpiimpl-devel python3-devel

%description -n python3-module-%oname-devel
This package is constructed on top of the MPI-1
specification and provides an object oriented interface
which closely follows MPI-2 C++ bindings. It supports
point-to-point (sends, receives) and collective
(broadcasts, scatters, gathers) communications of any
*picklable* Python object.

This package contains headers of MPI bindings for Python.
%endif

%package devel
Summary: Headers of MPI bindings for Python
Group: Development/Python
Requires: %name = %version-%release
Requires: %mpiimpl-devel python-devel

%description devel
This package is constructed on top of the MPI-1
specification and provides an object oriented interface
which closely follows MPI-2 C++ bindings. It supports
point-to-point (sends, receives) and collective
(broadcasts, scatters, gathers) communications of any
*picklable* Python object.

This package contains headers of MPI bindings for Python.

%package doc
Summary: Documentation for mpi4py, MPI bindings for Python
Group: Development/Documentation
BuildArch: noarch

%description doc
Documentation for mpi4py, MPI bindings for Python.

%prep
%setup
%if_with python3
rm -rf ../python3
cp -a . ../python3
%endif

%build
source %mpidir/bin/mpivars.sh
export OMPI_LDFLAGS="-Wl,--as-needed,-rpath,%mpidir/lib -L%mpidir/lib"

sed -i 's|(MPIDIR)|%mpidir|' setup.cfg
%add_optflags -I%mpidir/include -I%_includedir/python%_python_version
%make_ext config
%make_build_ext

%if_with python3
%define optflags %optflags_default
unset CFLAGS
unset CXXFLAGS
unset FFLAGS
%add_optflags -I%mpidir/include -I%_includedir/python%_python3_version
sed -i 's|^PYTHON.*|PYTHON = python3|' makefile
%make_ext config
%make_build_ext
%endif

%install
source %mpidir/bin/mpivars.sh
export OMPI_LDFLAGS="-Wl,--as-needed,-rpath,%mpidir/lib -L%mpidir/lib"
export PATH=$PATH:%mpidir/bin

%if_with python3
OPTFLAGS="%optflags -I%mpidir/include -I%_includedir/python%_python3_version"
export CFLAGS="${OPTFLAGS}"
export CXXFLAGS="${OPTFLAGS}"
export FFLAGS="${OPTFLAGS}"
%python3_install --optimize=2
%endif

OPTFLAGS="%optflags -I%mpidir/include -I%_includedir/python%_python_version"
export CFLAGS="${OPTFLAGS}"
export CXXFLAGS="${OPTFLAGS}"
export FFLAGS="${OPTFLAGS}"
%python_install --optimize=2

install -d %buildroot%_docdir/%name
cp -fR docs/source %buildroot%_docdir/%name/

%files
%doc LICENSE.txt HISTORY.txt README.txt THANKS.txt
%python_sitelibdir/*
%exclude %python_sitelibdir/%oname/include

%files devel
%python_sitelibdir/%oname/include

%files doc
%_docdir/%name

%if_with python3
%files -n python3-module-%oname
%doc LICENSE.txt HISTORY.txt README.txt THANKS.txt
%python3_sitelibdir/*
%exclude %python3_sitelibdir/%oname/include

%files -n python3-module-%oname-devel
%python3_sitelibdir/%oname/include
%endif

%changelog
* Sun Jun 24 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.3-alt2.hg20120510
- Rebuilt with OpenMPI 1.6

* Sat May 12 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.3-alt1.hg20120510
- New snapshot
- Added module for Python 3

* Thu Apr 12 2012 Vitaly Kuznetsov <vitty@altlinux.ru> 1.3-alt1.hg20120120.1
- Rebuild to remove redundant libpython2.7 dependency

* Mon Jan 30 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.3-alt1.hg20120120
- Version 1.3

* Wed Dec 14 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.2.2-alt2.svn20110826
- Fixed RPATH

* Mon Oct 24 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.2.2-alt1.svn20110826.1
- Rebuild with Python-2.7

* Sun Aug 28 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.2.2-alt1.svn20110826
- Version 1.2.2

* Mon Mar 07 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.2.1-alt1.svn20100626.2
- Rebuilt with debuginfo
- Extracted headers into separate package

* Tue Oct 12 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.2.1-alt1.svn20100626.1
- Fixed overlinking of libraries

* Tue Jul 13 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.2.1-alt1.svn20100626
- Version 1.2.1

* Wed Dec 16 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.0-alt1.M51.1
- Port for branch 5.1

* Thu Jul 23 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.0-alt2
- Rebuild with python 2.6

* Sun May 17 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.0-alt1
- Initial build for Sisyphus

