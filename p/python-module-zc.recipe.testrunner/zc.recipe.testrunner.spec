%define oname zc.recipe.testrunner

%def_with python3

Name: python-module-%oname
Version: 2.0.0
Release: alt2.1
Summary: ZC Buildout recipe for creating test runners
License: ZPLv2.1
Group: Development/Python
Url: http://pypi.python.org/pypi/zc.recipe.testrunner/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-devel python-module-setuptools
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
%endif

%py_requires zc.recipe zc.buildout zope.testrunner z3c.recipe.scripts
%py_requires zope.testing

%description
This recipe generates zope.testing test-runner scripts for testing a
collection of eggs. The eggs must already be installed (using the
zc.recipe.egg recipe).

%package -n python3-module-%oname
Summary: ZC Buildout recipe for creating test runners
Group: Development/Python3
%py3_requires zc.recipe zc.buildout zope.testrunner z3c.recipe.scripts
%py3_requires zope.testing

%description -n python3-module-%oname
This recipe generates zope.testing test-runner scripts for testing a
collection of eggs. The eggs must already be installed (using the
zc.recipe.egg recipe).

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

%if_with python3
%files -n python3-module-%oname
%doc *.txt
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*.pth
%endif

%changelog
* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 2.0.0-alt2.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Wed Jul 23 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.0.0-alt2
- Added module for Python 3

* Mon Apr 08 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.0.0-alt1
- Version 2.0.0

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.4.0-alt2.1
- Rebuild with Python-2.7

* Sun Jun 26 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.4.0-alt2
- Added necessary requirements
- Excluded *.pth

* Tue Jun 07 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.4.0-alt1
- Initial build for Sisyphus

