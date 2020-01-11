%define _unpackaged_files_terminate_build 1
%define mname bda
%define oname %mname.cache

%def_with check

Name: python3-module-%oname
Version: 1.3.0
Release: alt1
Summary: Simple caching infrastructure
License: GPL
Group: Development/Python3
Url: https://pypi.python.org/pypi/bda.cache/
#Git: https://github.com/bluedynamics/bda.cache.git

Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3

%if_with check
BuildRequires: python3-module-interlude
BuildRequires: python3-module-pytest
BuildRequires: python3-module-zope.component
BuildRequires: python3-module-zope.testing
%endif

%py3_provides %oname
Requires: python3-module-%mname = %EVR
Requires: python3-module-memcached
%py3_requires zope.component

%description
This package is designed to be used by applications which require
different kinds of caching flavour. This is abstracted due to the
interfaces ICacheProvider and ICacheManager. ICacheProvider takes care
of the concrete cache implementation, ICacheManager is the read/write
interface.

%package tests
Summary: Tests for %oname
Group: Development/Python3
Requires: %name = %EVR
%py3_requires zope.testing

%description tests
This package is designed to be used by applications which require
different kinds of caching flavour. This is abstracted due to the
interfaces ICacheProvider and ICacheManager. ICacheProvider takes care
of the concrete cache implementation, ICacheManager is the read/write
interface.

This package contains tests for %oname.

%package -n python3-module-%mname
Summary: Core files of %mname
Group: Development/Python3

%description -n python3-module-%mname
Core files of %mname.

%prep
%setup

%build
%python3_build_debug

%install
%python3_install

%if "%_libexecdir" != "%_libdir"
mv %buildroot%_libexecdir %buildroot%_libdir
%endif

install -p -m644 src/bda/__init__.py \
	%buildroot%python3_sitelibdir/bda/

%check
python3 setup.py test

%files
%doc *.txt
%python3_sitelibdir/%mname/*
%python3_sitelibdir/*.egg-info
%exclude %python3_sitelibdir/%mname/*/tests
%exclude %python3_sitelibdir/%mname/__init__.py*
%exclude %python3_sitelibdir/*-nspkg.pth

%files tests
%python3_sitelibdir/%mname/*/tests

%files -n python3-module-%mname
%dir %python3_sitelibdir/%mname
%python3_sitelibdir/%mname/__init__.py*

%changelog
* Sat Jan 11 2020 Nikolai Kostrigin <nickel@altlinux.org> 1.3.0-alt1
- NMU: 1.1.3 -> 1.3.0
- Remove python2 module build
- Rearrange unittests execution
- Add memcached to R:

* Tue May 24 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.1.3-alt2.git20091201.1
- (AUTO) subst_x86_64.

* Fri Feb 05 2016 Sergey Alembekov <rt@altlinux.ru> 1.1.3-alt2.git20091201
- disabled tests
- cleanup buildreq

* Sat Oct 25 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1.3-alt1.git20091201
- Initial build for Sisyphus

