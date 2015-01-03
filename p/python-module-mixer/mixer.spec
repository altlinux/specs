%define oname mixer

%def_without python3

Name: python-module-%oname
Version: 4.10.2
Release: alt1.git20141224
Summary: Mixer -- Is a fixtures replacement
License: BSD
Group: Development/Python
Url: https://pypi.python.org/pypi/mixer/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/klen/mixer.git
Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools-tests
BuildPreReq: python-module-django-tests python-module-flask_sqlalchemy
BuildPreReq: python-module-ipdb python-module-mongoengine
BuildPreReq: python-module-peewee python-module-pony
BuildPreReq: python-module-SQLAlchemy
BuildPreReq: python-module-django-dbbackend-sqlite3
BuildPreReq: python-module-sphinx-devel
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools-tests
BuildPreReq: python3-module-django-tests python3-module-flask_sqlalchemy
BuildPreReq: python3-module-ipdb python3-module-mongoengine
BuildPreReq: python3-module-peewee python3-module-pony
BuildPreReq: python3-module-SQLAlchemy
BuildPreReq: python3-module-django-dbbackend-sqlite3
%endif

%py_provides %oname

%description
Mixer is application to generate instances of Django or SQLAlchemy
models. It's useful for testing and fixtures replacement. Fast and
convenient test-data generation.

%package -n python3-module-%oname
Summary: Mixer -- Is a fixtures replacement
Group: Development/Python3
%py3_provides %oname

%description -n python3-module-%oname
Mixer is application to generate instances of Django or SQLAlchemy
models. It's useful for testing and fixtures replacement. Fast and
convenient test-data generation.

%package pickles
Summary: Pickles for %oname
Group: Development/Python

%description pickles
Mixer is application to generate instances of Django or SQLAlchemy
models. It's useful for testing and fixtures replacement. Fast and
convenient test-data generation.

This package contains pickles for %oname.

%package docs
Summary: Documentation for %oname
Group: Development/Documentation
BuildArch: noarch

%description docs
Mixer is application to generate instances of Django or SQLAlchemy
models. It's useful for testing and fixtures replacement. Fast and
convenient test-data generation.

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

export PYTHONPATH=%buildroot%python_sitelibdir
pushd docs
sphinx-build -b pickle -d _build/doctrees . _build/pickle
sphinx-build -b html -d _build/doctrees . _build/html
popd

cp -fR docs/_build/pickle %buildroot%python_sitelibdir/%oname/

%check
python setup.py test
%if_with python3
pushd ../python3
python3 setup.py test
popd
%endif

%files
%doc Changelog DESCRIPTION *.rst
%python_sitelibdir/*
%exclude %python_sitelibdir/*/pickle

%files pickles
%python_sitelibdir/*/pickle

%files docs
%doc docs/_build/html/*

%if_with python3
%files -n python3-module-%oname
%doc Changelog DESCRIPTION *.rst
%python3_sitelibdir/*
%endif

%changelog
* Sat Jan 03 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.10.2-alt1.git20141224
- Initial build for Sisyphus

