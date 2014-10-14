%define oname plone.app.dexterity

%def_disable check

Name: python-module-%oname
Version: 2.1.2
Release: alt1.dev0.git20141009
Summary: Dexterity is a content type system for Plone
License: GPL
Group: Development/Python
Url: https://pypi.python.org/pypi/plone.app.dexterity/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/plone/plone.app.dexterity.git
Source: %name-%version.tar

BuildPreReq: python-module-setuptools-tests python-module-Zope2-tests
BuildPReReq: python-module-sphinx-devel
BuildPreReq: python-module-lxml python-module-unittest2
BuildPreReq: python-module-plone.app.textfield
BuildPreReq: python-module-plone.behavior
BuildPreReq: python-module-plone.dexterity
BuildPreReq: python-module-plone.formwidget.namedfile
BuildPreReq: python-module-plone.namedfile
BuildPreReq: python-module-plone.rfc822
BuildPreReq: python-module-plone.schemaeditor
BuildPreReq: python-module-plone.app.content
BuildPreReq: python-module-plone.app.layout
BuildPreReq: python-module-plone.app.uuid
BuildPreReq: python-module-plone.app.z3cform
BuildPreReq: python-module-plone.autoform
BuildPreReq: python-module-plone.contentrules
BuildPreReq: python-module-plone.portlets
BuildPreReq: python-module-plone.supermodel
BuildPreReq: python-module-plone.z3cform
BuildPreReq: python-module-Products.CMFCore
BuildPreReq: python-module-Products.GenericSetup
BuildPreReq: python-module-zope.browserpage
BuildPreReq: python-module-zope.schema
BuildPreReq: python-module-zope.publisher
BuildPreReq: python-module-z3c.form
BuildPreReq: python-module-plone.app.robotframework
BuildPreReq: python-module-plone.app.testing
BuildPreReq: python-module-five.grok
BuildPreReq: python-module-plone.directives.dexterity
BuildPreReq: python-module-plone.directives.form
BuildPreReq: python-module-plone.app.relationfield
BuildPreReq: python-module-plone.app.intid
BuildPreReq: python-module-z3c.relationfield
#BuildPreReq: python-module-Products.CMFPlone

%py_provides %oname
Requires: python-module-Zope2
%py_requires plone.app.intid z3c.relationfield
%py_requires plone.directives.dexterity plone.app.relationfield
%py_requires zope.publisher z3c.form five.grok plone.directives.form
%py_requires zope.browserpage zope.interface zope.component zope.schema
%py_requires plone.z3cform Products.CMFCore Products.GenericSetup
%py_requires plone.contentrules plone.portlets plone.supermodel
%py_requires plone.app.uuid plone.app.z3cform plone.autoform
%py_requires plone.schemaeditor plone.app.content plone.app.layout
%py_requires plone.dexterity plone.formwidget.namedfile plone.namedfile
%py_requires plone.app plone.app.textfield plone.behavior plone.rfc822
#py_requires Products.CMFPlone

%description
Dexterity is a content type framework for CMF applications, with
particular emphasis on Plone. It can be viewed as an alternative to
Archetypes that is more light-weight and modular.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR
%py_requires plone.app.robotframework plone.app.testing

%description tests
Dexterity is a content type framework for CMF applications, with
particular emphasis on Plone. It can be viewed as an alternative to
Archetypes that is more light-weight and modular.

This package contains tests for %oname.

%package pickles
Summary: Pickles for %oname
Group: Development/Python

%description pickles
Dexterity is a content type framework for CMF applications, with
particular emphasis on Plone. It can be viewed as an alternative to
Archetypes that is more light-weight and modular.

This package contains pickles for %oname.

%package docs
Summary: Documentation for %oname
Group: Development/Documentation
BuildArch: noarch

%description docs
Dexterity is a content type framework for CMF applications, with
particular emphasis on Plone. It can be viewed as an alternative to
Archetypes that is more light-weight and modular.

This package contains documentation for %oname.

%prep
%setup

%prepare_sphinx .
ln -s ../objects.inv docs/

%build
%python_build_debug

%install
%python_install

%ifarch x86_64
mv %buildroot%_libexecdir %buildroot%_libdir
%endif

%make -C docs pickle
%make -C docs html

install -d %buildroot%python_sitelibdir/%oname
cp -fR docs/_build/pickle %buildroot%python_sitelibdir/%oname

%check
python setup.py test

%files
%doc *.txt *.rst
%python_sitelibdir/plone/app/*
%python_sitelibdir/*.egg-info
%exclude %python_sitelibdir/plone/app/*/test*
%dir %python_sitelibdir/%oname

%files pickles
%python_sitelibdir/%oname/pickle

%files docs
%doc docs/_build/html/*

%files tests
%python_sitelibdir/plone/app/*/test*

%changelog
* Tue Oct 14 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.1.2-alt1.dev0.git20141009
- Initial build for Sisyphus

