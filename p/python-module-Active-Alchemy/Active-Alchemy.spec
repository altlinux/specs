%define oname Active-Alchemy

%def_with python3

Name: python-module-%oname
Version: 0.4.3
Release: alt1.git20150713
Summary: A framework agnostic wrapper for SQLAlchemy
License: MIT
Group: Development/Python
Url: https://pypi.python.org/pypi/Active-Alchemy/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/mardix/active-alchemy.git
Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools-tests
BuildPreReq: python-module-SQLAlchemy python-module-pymysql
BuildPreReq: python-module-pg8000 python-module-Paginator
BuildPreReq: python-module-inflection python-module-six
BuildPreReq: python-modules-sqlite3
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools-tests
BuildPreReq: python3-module-SQLAlchemy python3-module-pymysql
BuildPreReq: python3-module-pg8000 python3-module-Paginator
BuildPreReq: python3-module-inflection python3-module-six
BuildPreReq: python3-modules-sqlite3
%endif

%py_provides active_alchemy
%py_requires sqlalchemy pymysql pg8000 paginator inflection

%description
A framework agnostic wrapper for SQLAlchemy that makes it really easy to
use by implementing a simple active record like api, while it still uses
the db.session underneath :copyright: (c) 2014/2015 by `Mardix`.
:license: MIT.

%if_with python3
%package -n python3-module-%oname
Summary: A framework agnostic wrapper for SQLAlchemy
Group: Development/Python3
%py3_provides active_alchemy
%py3_requires sqlalchemy pymysql pg8000 paginator inflection

%description -n python3-module-%oname
A framework agnostic wrapper for SQLAlchemy that makes it really easy to
use by implementing a simple active record like api, while it still uses
the db.session underneath :copyright: (c) 2014/2015 by `Mardix`.
:license: MIT.
%endif

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
python setup.py test -v
python tests.py -v
%if_with python3
pushd ../python3
python3 setup.py test -v
#python3 tests.py -v
popd
%endif

%files
%doc AUTHORS CHANGELOG *.md
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%oname
%doc AUTHORS CHANGELOG *.md
%python3_sitelibdir/*
%endif

%changelog
* Wed Jul 29 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.4.3-alt1.git20150713
- Initial build for Sisyphus

