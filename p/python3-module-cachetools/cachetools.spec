%define oname cachetools

Name:       python3-module-%oname
Version:    3.1.1
Release:    alt2

Summary:    Extensible memoizing collections and decorators
License:    MIT
Group:      Development/Python3
Url:        https://pypi.python.org/pypi/cachetools/

BuildArch:  noarch

#           https://github.com/tkem/cachetools.git
Source:     %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-nose

%py3_provides %oname


%description
This module provides various memoizing collections and decorators,
including a variant of the Python 3 Standard Library @lru_cache function
decorator.

%prep
%setup

%build
%python3_build_debug

%install
%python3_install

%check
%__python3 setup.py test

%files
%doc *.rst docs/*.rst
%python3_sitelibdir/*


%changelog
* Thu Feb 06 2020 Andrey Bychkov <mrdrew@altlinux.org> 3.1.1-alt2
- Build for python2 disabled.

* Mon Oct 21 2019 Grigory Ustinov <grenka@altlinux.org> 3.1.1-alt1
- Build new version.

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 2.0.0-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Mon Oct 17 2016 Alexey Shabalin <shaba@altlinux.ru> 2.0.0-alt1
- 2.0.0

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.0.0-alt1.git20141230.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Feb 05 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.0-alt1.git20141230
- Initial build for Sisyphus

