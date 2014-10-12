%define oname plone.intelligenttext
Name: python-module-%oname
Version: 2.0.3
Release: alt1.dev0.git20140826
Summary: Provides transforms from text/x-web-intelligent to text/html and vice versa
License: GPLv2
Group: Development/Python
Url: https://pypi.python.org/pypi/plone.intelligenttext/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/plone/plone.intelligenttext.git
Source: %name-%version.tar

BuildPreReq: python-module-setuptools-tests python-module-Zope2-tests

%py_provides %oname
%py_requires plone

%description
Provides transforms from text/x-web-intelligent to text/html and vice
versa.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR

%description tests
Provides transforms from text/x-web-intelligent to text/html and vice
versa.

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
%python_sitelibdir/plone/*
%python_sitelibdir/*.egg-info
%exclude %python_sitelibdir/plone/*/tests.*

%files tests
%python_sitelibdir/plone/*/tests.*

%changelog
* Sun Oct 12 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.0.3-alt1.dev0.git20140826
- Initial build for Sisyphus

