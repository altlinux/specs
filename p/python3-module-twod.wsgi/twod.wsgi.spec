%define oname twod.wsgi

Name: python3-module-%oname
Version: 2.0
Release: alt3

Summary: Enhanced WSGI support for Django applications
License: BSD
Group: Development/Python3
Url: http://pypi.python.org/pypi/twod.wsgi/
BuildArch: noarch

Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python-tools-2to3

Requires: python3-module-django python3-module-twod


%description
twod.wsgi unlocks Django applications so developers can take advantage
of the wealth of existing WSGI software, as the other popular Python
frameworks do. It won't break you existing Django applications because
it's 100%% compatible with Django and you can start using the
functionality offered by this library progressively. It should be really
easy to get started, particularly for developers who are familiar with
frameworks like Pylons or TurboGears.

%package tests
Summary: Tests for twod.wsgi
Group: Development/Python3
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

%package -n python3-module-twod
Summary: Core package for twod
Group: Development/Python3
%py3_provides twod

%description -n python3-module-twod
Core package for twod.

%prep
%setup

find ./ -type f -name '*.py' -exec 2to3 -w -n '{}' +

%build
%python3_build

%install
%python3_install

touch %buildroot%python3_sitelibdir/twod/__init__.py

%files
%doc README.txt
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*.pth
%exclude %python3_sitelibdir/twod/__init__.py
%exclude %python3_sitelibdir/twod/__pycache__/__init__.*

%files -n python3-module-twod
%python3_sitelibdir/twod/__init__.py
%python3_sitelibdir/twod/__pycache__/__init__.*


%changelog
* Wed Dec 18 2019 Andrey Bychkov <mrdrew@altlinux.org> 2.0-alt3
- build for python2 disabled

* Wed May 16 2018 Andrey Bychkov <mrdrew@altlinux.org> 2.0-alt2.b1.2
- (NMU) rebuild with python3.6

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

