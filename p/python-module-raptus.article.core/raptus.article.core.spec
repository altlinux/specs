%define mname raptus.article
%define oname %mname.core
Name: python-module-%oname
Version: 2.2
Release: alt1.dev0.git20141023
Summary: Provides a configurable article content type
License: GPL
Group: Development/Python
Url: https://pypi.python.org/pypi/raptus.article.core/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/Raptus/raptus.article.core.git
Source: %name-%version.tar

BuildPreReq: python-module-setuptools-tests python-module-Zope2-tests
BuildPreReq: python-module-Products.Archetypes
BuildPreReq: python-module-Products.CMFPlone
BuildPreReq: python-module-Products.CMFCore
BuildPreReq: python-module-Products.statusmessages
BuildPreReq: python-module-Products.ATContentTypes
BuildPreReq: python-module-Products.LinguaPlone
BuildPreReq: python-module-plone.app.layout
BuildPreReq: python-module-plone.app.viewletmanager
BuildPreReq: python-module-plone.app.contentmenu
BuildPreReq: python-module-plone.memoize
BuildPreReq: python-module-plone.i18n
BuildPreReq: python-module-plone.app.content
BuildPreReq: python-module-plone.app.upgrade
BuildPreReq: python-module-zope.publisher
BuildPreReq: python-module-zope.viewlet
BuildPreReq: python-module-zope.schema
BuildPreReq: python-module-zope.security
BuildPreReq: python-module-zope.configuration
BuildPreReq: python-module-zope.i18n
BuildPreReq: python-module-zope.event
BuildPreReq: python-module-zope.i18nmessageid

%py_provides %oname
Requires: python-module-%mname = %EVR
Requires: python-module-Zope2
%py_requires Products.Archetypes Products.CMFPlone Products.CMFCore
%py_requires Products.statusmessages plone.i18n
%py_requires Products.ATContentTypes Products.LinguaPlone plone.memoize
%py_requires plone.app.layout plone.app.viewletmanager plone.app.content
%py_requires plone.app.contentmenu plone.app.upgrade zope.publisher
%py_requires zope.viewlet zope.interface zope.component zope.schema
%py_requires zope.security zope.configuration zope.i18n zope.event
%py_requires zope.i18nmessageid

%description
This package provides a configurable article content type, which
replaces the default Page content type.

%package -n python-module-%mname
Summary: Core files of %mname
Group: Development/Python
%py_provides %mname
Requires: python-module-raptus = %EVR

%description -n python-module-%mname
Core files of %mname.

%package -n python-module-raptus
Summary: Core files of raptus
Group: Development/Python
%py_provides raptus

%description -n python-module-raptus
Core files of raptus.

%prep
%setup

%build
%python_build_debug

%install
%python_install

%ifarch x86_64
mv %buildroot%_libexecdir %buildroot%_libdir
%endif

install -p -m644 raptus/__init__.py \
	%buildroot%python_sitelibdir/raptus/
install -p -m644 raptus/article/__init__.py \
	%buildroot%python_sitelibdir/raptus/article/

%check
python setup.py test

%files
%doc *.rst docs/*
%python_sitelibdir/raptus/article/*
%python_sitelibdir/*.egg-info
%exclude %python_sitelibdir/raptus/article/__init__.py*

%files -n python-module-%mname
%dir %python_sitelibdir/raptus/article
%python_sitelibdir/raptus/article/__init__.py*

%files -n python-module-raptus
%dir %python_sitelibdir/raptus
%python_sitelibdir/raptus/__init__.py*

%changelog
* Mon Nov 24 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.2-alt1.dev0.git20141023
- Initial build for Sisyphus

