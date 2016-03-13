%define oname repoze.zcml

%def_with python3

Name: python-module-%oname
Version: 1.0
Release: alt1.b1.git20141211.1
Summary: Simplified ZCML directives, reduced dependencies
License: BSD
Group: Development/Python
Url: https://github.com/repoze/repoze.zcml
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/repoze/repoze.zcml.git
Source: %name-%version.tar

BuildPreReq: python-devel python-module-setuptools
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
%endif

%py_requires repoze zope.component zope.configuration

%description
``repoze.zcml`` is a package which provides basic ZCML directives for
the Zope Component Architecture (such as ``utility``, ``subscriber``,
and ``adapter``).  You should use ``repoze.zcml`` if your application
doesn't need the more advanced features of the "stock" directive types
of the same names present in ``zope.configuration`` (e.g. permissions,
and trusted adapters/utilities).

%package -n python3-module-%oname
Summary: Simplified ZCML directives, reduced dependencies
Group: Development/Python3
%py3_requires repoze zope.component zope.configuration

%description -n python3-module-%oname
``repoze.zcml`` is a package which provides basic ZCML directives for
the Zope Component Architecture (such as ``utility``, ``subscriber``,
and ``adapter``).  You should use ``repoze.zcml`` if your application
doesn't need the more advanced features of the "stock" directive types
of the same names present in ``zope.configuration`` (e.g. permissions,
and trusted adapters/utilities).

%package -n python3-module-%oname-tests
Summary: Tests for repoze.zcml
Group: Development/Python3
Requires: python3-module-%oname = %version-%release
%py3_requires zope.testing

%description -n python3-module-%oname-tests
``repoze.zcml`` is a package which provides basic ZCML directives for
the Zope Component Architecture (such as ``utility``, ``subscriber``,
and ``adapter``).  You should use ``repoze.zcml`` if your application
doesn't need the more advanced features of the "stock" directive types
of the same names present in ``zope.configuration`` (e.g. permissions,
and trusted adapters/utilities).

This package contains tests for repoze.zcml.

%package tests
Summary: Tests for repoze.zcml
Group: Development/Python
Requires: %name = %version-%release
%py_requires zope.testing

%description tests
``repoze.zcml`` is a package which provides basic ZCML directives for
the Zope Component Architecture (such as ``utility``, ``subscriber``,
and ``adapter``).  You should use ``repoze.zcml`` if your application
doesn't need the more advanced features of the "stock" directive types
of the same names present in ``zope.configuration`` (e.g. permissions,
and trusted adapters/utilities).

This package contains tests for repoze.zcml.

%prep
%setup

%if_with python3
cp -fR . ../python3
%endif

%build
%python_build

%if_with python3
pushd ../python3
%python3_build
popd
%endif

%install
%python_install
%ifarch x86_64
install -d %buildroot%python_sitelibdir
mv %buildroot%python_sitelibdir_noarch/* \
	%buildroot%python_sitelibdir/
%endif

%if_with python3
pushd ../python3
%python3_install
popd
%ifarch x86_64
install -d %buildroot%python3_sitelibdir
mv %buildroot%python3_sitelibdir_noarch/* \
	%buildroot%python3_sitelibdir/
%endif
%endif

%files
%doc *.txt docs/*.rst *.rst
%python_sitelibdir/*
%exclude %python_sitelibdir/*.pth
%exclude %python_sitelibdir/*/*/tests.*

%files tests
%python_sitelibdir/*/*/tests.*

%if_with python3
%files -n python3-module-%oname
%doc *.txt docs/*.rst *.rst
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*.pth
%exclude %python3_sitelibdir/*/*/tests.*
%exclude %python3_sitelibdir/*/*/*/tests.*

%files -n python3-module-%oname-tests
%python3_sitelibdir/*/*/tests.*
%python3_sitelibdir/*/*/*/tests.*
%endif

%changelog
* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.0-alt1.b1.git20141211.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Fri Dec 12 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0-alt1.b1.git20141211
- Version 1.0b1

* Thu Jul 31 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.5-alt2.git20120325
- Added module for Python 3

* Thu Apr 04 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.5-alt1.git20120325
- New snapshot

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.5-alt1.git20110222.1.1
- Rebuild with Python-2.7

* Thu Jun 30 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.5-alt1.git20110222.1
- Added necessary requirements
- Excluded *.pth

* Tue Jun 14 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.5-alt1.git20110222
- Initial build for Sisyphus

