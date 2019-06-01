%define oname grapy

%def_without python2
%def_with python3

Name: python-module-%oname
Version: 0.1.8
Release: alt1

Summary: Fast high-level web crawling framework for Python 3.3 or later base on asyncio

License: Free
Group: Development/Python
Url: https://pypi.python.org/pypi/grapy/

# https://github.com/Lupino/grapy.git
# Source-url: https://pypi.io/packages/source/g/%oname/%oname-%version.tar.gz
Source: %name-%version.tar

BuildArch: noarch

%if_with python2
BuildRequires: python-devel python-module-setuptools
BuildRequires: python2.7(asyncio) python-module-aiohttp
BuildRequires: python-module-BeautifulSoup4 python-module-requests
%endif
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel python3-module-setuptools
BuildRequires: python3(asyncio) python3-module-aiohttp
BuildRequires: python3-module-BeautifulSoup4 python3-module-requests
%endif

%py_provides %oname
%py_requires asyncio aiohttp bs4 requests

%description
Grapy, a fast high-level screen scraping and web crawling framework for
Python 3.3 or later base on asyncio.

%package -n python3-module-%oname
Summary: Fast high-level web crawling framework for Python 3.3 or later base on asyncio
Group: Development/Python3
%py3_provides %oname
%py3_requires asyncio aiohttp bs4 requests

%description -n python3-module-%oname
Grapy, a fast high-level screen scraping and web crawling framework for
Python 3.3 or later base on asyncio.

%prep
%setup
subst "s|self.async|self.fasync|" grapy/core/request.py

# don't explicitely require asyncio module, it's part of python3 base now
#sed -i \
#	-e "s|'asyncio', ||g" \
#	setup.py

%if_with python3
cp -fR . ../python3
%endif

%build
%if_with python2
%python_build_debug
%endif

%if_with python3
pushd ../python3
%python3_build_debug
popd
%endif

%install
%if_with python2
%python_install
%endif

%if_with python3
pushd ../python3
%python3_install
popd
%endif

%check
%if_with python2
python setup.py test
%endif
%if_with python3
pushd ../python3
python3 setup.py test
popd
%endif

%if_with python2
%files
%doc *.md docs/*.rst
%python_sitelibdir/*
%endif

%if_with python3
%files -n python3-module-%oname
%doc *.md docs/*.rst
%python3_sitelibdir/*
%endif

%changelog
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

