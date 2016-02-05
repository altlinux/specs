%def_disable check

%define mname bda
%define oname %mname.cache
Name: python-module-%oname
Version: 1.1.3
Release: alt2.git20091201
Summary: Simple caching infrastructure
License: GPL
Group: Development/Python
Url: https://pypi.python.org/pypi/bda.cache/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/bluedynamics/bda.cache.git
Source: %name-%version.tar

BuildRequires: python-module-interlude python-module-pytest python-module-zope.component python-module-zope.testing
#BuildPreReq: python-module-setuptools-tests
#BuildPreReq: python-module-memcached
#BuildPreReq: python-module-zope.component
#BuildPreReq: python-module-interlude
#BuildPreReq: python-module-zope.testing

%py_provides %oname
Requires: python-module-%mname = %EVR
#%py_requires zope.component

%description
This package is designed to be used by applications which require
different kinds of caching flavour. This is abstracted due to the
interfaces ICacheProvider and ICacheManager. ICacheProvider takes care
of the concrete cache implementation, ICacheManager is the read/write
interface.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR
#%py_requires zope.testing

%description tests
This package is designed to be used by applications which require
different kinds of caching flavour. This is abstracted due to the
interfaces ICacheProvider and ICacheManager. ICacheProvider takes care
of the concrete cache implementation, ICacheManager is the read/write
interface.

This package contains tests for %oname.

%package -n python-module-%mname
Summary: Core files of %mname
Group: Development/Python

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

install -p -m644 src/bda/__init__.py \
	%buildroot%python_sitelibdir/bda/

%check
python setup.py test
rm -fR build
py.test

%files
%doc *.txt
%python_sitelibdir/%mname/*
%python_sitelibdir/*.egg-info
%exclude %python_sitelibdir/%mname/*/tests
%exclude %python_sitelibdir/%mname/__init__.py*

%files tests
%python_sitelibdir/%mname/*/tests

%files -n python-module-%mname
%dir %python_sitelibdir/%mname
%python_sitelibdir/%mname/__init__.py*

%changelog

* Fri Feb 05 2016 Sergey Alembekov <rt@altlinux.ru> 1.1.3-alt2.git20091201
- disabled tests
- cleanup buildreq

* Sat Oct 25 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1.3-alt1.git20091201
- Initial build for Sisyphus

