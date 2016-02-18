%define oname MimiProxy

%def_without python2
%def_with python3
%def_disable check

Name: python-module-%oname
Version: 0.0.5
Release: alt1.git20140416.1
Summary: Small SOCKS5 proxy server on python3 and asyncio
License: MIT
Group: Development/Python
Url: https://pypi.python.org/pypi/MimiProxy/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/AyumuKasuga/MimiProxy.git
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
# optimized out: python-base python3 python3-base
BuildRequires: rpm-build-python3

%description
Small SOCKS5 proxy server on python3 and asyncio.

Use:

proxy.py 0.0.0.0 1080

%package -n python3-module-%oname
Summary: Small SOCKS5 proxy server on python3 and asyncio
Group: Development/Python3
Provides: proxy.py
%py3_provides %oname
%py3_requires asyncio

%description -n python3-module-%oname
Small SOCKS5 proxy server on python3 and asyncio.

Use:

proxy.py 0.0.0.0 1080

%prep
%setup

%if_with python3
cp -fR . ../python3
sed -i 's|@PYVER@|3|' ../python3/%oname/proxy.py
%endif

sed -i 's|@PYVER@||' %oname/proxy.py

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
install -d %buildroot%_bindir
ln -s %python3_sitelibdir/%oname/proxy.py %buildroot%_bindir/
chmod +x %buildroot%python3_sitelibdir/%oname/proxy.py
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
%doc *.md
%python_sitelibdir/*
%endif

%if_with python3
%files -n python3-module-%oname
%doc *.md
%_bindir/proxy.py
%python3_sitelibdir/*
%endif

%changelog
* Wed Jan 27 2016 Mikhail Efremov <sem@altlinux.org> 0.0.5-alt1.git20140416.1
- NMU: Use buildreq for BR.

* Tue Jan 13 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.0.5-alt1.git20140416
- Initial build for Sisyphus

