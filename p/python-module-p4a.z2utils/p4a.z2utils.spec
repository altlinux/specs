%define mname p4a
%define oname %mname.z2utils
Name: python-module-%oname
Version: 1.0.3
Release: alt1.git20130528
Summary: Miscellaneous utilities for Zope 2
License: GPL
Group: Development/Python
Url: https://pypi.python.org/pypi/p4a.z2utils/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/collective/p4a.z2utils.git
Source: %name-%version.tar

BuildPreReq: python-module-setuptools-tests python-module-Zope2-tests
BuildPreReq: python-module-zope.publisher
BuildPreReq: python-module-zope.app.traversing
BuildPreReq: python-module-zope.app.publication
BuildPreReq: python-module-Products.Archetypes
BuildPreReq: python-module-Products.CMFDynamicViewFTI
BuildPreReq: python-module-Products.CMFCore
BuildPreReq: python-module-Products.CMFPlone
BuildPreReq: python-module-zope.testing

%py_provides %oname
Requires: python-module-%mname = %EVR
Requires: python-module-Zope2
%py_requires zope.component zope.interface zope.publisher
%py_requires zope.app.traversing zope.app.publication Products.CMFCore
%py_requires Products.Archetypes Products.CMFDynamicViewFTI
%py_requires Products.CMFPlone

%description
Miscellaneous utilities for Zope 2.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR
%py_requires zope.testing

%description tests
Miscellaneous utilities for Zope 2.

This package contains tests for %oname.

%package -n python-module-%mname
Summary: Core files of %mname
Group: Development/Python
%py_provides %mname

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

install -p -m644 p4a/__init__.py %buildroot%python_sitelibdir/p4a/

%check
python setup.py test
rm -fR build
py.test

%files
%doc docs/*
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
* Fri Oct 31 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.3-alt1.git20130528
- Initial build for Sisyphus

