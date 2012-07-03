%define mpiimpl openmpi
%define mpidir %_libdir/%mpiimpl

%define ver 2.5
%define Name pyMPI

Name: pympi
Version: %ver.b6
Release: alt11.cvs20120513
Summary: Implementation of MPI in python
License: Free for non-commertial using
Group: Networking/Other
Url: http://pympi.sourceforge.net/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# cvs -z3 -d:pserver:anonymous@pympi.cvs.sourceforge.net:/cvsroot/pympi co -P pyMPI
Source: %name-%version.tar.gz

Requires: python-module-%Name = %version-%release

BuildPreReq: %mpiimpl-devel gcc-c++ swig fonts-type1-urw lout
BuildPreReq: python-devel libnumpy-devel R-base

BuildPreReq: python-module-sphinx-devel python-module-Pygments

%description
pyMPI is an implementation of MPI in python. pyMPI is intended to
support fast development of actual or prototypical parallel
applications as well as provide a tool for teaching parallel
programming methods without the intricacies of higher level languages.

%package -n lib%name-devel
Summary: Static development files of pyMPI
Group: Development/C
Requires: python-module-%Name = %version-%release

%description -n lib%name-devel
pyMPI is an implementation of MPI in python. pyMPI is intended to
support fast development of actual or prototypical parallel
applications as well as provide a tool for teaching parallel
programming methods without the intricacies of higher level languages.

This package contains static libraries and headers of pyMPI.

%package -n python-module-%Name
Summary: Python interface to MPI
Group: Development/Python
%setup_python_module mpi
%setup_python_module %Name
%py_provides mpi %Name

%description -n python-module-%Name
pyMPI is an implementation of MPI in python. pyMPI is intended to
support fast development of actual or prototypical parallel
applications as well as provide a tool for teaching parallel
programming methods without the intricacies of higher level languages.

This package contains python interface to MPI.

%package -n python-module-%Name-examples
Summary: Examples for pyMPI
Group: Development/Documentation
Requires: python-module-%Name = %version-%release

%description -n python-module-%Name-examples
pyMPI is an implementation of MPI in python. pyMPI is intended to
support fast development of actual or prototypical parallel
applications as well as provide a tool for teaching parallel
programming methods without the intricacies of higher level languages.

This package contains examples for pyMPI.

%package -n python-module-%Name-pickles
Summary: Pickles for pyMPI
Group: Development/Python

%description -n python-module-%Name-pickles
pyMPI is an implementation of MPI in python. pyMPI is intended to
support fast development of actual or prototypical parallel
applications as well as provide a tool for teaching parallel
programming methods without the intricacies of higher level languages.

This package contains pickles for pyMPI.

%package doc
Summary: Documentation for pyMPI
Group: Development/Documentation
BuildArch: noarch

%description doc
pyMPI is an implementation of MPI in python. pyMPI is intended to
support fast development of actual or prototypical parallel
applications as well as provide a tool for teaching parallel
programming methods without the intricacies of higher level languages.

This package contains documentation for pyMPI.

%prep
%setup

ln -s overview.html docs/index.html
%prepare_sphinx docs

%build
mpi-selector --set %mpiimpl
source %mpidir/bin/mpivars.sh
export OMPI_LDFLAGS="-Wl,--as-needed,-rpath,%mpidir/lib -L%mpidir/lib"

INCS="-I%mpidir/include -I%_includedir/python%_python_version"
INCS="$INCS -I%_includedir/numpy"
%add_optflags $INCS -DPYMPI_HAS_NUMPY -UPYMPI_HAS_NUMERIC

ADDLIBS="-L%mpidir/lib -Wl,-R%mpidir/lib:%mpidir/lib/%mpiimpl"
ADDLIBS="$ADDLIBS -lmpi_cxx -lmpi"
sed -i 's|@LIBDIR@|%_libdir|g' configure.ac
sed -i 's|@PYDIR@|%python_libdir|g' configure.ac
sed -i 's|@PYINC@|%_includedir/python%_python_version|g' configure.ac
sed -i "s|@ADDLIBS@|$ADDLIBS|g" configure.ac
sed -i 's|@MPIDIR@|%mpidir|g' Makefile.am configure.ac
sed -i 's|@MPIIMPL@|%mpiimpl|g' Makefile.am configure.ac
sed -i 's|@PYVER@|%_python_version|g' Makefile.am

%autoreconf
%configure CC="mpicc -g $INCS"
sed -i 's|/\*\*/||g' pyMPI_Config.h
sed -i \
	's|%_libexecdir/%Name%ver|%_includedir/%Name%ver|' \
	pyMPI_Config.h
%make
sed -i "s|%_bindir/||" augmentedMakefile

for i in simple_extension advanced_extension scaling
do
	pushd $i
	CC="mpicc -g" CFLAGS="-I%mpidir/include -DHAVE_MPI" \
		LDFLAGS="$ADDLIBS" python setup.py build
	popd
done
mv advanced_extension/test.py advanced_test.py
mv simple_extension/test.py simple_test.py

pushd examples/fortran_with_communicators
mpif77 %optflags %optflags_shared -I%mpidir/include \
	-c something.F
mpif77 -shared -Wl,-soname,libsomething.so.0 -Wl,-R%mpidir/lib \
	-o libsomething.so.0 something.o
ln -s libsomething.so.0 libsomething.so
popd
for i in fortran_with_communicators using_parallel_C using_simple_serial_C
do
	pushd examples/$i
	CC="mpicc -g" CFLAGS="-I%mpidir/include" \
		LDFLAGS="-L%mpidir/lib -Wl,-R%mpidir/lib" \
		python setup.py build
	popd
done

pushd docs
%make_build
popd

%install
source %mpidir/bin/mpivars.sh
export OMPI_LDFLAGS="-Wl,--as-needed,-rpath,%mpidir/lib -L%mpidir/lib"

%makeinstall_std

install -d %buildroot%python_sitelibdir/%Name/examples
touch %buildroot%python_sitelibdir/%Name/__init__.py
install -d %buildroot%_docdir/%Name

for i in simple_extension advanced_extension scaling
do
	pushd $i
	%python_install
	popd
done

pushd examples/fortran_with_communicators
install -m644 *.so* %buildroot%_libdir
rm -f *.so* *.o
popd
for i in fortran_with_communicators using_parallel_C using_simple_serial_C
do
	pushd examples/$i
	install -m644 build/lib.*/*.so %buildroot%python_sitelibdir/%Name
	rm -fR build
	popd
done

mv %buildroot%_libexecdir/%Name%ver/site-packages/* \
	%buildroot%python_sitelibdir/
rmdir %buildroot%_libexecdir/%Name%ver/site-packages
mv %buildroot%_libexecdir/%Name%ver/augmentedMakefile \
	%buildroot%_libexecdir/%Name%ver/pyMPI.exp \
	%buildroot%_includedir/%Name%ver/
mv %buildroot%_libexecdir/%Name%ver/* \
	%buildroot%_libdir/
for i in advanced pingpong simple
do
	mv %buildroot%python_sitelibdir/$i.so \
		%buildroot%python_sitelibdir/%Name/
done

rm -f %buildroot%_bindir/%Name
ln -s %Name%ver %buildroot%_bindir/%Name
ln -s %Name%{ver}_linker %buildroot%_bindir/%{Name}_linker

rm -f softload_setup.py scaling/setup.py
install -m644 *.py scaling/*.py \
	%buildroot%python_sitelibdir/%Name/examples

install -p -m644 docs/*.pdf \
	%buildroot%_docdir/%Name
#install -p -m644 docs/*.html docs/*.ps \
install -p -m644 docs/*.html \
	%buildroot%_docdir/%Name

rm -f $(find examples -name setup.py)
cp -fR examples/* %buildroot%python_sitelibdir/%Name/examples

# pickles
pushd docs
cp conf.py %buildroot%python_sitelibdir/
%generate_pickles %buildroot%python_sitelibdir $PWD %Name
rm -f %buildroot%python_sitelibdir/conf.py
cp -fR pickle %buildroot%python_sitelibdir/%Name/
popd

%files
%doc AUTHORS ChangeLog COPYING LICENSE.TXT NEWS README
%_bindir/%Name
%_bindir/%Name%ver

%files -n lib%name-devel
%_bindir/%{Name}*_linker
%_includedir/*
%_libdir/*.a
%_libdir/*.so

%files -n python-module-%Name
%dir %python_sitelibdir/%Name
%python_sitelibdir/*
%exclude %python_sitelibdir/%Name/examples
%exclude %python_sitelibdir/%Name/pstencil.so
%exclude %python_sitelibdir/%Name/stencil.so
%exclude %python_sitelibdir/%Name/example.so
%exclude %python_sitelibdir/%Name/pingpong.so
%exclude %python_sitelibdir/%Name/pickle

%files -n python-module-%Name-pickles
%dir %python_sitelibdir/%Name
%python_sitelibdir/%Name/pickle

%files doc
%_docdir/%Name

%files -n python-module-%Name-examples
%_libdir/libsomething.so.*
%python_sitelibdir/%Name/examples
%python_sitelibdir/%Name/pstencil.so
%python_sitelibdir/%Name/stencil.so
%python_sitelibdir/%Name/example.so
%python_sitelibdir/%Name/pingpong.so

%changelog
* Sun Jun 24 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.5.b6-alt11.cvs20120513
- Rebuilt with OpenMPI 1.6

* Sat May 12 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.5.b6-alt10.cvs20120513
- New snapshot

* Thu Apr 12 2012 Vitaly Kuznetsov <vitty@altlinux.ru> 2.5.b6-alt10.cvs20111128.1
- Rebuild to remove redundant libpython2.7 dependency

* Wed Dec 14 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.5.b6-alt10.cvs20111128
- Fixed RPATH

* Mon Nov 28 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.5.b6-alt9.cvs20111128
- New snapshot

* Fri Nov 25 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.5.b6-alt9.cvs20101201
- Enabled pickles

* Wed Nov 23 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.5.b6-alt8.cvs20101201.2
- Enabled docs (except pdf)

* Sat Oct 22 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 2.5.b6-alt8.cvs20101201.1.1
- Rebuild with Python-2.7

* Tue Apr 05 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.5.b6-alt8.cvs20101201.1
- Rebuilt with python-module-sphinx-devel

* Mon Mar 21 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.5.b6-alt8.cvs20101201
- Rebuilt for debuginfo
- New snapshot

* Tue Oct 12 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.5.b6-alt8.cvs20100617.1
- Fixed linking

* Thu Jun 17 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.5.b6-alt8.cvs20100617
- New snapshot
- Rebuilt with NumPy 2.0.0

* Fri Mar 05 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.5.b6-alt8
- Rebuilt with reformed NumPy
- Added pickles package

* Tue Jan 05 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.5.b6-alt7
- Rebuilt with new NumPy

* Thu Dec 24 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.5.b6-alt6
- Really rebuild without python-module-Numeric

* Wed Dec 23 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.5.b6-alt5
- Rebuilt without python-module-Numeric

* Wed Dec 16 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.5.b6-alt3.M51.1
- Port for branch 5.1

* Wed Nov 18 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.5.b6-alt4
- Rebuilt with python 2.6

* Mon Nov 02 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.5.b6-alt3
- Rebuilt without udapl support

* Thu Aug 20 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.5.b6-alt2
- Set doc package as noarch

* Tue Aug 18 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.5.b6-alt1
- Initial build for Sisyphus

