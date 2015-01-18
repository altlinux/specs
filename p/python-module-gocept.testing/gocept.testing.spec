%define mname gocept
%define oname %mname.testing
Name: python-module-%oname
Version: 1.10.1
Release: alt1
Summary: A collection of test helpers, additional assertions, and the like
License: ZPL
Group: Development/Python
Url: https://pypi.python.org/pypi/gocept.testing/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-module-setuptools-tests python-module-mock
BuildPreReq: python-module-six python-module-pytest-cov

%py_provides %oname
%py_requires %mname mock six

%description
This package collects various helpers for writing tests.

%prep
%setup

%build
%python_build_debug

%install
%python_install

%ifarch x86_64
mv %buildroot%_libexecdir %buildroot%_libdir
%endif

%check
python setup.py test
py.test -vv

%files
%doc *.txt
%python_sitelibdir/%mname/*
%python_sitelibdir/*.egg-info

%changelog
* Sun Jan 18 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.10.1-alt1
- Initial build for Sisyphus

