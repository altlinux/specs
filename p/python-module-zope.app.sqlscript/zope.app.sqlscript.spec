%define oname zope.app.sqlscript

%def_without python3

Name: python-module-%oname
Version: 3.5.0
Release: alt4
Summary: SQL Script -- Zope 3 Content Component
License: ZPLv2.1
Group: Development/Python
Url: http://pypi.python.org/pypi/zope.app.sqlscript/

Source: %name-%version.tar

BuildRequires: python-devel python-module-setuptools
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel python3-module-setuptools
BuildRequires: python-tools-2to3
%endif

%py_requires zope.app ZODB3 zope.annotation zope.app.cache
%py_requires zope.app.component zope.app.form zope.component
%py_requires zope.container zope.documenttemplate zope.i18nmessageid
%py_requires zope.interface zope.rdb zope.schema zope.traversing

%description
This package provides the SQL Script content type for Zope 3
applications. SQL Scripts are connected to execute SQL statements and
the result is return in an object-oriented data structure.

%if_with python3
%package -n python3-module-%oname
Summary: SQL Script -- Zope 3 Content Component
Group: Development/Python3
%py3_requires zope.app ZODB3 zope.annotation zope.app.cache
%py3_requires zope.app.component zope.app.form zope.component
%py3_requires zope.container zope.documenttemplate zope.i18nmessageid
%py3_requires zope.interface zope.rdb zope.schema zope.traversing

%description -n python3-module-%oname
This package provides the SQL Script content type for Zope 3
applications. SQL Scripts are connected to execute SQL statements and
the result is return in an object-oriented data structure.

%package -n python3-module-%oname-tests
Summary: Tests for zope.app.sqlscript
Group: Development/Python3
Requires: python3-module-%oname = %version-%release
%py3_requires zope.app.testing zope.app.securitypolicy zope.app.zptpage
%py3_requires zope.app.zcmlfiles

%description -n python3-module-%oname-tests
This package provides the SQL Script content type for Zope 3
applications. SQL Scripts are connected to execute SQL statements and
the result is return in an object-oriented data structure.

This package contains tests for zope.app.sqlscript.
%endif

%package tests
Summary: Tests for zope.app.sqlscript
Group: Development/Python
Requires: %name = %version-%release
%py_requires zope.app.testing zope.app.securitypolicy zope.app.zptpage
%py_requires zope.app.zcmlfiles

%description tests
This package provides the SQL Script content type for Zope 3
applications. SQL Scripts are connected to execute SQL statements and
the result is return in an object-oriented data structure.

This package contains tests for zope.app.sqlscript.

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
%doc *.txt
%python_sitelibdir/*
%exclude %python_sitelibdir/*.pth
%exclude %python_sitelibdir/*/*/*/test*
%exclude %python_sitelibdir/*/*/*/*/test*

%files tests
%python_sitelibdir/*/*/*/test*
%python_sitelibdir/*/*/*/*/test*

%if_with python3
%files -n python3-module-%oname
%doc *.txt
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*.pth
%exclude %python3_sitelibdir/*/*/*/test*
%exclude %python3_sitelibdir/*/*/*/*/test*
%exclude %python3_sitelibdir/*/*/*/*/*/test*

%files -n python3-module-%oname-tests
%python3_sitelibdir/*/*/*/test*
%python3_sitelibdir/*/*/*/*/test*
%python3_sitelibdir/*/*/*/*/*/test*
%endif

%changelog
* Fri Dec 29 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 3.5.0-alt4
- Rebuilt without python-3.

* Mon Jun 06 2016 Ivan Zakharyaschev <imz@altlinux.org> 3.5.0-alt3.1.1
- (AUTO) subst_x86_64.

* Mon Mar 14 2016 Ivan Zakharyaschev <imz@altlinux.org> 3.5.0-alt3.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Sat Jul 26 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.5.0-alt3
- Added module for Python 3

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 3.5.0-alt2.1
- Rebuild with Python-2.7

* Tue Jun 28 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.5.0-alt2
- Added necessary requirements
- Excluded *.pth

* Tue May 24 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.5.0-alt1
- Initial build for Sisyphus

