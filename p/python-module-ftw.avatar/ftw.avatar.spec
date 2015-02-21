%define mname ftw
%define oname %mname.avatar
Name: python-module-%oname
Version: 1.0.6
Release: alt1.dev0.git20150109
Summary: Better default user avatars for Plone
License: GPLv2+
Group: Development/Python
Url: https://pypi.python.org/pypi/ftw.avatar/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/4teamwork/ftw.avatar.git
Source: %name-%version.tar

BuildPreReq: python-module-setuptools-tests python-module-Zope2-tests
BuildPreReq: python-module-Pillow python-module-transaction
BuildPreReq: python-module-unittest2
BuildPreReq: python-module-Products.CMFCore
BuildPreReq: python-module-Products.PlonePAS
BuildPreReq: python-module-plone.scale
BuildPreReq: python-module-zope.annotation
BuildPreReq: python-module-ftw.builder-tests
BuildPreReq: python-module-ftw.testbrowser
BuildPreReq: python-module-plone.app.testing
BuildPreReq: python-module-zope.configuration

%py_provides %oname
Requires: python-module-Zope2
%py_requires %mname PIL Products.CMFCore Products.PlonePAS plone.scale
%py_requires zope.annotation zope.component zope.interface

%description
ftw.avatar generates a personal default avatar for new Plone users.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR
%py_requires ftw.builder.testing ftw.testbrowser plone.app.testing
%py_requires transaction unittest2 zope.configuration

%description tests
ftw.avatar generates a personal default avatar for new Plone users.

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
python test-generate-avatars.py -v

%files
%doc *.rst docs/*
%python_sitelibdir/%mname/*
%python_sitelibdir/*.egg-info
%exclude %python_sitelibdir/%mname/*/test*

%files tests
%python_sitelibdir/%mname/*/test*

%changelog
* Sat Feb 21 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.6-alt1.dev0.git20150109
- Initial build for Sisyphus

