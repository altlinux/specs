%define mpiimpl openmpi
%define mpidir %_libexecdir/%mpiimpl

%define oname pyipopt
Name: python-module-%oname
Version: 1.0
Release: alt1.svn20110318.1.1
Summary: Python interface to Ipopt
License: Artistic License/GPL
Group: Sciences/Mathematics
Url: http://code.google.com/p/pyipopt/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# http://pyipopt.googlecode.com/svn/trunk
Source: %oname-%version.tar.gz

%setup_python_module %oname
BuildPreReq: python-devel libnumpy-devel libipopt-devel gcc-fortran
BuildPreReq: %mpiimpl-devel liblapack-devel

%description
Ipopt is a state-of-the-art optimization solver for nonlinear
optimization problems. Unfortunately, the only interface available is
C/C++ or Fortran. As Python becomes more popular these days, a connector
to python is necessary.

%prep
%setup
sed -i 's|@PY_DIR@|%python_sitelibdir|g' makefile
sed -i \
	"s|@PY_INC@|$(pkg-config python --cflags|sed 's|\-I||g')|g" \
	makefile
sed -i "s|@PY_LIB@|$(pkg-config python --libs)|g" makefile

%install
export OMPI_LDFLAGS="-Wl,--as-needed,-Rpath=%mpidir/lib -L%mpidir/lib"

TOPDIR=$PWD
#pushd %mpidir/lib/%mpiimpl
#for i in $(ls *.so |sed -e 's/\.so//'); do
#	ln -s %mpidir/lib/%mpiimpl/$i.so $TOPDIR/lib$i.so
#	MCAS="$MCAS -l$i"
#done
MCAS="$MCAS -lompi_dbg_msgq -lmpi_cxx -lmpi_f77"
MCAS="-L$TOPDIR $MCAS -lmpi_f90 -lmpi -lopen-pal"
#popd

%make_build pyipopt \
	MPIDIR=%mpidir MPIIMPL=%mpiimpl MPILIBS="$MCAS"

%makeinstall_std \
	MPIDIR=%mpidir MPIIMPL=%mpiimpl MPILIBS="$MCAS"

%files
%doc README VERSION
%python_sitelibdir/*


%changelog
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

