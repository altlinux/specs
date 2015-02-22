%define mname uwosh
%define oname %mname.snippets
Name: python-module-%oname
Version: 0.9.29
Release: alt1.git20150105
Summary: Adds dynamic rich-text snippets to Plone
License: GPLv2+
Group: Development/Python
Url: https://pypi.python.org/pypi/uwosh.snippets/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/collective/snippets.git
Source: %name-%version.tar

BuildPreReq: python-module-setuptools-tests python-module-Zope2-tests
BuildPreReq: python-module-plone.directives.form
BuildPreReq: python-module-plone.app.testing
BuildPreReq: python-module-Products.CMFCore
BuildPreReq: python-module-Products.CMFPlone
BuildPreReq: python-module-Products.statusmessages
BuildPreReq: python-module-plone.transformchain
BuildPreReq: python-module-plone.registry
BuildPreReq: python-module-plone.autoform
BuildPreReq: python-module-plone.app.z3cform
BuildPreReq: python-module-zope.schema
BuildPreReq: python-module-zope.i18nmessageid
BuildPreReq: python-module-z3c.form
BuildPreReq: python-module-zope.configuration

%py_provides %oname
Requires: python-module-Zope2
%py_requires %mname plone.directives.form Products.CMFCore zope.schema
%py_requires Products.CMFPlone Products.statusmessages plone.registry
%py_requires plone.transformchain plone.autoform plone.app.z3cform
%py_requires zope.i18nmessageid zope.component zope.interface z3c.form

%description
The uwosh.snippets package allows the user to include dynamically
updated rich-text snippets into a Plone page. The snippets can be used
anywhere that rich-text can be used. They can be inserted into a page
much like a picture or hyperlink.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR
%py_requires plone.app.testing zope.configuration

%description tests
The uwosh.snippets package allows the user to include dynamically
updated rich-text snippets into a Plone page. The snippets can be used
anywhere that rich-text can be used. They can be inserted into a page
much like a picture or hyperlink.

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
%doc *.txt *.rst docs/*
%python_sitelibdir/%mname/*
%python_sitelibdir/*.egg-info
%exclude %python_sitelibdir/%mname/*/test*

%files tests
%python_sitelibdir/%mname/*/test*

%changelog
* Sun Feb 22 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.9.29-alt1.git20150105
- Initial build for Sisyphus

