%define oname aiobottle

%def_without python2
%def_with python3
%def_without check

Name: python-module-%oname
Version: 0.1.1
Release: alt2.git20140523
Summary: A warper bottle use aiohttp base on Asyncio (PEP-3156) 
License: Free
Group: Development/Python
Url: https://pypi.python.org/pypi/aiobottle

# https://github.com/Lupino/aiobottle.git
Source: %name-%version.tar
BuildArch: noarch

%if_with python2
BuildRequires: python-dev python-module-setuptools-tests
BuildRequires: python2.7(asyncio) python2.7(aiohttp) python2.7(bottle)
%endif
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-dev python3-module-setuptools-tests
BuildRequires: python3(asyncio) python3(aiohttp) python3(bottle)
%endif

%py_provides %oname

%description
Aiobottle, a warper bottle use aiohttp base on Asyncio (PEP-3156).

%package -n python3-module-%oname
Summary: A warper bottle use aiohttp base on Asyncio (PEP-3156)
Group: Development/Python3
%py3_provides %oname

%description -n python3-module-%oname
Aiobottle, a warper bottle use aiohttp base on Asyncio (PEP-3156).

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
%doc *.md example.py
%python_sitelibdir/*
%endif

%if_with python3
%files -n python3-module-%oname
%doc *.md example.py
%python3_sitelibdir/*
%endif

%changelog
* Mon Oct 16 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 0.1.1-alt2.git20140523
- Updated build and runtime dependencies.

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.1.1-alt1.git20140523.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Wed Jan 27 2016 Mikhail Efremov <sem@altlinux.org> 0.1.1-alt1.git20140523.1
- NMU: Use buildreq for BR.

* Thu Nov 27 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1.1-alt1.git20140523
- Initial build for Sisyphus

