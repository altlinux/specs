%define oname django-debug-toolbar

%def_with python3

Name: python-module-%oname
Version: 0.8.5
Release: alt1.gitbf39bb.1

Summary: A debug/profiling overlay for Django

License: GPL
Group: Development/Python
BuildArch: noarch
Url: http://github.com/dcramer/django-debug-toolbar
Packager: Denis Klimov <zver@altlinux.org>

# https://github.com/dcramer/django-debug-toolbar.git
Source: %name-%version.tar

BuildPreReq: python-module-setuptools
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
BuildPreReq: python-tools-2to3
%endif

%description
This is a fork of Rob Hudson's Debug Toolbar. It includes an
alternative style, performance optimizations, and some panels which
may not be available in the main repository.

%package -n python3-module-%oname
Summary: A debug/profiling overlay for Django
Group: Development/Python3

%description -n python3-module-%oname
This is a fork of Rob Hudson's Debug Toolbar. It includes an
alternative style, performance optimizations, and some panels which
may not be available in the main repository.

%package -n python3-module-%oname-tests
Summary: Tests for Django Debug Toolbar
Group: Development/Python3
Requires: python3-module-%oname = %version-%release

%description -n python3-module-%oname-tests
This is a fork of Rob Hudson's Debug Toolbar. It includes an
alternative style, performance optimizations, and some panels which
may not be available in the main repository.

This package contains tests for Django Debug Toolbar.

%package tests
Summary: Tests for Django Debug Toolbar
Group: Development/Python
Requires: %name = %version-%release

%description tests
This is a fork of Rob Hudson's Debug Toolbar. It includes an
alternative style, performance optimizations, and some panels which
may not be available in the main repository.

This package contains tests for Django Debug Toolbar.

%prep
%setup -n %name-%version

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

%if_with python3
pushd ../python3
%python3_install
popd
%endif

%files
%doc README.rst AUTHORS LICENSE NEWS
%python_sitelibdir/*
%exclude %python_sitelibdir/debug_toolbar/*tests*
%exclude %python_sitelibdir/example

%files tests
%python_sitelibdir/debug_toolbar/*tests*

%if_with python3
%files -n python3-module-%oname
%doc README.rst AUTHORS LICENSE NEWS
%python3_sitelibdir/*
%exclude %python3_sitelibdir/debug_toolbar/*tests*
%exclude %python3_sitelibdir/debug_toolbar/*/*tests*
%exclude %python3_sitelibdir/example

%files -n python3-module-%oname-tests
%python3_sitelibdir/debug_toolbar/*tests*
%python3_sitelibdir/debug_toolbar/*/*tests*
%endif

%changelog
* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.8.5-alt1.gitbf39bb.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Sat Jul 19 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.8.5-alt1.gitbf39bb
- Version 0.8.5
- Added module for Python 3

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

