%define mname simplelayout
%define oname %mname.types.common

Name: python-module-%oname
Version: 3.1.1
Release: alt2.dev0.git20141107
Summary: Simplelayout component providing content types
License: GPLv2+
Group: Development/Python
Url: https://pypi.python.org/pypi/simplelayout.types.common/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/4teamwork/simplelayout.types.common.git
Source: %name-%version.tar

BuildPreReq: python-module-setuptools-tests python-module-Zope2-tests
BuildPreReq: python-module-ftw.upgrade
BuildPreReq: python-module-ftw.testing
BuildPreReq: python-module-plone.app.testing
BuildPreReq: python-module-simplelayout.base
BuildPreReq: python-module-Products.CMFPlone
BuildPreReq: python-module-Products.CMFCore
BuildPreReq: python-module-Products.ATContentTypes
BuildPreReq: python-module-Products.Archetypes
BuildPreReq: python-module-Products.validation
BuildPreReq: python-module-Products.LinguaPlone
BuildPreReq: python-module-plone.app.blob
BuildPreReq: python-module-zope.viewlet
BuildPreReq: python-module-zope.schema
BuildPreReq: python-module-zope.i18nmessageid
BuildPreReq: python-module-zope.configuration

%py_provides %oname
Requires: python-module-%mname.types = %EVR
Requires: python-module-Zope2
%py_requires ftw.upgrade simplelayout.base Products.CMFPlone zope.schema
%py_requires Products.CMFCore Products.ATContentTypes plone.app.blob
%py_requires Products.Archetypes Products.validation zope.component
%py_requires Products.LinguaPlone zope.viewlet zope.interface
%py_requires zope.i18nmessageid

%description
Simplelayout component providing content types.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR
%py_requires ftw.testing plone.app.testing zope.configuration

%description tests
Simplelayout component providing content types.

This package contains tests for %oname.

%package -n python-module-%mname.types
Summary: Core files of %mname.types
Group: Development/Python
%py_provides %mname.types
%py_requires %mname

%description -n python-module-%mname.types
Core files of %mname.types.

%prep
%setup

%build
%python_build_debug

%install
%python_install

%ifarch x86_64
mv %buildroot%_libexecdir %buildroot%_libdir
%endif

install -p -m644 %mname/types/__init__.py \
	%buildroot%python_sitelibdir/%mname/types/

%check
python setup.py test

%files
%doc *.rst docs/*
%python_sitelibdir/%mname/types/*
%python_sitelibdir/*.egg-info
%exclude %python_sitelibdir/%mname/types/*/test*
%exclude %python_sitelibdir/%mname/types/__init__.py*

%files tests
%python_sitelibdir/%mname/types/*/test*

%files -n python-module-%mname.types
%dir %python_sitelibdir/%mname/types
%python_sitelibdir/%mname/types/__init__.py*

%changelog
* Sat Nov 29 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.1.1-alt2.dev0.git20141107
- Enabled testing

* Sat Nov 29 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.1.1-alt1.dev0.git20141107
- Initial build for Sisyphus

