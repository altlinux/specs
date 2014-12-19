%define oname node
Name: python-module-%oname
Version: 0.9.16
Release: alt1.dev0.git20141217
Summary: Building data structures as node trees
License: BSD
Group: Development/Python
Url: https://pypi.python.org/pypi/node/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/bluedynamics/node.git
Source: %name-%version.tar

BuildPreReq: python-module-setuptools-tests python-module-Zope2-tests
BuildPreReq: python-module-odict-tests python-module-plumber-tests
BuildPreReq: python-module-zope.lifecycleevent
BuildPreReq: python-module-zope.deprecation
BuildPreReq: python-module-uuid
BuildPreReq: python-module-interlude
BuildPreReq: python-module-plone.testing
BuildPreReq: python-module-unittest2 python-module-nose

%py_provides %oname
%py_requires zope.lifecycleevent zope.deprecation zope.component

%description
Data structures could be described as trees. Some are by nature treeish,
like XML documents, LDAP directories or filesystem directory trees,
while others can be treated that way.

Furthermore, python has elegant ways for customizing all sorts of
datamodel related APIs. The dictionary container type fits almost
completely the purpose of representing a node of a tree. The same API is
also described in zope.interface.common.mapping.IFullMapping.
Additionaly a node must provide hierarchy information. In this case the
contract of zope.location.interfaces.ILocation is used.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR
%py_requires plone.testing odict.tests plumber.tests

%description tests
Data structures could be described as trees. Some are by nature treeish,
like XML documents, LDAP directories or filesystem directory trees,
while others can be treated that way.

Furthermore, python has elegant ways for customizing all sorts of
datamodel related APIs. The dictionary container type fits almost
completely the purpose of representing a node of a tree. The same API is
also described in zope.interface.common.mapping.IFullMapping.
Additionaly a node must provide hierarchy information. In this case the
contract of zope.location.interfaces.ILocation is used.

This package contains tests for %oname

%prep
%setup

%build
%python_build_debug

%install
%python_install

%ifarch x86_64
mv %buildroot%_libexecdir %buildroot%_libdir
%endif

install -p -m644 src/node/__init__.py \
	%buildroot%python_sitelibdir/node/

%check
python setup.py test
nosetests

%files
%doc *.rst
%python_sitelibdir/*
%exclude %python_sitelibdir/*/test*

%files tests
%python_sitelibdir/*/test*

%changelog
* Fri Dec 19 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.9.16-alt1.dev0.git20141217
- Version 0.9.16.dev0

* Sat Oct 25 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.9.15-alt1.dev0.git20140821
- Initial build for Sisyphus

