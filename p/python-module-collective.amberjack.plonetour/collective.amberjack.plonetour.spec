%define mname collective.amberjack
%define oname %mname.plonetour
Name: python-module-%oname
Version: 1.1
Release: alt1.git20131218
Summary: Plone first install tour
License: GPL
Group: Development/Python
Url: https://pypi.python.org/pypi/collective.amberjack.plonetour/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/collective/collective.amberjack.plonetour.git
Source: %name-%version.tar

BuildPreReq: python-module-setuptools-tests python-module-Zope2-tests
BuildPreReq: python-module-collective.amberjack.core
BuildPreReq: python-module-unittest2

%py_provides %oname
%py_requires %mname.core

%description
This package provides plone tours for collective.amberjack package.

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
%python_sitelibdir/collective/amberjack/*
%python_sitelibdir/*.egg-info

%changelog
* Sat Oct 25 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1-alt1.git20131218
- Initial build for Sisyphus

