%define oname django-debug-toolbar

Name: python-module-%oname
Version: 1.9.1
Release: alt1

Summary: A debug/profiling overlay for Django
License: GPL
Group: Development/Python
Url: http://github.com/dcramer/django-debug-toolbar
BuildArch: noarch

Source: %oname-%version.tar

BuildRequires(pre): rpm-macros-sphinx
BuildRequires: python-module-setuptools
BuildRequires: python-module-django
BuildRequires: python-module-sphinx

BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
BuildPreReq: python3-module-django
BuildPreReq: python3-module-sphinx
BuildPreReq: python-tools-2to3


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

%package docs
Summary: Documentation for %name
Group: Development/Documentation
Requires: %name = %version-%release

%description docs
This is a fork of Rob Hudson's Debug Toolbar. It includes an
alternative style, performance optimizations, and some panels which
may not be available in the main repository.

This package contains documentation for %name

%prep
%setup -n %oname-%version

cp -fR . ../python3

%build
%python_build

pushd ../python3
find -type f -name '*.py' -exec 2to3 -w -n '{}' +
%python3_build
popd

export PYTHONPATH=$PWD
%make -C docs man

%install
%python_install

pushd ../python3
%python3_install
popd

%files
%doc README.rst LICENSE example/
%python_sitelibdir/*

%files -n python3-module-%oname
%doc README.rst LICENSE example/
%python3_sitelibdir/*

%files docs
%doc docs/_build/*


%changelog
* Mon Apr 02 2018 Andrey Bychkov <mrdrew@altlinux.org> 1.9.1-alt1
- Updated version to 1.9.1

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
