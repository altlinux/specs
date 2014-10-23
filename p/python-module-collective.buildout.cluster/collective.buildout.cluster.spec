%define mname collective.buildout
%define oname %mname.cluster

%def_disable check

Name: python-module-%oname
Version: 0.7
Release: alt1.dev.svn20100731
Summary: Introspect and manage a buildout-based cluster configuration
License: LGPL
Group: Development/Python
Url: https://pypi.python.org/pypi/collective.buildout.cluster/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# http://svn.plone.org/svn/collective/buildout/collective.buildout.cluster/trunk/
Source: %name-%version.tar

BuildPreReq: python-module-setuptools-tests python-module-Zope2-tests
BuildPreReq: python-module-zc.buildout-tests
BuildPreReq: python-module-iniparse
BuildPreReq: python-module-zope.testing
BuildPreReq: python-module-manuel-tests

%py_provides %oname
Requires: python-module-%mname = %EVR
%py_requires zc.buildout

%description
A package to introspect and manage a buildout-based cluster
configuration in an object-oriented way.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR
%py_requires zc.buildout.testing zope.testing manuel.testing

%description tests
A package to introspect and manage a buildout-based cluster
configuration in an object-oriented way.

This package contains tests for %oname.

%package -n python-module-%mname
Summary: Core files of %mname
Group: Development/Python
%py_requires collective

%description -n python-module-%mname
Core files of %mname.

%prep
%setup

%build
%python_build_debug

%install
%python_install

%ifarch x86_64
mv %buildroot%_libexecdir %buildroot%_libdir
%endif

install -p -m644 collective/buildout/__init__.py \
	%buildroot%python_sitelibdir/collective/buildout/

%check
python setup.py test

%files
%doc *.txt
%_bindir/*
%python_sitelibdir/collective/buildout/*
%python_sitelibdir/*.egg-info
%exclude %python_sitelibdir/collective/buildout/*/tests
%exclude %python_sitelibdir/collective/buildout/__init__.py*

%files tests
%python_sitelibdir/collective/buildout/*/tests

%files -n python-module-%mname
%dir %python_sitelibdir/collective/buildout
%python_sitelibdir/collective/buildout/__init__.py*

%changelog
* Thu Oct 23 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.7-alt1.dev.svn20100731
- Initial build for Sisyphus

