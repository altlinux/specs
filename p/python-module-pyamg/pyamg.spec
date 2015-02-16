%define oname pyamg

%def_without python3
%def_disable check

Name: python-module-%oname
Version: 2.2.1
Release: alt1
Summary: PyAMG: Algebraic Multigrid Solvers in Python
License: BSD
Group: Development/Python
Url: http://code.google.com/p/pyamg/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-devel libnumpy-devel gcc-c++
BuildPreReq: python-module-sphinx-devel python-module-scipy
BuildPreReq: python-module-nose
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel libnumpy-py3-devel python3-module-scipy
BuildPreReq: python3-module-nose
%endif

%py_requires numpy scipy
%add_python_req_skip example

%description
PyAMG is a library of Algebraic Multigrid (AMG) solvers with a
convenient Python interface.

%package -n python3-module-%oname
Summary: PyAMG: Algebraic Multigrid Solvers in Python
Group: Development/Python3
%py3_requires numpy scipy
%add_python3_req_skip example

%description -n python3-module-%oname
PyAMG is a library of Algebraic Multigrid (AMG) solvers with a
convenient Python interface.

%package -n python3-module-%oname-tests
Summary: Tests for PyAMG
Group: Development/Python3
Requires: python3-module-%oname = %EVR

%description -n python3-module-%oname-tests
PyAMG is a library of Algebraic Multigrid (AMG) solvers with a
convenient Python interface.

This package contains tests for PyAMG.

%package docs
Summary: Documentation for PyAMG
Group: Development/Documentation
BuildArch: noarch

%description docs
PyAMG is a library of Algebraic Multigrid (AMG) solvers with a
convenient Python interface.

This package contains documentation for PyAMG.

%package pickles
Summary: Pickles for PyAMG
Group: Development/Python

%description pickles
PyAMG is a library of Algebraic Multigrid (AMG) solvers with a
convenient Python interface.

This package contains pickles for PyAMG.

%package tests
Summary: Tests for PyAMG
Group: Development/Python
Requires: %name = %EVR

%description tests
PyAMG is a library of Algebraic Multigrid (AMG) solvers with a
convenient Python interface.

This package contains tests for PyAMG.

%prep
%setup

%if_with python3
cp -fR . ../python3
%endif

%prepare_sphinx Docs
ln -s ../objects.inv Docs/source/

%build
%python_build_debug

%if_with python3
pushd ../python3
%python3_build_debug
popd
%endif

%install
%python_install

%if_with python3
pushd ../python3
%python3_install
popd
%endif

export PYTHONPATH=%buildroot%python_sitelibdir
%make -C Docs html
%make -C Docs pickle

cp -fR Docs/build/pickle %buildroot%python_sitelibdir/%oname/

%check
python setup.py build_ext -i
nosetests -v
%if_with python3
pushd ../python3
python3 setup.py build_ext -i
nosetests3 -v
popd
%endif

%files
%doc *.txt *.md
%python_sitelibdir/*
%exclude %python_sitelibdir/*/testing
%exclude %python_sitelibdir/*/tests
%exclude %python_sitelibdir/*/*/tests
%exclude %python_sitelibdir/*/*/example*
%exclude %python_sitelibdir/*/pickle

%files docs
%doc Docs/build/html Docs/diagrams Docs/dev

%files pickles
%python_sitelibdir/*/pickle

%files tests
%python_sitelibdir/*/testing
%python_sitelibdir/*/tests
%python_sitelibdir/*/*/tests
%python_sitelibdir/*/*/example*

%if_with python3
%files -n python3-module-%oname
%doc *.txt *.md
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/testing
%exclude %python3_sitelibdir/*/tests
%exclude %python3_sitelibdir/*/*/tests
%exclude %python3_sitelibdir/*/*/example*
%exclude %python3_sitelibdir/*/*/*/example*

%files -n python3-module-%oname-tests
%python3_sitelibdir/*/testing
%python3_sitelibdir/*/tests
%python3_sitelibdir/*/*/tests
%python3_sitelibdir/*/*/example*
%python3_sitelibdir/*/*/*/example*
%endif

%changelog
* Mon Feb 16 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.2.1-alt1
- Version 2.2.1

* Sat Jul 19 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.1.0-alt2
- Avoid requirement on pythonX.Y(example)

* Wed Sep 18 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.1.0-alt1
- Version 2.1.0

* Fri Feb 15 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.0.5-alt2
- Moved examples into tests subpackage

* Thu Feb 14 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.0.5-alt1
- Initial build for Sisyphus

