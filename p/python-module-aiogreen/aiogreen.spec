%define oname aiogreen

%def_with python3
%def_disable check

Name: python-module-%oname
Version: 0.3
Release: alt3.1.1
Summary: asyncio event loop scheduling callbacks in eventlet
License: ASLv2.0
Group: Development/Python
Url: https://pypi.python.org/pypi/aiogreen
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar
BuildArch: noarch

#BuildPreReq: python-devel python-module-setuptools-tests
#BuildPreReq: python-module-eventlet python-module-futures
#BuildPreReq: python-module-trollius python-module-greenlet
#BuildPreReq: python-module-mock
%if_with python3
BuildRequires(pre): rpm-build-python3
#BuildPreReq: python3-devel python3-module-setuptools-tests
#BuildPreReq: python3-module-eventlet python3-module-greenlet
#BuildPreReq: python3-module-asyncio python3-module-mock
%endif

%py_provides %oname
%py_requires trollius

# Automatically added by buildreq on Wed Jan 27 2016 (-bi)
# optimized out: python-base python-devel python-module-cffi python-module-enum34 python-module-pyasn1 python-module-setuptools python-modules python-modules-compiler python-modules-ctypes python-modules-email python-modules-encodings python-modules-json python-modules-unittest python3 python3-base python3-module-cffi python3-module-cryptography python3-module-cssselect python3-module-enum34 python3-module-genshi python3-module-ntlm python3-module-pip python3-module-pycparser python3-module-setuptools
BuildRequires: python-module-cryptography python-module-dns python-module-greenlet python-module-pbr python-module-psycopg2 python-module-pytest python-module-unittest2 python3-module-dns python3-module-greenlet python3-module-html5lib python3-module-pbr python3-module-psycopg2 python3-module-pytest python3-module-unittest2 rpm-build-python3

%description
asyncio event loop scheduling callbacks in eventlet.

%package -n python3-module-%oname
Summary: asyncio event loop scheduling callbacks in eventlet
Group: Development/Python3
%py3_provides %oname
%py3_requires asyncio

%description -n python3-module-%oname
asyncio event loop scheduling callbacks in eventlet.

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
py.test -vv
%if_with python3
pushd ../python3
python3 setup.py test
py.test-%_python3_version -vv
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
* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.3-alt3.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 0.3-alt3.1
- NMU: Use buildreq for BR.

* Tue Apr 21 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.3-alt3
- Disabled tests

* Mon Mar 02 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.3-alt2
- Disabled tests for Python 2

* Mon Nov 24 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.3-alt1
- Version 0.3

* Fri Nov 21 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.2-alt1
- Version 0.2

* Wed Nov 19 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1-alt1
- Initial build for Sisyphus

