%define oname zope.app.generations

%def_with python3

Name: python-module-%oname
Version: 3.7.1
Release: alt2.1
Summary: ZMI UI for zope.generations
License: ZPLv2.1
Group: Development/Python
Url: http://pypi.python.org/pypi/zope.app.generations/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-devel python-module-setuptools
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
%endif

%py_requires ZODB3 zope.app.publication zope.app.renderer
%py_requires zope.applicationcontrol zope.generations zope.interface
%py_requires zope.processlifetime

%description
Generations are a way of updating objects in the database when the
application schema changes. An application schema is essentially the
structure of data, the structure of classes in the case of ZODB or the
table descriptions in the case of a relational database.

This package only contains the ZMI user interface for zope.generations

%package -n python3-module-%oname
Summary: ZMI UI for zope.generations
Group: Development/Python3
%py3_requires ZODB3 zope.app.publication zope.app.renderer
%py3_requires zope.applicationcontrol zope.generations zope.interface
%py3_requires zope.processlifetime

%description -n python3-module-%oname
Generations are a way of updating objects in the database when the
application schema changes. An application schema is essentially the
structure of data, the structure of classes in the case of ZODB or the
table descriptions in the case of a relational database.

This package only contains the ZMI user interface for zope.generations

%package -n python3-module-%oname-tests
Summary: Tests for zope.app.generations
Group: Development/Python3
Requires: python3-module-%oname = %version-%release
%py3_requires zope.app.testing zope.app.zcmlfiles zope.login
%py3_requires zope.publisher zope.securitypolicy zope.testing

%description -n python3-module-%oname-tests
Generations are a way of updating objects in the database when the
application schema changes. An application schema is essentially the
structure of data, the structure of classes in the case of ZODB or the
table descriptions in the case of a relational database.

This package contains tests for zope.app.generations.

%package tests
Summary: Tests for zope.app.generations
Group: Development/Python
Requires: %name = %version-%release
%py_requires zope.app.testing zope.app.zcmlfiles zope.login
%py_requires zope.publisher zope.securitypolicy zope.testing

%description tests
Generations are a way of updating objects in the database when the
application schema changes. An application schema is essentially the
structure of data, the structure of classes in the case of ZODB or the
table descriptions in the case of a relational database.

This package contains tests for zope.app.generations.

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
* Mon Mar 14 2016 Ivan Zakharyaschev <imz@altlinux.org> 3.7.1-alt2.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Fri Jul 18 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.7.1-alt2
- Added module for Python 3

* Tue Apr 09 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.7.1-alt1
- Version 3.7.1

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 3.7.0-alt2.1
- Rebuild with Python-2.7

* Mon Jun 27 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.7.0-alt2
- Added necessary requirements
- Excluded *.pth

* Sun May 22 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.7.0-alt1
- Initial build for Sisyphus

