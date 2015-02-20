%define oname projex_orb

%def_with python3

Name: python-module-%oname
Version: 4.4.0
Release: alt1.git20150219
Summary: ORB stands for Object Relation Builder and is simple to use database class generator
License: LGPLv3
Group: Development/Python
Url: https://pypi.python.org/pypi/projex_orb/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/ProjexSoftware/orb.git
Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools-tests
BuildPreReq: python-module-projex python-module-pytz
BuildPreReq: python-module-tzlocal python-modules-json
BuildPreReq: python-module-mako python-module-redis-py
BuildPreReq: python-module-psycopg2 python-module-requests
BuildPreReq: python-module-projex_xqt
BuildPreReq: python-module-yaml python-module-pyparsing
BuildPreReq: python-modules-xml python-modules-logging
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools-tests
BuildPreReq: python3-module-projex python3-module-pytz
BuildPreReq: python3-module-tzlocal
BuildPreReq: python3-module-mako python3-module-redis-py
BuildPreReq: python3-module-psycopg2 python3-module-requests
BuildPreReq: python3-module-projex_xqt
BuildPreReq: python3-module-yaml python3-module-pyparsing
BuildPreReq: python-tools-2to3
%endif

%py_provides orb
%py_requires json projex pytz tzlocal mako redis psycopg2 requests xqt
%py_requires urllib2 yaml pyparsing xml logging

%description
Object-oriented database object-relation mapping architecture for
Python.

%package -n python3-module-%oname
Summary: ORB stands for Object Relation Builder and is simple to use database class generator
Group: Development/Python3
%py3_provides orb
%py3_requires json projex pytz tzlocal mako redis psycopg2 requests xqt
%py3_requires yaml pyparsing xml logging

%description -n python3-module-%oname
Object-oriented database object-relation mapping architecture for
Python.

%prep
%setup

mv src/* ./

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
%python_install

%if_with python3
pushd ../python3
%python3_install
popd
%endif

%check
python setup.py test
py.test -vv $(find src -name '*.py')
%if_with python3
pushd ../python3
python3 setup.py test
py.test-%_python3_version -vv $(find src -name '*.py')
popd
%endif

%files
%doc *.md docs/*
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%oname
%doc *.md docs/*
%python3_sitelibdir/*
%endif

%changelog
* Fri Feb 20 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.4.0-alt1.git20150219
- Version 4.4.0
- Added module for Python 3

* Tue Nov 11 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.0.0-alt1.git20140719
- Initial build for Sisyphus

