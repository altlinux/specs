%define oname plone.schemaeditor
Name: python-module-%oname
Version: 2.0.1
Release: alt1.dev0.git20140930
Summary: Provides through-the-web editing of a zope schema/interface
License: BSD
Group: Development/Python
Url: https://pypi.python.org/pypi/plone.schemaeditor/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/plone/plone.schemaeditor.git
Source: %name-%version.tar

BuildPreReq: python-module-setuptools-tests python-module-Zope2-tests
BuildPreReq: python-module-zope.lifecycleevent
BuildPreReq: python-module-zope.schema
BuildPreReq: python-module-zope.publisher
BuildPreReq: python-module-z3c.form
BuildPreReq: python-module-plone.z3cform
BuildPreReq: python-module-plone.autoform
BuildPreReq: python-module-plone.app.testing
BuildPreReq: python-module-plone.app.robotframework
#BuildPreReq: python-module-plone.app.dexterity

%py_provides %oname
Requires: python-module-Zope2
%py_requires plone zope.component zope.container zope.interface
%py_requires zope.lifecycleevent zope.schema zope.publisher z3c.form
%py_requires plone.z3cform plone.autoform

%description
plone.schemaeditor provides a through-the-web interface for modifying
Zope 3 schemata (interfaces).

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR
%py_requires plone.app.testing plone.app.robotframework
#py_requires plone.app.dexterity

%description tests
plone.schemaeditor provides a through-the-web interface for modifying
Zope 3 schemata (interfaces).

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
%python_sitelibdir/plone/*
%python_sitelibdir/*.egg-info
%exclude %python_sitelibdir/plone/*/test*

%files tests
%python_sitelibdir/plone/*/test*

%changelog
* Mon Oct 13 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.0.1-alt1.dev0.git20140930
- Initial build for Sisyphus

