%define oname induction

%def_without python2
%def_with python3

Name: python-module-%oname
Version: 0.2
Release: alt1.git20140925.1
Summary: A simple web framework based on asyncio
License: BSD
Group: Development/Python
Url: https://pypi.python.org/pypi/induction/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/brutasse/induction.git
Source: %name-%version.tar
BuildArch: noarch

%if_with python2
#BuildPreReq: python-devel python-module-setuptools-tests
#BuildPreReq: python-module-asyncio python-module-jinja2
#BuildPreReq: python-module-routes python-module-aiohttp
%endif
%if_with python3
BuildRequires(pre): rpm-build-python3
#BuildPreReq: python3-devel python3-module-setuptools-tests
#BuildPreReq: python3-module-asyncio python3-module-jinja2
#BuildPreReq: python3-module-routes python3-module-aiohttp
%endif

%py_provides %oname
%py_requires asyncio jinja2 routes aiohttp

# Automatically added by buildreq on Thu Jan 28 2016 (-bi)
# optimized out: python-base python3 python3-base python3-module-asyncio python3-module-cffi python3-module-chardet python3-module-cryptography python3-module-django python3-module-dns python3-module-enum34 python3-module-greenlet python3-module-gunicorn python3-module-jinja2 python3-module-markupsafe python3-module-paste python3-module-psycopg2 python3-module-pycares python3-module-pycparser python3-module-pytest python3-module-repoze python3-module-repoze.lru python3-module-setuptools python3-module-yaml python3-module-zope python3-module-zope.interface
BuildRequires: python3-module-aiohttp python3-module-jinja2-tests python3-module-routes python3-module-setuptools-tests rpm-build-python3

%description
A simple web framework based on asyncio.

%package -n python3-module-%oname
Summary: A simple web framework based on asyncio
Group: Development/Python3
%py3_provides %oname
%py3_requires asyncio jinja2 routes aiohttp

%description -n python3-module-%oname
A simple web framework based on asyncio.

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
%doc *.rst
%python_sitelibdir/*
%endif

%if_with python3
%files -n python3-module-%oname
%doc *.rst
%python3_sitelibdir/*
%endif

%changelog
* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 0.2-alt1.git20140925.1
- NMU: Use buildreq for BR.

* Sun Jan 11 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.2-alt1.git20140925
- Initial build for Sisyphus

