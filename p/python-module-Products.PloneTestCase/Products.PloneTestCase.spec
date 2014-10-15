%define oname Products.PloneTestCase

Name: python-module-%oname
Version: 0.9.19
Release: alt2.dev0.git20140302
Summary: Integration testing framework for Plone
License: GPL
Group: Development/Python
Url: https://pypi.python.org/pypi/Products.PloneTestCase/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/plone/Products.PloneTestCase.git
Source: %name-%version.tar

BuildPreReq: python-module-setuptools-tests python-module-Zope2-tests
BuildPreReq: python-module-Products.ATContentTypes
BuildPreReq: python-module-Products.CMFCore
BuildPreReq: python-module-Products.GenericSetup
BuildPreReq: python-module-Products.CMFPlone
BuildPreReq: python-module-unittest2

%py_provides %oname
Requires: python-module-Zope2
%py_requires zope.component zope.interface zope.site zope.testing
%py_requires Products.ATContentTypes Products.CMFCore
%py_requires Products.GenericSetup ZODB3
%py_requires Products.CMFPlone

%description
PloneTestCase is a thin layer on top of the ZopeTestCase package. It has
been developed to simplify testing of Plone-based applications and
products.

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

%files
%doc *.txt
%python_sitelibdir/Products/*
%python_sitelibdir/*.egg-info

%changelog
* Wed Oct 15 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.9.19-alt2.dev0.git20140302
- Added necessary requirements
- Enabled testing

* Tue Oct 14 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.9.19-alt1.dev0.git20140302
- Initial build for Sisyphus

