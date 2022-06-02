%define oname grapy

Name: python3-module-%oname
Version: 0.1.11
Release: alt1

Summary: Fast high-level web crawling framework for Python 3.3 or later base on asyncio

License: Free
Group: Development/Python3
Url: https://pypi.python.org/pypi/grapy

# There are no tags on github=(
# https://github.com/Lupino/grapy.git
Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-aiohttp
BuildRequires: python3-module-BeautifulSoup4
BuildRequires: python3-module-requests

%py3_provides %oname
%py3_requires asyncio aiohttp bs4 requests

BuildArch: noarch

%description
Grapy, a fast high-level screen scraping and web crawling framework for
Python 3.3 or later base on asyncio.

%prep
%setup

%build
%python3_build

%install
%python3_install

%check
# there is no any tests

%files
%doc README
%python3_sitelibdir/%oname
%python3_sitelibdir/%oname-%version-py%_python3_version.egg-info

%changelog
* Thu Jun 02 2022 Grigory Ustinov <grenka@altlinux.org> 0.1.11-alt1
- Build new version.

* Fri Jul 23 2021 Grigory Ustinov <grenka@altlinux.org> 0.1.8-alt2
- Drop python2 support.

* Sat Jun 01 2019 Vitaly Lipatov <lav@altlinux.ru> 0.1.8-alt1
- new version 0.1.8 (with rpmrb script)
- switch to build from tarball

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 0.1.6-alt2.git20141223.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Wed Oct 18 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 0.1.6-alt2.git20141223
- Fixed build.

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.1.6-alt1.git20141223.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 0.1.6-alt1.git20141223.1
- NMU: Use buildreq for BR.

* Wed Jan 07 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1.6-alt1.git20141223
- Initial build for Sisyphus

