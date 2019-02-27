%define oname zope.deprecation

Name: python-module-%oname
Epoch: 1
Version: 4.4.0
Release: alt1

Summary: Zope 3 Deprecation Infrastructure
License: ZPLv2.1
Group: Development/Python
Url: http://pypi.python.org/pypi/zope.deprecation/
# git://github.com/zopefoundation/zope.deprecation.git
Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3

BuildRequires: python-module-setuptools python3-module-setuptools rpm-build-python3

%py_requires zope


%description
When we started working on Zope 3.1, we noticed that the hardest part of
the development process was to ensure backward-compatibility and
correctly mark deprecated modules, classes, functions, methods and
properties. This package provides a simple function called
'deprecated(names, reason)' to deprecate the previously mentioned Python
objects.

%package -n python3-module-%oname
Summary: Zope 3 Deprecation Infrastructure (Python 3)
Group: Development/Python3
%py3_requires zope

%description -n python3-module-%oname
When we started working on Zope 3.1, we noticed that the hardest part of
the development process was to ensure backward-compatibility and
correctly mark deprecated modules, classes, functions, methods and
properties. This package provides a simple function called
'deprecated(names, reason)' to deprecate the previously mentioned Python
objects.

%package -n python3-module-%oname-tests
Summary: Tests for Zope 3 Deprecation Infrastructure (Python 3)
Group: Development/Python3
Requires: python3-module-%oname = %EVR
%py3_requires zope.testing
%add_python3_req_skip deprecation

%description -n python3-module-%oname-tests
When we started working on Zope 3.1, we noticed that the hardest part of
the development process was to ensure backward-compatibility and
correctly mark deprecated modules, classes, functions, methods and
properties. This package provides a simple function called
'deprecated(names, reason)' to deprecate the previously mentioned Python
objects.

This package contains tests for Zope 3 Deprecation Infrastructure.

%package tests
Summary: Tests for Zope 3 Deprecation Infrastructure
Group: Development/Python
Requires: %name = %EVR
%py_requires zope.testing
%add_python_req_skip deprecation

%description tests
When we started working on Zope 3.1, we noticed that the hardest part of
the development process was to ensure backward-compatibility and
correctly mark deprecated modules, classes, functions, methods and
properties. This package provides a simple function called
'deprecated(names, reason)' to deprecate the previously mentioned Python
objects.

This package contains tests for Zope 3 Deprecation Infrastructure.

%prep
%setup

rm -rf ../python3
cp -a . ../python3

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

%files
%doc *.txt
%python_sitelibdir/*
%exclude %python_sitelibdir/*.pth
%exclude %python_sitelibdir/*/*/tests.*

%files tests
%python_sitelibdir/*/*/tests.*

%files -n python3-module-%oname
%doc *.txt
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*.pth
%exclude %python3_sitelibdir/*/*/tests.*
%exclude %python3_sitelibdir/*/*/__pycache__/tests.*

%files -n python3-module-%oname-tests
%python3_sitelibdir/*/*/tests.*
%python3_sitelibdir/*/*/__pycache__/tests.*


%changelog
* Wed Feb 27 2019 Andrey Bychkov <mrdrew@altlinux.org> 1:4.4.0-alt1
- Version updated to 4.4.0

* Tue Jun 07 2016 Ivan Zakharyaschev <imz@altlinux.org> 1:4.1.3-alt1.dev0.git20150113.1.1.1
- (AUTO) subst_x86_64.

* Mon Mar 14 2016 Ivan Zakharyaschev <imz@altlinux.org> 1:4.1.3-alt1.dev0.git20150113.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Fri Jan 29 2016 Mikhail Efremov <sem@altlinux.org> 1:4.1.3-alt1.dev0.git20150113.1
- NMU: Use buildreq for BR.

* Thu Jan 15 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1:4.1.3-alt1.dev0.git20150113
- Version 4.1.3.dev0

* Sat Jul 26 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1:4.1.1-alt1
- Version 4.1.1

* Wed Mar 13 2013 Aleksey Avdeev <solo@altlinux.ru> 4.2.2-alt1
- Version 4.0.2

* Sat May 05 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.5.1-alt1
- Version 3.5.1
- Added module for Python 3

* Mon Dec 12 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.5.0-alt1
- Version 3.5.0

* Mon Oct 24 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 3.4.0-alt3.1
- Rebuild with Python-2.7

* Tue Jun 28 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.4.0-alt3
- Added necessary requirements
- Excluded *.pth

* Sat May 28 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.4.0-alt2
- Enable tests

* Sat May 21 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.4.0-alt1
- Initial build for Sisyphus
