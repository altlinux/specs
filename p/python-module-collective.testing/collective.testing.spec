%define mname collective
%define oname %mname.testing
Name: python-module-%oname
Version: 0.3
Release: alt1.svn20070503
Summary: General package for testing and debugging aids for CMF, Plone, Zope2 and Zope3
License: MIT
Group: Development/Python
Url: https://pypi.python.org/pypi/collective.testing/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://svn.plone.org/svn/collective/collective.testing/trunk/
Source: %name-%version.tar

BuildPreReq: python-module-setuptools-tests python-module-Zope2-tests
BuildPreReq: python-module-Products.PloneTestCase python-module-nose
BuildPreReq: python-module-zope.testing
BuildPreReq: python-module-zope.publisher
BuildPreReq: python-module-zope.app.component

%py_provides %oname
Requires: python-module-Zope2 python-test
%py_requires %mname Products.PloneTestCase zope.testing zope.interface
%py_requires zope.publisher zope.app.component
%add_python_req_skip test

%description
General package for testing and debugging aids for CMF, Plone, Zope2 and
Zope3.

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
nosetests

%files
%doc *.txt docs/*
%python_sitelibdir/%mname/*
%python_sitelibdir/*.egg-info

%changelog
* Sun Nov 09 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.3-alt1.svn20070503
- Initial build for Sisyphus

