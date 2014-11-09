%define oname pyramid_cron

%def_with python3
%def_disable check

Name: python-module-%oname
Version: 0.1
Release: alt1.git20141102
Summary: Simple scheduled tasks for Pyramid
License: MIT
Group: Development/Python
Url: https://pypi.python.org/pypi/pyramid_cron
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/cartlogic/pyramid_cron.git
Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools-tests
BuildPreReq: python-module-pyramid-tests python-module-nose
BuildPreReq: python-module-coverage python-module-nose-cover3
BuildPreReq: python-module-sphinx-devel
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools-tests
BuildPreReq: python3-module-pyramid-tests python3-module-nose
BuildPreReq: python3-module-coverage python3-module-nose-cover3
%endif

%py_provides %oname

%description
Provides the ability to register simple tasks (callback functions) for
scheduled execution with a cron-like syntax.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR
%py_requires pyramid.testing

%description tests
Provides the ability to register simple tasks (callback functions) for
scheduled execution with a cron-like syntax.

This package contains tests for %oname.

%package -n python3-module-%oname
Summary: Simple scheduled tasks for Pyramid
Group: Development/Python3
%py3_provides %oname

%description -n python3-module-%oname
Provides the ability to register simple tasks (callback functions) for
scheduled execution with a cron-like syntax.

%package -n python3-module-%oname-tests
Summary: Tests for %oname
Group: Development/Python3
Requires: python3-module-%oname = %EVR
%py3_requires pyramid.testing

%description -n python3-module-%oname-tests
Provides the ability to register simple tasks (callback functions) for
scheduled execution with a cron-like syntax.

This package contains tests for %oname.

%package pickles
Summary: Pickles for %oname
Group: Development/Python

%description pickles
Provides the ability to register simple tasks (callback functions) for
scheduled execution with a cron-like syntax.

This package contains pickles for %oname.

%package docs
Summary: Documentation for %oname
Group: Development/Documentation
BuildArch: noarch

%description docs
Provides the ability to register simple tasks (callback functions) for
scheduled execution with a cron-like syntax.

This package contains documentation for %oname.

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

%make -C docs pickle
%make -C docs html

cp -fR docs/_build/pickle %buildroot%python_sitelibdir/%oname/

%check
python setup.py test
#if_with python3
%if 0
pushd ../python3
python3 setup.py test
popd
%endif

%files
%doc CHANGES *.rst
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
%doc CHANGES *.rst
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/tests

%files -n python3-module-%oname-tests
%python3_sitelibdir/*/tests
%endif

%changelog
* Sun Nov 09 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1-alt1.git20141102
- Initial build for Sisyphus

