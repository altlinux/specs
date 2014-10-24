%define mname collective.dms
%define oname %mname.basecontent
Name: python-module-%oname
Version: 0.4
Release: alt1.dev0.git20141024
Summary: Base content types for document management system
License: GPL
Group: Development/Python
Url: https://pypi.python.org/pypi/collective.dms.basecontent/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/collective/collective.dms.basecontent.git
Source: %name-%version.tar

BuildPreReq: python-module-setuptools-tests python-module-Zope2-tests
BuildPreReq: python-module-five.grok
BuildPreReq: python-module-collective.documentviewer
BuildPreReq: python-module-plone.api
BuildPreReq: python-module-plone.app.dexterity
BuildPreReq: python-module-plone.namedfile
BuildPreReq: python-module-z3c.blobfile
BuildPreReq: python-module-plone.app.contenttypes
BuildPreReq: python-module-plone.app.relationfield
BuildPreReq: python-module-plone.formwidget.contenttree
BuildPreReq: python-module-plone.principalsource
BuildPreReq: python-module-collective.z3cform.chosen
BuildPreReq: python-module-collective.z3cform.rolefield
BuildPreReq: python-module-z3c.table
BuildPreReq: python-module-plone.app.testing
BuildPreReq: python-module-ecreall.helpers.testing
BuildPreReq: python-module-plone.app.vocabularies
BuildPreReq: python-module-openid
BuildPreReq: python-module-grokcore.component-tests
BuildPreReq: python-module-grokcore.annotation-tests
BuildPreReq: python-module-grokcore.security-tests
BuildPreReq: python-module-grokcore.site-tests
BuildPreReq: python-module-grokcore.view-tests
BuildPreReq: python-module-grokcore.viewlet-tests

%py_provides %oname
Requires: python-module-%mname = %EVR
%py_requires five.grok collective.documentviewer plone.api z3c.table
%py_requires plone.app.dexterity plone.namedfile z3c.blobfile
%py_requires plone.app.contenttypes plone.app.relationfield
%py_requires plone.formwidget.contenttree plone.principalsource
%py_requires collective.z3cform.chosen collective.z3cform.rolefield

%description
Base content types for document management system.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR
%py_requires plone.app.testing ecreall.helpers.testing
%py_requires plone.app.vocabularies grokcore.component.testing
%py_requires grokcore.annotation.testing grokcore.security.testing
%py_requires grokcore.site.testing grokcore.view.testing
%py_requires grokcore.viewlet.testing

%description tests
Base content types for document management system.

This package contains tests for %oname.

%package -n python-module-%mname
Summary: Core files of %mname
Group: Development/Python
%py_requires collective

%description -n python-module-%mname
Core files of %mname.

%prep
%setup

%build
%python_build_debug

%install
%python_install

%ifarch x86_64
mv %buildroot%_libexecdir %buildroot%_libdir
%endif

install -p -m644 src/collective/dms/__init__.py \
	%buildroot%python_sitelibdir/collective/dms/

%check
python setup.py test

%files
%doc *.rst docs/*
%python_sitelibdir/collective/dms/*
%python_sitelibdir/*.egg-info
%exclude %python_sitelibdir/collective/dms/*/test*
%exclude %python_sitelibdir/collective/dms/__init__.py*

%files tests
%python_sitelibdir/collective/dms/*/test*

%files -n python-module-%mname
%dir %python_sitelibdir/collective/dms
%python_sitelibdir/collective/dms/__init__.py*

%changelog
* Fri Oct 24 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.4-alt1.dev0.git20141024
- Initial build for Sisyphus

