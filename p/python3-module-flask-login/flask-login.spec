%define _unpackaged_files_terminate_build 1
%define oname flask-login

%def_enable check

Name: python3-module-%oname
Version: 0.6.3
Release: alt1

Summary: User session management for Flask
License: MIT
Group: Development/Python3
Url: https://pypi.org/project/Flask-Login/
Vcs: https://github.com/maxcountryman/flask-login

BuildArch: noarch

Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-wheel
%if_enabled check
BuildRequires: python3-module-flask
BuildRequires: python3-module-blinker
BuildRequires: python3-module-semantic_version
BuildRequires: python3-module-asgiref
BuildRequires: python3-module-pytest
%endif

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

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest -vra

%files
%doc CHANGES.md LICENSE README.md
%python3_sitelibdir/flask_login/
%python3_sitelibdir/Flask_Login-%version.dist-info/

%changelog
* Mon Dec 18 2023 Anton Zhukharev <ancieg@altlinux.org> 0.6.3-alt1
- Updated to 0.6.3.

* Thu Jun 08 2023 Danil Shein <dshein@altlinux.org> 0.6.2-alt2
- NMU: fix FTBFS due to tests failed
  + migrate to pyproject macroses

* Thu Sep 22 2022 Danil Shein <dshein@altlinux.org> 0.6.2-alt1
- NMU: new version 0.6.2
  + compatible with Werkzeug 2.2 and Flask 2.2
  + enable tests

* Mon May 30 2022 Grigory Ustinov <grenka@altlinux.org> 0.3.0-alt5
- Fixed BuildRequires.

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

