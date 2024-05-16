%define modulename python-memcached

Name: python3-module-memcached
Version: 1.62
Release: alt1

Summary: A Python module for memcached daemon
Group: Development/Python3
License: Python-2.0
URL: https://pypi.org/project/python-memcached
VCS: https://github.com/linsomniac/python-memcached

Source: %name-%version.tar

BuildArch: noarch

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-wheel

%py3_provides memcache

%description
%modulename is a Python module that interfaces to the memcached -
distributed memory object caching system.

%prep
%setup

sed -i 's/1.60/%version/' memcache.py

%build
%pyproject_build

%install
%pyproject_install

%files
%doc ChangeLog PKG-INFO test-requirements.txt README.md
%python3_sitelibdir/memcache.py
%python3_sitelibdir/__pycache__/
%python3_sitelibdir/python_memcached-%version.dist-info


%changelog
* Thu May 16 2024 Grigory Ustinov <grenka@altlinux.org> 1.62-alt1
- Build new version.

* Mon Apr 25 2022 Grigory Ustinov <grenka@altlinux.org> 1.59-alt1
- Build new version.

* Thu Jul 22 2021 Grigory Ustinov <grenka@altlinux.org> 1.58-alt2
- Drop python2 support.

* Tue Jan 17 2017 Igor Vlasenko <viy@altlinux.ru> 1.58-alt1
- automated PyPI update

* Tue Apr 12 2016 Alexey Shabalin <shaba@altlinux.ru> 1.57-alt1
- 1.57

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.53-alt3.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Tue Feb 17 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.53-alt3
- Added provides: memcache

* Fri Aug 22 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.53-alt2
- Added module for Python 3

* Mon Sep 23 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.53-alt1
- Version 1.53

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.45-alt1.1
- Rebuild with Python-2.7

* Tue Dec 01 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.45-alt1
- Version 1.45 (ALT #17271)

* Sat Nov 21 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.2-alt2.tummy5.2
- Rebuilt with python 2.6

* Thu Jan 31 2008 Grigory Batalov <bga@altlinux.ru> 1.2-alt2.tummy5.1
- Rebuilt with python-2.5.

* Thu Jan 31 2008 Grigory Batalov <bga@altlinux.ru> 1.2-alt2.tummy5
- Build as noarch.

* Mon Nov 14 2005 LAKostis <lakostis at altlinux.ru> 1.2-alt1.tummy5
- First build for Sisyphus.

