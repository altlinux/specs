%define oname aio_periodic

Name: python3-module-%oname
Version: 0.2.8
Release: alt1
Summary: The periodic task system client for python3 base on asyncio
License: Free
Group: Development/Python3
Url: https://pypi.python.org/pypi/aio_periodic/

# https://github.com/Lupino/python-aio-periodic.git
Source: %name-%version.tar
BuildArch: noarch

BuildRequires(pre): rpm-build-python3

%py3_provides %oname
%py3_requires asyncio

%description
The periodic task system client for python3 base on asyncio.

%prep
%setup

%build
%python3_build_debug

%install
%python3_install

%files
%doc README
%python3_sitelibdir/*

%changelog
* Wed Sep 13 2023 Grigory Ustinov <grenka@altlinux.org> 0.2.8-alt1
- Build new version.

* Thu Jul 22 2021 Grigory Ustinov <grenka@altlinux.org> 0.1.6-alt1.git20141231.2
- Drop python2 support.

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 0.1.6-alt1.git20141231.1.1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.1.6-alt1.git20141231.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Wed Jan 27 2016 Mikhail Efremov <sem@altlinux.org> 0.1.6-alt1.git20141231.1
- NMU: Use buildreq for BR.

* Sun Jan 04 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1.6-alt1.git20141231
- Initial build for Sisyphus

