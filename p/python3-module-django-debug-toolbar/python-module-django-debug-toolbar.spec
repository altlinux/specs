%define oname django-debug-toolbar

Name: python3-module-%oname
Version: 1.9.1
Release: alt2

Summary: A debug/profiling overlay for Django
License: GPL
Group: Development/Python3
Url: http://github.com/dcramer/django-debug-toolbar
BuildArch: noarch

Source: %oname-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-django
BuildRequires: python3-module-sphinx
BuildRequires: python-tools-2to3


%description
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

sed -i 's|sphinx-build|sphinx-build-3|' docs/Makefile

sed -i 's|from.*Command|# from.*Command|' \
    $(find ./ -name 'debugsqlshell.py')

find -type f -name '*.py' -exec 2to3 -w -n '{}' +

sed -i 's|#!/usr/bin/env python|#!/usr/bin/env python3|' \
    $(find ./ -name '*.py')

%build
%python3_build

export PYTHONPATH=$PWD
%make -C docs man

%install
%python3_install

%files
%doc README.rst LICENSE example/
%python3_sitelibdir/*

%files docs
%doc docs/_build/*


%changelog
* Thu Dec 19 2019 Andrey Bychkov <mrdrew@altlinux.org> 1.9.1-alt2
- build for python2 disabled

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
