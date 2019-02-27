%define oname zope.deferredimport
%def_without check

Name: python-module-%oname
Version: 4.3
Release: alt1
Summary: Allows you to perform imports names that will be resolved when used in the code
License: ZPLv2.1
Group: Development/Python
Url: http://pypi.python.org/pypi/zope.deferredimport/
# https://github.com/zopefoundation/zope.deferredimport.git

Source: %name-%version.tar

BuildRequires: python-devel python-module-setuptools
BuildRequires: python-module-zope.proxy python-module-zope.testrunner

BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
BuildPreReq: python3-module-zope.proxy python3-module-zope.testrunner

%py_requires zope zope.proxy


%description
Often, especially for package modules, you want to import names for
convenience, but not actually perform the imports until necessary. The
zope.deferredimport package provided facilities for defining names in
modules that will be imported from somewhere else when used. You can
also cause deprecation warnings to be issued when a variable is used.

%package -n python3-module-%oname
Summary: Allows you to perform imports names that will be resolved when used in the code
Group: Development/Python3
%py3_requires zope zope.proxy

%description -n python3-module-%oname
Often, especially for package modules, you want to import names for
convenience, but not actually perform the imports until necessary. The
zope.deferredimport package provided facilities for defining names in
modules that will be imported from somewhere else when used. You can
also cause deprecation warnings to be issued when a variable is used.

%package -n python3-module-%oname-tests
Summary: Tests for zope.deferredimport
Group: Development/Python3
Requires: python3-module-%oname = %version-%release
%py3_requires zope.testing

%description -n python3-module-%oname-tests
Often, especially for package modules, you want to import names for
convenience, but not actually perform the imports until necessary. The
zope.deferredimport package provided facilities for defining names in
modules that will be imported from somewhere else when used. You can
also cause deprecation warnings to be issued when a variable is used.

This package contains tests for zope.deferredimport.

%package tests
Summary: Tests for zope.deferredimport
Group: Development/Python
Requires: %name = %version-%release
%py_requires zope.testing

%description tests
Often, especially for package modules, you want to import names for
convenience, but not actually perform the imports until necessary. The
zope.deferredimport package provided facilities for defining names in
modules that will be imported from somewhere else when used. You can
also cause deprecation warnings to be issued when a variable is used.

This package contains tests for zope.deferredimport.

%package examples
Summary: Example files for %oname
Group: Development/Python
BuildArch: noarch
Requires: %name = %EVR

%description examples
Example files for %oname.

%prep
%setup
mv src/zope/deferredimport/samples ./

cp -fR . ../python3

%build
%python_build

pushd ../python3
%python3_build
popd

%install
%python_install
%if "%python_sitelibdir_noarch" != "%python_sitelibdir"
install -d %buildroot%python_sitelibdir
mv %buildroot%python_sitelibdir_noarch/* \
	%buildroot%python_sitelibdir/
%endif

pushd ../python3
%python3_install
popd
%if "%python3_sitelibdir_noarch" != "%python3_sitelibdir"
install -d %buildroot%python3_sitelibdir
mv %buildroot%python3_sitelibdir_noarch/* \
	%buildroot%python3_sitelibdir/
%endif

install -d %buildroot%_docdir/%name
cp -fR samples %buildroot%_docdir/%name

%if_with check
%check
python setup.py test -v

pushd ../python3
python3 setup.py test -v
popd
%endif


%files
%doc *.txt *.rst
%python_sitelibdir/*
%exclude %python_sitelibdir/*.pth
%exclude %python_sitelibdir/*/*/tests.*

%files tests
%python_sitelibdir/*/*/tests.*

%files -n python3-module-%oname
%doc *.txt *.rst
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*.pth
%exclude %python3_sitelibdir/*/*/tests.*
%exclude %python3_sitelibdir/*/*/*/tests.*

%files -n python3-module-%oname-tests
%python3_sitelibdir/*/*/tests.*
%python3_sitelibdir/*/*/*/tests.*

%files examples
%doc %_docdir/%name/samples


%changelog
* Wed Feb 27 2019 Andrey Bychkov <mrdrew@altlinux.org> 4.3-alt1
- Version updated to 4.3

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 4.1.1-alt1.dev0.git20150402.1.1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools
- Move samples to examples subpackage

* Tue Jun 07 2016 Ivan Zakharyaschev <imz@altlinux.org> 4.1.1-alt1.dev0.git20150402.1.1
- (AUTO) subst_x86_64.

* Mon Mar 14 2016 Ivan Zakharyaschev <imz@altlinux.org> 4.1.1-alt1.dev0.git20150402.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Fri Aug 28 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.1.1-alt1.dev0.git20150402
- Version 4.1.1.dev0
- Enabled check

* Mon Dec 29 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.1.0-alt1
- Version 4.1.0

* Mon Jul 21 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.0.0-alt2
- Added module for Python 3

* Tue Apr 09 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.0.0-alt1
- Version 4.0.0

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 3.5.3-alt2.1
- Rebuild with Python-2.7

* Tue Jun 28 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.5.3-alt2
- Added necessary requirements
- Excluded *.pth

* Fri May 27 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.5.3-alt1
- Initial build for Sisyphus

