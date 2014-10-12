%define oname Products.CMFTestCase
Name: python-module-%oname
Version: 0.9.13
Release: alt1.dev0.git20120702
Summary: Integration testing framework for CMF
License: ZPL
Group: Development/Python
Url: https://pypi.python.org/pypi/Products.CMFTestCase/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/plone/Products.CMFTestCase.git
Source: %name-%version.tar

BuildPreReq: python-module-setuptools-tests python-module-Zope2-tests
BuildPreReq: python-module-zope.site
BuildPreReq: python-module-zope.testing
BuildPreReq: python-module-Products.CMFCalendar
BuildPreReq: python-module-Products.CMFCore
BuildPreReq: python-module-Products.CMFDefault
BuildPreReq: python-module-Products.GenericSetup

%py_provides %oname
Requires: python-module-Zope2
%py_requires Products.CMFCalendar Products.CMFCore Products.CMFDefault
%py_requires zope.component zope.interface ZODB3 zope.site zope.testing
%py_requires Products.GenericSetup

%description
CMFTestCase is a thin layer on top of the ZopeTestCase package. It has
been developed to simplify testing of CMF-based applications and
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
%python_sitelibdir/*

%changelog
* Sun Oct 12 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.9.13-alt1.dev0.git20120702
- Initial build for Sisyphus

