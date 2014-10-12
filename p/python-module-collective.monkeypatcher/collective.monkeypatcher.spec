%define mname collective
%define oname %mname.monkeypatcher
Name: python-module-%oname
Version: 1.0.2
Release: alt1.git20140826
Summary: Support for applying monkey patches late in the startup cycle
License: BSD
Group: Development/Python
Url: https://pypi.python.org/pypi/collective.monkeypatcher/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/plone/collective.monkeypatcher.git
Source: %name-%version.tar

BuildPreReq: python-module-setuptools-tests

%py_provides %oname
Requires: python-module-%mname = %EVR

%description
Sometimes, a monkey patch is a necessary evil.

This package makes it easier to apply a monkey patch during Zope
startup. It uses the ZCML configuration machinery to ensure that patches
are loaded "late" in the startup cycle, so that the original code has
had time to be fully initialised and configured. This is similar to
using the initialize() method in a product's __init__.py, except it does
not require that the package be a full-blown Zope 2 product with a
persistent Control_Panel entry.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR

%description tests
Sometimes, a monkey patch is a necessary evil.

This package makes it easier to apply a monkey patch during Zope
startup. It uses the ZCML configuration machinery to ensure that patches
are loaded "late" in the startup cycle, so that the original code has
had time to be fully initialised and configured. This is similar to
using the initialize() method in a product's __init__.py, except it does
not require that the package be a full-blown Zope 2 product with a
persistent Control_Panel entry.

This package contains tests for %oname.

%package -n python-module-%mname
Summary: Core files of %mname
Group: Development/Python

%description -n python-module-%mname
Core files of %mname.

%prep
%setup

%build
%python_build_debug

%install
%python_install

%ifarch x86_64
mv %buildroot%_libexecdir %buildroot%_libdir
%endif

install -p -m644 %mname/__init__.py \
	%buildroot%python_sitelibdir/%mname/

%check
python setup.py test

%files
%doc *.txt docs/*
%python_sitelibdir/%mname/*
%python_sitelibdir/*.egg-info
%exclude %python_sitelibdir/%mname/*/tests
%exclude %python_sitelibdir/%mname/__init__.py*

%files tests
%python_sitelibdir/%mname/*/tests

%files -n python-module-%mname
%dir %python_sitelibdir/%mname
%python_sitelibdir/%mname/__init__.py*

%changelog
* Sun Oct 12 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.2-alt1.git20140826
- Initial build for Sisyphus

