%define oname ddt

%def_with python3

Name: python-module-%oname
Version: 1.0.0
Release: alt1.git20150514
Summary: Data-Driven/Decorated Tests
License: MIT
Group: Development/Python
Url: https://pypi.python.org/pypi/ddt/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/txels/ddt.git
Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools-tests
BuildPreReq: python-module-wheel python-module-codecov
BuildPreReq: python-module-coverage python-module-flake8
BuildPreReq: python-module-nose python-module-six
BuildPreReq: python-module-sphinx-devel
BuildPreReq: python-module-sphinxcontrib-programoutput
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools-tests
BuildPreReq: python3-module-wheel python3-module-codecov
BuildPreReq: python3-module-coverage python3-module-flake8
BuildPreReq: python3-module-nose python3-module-six
%endif

%py_provides %oname

%description
DDT (Data-Driven Tests) allows you to multiply one test case by running
it with different test data, and make it appear as multiple test cases.

%if_with python3
%package -n python3-module-%oname
Summary: Data-Driven/Decorated Tests
Group: Development/Python3
%py3_provides %oname

%description -n python3-module-%oname
DDT (Data-Driven Tests) allows you to multiply one test case by running
it with different test data, and make it appear as multiple test cases.
%endif

%package pickles
Summary: Pickles for %oname
Group: Development/Python

%description pickles
DDT (Data-Driven Tests) allows you to multiply one test case by running
it with different test data, and make it appear as multiple test cases.

This package contains pickles for %oname.

%prep
%setup

%if_with python3
cp -fR . ../python3
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

export PYTHONPATH=%buildroot%python_sitelibdir
%make -C docs pickle
%make -C docs html

install -d %buildroot%python_sitelibdir/%oname
cp -fR docs/_build/pickle %buildroot%python_sitelibdir/%oname/

%check
python setup.py test -v
nosetests -vv --with-coverage --cover-html --cover-package=ddt
%if_with python3
pushd ../python3
python3 setup.py test -v
nosetests3 -vv --with-coverage --cover-html --cover-package=ddt
popd
%endif

%files
%doc *.md docs/_build/html
%python_sitelibdir/*
%exclude %python_sitelibdir/*/pickle

%files pickles
%python_sitelibdir/*/pickle

%if_with python3
%files -n python3-module-%oname
%doc *.md docs/_build/html
%python3_sitelibdir/*
%endif

%changelog
* Fri Jul 31 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.0-alt1.git20150514
- Initial build for Sisyphus

