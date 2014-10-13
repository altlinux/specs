%define oname plone.app.search

%def_disable check

Name: python-module-%oname
Version: 1.2.2
Release: alt1.dev0.git20141009
Summary: Search user interface for Plone CMS
License: GPL
Group: Development/Python
Url: https://pypi.python.org/pypi/plone.app.search/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/plone/plone.app.search.git
Source: %name-%version.tar

BuildPreReq: python-module-setuptools-tests python-module-Zope2-tests
BuildPreReq: python-module-selenium
BuildPreReq: python-module-plone.app.testing
#BuildPreReq: python-module-plone.app.contentlisting

%py_provides %oname
%py_requires plone.app
#py_requires plone.app.contentlisting

%description
plone.app.search combines search results listing with Advanced Search
form. This provides search results view for Plone CMS with possibilities
to filter, sort and apply advanced filters to the search results
without. When changing a search criteria on the search view, AJAX call
is delivering you the updated results instead of reloaded page that lets
you get to what you're searching for faster without much distraction
caused by page reloading. The package is part of Plone 4.1.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR
%py_requires plone.app.testing

%description tests
plone.app.search combines search results listing with Advanced Search
form. This provides search results view for Plone CMS with possibilities
to filter, sort and apply advanced filters to the search results
without. When changing a search criteria on the search view, AJAX call
is delivering you the updated results instead of reloaded page that lets
you get to what you're searching for faster without much distraction
caused by page reloading. The package is part of Plone 4.1.

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
%python_sitelibdir/plone/app/*
%python_sitelibdir/*.egg-info
%exclude %python_sitelibdir/plone/app/*/tests

%files tests
%python_sitelibdir/plone/app/*/tests

%changelog
* Mon Oct 13 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.2.2-alt1.dev0.git20141009
- Initial build for Sisyphus

