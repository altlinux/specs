%define oname zope.deprecation

%def_with python3

Name: python-module-%oname
Epoch: 1
Version: 4.1.3
Release: alt1.dev0.git20150113.1
Summary: Zope 3 Deprecation Infrastructure
License: ZPLv2.1
Group: Development/Python
Url: http://pypi.python.org/pypi/zope.deprecation/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# git://github.com/zopefoundation/zope.deprecation.git
Source: %name-%version.tar

#BuildPreReq: python-devel python-module-distribute
%if_with python3
BuildRequires(pre): rpm-build-python3
# Automatically added by buildreq on Thu Jan 28 2016 (-bi)
# optimized out: python-base python-devel python-modules python-modules-compiler python-modules-ctypes python-modules-email python-modules-encodings python-modules-unittest python3 python3-base
BuildRequires: python-module-setuptools python3-module-setuptools rpm-build-python3

#BuildRequires: python3-devel python3-module-distribute
%endif

%py_requires zope

%description
When we started working on Zope 3.1, we noticed that the hardest part of
the development process was to ensure backward-compatibility and
correctly mark deprecated modules, classes, functions, methods and
properties. This package provides a simple function called
'deprecated(names, reason)' to deprecate the previously mentioned Python
objects.

%if_with python3
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
%endif

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
%exclude %python_sitelibdir/*/*/tests.*

%files tests
%python_sitelibdir/*/*/tests.*

%if_with python3
%files -n python3-module-%oname
%doc *.txt
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*.pth
%exclude %python3_sitelibdir/*/*/tests.*
%exclude %python3_sitelibdir/*/*/__pycache__/tests.*

%files -n python3-module-%oname-tests
%python3_sitelibdir/*/*/tests.*
%python3_sitelibdir/*/*/__pycache__/tests.*
%endif

%changelog
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
