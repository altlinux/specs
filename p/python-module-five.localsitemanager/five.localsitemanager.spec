%define mname five
%define oname %mname.localsitemanager
Name: python-module-%oname
Version: 2.0.6
Release: alt1.dev.git20130915
Summary: Local site manager implementation for Zope 2
License: ZPLv2.1
Group: Development/Python
Url: https://pypi.python.org/pypi/five.localsitemanager/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/zopefoundation/five.localsitemanager.git
Source: %name-%version.tar

BuildPreReq: python-module-setuptools-tests python-module-Zope2-tests

%py_provides %oname
Requires: python-module-%mname = %EVR
Requires: python-module-Zope2
%py_requires ZODB3 zope.component zope.event zope.interface
%py_requires zope.location zope.lifecycleevent
# for tests
%py_requires zope.testing

%description
five.localsitemanager attempts to provide a local site manager
implementation that is as close to the zope.interface / zope.component
implementation as possible. Some reservations that do not conflict with
the original API have been made to ease the path with CMF.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR

%description tests
five.localsitemanager attempts to provide a local site manager
implementation that is as close to the zope.interface / zope.component
implementation as possible. Some reservations that do not conflict with
the original API have been made to ease the path with CMF.

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

install -p -m644 src/%mname/__init__.py \
	%buildroot%python_sitelibdir/%mname/

%check
export PYTHONPATH=%buildroot%python_sitelibdir
python setup.py test

%files
%doc *.rst
%python_sitelibdir/%mname/*
%exclude %python_sitelibdir/%mname/__init__.py*
%python_sitelibdir/*.egg-info
%exclude %python_sitelibdir/%mname/*/tests.*

%files tests
%python_sitelibdir/%mname/*/tests.*

%files -n python-module-%mname
%dir %python_sitelibdir/%mname
%python_sitelibdir/%mname/__init__.py*

%changelog
* Sat Oct 11 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.0.6-alt1.dev.git20130915
- Initial build for Sisyphus

