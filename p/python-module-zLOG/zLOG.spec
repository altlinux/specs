%define oname zLOG
Name: python-module-%oname
Version: 2.12.0
Release: alt1.git20130313
Summary: A general logging facility
License: ZPLv2.1
Group: Development/Python
Url: https://pypi.python.org/pypi/zLOG/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/zopefoundation/zLOG.git
Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-module-setuptools-tests python-module-zconfig

%py_provides %oname

%description
This package provides a general logging facility that, at this point, is
just a small shim over Python's logging module. Therefore, unless you
need to support a legacy package from the Zope 2 world, you're probably
better off using Python's logging module.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR

%description tests
This package provides a general logging facility that, at this point, is
just a small shim over Python's logging module. Therefore, unless you
need to support a legacy package from the Zope 2 world, you're probably
better off using Python's logging module.

This package contains tests for %oname.

%prep
%setup

%build
%python_build_debug

%install
%python_install

%check
python setup.py test

%files
%doc *.txt
%python_sitelibdir/*
%exclude %python_sitelibdir/*/tests

%files tests
%python_sitelibdir/*/tests

%changelog
* Thu Oct 16 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.12.0-alt1.git20130313
- Snapshot from git

* Sat Oct 11 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.12.0-alt1
- Initial build for Sisyphus

