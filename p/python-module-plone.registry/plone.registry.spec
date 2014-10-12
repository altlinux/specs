%define oname plone.registry
Name: python-module-%oname
Version: 1.0.3
Release: alt1.dev0.git20140911
Summary: A debconf-like (or about:config-like) registry for storing application settings
License: GPL
Group: Development/Python
Url: https://pypi.python.org/pypi/plone.registry/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/plone/plone.registry.git
Source: %name-%version.tar

BuildPreReq: python-module-setuptools-tests python-module-Zope2-tests
BuildPreReq: python-module-zope.schema
BuildPreReq: python-module-zope.dottedname
BuildPreReq: python-module-zope.event
BuildPreReq: python-module-zope.testing

%py_provides %oname
%py_requires plone ZODB3 zope.schema zope.interface zope.component
%py_requires zope.dottedname zope.event

%description
This package provides debconf-like (or about:config-like) settings
registries for Zope applications. A ``registry``, with a dict-like API,
is used to get and set values stored in ``records``. Each record
contains the actual value, as well as a ``field`` that describes the
record in more detail. At a minimum, the field contains information
about the type of value allowed, as well as a short title describing the
record's purpose.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR
%py_requires zope.testing

%description tests
This package provides debconf-like (or about:config-like) settings
registries for Zope applications. A ``registry``, with a dict-like API,
is used to get and set values stored in ``records``. Each record
contains the actual value, as well as a ``field`` that describes the
record in more detail. At a minimum, the field contains information
about the type of value allowed, as well as a short title describing the
record's purpose.

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
* Sun Oct 12 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.3-alt1.dev0.git20140911
- Initial build for Sisyphus

