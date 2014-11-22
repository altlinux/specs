%define oname plone.multilingualbehavior
Name: python-module-%oname
Version: 1.2.2
Release: alt2.dev0.git20140523
Summary: Dexterity behavior for enabling multilingual extensions
License: GPL
Group: Development/Python
Url: https://pypi.python.org/pypi/plone.multilingualbehavior/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/plone/plone.multilingualbehavior.git
Source: %name-%version.tar

BuildPreReq: python-module-setuptools-tests python-module-nose
BuildPreReq: python-module-plone.directives.form
BuildPreReq: python-module-plone.directives.dexterity
BuildPreReq: python-module-plone.app.dexterity
BuildPreReq: python-module-plone.multilingual
BuildPreReq: python-module-plone.app.multilingual
BuildPreReq: python-module-plone.app.testing
BuildPreReq: python-module-Products.CMFCore
BuildPreReq: python-module-Products.GenericSetup
BuildPreReq: python-module-plone.dexterity
BuildPreReq: python-module-plone.registry
BuildPreReq: python-module-plone.schemaeditor
BuildPreReq: python-module-plone.supermodel
BuildPreReq: python-module-zope.app.intid
BuildPreReq: python-module-zope.component
BuildPreReq: python-module-zope.interface
BuildPreReq: python-module-zope.lifecycleevent
BuildPreReq: python-module-zope.event
BuildPreReq: python-module-zope.schema
BuildPreReq: python-module-zope.i18nmessageid
BuildPreReq: python-module-zope.deferredimport
BuildPreReq: python-module-z3c.relationfield
BuildPreReq: python-module-z3c.form
BuildPreReq: python-module-plone.formwidget.contenttree
BuildPreReq: python-module-plone.testing
BuildPreReq: python-module-zope.configuration

%py_provides %oname
%py_requires plone.directives.form plone.directives.dexterity
%py_requires plone.app.dexterity plone.multilingual Products.CMFCore
%py_requires plone.app.multilingual Products.GenericSetup plone.registry
%py_requires plone.dexterity plone.schemaeditor plone.supermodel
%py_requires zope.app.intid zope.component zope.interface zope.event
%py_requires zope.lifecycleevent zope.schema zope.i18nmessageid
%py_requires zope.deferredimport z3c.relationfield z3c.form

%description
plone.multilingualbehavior adds multilingual behavior to content types
built with Dexterity. It uses the next generation multilingual engine
powered by five/Zope3 technologies, plone.multilingual.

The behavior provides the Dexterity-driven content with a marker
interface "ITranslatable", and makes available to that translation
enabled type all the translation UI components such as menus, views,
etc...

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR
%py_requires plone.app.testing plone.formwidget.contenttree
%py_requires plone.testing zope.configuration

%description tests
plone.multilingualbehavior adds multilingual behavior to content types
built with Dexterity. It uses the next generation multilingual engine
powered by five/Zope3 technologies, plone.multilingual.

The behavior provides the Dexterity-driven content with a marker
interface "ITranslatable", and makes available to that translation
enabled type all the translation UI components such as menus, views,
etc...

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

# There is a file in the package named .DS_Store or .DS_Store.gz, 
# the file name used by Mac OS X to store folder attributes.  
# Such files are generally useless in packages and were usually accidentally 
# included by copying complete directories from the source tarball.
find $RPM_BUILD_ROOT \( -name '*.DS_Store' -o -name '*.DS_Store.gz' \) -print -delete

%check
python setup.py test
nosetests

%files
%doc *.rst docs/*
%python_sitelibdir/plone/*
%python_sitelibdir/*.egg-info
%exclude %python_sitelibdir/plone/*/test*

%files tests
%python_sitelibdir/plone/*/test*

%changelog
* Sat Nov 22 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.2.2-alt2.dev0.git20140523
- Applied python-module-plone.multilingualbehavior-1.2.2-alt1.dev0.git20140523.diff

* Fri Nov 21 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.2.2-alt1.dev0.git20140523
- Initial build for Sisyphus

