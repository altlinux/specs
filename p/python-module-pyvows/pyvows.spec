%define oname pyvows
Name: python-module-%oname
Version: 2.0.6
Release: alt1.git20141008.1
Summary: pyVows is a BDD test engine based on Vows.js (http://vowsjs.org )
License: MIT
Group: Development/Python
Url: https://pypi.python.org/pypi/pyVows/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/heynemann/pyvows.git
Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-module-setuptools python-module-gevent
BuildPreReq: python-module-preggy python-module-argparse
BuildPreReq: python-module-colorama python-module-coverage
BuildPreReq: python-module-six python-module-unidecode

%py_provides %oname

%description
pyVows is a test engine based on Vows.js. It features topic-based
testing, (fast) parallel running of tests, code coverage reports, test
profiling, and more: http://pyvows.org

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR

%description tests
pyVows is a test engine based on Vows.js. It features topic-based
testing, (fast) parallel running of tests, code coverage reports, test
profiling, and more: http://pyvows.org

This package contains tests for %oname.

%prep
%setup

%build
%python_build_debug

%install
%python_install

%check
python setup.py test
%make vows test
%make ci_test

%files
%doc *.md
%_bindir/*
%python_sitelibdir/*
%exclude %python_sitelibdir/*/*/test.*

%files tests
%python_sitelibdir/*/*/test.*

%changelog
* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 2.0.6-alt1.git20141008.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Fri Nov 21 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.0.6-alt1.git20141008
- Initial build for Sisyphus

