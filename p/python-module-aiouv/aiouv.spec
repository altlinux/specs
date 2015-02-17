%define oname aiouv

%def_without python2
%def_with python3

Name: python-module-%oname
Version: 0.0.1
Release: alt1.git20150213
Summary: A PEP-3156 compatible event loop
License: MIT
Group: Development/Python
Url: https://pypi.python.org/pypi/aiouv/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/saghul/aiouv.git
Source: %name-%version.tar
BuildArch: noarch

%if_with python2
BuildPreReq: python-devel python-module-setuptools-tests
BuildPreReq: python-module-asyncio-tests python-module-pyuv
BuildPreReq: python-module-aiotest
%endif
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools-tests
BuildPreReq: python3-module-asyncio-tests python3-module-pyuv
BuildPreReq: python3-module-aiotest
%endif

%py_provides %oname
%py_requires asyncio pyuv

%description
libuv based event loop for asyncio.

%package -n python3-module-%oname
Summary: A PEP-3156 compatible event loop
Group: Development/Python3
%py3_provides %oname
%py3_requires asyncio pyuv

%description -n python3-module-%oname
libuv based event loop for asyncio.

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
%doc *.rst examples
%python_sitelibdir/*
%endif

%if_with python3
%files -n python3-module-%oname
%doc *.rst examples
%python3_sitelibdir/*
%endif

%changelog
* Tue Feb 17 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.0.1-alt1.git20150213
- Initial build for Sisyphus

