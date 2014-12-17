%define mname eea
%define oname %mname.converter
Name: python-module-%oname
Version: 8.5
Release: alt1
Summary: SVG, PNG, PDF converters using external tools as ImageMagick
License: GPLv2+
Group: Development/Python
Url: https://pypi.python.org/pypi/eea.converter/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: ImageMagick-tools wkhtmltopdf pdftk python-module-Pillow
BuildPreReq: python-module-setuptools-tests python-module-Zope2-tests
BuildPreReq: python-module-Products.statusmessages
BuildPreReq: python-module-plone.app.testing
BuildPreReq: python-module-zope.publisher
BuildPreReq: python-module-zope.i18nmessageid

%py_provides %oname
Requires: ImageMagick-tools wkhtmltopdf pdftk
Requires: python-module-Zope2
%py_requires %mname PIL Products.statusmessages zope.interface
%py_requires zope.component zope.publisher zope.i18nmessageid

%description
This package provides utilities to convert images and PDF files using
ImageMagick. It also provides a generic /download.pdf browser view that
allow your users to download Plone pages as PDF files with custom PDF
cover, disclaimer and back cover.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR
%py_requires plone.app.testing

%description tests
This package provides utilities to convert images and PDF files using
ImageMagick. It also provides a generic /download.pdf browser view that
allow your users to download Plone pages as PDF files with custom PDF
cover, disclaimer and back cover.

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
%doc *.md *.rst docs/*
%python_sitelibdir/%mname/*
%python_sitelibdir/*.egg-info
%exclude %python_sitelibdir/%mname/*/tests

%files tests
%python_sitelibdir/%mname/*/tests

%changelog
* Wed Dec 17 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 8.5-alt1
- Initial build for Sisyphus

