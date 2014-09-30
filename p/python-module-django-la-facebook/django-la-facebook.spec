%define oname django-la-facebook

%def_with python3

Name: python-module-%oname
Version: 0.1.1
Release: alt1.git20110418
Summary: Definitive facebook auth for Django
License: BSD
Group: Development/Python
Url: https://pypi.python.org/pypi/django-la-facebook/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/cartwheelweb/django-la-facebook.git
Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools
BuildPreReq: python-module-sphinx-devel
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
BuildPreReq: python-tools-2to3
%endif

%description
Dedicated facebook authentication for Django that does it via the
backend and not javascript. Has lots of tests and a trivial-to-setup
test project with working code.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR

%description tests
Dedicated facebook authentication for Django that does it via the
backend and not javascript. Has lots of tests and a trivial-to-setup
test project with working code.

This package contains tests for %oname.

%package -n python3-module-%oname
Summary: Definitive facebook auth for Django
Group: Development/Python3

%description -n python3-module-%oname
Dedicated facebook authentication for Django that does it via the
backend and not javascript. Has lots of tests and a trivial-to-setup
test project with working code.

%package -n python3-module-%oname-tests
Summary: Tests for %oname
Group: Development/Python3
Requires: python3-module-%oname = %EVR

%description -n python3-module-%oname-tests
Dedicated facebook authentication for Django that does it via the
backend and not javascript. Has lots of tests and a trivial-to-setup
test project with working code.

This package contains tests for %oname.

%package pickles
Summary: Pickles for %oname
Group: Development/Python

%description pickles
Dedicated facebook authentication for Django that does it via the
backend and not javascript. Has lots of tests and a trivial-to-setup
test project with working code.

This package contains pickles for %oname.

%package docs
Summary: Documentation for %oname
Group: Development/Documentation
BuildArch: noarch

%description docs
Dedicated facebook authentication for Django that does it via the
backend and not javascript. Has lots of tests and a trivial-to-setup
test project with working code.

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

export PYTHONPATH=%buildroot%python_sitelibdir
%make -C docs pickle
%make -C docs html

install -d %buildroot%python_sitelibdir/%oname
cp -fR docs/_build/pickle %buildroot%python_sitelibdir/%oname/

%files
%doc CONTRIBUTORS *.rst
%python_sitelibdir/*
%exclude %python_sitelibdir/*/pickle
%exclude %python_sitelibdir/test_project
%exclude %python_sitelibdir/*/tests

%files tests
%python_sitelibdir/*/tests

%files pickles
%python_sitelibdir/*/pickle

%files docs
%doc docs/_build/html/*

%if_with python3
%files -n python3-module-%oname
%doc CONTRIBUTORS *.rst
%python3_sitelibdir/*
%exclude %python3_sitelibdir/test_project
%exclude %python3_sitelibdir/*/tests

%files -n python3-module-%oname-tests
%python3_sitelibdir/*/tests
%endif

%changelog
* Tue Sep 30 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1.1-alt1.git20110418
- Initial build for Sisyphus

