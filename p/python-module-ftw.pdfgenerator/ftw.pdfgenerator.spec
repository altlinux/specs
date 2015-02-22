%define mname ftw
%define oname %mname.pdfgenerator
Name: python-module-%oname
Version: 1.3.6
Release: alt1.dev0.git20150219
Summary: A library for generating PDF representations of Plone objects with LaTeX
License: GPLv2+
Group: Development/Python
Url: https://pypi.python.org/pypi/ftw.pdfgenerator/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/4teamwork/ftw.pdfgenerator.git
Source: %name-%version.tar

BuildPreReq: python-module-setuptools-tests python-module-Zope2-tests
BuildPreReq: python-module-mako python-module-BeautifulSoup
BuildPreReq: python-module-unittest2 python-module-mocker
BuildPreReq: python-module-plone.mocktestcase %_bindir/pdflatex
BuildPreReq: python-module-zope.annotation
BuildPreReq: python-module-zope.i18n
BuildPreReq: python-module-zope.i18nmessageid
BuildPreReq: python-module-Products.Archetypes
BuildPreReq: python-module-Products.CMFCore
BuildPreReq: python-module-ftw.testing
BuildPreReq: python-module-plone.testing
BuildPreReq: python-module-zope.annotation
BuildPreReq: python-module-zope.publisher

%py_provides %oname
Requires: python-module-Zope2 %_bindir/pdflatex
%py_requires %mname zope.annotation zope.component zope.i18n mako
%py_requires zope.i18nmessageid zope.interface Products.Archetypes
%py_requires Products.CMFCore

%description
ftw.pdfgenerator is meant to be used for generating PDFs from structured
data using predefined LaTeX views. It is not useful for converting full
HTML pages into LaTeX / PDFs, although it is able to convert small HTML
chunks into LaTeX.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR
%py_requires ftw.testing plone.testing zope.annotation zope.publisher

%description tests
ftw.pdfgenerator is meant to be used for generating PDFs from structured
data using predefined LaTeX views. It is not useful for converting full
HTML pages into LaTeX / PDFs, although it is able to convert small HTML
chunks into LaTeX.

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
* Sun Feb 22 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.3.6-alt1.dev0.git20150219
- Version 1.3.6.dev0

* Wed Dec 24 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.3.5-alt1.dev0.git20141107
- Initial build for Sisyphus

