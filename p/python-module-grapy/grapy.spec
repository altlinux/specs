%define oname grapy

%def_without python2
%def_with python3

Name: python-module-%oname
Version: 0.1.6
Release: alt1.git20141223.1
Summary: Fast high-level web crawling framework for Python 3.3 or later base on asyncio
License: Free
Group: Development/Python
Url: https://pypi.python.org/pypi/grapy/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/Lupino/grapy.git
Source: %name-%version.tar
BuildArch: noarch

%if_with python2
#BuildPreReq: python-devel python-module-setuptools-tests
#BuildPreReq: python-module-asyncio python-module-aiohttp
#BuildPreReq: python-module-BeautifulSoup4 python-module-requests
%endif
%if_with python3
BuildRequires(pre): rpm-build-python3
#BuildPreReq: python3-devel python3-module-setuptools-tests
#BuildPreReq: python3-module-asyncio python3-module-aiohttp
#BuildPreReq: python3-module-BeautifulSoup4 python3-module-requests
%endif

%py_provides %oname
%py_requires asyncio aiohttp bs4 requests

# Automatically added by buildreq on Thu Jan 28 2016 (-bi)
# optimized out: python-base python3 python3-base python3-module-cffi python3-module-chardet python3-module-cryptography python3-module-cssselect python3-module-django python3-module-dns python3-module-enum34 python3-module-genshi python3-module-greenlet python3-module-gunicorn python3-module-html5lib python3-module-ndg-httpsclient python3-module-ntlm python3-module-paste python3-module-psycopg2 python3-module-pycares python3-module-pycparser python3-module-pytest python3-module-setuptools python3-module-urllib3 python3-module-yaml python3-module-zope python3-module-zope.interface
BuildRequires: python3-module-BeautifulSoup4 python3-module-aiohttp python3-module-requests python3-module-setuptools-tests rpm-build-python3

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
* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 0.1.6-alt1.git20141223.1
- NMU: Use buildreq for BR.

* Wed Jan 07 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1.6-alt1.git20141223
- Initial build for Sisyphus

