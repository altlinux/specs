%define oname twod.wsgi

%def_with python3

Name: python-module-%oname
Version: 2.0
Release: alt2.b1.1
Summary: Enhanced WSGI support for Django applications
License: BSD
Group: Development/Python
Url: http://pypi.python.org/pypi/twod.wsgi/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
BuildPreReq: python-tools-2to3
%endif

Requires: python-module-django python-module-twod

%description
twod.wsgi unlocks Django applications so developers can take advantage
of the wealth of existing WSGI software, as the other popular Python
frameworks do. It won't break you existing Django applications because
it's 100%% compatible with Django and you can start using the
functionality offered by this library progressively. It should be really
easy to get started, particularly for developers who are familiar with
frameworks like Pylons or TurboGears.

%package -n python3-module-%oname
Summary: Enhanced WSGI support for Django applications
Group: Development/Python3
Requires: python3-module-django python3-module-twod

%description -n python3-module-%oname
twod.wsgi unlocks Django applications so developers can take advantage
of the wealth of existing WSGI software, as the other popular Python
frameworks do. It won't break you existing Django applications because
it's 100%% compatible with Django and you can start using the
functionality offered by this library progressively. It should be really
easy to get started, particularly for developers who are familiar with
frameworks like Pylons or TurboGears.

%package -n python3-module-%oname-tests
Summary: Tests for twod.wsgi
Group: Development/Python3
Requires: python3-module-%oname = %version-%release

%description -n python3-module-%oname-tests
twod.wsgi unlocks Django applications so developers can take advantage
of the wealth of existing WSGI software, as the other popular Python
frameworks do. It won't break you existing Django applications because
it's 100%% compatible with Django and you can start using the
functionality offered by this library progressively. It should be really
easy to get started, particularly for developers who are familiar with
frameworks like Pylons or TurboGears.

This package contains tests for twod.wsgi.

%package tests
Summary: Tests for twod.wsgi
Group: Development/Python
Requires: %name = %version-%release

%description tests
twod.wsgi unlocks Django applications so developers can take advantage
of the wealth of existing WSGI software, as the other popular Python
frameworks do. It won't break you existing Django applications because
it's 100%% compatible with Django and you can start using the
functionality offered by this library progressively. It should be really
easy to get started, particularly for developers who are familiar with
frameworks like Pylons or TurboGears.

This package contains tests for twod.wsgi.

%package -n python-module-twod
Summary: Core package for twod
Group: Development/Python
%py_provides twod

%description -n python-module-twod
Core package for twod.

%package -n python3-module-twod
Summary: Core package for twod
Group: Development/Python3
%py3_provides twod

%description -n python3-module-twod
Core package for twod.

%prep
%setup

%if_with python3
cp -fR . ../python3
find ../python3 -type f -name '*.py' -exec 2to3 -w -n '{}' +
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
touch %buildroot%python_sitelibdir/twod/__init__.py

%if_with python3
pushd ../python3
%python3_install
popd
touch %buildroot%python3_sitelibdir/twod/__init__.py
%endif

%files
%doc README.txt
%python_sitelibdir/*
%exclude %python_sitelibdir/*.pth
%exclude %python_sitelibdir/twod/__init__.py*
#exclude %python_sitelibdir/*test*

#files tests
#python_sitelibdir/*test*

%files -n python-module-twod
%python_sitelibdir/twod/__init__.py*

%if_with python3
%files -n python3-module-%oname
%doc README.txt
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*.pth
%exclude %python3_sitelibdir/twod/__init__.py
%exclude %python3_sitelibdir/twod/__pycache__/__init__.*

%files -n python3-module-twod
%python3_sitelibdir/twod/__init__.py
%python3_sitelibdir/twod/__pycache__/__init__.*
%endif

%changelog
* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 2.0-alt2.b1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Wed Jul 30 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.0-alt2.b1
- Added module for Python 3

* Thu Sep 19 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.0-alt1.b1
- Version 2.0b1

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.0.1-alt1.1
- Rebuild with Python-2.7

* Thu Jun 30 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.1-alt1
- Initial build for Sisyphus

