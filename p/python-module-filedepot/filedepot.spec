%define oname filedepot

%def_with python3
%def_disable check

Name: python-module-%oname
Version: 0.0.3
Release: alt1.git20150209
Summary: Toolkit for storing files and attachments in web applications
License: MIT
Group: Development/Python
Url: https://pypi.python.org/pypi/filedepot/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/amol-/depot.git
Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools-tests
BuildPreReq: python-module-mock python-module-pymongo
BuildPreReq: python-module-SQLAlchemy python-module-Pillow
BuildPreReq: python-module-Ming python-module-TurboGears2
BuildPreReq: python-module-webtest python-module-nose
BuildPreReq: python-module-boto python-module-repoze.lru
BuildPreReq: python-module-sphinx-devel
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools-tests
BuildPreReq: python3-module-mock python3-module-pymongo
BuildPreReq: python3-module-SQLAlchemy python3-module-Pillow
BuildPreReq: python3-module-Ming python3-module-TurboGears2
BuildPreReq: python3-module-webtest python3-module-nose
BuildPreReq: python3-module-boto python3-module-repoze.lru
%endif

%py_provides %oname depot
%py_requires pymongo sqlalchemy PIL ming boto

%description
DEPOT is a framework for easily storing and serving files in web
applications on Python2.6+ and Python3.2+.

%package -n python3-module-%oname
Summary: Toolkit for storing files and attachments in web applications
Group: Development/Python3
%py3_provides %oname depot
%py3_requires pymongo sqlalchemy PIL ming boto

%description -n python3-module-%oname
DEPOT is a framework for easily storing and serving files in web
applications on Python2.6+ and Python3.2+.

%package pickles
Summary: Pickles for %oname
Group: Development/Python

%description pickles
DEPOT is a framework for easily storing and serving files in web
applications on Python2.6+ and Python3.2+.

This package contains pickles for %oname.

%package docs
Summary: Documentation for %oname
Group: Development/Documentation
BuildArch: noarch

%description docs
DEPOT is a framework for easily storing and serving files in web
applications on Python2.6+ and Python3.2+.

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

install -d %buildroot%python_sitelibdir/%oname
cp -fR docs/_build/pickle %buildroot%python_sitelibdir/%oname/

%check
python setup.py test
%if_with python3
pushd ../python3
python3 setup.py test
popd
%endif
exit 1

%files
%doc *.rst
%python_sitelibdir/*
%exclude %python_sitelibdir/*/pickle

%files pickles
%python_sitelibdir/*/pickle

%files docs
%doc docs/_build/html examples

%if_with python3
%files -n python3-module-%oname
%doc *.rst
%python3_sitelibdir/*
%endif

%changelog
* Fri Feb 13 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.0.3-alt1.git20150209
- Initial build for Sisyphus

