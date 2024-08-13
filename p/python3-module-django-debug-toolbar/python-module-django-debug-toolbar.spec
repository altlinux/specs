%define oname django-debug-toolbar

Name: python3-module-%oname
Version: 4.4.6
Release: alt1

Summary: A configurable set of panels that display various debug information about the current request/response.
License: BSD-3-Clause
Group: Development/Python3
Url: https://github.com/jazzband/django-debug-toolbar
BuildArch: noarch

Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools python3-module-wheel
BuildRequires: python3-module-django
BuildRequires: python3-module-hatchling
#BuildRequires: python3-module-sphinx

%description
The Django Debug Toolbar is a configurable set of panels that
display various debug information about the current request/response
and when clicked, display more details about the panel's content.

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
%setup

sed -i 's|sphinx-build|sphinx-build-3|' docs/Makefile

sed -i 's|from.*Command|# from.*Command|' \
    $(find ./ -name 'debugsqlshell.py')

sed -i 's|#!/usr/bin/env python|#!/usr/bin/env python3|' \
    $(find ./ -name '*.py')

%build
%pyproject_build

#export PYTHONPATH=$PWD
#%%make -C docs man

%install
%pyproject_install

%files
%doc README.rst LICENSE
%python3_sitelibdir/*

#%%files docs
#%%doc docs/_build/* example

%changelog
* Mon Aug 12 2024 Alexander Burmatov <thatman@altlinux.org> 4.4.6-alt1
- new version 4.4.6.
- using the new pyproject macros

* Wed Aug 18 2021 Alexey Shabalin <shaba@altlinux.org> 3.2.2-alt1
- new version 3.2.2
- disable build docs

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
