%define oname plone.app.contentlisting
Name: python-module-%oname
Version: 1.1.1
Release: alt1.dev0.git20140416
Summary: Generic way to make listings of Plone content
License: GPLv2
Group: Development/Python
Url: https://pypi.python.org/pypi/plone.app.contentlisting/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/plone/plone.app.contentlisting.git
Source: %name-%version.tar

BuildPreReq: python-module-setuptools-tests python-module-Zope2-tests
BuildPreReq: python-module-plone.uuid
BuildPreReq: python-module-plone.app.contenttypes
BuildPreReq: python-module-plone.app.testing

%py_provides %oname
Requires: python-module-Zope2
%py_requires plone.app plone.uuid

%description
Listing of content for the Plone CMS.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR
%py_requires plone.app.contenttypes plone.app.testing

%description tests
Listing of content for the Plone CMS.

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
%python_sitelibdir/plone/app/*
%python_sitelibdir/*.egg-info
%exclude %python_sitelibdir/plone/app/*/tests

%files tests
%python_sitelibdir/plone/app/*/tests

%changelog
* Tue Oct 14 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1.1-alt1.dev0.git20140416
- Initial build for Sisyphus

