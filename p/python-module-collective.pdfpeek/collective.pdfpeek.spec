%define mname collective
%define oname %mname.pdfpeek
Name: python-module-%oname
Version: 2.0.1
Release: alt1.dev0.git20141204
Summary: Generate image previews of PDF files uploaded to Plone
License: GPLv2+
Group: Development/Python
Url: https://pypi.python.org/pypi/collective.pdfpeek/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/collective/collective.pdfpeek.git
Source: %name-%version.tar

BuildPreReq: python-module-setuptools-tests python-module-Zope2-tests
BuildPreReq: python-module-PyPDF2 python-module-Pillow %_bindir/gs
BuildPreReq: python-module-msgpack python-module-openid
BuildPreReq: python-module-plone.app.registry
BuildPreReq: python-module-plone.browserlayer
BuildPreReq: python-module-plone.rfc822
BuildPreReq: python-module-plone.api
BuildPreReq: python-module-Products.Archetypes
BuildPreReq: python-module-Products.ATContentTypes
BuildPreReq: python-module-plone.behavior
BuildPreReq: python-module-plone.app.contenttypes
BuildPreReq: python-module-collective.zamqp
BuildPreReq: python-module-plone.app.testing
BuildPreReq: python-module-Products.CMFPlone
BuildPreReq: python-module-Products.CMFCore
BuildPreReq: python-module-zope.annotation
BuildPreReq: python-module-zope.traversing
BuildPreReq: python-module-zope.publisher
BuildPreReq: python-module-zope.schema
BuildPreReq: python-module-zope.i18nmessageid
BuildPreReq: python-module-zc.lockfile

%py_provides %oname
Requires: python-module-Zope2 %_bindir/gs
%py_requires %mname PyPDF2 plone.app.registry plone.browserlayer PIL
%py_requires plone.rfc822 plone.api Products.Archetypes plone.behavior
%py_requires Products.ATContentTypes plone.app.contenttypes msgpack
%py_requires collective.zamqp Products.CMFPlone Products.CMFCore
%py_requires zope.component zope.interface zope.annotation zope.schema
%py_requires zope.traversing zope.publisher zope.i18nmessageid
%py_requires zc.lockfile

%description
A Plone 4 product that generates image thumbnail previews of PDF files
stored on ATFile based objects.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR
%py_requires plone.app.testing

%description tests
A Plone 4 product that generates image thumbnail previews of PDF files
stored on ATFile based objects.

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
* Fri Dec 12 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.0.1-alt1.dev0.git20141204
- Initial build for Sisyphus

