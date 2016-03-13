%define oname z3c.recipe.compattest

%def_with python3

Name: python-module-%oname
Version: 1.0
Release: alt2.1
Summary: Buildout recipe to create testrunners for testing compatibility with other packages
License: ZPLv2.1
Group: Development/Python
Url: http://pypi.python.org/pypi/z3c.recipe.compattest/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-devel python-module-setuptools
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
%endif

%py_requires z3c.recipe zc.buildout zc.recipe.testrunner

%description
Buildout recipe to create testrunners for testing compatibility with
other packages.

%package -n python3-module-%oname
Summary: Buildout recipe to create testrunners for testing compatibility with other packages
Group: Development/Python3
%py3_requires z3c.recipe zc.buildout zc.recipe.testrunner

%description -n python3-module-%oname
Buildout recipe to create testrunners for testing compatibility with
other packages.

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
%doc *.rst
%python_sitelibdir/*
%exclude %python_sitelibdir/*.pth

%if_with python3
%files -n python3-module-%oname
%doc *.rst
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*.pth
%endif

%changelog
* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.0-alt2.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Wed Jul 23 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0-alt2
- Added module for Python 3

* Fri Apr 05 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0-alt1
- Version 1.0

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.13.1-alt2.1
- Rebuild with Python-2.7

* Fri Jun 24 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.13.1-alt2
- Added necessary requirements
- Excluded *.pth

* Sat Jun 04 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.13.1-alt1
- Initial build for Sisyphus

