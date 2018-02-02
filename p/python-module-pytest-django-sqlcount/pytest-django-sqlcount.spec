%define oname pytest-django-sqlcount

%def_with python3

Name: python-module-%oname
Version: 0.1.0
Release: alt1.git20141028.1.1
Summary: py.test plugin for reporting the number of SQLs executed per django testcase
License: MIT
Group: Development/Python
Url: https://pypi.python.org/pypi/pytest-django-sqlcount/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/stj/pytest-django-sqlcount.git
Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools
BuildPreReq: python-module-pytest-django
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
BuildPreReq: python3-module-pytest-django
%endif

%py_provides pytest_django_sqlcount
%py_requires django.test.utils

%description
This plugin adds the number of SQLs executed on the default database
connection per test to the terminal report.

All features offered by the default py.test terminal plugin should be
available.

%package -n python3-module-%oname
Summary: py.test plugin for reporting the number of SQLs executed per django testcase
Group: Development/Python3
%py3_provides pytest_django_sqlcount
%py3_requires django.test.utils

%description -n python3-module-%oname
This plugin adds the number of SQLs executed on the default database
connection per test to the terminal report.

All features offered by the default py.test terminal plugin should be
available.

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
%doc *.rst
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%oname
%doc *.rst
%python3_sitelibdir/*
%endif

%changelog
* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 0.1.0-alt1.git20141028.1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.1.0-alt1.git20141028.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Fri Oct 31 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1.0-alt1.git20141028
- Initial build for Sisyphus

