%define oname Products.SiteErrorLog
Name: python-module-%oname
Version: 2.13.3
Release: alt1.dev0.git20141106
Summary: Error log for Zope 2
License: ZPLv2.1
Group: Development/Python
Url: https://pypi.python.org/pypi/Products.SiteErrorLog/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/zopefoundation/Products.SiteErrorLog.git
Source: %name-%version.tar

BuildPreReq: python-module-setuptools-tests python-module-Zope2-tests
BuildPreReq: python-module-zope.event

%py_provides %oname
Requires: python-module-Zope2
%py_requires zope.event zope.interface

%description
SiteErrorLog records errors/exceptions happening anywhere in your Zope.
SiteErrorLog recorded errors are not persistent.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR
Requires: python-module-Zope2-tests
%py_requires zope.component

%description tests
SiteErrorLog records errors/exceptions happening anywhere in your Zope.
SiteErrorLog recorded errors are not persistent.

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
%doc *.txt
%python_sitelibdir/Products/*
%python_sitelibdir/*.egg-info
%exclude %python_sitelibdir/Products/*/tests

%files tests
%python_sitelibdir/Products/*/tests

%changelog
* Fri Nov 07 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.13.3-alt1.dev0.git20141106
- Initial build for Sisyphus

