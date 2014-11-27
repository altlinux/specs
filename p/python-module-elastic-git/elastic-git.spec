%define oname elastic-git
Name: python-module-%oname
Version: 0.3.1
Release: alt1.git20141127
Summary: JSON Object storage backed by Git & Elastic Search
License: BSD
Group: Development/Python
Url: https://pypi.python.org/pypi/elastic-git/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/universalcore/elastic-git.git
Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools-tests
BuildPreReq: python-module-confmodel python-module-elasticutils
BuildPreReq: python-module-GitPython python-module-jinja2
BuildPreReq: python-module-pytest python-module-pytest-cov
BuildPreReq: python-module-pytest-xdist python-module-sphinx-devel
BuildPreReq: python-module-sphinx_rtd_theme python-module-GitDB
BuildPreReq: python-module-sphinx-argparse python-module-unidecode

%py_provides elasticgit

%description
Adventures in an declarative object-y thing backed by Git and using
Elastic Search as a query backend.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR

%description tests
Adventures in an declarative object-y thing backed by Git and using
Elastic Search as a query backend.

This package contains tests for %oname.

%package pickles
Summary: Pickles for %oname
Group: Development/Python

%description pickles
Adventures in an declarative object-y thing backed by Git and using
Elastic Search as a query backend.

This package contains pickles for %oname.

%package docs
Summary: Documentation for %oname
Group: Development/Documentation
BuildArch: noarch

%description docs
Adventures in an declarative object-y thing backed by Git and using
Elastic Search as a query backend.

This package contains documentation for %oname.

%prep
%setup

%prepare_sphinx .
ln -s ../objects.inv docs/

%build
%python_build_debug

%install
%python_install

export PYTHONPATH=$PWD
%make -C docs pickle
%make -C docs html

install -d %buildroot%python_sitelibdir/%oname
cp -fR docs/_build/pickle %buildroot%python_sitelibdir/%oname/

%check
python setup.py test

%files
%doc *.rst examples
%_bindir/*
%python_sitelibdir/*
%exclude %python_sitelibdir/examples
%exclude %python_sitelibdir/*/tests
%exclude %python_sitelibdir/*/*/tests
%exclude %python_sitelibdir/*/pickle

%files pickles
%python_sitelibdir/*/pickle

%files docs
%doc docs/_build/html examples

%files tests
%python_sitelibdir/*/tests
%python_sitelibdir/*/*/tests

%changelog
* Thu Nov 27 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.3.1-alt1.git20141127
- Version 0.3.1

* Mon Nov 24 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.2.12-alt1.git20141124
- Version 0.2.12

* Wed Nov 19 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.2.10-alt1.git20141119
- Version 0.2.10

* Tue Nov 11 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.2.8-alt1.git20141110
- Version 0.2.8

* Thu Nov 06 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.2.6-alt1.git20141104
- Version 0.2.6

* Thu Oct 30 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.2.4-alt1.git20141024
- Initial build for Sisyphus

