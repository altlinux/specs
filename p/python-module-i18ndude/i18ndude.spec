%define oname i18ndude
Name: python-module-%oname
Version: 3.4.1
Release: alt1.dev0.git20141127
Summary: i18ndude performs various tasks related to ZPT's, Python Scripts and i18n
License: GPL
Group: Development/Python
Url: https://pypi.python.org/pypi/i18ndude/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/collective/i18ndude.git
Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-module-setuptools-tests
BuildPreReq: python-module-zest.releaser
BuildPreReq: python-module-zope.tal
BuildPreReq: python-module-zope.interface
BuildPreReq: python-module-zope.i18nmessageid
BuildPreReq: python-module-plone.i18n
BuildPreReq: python-module-ordereddict
BuildPreReq: python-module-unidecode

%py_provides %oname
%py_requires zest.releaser zope.tal zope.interface zope.i18nmessageid
%py_requires plone.i18n

%description
i18ndude performs various tasks related to ZPT's, Python Scripts and
i18n.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR

%description tests
i18ndude performs various tasks related to ZPT's, Python Scripts and
i18n.

This package contains tests for %oname.

%prep
%setup

%build
%python_build_debug

%install
%python_install

%check
python setup.py test

%files
%doc *.rst docs/*
%_bindir/*
%python_sitelibdir/*
%exclude %python_sitelibdir/*/tests

%files tests
%python_sitelibdir/*/tests

%changelog
* Fri Nov 28 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.4.1-alt1.dev0.git20141127
- Version 3.4.1.dev0

* Fri Oct 24 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.3.6-alt1.dev0.git20140805
- Initial build for Sisyphus

