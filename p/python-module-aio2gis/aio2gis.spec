%define oname aio2gis

%def_without python2
%def_with python3

Name: python-module-%oname
Version: 0.0.1
Release: alt1.git20140623.1.1.1
Summary: asyncio-powered 2gis library for Python
License: BSD
Group: Development/Python
Url: https://pypi.python.org/pypi/aio2gis/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/svartalf/python-aio2gis.git
Source: %name-%version.tar
BuildArch: noarch

%if_with python2
#BuildPreReq: python-devel python-module-setuptools
#BuildPreReq: python-module-asyncio python-module-aiohttp
%endif
%if_with python3
BuildRequires(pre): rpm-build-python3
#BuildPreReq: python3-devel python3-module-setuptools
#BuildPreReq: python3-module-asyncio python3-module-aiohttp
%endif

%py_provides %oname
%py_requires asyncio aiohttp

# Automatically added by buildreq on Wed Jan 27 2016 (-bi)
# optimized out: python-base python3 python3-base python3-module-cffi python3-module-chardet python3-module-cryptography python3-module-django python3-module-dns python3-module-enum34 python3-module-greenlet python3-module-gunicorn python3-module-paste python3-module-psycopg2 python3-module-pycares python3-module-pycparser python3-module-pytest python3-module-setuptools python3-module-yaml python3-module-zope python3-module-zope.interface
BuildRequires: python3-module-aiohttp python3-module-setuptools rpm-build-python3
BuildRequires: python3-module-chardet

%description
A Python library for accessing the 2gis API (http://api.2gis.ru)
powered with asyncio.

%package -n python3-module-%oname
Summary: asyncio-powered 2gis library for Python
Group: Development/Python3
%py3_provides %oname
%py3_requires asyncio aiohttp

%description -n python3-module-%oname
A Python library for accessing the 2gis API (http://api.2gis.ru)
powered with asyncio.

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
%doc *.md examples
%python_sitelibdir/*
%endif

%if_with python3
%files -n python3-module-%oname
%doc *.md examples
%python3_sitelibdir/*
%endif

%changelog
* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 0.0.1-alt1.git20140623.1.1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.0.1-alt1.git20140623.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Wed Jan 27 2016 Mikhail Efremov <sem@altlinux.org> 0.0.1-alt1.git20140623.1
- NMU: Use buildreq for BR.

* Thu Jan 08 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.0.1-alt1.git20140623
- Initial build for Sisyphus

