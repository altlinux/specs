%define mname ztfy
%define oname %mname.security
Name: python-module-%oname
Version: 0.4.2
Release: alt1
Summary: ZTFY package used to add wrapper around Zope security
License: ZPLv2.1
Group: Development/Python
Url: https://pypi.python.org/pypi/ztfy.security/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-module-setuptools-tests
BuildPreReq: python-module-fanstatic
BuildPreReq: python-module-z3c.form
BuildPreReq: python-module-z3c.formjs
BuildPreReq: python-module-z3c.jsonrpc
BuildPreReq: python-module-zope.annotation
BuildPreReq: python-module-zope.authentication
BuildPreReq: python-module-zope.component
BuildPreReq: python-module-zope.container
BuildPreReq: python-module-zope.interface
BuildPreReq: python-module-zope.lifecycleevent
BuildPreReq: python-module-zope.pluggableauth
BuildPreReq: python-module-zope.schema
BuildPreReq: python-module-zope.security
BuildPreReq: python-module-zope.securitypolicy
BuildPreReq: python-module-zope.tales
BuildPreReq: python-module-zope.traversing
BuildPreReq: python-module-ztfy.jqueryui
BuildPreReq: python-module-ztfy.skin
BuildPreReq: python-module-ztfy.utils
BuildPreReq: python-module-zope.testing
BuildPreReq: python-module-zope.testrunner

%py_provides %oname
%py_requires %mname fanstatic z3c.form z3c.formjs z3c.jsonrpc zope.tales
%py_requires zope.annotation zope.authentication zope.component
%py_requires zope.container zope.interface zope.lifecycleevent ztfy.skin
%py_requires zope.pluggableauth zope.schema zope.security ztfy.jqueryui
%py_requires zope.securitypolicy zope.traversing ztfy.utils

%description
ztfy.security is a thin wrapper around zope.security and
zope.securitypolicy packages.

It provides an adapter to ISecurityManager interfaces, which allows you
to get and set roles and permissions applied to a given principal on a
given adapted context.

This adapter also allows you to fire events when a role is granted or
revoked to a given principal ; this functionality can be useful, for
example, when you want to forbid removal of a 'contributor' role to a
principal when he already owns a set of contents.

Finally, ztfy.security provides a small set of schema fields, which can
be used when you want to define a field as a principal id or as a list
of principals ids.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR
%py_requires zope.testing zope.testrunner

%description tests
ztfy.security is a thin wrapper around zope.security and
zope.securitypolicy packages.

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
rm -fR build
py.test -vv

%files
%doc docs/*
%python_sitelibdir/%mname/*
%python_sitelibdir/*.egg-info
%exclude %python_sitelibdir/%mname/*/tests

%files tests
%python_sitelibdir/%mname/*/tests

%changelog
* Sun Feb 22 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.4.2-alt1
- Initial build for Sisyphus

