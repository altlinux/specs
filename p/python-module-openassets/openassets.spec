%define oname openassets

%def_without python2
%def_with python3

Name: python-module-%oname
Version: 1.3
Release: alt1.git20141102.1
Summary: Reference implementation of the Open Assets Protocol
License: MIT
Group: Development/Python
Url: https://pypi.python.org/pypi/openassets/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/OpenAssets/openassets.git
Source: %name-%version.tar
BuildArch: noarch

%if_with python2
#BuildPreReq: python-devel python-module-setuptools-tests
#BuildPreReq: python-module-asyncio python-module-bitcoinlib
#BuildPreReq: python-module-enum34
%endif
%if_with python3
BuildRequires(pre): rpm-build-python3
#BuildPreReq: python3-devel python3-module-setuptools-tests
#BuildPreReq: python3-module-asyncio python3-module-bitcoinlib
#BuildPreReq: python3-module-enum34
%endif

%py_provides %oname
Requires: python-module-bitcoinlib
Requires: python-module-enum34
%py_requires asyncio

# Automatically added by buildreq on Thu Jan 28 2016 (-bi)
# optimized out: python-base python3 python3-base python3-module-pytest python3-module-setuptools
BuildRequires: python3-module-asyncio python3-module-bitcoinlib python3-module-enum34 python3-module-setuptools-tests rpm-build-python3

%description
The openassets Python package is the reference implementation of the
colored coins Open Assets Protocol.

Open Assets is a protocol for issuing and transferring custom digital
tokens in a secure way on the Bitcoin blockchain (or any compatible
blockchain).

%package -n python3-module-%oname
Summary: Reference implementation of the Open Assets Protocol
Group: Development/Python3
%py3_provides %oname
Requires: python3-module-bitcoinlib
Requires: python3-module-enum34
%py3_requires asyncio

%description -n python3-module-%oname
The openassets Python package is the reference implementation of the
colored coins Open Assets Protocol.

Open Assets is a protocol for issuing and transferring custom digital
tokens in a secure way on the Bitcoin blockchain (or any compatible
blockchain).

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
* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 1.3-alt1.git20141102.1
- NMU: Use buildreq for BR.

* Sat Jan 17 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.3-alt1.git20141102
- Initial build for Sisyphus

