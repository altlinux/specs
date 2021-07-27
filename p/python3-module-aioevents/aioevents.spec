%define oname aioevents

%def_disable check

Name: python3-module-%oname
Version: 0.1
Release: alt3.git20140222
Summary: Events for asyncio (PEP 3156)
License: MIT
Group: Development/Python3
BuildArch: noarch
Url: https://pypi.python.org/pypi/aioevents/

# https://github.com/astronouth7303/aioevents.git
Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3

%py3_provides %oname
%py3_requires asyncio

%description
Events for asyncio (PEP 3156).

%prep
%setup

%build
%python3_build

%install
%python3_install

%check
py.test3 -vv

%files
%doc *.md test.py
%python3_sitelibdir/*

%changelog
* Tue Jul 27 2021 Grigory Ustinov <grenka@altlinux.org> 0.1-alt3.git20140222
- Drop python2 support.

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 0.1-alt2.git20140222.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Fri Dec 01 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 0.1-alt2.git20140222
- Fixed build.

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.1-alt1.git20140222.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 0.1-alt1.git20140222.1
- NMU: Use buildreq for BR.

* Sat Jan 10 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1-alt1.git20140222
- Initial build for Sisyphus

