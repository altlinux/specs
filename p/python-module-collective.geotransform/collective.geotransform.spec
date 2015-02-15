%define mname collective
%define oname %mname.geotransform
Name: python-module-%oname
Version: 1.0.2
Release: alt1.dev0.git20150203
Summary: Gracefully email obfuscation for Plone
License: GPLv2+
Group: Development/Python
Url: https://pypi.python.org/pypi/collective.geotransform/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/collective/collective.geotransform.git
Source: %name-%version.tar

BuildPreReq: python-module-setuptools-tests
BuildPreReq: python-module-BeautifulSoup4 python-module-openid
BuildPreReq: python-module-plone.api
BuildPreReq: python-module-plone.transformchain
BuildPreReq: python-module-plone.app.testing
BuildPreReq: python-module-plone.app.robotframework-tests
BuildPreReq: python-module-Products.CMFCore
BuildPreReq: python-module-zope.component
BuildPreReq: python-module-zope.interface

%py_provides %oname
%py_requires %mname plone.api plone.transformchain bs4 Products.CMFCore
%py_requires zope.component zope.interface

%description
GEO stands for "Gracefully E-mail Obfuscation". This package implements
the solution exposed in this post of List Apart web site authored by
Roel Van Gils:

http://www.alistapart.com/articles/gracefulemailobfuscation/

collective.geotransform uses plone.transformchain to transform the
response output from Zope before it reaches your browser. It searches
for all "mailto:" occurences inside the response and transform them into
encoded harmless links. It also searches for plain email addresses
(without links) inside the response and transform them into encrypted
spans. This codification is done via a simple base64 encoding, but
enough to fool a spam robot.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR
%py_requires plone.app.testing plone.app.robotframework.testing

%description tests
GEO stands for "Gracefully E-mail Obfuscation". This package implements
the solution exposed in this post of List Apart web site authored by
Roel Van Gils:

http://www.alistapart.com/articles/gracefulemailobfuscation/

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
%doc *.txt docs/*
%python_sitelibdir/%mname/*
%python_sitelibdir/*.egg-info
%exclude %python_sitelibdir/%mname/*/test*

%files tests
%python_sitelibdir/%mname/*/test*

%changelog
* Sun Feb 15 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.2-alt1.dev0.git20150203
- Initial build for Sisyphus

