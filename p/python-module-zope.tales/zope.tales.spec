# REMOVE ME (I was set for NMU) and uncomment real Release tags:
Release: alt1.1.1.1
%define oname zope.tales

%def_with python3

Name: python-module-%oname
Version: 4.1.1
#Release: alt1.1
Summary: Zope Template Application Language Expression Syntax (TALES)
License: ZPL
Group: Development/Python
Url: http://pypi.python.org/pypi/zope.tales/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-devel python-module-setuptools
BuildPreReq: python-module-zope.tal python-module-six
BuildPreReq: python-module-zope.testrunner
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel python3-module-setuptools
BuildPreReq: python3-module-zope.tal python3-module-six
BuildPreReq: python3-module-zope.testrunner
BuildPreReq: python-tools-2to3
%endif

%py_requires zope zope.interface zope.tal six

%description
Template Attribute Language - Expression Syntax.

%if_with python3
%package -n python3-module-%oname
Summary: Zope Template Application Language Expression Syntax (TALES) (Python 3)
Group: Development/Python3
%py3_requires zope zope.interface zope.tal six

%description -n python3-module-%oname
Template Attribute Language - Expression Syntax.

%package -n python3-module-%oname-tests
Summary: Tests for zope.tales (Python 3)
Group: Development/Python3
Requires: python3-module-%oname = %version-%release
%py3_requires zope.testing

%description -n python3-module-%oname-tests
Template Attribute Language - Expression Syntax.

This package contains tests for zope.tales.
%endif

%package tests
Summary: Tests for zope.tales
Group: Development/Python
Requires: %name = %version-%release
%py_requires zope.testing

%description tests
Template Attribute Language - Expression Syntax.

This package contains tests for zope.tales.

%prep
%setup
%if_with python3
rm -rf ../python3
cp -a . ../python3
%endif

%build
%python_build
%if_with python3
pushd ../python3
find -type f -name '*.py' -exec 2to3 -w '{}' +
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

%check
python setup.py test -v
%if_with python3
pushd ../python3
python3 setup.py test -v
popd
%endif

%files
%doc *.txt *.rst
%python_sitelibdir/*
%exclude %python_sitelibdir/*.pth
%exclude %python_sitelibdir/*/*/tests

%files tests
%python_sitelibdir/*/*/tests

%if_with python3
%files -n python3-module-%oname
%doc *.txt *.rst
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*.pth
%exclude %python3_sitelibdir/*/*/tests

%files -n python3-module-%oname-tests
%python3_sitelibdir/*/*/tests
%endif

%changelog
* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 4.1.1-alt1.1.1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Mon Jun 06 2016 Ivan Zakharyaschev <imz@altlinux.org> 4.1.1-alt1.1.1
- (AUTO) subst_x86_64.

* Mon Mar 14 2016 Ivan Zakharyaschev <imz@altlinux.org> 4.1.1-alt1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Fri Aug 28 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.1.1-alt1
- Version 4.1.1
- Enabled check

* Tue Dec 30 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.1.0-alt1
- Version 4.1.0

* Mon Dec 02 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.0.2-alt1
- Version 4.0.2

* Wed Apr 10 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.0.1-alt1
- Version 4.0.1

* Fri Mar 22 2013 Aleksey Avdeev <solo@altlinux.ru> 3.5.1-alt4.1
- Rebuild with Python-3.3

* Tue Apr 17 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.5.1-alt4
- Added module for Python 3

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 3.5.1-alt3.1
- Rebuild with Python-2.7

* Wed Jun 29 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.5.1-alt3
- Added necessary requirements
- Excluded *.pth

* Thu May 19 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.5.1-alt2
- Set as archdep package

* Tue May 17 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.5.1-alt1
- Initial build for Sisyphus

