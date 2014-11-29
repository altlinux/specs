%define mname simplelayout
%define oname %mname.portlet.dropzone
Name: python-module-%oname
Version: 1.2.3
Release: alt1.dev0.git20130814
Summary: Plone portlet with a simplelayout dropzone
License: GPLv2+
Group: Development/Python
Url: https://pypi.python.org/pypi/simplelayout.portlet.dropzone/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/4teamwork/simplelayout.portlet.dropzone.git
Source: %name-%version.tar

BuildPreReq: python-module-setuptools-tests python-module-Zope2-tests
BuildPreReq: python-module-plone.app.portlets
BuildPreReq: python-module-simplelayout.base
BuildPreReq: python-module-Products.statusmessages
BuildPreReq: python-module-Products.CMFCore
BuildPreReq: python-module-plone.protect
BuildPreReq: python-module-plone.fieldsets
BuildPreReq: python-module-plone.app.form
BuildPreReq: python-module-plone.app.controlpanel
BuildPreReq: python-module-plone.portlets
BuildPreReq: python-module-zope.schema
BuildPreReq: python-module-zope.formlib
BuildPreReq: python-module-zope.event
BuildPreReq: python-module-zope.viewlet
BuildPreReq: python-module-zope.contentprovider
BuildPreReq: python-module-zope.i18nmessageid
BuildPreReq: python-module-Products.PloneTestCase
BuildPreReq: python-module-zope.testing

%py_provides %oname
Requires: python-module-%mname.portlet = %EVR
Requires: python-module-Zope2
%py_requires plone.app.portlets simplelayout.base Products.CMFCore
%py_requires Products.statusmessages plone.protect plone.fieldsets
%py_requires plone.app.form plone.app.controlpanel plone.portlets
%py_requires zope.interface zope.schema zope.formlib zope.event
%py_requires zope.component zope.viewlet zope.contentprovider
%py_requires zope.i18nmessageid

%description
Provides a portlet with a "drop zone" for simplelayout blocks. You can
simply drag a block and drop it into the portlet area. The block is now
shown as portlet. This package has its own configlet for image sizes.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR
%py_requires Products.PloneTestCase zope.testing

%description tests
Provides a portlet with a "drop zone" for simplelayout blocks. You can
simply drag a block and drop it into the portlet area. The block is now
shown as portlet. This package has its own configlet for image sizes.

This package contains tests for %oname.

%package -n python-module-%mname.portlet
Summary: Core files of %mname.portlet
Group: Development/Python
%py_provides %mname.portlet
%py_requires %mname

%description -n python-module-%mname.portlet
Core files of %mname.portlet.

%prep
%setup

%build
%python_build_debug

%install
%python_install

%ifarch x86_64
mv %buildroot%_libexecdir %buildroot%_libdir
%endif

install -p -m644 %mname/portlet/__init__.py \
	%buildroot%python_sitelibdir/%mname/portlet/

%check
python setup.py test
py.test %mname/portlet/dropzone/tests.py

%files
%doc *.rst docs/*
%python_sitelibdir/%mname/portlet/*
%python_sitelibdir/*.egg-info
%exclude %python_sitelibdir/%mname/portlet/*/tests.*
%exclude %python_sitelibdir/%mname/portlet/__init__.py*

%files tests
%python_sitelibdir/%mname/portlet/*/tests.*

%files -n python-module-%mname.portlet
%dir %python_sitelibdir/%mname/portlet
%python_sitelibdir/%mname/portlet/__init__.py*

%changelog
* Sat Nov 29 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.2.3-alt1.dev0.git20130814
- Initial build for Sisyphus

