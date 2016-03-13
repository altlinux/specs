%define oname z3c.zalchemy

%def_with python3

Name: python-module-%oname
Version: 0.2.2
Release: alt2.1
Summary: SQLAlchemy integration into Zope 3
License: ZPLv2.1
Group: Development/Python
Url: http://pypi.python.org/pypi/z3c.zalchemy/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-devel python-module-setuptools
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
BuildPreReq: python-tools-2to3
%endif

%py_requires z3c SQLAlchemy ZODB3 zope.component zope.interface
%py_requires zope.schema zope.app.testing zope.app.component
%py_requires zope.app.keyreference zope.app.container
%py_requires zope.app.pagetemplate

%description
"z3c.zalchemy" integrates the object relational mapper SQLAlchemy into
Zope 3 as SQLOS integrates sqlobject.

zalchemy tries to do its best not to interfere with the standard
SQLAlchemy usage. The main part of zalchemy is the integration of the
SQLAlchemy transaction into the Zope transaction. This is solved by
using a data manager which joins the Zope transaction for every newly
created thread.

%package -n python3-module-%oname
Summary: SQLAlchemy integration into Zope 3
Group: Development/Python3
%py3_requires z3c SQLAlchemy ZODB3 zope.component zope.interface
%py3_requires zope.schema zope.app.testing zope.app.component
%py3_requires zope.app.keyreference zope.app.container
%py3_requires zope.app.pagetemplate

%description -n python3-module-%oname
"z3c.zalchemy" integrates the object relational mapper SQLAlchemy into
Zope 3 as SQLOS integrates sqlobject.

zalchemy tries to do its best not to interfere with the standard
SQLAlchemy usage. The main part of zalchemy is the integration of the
SQLAlchemy transaction into the Zope transaction. This is solved by
using a data manager which joins the Zope transaction for every newly
created thread.

%package -n python3-module-%oname-tests
Summary: Tests for z3c.zalchemy
Group: Development/Python3
Requires: python3-module-%oname = %version-%release

%description -n python3-module-%oname-tests
"z3c.zalchemy" integrates the object relational mapper SQLAlchemy into
Zope 3 as SQLOS integrates sqlobject.

zalchemy tries to do its best not to interfere with the standard
SQLAlchemy usage. The main part of zalchemy is the integration of the
SQLAlchemy transaction into the Zope transaction. This is solved by
using a data manager which joins the Zope transaction for every newly
created thread.

This package contains tests for z3c.zalchemy.

%package tests
Summary: Tests for z3c.zalchemy
Group: Development/Python
Requires: %name = %version-%release
%py_requires pysqlite

%description tests
"z3c.zalchemy" integrates the object relational mapper SQLAlchemy into
Zope 3 as SQLOS integrates sqlobject.

zalchemy tries to do its best not to interfere with the standard
SQLAlchemy usage. The main part of zalchemy is the integration of the
SQLAlchemy transaction into the Zope transaction. This is solved by
using a data manager which joins the Zope transaction for every newly
created thread.

This package contains tests for z3c.zalchemy.

%prep
%setup

%if_with python3
cp -fR . ../python3
%endif

%build
%python_build

%if_with python3
pushd ../python3
find -type f -name '*.py' -exec 2to3 -w -n '{}' +
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
rm -f %buildroot%python3_sitelibdir/z3c/__init__.py
%endif

%files
%doc *.txt
%python_sitelibdir/*
%exclude %python_sitelibdir/*/__init__.*
%exclude %python_sitelibdir/*/*/test*
%exclude %python_sitelibdir/*/*/*/test*

%files tests
%python_sitelibdir/*/*/test*
%python_sitelibdir/*/*/*/test*

%if_with python3
%files -n python3-module-%oname
%doc *.txt
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/*/test*
%exclude %python3_sitelibdir/*/*/*/test*
%exclude %python3_sitelibdir/*/*/*/*/test*

%files -n python3-module-%oname-tests
%python3_sitelibdir/*/*/test*
%python3_sitelibdir/*/*/*/test*
%python3_sitelibdir/*/*/*/*/test*
%endif

%changelog
* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.2.2-alt2.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jul 24 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.2.2-alt2
- Added module for Python 3

* Wed Dec 28 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.2.2-alt1
- Version 0.2.2

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.2.1-alt3.1
- Rebuild with Python-2.7

* Sun Jun 26 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.2.1-alt3
- Added necessary requirements

* Fri Jun 03 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.2.1-alt2
- Avoid conflict with python-module-z3c

* Thu Jun 02 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.2.1-alt1
- Initial build for Sisyphus

