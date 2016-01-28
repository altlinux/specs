%define oname asyncio_amp

%def_without python2
%def_with python3

Name: python-module-%oname
Version: 0.1
Release: alt1.git20140129.1
Summary: AMP client and server library for asyncio
License: BSD
Group: Development/Python
Url: https://github.com/jonathanslenders/asyncio-amp
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/jonathanslenders/asyncio-amp.git
Source: %name-%version.tar
BuildArch: noarch

%if_with python2
#BuildPreReq: python-devel python-module-setuptools-tests
#BuildPreReq: python-module-asyncio
%endif
%if_with python3
BuildRequires(pre): rpm-build-python3
#BuildPreReq: python3-devel python3-module-setuptools-tests
#BuildPreReq: python3-module-asyncio
%endif

%py_provides %oname
%py_requires asyncio

# Automatically added by buildreq on Wed Jan 27 2016 (-bi)
# optimized out: python-base python3 python3-base python3-module-pytest python3-module-setuptools
BuildRequires: python3-module-asyncio python3-module-setuptools-tests rpm-build-python3

%description
AMP client and server library for asyncio.

AMP, short for asynchronous messaging protocol, is a protocol for
asynchronous interprocess communication. You can call exposed functions
in another process and receive the answer when it's ready.

%package -n python3-module-%oname
Summary: AMP client and server library for asyncio
Group: Development/Python3
%py3_provides %oname
%py3_requires asyncio

%description -n python3-module-%oname
AMP client and server library for asyncio.

AMP, short for asynchronous messaging protocol, is a protocol for
asynchronous interprocess communication. You can call exposed functions
in another process and receive the answer when it's ready.

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
python tests.py -v
%endif
%if_with python3
pushd ../python3
python3 setup.py test
python3 tests.py -v
popd
%endif

%if_with python2
%files
%doc *.txt *.rst examples
%python_sitelibdir/*
%endif

%if_with python3
%files -n python3-module-%oname
%doc *.txt *.rst examples
%python3_sitelibdir/*
%endif

%changelog
* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 0.1-alt1.git20140129.1
- NMU: Use buildreq for BR.

* Sat Jan 17 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1-alt1.git20140129
- Initial build for Sisyphus

