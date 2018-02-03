%define oname flask-login

%def_with python3
%def_disable check

Name: python-module-%oname
Version: 0.3.0
Release: alt2.git20150202.1.1
Summary: User session management for Flask
License: MIT
Group: Development/Python
Url: https://pypi.python.org/pypi/Flask-Login/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/maxcountryman/flask-login.git
Source: %name-%version.tar
BuildArch: noarch

BuildRequires: python-module-setuptools
BuildRequires: python-module-blinker python-module-coverage python-module-nose python-module-pbr python-module-pytest python-module-unittest2 python-tools-pep8 
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-blinker python3-module-coverage python3-module-html5lib python3-module-nose python3-module-pbr python3-module-unittest2 python3-pyflakes python3-tools-pep8
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
* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 0.3.0-alt2.git20150202.1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.3.0-alt2.git20150202.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Fri Feb 05 2016 Sergey Alembekov <rt@altlinux.ru> 0.3.0-alt2.git20150202
- cleanup buildreq
- disable check

* Mon Mar 02 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.3.0-alt1.git20150202
- New snapshot

* Thu Oct 16 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.3.0-alt1.git20141006
- Initial build for Sisyphus

