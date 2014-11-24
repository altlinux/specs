%define mname collective
%define oname %mname.prettyphoto
Name: python-module-%oname
Version: 0.6
Release: alt1.dev0.git20130418
Summary: prettyPhoto integration for Plone
License: GPL
Group: Development/Python
Url: https://pypi.python.org/pypi/collective.prettyphoto/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/collective/collective.prettyphoto.git
Source: %name-%version.tar

BuildPreReq: python-module-setuptools-tests python-module-Zope2-tests
BuildPreReq: python-module-Products.CMFPlone
BuildPreReq: python-module-Products.CMFCore
BuildPreReq: python-module-plone.theme
BuildPreReq: python-module-plone.browserlayer
BuildPreReq: python-module-zope.configuration
BuildPreReq: python-module-plone.app.testing

%py_provides %oname
Requires: python-module-Zope2
%py_requires %mname Products.CMFPlone Products.CMFCore plone.theme
%py_requires plone.browserlayer zope.component zope.interface

%description
prettyPhoto is a jQuery based lightbox clone. It supports images, it
also add support for videos, flash, YouTube, iFrames and ajax.

It's a full blown media lightbox. The setup is easy and quick, plus the
script is compatible in every major browser.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR
%py_requires plone.app.testing zope.configuration

%description tests
prettyPhoto is a jQuery based lightbox clone. It supports images, it
also add support for videos, flash, YouTube, iFrames and ajax.

It's a full blown media lightbox. The setup is easy and quick, plus the
script is compatible in every major browser.

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
%exclude %python_sitelibdir/%mname/*/*/test*

%files tests
%python_sitelibdir/%mname/*/test*
%python_sitelibdir/%mname/*/*/test*

%changelog
* Mon Nov 24 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.6-alt1.dev0.git20130418
- Initial build for Sisyphus

