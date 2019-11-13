%define _unpackaged_files_terminate_build 1

%define oname Flask-WebTest

Name: python3-module-%oname
Version: 0.0.9
Release: alt2

Summary: Utilities for testing Flask applications with WebTest
License: BSD
Group: Development/Python3
Url: https://pypi.python.org/pypi/Flask-WebTest/
# https://github.com/aromanovich/flask-webtest.git
BuildArch: noarch

Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-flask python-tools-2to3
BuildRequires: python3-module-flask_sqlalchemy python3-module-webtest
BuildRequires: python3-module-blinker python3-modules-sqlite3

%py3_provides flask_webtest


%description
Provides a set of utilities to ease testing Flask applications with
WebTest.

%prep
%setup

find -type f -name '*.py' -exec 2to3 -w -n '{}' +

%build
%python3_build_debug

%install
%python3_install

%check
%__python3 setup.py test

%files
%doc *.rst docs/*.rst
%python3_sitelibdir/*


%changelog
* Wed Nov 13 2019 Andrey Bychkov <mrdrew@altlinux.org> 0.0.9-alt2
- python2 -> python3

* Thu Sep 13 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 0.0.9-alt1
- Updated to upstream version 0.0.9.

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 0.0.7-alt1.git20141009.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Mon Jan 05 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.0.7-alt1.git20141009
- Initial build for Sisyphus

