%define oname CherryPy-SQLAlchemy

%def_with python3

Name: python-module-%oname
Version: 0.5.2
Release: alt1.git20150111
Summary: Use SQLAlchemy with CherryPy
License: BSD
Group: Development/Python
Url: https://pypi.python.org/pypi/CherryPy-SQLAlchemy/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/ionrock/cherrypy-sqlalchemy.git
Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools-tests
BuildPreReq: python-module-cherrypy python-module-SQLAlchemy
BuildPreReq: python-module-mock python-module-bumpversion
BuildPreReq: python-modules-sqlite3
BuildPreReq: python-module-sphinx-devel
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools-tests
BuildPreReq: python3-module-cherrypy python3-module-SQLAlchemy
BuildPreReq: python3-module-mock python3-module-bumpversion
BuildPreReq: python3-modules-sqlite3
%endif

%py_provides cp_sqlalchemy
%py_requires cherrypy sqlalchemy

%description
CherryPy-SQLAlchemy makes it easy to use SQLAlchemy within CherryPy
apps.

%package -n python3-module-%oname
Summary: Use SQLAlchemy with CherryPy
Group: Development/Python3
%py3_provides cp_sqlalchemy
%py3_requires cherrypy sqlalchemy

%description -n python3-module-%oname
CherryPy-SQLAlchemy makes it easy to use SQLAlchemy within CherryPy
apps.

%package pickles
Summary: Pickles for %oname
Group: Development/Python

%description pickles
CherryPy-SQLAlchemy makes it easy to use SQLAlchemy within CherryPy
apps.

This package contains pickles for %oname.

%package docs
Summary: Documentation for %oname
Group: Development/Documentation
BuildArch: noarch

%description docs
CherryPy-SQLAlchemy makes it easy to use SQLAlchemy within CherryPy
apps.

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

%make docs

install -d %buildroot%python_sitelibdir/%oname
cp -fR docs/_build/pickle %buildroot%python_sitelibdir/%oname/

%check
python setup.py test
%if_with python3
pushd ../python3
python3 setup.py test
popd
%endif

%files
%doc *.rst example.py
%python_sitelibdir/*
%exclude %python_sitelibdir/*/pickle

%files pickles
%python_sitelibdir/*/pickle

%files docs
%doc docs/_build/html/*

%if_with python3
%files -n python3-module-%oname
%doc *.rst example.py
%python3_sitelibdir/*
%endif

%changelog
* Sun Jan 18 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.5.2-alt1.git20150111
- Initial build for Sisyphus

