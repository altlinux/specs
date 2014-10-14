%define oname plone.app.redirector
Name: python-module-%oname
Version: 1.2.2
Release: alt1.dev0.git20140730
Summary: Redirects to moved content after accessing old URLs
License: GPLv2
Group: Development/Python
Url: https://pypi.python.org/pypi/plone.app.redirector/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/plone/plone.app.redirector.git
Source: %name-%version.tar

BuildPreReq: python-module-setuptools-tests python-module-Zope2-tests
BuildPreReq: python-module-plone.memoize
BuildPreReq: python-module-plone.app.testing
#BuildPreReq: python-module-plone.app.contenttypes

%py_provides %oname
%py_requires plone.app plone.memoize

%description
Bring dead links back to life! plone.app.redirector knows where your
content used to be and can bring you to its new location when content
moves.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR
%py_requires plone.app.testing
#py_requires plone.app.contenttypes

%description tests
Bring dead links back to life! plone.app.redirector knows where your
content used to be and can bring you to its new location when content
moves.

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
%exclude %python_sitelibdir/plone/app/*/test*

%files tests
%python_sitelibdir/plone/app/*/test*

%changelog
* Tue Oct 14 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.2.2-alt1.dev0.git20140730
- Initial build for Sisyphus

