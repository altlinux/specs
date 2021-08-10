%define oname flask-login

%def_disable check

Name: python3-module-%oname
Version: 0.3.0
Release: alt4

Summary: User session management for Flask
License: MIT
Group: Development/Python3
Url: https://pypi.python.org/pypi/Flask-Login/
# https://github.com/maxcountryman/flask-login.git
BuildArch: noarch

Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-blinker python3-module-coverage
BuildRequires: python3-module-html5lib python3-module-nose
BuildRequires: python3-module-pbr python3-module-unittest2
BuildRequires: python3-pyflakes


%description
Flask-Login provides user session management for Flask. It handles the
common tasks of logging in, logging out, and remembering your users'
sessions over extended periods of time.

Flask-Login is not bound to any particular database system or
permissions model. The only requirement is that your user objects
implement a few methods, and that you provide a callback to the
extension capable of loading users from their ID.

%prep
%setup

sed -i 's|nosetests|nosetests3|' ./run-tests.sh

%build
%python3_build_debug

%install
%python3_install

%check
python3 setup.py test

%files
%doc CHANGES README* docs/*.rst
%python3_sitelibdir/*


%changelog
* Tue Aug 10 2021 Grigory Ustinov <grenka@altlinux.org> 0.3.0-alt4
- Fixed BuildRequires.

* Wed Nov 13 2019 Andrey Bychkov <mrdrew@altlinux.org> 0.3.0-alt3
- python2 disabled

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

