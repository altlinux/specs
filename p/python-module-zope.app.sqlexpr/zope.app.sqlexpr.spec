%define oname zope.app.sqlexpr

%def_without python3

Name: python-module-%oname
Version: 0.1
Release: alt4
Summary: allow quick SQL queries in TALES expressions and Zope Page Templates
License: ZPLv2.1
Group: Development/Python
Url: http://pypi.python.org/pypi/zope.app.sqlexpr/

Source: %name-%version.tar

BuildRequires: python-devel python-module-setuptools
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel python3-module-setuptools
BuildRequires: python-tools-2to3
%endif

%py_requires zope.app zope.component zope.interface zope.tales
%py_requires zope.exceptions zope.rdb

%description
The goal of the SQL TALES expression is to allow quick SQL queries right
out of TALES expressions and Zope Page Templates. While this is
certainly not the Zopeish way of doing things, it allows the newbie Web
scripter an easier entrance to the world of Zope 3.

%if_with python3
%package -n python3-module-%oname
Summary: allow quick SQL queries in TALES expressions and Zope Page Templates
Group: Development/Python3
%py3_requires zope.app zope.component zope.interface zope.tales
%py3_requires zope.exceptions zope.rdb

%description -n python3-module-%oname
The goal of the SQL TALES expression is to allow quick SQL queries right
out of TALES expressions and Zope Page Templates. While this is
certainly not the Zopeish way of doing things, it allows the newbie Web
scripter an easier entrance to the world of Zope 3.

%package -n python3-module-%oname-tests
Summary: Tests for zope.app.sqlexpr
Group: Development/Python3
Requires: python3-module-%oname = %version-%release
%py3_requires zope.app.sqlexpr

%description -n python3-module-%oname-tests
The goal of the SQL TALES expression is to allow quick SQL queries right
out of TALES expressions and Zope Page Templates. While this is
certainly not the Zopeish way of doing things, it allows the newbie Web
scripter an easier entrance to the world of Zope 3.

This package contains tests for zope.app.sqlexpr.
%endif

%package tests
Summary: Tests for zope.app.sqlexpr
Group: Development/Python
Requires: %name = %version-%release
%py_requires zope.app.sqlexpr

%description tests
The goal of the SQL TALES expression is to allow quick SQL queries right
out of TALES expressions and Zope Page Templates. While this is
certainly not the Zopeish way of doing things, it allows the newbie Web
scripter an easier entrance to the world of Zope 3.

This package contains tests for zope.app.sqlexpr.

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
%exclude %python_sitelibdir/*/*/*/tests.*

%files tests
%python_sitelibdir/*/*/*/tests.*

%if_with python3
%files -n python3-module-%oname
%doc *.txt
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*.pth
%exclude %python3_sitelibdir/*/*/*/tests.*
%exclude %python3_sitelibdir/*/*/*/*/tests.*

%files -n python3-module-%oname-tests
%python3_sitelibdir/*/*/*/tests.*
%python3_sitelibdir/*/*/*/*/tests.*
%endif

%changelog
* Fri Dec 29 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 0.1-alt4
- Rebuilt without python-3.

* Mon Jun 06 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.1-alt3.1.1
- (AUTO) subst_x86_64.

* Mon Mar 14 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.1-alt3.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Sat Jul 26 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1-alt3
- Added module for Python 3

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.1-alt2.1
- Rebuild with Python-2.7

* Tue Jun 28 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1-alt2
- Added necessary requirements
- Excluded *.pth

* Tue May 24 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1-alt1
- Initial build for Sisyphus

