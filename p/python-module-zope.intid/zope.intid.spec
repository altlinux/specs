%define _unpackaged_files_terminate_build 1
# REMOVE ME (I was set for NMU) and uncomment real Release tags:
Release: alt1
%define oname zope.intid

%def_with python3

Name: python-module-%oname
Version: 4.2.0
#Release: alt1.1
Summary: Integer Id Utility
License: ZPLv2.1
Group: Development/Python
Url: http://pypi.python.org/pypi/zope.intid
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source0: https://pypi.python.org/packages/61/97/ab669ff465d0ab7a606e3bc525ce1838522bc3227da857155c78460e125d/%{oname}-%{version}.tar.gz

BuildPreReq: python-devel python-module-setuptools
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
%endif

%py_requires zope zope.lifecycleevent zope.component zope.event ZODB3
%py_requires zope.interface zope.keyreference zope.location zope.security

%description
This package provides an API to create integer ids for any object. Later
objects can be looked up by their id as well. This functionality is
commonly used in situations where dealing with objects is undesirably,
such as in search indices or any code that needs an easy hash of an
object.

%package -n python3-module-%oname
Summary: Integer Id Utility
Group: Development/Python3
%py3_requires zope zope.lifecycleevent zope.component zope.event ZODB3
%py3_requires zope.interface zope.keyreference zope.location zope.security

%description -n python3-module-%oname
This package provides an API to create integer ids for any object. Later
objects can be looked up by their id as well. This functionality is
commonly used in situations where dealing with objects is undesirably,
such as in search indices or any code that needs an easy hash of an
object.

%package -n python3-module-%oname-tests
Summary: Tests for zope.intid
Group: Development/Python3
Requires: python3-module-%oname = %version-%release
%py3_requires zope.testing zope.site zope.traversing zope.container

%description -n python3-module-%oname-tests
This package provides an API to create integer ids for any object. Later
objects can be looked up by their id as well. This functionality is
commonly used in situations where dealing with objects is undesirably,
such as in search indices or any code that needs an easy hash of an
object.

This package contains tests for zope.intid.

%package tests
Summary: Tests for zope.intid
Group: Development/Python
Requires: %name = %version-%release
%py_requires zope.testing zope.site zope.traversing zope.container

%description tests
This package provides an API to create integer ids for any object. Later
objects can be looked up by their id as well. This functionality is
commonly used in situations where dealing with objects is undesirably,
such as in search indices or any code that needs an easy hash of an
object.

This package contains tests for zope.intid.

%prep
%setup -q -n %{oname}-%{version}

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
%if "%python_sitelibdir_noarch" != "%python_sitelibdir"
install -d %buildroot%python_sitelibdir
mv %buildroot%python_sitelibdir_noarch/* \
	%buildroot%python_sitelibdir/
%endif

%if_with python3
pushd ../python3
%python3_install
popd
%if "%python3_sitelibdir_noarch" != "%python3_sitelibdir"
install -d %buildroot%python3_sitelibdir
mv %buildroot%python3_sitelibdir_noarch/* \
	%buildroot%python3_sitelibdir/
%endif
%endif

%files
%doc *.txt *.rst
%python_sitelibdir/*
%exclude %python_sitelibdir/*.pth
%exclude %python_sitelibdir/*/*/tests.*

%files tests
%python_sitelibdir/*/*/tests.*

%if_with python3
%files -n python3-module-%oname
%doc *.txt *.rst
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*.pth
%exclude %python3_sitelibdir/*/*/tests.*
%exclude %python3_sitelibdir/*/*/*/tests.*

%files -n python3-module-%oname-tests
%python3_sitelibdir/*/*/tests.*
%python3_sitelibdir/*/*/*/tests.*
%endif

%changelog
* Wed Jan 11 2017 Igor Vlasenko <viy@altlinux.ru> 4.2.0-alt1
- automated PyPI update

* Mon Jun 06 2016 Ivan Zakharyaschev <imz@altlinux.org> 4.1.0-alt1.1.1
- (AUTO) subst_x86_64.

* Mon Mar 14 2016 Ivan Zakharyaschev <imz@altlinux.org> 4.1.0-alt1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Mon Dec 29 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.1.0-alt1
- Version 4.1.0

* Mon Dec 22 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.0.0-alt4
- Version 4.0.0

* Fri Jul 18 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.0.0-alt3.a1
- Added module for Python 3

* Wed Jul 16 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.0.0-alt2.a1
- Avoid requirement on ZODB3

* Tue Apr 09 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.0.0-alt1.a1
- Version 4.0.0a1

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 3.7.2-alt2.1
- Rebuild with Python-2.7

* Wed Jun 29 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.7.2-alt2
- Added necessary requirements
- Excluded *.pth

* Sat May 21 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.7.2-alt1
- Initial build for Sisyphus

