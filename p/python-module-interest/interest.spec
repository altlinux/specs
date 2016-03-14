%define oname interest

%def_without python2
%def_with python3

Name: python-module-%oname
Version: 0.4.1
Release: alt1.git20150216.1
Summary: Interest is a web framework on top of asyncio and aiohttp
License: MIT
Group: Development/Python
Url: https://pypi.python.org/pypi/interest/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/interest-hub/interest.git
Source: %name-%version.tar
BuildArch: noarch

%if_with python2
BuildPreReq: python-devel python-module-setuptools-tests
BuildPreReq: python-module-asyncio python-module-aiohttp
BuildPreReq: python-module-nose python-module-coverage
BuildPreReq: python-module-mario python-module-runfile
BuildPreReq: python-module-pathlib
%endif
BuildPreReq: python-module-sphinx-devel python3-module-sphinx
BuildPreReq: python3-module-sphinx_rtd_theme
BuildPreReq: python3-module-sphinx-settings
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools-tests
BuildPreReq: python3-module-asyncio python3-module-aiohttp
BuildPreReq: python3-module-nose python3-module-coverage
BuildPreReq: python3-module-mario python3-module-runfile
BuildPreReq: python3-module-pathlib
%endif

%py_provides %oname
%py_requires asyncio aiohttp mario

%description
Interest is a web framework on top of asyncio and aiohttp.

%package -n python3-module-%oname
Summary: Interest is a web framework on top of asyncio and aiohttp
Group: Development/Python3
%py3_provides %oname
%py3_requires asyncio aiohttp mario

%description -n python3-module-%oname
Interest is a web framework on top of asyncio and aiohttp.

%prep
%setup

%if_with python3
cp -fR . ../python3
%endif

%prepare_sphinx .
ln -s ../objects.inv docs/

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

export PYTHONPATH=$PWD
pushd docs
py3_sphinx-build -b html -d _build/doctrees . _build/html
popd

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
%doc *.rst bench demo docs/_build/html
%python_sitelibdir/*
%endif

%if_with python3
%files -n python3-module-%oname
%doc *.rst bench demo docs/_build/html
%python3_sitelibdir/*
%endif

%changelog
* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.4.1-alt1.git20150216.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Mon Feb 16 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.4.1-alt1.git20150216
- Version 0.4.1

* Mon Jan 26 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.2.0-alt1.git20150125
- Initial build for Sisyphus

