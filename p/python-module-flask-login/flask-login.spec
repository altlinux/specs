%define oname flask-login

%def_with python3

Name: python-module-%oname
Version: 0.3.0
Release: alt1.git20141006
Summary: User session management for Flask
License: MIT
Group: Development/Python
Url: https://pypi.python.org/pypi/Flask-Login/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/maxcountryman/flask-login.git
Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools-tests
BuildPreReq: python-module-flask python-module-werkzeug
BuildPreReq: python-module-blinker python-module-coverage
BuildPreReq: python-module-mock python-module-nose python-tools-pep8
BuildPreReq: pyflakes python-module-unittest2
BuildPreReq: python-module-yanc
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools-tests
BuildPreReq: python3-module-flask python3-module-werkzeug
BuildPreReq: python3-module-blinker python3-module-coverage
BuildPreReq: python3-module-mock python3-module-nose python3-tools-pep8
BuildPreReq: python3-pyflakes python3-module-unittest2
BuildPreReq: python3-module-yanc
%endif

%description
Flask-Login provides user session management for Flask. It handles the
common tasks of logging in, logging out, and remembering your users'
sessions over extended periods of time.

Flask-Login is not bound to any particular database system or
permissions model. The only requirement is that your user objects
implement a few methods, and that you provide a callback to the
extension capable of loading users from their ID.

%package -n python3-module-%oname
Summary: User session management for Flask
Group: Development/Python3

%description -n python3-module-%oname
Flask-Login provides user session management for Flask. It handles the
common tasks of logging in, logging out, and remembering your users'
sessions over extended periods of time.

Flask-Login is not bound to any particular database system or
permissions model. The only requirement is that your user objects
implement a few methods, and that you provide a callback to the
extension capable of loading users from their ID.

%prep
%setup

%if_with python3
cp -fR . ../python3
sed -i 's|nosetests|nosetests3|' ../python3/run-tests.sh
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
%doc CHANGES README* docs/*.rst
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%oname
%doc CHANGES README* docs/*.rst
%python3_sitelibdir/*
%endif

%changelog
* Thu Oct 16 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.3.0-alt1.git20141006
- Initial build for Sisyphus

