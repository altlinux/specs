%define oname koa

%def_without python2
%def_with python3

Name: python-module-%oname
Version: 0.3
Release: alt1.git20141111
Summary: koa.js port to Python asyncio
License: MIT
Group: Development/Python
Url: https://pypi.python.org/pypi/koa/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/KjellSchubert/koa.git
Source: %name-%version.tar
BuildArch: noarch

%if_with python2
BuildPreReq: python-devel python-module-setuptools-tests
BuildPreReq: python-module-aiohttp python-module-coverage
BuildPreReq: python-module-coveralls
%endif
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools-tests
BuildPreReq: python3-module-aiohttp python3-module-coverage
BuildPreReq: python3-module-coveralls
%endif

%py_provides %oname

%description
Koa.js web framework port for asyncio + aiohttp.

%package -n python3-module-%oname
Summary: koa.js port to Python asyncio
Group: Development/Python3
%py3_provides %oname

%description -n python3-module-%oname
Koa.js web framework port for asyncio + aiohttp.

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
rm -f setup.cfg
export PYTHONPATH=$PWD
py.test
%endif
%if_with python3
pushd ../python3
rm -f setup.cfg
export PYTHONPATH=$PWD
py.test-%_python3_version
popd
%endif

%if_with python2
%files
%doc *.md example*
%python_sitelibdir/*
%endif

%if_with python3
%files -n python3-module-%oname
%doc *.md example*
%python3_sitelibdir/*
%endif

%changelog
* Fri Nov 28 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.3-alt1.git20141111
- Initial build for Sisyphus

