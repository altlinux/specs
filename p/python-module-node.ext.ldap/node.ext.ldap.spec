%define mname node.ext
%define oname %mname.ldap
Name: python-module-%oname
Version: 0.9.7
Release: alt1.git20140618
Summary: Node based LDAP support
License: BSD
Group: Development/Python
Url: https://pypi.python.org/pypi/node.ext.ldap/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/bluedynamics/node.ext.ldap.git
Source: %name-%version.tar

BuildPreReq: python-module-setuptools-tests python-module-node-tests
BuildPreReq: python-module-ldap python-module-smbpasswd
BuildPreReq: python-module-argparse
BuildPreReq: python-module-bda.cache
BuildPreReq: python-module-node.ext.ugm
BuildPreReq: python-module-interlude
BuildPreReq: python-module-plone.testing
BuildPreReq: python-module-unittest2
BuildPreReq: python-module-zope.configuration
BuildPreReq: python-module-zope.testing
BuildPreReq: python-module-nose

%py_provides %oname
%py_requires %mname bda.cache

%description
node.ext.ldap is a LDAP convenience library for LDAP communication based
on python-ldap (version 2.4 or later) and node.

The package contains base configuration and communication objects, a
LDAP node object and a LDAP node based user and group management
implementation utilizing node.ext.ugm.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR
%py_requires plone.testing zope.configuration zope.testing

%description tests
node.ext.ldap is a LDAP convenience library for LDAP communication based
on python-ldap (version 2.4 or later) and node.

The package contains base configuration and communication objects, a
LDAP node object and a LDAP node based user and group management
implementation utilizing node.ext.ugm.

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
nosetests

%files
%doc *.rst *.org
%python_sitelibdir/node/ext/*
%python_sitelibdir/*.egg-info
%exclude %python_sitelibdir/node/ext/*/test*

%files tests
%_bindir/*
%python_sitelibdir/node/ext/*/test*

%changelog
* Sat Oct 25 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.9.7-alt1.git20140618
- Initial build for Sisyphus

