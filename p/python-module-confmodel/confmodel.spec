%define oname confmodel

%def_with python3

Name: python-module-%oname
Version: 0.2.0.1
Release: alt3.git20140605.1
Summary: Declarative configuration access and validation system
License: BSD
Group: Development/Python
Url: https://pypi.python.org/pypi/confmodel/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/praekelt/confmodel.git
Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools-tests
BuildPreReq: python-module-zope.interface python-module-pytest-cov
BuildPreReq: python-module-flake8 python-module-six
BuildPreReq: python-module-sphinx-devel python-module-sphinx_rtd_theme
BuildPreReq: python-module-repoze.sphinx.autointerface
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools-tests
BuildPreReq: python3-module-zope.interface python3-module-pytest-cov
BuildPreReq: python3-module-flake8 python3-module-six
%endif

%py_provides %oname
%py_requires zope.interface

%description
Declarative configuration access and validation system.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR

%description tests
Declarative configuration access and validation system.

This package contains tests for %oname.

%if_with python3
%package -n python3-module-%oname
Summary: Declarative configuration access and validation system
Group: Development/Python3
%py3_provides %oname
%py3_requires zope.interface

%description -n python3-module-%oname
Declarative configuration access and validation system.

%package -n python3-module-%oname-tests
Summary: Tests for %oname
Group: Development/Python3
Requires: python3-module-%oname = %EVR

%description -n python3-module-%oname-tests
Declarative configuration access and validation system.

This package contains tests for %oname.
%endif

%package pickles
Summary: Pickles for %oname
Group: Development/Python

%description pickles
Declarative configuration access and validation system.

This package contains pickles for %oname.

%package docs
Summary: Documentation for %oname
Group: Development/Documentation
BuildArch: noarch

%description docs
Declarative configuration access and validation system.

This package contains documentation for %oname.

%prep
%setup

%if_with python3
cp -fR . ../python3
find ../python3 -type f -name '*.py' -exec 2to3 -w -n '{}' +
%endif

%prepare_sphinx .
ln -s ../objects.inv docs/

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

export PYTHONPATH=$PWD
%make -C docs pickle
%make -C docs html

cp -fR docs/_build/pickle %buildroot%python_sitelibdir/%oname/

%check
python setup.py test
rm -fR build
py.test -vv
%if_with python3
pushd ../python3
python3 setup.py test
rm -fR build
py.test-%_python3_version -vv
popd
%endif

%files
%doc *.rst
%python_sitelibdir/*
%exclude %python_sitelibdir/*/pickle
%exclude %python_sitelibdir/*/tests

%files tests
%python_sitelibdir/*/tests

%files pickles
%python_sitelibdir/*/pickle

%files docs
%doc docs/_build/html/*

%if_with python3
%files -n python3-module-%oname
%doc *.rst
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/tests

%files -n python3-module-%oname-tests
%python3_sitelibdir/*/tests
%endif

%changelog
* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.2.0.1-alt3.git20140605.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Tue Mar 10 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.2.0.1-alt3.git20140605
- Added module for Python 3

* Mon Mar 02 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.2.0.1-alt2.git20140605
- Fixed build

* Thu Oct 30 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.2.0.1-alt1.git20140605
- Initial build for Sisyphus

