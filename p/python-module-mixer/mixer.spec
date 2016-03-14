%define oname mixer

%def_with python3

Name: python-module-%oname
Version: 5.1.10
Release: alt1.git20150727.1
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
BuildPreReq: python-module-SQLAlchemy python-module-fake-factory
BuildPreReq: python-module-django-dbbackend-sqlite3
BuildPreReq: python-module-sphinx-devel
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools-tests
BuildPreReq: python3-module-django-tests python3-module-flask_sqlalchemy
BuildPreReq: python3-module-ipdb python3-module-mongoengine
BuildPreReq: python3-module-peewee python3-module-pony
BuildPreReq: python3-module-SQLAlchemy python3-module-fake-factory
BuildPreReq: python3-module-django-dbbackend-sqlite3
%endif

%py_provides %oname
Requires: python-module-fake-factory
%py_requires faker

%description
Mixer is application to generate instances of Django or SQLAlchemy
models. It's useful for testing and fixtures replacement. Fast and
convenient test-data generation.

%if_with python3
%package -n python3-module-%oname
Summary: Mixer -- Is a fixtures replacement
Group: Development/Python3
%py3_provides %oname
%py3_requires faker

%description -n python3-module-%oname
Mixer is application to generate instances of Django or SQLAlchemy
models. It's useful for testing and fixtures replacement. Fast and
convenient test-data generation.
%endif

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
export LC_ALL=en_US.UTF-8
%python_build_debug

%if_with python3
pushd ../python3
%python3_build_debug
popd
%endif

%install
export LC_ALL=en_US.UTF-8
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
export LC_ALL=en_US.UTF-8
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
* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 5.1.10-alt1.git20150727.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Tue Jul 28 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 5.1.10-alt1.git20150727
- Version 5.1.10

* Tue Mar 03 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 5.0.7-alt2.git20150123
- Fixed for new fake-factory & Django 1.8+

* Tue Mar 03 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 5.0.7-alt1.git20150123
- Version 5.0.7

* Sun Jan 18 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.10.2-alt2.git20141224
- Added module for Python 3

* Sat Jan 03 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.10.2-alt1.git20141224
- Initial build for Sisyphus

