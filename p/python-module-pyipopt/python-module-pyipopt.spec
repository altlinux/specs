%define mpiimpl openmpi
%define mpidir %_libexecdir/%mpiimpl

%define oname pyipopt
Name: python-module-%oname
Version: 1.0
Release: alt3.git20140116
Summary: Python interface to Ipopt
License: Artistic License/GPL
Group: Development/Python
Url: https://github.com/xuy/pyipopt

# https://github.com/xuy/pyipopt.git
Source: %oname-%version.tar.gz

%setup_python_module %oname
BuildPreReq: python-devel libnumpy-devel libipopt-devel gcc-fortran
BuildPreReq: %mpiimpl-devel liblapack-devel

%description
Ipopt is a state-of-the-art optimization solver for nonlinear
optimization problems. Unfortunately, the only interface available is
C/C++ or Fortran. As Python becomes more popular these days, a connector
to python is necessary.

%package examples
Summary: Examples for Python interface to Ipopt
Group: Development/Python
BuildArch: noarch

%description examples
Ipopt is a state-of-the-art optimization solver for nonlinear
optimization problems. Unfortunately, the only interface available is
C/C++ or Fortran. As Python becomes more popular these days, a connector
to python is necessary.

%prep
%setup

%install
export OMPI_LDFLAGS="-Wl,--as-needed,-Rpath=%mpidir/lib -L%mpidir/lib"

%add_optflags -fno-strict-aliasing -I%_includedir/coin
%python_build_debug
%python_install

%files
%doc Changelog README.md
%python_sitelibdir/*

%files examples
%doc examples/*

%changelog
* Mon Nov 20 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 1.0-alt3.git20140116
- Rebuilt with new libipopt.

* Mon Jul 14 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0-alt2.git20140116
- New snapshot

* Wed Aug 15 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0-alt1.svn20120531
- New snapshot

* Thu Apr 12 2012 Vitaly Kuznetsov <vitty@altlinux.ru> 1.0-alt1.svn20110318.1.1
- Rebuild to remove redundant libpython2.7 dependency

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.0-alt1.svn20110318.1
- Rebuild with Python-2.7

* Mon May 16 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0-alt1.svn20110318
- Version 1.0

* Sat Mar 26 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.7-alt4.svn20090825.4
- Rebuilt for debuginfo

* Sun Oct 17 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.7-alt4.svn20090825.3
- Fixed linking

* Sat Mar 06 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.7-alt4.svn20090825.2
- Rebuilt with reformed NumPy

* Wed Dec 16 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.7-alt4.svn20090825.0.M51.1
- Port for branch 5.1

* Wed Nov 11 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.7-alt4.svn20090825.1
- Rebuilt with python 2.6

* Mon Nov 02 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.7-alt4.svn20090825
- New snapshot
- Rebuilt without udapl support

* Sat Sep 05 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.7-alt3
- Rebuilt with ipopt-3.7.0-alt2

* Tue Aug 04 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.7-alt2
- Fixed linking with OpenMPI

* Tue Aug 04 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.7-alt1
- Initial build for Sisyphus

