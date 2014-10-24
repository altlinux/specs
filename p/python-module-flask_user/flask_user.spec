%define oname flask_user

%def_with python3

Name: python-module-%oname
Version: 0.5.5
Release: alt1.git20141023
Summary: Customizable User Account Management for Flask
License: BSD
Group: Development/Python
Url: https://pypi.python.org/pypi/Flask-User/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/lingthio/Flask-User.git
Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools-tests
BuildPreReq: python-module-passlib
BuildPreReq: python-module-bcrypt
BuildPreReq: python-module-Crypto
BuildPreReq: python-module-flask
BuildPreReq: python-module-flask-login
BuildPreReq: python-module-flask_mail
BuildPreReq: python-module-flask_sqlalchemy
BuildPreReq: python-module-flask-wtf
BuildPreReq: python-module-speaklater
BuildPreReq: python-module-flask-babel
BuildPreReq: python-module-pysqlite2
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools-tests
BuildPreReq: python3-module-passlib
BuildPreReq: python3-module-Crypto
BuildPreReq: python3-module-flask
BuildPreReq: python3-module-flask-login
BuildPreReq: python3-module-flask_mail
BuildPreReq: python3-module-flask_sqlalchemy
BuildPreReq: python3-module-flask-wtf
BuildPreReq: python3-module-speaklater
BuildPreReq: python3-module-flask-babel
%endif

%py_provides %oname

%description
Customizable User Account Management for Flask: Register, Confirm email,
Login, Change username, Change password, Forgot password and more.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR

%description tests
Customizable User Account Management for Flask: Register, Confirm email,
Login, Change username, Change password, Forgot password and more.

This package contains tests for %oname.

%package -n python3-module-%oname
Summary: Customizable User Account Management for Flask
Group: Development/Python3
%py3_provides %oname

%description -n python3-module-%oname
Customizable User Account Management for Flask: Register, Confirm email,
Login, Change username, Change password, Forgot password and more.

%package -n python3-module-%oname-tests
Summary: Tests for %oname
Group: Development/Python3
Requires: python3-module-%oname = %EVR

%description -n python3-module-%oname-tests
Customizable User Account Management for Flask: Register, Confirm email,
Login, Change username, Change password, Forgot password and more.

This package contains tests for %oname.

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
#if_with python3
%if 0
pushd ../python3
python3 setup.py test
popd
%endif

%files
%doc *.txt *.rst
%python_sitelibdir/*
%exclude %python_sitelibdir/*/tests

%files tests
%python_sitelibdir/*/tests

%if_with python3
%files -n python3-module-%oname
%doc *.txt *.rst
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/tests

%files -n python3-module-%oname-tests
%python3_sitelibdir/*/tests
%endif

%changelog
* Fri Oct 24 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.5.5-alt1.git20141023
- Initial build for Sisyphus

