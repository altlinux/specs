%define mname collective
%define oname %mname.folderishtypes
Name: python-module-%oname
Version: 2.0
Release: alt1.dev0.git20141017
Summary: Provides folderish types as a replacement for some ATContentTypes
License: GPL
Group: Development/Python
Url: https://pypi.python.org/pypi/collective.folderishtypes/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/collective/collective.folderishtypes.git
Source: %name-%version.tar

BuildPreReq: python-module-setuptools-tests python-module-Zope2-tests
BuildPreReq: python-module-unittest2 python-module-argparse
BuildPreReq: python-module-zope.interface
BuildPreReq: python-module-zope.schema
BuildPreReq: python-module-plone.app.imaging
BuildPreReq: python-module-zope.i18nmessageid
BuildPreReq: python-module-Products.ATContentTypes
BuildPreReq: python-module-plone.app.contenttypes
BuildPreReq: python-module-Products.contentmigration
BuildPreReq: python-module-Products.CMFPlone
BuildPreReq: python-module-Products.CMFCore
BuildPreReq: python-module-Products.Archetypes
BuildPreReq: python-module-Products.LinguaPlone
BuildPreReq: python-module-Products.PloneArticle
BuildPreReq: python-module-plone.registry
BuildPreReq: python-module-plone.app.discussion
BuildPreReq: python-module-plone.app.event
BuildPreReq: python-module-plone.app.portlets
BuildPreReq: python-module-plone.portlets
BuildPreReq: python-module-plone.dexterity
BuildPreReq: python-module-zope.formlib

%py_provides %oname
Requires: python-module-Zope2
%py_requires %mname zope.interface zope.schema plone.app.imaging
%py_requires zope.i18nmessageid Products.ATContentTypes Products.CMFCore
%py_requires plone.app.contenttypes Products.contentmigration
%py_requires Products.CMFPlone Products.Archetypes Products.LinguaPlone
%py_requires Products.PloneArticle plone.registry plone.app.discussion
%py_requires plone.app.event plone.app.portlets plone.portlets
%py_requires plone.dexterity zope.formlib zope.component

%description
Provides the types "Folderish Event", "Folderish News Item" and
"Folderish Document" as replacements for their ATContentTypes
equivalents. Those types are able to hold any other content, like a
Folder.

There is a "portlet" profile, which installs a portlet to show the
contents of an folderish type.

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

%changelog
* Wed Nov 12 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.0-alt1.dev0.git20141017
- Initial build for Sisyphus

