%define oname zc.twist

%def_with python3

Name: python-module-%oname
Version: 1.3.1
Release: alt4.1
Summary: Mixing Twisted and ZODB
License: ZPL
Group: Development/Python
Url: http://pypi.python.org/pypi/zc.twist/

Source: %name-%version.tar

BuildPreReq: python-devel python-module-setuptools
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
%endif
BuildPreReq: python-tools-2to3

Requires: python-module-twisted-core
%py_requires zc ZODB3 zope.component zope.testing

%description
Twist: Talking to the ZODB in Twisted Reactor Calls.

The twist package contains a few functions and classes, but primarily a
helper for having a deferred call on a callable persistent object, or on
a method on a persistent object. This lets you have a Twisted reactor
call or a Twisted deferred callback affect the ZODB. Everything can be
done within the main thread, so it can be full-bore Twisted usage,
without threads.

%package -n python3-module-%oname
Summary: Mixing Twisted and ZODB
Group: Development/Python3
Requires: python3-module-twisted-core
%py3_requires zc ZODB3 zope.component zope.testing

%description -n python3-module-%oname
Twist: Talking to the ZODB in Twisted Reactor Calls.

The twist package contains a few functions and classes, but primarily a
helper for having a deferred call on a callable persistent object, or on
a method on a persistent object. This lets you have a Twisted reactor
call or a Twisted deferred callback affect the ZODB. Everything can be
done within the main thread, so it can be full-bore Twisted usage,
without threads.

%package -n python3-module-%oname-tests
Summary: Tests for Mixing Twisted and ZODB
Group: Development/Python3
Requires: python3-module-%oname = %version-%release

%description -n python3-module-%oname-tests
Twist: Talking to the ZODB in Twisted Reactor Calls.

The twist package contains a few functions and classes, but primarily a
helper for having a deferred call on a callable persistent object, or on
a method on a persistent object. This lets you have a Twisted reactor
call or a Twisted deferred callback affect the ZODB. Everything can be
done within the main thread, so it can be full-bore Twisted usage,
without threads.

This package contains tests for Mixing Twisted and ZODB.

%package tests
Summary: Tests for Mixing Twisted and ZODB
Group: Development/Python
Requires: %name = %version-%release

%description tests
Twist: Talking to the ZODB in Twisted Reactor Calls.

The twist package contains a few functions and classes, but primarily a
helper for having a deferred call on a callable persistent object, or on
a method on a persistent object. This lets you have a Twisted reactor
call or a Twisted deferred callback affect the ZODB. Everything can be
done within the main thread, so it can be full-bore Twisted usage,
without threads.

This package contains tests for Mixing Twisted and ZODB.

%prep
%setup

%if_with python3
cp -fR . ../python3
find ../python3 -type f -name '*.py' -exec 2to3 -w -n '{}' +
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

%if_with python3
pushd ../python3
%python3_install
popd
rm -f %buildroot%python3_sitelibdir/*/__init__.py
%endif

%files
%doc *.txt
%python_sitelibdir/*
%exclude %python_sitelibdir/*/__init__.*
%exclude %python_sitelibdir/*/*/tests.*

%files tests
%python_sitelibdir/*/*/tests.*

%if_with python3
%files -n python3-module-%oname
%doc *.txt
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/*/tests.*
%exclude %python3_sitelibdir/*/*/*/tests.*

%files -n python3-module-%oname-tests
%python3_sitelibdir/*/*/tests.*
%python3_sitelibdir/*/*/*/tests.*
%endif

%changelog
* Thu Mar 22 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 1.3.1-alt4.1
- (NMU) Rebuilt with python-3.6.4.

* Wed Aug 16 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 1.3.1-alt4
- Rebuilt with new Twist.

* Thu Mar 17 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.3.1-alt3.1
- (NMU) rebuild with python3-3.5 & rpm-build-python3-0.1.10
  (for ABI dependence and new python3(*) reqs)

* Fri Jul 25 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.3.1-alt3
- Added module for Python 3

* Thu Apr 12 2012 Vitaly Kuznetsov <vitty@altlinux.ru> 1.3.1-alt2.1.1
- Rebuild to remove redundant libpython2.7 dependency

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.3.1-alt2.1
- Rebuild with Python-2.7

* Mon Jun 27 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.3.1-alt2
- Added necessary requirements

* Mon Jun 06 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.3.1-alt1
- Initial build for Sisyphus

