%define oname Products.PlacelessTranslationService
Name: python-module-%oname
Version: 2.0.6
Release: alt1.dev0.git20140416
Summary: provides a way of internationalizing and localizing software for Zope 2
License: GPL
Group: Development/Python
Url: https://pypi.python.org/pypi/Products.PlacelessTranslationService/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/plone/Products.PlacelessTranslationService.git
Source: %name-%version.tar

BuildPreReq: python-module-setuptools-tests python-module-Zope2-tests
BuildPreReq: python-module-docutils python-module-gettext
BuildPreReq: python-module-unittest2
BuildPreReq: python-module-zope.annotation
BuildPreReq: python-module-zope.deferredimport
BuildPreReq: python-module-zope.deprecation
BuildPreReq: python-module-zope.i18n
BuildPreReq: python-module-zope.publisher

%py_provides %oname
Requires: python-module-Zope2
%py_requires zope.annotation zope.component zope.deferredimport ZODB3
%py_requires zope.deprecation zope.i18n zope.interface zope.publisher

%description
PTS is a way of internationalizing (i18n'ing) and localizing (l10n'ing)
software for Zope 2. It's based on the files supported by the GNU
gettext set of utilities.

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
%doc *.txt docs/*
%python_sitelibdir/Products/*
%python_sitelibdir/*.egg-info

%changelog
* Wed Oct 15 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.0.6-alt1.dev0.git20140416
- Initial build for Sisyphus

