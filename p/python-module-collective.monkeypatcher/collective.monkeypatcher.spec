%define _unpackaged_files_terminate_build 1
%define mname collective
%define oname %mname.monkeypatcher

Name: python-module-%oname
Version: 1.1.3
Release: alt1.1
Summary: Support for applying monkey patches late in the startup cycle
License: BSD
Group: Development/Python
Url: https://pypi.python.org/pypi/collective.monkeypatcher/

# https://github.com/plone/collective.monkeypatcher.git
Source: %name-%version.tar

BuildRequires: python-module-setuptools
BuildRequires: python2.7(zope.interface) python2.7(zope.schema) python2.7(zope.component) python2.7(zope.component.testing) python2.7(zope.configuration.xmlconfig)

%py_provides %oname
Requires: python-module-%mname = %EVR
%py_requires zope.component zope.schema zope.interface zope.event
%py_requires zope.configuration

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
%py_requires zope.component.testing

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

%if "%_libexecdir" != "%_libdir"
mv %buildroot%_libexecdir %buildroot%_libdir
%endif

install -p -m644 %mname/__init__.py \
	%buildroot%python_sitelibdir/%mname/

%check
python setup.py test

%files
%doc *.rst docs/*
%python_sitelibdir/%mname/*
%python_sitelibdir/*.egg-info
%python_sitelibdir/*-nspkg.pth
%exclude %python_sitelibdir/%mname/*/tests
%exclude %python_sitelibdir/%mname/__init__.py*

%files tests
%python_sitelibdir/%mname/*/tests

%files -n python-module-%mname
%dir %python_sitelibdir/%mname
%python_sitelibdir/%mname/__init__.py*

%changelog
* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 1.1.3-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Tue Dec 12 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 1.1.3-alt1
- Updated to upstream version 1.1.3.

* Tue May 24 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.1.1-alt1.git20141210.1
- (AUTO) subst_x86_64.

* Thu Dec 11 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1.1-alt1.git20141210
- Version 1.1.1

* Sun Oct 12 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.2-alt1.git20140826
- Initial build for Sisyphus

