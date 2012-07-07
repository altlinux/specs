%define mpiimpl openmpi
%define mpidir %_libdir/%mpiimpl
#set_gcc_version 4.5

%def_enable docs

%define scalar_type real
%if "%scalar_type" == "real"
%define alttype complex
%else
%define alttype real
%endif

%define oname petsc4py
%define ldir %_libdir/petsc-%scalar_type
Name: %oname-%scalar_type
Version: 1.2
%define exampledir %_docdir/%oname-%version/examples
Release: alt2.hg20120531
Summary: PETSc for Python (%scalar_type scalars)
License: Public
Group: Sciences/Mathematics
Url: http://code.google.com/p/petsc4py
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# hg clone https://petsc4py.googlecode.com/hg/ petsc4py
Source: %oname-%version.tar.gz

Requires: python-module-%name = %version-%release

BuildPreReq: python-devel python-module-Pyro4 chrpath rpm-macros-make
BuildPreReq: %mpiimpl-devel libpetsc-%scalar_type-devel libnumpy-devel
BuildPreReq: libmpe2-devel libhdf5-mpi-devel libtriangle-devel libX11-devel
BuildPreReq: liby12m-devel libsundials-devel libsz2-devel zlib-devel
BuildPreReq: libexpat-devel libtetgen-devel python-module-mpi4py
BuildPreReq: python-module-sphinx-devel python-module-Pygments
BuildPreReq: texlive-latex-base /usr/bin/ssh
BuildPreReq: python-module-Cython gcc-c++ gcc-fortran libgomp-devel
%if "%scalar_type" == "complex"
BuildPreReq: libfftw3-mpi-devel
%endif
BuildPreReq: libamesos10 libepetraext10 libifpack10 libtrilinos10
BuildPreReq: libgaleri10
BuildPreReq: libamesos10-devel libepetraext10-devel libifpack10-devel

%description
Python bindings for PETSc (%scalar_type scalars).

%package -n python-module-%name
Summary: Python module with bindings for PETSc (%scalar_type scalars)
Group: Development/Python
%add_python_lib_path %ldir/python
%setup_python_module %oname
Provides: python%_python_version(%oname) = %version-%release
%py_provides %oname
Requires: %name = %version-%release

%description -n python-module-%name
Python module with bindings for PETSc (%scalar_type scalars)

Note: for work with this module You need run:
source %_bindir/%name.sh

%package -n %oname-examples
Summary: Examples for Python bindings for PETSc
Group: Development/Documentation
BuildArch: noarch
Provides: %name-examples = %version-%release
Conflicts: %name-examples < %version-%release
Obsoletes: %name-examples < %version-%release

%description -n %oname-examples
Examples for Python bindings for PETSc.

%if_enabled docs

%package -n python-module-%name-pickles
Summary: Pickles for Python bindings for PETSc
Group: Development/Documentation
Provides: %name-examples = %version-%release
Conflicts: %name-examples < %version-%release
Obsoletes: %name-examples < %version-%release

%description -n python-module-%name-pickles
Pickles for Python bindings for PETSc.

%package -n %oname-doc
Summary: Documentation for Python bindings for PETSc
Group: Development/Documentation
BuildArch: noarch
Provides: %name-doc = %version-%release
Conflicts: %name-doc < %version-%release
Obsoletes: %name-doc < %version-%release

%description -n %oname-doc
Documentation for Python bindings for PETSc.

%endif

%prep
%setup

sed -i 's|@PYVER@|%_python_version|g' docs/source/Makefile
rm -f src/petsc4py.PETSc.c
#rm -f src/*.c

%install
mpi-selector --set %mpiimpl
source %_bindir/petsc-%scalar_type.sh
export OMPI_LDFLAGS="-Wl,--as-needed,-rpath,%mpidir/lib -L%mpidir/lib"

#sed -i 's|@MPIDIR@|%mpidir|g' conf/core/confutils.py
#sed -i 's|@MPIIMPL@|%mpiimpl|g' conf/core/confutils.py
#sed -i "s|@PETSCDIR@|$PETSC_DIR|g" conf/core/confutils.py
#sed -i "s|@MPILIBS@||g" conf/core/confcore.py
%add_optflags %optflags_shared -fno-strict-aliasing
#python_build
%make_ext config
%make_ext cython
for i in SNESPythonGetContext PCPythonGetContext \
	PetscPythonRegisterAll MatPythonGetContext \
	KSPPythonGetContext TSPythonGetContext
do
sed -i \
	"s|\(PetscErrorCode $i\)|extern \"C\" \1|" \
	src/libpetsc4py/libpetsc4py.c
done
sed -i \
	"s|\(int import_libpetsc4py\)|extern \"C\" \1|" \
	src/libpetsc4py/libpetsc4py.c
%make_build_ext

%if_enabled docs
ln -s build/html/objects.inv docs/source/
%make -C docs/source html
%endif

%python_install

install -d %buildroot%ldir/python
mv %buildroot%python_sitelibdir/* \
	%buildroot%ldir/python/
sed -i 's|^\(PETSC_ARCH\).*|\1 =|' \
	%buildroot%ldir/python/%oname/lib/petsc.cfg

%if_enabled docs
install -d %buildroot%_docdir/%oname-%version
cp -fR docs/source/_build/html \
	%buildroot%_docdir/%oname-%version/
install -d %buildroot%python_sitelibdir/%name
cp -fR docs/source/_build/pickle \
	%buildroot%python_sitelibdir/%name/
%endif

install -d %buildroot%exampledir
sed -i 's|@EXAMPLES@|%exampledir|g' demo/kspsolve/test_mat_*.py
cp -fR demo/* %buildroot%exampledir/

# example modules

export PYTHONPATH=$PYTHONPATH:%buildroot%ldir/python
pushd demo/bratu2d
%make_build_ext bratu2df90
install -m644 *.so %buildroot%ldir/python
popd
pushd demo/poisson3d
#f2py -m del2lib -c del2lib.f90
%make_build_ext run del2lib.so poisson3d
install -m644 *.so %buildroot%ldir/python
install -d %buildroot%ldir/bin
install -m755 poisson3d %buildroot%ldir/bin
popd

for i in %buildroot%ldir/bin/poisson3d \
	%buildroot%ldir/python/%oname/lib/PETSc.so
do
	chrpath -r %mpidir/lib:%ldir/lib $i
done

%files
%doc HISTORY.txt LICENSE.txt README.txt
%ldir/bin/*

%files -n python-module-%name
%dir %ldir/python
%ldir/python/*

%if "%scalar_type" == "real"
%if_enabled docs
%files -n %oname-doc
%doc %dir %_docdir/%oname-%version
%doc %_docdir/%oname-%version/*
%exclude %_docdir/%oname-%version/examples
%endif

%files -n %oname-examples
%doc %dir %_docdir/%oname-%version
%doc %_docdir/%oname-%version/examples
%endif

%if_enabled docs
%files -n python-module-%name-pickles
%dir %python_sitelibdir/%name
%python_sitelibdir/%name/pickle
%endif

%changelog
* Fri Jul 06 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.2-alt2.hg20120531
- Changed native directory: %%_libexecdir/%name -> %%_libdir/%name

* Sat Jun 02 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.2-alt1.hg20120531
- New snapshot

* Mon Apr 16 2012 Vitaly Kuznetsov <vitty@altlinux.ru> 1.2-alt1.hg20120223.1
- Rebuild to remove redundant libpython2.7 dependency

* Fri Feb 24 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.2-alt1.hg20120223
- New snapshot

* Sun Dec 04 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.2-alt1.hg20111109
- Version 1.2

* Mon Nov 28 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1.2-alt2.hg20110505
- Rebuilt with docs (except pdf)

* Sat Oct 22 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.1.2-alt1.hg20110505.1
- Rebuild with Python-2.7

* Wed May 11 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1.2-alt1.hg20110505
- New snapshot

* Tue Apr 05 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1.2-alt1.hg20101112.2
- Rebuilt with python-module-sphinx-devel

* Mon Mar 07 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1.2-alt1.hg20101112.1
- Rebuilt for debuginfo

* Thu Nov 18 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1.2-alt1.hg20101112
- Version 1.1.2

* Tue Oct 26 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1-alt1.hg20100803.2
- Rebuilt for soname set-versions

* Fri Oct 15 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1-alt1.hg20100803.1
- Avoid --no-as-needed

* Thu Aug 05 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1-alt1.hg20100803
- New snapshot

* Mon Jul 19 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1-alt1.hg20100712.1
- Rebuilt with PETSc 3.1

* Tue Jul 13 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1-alt1.hg20100712
- Version 1.1

* Wed Jul 07 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.3-alt1.hg20100225.2
- Rebuilt with reformed ParMetis

* Fri Jun 18 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.3-alt1.hg20100225.1
- Rebuilt with superlu_dist 2.4

* Thu Mar 04 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.3-alt1.hg20100225
- Version 1.0.3
- Added pickles package

* Tue Jan 05 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.2-alt8.hg20091030.3
- Rebuild with new NumPy

* Wed Dec 16 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.2-alt8.hg20091030.1.M51.1
- Port for branch 5.1

* Sun Dec 06 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.2-alt8.hg20091030.2
- Rebuild with Trilinos v10

* Mon Nov 16 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.2-alt8.hg20091030.1
- Rebuilt with python 2.6

* Wed Nov 04 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.2-alt8.hg20091030
- New snapshot

* Mon Nov 02 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.2-alt7
- Rebuilt without udapl support

* Tue Sep 08 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.2-alt6
- Rebuilt with PETSc-3.0.0_p7-alt6
- Fixed examples and added example modules

* Tue Aug 18 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.2-alt5
- Rebuilt with PETSc-3.0.0_p7-alt5

* Tue Jul 28 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.2-alt4.1
- Renamed petsc4py-real-doc -> petsc4py-doc
  and petsc4py-real-examples -> petsc4py-examples

* Sun Jul 19 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.2-alt3
- Moved module files from %python_sitelibdir into %ldir/python

* Sat Jul 18 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.2-alt2
- Added link to Python module into PETSC_DIR/python

* Tue Jul 14 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.2-alt1
- Initial build for Sisyphus
