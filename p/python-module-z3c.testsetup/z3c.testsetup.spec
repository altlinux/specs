# REMOVE ME (I was set for NMU) and uncomment real Release tags:
Release: alt1.dev.svn20100915.1.1.1
%define oname z3c.testsetup

%def_with python3

Name: python-module-%oname
Version: 0.8.4
#Release: alt1.dev.svn20100915.1
Summary: Easier test setup for Zope 3 projects and other Python packages
License: ZPLv2.1
Group: Development/Python
Url: http://pypi.python.org/pypi/z3c.testsetup/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# svn://svn.zope.org/repos/main/z3c.testsetup/trunk/
Source: %name-%version.tar

BuildPreReq: python-devel python-module-setuptools
BuildPreReq: python-module-zope.testing
BuildPreReq: python-module-martian
BuildPreReq: python-module-zope.app.testing
BuildPreReq: python-module-zope.app.zcmlfiles
BuildPreReq: python-module-zope.component
BuildPreReq: python-module-zope.untrustedpython
BuildPreReq: python-module-zope.hookable
BuildPreReq: python-module-WSGIProxy2
BuildPreReq: python-module-zodbpickle
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
BuildPreReq: python-tools-2to3
BuildPreReq: python3-module-zope.testing
BuildPreReq: python3-module-martian
BuildPreReq: python3-module-zope.app.testing
BuildPreReq: python3-module-zope.app.zcmlfiles
BuildPreReq: python3-module-zope.component
BuildPreReq: python3-module-zope.hookable
BuildPreReq: python3-module-WSGIProxy2
BuildPreReq: python3-module-zodbpickle
%endif

%py_requires zope.testing martian zope.app.testing zope.app.zcmlfiles
%py_requires zope.component

%add_python_req_skip non_existing_package

%description
Setting up tests for Zope 3 projects sometimes tends to be cumbersome.
You often have to prepare complex things like test layers, setup
functions, teardown functions and much more. Often these steps have to
be done again and again. z3c.testsetup jumps in here, to support much
flatter test setups. The package supports normal Python unit tests and
doctests.

Doctests and test modules are found throughout a whole package and
registered with sensible, modifiable defaults. This saves a lot of
manual work!

See README.txt and the other .txt files in the src/z3c/testsetup
directory for API documentation. (Or further down this page when reading
this on pypi).

%package -n python3-module-%oname
Summary: Easier test setup for Zope 3 projects and other Python packages
Group: Development/Python3
%py3_requires zope.testing martian zope.app.testing zope.app.zcmlfiles
%py3_requires zope.component
%add_python3_req_skip non_existing_package

%description -n python3-module-%oname
Setting up tests for Zope 3 projects sometimes tends to be cumbersome.
You often have to prepare complex things like test layers, setup
functions, teardown functions and much more. Often these steps have to
be done again and again. z3c.testsetup jumps in here, to support much
flatter test setups. The package supports normal Python unit tests and
doctests.

Doctests and test modules are found throughout a whole package and
registered with sensible, modifiable defaults. This saves a lot of
manual work!

See README.txt and the other .txt files in the src/z3c/testsetup
directory for API documentation. (Or further down this page when reading
this on pypi).

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
python setup.py test
%if_with python3
pushd ../python3
python3 setup.py test
popd
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
* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 0.8.4-alt1.dev.svn20100915.1.1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Tue Jun 07 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.8.4-alt1.dev.svn20100915.1.1
- (AUTO) subst_x86_64.

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.8.4-alt1.dev.svn20100915.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Oct 23 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.8.4-alt1.dev.svn20100915
- Version 0.8.4dev

* Wed Jul 23 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.8.3-alt3
- Added module for Python 3

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.8.3-alt2.1
- Rebuild with Python-2.7

* Sun Jun 26 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.8.3-alt2
- Added necessary requirements
- Excluded *.pth

* Mon May 30 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.8.3-alt1
- Initial build for Sisyphus

