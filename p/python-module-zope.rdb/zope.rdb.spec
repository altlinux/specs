%define oname zope.rdb

%def_without python3

Name: python-module-%oname
Version: 3.5.0
Release: alt4
Summary: Zope RDBMS transaction integration
License: ZPLv2.1
Group: Development/Python
Url: http://pypi.python.org/pypi/zope.rdb/

Source: %name-%version.tar

BuildRequires: python-devel python-module-setuptools
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel python3-module-setuptools
BuildRequires: python-tools-2to3
%endif

%py_requires zope transaction ZODB3 zope.container zope.interface
%py_requires zope.i18nmessageid zope.security zope.configuration
%py_requires zope.container zope.schema zope.thread

%description
Zope RDBMS Transaction Integration.

Provides a proxy for interaction between the zope transaction framework
and the db-api connection. Databases which want to support sub
transactions need to implement their own proxy.

%if_with python3
%package -n python3-module-%oname
Summary: Zope RDBMS transaction integration
Group: Development/Python3
%py3_requires zope transaction ZODB3 zope.container zope.interface
%py3_requires zope.i18nmessageid zope.security zope.configuration
%py3_requires zope.container zope.schema zope.thread

%description -n python3-module-%oname
Zope RDBMS Transaction Integration.

Provides a proxy for interaction between the zope transaction framework
and the db-api connection. Databases which want to support sub
transactions need to implement their own proxy.

%package -n python3-module-%oname-tests
Summary: Tests for Zope RDBMS transaction integration
Group: Development/Python3
Requires: python3-module-%oname = %version-%release

%description -n python3-module-%oname-tests
Zope RDBMS Transaction Integration.

Provides a proxy for interaction between the zope transaction framework
and the db-api connection. Databases which want to support sub
transactions need to implement their own proxy.

This package contains tests for Zope RDBMS transaction integration.
%endif

%package tests
Summary: Tests for Zope RDBMS transaction integration
Group: Development/Python
Requires: %name = %version-%release

%description tests
Zope RDBMS Transaction Integration.

Provides a proxy for interaction between the zope transaction framework
and the db-api connection. Databases which want to support sub
transactions need to implement their own proxy.

This package contains tests for Zope RDBMS transaction integration.

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
%if "%_lib" == "lib64"
install -d %buildroot%python_sitelibdir
mv %buildroot%python_sitelibdir_noarch/* \
	%buildroot%python_sitelibdir/
%endif

%if_with python3
pushd ../python3
%python3_install
popd
%if "%_lib" == "lib64"
install -d %buildroot%python3_sitelibdir
mv %buildroot%python3_sitelibdir_noarch/* \
	%buildroot%python3_sitelibdir/
%endif
%endif

%files
%doc *.txt
%python_sitelibdir/*
%exclude %python_sitelibdir/*.pth
%exclude %python_sitelibdir/*/*/tests

%files tests
%python_sitelibdir/*/*/tests

%if_with python3
%files -n python3-module-%oname
%doc *.txt
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*.pth
%exclude %python3_sitelibdir/*/*/tests

%files -n python3-module-%oname-tests
%python3_sitelibdir/*/*/tests
%endif

%changelog
* Fri Dec 29 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 3.5.0-alt4
- Rebuilt without python-3.

* Mon Mar 14 2016 Ivan Zakharyaschev <imz@altlinux.org> 3.5.0-alt3.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Sat Jul 26 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.5.0-alt3
- Added module for Python 3

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 3.5.0-alt2.1
- Rebuild with Python-2.7

* Wed Jun 29 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.5.0-alt2
- Added necessary requirements
- Excluded *.pth

* Fri May 27 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.5.0-alt1
- Initial build for Sisyphus

