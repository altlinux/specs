Name: python-module-django-debug-toolbar
Version: 0.8.4
Release: alt1.gita3e8ce.1

Summary: A debug/profiling overlay for Django

License: GPL
Group: Development/Python
BuildArch: noarch
Url: http://github.com/dcramer/django-debug-toolbar
Packager: Denis Klimov <zver@altlinux.org>

# https://github.com/dcramer/django-debug-toolbar.git
Source: %name-%version.tar

BuildPreReq: python-module-setuptools

%description
This is a fork of Rob Hudson's Debug Toolbar. It includes an
alternative style, performance optimizations, and some panels which
may not be available in the main repository.

%package tests
Summary: Tests for Django Debug Toolbar
Group: Development/Python
Requires: %name = %version-%release
%add_python_req_skip dingus

%description tests
This is a fork of Rob Hudson's Debug Toolbar. It includes an
alternative style, performance optimizations, and some panels which
may not be available in the main repository.

This package contains tests for Django Debug Toolbar.

%prep
%setup -n %name-%version

%build
%python_build

%install
%python_install

%files
%doc README.rst AUTHORS LICENSE NEWS
%python_sitelibdir/*
%exclude %python_sitelibdir/debug_toolbar/*tests*

%files tests
%python_sitelibdir/debug_toolbar/*tests*

%changelog
* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.8.4-alt1.gita3e8ce.1
- Rebuild with Python-2.7

* Tue May 10 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.8.4-alt1.gita3e8ce
- Version 0.8.4

* Fri Feb 25 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.2-alt1.gitd478b5
- Version 0.2

* Thu Nov 19 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.0.0-alt1.gita2802d.1
- Rebuilt with python 2.6

* Sat Feb 14 2009 Denis Klimov <zver@altlinux.org> 0.0.0-alt1.gita2802d
- Initial build for ALT Linux

