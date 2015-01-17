%define oname pyramid_skosprovider

%def_with python3

Name: python-module-%oname
Version: 0.5.0
Release: alt1.git20141219
Summary: Integration of skosprovider in pyramid
License: MIT
Group: Development/Python
Url: https://pypi.python.org/pypi/pyramid_skosprovider/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/koenedaele/pyramid_skosprovider.git
Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools-tests
BuildPreReq: python-module-pyramid-tests python-module-skosprovider
BuildPreReq: python-module-pytest-cov python-module-webtest
BuildPreReq: python-module-sphinx-devel
BuildPreReq: python-module-sphinxcontrib-httpdomain
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools-tests
BuildPreReq: python3-module-pyramid-tests python3-module-skosprovider
BuildPreReq: python3-module-pytest-cov python3-module-webtest
%endif

%py_provides %oname
%py_requires pyramid skosprovider

%description
This library integrates skosprovider in a pyramid application.

%package -n python3-module-%oname
Summary: Integration of skosprovider in pyramid
Group: Development/Python3
%py3_provides %oname
%py3_requires pyramid skosprovider

%description -n python3-module-%oname
This library integrates skosprovider in a pyramid application.

%package pickles
Summary: Pickles for %oname
Group: Development/Python

%description pickles
This library integrates skosprovider in a pyramid application.

This package contains pickles for %oname.

%package docs
Summary: Documentation for %oname
Group: Development/Documentation
BuildArch: noarch

%description docs
This library integrates skosprovider in a pyramid application.

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

export PYTHONPATH=$PWD
%make -C docs pickle
%make -C docs html

cp -fR docs/_build/pickle %buildroot%python_sitelibdir/%oname/

%check
export LC_ALL=en_US.UTF-8
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
%exclude %python_sitelibdir/tests
%exclude %python_sitelibdir/*/pickle

%files pickles
%python_sitelibdir/*/pickle

%files docs
%doc docs/_build/html/*

%if_with python3
%files -n python3-module-%oname
%doc *.rst
%python3_sitelibdir/*
%exclude %python3_sitelibdir/tests
%endif

%changelog
* Sat Jan 17 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.5.0-alt1.git20141219
- Initial build for Sisyphus

