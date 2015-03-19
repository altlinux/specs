%define oname web_utils

%def_with python3

Name: python-module-%oname
Version: 0.0.4
Release: alt1.git20150319
Summary: Web development utils classes and functions
License: GPLv3
Group: Development/Python
Url: https://pypi.python.org/pypi/web_utils/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/winkidney/web_utils.git
Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools-tests
BuildPreReq: python-module-wtforms python-module-jsonschema
BuildPreReq: python-module-bcrypt python-module-SQLAlchemy
BuildPreReq: python-module-psycopg2 python-module-pycrypto
BuildPreReq: python-module-nose python-module-coverage
BuildPreReq: python-module-pyramid
BuildPreReq: python-modules-json python-modules-logging
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools-tests
BuildPreReq: python3-module-wtforms python3-module-jsonschema
BuildPreReq: python3-module-bcrypt python3-module-SQLAlchemy
BuildPreReq: python3-module-psycopg2 python3-module-pycrypto
BuildPreReq: python3-module-nose python3-module-coverage
BuildPreReq: python3-module-pyramid
BuildPreReq: python-tools-2to3
%endif

%py_provides %oname
%py_requires wtforms jsonschema bcrypt sqlalchemy psycopg2 Crypto json
%py_requires logging

%description
web_utils collection that used in web development process.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR

%description tests
web_utils collection that used in web development process.

This package contains tests for %oname.

%if_with python3
%package -n python3-module-%oname
Summary: Web development utils classes and functions
Group: Development/Python3
%py3_provides %oname
%py3_requires wtforms jsonschema bcrypt sqlalchemy psycopg2 Crypto json
%py3_requires logging

%description -n python3-module-%oname
web_utils collection that used in web development process.

%package -n python3-module-%oname-tests
Summary: Tests for %oname
Group: Development/Python3
Requires: python3-module-%oname = %EVR

%description -n python3-module-%oname-tests
web_utils collection that used in web development process.

This package contains tests for %oname.
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
%python_install

%if_with python3
pushd ../python3
%python3_install
popd
%endif

%check
python setup.py test
nosetests -v web_utils/tests.py \
	--with-coverage --cover-package=web_utils
#if_with python3
%if 0
pushd ../python3
python3 setup.py test
nosetests3 -v web_utils/tests.py \
	--with-coverage --cover-package=web_utils
popd
%endif

%files
%doc *.txt *.md
%python_sitelibdir/*
%exclude %python_sitelibdir/*/tests.*
%exclude %python_sitelibdir/*/*/tests.*

%files tests
%python_sitelibdir/*/tests.*
%python_sitelibdir/*/*/tests.*

%if_with python3
%files -n python3-module-%oname
%doc *.txt *.md
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/tests.*
%exclude %python3_sitelibdir/*/*/tests.*
%exclude %python3_sitelibdir/*/*/*/tests.*

%files -n python3-module-%oname-tests
%python3_sitelibdir/*/tests.*
%python3_sitelibdir/*/*/tests.*
%python3_sitelibdir/*/*/*/tests.*
%endif

%changelog
* Thu Mar 19 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.0.4-alt1.git20150319
- Initial build for Sisyphus

