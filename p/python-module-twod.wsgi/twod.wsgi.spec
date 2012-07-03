%define oname twod.wsgi
Name: python-module-%oname
Version: 1.0.1
Release: alt1.1
Summary: Enhanced WSGI support for Django applications
License: BSD
Group: Development/Python
Url: http://pypi.python.org/pypi/twod.wsgi/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-distribute

Requires: python-module-django

%description
twod.wsgi unlocks Django applications so developers can take advantage
of the wealth of existing WSGI software, as the other popular Python
frameworks do. It won't break you existing Django applications because
it's 100% compatible with Django and you can start using the
functionality offered by this library progressively. It should be really
easy to get started, particularly for developers who are familiar with
frameworks like Pylons or TurboGears.

%package tests
Summary: Tests for twod.wsgi
Group: Development/Python
Requires: %name = %version-%release

%description tests
twod.wsgi unlocks Django applications so developers can take advantage
of the wealth of existing WSGI software, as the other popular Python
frameworks do. It won't break you existing Django applications because
it's 100% compatible with Django and you can start using the
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

%prep
%setup

%build
%python_build

%install
%python_install

touch %buildroot%python_sitelibdir/twod/__init__.py

%files
%doc README.txt
%python_sitelibdir/*
%exclude %python_sitelibdir/*.pth
%exclude %python_sitelibdir/twod/__init__.py*
%exclude %python_sitelibdir/*test*

%files tests
%python_sitelibdir/*test*

%files -n python-module-twod
%python_sitelibdir/twod/__init__.py

%changelog
* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.0.1-alt1.1
- Rebuild with Python-2.7

* Thu Jun 30 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.1-alt1
- Initial build for Sisyphus

