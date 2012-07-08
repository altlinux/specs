%define mpiimpl openmpi
%define mpidir %_libdir/%mpiimpl

%define oname slepc4py
%define scalar_type complex
%define ldir %_libdir/petsc-%scalar_type

%def_enable docs

Name: %oname-%scalar_type
Version: 1.2
Release: alt3.hg20111105
Summary: SLEPc for Python (%scalar_type scalars)
License: Public
Group: Sciences/Mathematics
Url: http://slepc4py.googlecode.com/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# hg clone https://code.google.com/p/slepc4py/
Source: %oname-%version.tar.gz

Requires: python-module-%name = %version-%release
BuildRequires(pre): rpm-build-python rpm-macros-make
BuildPreReq: python-devel python-module-Cython chrpath
BuildPreReq: %mpiimpl-devel libslepc-%scalar_type-devel python-module-mpi4py
BuildPreReq: libnumpy-devel python-module-petsc4py-%scalar_type
BuildPreReq: python-module-docutils python-module-epydoc
%if "%scalar_type" == "real"
BuildPreReq: python-module-Pygments
BuildPreReq: texlive-latex-extra
%endif
BuildPreReq: libtrilinos10-devel libamesos10-devel libepetraext10-devel
BuildPreReq: libifpack10-devel python-module-sphinx-devel

%description
slepc4py are Python bindings for SLEPc, the Scalable Library for Eigenvalue
Problem Computations.

%package -n python-module-%name
Summary: Python module of SLEPc for Python (%scalar_type scalars)
Group: Development/Python
%setup_python_module %oname
Provides: python%_python_version(%oname) = %version-%release
%py_provides %oname
Requires: libslepc-%scalar_type python-module-petsc4py-%scalar_type
Requires: python-module-mpi4py

%description -n python-module-%name
slepc4py are Python bindings for SLEPc, the Scalable Library for Eigenvalue
Problem Computations.

This package contains Python module of SLEPc for Python
(%scalar_type scalars).

%if_enabled docs

%package -n python-module-%name-pickles
Summary: Pickles for Python module of SLEPc for Python (%scalar_type scalars)
Group: Development/Python

%description -n python-module-%name-pickles
slepc4py are Python bindings for SLEPc, the Scalable Library for Eigenvalue
Problem Computations.

This package contains pickles for Python module of SLEPc for Python
(%scalar_type scalars).

%package -n %oname-doc
Summary: Documentation for SLEPc for Python
Group: Development/Documentation
BuildArch: noarch

%description -n %oname-doc
slepc4py are Python bindings for SLEPc, the Scalable Library for Eigenvalue
Problem Computations.

This package contains documentation for SLEPc for Python.

%endif

%package -n %oname-examples
Summary: Examples for SLEPc for Python
Group: Development/Documentation
BuildArch: noarch

%description -n %oname-examples
slepc4py are Python bindings for SLEPc, the Scalable Library for Eigenvalue
Problem Computations.

This package contains examples for SLEPc for Python.

%prep
%setup
sed -i 's|@VERSION@|%version|' docs/source/conf.py
sed -i "s|@TOP@|$PWD|" docs/source/conf.py
sed -i 's|@PYVER@|%_python_version|' docs/source/Makefile

%if_enabled docs
%prepare_sphinx docs/source
%endif

%build
mpi-selector --set %mpiimpl
source %_bindir/petsc-%scalar_type.sh
export OMPI_LDFLAGS="-Wl,--as-needed,-rpath,%mpidir/lib -L%mpidir/lib"

%add_optflags %optflags_shared
%make_ext config
python conf/cythonize.py
%make_build_ext

%install
source %_bindir/petsc-%scalar_type.sh
export OMPI_LDFLAGS="-Wl,--as-needed,-rpath,%mpidir/lib -L%mpidir/lib"

%python_install --optimize=2

install -d %buildroot%ldir/python
mv %buildroot%python_sitelibdir/* %buildroot%ldir/python/

%if "%scalar_type" == "real"
export PYTHONPATH=$PYTHONPATH:%buildroot%ldir/python
install -d %buildroot%_docdir/%oname-%version/examples

%if_enabled docs
%make docs
pushd docs/source
%make_build latex
cp -fR build/html %buildroot%_docdir/%oname-%version/
popd
%make epydoc

install -p -m644 docs/*.pdf \
	%buildroot%_docdir/%oname-%version
cp -fR docs/apiref docs/usrman %buildroot%_docdir/%oname-%version/
%endif

install -p -m644 demo/* \
	%buildroot%_docdir/%oname-%version/examples

%if_enabled docs
sed -i 's|%buildroot||g' \
	%buildroot%_docdir/%oname-%version/apiref/epydoc-log.html
%endif

%else
%if_enabled docs
pushd docs/source
%make_build pickle
popd
%endif
%endif
%if_enabled docs
cp -fR docs/source/build/pickle %buildroot%ldir/python/%oname/
%endif

chrpath -r %mpidir/lib:%ldir/lib \
	%buildroot%ldir/python/%oname/lib/SLEPc.so

%pre
rm -f %ldir/python/%oname/lib/SLEPc.so

%files
%doc HISTORY.txt LICENSE.txt

%files -n python-module-%name
%dir %ldir/python
%ldir/python/*
%if_enabled docs
%exclude %ldir/python/%oname/pickle
%endif

%if_enabled docs
%files -n python-module-%name-pickles
%dir %ldir/python
%dir %ldir/python/%oname
%ldir/python/%oname/pickle
%endif

%if "%scalar_type" == "real"
%if_enabled docs
%files -n %oname-doc
%doc %dir %_docdir/%oname-%version
%doc %_docdir/%oname-%version/apiref
%doc %_docdir/%oname-%version/usrman
%doc %_docdir/%oname-%version/html
%doc %_docdir/%oname-%version/*.pdf
%endif

%files -n %oname-examples
%doc %dir %_docdir/%oname-%version
%doc %_docdir/%oname-%version/examples
%endif

%changelog
* Fri Jul 06 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.2-alt3.hg20111105
- Rebuilt with OpenMPI 1.6

* Sat Jun 02 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.2-alt2.hg20111105
- Rebuilt with new SLEPc

* Mon Apr 16 2012 Vitaly Kuznetsov <vitty@altlinux.ru> 1.2-alt1.hg20111105.1
- Rebuild to remove redundant libpython2.7 dependency

* Mon Dec 05 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.2-alt1.hg20111105
- Version 1.2

* Sat Oct 22 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.1-alt1.hg20110506.1
- Rebuild with Python-2.7

* Thu May 12 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1-alt1.hg20110506
- New snapshot

* Tue Apr 05 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1-alt1.hg20110312.1
- Rebuilt with python-module-sphinx-devel

* Wed Mar 30 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1-alt1.hg20110312
- New snapshot

* Sun Mar 06 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1-alt1.hg20101001.1
- Rebuilt for debuginfo

* Tue Nov 16 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1-alt1.hg20101001
- Version 1.1

* Mon Oct 18 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.0-alt6.hg20100804.2
- Fixed overlinking

* Mon Aug 30 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.0-alt6.hg20100804.1
- Removed paths to buildroot

* Thu Aug 05 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.0-alt6.hg20100804
- Rebuilt with SLEPc 3.1-p0

* Wed Mar 03 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.0-alt6.hg20090916.5
- Rebuilt with updated %%prepare_sphinx

* Sat Feb 06 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.0-alt6.hg20090916.4
- Rebuilt with reformed NumPy
- Added:
  + documentation in HTML
  + pickles package

* Tue Jan 05 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.0-alt6.hg20090916.3
- Rebuilt with new NumPy

* Wed Dec 16 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.0-alt6.hg20090916.1.M51.1
- Port for branch 5.1

* Sun Dec 06 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.0-alt6.hg20090916.2
- Rebuilt with Trilinos v10

* Mon Nov 16 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.0-alt6.hg20090916.1
- Rebuilt with python 2.6

* Fri Nov 06 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.0-alt6.hg20090916
- New snapshot
- Rebuilt with SLEPc 3.0.0_p7-alt1

* Mon Nov 02 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.0-alt5
- Rebuilt without udapl support

* Thu Sep 10 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.0-alt4
- Rebuild with SLEPc-3.0.0_p5-alt1

* Tue Aug 18 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.0-alt3
- Rebuild with SLEPc-3.0.0_p4-alt3

* Thu Jul 23 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.0-alt2
- Rebuild with python 2.6

* Sun Jul 19 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.0-alt1.1
- Fixed linking of python library

* Sat Jul 18 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.0-alt1
- Initial build for Sisyphus

