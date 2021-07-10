%define oname repoze.lru

Name: python3-module-%oname
Version: 0.7
Release: alt1

Summary: Tiny LRU cache

License: BSD
Group: Development/Python3
Url: https://github.com/repoze/repoze.lru

# Source-url: %__pypi_url %oname
Source: %name-%version.tar

BuildArch: noarch

BuildRequires(pre): rpm-build-intro >= 2.2.5
BuildRequires(pre): rpm-build-python3

BuildRequires: python3-module-setuptools

%py3_requires repoze

%description
``repoze.lru`` is a LRU (least recently used) cache implementation.
Keys and values that are not used frequently will be evicted from the
cache faster than keys and values that are used frequently.

%prep
%setup

%build
%python3_build

%install
%python3_install
%python3_prune
rm -fv %buildroot%python3_sitelibdir/*.pth

%files
%doc *.txt
%python3_sitelibdir/*

%changelog
* Sun Jul 11 2021 Vitaly Lipatov <lav@altlinux.ru> 0.7-alt1
- build python3 module separately

* Tue Apr 30 2019 Grigory Ustinov <grenka@altlinux.org> 0.6-alt2.git20140202.2
- Rebuild with python3.7.

* Mon Jun 06 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.6-alt2.git20140202.1.1.1
- (AUTO) subst_x86_64.

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.6-alt2.git20140202.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 0.6-alt2.git20140202.1
- NMU: Use buildreq for BR.

* Fri Jan 02 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.6-alt2.git20140202
- Fixed version

* Tue Jul 15 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.6-alt1.git20140202
- New snapshot

* Tue Sep 24 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.6-alt1.git20130722
- New snapshot

* Sat Mar 02 2013 Aleksey Avdeev <solo@altlinux.ru> 0.6-alt1
- Version 0.6

* Sat May 05 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.5-alt1.git20120324
- Version 0.5
- Added module for Python 3

* Mon Dec 12 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.4-alt1.git20110904
- Version 0.4

* Mon Oct 24 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.3-alt1.git20110225.1.1
- Rebuild with Python-2.7

* Thu Jun 30 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.3-alt1.git20110225.1
- Excluded *.pth

* Fri Jun 10 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.3-alt1.git20110225
- Initial build for Sisyphus

