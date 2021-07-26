%define _unpackaged_files_terminate_build 1
%define oname redis_structures

Name: python3-module-%oname
Version: 0.1.6
Release: alt3
Summary: Redis data structures wrapped with Python 3
License: MIT
Group: Development/Python3
BuildArch: noarch
Url: https://pypi.python.org/pypi/redis_structures/

# https://github.com/jaredlunde/redis_structures.git
Source: %oname-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-redis-py python3-module-ujson
BuildRequires: python3-module-pip python-tools-2to3
BuildRequires: python3-module-html5lib python3-module-pytest

%py3_provides %oname
%py3_requires redis ujson

%description
Pythonic data structures backed by Redis.

%prep
%setup -n %{oname}-%{version}

%build
2to3 -w -n %oname/__init__.py
%python3_build

%install
%python3_install

%check
python3 setup.py test

%files
%python3_sitelibdir/*

%changelog
* Mon Jul 26 2021 Grigory Ustinov <grenka@altlinux.org> 0.1.6-alt3
- Drop python2 support.

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 0.1.6-alt2.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Wed Dec 27 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 0.1.6-alt2
- Fixed build.

* Wed Jan 11 2017 Igor Vlasenko <viy@altlinux.ru> 0.1.6-alt1
- automated PyPI update

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.0.1-alt1.a0.git20150318.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 0.0.1-alt1.a0.git20150318.1
- NMU: Use buildreq for BR.

* Thu Mar 19 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.0.1-alt1.a0.git20150318
- Initial build for Sisyphus

