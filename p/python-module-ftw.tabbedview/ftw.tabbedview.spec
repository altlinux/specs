%define mname ftw
%define oname %mname.tabbedview
Name: python-module-%oname
Version: 3.3.14
Release: alt1.dev0.git20141107
Summary: A generic tabbed view for plone content types
License: GPLv2+
Group: Development/Python
Url: https://pypi.python.org/pypi/ftw.tabbedview/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/4teamwork/ftw.tabbedview.git
Source: %name-%version.tar

BuildPreReq: python-module-setuptools-tests python-module-pyquery
BuildPreReq: python-module-ftw.table
BuildPreReq: python-module-collective.quickupload
BuildPreReq: python-module-plone.batching
BuildPreReq: python-module-collective.js.throttledebounce
BuildPreReq: python-module-plone.app.registry
BuildPreReq: python-module-ftw.dictstorage
BuildPreReq: python-module-ftw.upgrade
BuildPreReq: python-module-plone.app.testing
BuildPreReq: python-module-ftw.testing

%py_provides %oname
%py_requires ftw.table collective.quickupload plone.batching
%py_requires collective.js.throttledebounce plone.app.registry
%py_requires ftw.dictstorage ftw.upgrade

%description
This package provides a generic view with multiple tabs for plone. It
provides a generic base tab for listing contents in a table, based on
ftw.table.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR
%py_requires plone.app.testing ftw.testing

%description tests
This package provides a generic view with multiple tabs for plone. It
provides a generic base tab for listing contents in a table, based on
ftw.table.

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
%doc *.rst docs/*
%python_sitelibdir/%mname/*
%python_sitelibdir/*.egg-info
%exclude %python_sitelibdir/%mname/*/test*

%files tests
%python_sitelibdir/%mname/*/test*

%changelog
* Tue Dec 09 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.3.14-alt1.dev0.git20141107
- Initial build for Sisyphus

