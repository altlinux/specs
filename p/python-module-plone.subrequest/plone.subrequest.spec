%define oname plone.subrequest
Name: python-module-%oname
Version: 1.6.8
Release: alt1.dev0.git20140220
Summary: Subrequests for Zope2
License: GPLv2
Group: Development/Python
Url: https://pypi.python.org/pypi/plone.subrequest/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/plone/plone.subrequest.git
Source: %name-%version.tar

BuildPreReq: python-module-setuptools-tests python-module-Zope2-tests
BuildPreReq: python-module-manuel python-module-docutils
BuildPreReq: python-module-five.globalrequest
BuildPreReq: python-module-zope.globalrequest
BuildPreReq: python-module-five.localsitemanager
BuildPreReq: python-module-plone.testing
BuildPreReq: python-module-plone.app.blob

%py_provides %oname
%py_requires plone five.globalrequest zope.globalrequest

%description
plone.subrequest provides a mechanism for issuing subrequests under
Zope2.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR
%py_requires five.localsitemanager plone.testing plone.app.blob

%description tests
plone.subrequest provides a mechanism for issuing subrequests under
Zope2.

This package contains tests for %oname.

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
%doc *.txt docs/*
%python_sitelibdir/plone/*
%python_sitelibdir/*.egg-info
%exclude %python_sitelibdir/plone/*/test*

%files tests
%python_sitelibdir/plone/*/test*

%changelog
* Tue Oct 14 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.6.8-alt1.dev0.git20140220
- Initial build for Sisyphus

