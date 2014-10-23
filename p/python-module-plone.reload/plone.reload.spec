%define oname plone.reload
Name: python-module-%oname
Version: 2.1
Release: alt1.dev.git20110604
Summary: Configuration and code reload without server restarts
License: BSD
Group: Development/Python
Url: https://pypi.python.org/pypi/plone.reload/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/plone/plone.reload.git
Source: %name-%version.tar

BuildPreReq: python-module-setuptools-tests python-module-Zope2-tests
BuildPreReq: python-module-zope.processlifetime
BuildPreReq: python-module-zope.publisher
BuildPreReq: python-module-zope.site
BuildPreReq: python-module-zope.testing
BuildPreReq: python-module-Products.CMFCore

%py_provides %oname
Requires: python-module-Zope2
%py_requires plone zope.component zope.interface zope.processlifetime
%py_requires zope.publisher zope.site zope.testing Products.CMFCore

%description
Configuration and code reload for Zope 2 and Plone without server
restarts.

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
%doc *.txt *.rst docs/*
%python_sitelibdir/*

%changelog
* Thu Oct 23 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.1-alt1.dev.git20110604
- Initial build for Sisyphus

