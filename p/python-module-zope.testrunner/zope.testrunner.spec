%define oname zope.testrunner

%def_with python3

Name: python-module-%oname
Version: 4.4.9
Release: alt1.1
Summary: Zope testrunner script
License: ZPL
Group: Development/Python
Url: http://pypi.python.org/pypi/zope.testrunner/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

#BuildPreReq: python-devel python-module-setuptools-tests
%if_with python3
BuildRequires(pre): rpm-build-python3
# Automatically added by buildreq on Thu Jan 28 2016 (-bi)
# optimized out: python-base python-devel python-module-pytest python-module-setuptools python-modules python-modules-compiler python-modules-ctypes python-modules-email python-modules-encodings python-modules-unittest python3 python3-base python3-module-pytest python3-module-setuptools python3-module-zope python3-module-zope.interface
BuildRequires: python-module-setuptools-tests python3-module-setuptools-tests python3-module-zope.fixers rpm-build-python3

#BuildRequires: python3-devel python3-module-setuptools-tests
#BuildPreReq: python3-module-zope.fixers python-tools-2to3
%endif

%py_requires zope zope.testing subunit zope.exceptions zope.interface

%description
This package provides a flexible test runner with layer support.

%package tests
Summary: Tests for zope.testrunner
Group: Development/Python
Requires: %name = %EVR

%description tests
This package provides a flexible test runner with layer support.

This package contains tests for zope.testrunner.

%if_with python3
%package -n python3-module-%oname
Summary: Zope testrunner script (Python 3)
Group: Development/Python3
%py3_requires zope zope.testing subunit zope.exceptions zope.interface

%description -n python3-module-%oname
This package provides a flexible test runner with layer support.

%package -n python3-module-%oname-tests
Summary: Tests for zope.testrunner
Group: Development/Python3
Requires: python3-module-%oname = %EVR

%description -n python3-module-%oname-tests
This package provides a flexible test runner with layer support.

This package contains tests for zope.testrunner.
%endif

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
%if_with python3
pushd ../python3
%python3_install
popd
mv %buildroot%_bindir/zope-testrunner \
	%buildroot%_bindir/zope-testrunner3
%ifarch x86_64
install -d %buildroot%python3_sitelibdir
mv %buildroot%python3_sitelibdir_noarch/* \
	%buildroot%python3_sitelibdir/
%endif
%endif

%python_install
%ifarch x86_64
install -d %buildroot%python_sitelibdir
mv %buildroot%python_sitelibdir_noarch/* \
	%buildroot%python_sitelibdir/
%endif

%files
%doc *.rst
%_bindir/*
%exclude %_bindir/zope-testrunner3
%python_sitelibdir/*
%exclude %python_sitelibdir/*.pth
%exclude %python_sitelibdir/*/*/tests

%files tests
%python_sitelibdir/*/*/tests

%if_with python3
%files -n python3-module-%oname
%doc *.rst
%_bindir/zope-testrunner3
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/*/tests

%files -n python3-module-%oname-tests
%python3_sitelibdir/*/*/tests
%endif

%changelog
* Fri Jan 29 2016 Mikhail Efremov <sem@altlinux.org> 4.4.9-alt1.1
- NMU: Use buildreq for BR.

* Wed Aug 26 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.4.9-alt1
- Version 4.4.9

* Sat Feb 14 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.4.6-alt1
- Version 4.4.6

* Wed Jan 07 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.4.5-alt1
- Version 4.4.5

* Mon Dec 29 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.4.4-alt1
- Version 4.4.4

* Sun Jul 27 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.4.3-alt1
- Version 4.4.3

* Tue Sep 24 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.4.1-alt1
- Version 4.4.1

* Mon Apr 08 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.3.3-alt1
- Version 4.3.3

* Fri Mar 22 2013 Aleksey Avdeev <solo@altlinux.ru> 4.0.4-alt2.1
- Rebuild with Python-3.3

* Thu Apr 12 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.0.4-alt2
- Added module for Python 3

* Thu Dec 29 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.0.4-alt1
- Version 4.0.4

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 4.0.3-alt3.1
- Rebuild with Python-2.7

* Wed Jun 29 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.0.3-alt3
- Added necessary requirements
- Excluded *.pth

* Thu May 19 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.0.3-alt2
- Set as archdep package

* Tue May 17 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.0.3-alt1
- Initial build for Sisyphus

