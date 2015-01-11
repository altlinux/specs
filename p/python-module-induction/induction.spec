%define oname induction

%def_without python2
%def_with python3

Name: python-module-%oname
Version: 0.2
Release: alt1.git20140925
Summary: A simple web framework based on asyncio
License: BSD
Group: Development/Python
Url: https://pypi.python.org/pypi/induction/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/brutasse/induction.git
Source: %name-%version.tar
BuildArch: noarch

%if_with python2
BuildPreReq: python-devel python-module-setuptools-tests
BuildPreReq: python-module-asyncio python-module-jinja2
BuildPreReq: python-module-routes python-module-aiohttp
%endif
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools-tests
BuildPreReq: python3-module-asyncio python3-module-jinja2
BuildPreReq: python3-module-routes python3-module-aiohttp
%endif

%py_provides %oname
%py_requires asyncio jinja2 routes aiohttp

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
* Sun Jan 11 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.2-alt1.git20140925
- Initial build for Sisyphus

