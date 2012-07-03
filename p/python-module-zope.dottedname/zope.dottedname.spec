%define oname zope.dottedname

%def_with python3

Name: python-module-%oname
Version: 3.4.6
Release: alt3
Summary: Resolver for Python dotted names
License: ZPLv2.1
Group: Development/Python
Url: http://pypi.python.org/pypi/zope.dottedname/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-devel python-module-distribute
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel python3-module-distribute
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

#files -n python3-module-%oname-tests
#python3_sitelibdir/*/*/tests.*
%endif

%changelog
* Mon Apr 16 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.4.6-alt3
- Added module for Python 3

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 3.4.6-alt2.1
- Rebuild with Python-2.7

* Tue Jun 28 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.4.6-alt2
- Added necessary requirements
- Excluded *.pth

* Mon May 30 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.4.6-alt1
- Initial build for Sisyphus

