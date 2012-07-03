%define oname zope.fixers
%def_with python3

Name: python-module-%oname
Version: 1.0
Release: alt4
Summary: 2to3 fixers for Zope
License: ZPL
Group: Development/Python
Url: http://pypi.python.org/pypi/zope.fixers/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-devel python-module-distribute
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel python3-module-distribute
BuildPreReq: python-tools-2to3
%endif

%py_requires zope

%description
Fixers for Zope Component Architecture and the frameworks built with it.

Currently, there is only one fixer, fix_implements. This fixer will
change all uses of implements(IFoo) in a class body to the class
decorator @implementer(IFoo), which is the most likely Python 3 syntax
for zope.interfaces implements statements.

%if_with python3
%package -n python3-module-%oname
Summary: 2to3 fixers for Zope (Python 3)
Group: Development/Python3
%py3_requires zope

%description -n python3-module-%oname
Fixers for Zope Component Architecture and the frameworks built with it.

Currently, there is only one fixer, fix_implements. This fixer will
change all uses of implements(IFoo) in a class body to the class
decorator @implementer(IFoo), which is the most likely Python 3 syntax
for zope.interfaces implements statements.

%package -n python3-module-%oname-tests
Summary: Tests for zope.fixers (Python 3)
Group: Development/Python3
Requires: python3-module-%oname = %version-%release

%description -n python3-module-%oname-tests
Fixers for Zope Component Architecture and the frameworks built with it.

Currently, there is only one fixer, fix_implements. This fixer will
change all uses of implements(IFoo) in a class body to the class
decorator @implementer(IFoo), which is the most likely Python 3 syntax
for zope.interfaces implements statements.

This package contains tests for zope.fixers.
%endif

%package tests
Summary: Tests for zope.fixers
Group: Development/Python
Requires: %name = %version-%release

%description tests
Fixers for Zope Component Architecture and the frameworks built with it.

Currently, there is only one fixer, fix_implements. This fixer will
change all uses of implements(IFoo) in a class body to the class
decorator @implementer(IFoo), which is the most likely Python 3 syntax
for zope.interfaces implements statements.

This package contains tests for zope.fixers.

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
%exclude %python_sitelibdir/*/*/tests.py*

%files tests
%python_sitelibdir/*/*/tests.py*

%if_with python3
%files -n python3-module-%oname
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/*/tests.*

%files -n python3-module-%oname-tests
%python3_sitelibdir/*/*/tests.*
%endif

%changelog
* Thu Apr 12 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0-alt4
- Added module for Python 3

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.0-alt3.1
- Rebuild with Python-2.7

* Tue Jun 28 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0-alt3
- Added necessary requirements
- Excluded *.pth

* Thu May 19 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0-alt2
- Set as archdep package

* Tue May 17 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0-alt1
- Initial build for Sisyphus

