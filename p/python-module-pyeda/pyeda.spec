%define oname pyeda

%def_without python2
%def_with python3
#def_disable check

Name: python-module-%oname
Version: 0.27.1
Release: alt1.git20150315
Summary: Python Electronic Design Automation
License: BSD
Group: Development/Python
Url: https://pypi.python.org/pypi/pyeda/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/cjdrake/pyeda.git
Source: %name-%version.tar

BuildRequires(pre): rpm-macros-sphinx
BuildPreReq: libpicosat-devel
%if_with python2
BuildPreReq: python-devel python-module-setuptools-tests
BuildPreReq: python-module-nose
%endif
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools-tests
BuildPreReq: python3-module-nose
%endif
BuildPreReq: python3-module-sphinx-devel

%py_provides %oname

%description
PyEDA is a Python library for electronic design automation.

Features:

* Symbolic Boolean algebra with a selection of function representations:
  * Logic expressions
  * Truth tables, with three output states (0, 1, "don't care")
  * Reduced, ordered binary decision diagrams (ROBDDs)
* SAT solvers:
  * Backtracking
  * PicoSAT
* Espresso logic minimization
* Formal equivalence
* Multi-dimensional bit vectors
* DIMACS CNF/SAT parsers
* Logic expression parser

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR

%description tests
PyEDA is a Python library for electronic design automation.

This package contains tests for %oname.

%if_with python3
%package -n python3-module-%oname
Summary: Python Electronic Design Automation
Group: Development/Python3
%py3_provides %oname

%description -n python3-module-%oname
PyEDA is a Python library for electronic design automation.

Features:

* Symbolic Boolean algebra with a selection of function representations:
  * Logic expressions
  * Truth tables, with three output states (0, 1, "don't care")
  * Reduced, ordered binary decision diagrams (ROBDDs)
* SAT solvers:
  * Backtracking
  * PicoSAT
* Espresso logic minimization
* Formal equivalence
* Multi-dimensional bit vectors
* DIMACS CNF/SAT parsers
* Logic expression parser

%package -n python3-module-%oname-tests
Summary: Tests for %oname
Group: Development/Python3
Requires: python3-module-%oname = %EVR

%description -n python3-module-%oname-tests
PyEDA is a Python library for electronic design automation.

This package contains tests for %oname.
%endif

%prep
%setup

%if_with python3
cp -fR . ../python3
%endif

%build
%if_with python2
%python_build_debug
%endif

%if_with python3
pushd ../python3
%python3_build_debug

%prepare_sphinx doc
ln -s ../objects.inv doc/source/
python3 setup.py build_ext -i
%make -C doc html
popd
%endif

%install
%if_with python2
%python_install
%endif

%if_with python3
pushd ../python3
%python3_install
popd
%endif

%check
%if_with python2
python setup.py test
%endif
%if_with python3
pushd ../python3
python3 setup.py test
popd
%endif

%if_with python2
%files
%doc *.rst ipynb/* doc/build/html
%python_sitelibdir/*
%exclude %python_sitelibdir/*/test
%exclude %python_sitelibdir/*/*/test

%files tests
%python_sitelibdir/*/test
%python_sitelibdir/*/*/test
%endif

%if_with python3
%files -n python3-module-%oname
%doc *.rst ipynb/* ../python3/doc/build/html
%_bindir/*
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/test
%exclude %python3_sitelibdir/*/*/test

%files -n python3-module-%oname-tests
%python3_sitelibdir/*/test
%python3_sitelibdir/*/*/test
%endif

%changelog
* Tue Mar 17 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.27.1-alt1.git20150315
- Initial build for Sisyphus

