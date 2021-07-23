%define oname grapy

Name: python3-module-%oname
Version: 0.1.8
Release: alt2

Summary: Fast high-level web crawling framework for Python 3.3 or later base on asyncio

License: Free
Group: Development/Python3
Url: https://pypi.python.org/pypi/grapy/

# https://github.com/Lupino/grapy.git
# Source-url: https://pypi.io/packages/source/g/%oname/%oname-%version.tar.gz
Source: %name-%version.tar

BuildArch: noarch

BuildRequires(pre): rpm-build-python3
BuildRequires: python3(asyncio) python3-module-aiohttp
BuildRequires: python3-module-BeautifulSoup4 python3-module-requests

%py3_provides %oname
%py3_requires asyncio aiohttp bs4 requests

%description
Grapy, a fast high-level screen scraping and web crawling framework for
Python 3.3 or later base on asyncio.

%prep
%setup
subst "s|self.async|self.fasync|" grapy/core/request.py

# don't explicitely require asyncio module, it's part of python3 base now
#sed -i \
#	-e "s|'asyncio', ||g" \
#	setup.py

%build
%python3_build

%install
%python3_install

%check
python3 setup.py test

%files
%doc *.md docs/*.rst
%python3_sitelibdir/*

%changelog
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

