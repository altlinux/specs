%define oname zope.testing

%def_with python3
%def_without check
%def_enable light_version

Name: python-module-%oname
Version: 4.4.0
Release: alt2.git20150825.1
Summary: Zope testing helpers
License: ZPL
Group: Development/Python
Url: http://pypi.python.org/pypi/zope.testing/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/zopefoundation/zope.testing.git
Source: %name-%version.tar

#BuildPreReq: python-devel python-module-setuptools-tests
#BuildPreReq: python-module-zope.exceptions
#BuildPreReq: python-module-zope.interface
%if_disabled light_version
#BuildPreReq: python-module-zope.testrunner
%endif
%if_with python3
BuildRequires(pre): rpm-build-python3
# Automatically added by buildreq on Thu Jan 28 2016 (-bi)
# optimized out: python-base python-devel python-module-setuptools python-module-zope.interface python-modules python-modules-compiler python-modules-ctypes python-modules-email python-modules-encodings python-modules-unittest python3 python3-base python3-module-setuptools python3-module-zope python3-module-zope.interface
BuildRequires: python-module-pytest python-module-zope.exceptions python3-module-pytest python3-module-zope.exceptions rpm-build-python3

#BuildRequires: python3-devel python3-module-setuptools-tests
#BuildPreReq: python3-module-zope.exceptions
#BuildPreReq: python3-module-zope.interface
%if_disabled light_version
#BuildPreReq: python3-module-zope.testrunner
#BuildPreReq: python-tools-2to3
%endif
%endif

%py_requires zope.exceptions zope.interface 
%if_disabled light_version
%py_requires zope.testrunner
%endif

%description
This package provides a number of testing frameworks. It includes a
flexible test runner, and supports both doctest and unittest.

%if_with python3
%package -n python3-module-%oname
Summary: Zope testing helpers (Python 3)
Group: Development/Python3
%py3_requires zope.exceptions zope.interface 
%if_disabled light_version
%py3_requires zope.testrunner
%endif

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
* Fri Jan 29 2016 Mikhail Efremov <sem@altlinux.org> 4.4.0-alt2.git20150825.1
- NMU: Use buildreq for BR.

* Tue Jan 19 2016 Sergey Alembekov <rt@altlinux.ru> 4.4.0-alt2.git20150825
- Rebuild light version to break cycle

* Wed Aug 26 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.4.0-alt1.git20150825
- Version 4.4.0

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

