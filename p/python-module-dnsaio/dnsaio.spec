%define oname dnsaio

%def_without python2
%def_with python3

Name: python-module-%oname
Version: 0.1.0
Release: alt1.git20140722.1.1
Summary: Asyncio wrapper around dnspython3
License: BSD
Group: Development/Python
Url: https://pypi.python.org/pypi/dnsaio/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/dzen/dnsaio.git
Source: %name-%version.tar
BuildArch: noarch

%if_with python2
#BuildPreReq: python-devel python-module-setuptools-tests
#BuildPreReq: python-module-asyncio python-module-dns
%endif
%if_with python3
BuildRequires(pre): rpm-build-python3
#BuildPreReq: python3-devel python3-module-setuptools-tests
#BuildPreReq: python3-module-asyncio python3-module-dns
%endif

%py_provides %oname
%py_requires asyncio dns

# Automatically added by buildreq on Thu Jan 28 2016 (-bi)
# optimized out: python-base python3 python3-base python3-module-pytest python3-module-setuptools
BuildRequires: python3-module-dns python3-module-setuptools-tests rpm-build-python3

%description
Python3 implementation of an asynchronous dns client using dnspython3
and asyncio.

%package -n python3-module-%oname
Summary: Asyncio wrapper around dnspython3
Group: Development/Python3
%py3_provides %oname
%py3_requires asyncio dns

%description -n python3-module-%oname
Python3 implementation of an asynchronous dns client using dnspython3
and asyncio.

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
%doc README.* examples
%python_sitelibdir/*
%endif

%if_with python3
%files -n python3-module-%oname
%doc README.* examples
%python3_sitelibdir/*
%endif

%changelog
* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.1.0-alt1.git20140722.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 0.1.0-alt1.git20140722.1
- NMU: Use buildreq for BR.

* Sat Jan 10 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1.0-alt1.git20140722
- Initial build for Sisyphus

