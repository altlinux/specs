%define oname pyramid_basemodel

%def_with python3

Name: python-module-%oname
Version: 0.2.5
Release: alt1.git20141121
Summary: Global base classes for Pyramid SQLAlchemy applications
License: Public domain
Group: Development/Python
Url: https://pypi.python.org/pypi/pyramid_basemodel/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/thruflo/pyramid_basemodel.git
Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools-tests
BuildPreReq: python-module-pyramid_tm python-module-pyramid
BuildPreReq: python-module-requests python-module-slugify
BuildPreReq: python-module-zope.interface python-module-zope.sqlalchemy
BuildPreReq: python-module-SQLAlchemy python-module-inflect
BuildPreReq: python-module-PasteDeploy python-module-zope.deprecation
BuildPreReq: python-module-repoze.lru
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools-tests
BuildPreReq: python3-module-pyramid_tm python3-module-pyramid
BuildPreReq: python3-module-requests python3-module-slugify
BuildPreReq: python3-module-zope.interface python3-module-zope.sqlalchemy
BuildPreReq: python3-module-SQLAlchemy python3-module-inflect
BuildPreReq: python3-module-PasteDeploy python3-module-zope.deprecation
BuildPreReq: python3-module-repoze.lru
%endif

%py_provides %oname
%py_requires zope.interface zope.sqlalchemy

%description
pyramid_basemodel is a thin, low level package that provides an
SQLAlchemy declarative Base and a thread local scoped Session that can
be used by different packages whilst only needing to be bound to a db
engine once.

%package -n python3-module-%oname
Summary: Global base classes for Pyramid SQLAlchemy applications
Group: Development/Python3
%py3_provides %oname
%py3_requires zope.interface zope.sqlalchemy

%description -n python3-module-%oname
pyramid_basemodel is a thin, low level package that provides an
SQLAlchemy declarative Base and a thread local scoped Session that can
be used by different packages whilst only needing to be bound to a db
engine once.

%prep
%setup

%if_with python3
cp -fR . ../python3
%endif

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

%check
python setup.py test
%if_with python3
pushd ../python3
python3 setup.py test
popd
%endif

%files
%doc *.md UNLICENSE
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%oname
%doc *.md UNLICENSE
%python3_sitelibdir/*
%endif

%changelog
* Fri Nov 21 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.2.5-alt1.git20141121
- Version 0.2.5

* Fri Nov 21 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.2.4-alt1
- Version 0.2.4

* Fri Oct 31 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.2.3-alt1.git20140626
- Initial build for Sisyphus

