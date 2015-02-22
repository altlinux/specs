%define mname zopyx.smartprintng
%define oname %mname.plone
Name: python-module-%oname
Version: 2.1.27
Release: alt1.git20150217
Summary: Produce & Publisher server integration with Plone
License: GPL
Group: Development/Python
Url: https://pypi.python.org/pypi/zopyx.smartprintng.plone/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/zopyx/zopyx.smartprintng.plone.git
Source: %name-%version.tar

BuildPreReq: python-module-setuptools-tests python-module-Zope2-tests
BuildPreReq: python-module-BeautifulSoup python-module-Pillow
BuildPreReq: python-module-lxml python-module-uuid
BuildPreReq: python-module-unittest2 python-module-sphinx-devel
BuildPreReq: python-module-archetypes.schemaextender
BuildPreReq: python-module-zope.testing
BuildPreReq: python-module-zopyx.smartprintng.client
BuildPreReq: python-module-zopyx.convert2
BuildPreReq: python-module-Products.ATContentTypes
BuildPreReq: python-module-Products.Archetypes
BuildPreReq: python-module-Products.CMFCore
BuildPreReq: python-module-plone.dexterity
BuildPreReq: python-module-plone.app.imaging
BuildPreReq: python-module-zope.schema
BuildPreReq: python-module-zope.browserpage
BuildPreReq: python-module-zope.app.pagetemplate
BuildPreReq: python-module-zope.app.component

%py_provides %oname
Requires: python-module-Zope2
%py_requires %mname BeautifulSoup lxml uuid PIL zopyx.convert2
%py_requires archetypes.schemaextender zopyx.smartprintng.client
%py_requires Products.ATContentTypes Products.Archetypes plone.dexterity
%py_requires Products.CMFCore plone.app.imaging zope.interface
%py_requires zope.component zope.schema zope.browserpage
%py_requires zope.app.pagetemplate zope.app.component

%description
The Produce & Publish Client Connector for Plone.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR
%py_requires unittest2 zope.testing

%description tests
The Produce & Publish Client Connector for Plone.

This package contains tests for %oname.

%prep
%setup

%build
%python_build_debug

%install
install -d %buildroot%python_sitelibdir/zopyx/smartprintng/
cp -fR zopyx/smartprintng/plone \
	%buildroot%python_sitelibdir/zopyx/smartprintng/
cp -fR *.egg-info \
	%buildroot%python_sitelibdir/
 
%check
python setup.py test

%files
%doc *.txt
%python_sitelibdir/zopyx/smartprintng/plone
%python_sitelibdir/*.egg-info
%exclude %python_sitelibdir/zopyx/smartprintng/plone/*/tests

%files tests
%python_sitelibdir/zopyx/smartprintng/plone/*/tests

%changelog
* Sun Feb 22 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.1.27-alt1.git20150217
- Initial build for Sisyphus

