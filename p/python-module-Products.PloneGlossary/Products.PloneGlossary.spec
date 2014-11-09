%define oname Products.PloneGlossary
Name: python-module-%oname
Version: 1.7.2
Release: alt1.dev0.git20141107
Summary: Highlight Plone content terms, mouseover shows the term definition as tooltip
License: GPL
Group: Development/Python
Url: https://pypi.python.org/pypi/Products.PloneGlossary/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/collective/Products.PloneGlossary.git
Source: %name-%version.tar

BuildPreReq: python-module-setuptools-tests python-module-Zope2-tests
BuildPreReq: python-module-wicked
BuildPreReq: python-module-Products.PloneTestCase
BuildPreReq: python-module-Products.GenericSetup
BuildPreReq: python-module-Products.CMFCore
BuildPreReq: python-module-Products.ZCatalog
BuildPreReq: python-module-Products.ZCTextIndex
BuildPreReq: python-module-Products.LinguaPlone
BuildPreReq: python-module-Products.Archetypes
BuildPreReq: python-module-Products.ATContentTypes
BuildPreReq: python-module-Products.CMFPlone
BuildPreReq: python-module-plone.memoize
BuildPreReq: python-module-plone.i18n
BuildPreReq: python-module-plone.indexer
BuildPreReq: python-module-plone.app.portlets
BuildPreReq: python-module-plone.portlets
BuildPreReq: python-module-plone.app.upgrade
BuildPreReq: python-module-zope.app.component
BuildPreReq: python-module-zope.formlib
BuildPreReq: python-module-zope.i18nmessageid

%py_provides %oname
Requires: python-module-Zope2
%py_requires Products.GenericSetup Products.CMFCore Products.ZCatalog
%py_requires Products.ZCTextIndex Products.LinguaPlone Products.CMFPlone
%py_requires Products.Archetypes Products.ATContentTypes plone.memoize
%py_requires plone.i18n plone.indexer plone.app.portlets plone.portlets
%py_requires plone.app.upgrade zope.interface zope.component
%py_requires zope.app.component zope.formlib zope.i18nmessageid

%description
PloneGlossary is a Plone content type that allows you to manage your own
glossaries, propose definitions and search in one or more glossaries.
Any word defined is instantly highlighted in the content of your site.

After adding a glossary, you can add your definitions to it. Definitions
are a simple content type. Enter the word you want to define as the
title, and the definition of the word in the text body. You can also
specify variants of the word. For example if you define the word
yoghurt, you may also want to allow the variants yogurt or yoghourt to
be valid. Definitions will be highlighted (like an acronym) when they
appear elsewhere in your site. (Also see the ploneglossary configlet.)

Once you have a large number of definitions in your glossary, you can
browse the glossary by the means of an alphabetic index, or perform a
search in the glossary. Each glossary has an integrated search engine,
which is simply a ZCatalog.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR
%py_requires Products.PloneTestCase

%description tests
PloneGlossary is a Plone content type that allows you to manage your own
glossaries, propose definitions and search in one or more glossaries.
Any word defined is instantly highlighted in the content of your site.

After adding a glossary, you can add your definitions to it. Definitions
are a simple content type. Enter the word you want to define as the
title, and the definition of the word in the text body. You can also
specify variants of the word. For example if you define the word
yoghurt, you may also want to allow the variants yogurt or yoghourt to
be valid. Definitions will be highlighted (like an acronym) when they
appear elsewhere in your site. (Also see the ploneglossary configlet.)

Once you have a large number of definitions in your glossary, you can
browse the glossary by the means of an alphabetic index, or perform a
search in the glossary. Each glossary has an integrated search engine,
which is simply a ZCatalog.

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
%doc *.txt *.rst
%python_sitelibdir/Products/*
%python_sitelibdir/*.egg-info
%exclude %python_sitelibdir/Products/*/tests

%files tests
%python_sitelibdir/Products/*/tests

%changelog
* Sun Nov 09 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.7.2-alt1.dev0.git20141107
- Initial build for Sisyphus

