%define oname greenio

%def_with python3

Name: python-module-%oname
Version: 0.6.0
Release: alt1.git20141105
Summary: Greenlets for asyncio (PEP 3156)
License: ASLv2.0
Group: Development/Python
Url: https://pypi.python.org/pypi/greenio/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/1st1/greenio.git
Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools-tests
BuildPreReq: python-module-argparse python-module-greenlet
BuildPreReq: python-module-trollius
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools-tests
BuildPreReq: python3-module-argparse python3-module-greenlet
BuildPreReq: python3-module-asyncio
%endif

%py_provides %oname
%py_requires greenlet trollius

%description
Greenlets support for asyncio (PEP 3156).

%package -n python3-module-%oname
Summary: Greenlets for asyncio (PEP 3156)
Group: Development/Python3
%py3_provides %oname
%py3_requires greenlet asyncio

%description -n python3-module-%oname
Greenlets support for asyncio (PEP 3156).

%prep
%setup

%if_with python3
cp -fR . ../python3
%endif

%build
%python_build_debug

%if_with python3
pushd ../python3
%python3_build_debug
popd
%endif

%install
%python_install

%if_with python3
pushd ../python3
%python3_install
popd
%endif

%check
python setup.py test
#python runtests.py -v
%if_with python3
pushd ../python3
python3 setup.py test
python3 runtests.py -v
popd
%endif

%files
%doc AUTHORS NEWS *.rst examples
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%oname
%doc AUTHORS NEWS *.rst examples
%python3_sitelibdir/*
%endif

%changelog
* Sat Jan 10 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.6.0-alt1.git20141105
- Initial build for Sisyphus

