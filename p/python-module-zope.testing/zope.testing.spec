%define oname zope.testing

%def_with python3

Name: python-module-%oname
Version: 4.1.4
Release: alt2.dev0.git20150128
Summary: Zope testing helpers
License: ZPL
Group: Development/Python
Url: http://pypi.python.org/pypi/zope.testing/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-devel python-module-setuptools-tests
BuildPreReq: python-module-zope.exceptions
BuildPreReq: python-module-zope.interface
BuildPreReq: python-module-zope.testrunner
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel python3-module-setuptools-tests
BuildPreReq: python3-module-zope.exceptions
BuildPreReq: python3-module-zope.interface
BuildPreReq: python3-module-zope.testrunner
BuildPreReq: python-tools-2to3
%endif

%py_requires zope.exceptions zope.interface zope.testrunner

%description
This package provides a number of testing frameworks. It includes a
flexible test runner, and supports both doctest and unittest.

%if_with python3
%package -n python3-module-%oname
Summary: Zope testing helpers (Python 3)
Group: Development/Python3
%py3_requires zope.exceptions zope.interface zope.testrunner

%description -n python3-module-%oname
This package provides a number of testing frameworks. It includes a
flexible test runner, and supports both doctest and unittest.
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

%check
python setup.py test
%if_with python3
pushd ../python3
python3 setup.py test
popd
%endif

%files
%doc *.txt *.rst
%python_sitelibdir/*
%exclude %python_sitelibdir/*.pth

%if_with python3
%files -n python3-module-%oname
%doc *.txt *.rst
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*.pth
%endif

%changelog
* Mon Feb 23 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.1.4-alt2.dev0.git20150128
- Version 4.1.4.dev0

* Wed Oct 22 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.1.4-alt1.dev.git20140319
- Version 4.1.4dev

* Sun Jul 27 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.1.3-alt1
- Version 4.1.3

* Wed Apr 10 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.1.2-alt1
- Version 4.1.2

* Fri Mar 22 2013 Aleksey Avdeev <solo@altlinux.ru> 4.1.1-alt1.1
- Rebuild with Python-3.3

* Thu Apr 12 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.1.1-alt1
- Version 4.1.1
- Added module for Python 3

* Thu Dec 29 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.0.0-alt1
- Version 4.0.0

* Mon Oct 24 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 3.10.2-alt3.1
- Rebuild with Python-2.7

* Sun Jun 19 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.10.2-alt3
- Added necessary requirements
- Excluded *.pth

* Thu May 19 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.10.2-alt2
- Set as archdep package

* Tue May 17 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.10.2-alt1
- Initial build for Sisyphus

