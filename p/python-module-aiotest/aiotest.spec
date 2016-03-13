%define oname aiotest

%def_with python3

Name: python-module-%oname
Version: 0.3
Release: alt1.hg20141227.1.1
Summary: Test suite to validate an implementation of the asyncio API, the PEP 3156
License: ASLv2.0
Group: Development/Python
Url: https://pypi.python.org/pypi/aiotest/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar
BuildArch: noarch

#BuildPreReq: python-devel python-module-setuptools-tests
#BuildPreReq: python-module-trollius python-module-mock
%if_with python3
BuildRequires(pre): rpm-build-python3
#BuildPreReq: python3-devel python3-module-setuptools-tests
#BuildPreReq: python3-module-asyncio python3-module-mock
%endif

%py_provides %oname
%py_requires trollius

# Automatically added by buildreq on Wed Jan 27 2016 (-bi)
# optimized out: python-base python-devel python-module-funcsigs python-module-futures python-module-linecache2 python-module-pbr python-module-pytest python-module-setuptools python-module-six python-module-traceback2 python-module-unittest2 python-modules python-modules-compiler python-modules-ctypes python-modules-email python-modules-encodings python-modules-json python-modules-logging python-modules-multiprocessing python-modules-unittest python3 python3-base python3-module-cffi python3-module-cryptography python3-module-cssselect python3-module-enum34 python3-module-genshi python3-module-linecache2 python3-module-ntlm python3-module-pip python3-module-pycparser python3-module-pytest python3-module-setuptools python3-module-six python3-module-traceback2
BuildRequires: python-module-mock python-module-setuptools-tests python-module-trollius python3-module-asyncio python3-module-html5lib python3-module-pbr python3-module-setuptools-tests python3-module-unittest2 rpm-build-python3

%description
aiotest is a test suite to validate an implementation of the asyncio
API, the PEP 3156.

%package -n python3-module-%oname
Summary: Test suite to validate an implementation of the asyncio API, the PEP 3156
Group: Development/Python3
%py3_provides %oname
%py3_requires asyncio

%description -n python3-module-%oname
aiotest is a test suite to validate an implementation of the asyncio
API, the PEP 3156.

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
./test_trollius.py
%if_with python3
pushd ../python3
python3 setup.py test
./test_asyncio.py
popd
%endif

%files
%doc README
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%oname
%doc README
%python3_sitelibdir/*
%endif

%changelog
* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.3-alt1.hg20141227.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 0.3-alt1.hg20141227.1
- NMU: Use buildreq for BR.

* Mon Apr 27 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.3-alt1.hg20141227
- Version 0.3

* Mon Mar 02 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.2-alt2
- Fixed build

* Mon Jan 05 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.2-alt1
- Initial build for Sisyphus

