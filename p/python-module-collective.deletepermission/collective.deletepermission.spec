%define mname collective
%define oname %mname.deletepermission
Name: python-module-%oname
Version: 1.1.4
Release: alt1.dev0.git20141107
Summary: Implements a new permission "Delete portal content" for Plone
License: GPLv2+
Group: Development/Python
Url: https://pypi.python.org/pypi/collective.deletepermission/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/4teamwork/collective.deletepermission.git
Source: %name-%version.tar

BuildPreReq: python-module-setuptools-tests python-module-Zope2-tests
BuildPreReq: python-module-lxml python-module-mechanize
BuildPreReq: python-module-transaction python-module-unittest2
BuildPreReq: python-module-Products.Archetypes
BuildPreReq: python-module-Products.CMFCore
BuildPreReq: python-module-Products.CMFPlone
BuildPreReq: python-module-Products.PythonScripts
BuildPreReq: python-module-collective.monkeypatcher
BuildPreReq: python-module-ftw.upgrade
BuildPreReq: python-module-Products.GenericSetup
BuildPreReq: python-module-plone.app.portlets
BuildPreReq: python-module-plone.app.testing
BuildPreReq: python-module-zope.configuration
BuildPreReq: python-module-ftw.builder-tests

%py_provides %oname
Requires: python-module-Zope2
%py_requires %mname Products.Archetypes Products.CMFCore ftw.upgrade
%py_requires Products.CMFPlone Products.PythonScripts
%py_requires collective.monkeypatcher

%description
The default Plone permission for deleting content does not allow to
delete content from a folder without being able to delete the folder
itself.

The collective.deletepermission package introduces an additional
permission Delete portal content. By seperating the permission Delete
portal content (I can delete this content object) from the permission
Delete objects (I can delete something IN this folder), we now can allow
a Contributor to delete content he created (Owner role) without letting
him delete folders and objects belonging to other users - even in a
nested environment.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR
%py_requires Products.GenericSetup plone.app.portlets plone.app.testing
%py_requires zope.configuration ftw.builder.testing

%description tests
The default Plone permission for deleting content does not allow to
delete content from a folder without being able to delete the folder
itself.

The collective.deletepermission package introduces an additional
permission Delete portal content. By seperating the permission Delete
portal content (I can delete this content object) from the permission
Delete objects (I can delete something IN this folder), we now can allow
a Contributor to delete content he created (Owner role) without letting
him delete folders and objects belonging to other users - even in a
nested environment.

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
* Mon Dec 15 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1.4-alt1.dev0.git20141107
- Initial build for Sisyphus

