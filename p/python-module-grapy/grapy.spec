%define oname grapy

%def_without python2
%def_with python3

Name: python-module-%oname
Version: 0.1.6
Release: alt1.git20141223
Summary: Fast high-level web crawling framework for Python 3.3 or later base on asyncio
License: Free
Group: Development/Python
Url: https://pypi.python.org/pypi/grapy/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/Lupino/grapy.git
Source: %name-%version.tar
BuildArch: noarch

%if_with python2
BuildPreReq: python-devel python-module-setuptools-tests
BuildPreReq: python-module-asyncio python-module-aiohttp
BuildPreReq: python-module-BeautifulSoup4 python-module-requests
%endif
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools-tests
BuildPreReq: python3-module-asyncio python3-module-aiohttp
BuildPreReq: python3-module-BeautifulSoup4 python3-module-requests
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
* Wed Jan 07 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1.6-alt1.git20141223
- Initial build for Sisyphus

