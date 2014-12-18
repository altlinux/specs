%define mname p4a
%define oname %mname.video
Name: python-module-%oname
Version: 1.4
Release: alt1.dev.git20130827
Summary: Plone4Artists video abstraction library
License: GPLv2+
Group: Development/Python
Url: https://pypi.python.org/pypi/p4a.video/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/collective/p4a.video.git
Source: %name-%version.tar

BuildPreReq: python-module-setuptools-tests python-module-Zope2-tests
BuildPreReq: python-module-hachoir-core python-module-hachoir-metadata
BuildPreReq: python-module-hachoir-parser
BuildPreReq: python-module-p4a.subtyper
BuildPreReq: python-module-p4a.common
BuildPreReq: python-module-p4a.z2utils
BuildPreReq: python-module-p4a.fileimage
BuildPreReq: python-module-Products.CMFPlone
BuildPreReq: python-module-Products.CMFCore
BuildPreReq: python-module-Products.CMFDynamicViewFTI
BuildPreReq: python-module-Products.ContentLicensing
BuildPreReq: python-module-Products.statusmessages
BuildPreReq: python-module-zope.annotation
BuildPreReq: python-module-zope.lifecycleevent
BuildPreReq: python-module-zope.event
BuildPreReq: python-module-zope.formlib
BuildPreReq: python-module-zope.i18nmessageid
BuildPreReq: python-module-zope.app.i18n
BuildPreReq: python-module-zope.schema
BuildPreReq: python-module-zope.app.form
BuildPreReq: python-module-Products.PloneTestCase
BuildPreReq: python-module-zope.testing
BuildPreReq: python-module-zope.component-tests

%py_provides %oname
Requires: python-module-Zope2
%py_requires %mname p4a.subtyper p4a.common p4a.z2utils p4a.fileimage
%py_requires Products.CMFPlone Products.CMFCore Products.statusmessages
%py_requires Products.CMFDynamicViewFTI Products.ContentLicensing
%py_requires zope.component zope.interface zope.annotation zope.event
%py_requires zope.lifecycleevent zope.formlib zope.i18nmessageid
%py_requires zope.app.i18n zope.schema zope.app.form

%description
The p4a.video package provides a framework for handling video content on
the Zope 2 and Zope 3 platforms. It was inspired by the Plone ATVideo
product and even borrows some UI.

p4a.video allows you to:

* convert a file object to a video
* extract the video metadata
* render an appropriate view (depending on the file format)

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR
%py_requires Products.PloneTestCase zope.testing zope.component.testing

%description tests
The p4a.video package provides a framework for handling video content on
the Zope 2 and Zope 3 platforms. It was inspired by the Plone ATVideo
product and even borrows some UI.

p4a.video allows you to:

* convert a file object to a video
* extract the video metadata
* render an appropriate view (depending on the file format)

This package contains tests for %oname.

%prep
%setup

%build
%python_build_debug

%install
install -d %buildroot%python_sitelibdir/%mname
cp -fR %mname/video %buildroot%python_sitelibdir/%mname/
cp -fR *.egg-info %buildroot%python_sitelibdir/

%check
python setup.py test

%files
%doc *.txt docs/*
%python_sitelibdir/%mname/*
%python_sitelibdir/*.egg-info
%exclude %python_sitelibdir/%mname/*/test*

%files tests
%python_sitelibdir/%mname/*/test*

%changelog
* Thu Dec 18 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.4-alt1.dev.git20130827
- Initial build for Sisyphus

