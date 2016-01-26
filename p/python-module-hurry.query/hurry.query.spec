%define mname hurry
%define oname %mname.query
%def_disable check

Name: python-module-%oname
Version: 1.1.2
Release: alt2.dev0.git20141106
Summary: Higher level query system for the zope.catalog
License: ZPLv2.1
Group: Development/Python
Url: https://pypi.python.org/pypi/hurry.query/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/zopefoundation/hurry.query.git
Source: %name-%version.tar

BuildRequires: python-module-pytest python-module-zc.catalog python-module-zope.testing

#BuildPreReq: python-module-setuptools-tests
#BuildPreReq: python-module-ZODB3
#BuildPreReq: python-module-zc.catalog
#BuildPreReq: python-module-zope.catalog
#BuildPreReq: python-module-zope.component
#BuildPreReq: python-module-zope.interface
#BuildPreReq: python-module-zope.intid
#BuildPreReq: python-module-zope.testing

%py_provides %oname
#%py_requires %mname zc.catalog ZODB3 zope.catalog zope.component
#%py_requires zope.interface zope.intid

%description
The hurry query system for the zope.catalog builds on its catalog
indexes, as well as the indexes in zc.catalog. It is in part inspired by
AdvancedQuery for Zope 2 by Dieter Maurer, though has an independent
origin.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR
#%py_requires zope.testing

%description tests
The hurry query system for the zope.catalog builds on its catalog
indexes, as well as the indexes in zc.catalog. It is in part inspired by
AdvancedQuery for Zope 2 by Dieter Maurer, though has an independent
origin.

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
py.test -vv src/hurry/query/tests.py

%files
%doc *.txt
%python_sitelibdir/%mname/*
%python_sitelibdir/*.egg-info
%exclude %python_sitelibdir/%mname/*/tests.*

%files tests
%python_sitelibdir/%mname/*/tests.*

%changelog
* Tue Jan 26 2016 Sergey Alembekov <rt@altlinux.ru> 1.1.2-alt2.dev0.git20141106
- Rebuild with "def_disable check"
- Cleanup buildreq

* Sun Feb 22 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1.2-alt1.dev0.git20141106
- Initial build for Sisyphus

