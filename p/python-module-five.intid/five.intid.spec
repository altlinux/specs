%define oname five.intid
Name: python-module-%oname
Version: 1.0.3
Release: alt1.git20121005
Summary: Zope2 support for zope.intid
License: ZPL
Group: Development/Python
Url: https://pypi.python.org/pypi/five.intid/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/plone/five.intid.git
Source: %name-%version.tar

BuildPreReq: python-module-setuptools-tests python-module-Zope2-tests
BuildPreReq: python-module-zope.intid python-module-docutils
BuildPreReq: python-module-zope.event
BuildPreReq: python-module-zope.lifecycleevent
BuildPreReq: python-module-zope.keyreference
BuildPreReq: python-module-zope.site
BuildPreReq: python-module-zope.location
BuildPreReq: python-module-five.localsitemanager

%py_provides %oname
Requires: python-module-Zope2
%py_requires five zope.intid zope.component zope.event zope.interface
%py_requires zope.lifecycleevent zope.keyreference zope.site
%py_requires zope.location five.localsitemanager

%description
This package makes it possible to use zope.intid (and consequentially
other packages that rely on it such as zope.keyreference) in a Zope2
environment.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR

%description tests
This package makes it possible to use zope.intid (and consequentially
other packages that rely on it such as zope.keyreference) in a Zope2
environment.

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
%python_sitelibdir/five/*
%python_sitelibdir/*.egg-info
%exclude %python_sitelibdir/five/*/tests.*

%files tests
%python_sitelibdir/five/*/tests.*

%changelog
* Tue Oct 14 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.3-alt1.git20121005
- Initial build for Sisyphus

