# REMOVE ME (I was set for NMU) and uncomment real Release tags:
Release: alt1.dev0.git20150226.1.1.1
%define oname zope.dottedname

%def_with python3

Name: python-module-%oname
Version: 4.1.1
#Release: alt1.dev0.git20150226.1
Summary: Resolver for Python dotted names
License: ZPLv2.1
Group: Development/Python
Url: http://pypi.python.org/pypi/zope.dottedname/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-devel python-module-setuptools
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel python3-module-setuptools
%endif

%py_requires zope

%description
The zope.dottedname module provides one function, resolve that resolves
strings containing dotted names into the appropriate python object.

Dotted names are resolved by importing modules and by getting attributes
from imported modules. Names may be relative, provided the module they
are relative to is supplied.

%if_with python3
%package -n python3-module-%oname
Summary: Resolver for Python 3 dotted names
Group: Development/Python3

%description -n python3-module-%oname
The zope.dottedname module provides one function, resolve that resolves
strings containing dotted names into the appropriate python object.

Dotted names are resolved by importing modules and by getting attributes
from imported modules. Names may be relative, provided the module they
are relative to is supplied.

%package -n python3-module-%oname-tests
Summary: Tests for Resolver for Python 3 dotted names
Group: Development/Python3
Requires: python3-module-%oname = %version-%release
%py3_requires zope.testing

%description -n python3-module-%oname-tests
The zope.dottedname module provides one function, resolve that resolves
strings containing dotted names into the appropriate python object.

Dotted names are resolved by importing modules and by getting attributes
from imported modules. Names may be relative, provided the module they
are relative to is supplied.

This package contains tests for Resolver for Python dotted names.
%endif

%package tests
Summary: Tests for Resolver for Python dotted names
Group: Development/Python
Requires: %name = %version-%release
%py_requires zope.testing

%description tests
The zope.dottedname module provides one function, resolve that resolves
strings containing dotted names into the appropriate python object.

Dotted names are resolved by importing modules and by getting attributes
from imported modules. Names may be relative, provided the module they
are relative to is supplied.

This package contains tests for Resolver for Python dotted names.

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
python setup.py test -v
%if_with python3
pushd ../python3
python3 setup.py test -v
popd
%endif

%files
%doc *.txt *.rst
%python_sitelibdir/*
%exclude %python_sitelibdir/*.pth
%exclude %python_sitelibdir/*/*/tests.*
%exclude %python_sitelibdir/*/*/example.*

%files tests
%python_sitelibdir/*/*/tests.*
%python_sitelibdir/*/*/example.*

%if_with python3
%files -n python3-module-%oname
%doc *.txt *.rst
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*.pth
%exclude %python3_sitelibdir/*/*/tests.*
%exclude %python3_sitelibdir/*/*/*/tests.*
%exclude %python3_sitelibdir/*/*/example.*
%exclude %python3_sitelibdir/*/*/*/example.*

%files -n python3-module-%oname-tests
%python3_sitelibdir/*/*/tests.*
%python3_sitelibdir/*/*/*/tests.*
%python3_sitelibdir/*/*/example.*
%python3_sitelibdir/*/*/*/example.*
%endif

%changelog
* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 4.1.1-alt1.dev0.git20150226.1.1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Tue Jun 07 2016 Ivan Zakharyaschev <imz@altlinux.org> 4.1.1-alt1.dev0.git20150226.1.1
- (AUTO) subst_x86_64.

* Mon Mar 14 2016 Ivan Zakharyaschev <imz@altlinux.org> 4.1.1-alt1.dev0.git20150226.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Fri Aug 28 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.1.1-alt1.dev0.git20150226
- Version 4.1.1.dev0
- Enabled check

* Mon Dec 29 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.1.0-alt1
- Version 4.1.0

* Tue Apr 09 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.0.1-alt1
- Version 4.0.1

* Mon Apr 16 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.4.6-alt3
- Added module for Python 3

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 3.4.6-alt2.1
- Rebuild with Python-2.7

* Tue Jun 28 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.4.6-alt2
- Added necessary requirements
- Excluded *.pth

* Mon May 30 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.4.6-alt1
- Initial build for Sisyphus

