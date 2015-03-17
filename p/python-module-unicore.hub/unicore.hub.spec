%define mname unicore
%define oname %mname.hub

%def_with python3
%def_disable check

Name: python-module-%oname
Version: 0.1.0
Release: alt1.git20150317
Summary: User authentication and data storage for universal core
License: BSD
Group: Development/Python
Url: https://github.com/universalcore/unicore.hub
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/universalcore/unicore.hub.git
Source: %name-%version.tar

BuildPreReq: python-devel python-module-setuptools-tests
BuildPreReq: python-module-pyramid_beaker python-module-SQLAlchemy
BuildPreReq: python-module-SQLAlchemy-Utils python-module-webtest
BuildPreReq: python-module-alembic python-module-click-tests
BuildPreReq: python-module-colander python-module-cornice
BuildPreReq: python-module-deform python-module-mock
BuildPreReq: python-module-pyramid_beaker python-module-pyramid_jinja2
BuildPreReq: python-module-zope.interface python-module-pytest-cov
BuildPreReq: python-module-pyramid-tests python-module-passlib
BuildPreReq: python-module-psycopg2
BuildPreReq: python-modules-json python-modules-logging
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools-tests
BuildPreReq: python3-module-pyramid_beaker python3-module-SQLAlchemy
BuildPreReq: python3-module-SQLAlchemy-Utils python3-module-webtest
BuildPreReq: python3-module-alembic python3-module-click-tests
BuildPreReq: python3-module-colander python3-module-cornice
BuildPreReq: python3-module-deform python3-module-mock
BuildPreReq: python3-module-pyramid_beaker python3-module-pyramid_jinja2
BuildPreReq: python3-module-zope.interface python3-module-pytest-cov
BuildPreReq: python3-module-pyramid-tests python3-module-passlib
BuildPreReq: python3-module-psycopg2
BuildPreReq: python-tools-2to3
%endif

%py_provides %oname
%py_requires %mname pyramid_beaker sqlalchemy sqlalchemy_utils alembic
%py_requires click colander cornice deform pyramid_beaker pyramid_jinja2
%py_requires zope.interface json logging passlib psycopg2

%description
User authentication and data storage for universal core.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR

%description tests
User authentication and data storage for universal core.

This package contains tests for oname.

%if_with python3
%package -n python3-module-%oname
Summary: User authentication and data storage for universal core
Group: Development/Python3
%py3_provides %oname
%py3_requires %mname pyramid_beaker sqlalchemy sqlalchemy_utils alembic
%py3_requires click colander cornice deform pyramid_beaker pyramid_jinja2
%py3_requires zope.interface json logging passlib psycopg2

%description -n python3-module-%oname
User authentication and data storage for universal core.

%package -n python3-module-%oname-tests
Summary: Tests for %oname
Group: Development/Python3
Requires: python3-module-%oname = %EVR

%description -n python3-module-%oname-tests
User authentication and data storage for universal core.

This package contains tests for oname.
%endif

%prep
%setup

%if_with python3
cp -fR . ../python3
find ../python3 -type f -name '*.py' -exec 2to3 -w -n '{}' +
%endif

%build
%python_build_debug

%if_with python3
pushd ../python3
%python3_build_debug
popd
%endif

%install
%if_with python3
pushd ../python3
%python3_install
popd
pushd %buildroot%_bindir
for i in $(ls); do
	mv $i $i.py3
done
popd
%endif

%python_install

%ifarch x86_64
mv %buildroot%_libexecdir %buildroot%_libdir
%endif

%check
python setup.py test
py.test -vv --cov ./unicore/hub unicore/hub
%if_with python3
pushd ../python3
python3 setup.py test
py.test-%_python3_version -vv --cov ./unicore/hub unicore/hub
popd
%endif

%files
%doc *.rst
%_bindir/*
%if_with python3
%exclude %_bindir/*.py3
%endif
%python_sitelibdir/%mname/*
%python_sitelibdir/*.egg-info
%exclude %python_sitelibdir/%mname/*/*/tests
%exclude %python_sitelibdir/%mname/*/*/*/tests

%files tests
%python_sitelibdir/%mname/*/*/tests
%python_sitelibdir/%mname/*/*/*/tests

%if_with python3
%files -n python3-module-%oname
%doc *.rst
%_bindir/*.py3
%python3_sitelibdir/%mname/*
%python3_sitelibdir/*.egg-info
%exclude %python3_sitelibdir/%mname/*/*/tests
%exclude %python3_sitelibdir/%mname/*/*/*/tests

%files -n python3-module-%oname-tests
%python3_sitelibdir/%mname/*/*/tests
%python3_sitelibdir/%mname/*/*/*/tests
%endif

%changelog
* Tue Mar 17 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1.0-alt1.git20150317
- Initial build for Sisyphus

